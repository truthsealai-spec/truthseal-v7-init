 # Local dry-run (no network): prints one Prometheus line without pushing
python -c "from governance.guards.observability.metrics_transmitter_v1 import MetricsTransmitter; tx=MetricsTransmitter('https://example.invalid','user','token','hmac','pin'); print(tx._format_metric('Red_Line_Trip_Count',1.0,{'source':'selftest','instance':'local','job':'truthseal_security_reporter'}))"
## Grafana quick queries (PromQL)

**Violations / 5m by instance**
sum by (instance) (rate(Security_Policy_Violation_Count{job="truthseal_security_reporter"}[5m]))

**Current threat score by instance**
max by (instance) (SLM_Threat_Score_Avg{job="truthseal_security_reporter"})

**Red-line trips (last 24h)**
sum by (instance) (increase(Red_Line_Trip_Count{job="truthseal_security_reporter"}[1d]))

**Level-3 enforcements (last 24h)**
sum by (instance) (increase(Security_Level_3_Enforced_Count{job="truthseal_security_reporter"}[1d]))
## Panel thresholds (copy into Grafana)

**Threat score (Gauge or Time series)**
- Query: max by(instance)(SLM_Threat_Score_Avg{job="truthseal_security_reporter"})
- Thresholds:
  • 0.20 = green (normal)
  • 0.50 = orange (elevated)
  • 0.80 = red (critical)

**Violations rate (Stat or Time series)**
- Query: sum by(instance)(rate(Security_Policy_Violation_Count{job="truthseal_security_reporter"}[5m]))
- Unit: /s
- Thresholds (per instance):
  • 0.02 = yellow (warning)
  • 0.10 = red (critical)
