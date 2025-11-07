# TruthSeal Observability — minimal guide (no secrets)

## Purpose
Real-time reporting of security, integrity, and performance metrics to the metrics endpoint for dashboards and alerts.

## Files in this folder
- `metrics_transmitter_v1.py` — sends metrics over secure https with basic auth, hash-based message authentication, and certificate pin.
- `observer_loop_v1.py` — collects counters from environment variables and pushes every few seconds.
- `observer.env.example` — sample environment file (placeholders only).
- `__init__.py` — package marker.

## Environment variables (set these outside the repository)
- METRICS_ENDPOINT — https address of the metrics receiver.
- METRICS_USERNAME — reporter account name.
- METRICS_API_KEY — access token for the reporter.
- METRICS_HMAC_KEY — secret key for message authentication.
- METRICS_TLS_CERT_PIN_SHA256 — certificate fingerprint for pinning.
- METRICS_JOB_NAME — label to group reports.
- INSTANCE_ID — label of the running node.
- METRICS_REPORT_EVERY_SECONDS — interval between pushes.
- THREAT_SCORE_AVG, SECURITY_POLICY_VIOLATION_COUNT, SECURITY_LEVEL — counters read by the observer.

## Security notes
- Do not commit a real `.env`. The root `.gitignore` already prevents that.
- Keep keys in a secret manager or a hardware security module. The example file is for local testing only.
- The observer has one job: collect and push metrics. It cannot read decryption keys or submit jobs.

## Next hook
When “Epoch Verification Ledger Hash Mismatch Count” rises above zero, trigger the alerting system to set “Security Level” to “3” and pause job submissions until a human review is done.
