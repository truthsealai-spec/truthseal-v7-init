# TruthSeal Anchoring Status — v9.1 (mobile audit stub)

composite_sha256: d37941449bab19af6777f111ae065a2aa7ff1361f17cf19fcc662c2e14a29de8

ULIC_v9.1:
  ots_receipt: governance/ledger/ULIC_v9.1.ots
  ots_calendar_id: 0562721047c137584caa1fa57effdb6cf3a83fb47b5f7150faa04d4789bf2c7d
  ots_anchor_status: "Receipt issued — awaiting Bitcoin confirmation (OpenTimestamps)"

EVL_v9.0:
  ulic_registry_ref: governance/ledger/ULIC_v9.1.yaml
  ulic_registry_sha256: d37941449bab19af6777f111ae065a2aa7ff1361f17cf19fcc662c2e14a29de8
  ots_receipt: governance/ledger/EVL_v9.0.ots
  ots_calendar_id: ae277fd4755d3eef0c4ad21a2ef94b9c9239a37cdc9f8de1ba930fcf104b9960
  ots_anchor_status: "Receipt issued — awaiting Bitcoin confirmation (OpenTimestamps)"

QCEP_Epoch_Manifest_v9.0:
  ulic_registry_sha256: d37941449bab19af6777f111ae065a2aa7ff1361f17cf19fcc662c2e14a29de8
  anchor_status: "Receipt issued — awaiting Bitcoin confirmation (OpenTimestamps)"
  ots_anchor_tx: "pending"

Integrity_Manifest_v8_pre:
  ulic_registry_sha256: d37941449bab19af6777f111ae065a2aa7ff1361f17cf19fcc662c2e14a29de8
  anchor_status: "Receipt issued — awaiting Bitcoin confirmation (OpenTimestamps)"

Next actions:
  - Upload .ots files (ULIC_v9.1.ots, EVL_v9.0.ots) into governance/ledger/ when on desktop.
  - When confirmations land, flip all ots_anchor_status values to: "Anchored — Epoch Verification Confirmed".
