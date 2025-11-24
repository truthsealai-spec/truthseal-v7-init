# TruthSeal™
## Anchoring Status — v9.1

Last update (UTC): 2025-11-23T22:51:00Z

This page tracks the anchoring state of the v9.1 registry and linked epoch artifacts (ULIC v9.1, EVL v9.0, QCEP v9.0, Integrity v8_pre).

---

## ULIC Registry (v9.1)

- **File:** `governance/ledger/ULIC_v9.1.yaml`  
- **registry_sha256:** `f46a18bb37d24f035ab5fefa0b6a024d40ff98ad64acfe3710fb9ecc924477ab`  
- **ots_calendar_id:** `0562721047c137584caa1fa57effdb6cf3a83fb47b5f7150faa04d4789bf2c7d`  
- **ots_receipt:** `governance/ledger/ULIC_v9.1.ots` (upload when available)  
- **status:** Receipt issued — awaiting Bitcoin confirmation (OpenTimestamps)

---

## Epoch Verification Ledger (EVL v9.0)

- **File:**  
  `governance/ledger/EVL_v9.0.yaml`

- **sha256:**  
  - `173703a64fa4c18948f439b85c16627f6ee47a9b66c7f8008505062b0b45447d`  
  - `55f6ea93192b3a490b5b65dfc0ff4275358d92f237134cea54437bdcdf144bbb`

- **ots_calendar_id:**  
  `ae277fd4755d3eef0c4ad21a2ef94b9c9239a37cdc9f8de1ba930fcf104b9960`

- **ots_receipt:**  
  `governance/ledger/EVL_v9.0.ots` (upload when available)

- **status:**  
  Receipt issued — awaiting Bitcoin confirmation (OpenTimestamps)
- **timestamp:** `2025-11-05T06:54:00+11:00`

---
### QCEP Epoch Manifest (v9.0)

- **File:** `governance/ledger/seals/QCEP_Epoch_Manifest_v9.0.yaml`
- **sha256:** `251463d574b1cca2ccf8e68879a12019e94b3a057638d330af273b3824514e9`
- **ots_receipt:** `governance/ledger/receipts/2025-11-23T23:15:00Z__QCEP_Epoch_Manifest_v9.0.yaml__sha256_251463d574b1.json`
- **status:** Receipt issued — awaiting Bitcoin confirmation (OpenTimestamps)
## QCEP Epoch Manifest (v9.0)

- **File:** `governance/governance/ledger/seals/QCEP_Epoch_Manifest_v9.0.yaml`  
- **sha256:** `251463d574b1cca2ccf8be68879a12019e94b3a05763ad330af273b3824514e9`  
- **ots_receipt:** `governance/ledger/receipts/QCEP_Epoch_Manifest_v9.0.ots` (upload when available)  
- **anchor_status:** **Anchored — OpenTimestamps**  
- **ots_anchor_tx:** `9d5b2d5b75207756bcd674d2...`

---

## Integrity Manifest (v8_pre)

- **File:** `governance/governance/ledger/seals/Integrity_Manifest_v8_pre.yaml`  
- **outcome:** verified  
- **composite_digest:** `b6f666d2d45fd01884cc358626ada982ce4852f31a0b1f69b50f3c2b5d90a7a0`  
- **composite_update.timestamp_utc:** `2025-11-05T22:44:00Z`  
- **ots_receipt:** `governance/ledger/receipts/Integrity_Manifest_v8_pre.ots` (upload when available)  
- **ots_anchor_status:** **Anchored — OpenTimestamps**

---

### Next actions
- When OTS/OriginStamp/BTCStamp are live, upload the missing `.ots` files under `governance/ledger/receipts/` and flip any **status** lines from “Receipt issued — …” to “Anchored — <UTC time>”.  
- When anchoring confirms, record **TX id(s)** where applicable.  
- (Planned) Normalize `governance/governance/ledger/seals/` → `governance/ledger/seals/` in a dedicated follow-up commit and update paths here accordingly.
- ---

## Receipts (queue)

For the live JSON receipts (one per artifact/batch), see the index:

- `governance/ledger/receipts/INDEX_v1.0.md`
