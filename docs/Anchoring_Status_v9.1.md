# Anchoring Status v9.1 — Mobile Audit Stub

Purpose: Single page tracking of anchoring for the current registry set.
Legend: Pending → Receipt issued → Anchored (with TX / UTC)

## ULIC v9.1
path: governance/ledger/ULIC_v9.1.yaml
registry_sha256: f46a18bb37d24f035ab5fefa0b6a024d40ff98ad64acfe3710fb9ecc924477ab
ots_calendar_id: 0562721047c137584caa1fa57effdb6cf3a83fb47b5f7150faa04d4789bf2c7d
anchor_status: Receipt issued — awaiting Bitcoin confirmation

## EVL v9.0
path: governance/ledger/EVL_v9.0.yaml
sha256: 55f6ea93192b3a490b5b65dfc0ff4275358d92f237134cea54437bdcdf144bbb
ots_calendar_id: ae277fd4755d3eef0c4ad21a2ef94b9c9239a37cdc9f8de1ba930fcf104b9960
anchor_status: Receipt issued — awaiting Bitcoin confirmation

## QCEP v9.0
path: governance/governance/ledger/seals/QCEP_Epoch_Manifest_v9.0.yaml
sha256: 251463d574b1cca2ccf8be68879a12019e94b3a057638d330af273b3824514e9
ots_anchor_status: Anchored — OpenTimestamps
ots_anchor_tx: 9d5b2d5b75207756bcd674d2...

## Integrity Manifest v8_pre
path: governance/governance/ledger/seals/Integrity_Manifest_v8_pre.yaml
composite_digest: b6f666d2d45fd01884cc358626ada982ce4852f31a0b1f69b50f3c2b5d90a7a0
ots_receipt: governance/ledger/receipts/Integrity_Manifest_v8_pre.ots
ots_anchor_status: Anchored — OpenTimestamps
composite_update_utc: 2025-11-05T22:44:00Z

## QENC v1.0 ProofCapsule
path: governance/governance/ledger/seals/QENC_v1_0_ProofCapsule.json
sha256: a54fb4dd47f0d5d9677ad7089e363d8e0c3a1cecb20ed7973a56f2ba15006f2b
anchor_status: Pending anchor (queue for OpenTimestamps)

### Next actions
- When OTS confirms for ULIC/EVL, record TX and flip to “Anchored — <UTC>”.
- On desktop, upload .ots receipts to governance/ledger/receipts/.
- Update this page after each anchor event.
- QENC v1.0

path: governance/governance/ledger/seals/QENC_v1_0_ProofCapsule.json
sha256: a54fb4dd47f0d5d9677ad7089e363d8e0c3a1cecb20ed7973a56f2ba15006f2b
anchor_status: Pending — prepare OpenTimestamps receipt
