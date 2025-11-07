# TruthSeal™ Observability — Minimal Security Reporter Loop (v1.0)
# Reads configuration only from environment variables. No secrets in code.

import os
import time
from typing import List, Dict, Any

from .metrics_transmitter_v1 import (
    MetricsTransmitter,
    FINAL_ENDPOINT,
    USERNAME,
    API_KEY,
    HMAC_KEY,
    PIN_SHA256,
)

# How often to report, in seconds (default: 10)
REPORT_EVERY_SECONDS = int(os.getenv("METRICS_REPORT_EVERY_SECONDS", "10"))

def collect_metrics() -> List[Dict[str, Any]]:
    """
    Minimal collector:
      - threat score average comes from an environment variable
      - violation count comes from an environment variable
      - level-three enforced flag derives from SECURITY_LEVEL
    """
    # Pull counters from environment (agent or commander sets these)
    threat_avg = float(os.getenv("THREAT_SCORE_AVG", "0.0"))
    violations = float(os.getenv("SECURITY_POLICY_VIOLATION_COUNT", "0"))
    level = os.getenv("SECURITY_LEVEL", "2").strip()
    enforced = 1.0 if level == "3" else 0.0

    return [
        {"name": "SLM_Threat_Score_Avg", "value": threat_avg, "labels": {"source": "slm_aggregate"}},
        {"name": "Security_Policy_Violation_Count", "value": violations, "labels": {"source": "commander"}},
        {"name": "Security_Level_3_Enforced_Count", "value": enforced, "labels": {"source": "commander"}},
    ]

def main() -> None:
    tx = MetricsTransmitter(
        endpoint=FINAL_ENDPOINT,
        username=USERNAME,
        api_key=API_KEY,
        hmac_key=HMAC_KEY,
        pin_sha256=PIN_SHA256,
    )

    while True:
        batch = collect_metrics()
        _ok = tx.push_to_endpoint(batch)
        time.sleep(REPORT_EVERY_SECONDS)

if __name__ == "__main__":
    main()
