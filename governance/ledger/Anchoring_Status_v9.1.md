# TruthSeal Anchoring Status — v9.1 (mobile audit stub)

composite_sha256: d37941449bab19af6777f111ae065a2aa7ff1361f17cf19fcc662c2e14a29de8
last_checked_utc: "2025-11-06T07:00:53Z"
Verification summary:
• Commander policy v2.1 → sha256 matches EVL ✅
  e0708a6dc6038bcb80ab2b8f6c3fd982386f41f53f6ab244077ebfa7d96addc4
- Validator (job_validator_v1.py) → matches EVL validator_sha256 ✅
- ULIC_v9.1 → registry_sha256 matches composite ✅
- EVL_v9.0 → ulic_registry_sha256 matches composite ✅
- QCEP_Epoch_Manifest_v9.0 → added_refs.ulic_registry_sha256 matches composite ✅
- Integrity_Manifest_v8_pre → added_refs.ulic_registry_sha256 matches composite ✅
- Paramount_Policy_Charter_v1.0 → sha256 matches EVL policy_refs ✅
  path: governance/TruthSeal_Paramount_Policy_Charter_v1.0.md
  sha256: 32c9952b67bfdfaa858b8aaa983f0d71a27930e6c58dbac36bbf381589b747b6
  evl_ref: governance/ledger/EVL_v9.0.yaml
  ulic_registry_sha256: d37941449bab19af6777f111ae065a2aa7ff1361f17cf19fcc662c2e14a29de8
  ots_receipt: governance/ledger/receipts/TruthSeal_Paramount_Policy_Charter_v1.0.ots
  ots_anchor_status: "Pending"

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
  

  Paramount_Policy_Charter_v1_0:
  path: governance/TruthSeal_Paramount_Policy_Charter_v1.0.md
  sha256: <0f74f785949e16e45c4ef9c65549a9d1873548ac6fd32d4abe3141e2a3fbb490>
  evl_ref: governance/ledger/EVL_v9.0.yaml
  ulic_registry_sha256: d37941449bab19af6777f111ae065a2aa7ff1361f7cf19fcc662c2e14a29de8
  ots_receipt: governance/ledger/receipts/TruthSeal_Paramount_Policy_Charter_v1.0.ots
  ots_anchor_status: "Pending"

  
Next actions:
  - Upload .ots files (ULIC_v9.1.ots, EVL_v9.0.ots) into governance/ledger/ when on desktop.
  - When confirmations land, flip all ots_anchor_status values to: "Anchored — Epoch Verification Confirmed"
  - Commander policy (v2.1)
- sha256: e0708a6dc6038bcb80ab2b8f6c3fd982386f41f53f6ab244077ebfa7d96addc4
- red_line: "NO_INDEPENDENT_AGENCY"
- output_contract: "JSON-only {status, code, qid, summary}"
- lockdown_on_red_line: true
- telemetry_counters:
  - Red_Line_Trip_Count
  - Security_Level_3_Enforced_Count
  - • alert_rules_v1.yml → sha256=6812b3a4c70b1793341d2952537a5d7d09a128c64843d2c694967a36a5e96898 matches EVL observability_refs ✅
• alertmanager_receiver_v1.yml → sha256=2028899f80c9e183e6e37a11aa2e34a0b36dba5616aaea216f12731ab82afca5 matches EVL observability_refs ✅
