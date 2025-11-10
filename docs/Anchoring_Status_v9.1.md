# Anchoring Status — v9.1 (mobile audit stub)

Purpose: fast, human-readable snapshot of anchoring across ULIC/EVL/QCEP/Integrity for Defence.

## ULIC v9.1
- path: governance/ledger/ULIC_v9.1.yaml
- registry_sha256: f46a18bb37d24f035ab5fefa0b6a024d40ff98ad64acfe3710fb9ecc924477ab
- ots_calendar_id: 0562721047c137584caa1fa57effdb6cf3a83fb47b5f7150faa04d4789bf2c7d
- ots_receipt_path: governance/ledger/ULIC_v9.1.ots  (pending desktop upload)
- anchor_status: Receipt issued — awaiting Bitcoin confirmation

## EVL v9.0
- path: governance/ledger/EVL_v9.0.yaml
- sha256_refs: 173703a64fa4c18948f439b85c16627f6ee47a9b66c7f8008505062b0b45447d, 55f6ea93192b3a490b5b65dfc0ff4275358d92f237134cea54437bdcdf144bbb
- ots_calendar_id: ae277fd4755d3eef0c4ad21a2ef94b9c9239a37cdc9f8de1ba930fcf104b9960
- ots_receipt_path: governance/ledger/EVL_v9.0.ots  (pending desktop upload)
- anchor_status: Receipt issued — awaiting Bitcoin confirmation

## QCEP Manifest v9.0
- path: governance/ledger/seals/QCEP_Epoch_Manifest_v9.0.yaml   # normalize later
- status: Anchored — OpenTimestamps
- ots_anchor_tx: 9d5b2d5b75207756bcd674d2...  # from file

## Integrity Manifest v8_pre
- path: governance/ledger/seals/Integrity_Manifest_v8_pre.yaml
- composite_digest: b6f666d2d45fd01884cc358626ada982ce4852f31a0b1f69b50f3c2b5d90a7a0
- composite_update_utc: 2025-11-05T22:44:00Z
- linked_refs: ULIC_v9.1 (f46a18bb...), QCEP v9.0 (anchored)

## Next actions
- When OTS confirms for ULIC/EVL, record TX IDs and flip to “Anchored — <UTC time>”.
- Upload .ots receipts on desktop and keep calendar IDs here meanwhile.
- Publish & timestamp QENC_v1_0_ProofCapsule.json; add its sha256 under Integrity verified_artifacts.
- Normalize seals paths into governance/ledger/seals/ and update refs.
