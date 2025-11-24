# TruthSeal™ Ledger Receipts — Queue (v1.0)

**Purpose.** Temporary home for local receipt files (JSON) until external anchoring (OpenTimestamps / OriginStamp / BTCStamp) is live. These receipts cover ULIC v9.1, EVL v9.0, QCEP v9.0, Integrity v8_pre, and demo/test artifacts.

**Folder.** `governance/ledger/receipts/`

**One-receipt-per-artifact/batch.** Use this filename pattern:
`<YYYYMMDDTHHMMSSZ>__<artifact_short>__sha256_<first12>.json`

Examples  
• `2025-11-23T23:05:00Z__ULIC_v9.1.yaml__sha256_f46a18bb37d2.json`  
• `2025-11-23T23:07:00Z__EVL_v9.0.yaml__sha256_173703a64fa4.json`

## Minimal JSON schema (v1.0)

```json
{
  "artifact_path": "governance/ledger/ULIC_v9.1.yaml",
  "sha256": "f46a18bb37d24f035ab5fefa0b6a024d40ff98ad64acfe3710fb9ecc924477ab",
  "created_utc": "<ISO8601>",
  "source": "ACS demo | ops | calibration",
  "note": "<optional context>",
  "ots_status": "pending | receipt_issued | anchored",
  "ots_calendar_id": "<if issued>",
  "ots_receipt_path": "governance/ledger/receipts/ULIC_v9.1.ots",
  "ots_tx": "<txid if anchored>",
  "anchor_utc": "<UTC when anchored>"
}
