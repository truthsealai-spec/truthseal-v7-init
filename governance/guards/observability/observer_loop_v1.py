# Package marker for observability components.
# Do not place secrets or runtime config here.
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
