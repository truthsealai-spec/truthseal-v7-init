# TS-A1 ↔ RRAM — Deployment Acceptance Template (v1.0)

**Deployment name:** `________`  
**Site / cluster:** `________` • **Date (UTC):** `________`  
**RRAM chip / firmware:** `________` • **TS-A1 version:** `________`  
**Security level:** `L1 / L2 / L3`

## Calibration
- Calibration dataset & method: `________`
- Calibration **sha256:** `________`
- Baseline ACS: `________`

## Validation results
- Purity Gate (ACS drop ≤ 0.01):  ✅ / ❌  • measured: `________`  
- Stability Gate (24h drift ≤ 1e-3): ✅ / ❌  • measured: `________`  
- Receipt Gate (all batches hashed; OTS queued): ✅ / ❌  
- Fail-safe armed (auto-halt): ✅ / ❌

## Ledger references
- ULIC v9.1: `governance/ledger/ULIC_v9.1.yaml` • `registry_sha256: f46a18bb37d24f035ab5fefa0b6a024d40ff98ad64acfe3710fb9ecc924477ab`  
- EVL v9.0: `governance/ledger/EVL_v9.0.yaml` • `ots_receipt: governance/ledger/EVL_v9.0.ots`  
- QCEP v9.0: `governance/governance/ledger/seals/QCEP_Epoch_Manifest_v9.0.yaml`

## Decision
- **ACCEPT / REJECT** (circle one)  
- Conditions / follow-ups: `________`

**Sign-offs**  
- Operator: `________`  
- Auditor (TruthSeal): `________`  
- Owner (Dr. Nickolay Traykov): `________`
