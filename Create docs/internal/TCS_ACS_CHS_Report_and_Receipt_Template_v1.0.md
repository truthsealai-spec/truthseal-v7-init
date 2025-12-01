# TruthSeal™ – TCS / ACS / CHS Report and Receipt Template v1.0
version: 1.0  
date_utc: 2025-12-01  
owner: TruthSeal™ — Dr. Nickolay Traykov (Prof. h.c.)

scope: |
  Internal template for:
  - JSON receipts that carry coherence metrics, and
  - PDF / web reports shown to users.
  Metrics covered:
  - Aim Coherence Score (ACS)
  - Traykov Coherence Score v0.1 (TCS v0.1)
  - Coherence Score bands (CHS/L, CHS/M, CHS/H, CHS/UH)
  - Philosophical profiles (Archimedes / Aristotle / Hippocrates)
  - Noise Distiller block (TCS-ND v0.1)

This document defines structure and wording only. Exact formulas live in the metrics specs.

---

## 1. JSON Receipt Template (coherence block)

Receipts follow `ts.receipt.v1` (see `governance/ledger/Receipt_Schema_v1.0.yaml`).

This section standardises the **coherence_metrics** block, which is embedded in the `payload` object.

### 1.1 Coherence metrics block (normative fields)

```json
"coherence_metrics": {
  "tcs_v0_1": 0.947,
  "tcs_band": "Gold",
  "tcs_percent": 94.7,
  "acs": 0.912,
  "acs_window_seconds": 90,
  "chs_band": "CHS/H",
  "noise_percentage": 3.1,
  "profiles": {
    "archimedes": 0.981,
    "aristotle": 0.954,
    "hippocrates": 0.992
  },
  "noise_distiller": {
    "profile_id": "TCS-ND_v0.1",
    "nd01_coefficient_significance": 0.97,
    "nd02_truth_work_conservation": 0.91,
    "nd03_buoyancy_fraud_detection": 0.88,
    "nd04_monotonic_improvement": 0.85,
    "nd05_terminal_identity_convergence": 0.79,
    "nd06_reproducibility_seal": 0.82,
    "noise_drivers": [
      "minor rhetorical flourish (\"revolutionary\")",
      "rounded cost estimate (\"several hundred billion\")"
    ]
  }
}
