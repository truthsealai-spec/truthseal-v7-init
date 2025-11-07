import os, time, json, hmac, hashlib, secrets
from typing import Dict, Any, List, Tuple
from datetime import datetime, timezone

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# =========================
# Configuration (read-only)
# =========================
# NOTE: In production load from a secret manager or hardware module; environment is a development fallback only.
BASE_ENDPOINT = os.getenv("METRICS_ENDPOINT_URL", "https://metrics.truthseal.ai")
USERNAME      = os.getenv("METRICS_USERNAME", "truthseal_reporter")
API_KEY       = os.getenv("METRICS_API_KEY",    "REPLACE_WITH_SECRET")        # scope: metrics:write only
HMAC_KEY      = os.getenv("METRICS_HMAC_KEY",   "REPLACE_WITH_SECRET")        # provided by key service
PIN_SHA256    = os.getenv("METRICS_TLS_CERT_SHA256", "")                      # e.g. "AA:BB:CC:...:FF" (server certificate fingerprint)
JOB_NAME      = os.getenv("METRICS_JOB_NAME",   "truthseal_security_reporter")
INSTANCE_ID   = os.getenv("INSTANCE_ID",        os.environ.get("HOSTNAME", "commander-instance-01"))

# If BASE_ENDPOINT already contains /metrics/job/... we will not append; otherwise we will construct a Pushgateway-style path.
def _compute_endpoint(base: str, job: str, instance: str) -> str:
    base = base.rstrip("/")
    if "/metrics/job/" in base:
        return base
    return f"{base}/metrics/job/{job}/instance/{instance}"

FINAL_ENDPOINT = _compute_endpoint(BASE_ENDPOINT, JOB_NAME, INSTANCE_ID)

# Canonical metric allow-list (names only). Keep tight to prevent exfiltration via creative names.
ALLOWED_METRICS = {
    "SLM_Threat_Score_Avg",
    "Security_Policy_Violation_Count",
    "Forbidden_Domain_Count",
    "EVL_Hash_Mismatch_Count",
    "PQC_Decaps_Failure_Rate",
    "Unapproved_Op_Count",
    "Job_Wall_Time_Violation_Count",
    "Security_Level_3_Enforced_Count",
}

# Canonical label allow-list (keys only). Values are length-checked and control characters stripped.
ALLOWED_LABEL_KEYS = {
    "source", "violation_type", "severity", "env", "region",
    "job", "instance"
}

MAX_BATCH_METRICS = 100
MAX_LABEL_LEN = 64
MAX_VALUE_LEN = 256


# =========================
# Transport with TLS pinning
# =========================
class _FingerprintAdapter(HTTPAdapter):
    """HTTP adapter that pins the server certificate fingerprint (SHA-256, colon-separated)."""
    def __init__(self, fingerprint: str, *args, **kwargs):
        self.fingerprint = fingerprint
        super().__init__(*args, **kwargs)

    def init_poolmanager(self, *args, **kwargs):
        if self.fingerprint:
            # urllib3 supports assert_fingerprint (SHA256 in colon-separated hex)
            kwargs["assert_fingerprint"] = self.fingerprint
        return super().init_poolmanager(*args, **kwargs)


# =========================
# Helpers
# =========================
def _utc_now_ms() -> int:
    return int(datetime.now(timezone.utc).timestamp() * 1000)

def _sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def _sanitize_label_value(v: str) -> str:
    v = "".join(ch for ch in str(v) if 32 <= ord(ch) <= 126)  # strip control chars
    return v[:MAX_LABEL_LEN]

def _format_prom_line(metric: str, value: float, labels: Dict[str, str], ts_ms: int) -> str:
    label_str = ",".join([f'{k}="{_sanitize_label_value(v)}"' for k, v in labels.items() if k in ALLOWED_LABEL_KEYS])
    return f'{metric}{{{label_str}}} {float(value)} {ts_ms}\n'


# =========================
# Main transmitter
# =========================
class MetricsTransmitter:
    """
    Hardened transmitter:
      - Transport Layer Security certificate pinning (optional, env).
      - HMAC signature headers per batch (timestamp + nonce + payload).
      - Strict metric and label allow-lists.
      - Bounded retries with jitter, short timeout.
    """
    def __init__(self, endpoint: str, username: str, api_key: str, hmac_key: str, pin_sha256: str = ""):
        self.endpoint = endpoint
        self.session = requests.Session()
        self.session.auth = (username, api_key)
        self.session.verify = True  # system trust store

        retries = Retry(
            total=3,
            backoff_factor=0.4,
            status_forcelist=[500, 502, 503, 504],
            allowed_methods=["POST"]
        )

        adapter = _FingerprintAdapter(pin_sha256)
        adapter.max_retries = retries
        self.session.mount("https://", adapter)
        self.hmac_key = hmac_key.encode("utf-8")

    def _build_payload(self, metrics: List[Dict[str, Any]]) -> Tuple[bytes, Dict[str, str]]:
        # Enforce batch size and filter
        if len(metrics) > MAX_BATCH_METRICS:
            metrics = metrics[:MAX_BATCH_METRICS]

        ts_ms = _utc_now_ms()
        lines: List[str] = []
        for m in metrics:
            name = m.get("name")
            if name not in ALLOWED_METRICS:
                # skip unapproved metrics; do not fail the whole batch
                continue
            val = m.get("value", 0.0)
            try:
                val = float(val)
            except Exception:
                continue  # non-numeric → drop

            labels = dict(m.get("labels", {}))
            labels["job"] = JOB_NAME
            labels["instance"] = INSTANCE_ID

            # keep only allowed label keys; enforce lengths
            labels = {k: _sanitize_label_value(labels[k]) for k in list(labels.keys()) if k in ALLOWED_LABEL_KEYS}

            lines.append(_format_prom_line(name, val, labels, ts_ms))

        payload = "".join(lines).encode("utf-8")
        # Build tamper-evident headers
        nonce = secrets.token_hex(16)
        digest = _sha256_hex(payload)
        msg = f"{ts_ms}|{nonce}|{digest}".encode("utf-8")
        sig = hmac.new(self.hmac_key, msg, hashlib.sha256).hexdigest()

        headers = {
            "Content-Type": "text/plain",
            "X-TS-Timestamp": str(ts_ms),
            "X-TS-Nonce": nonce,
            "X-TS-Batch-SHA256": digest,
            "X-TS-Signature": sig,
            "X-TS-Policy-Version": "ObservabilityAgent-1.0",
        }
        return payload, headers

    def push(self, metrics: List[Dict[str, Any]]) -> bool:
        payload, headers = self._build_payload(metrics)
        if not payload:
            return True  # nothing to send

        try:
            resp = self.session.post(self.endpoint, data=payload, headers=headers, timeout=5)
            if resp.status_code in (200, 202):
                return True
            # Soft failure: caller can increment Transmit_Failure_Warning_Count
            print(f"Transmit_Failure_Warning: status={resp.status_code}, body={resp.text[:128]}")
            return False
        except requests.exceptions.RequestException as e:
            print(f"Transmit_Failure_Warning: transport_error={e}")
            return False


# =========================
# Example usage (development)
# =========================
if __name__ == "__main__":
    tx = MetricsTransmitter(
        endpoint=FINAL_ENDPOINT,
        username=USERNAME,
        api_key=API_KEY,
        hmac_key=HMAC_KEY,
        pin_sha256=PIN_SHA256
    )

    sample = [
        {"name": "SLM_Threat_Score_Avg", "value": 0.12, "labels": {"source": "slm_api", "env": "dev"}},
        {"name": "Security_Policy_Violation_Count", "value": 1, "labels": {"violation_type": "Jailbreak", "severity": "critical"}},
        {"name": "EVL_Hash_Mismatch_Count", "value": 0, "labels": {"severity": "critical"}},
    ]
    ok = tx.push(sample)
    print("pushed=", ok)
