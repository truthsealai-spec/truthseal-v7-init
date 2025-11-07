# Metrics endpoint used by the observer/transmitter.
# Example: https://metrics.truthseal.ai/api/prom/push
METRICS_ENDPOINT=https://metrics.truthseal.ai/api/prom/push

# Basic auth for the metrics endpoint.
METRICS_USERNAME=truthseal_reporter
METRICS_API_KEY=REPLACE_WITH_SECURE_TOKEN

# Hash-based message authentication code (HMAC) secret for payload signing.
METRICS_HMAC_KEY=REPLACE_WITH_RANDOM_32B_SECRET

# TLS certificate pin (SHA-256) for endpoint certificate locking.
METRICS_TLS_CERT_PIN_SHA256=REPLACE_WITH_CERT_PIN_SHA256

# Job labels for Grafana/Prometheus.
METRICS_JOB_NAME=truthseal_security_reporter
INSTANCE_ID=commander-instance-01

# Observer timing (seconds between pushes).
METRICS_REPORT_EVERY_SECONDS=10

# Runtime counters/flags (read-only in prod; useful for local dry-runs).
THREAT_SCORE_AVG=0.0
SECURITY_POLICY_VIOLATION_COUNT=0
SECURITY_LEVEL=2
import os, time
from typing import List, Dict, Any

# Reuse the hardened transmitter
from .metrics_transmitter_v1 import (
    MetricsTransmitter, FINAL_ENDPOINT, USERNAME, API_KEY, HMAC_KEY, PIN_SHA256
)

REPORT_EVERY_SECONDS = int(os.getenv("METRICS_INTERVAL_SECONDS", "10"))

def collect_metrics() -> List[Dict[str, Any]]:
    """
    Minimal collector:
      - threat score average comes from an env var (fallback 0.10)
      - violation count comes from an env var (fallback 0)
      - level-three enforced flag derives from SECURITY_LEVEL env var
    """
    threat_avg = float(os.getenv("THREAT_SCORE_AVG", "0.10"))
    violations = float(os.getenv("SECURITY_POLICY_VIOLATION_COUNT", "0"))
    level = os.getenv("SECURITY_LEVEL", "2")
    enforced = 1.0 if level.strip() == "3" else 0.0

    return [
        {"name": "SLM_Threat_Score_Avg", "value": threat_avg, "labels": {"source": "commander"}},
        {"name": "Security_Policy_Violation_Count", "value": violations, "labels": {"violation_type": "aggregate"}},
        {"name": "Security_Level_3_Enforced_Count", "value": enforced, "labels": {"severity": "critical" if enforced else "normal"}},
    ]

def main() -> None:
    tx = MetricsTransmitter(
        endpoint=FINAL_ENDPOINT,
        username=USERNAME,
        api_key=API_KEY,
        hmac_key=HMAC_KEY,
        pin_sha256=PIN_SHA256
    )
    while True:
        batch = collect_metrics()
        ok = tx.push(batch)
        # Optional: reflect transmit status to console logs
        print(f"[observer] pushed={ok}, metrics={len(batch)}")
        time.sleep(REPORT_EVERY_SECONDS)

if __name__ == "__main__":
    main()
