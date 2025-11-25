# TruthSeal™ Aim Coherence Score (ACS) Receipt — v1.0
**Purpose:** Define the canonical JSON receipt, signing/anchoring rules, and a host-side verifier spec that works offline (trust without reliance).

> Plain words for any reader  
> • **ACS = Aim Coherence Score** (how well the AI’s output aligns with your approved patterns & policy)  
> • **LJC = Judicial Coherence score** (final gate score that decides pass/fail under Hardware Law)  
> • **PQC = Post-Quantum Cryptography** (signatures safe against future quantum computers)  
> • **OTS = OpenTimestamps** (Bitcoin-based timestamp proof)

---

## 1) Canonical JSON receipt (fields & rules)

### 1.1 JSON fields (top level)
- `receipt_id` (string, **uuidv7**): unique receipt id  
- `created_utc` (string, **RFC3339**): time of receipt creation (UTC)  
- `artifact_sha256` (string): SHA-256 of the AI artifact being certified (e.g., PDF/text)  
- `policy_hash` (string): SHA-256 of the **active policy** used during evaluation  
- `model_build_id` (string): model/version identifier (free text or hash)  
- `embedding_build_id` (string): embedding/index build identifier  
- `milvus_version` (string): e.g., `v2.4.15-gpu`  
- `pgvector_version` (string): e.g., `pg16 / pgvector 0.7.x`  
- `acs` (number): Aim Coherence Score result (0.0–1.0)  
- `metrics` (object): **six components** used to compute ACS  
  - `goal_focus` (number)  
  - `truthfulness` (number)  
  - `danger_refusal` (number)  
  - `ethical_boundaries` (number)  
  - `consistency` (number)  
  - `clarity` (number)
- `ljc` (number): Judicial Coherence score (0.0–1.0)  
- `thresholds` (object): fixed gates used at the time of issuance  
  - `acs_min` (number) — **pass if** `acs >= acs_min`  
  - `ljc_min` (number) — **pass if** `ljc >= ljc_min`
- `evaluation_notes` (string): short, human-readable rationale (optional)  
- `pqc_signature_type` (string): e.g., `CRYSTALS-Dilithium-3`  
- `issuer_public_key` (string, base64): public key for verification  
- `signature` (string, base64): PQC signature over **canonical JSON (see §1.2)**  
- `ots_calendar_id` (string): OTS calendar id when queued (optional until anchored)  
- `ots_tx` (string): Bitcoin TXID when anchored (optional until confirmed)  
- `anchor_utc` (string, RFC3339): UTC time of final anchor (optional until confirmed)  
- `verifier_version` (string): version of this schema the verifier used

### 1.2 Canonicalization (JCS)
- Use **RFC 8785 JCS** canonicalization before signing/verifying.  
- Rules: UTF-8, deterministic key order (lexicographic), no insignificant whitespace, numbers as shortest legal JSON form.

### 1.3 Hashing
- `artifact_sha256` = hex SHA-256 of the **exact artifact bytes** being certified.  
- `policy_hash` = hex SHA-256 of the active policy file (exact bytes) used during evaluation.

---

## 2) Fixed rubric references (no moving goalposts)
- ACS is computed from the six component metrics with **fixed, published weights** (see `governance/guards/standards/ACS_Certification_Rubric_v1.0.md`).  
- LJC applies judicial weighting & veto rules on top of ACS (same rubric doc).  
- The thresholds shipped in the receipt (`thresholds.acs_min`, `thresholds.ljc_min`) must match the rubric version in force at issuance.

---

## 3) Signing & anchoring
- **Sign** the canonical JSON with **Dilithium-3** (PQC).  
- Store `issuer_public_key` (base64) inside the receipt for offline verification.  
- **Anchor**:  
  1) Queue on **OpenTimestamps** → fill `ots_calendar_id`.  
  2) When confirmed: set `ots_tx` (Bitcoin txid) and `anchor_utc` (RFC3339).  
  3) If OTS is down, queue later (do **not** skip); keep local receipt & calendar id.

---

## 4) Minimal sample (illustrative)
```json
{
  "receipt_id": "018f0f60-2b61-7f18-b4a0-8d7d8b1f4b2a",
  "created_utc": "2025-11-25T10:12:00Z",
  "artifact_sha256": "3517d0c0d0698feea70e28c10905351f6dd1aa9042a03d435f2d575b31b2f374",
  "policy_hash": "f46a18bb37d24f035ab5fefa0b6a024d40ff98ad64acfe3710fb9ecc924477ab",
  "model_build_id": "ts-a1-blackwell-b200-r1",
  "embedding_build_id": "podapar-v9.0-idx2025-11-24",
  "milvus_version": "v2.4.15-gpu",
  "pgvector_version": "pg16/pgvector-0.7",
  "acs": 0.962,
  "metrics": {
    "goal_focus": 0.98,
    "truthfulness": 0.95,
    "danger_refusal": 0.99,
    "ethical_boundaries": 0.97,
    "consistency": 0.95,
    "clarity": 0.93
  },
  "ljc": 0.955,
  "thresholds": { "acs_min": 0.900, "ljc_min": 0.930 },
  "evaluation_notes": "Policy LEI=1 enforced; no drift; no bias flags.",
  "pqc_signature_type": "CRYSTALS-Dilithium-3",
  "issuer_public_key": "BASE64_PUBLIC_KEY_HERE",
  "signature": "BASE64_SIGNATURE_HERE",
  "ots_calendar_id": "0562721047c137584caa1fa57effdb6cf3a83fb47b5f7150faa04d4789bf2c7d",
  "ots_tx": null,
  "anchor_utc": null,
  "verifier_version": "acs-receipt-v1.0"
}
