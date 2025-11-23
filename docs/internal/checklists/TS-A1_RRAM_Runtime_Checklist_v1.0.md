# TS-A1 ↔ RRAM — Operator Runtime Checklist (v1.0)

> If `governance/ledger/receipts/` doesn’t exist yet, keep receipts under `governance/ledger/` for now.

**Deployment ID:** `_______`  
**RRAM chip / vendor:** `_______`  
**TS-A1 build tag:** `_______` (commit/tag)  
**Security level:** `L1 / L2 / L3`  
**Calibration hash:** `sha256: _______` (for this build + chip)

## Gates
- [ ] **Purity Gate** — ACS drop ≤ **0.01** vs calibrated baseline  
- [ ] **Stability Gate** — 24h drift ≤ **1e-3**  
- [ ] **Receipt Gate** — all batches hashed; OTS queued when live  
- [ ] **Fail-safe armed** — auto-halt on violation

## Ledger links
- **ULIC registry ref:** `governance/ledger/ULIC_v9.1.yaml`  
  - `registry_sha256:` `f46a18bb37d24f035ab5fefa0b6a024d40ff98ad64acfe3710fb9ecc924477ab`
- **EVL v9.0:** `governance/ledger/EVL_v9.0.yaml`  
  - `sha256:` `173703a64fa4c18948f439b85c16627f6ee47a9b66c7f8008505062b0b45447d`, `55f6ea93192b3a490b5b65dfc0ff4275358d92f237134cea54437bdcdf144bbb`
- **QCEP v9.0:** `governance/governance/ledger/seals/QCEP_Epoch_Manifest_v9.0.yaml`  
  - `sha256:` `251463d574b1cca2ccf8be68879a12019e94b3a057638d330af273b3824514e9`

## Anchoring status
- ULIC: `ots_receipt: governance/ledger/ULIC_v9.1.ots` • `ots_anchor_status: Receipt issued — awaiting Bitcoin confirmation (OpenTimestamps)`  
- EVL:  `ots_receipt: governance/ledger/EVL_v9.0.ots`  • `ots_calendar_id: ae277fd4755d3eef0c4ad21a2ef94b9c9239a37cdc9f8de1ba930fcf104b9960`  
- QCEP: **Anchored — OpenTimestamps** (tx recorded in manifest)

## Operator log
- **Batch hashes (sha256):**  
  - `________`  
  - `________`
- **Incidents / notes:**  
  - `________`

**Sign-off:** Operator `_______` • Auditor `_______` • UTC `_______`
