# TruthSeal™ Anchoring Status — v9.1

Last update: <set current UTC>

## ULIC Registry (v9.1)
- File: governance/ledger/ULIC_v9.1.yaml
- registry_sha256: f46a18bb37d24f035ab5fefa0b6a024d40ff98ad64acfe3710fb9ecc924477ab
- ots_calendar_id: 0562721047c137584caa1fa57effdb6cf3a83fb47b5f7150faa04d4789bf2c7d
- ots_receipt: governance/ledger/ULIC_v9.1.ots  (to upload when available)
- status: Receipt issued — awaiting Bitcoin confirmation (OpenTimestamps)

## Epoch Verification Ledger (EVL v9.0)
- File: governance/ledger/EVL_v9.0.yaml
- sha256: e650ca5a935f4ff25c5186dbaf83887bfa587de806e17ccd27edb3c509bbf921
- ots_calendar_id: ae277fd4755d3eef0c4ad21a2ef94b9c9239a37cdc9f8de1ba930fcf104b9960
- ots_receipt: governance/ledger/EVL_v9.0.ots  (to upload when available)
- status: Receipt issued — awaiting Bitcoin confirmation (OpenTimestamps)

## Integrity Manifest (v8_pre)
- File: governance/ledger/Integrity_Manifest_v8_pre.yaml
- composite_digest: (see file)
- ots_fields: present in file
- status: Anchoring fields recorded (awaiting final receipt upload if applicable)

## QECP Epoch Manifest (v9.0)
- File: governance/ledger/QCEP_Epoch_Manifest_v9.0.yaml
- sha256: 251463d574b1cca2ccf8be68879a12019e94b3a057638d330af273b3824514e9
- timestamp_tx: 9d5b2d5b75207765bcd674d2edd311b98f916421a3b2ae4f5c922e5e63dce4f8
- status: Anchored — OpenTimestamps

---

### Operator notes
- If external anchoring is down, keep calendar IDs in YAML and log status here.
- When services are back: upload `.ots` files into `governance/ledger/` and flip each status to **Anchored — <UTC>**.
- This page is the single source of truth for anchor state in v9.1.
