# TS-A1 Mobile Readiness — Notes v1.0
Scope: prepare TruthSeal AEGIS Core (TS-A1) for potential AI-native smartphones (any vendor).

Why now (signals, not certainties):
- No confirmed NVIDIA-branded phone as of today; focus is on AI factories + telecom edges. Treat phone talk as unverified.
- If AI-native phones land, they’ll need on-device safety + receipts to pass enterprise/regulatory checks.

What we ship (device-agnostic):
- ACS Gate (Purity): enforce ≤0.01 drop from calibrated baseline.
- Stability Gate: 24h drift ≤1e-3; auto-halt on violation (LEI=1).
- Receipt Engine: per-batch SHA-256 + queue OTS when services are up.
- Local-first mode: works offline; anchors later when networks/services return.

Integration sketch:
- Android/Linux kernel module or privileged service binding to NPUs/accelerators.
- Minimal telemetry: ACS, drift, halt events, receipt IDs (no user content).
- Config via YAML; receipts stored under governance/ledger/ (device profile).

Open items:
- Battery/thermal policy: throttle bands for mobile.
- Privacy profile: strict PII redaction in receipts.
- Partner shortlist: leading Android OEMs and ODMs (original design manufacturers).

State today:
- Data center + edge path proven in repo.
- Mobile path defined; implementation deferred until credible partner signal.

Status label: Ready-to-brief (no NDA required for high-level).
