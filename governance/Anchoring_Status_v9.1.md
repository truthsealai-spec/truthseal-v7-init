# TruthSeal™ — Anchoring Status (v9.1)

_Last update (UTC): 2025-11-23T23:40:00Z_

Purpose: Track the anchoring state of the v9.1 registry and linked epoch artifacts (ULIC v9.1, EVL v9.0, QCEP v9.0, Integrity v8_pre), plus a quick view of external timestamping services.

---

## ULIC Registry (v9.1)

- **File:** `governance/ledger/ULIC_v9.1.yaml`
- **registry_sha256:** `f46a18bb37d24f035ab5fefa0b6a024d40ff98ad64acfe3710fb9ecc924477ab`
- **ots_calendar_id:** `0562721047c137584caa1fa57effdbc6f3a83fb47b5f7150faa04d4789bf2c7d`
- **ots_receipt:** `governance/ledger/ULIC_v9.1.ots` _(upload when available)_
- **status:** **Receipt issued — awaiting Bitcoin confirmation (OpenTimestamps)**

---

## Epoch Verification Ledger (EVL v9.0)

- **File:** `governance/ledger/EVL_v9.0.yaml`
- **sha256:**
  - `173703a64fa4c18948f439b85c16627f6ee47a9b66c7f8008505062b0b45447d`
  - `55f6ea93192b3a490b5b65dfc0ff4275358d92f237134cea54437bdcdf144bbb`
- **ots_calendar_id:** `ae277fd4755d3eef0c4ad21a2ef94b9c9239a37cdc9f8de1ba930fcf104b9960`
- **status:** **Receipt issued — awaiting Bitcoin confirmation (OpenTimestamps)**

---

## QCEP Epoch Manifest (v9.0)

- **File:** `governance/ledger/seals/QCEP_Epoch_Manifest_v9.0.yaml`
- **sha256:** `251463d574b1cca2ccf8e68879a12019e94b3a057638d330af273b3824514e9`
- **status:** **Anchored — OpenTimestamps** _(tx recorded in file)_

---

## Integrity Manifest (v8_pre)

- **File:** `governance/ledger/seals/Integrity_Manifest_v8_pre.yaml`
- **composite_update.timestamp_utc:** `2025-11-05T22:44:00Z`
- **ots_receipt:** `governance/ledger/receipts/Integrity_Manifest_v8_pre.ots` _(upload when available)_
- **ots_anchor_status:** **Anchored — OpenTimestamps**

---

## External timestamping services (quick check)

> This section is informational to guide next actions; keep receipts in the queue below.

- **OpenTimestamps:** LIVE (calendars reachable)
- **OriginStamp:** LIVE (public site reachable)
- **BTCStamp (Bitcoin Stamps):** LIVE (core site reachable)

**Action:** Publish and timestamp `QENC_v1_0_ProofCapsule.json` now when ready.

---

## Receipts (queue)

For live JSON receipts (one per artifact/batch), see the index:

- `governance/ledger/receipts/INDEX_v1.0.md`

---

## Next actions

1) When anchoring confirms, flip any “Receipt issued — …” to **“Anchored — …”** and record **TX id(s)** + **anchor_utc** where applicable.  
2) Upload missing `.ots` files under `governance/ledger/receipts/` once obtained.  
3) Keep EVL/ULIC/QCEP/Integrity paths and hashes in sync with their source files.
