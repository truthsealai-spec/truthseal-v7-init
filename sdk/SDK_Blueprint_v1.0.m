# TruthSeal™ SDK Blueprint v1.0 (Minimal, Opinionated)

## Goal
Give developers two dead-simple calls that hide all complexity:
- `seal_data(record)` → returns a **Certificate JSON** (+ ID/QR) after hashing, signing (PQC placeholder), store/log, and optional anchor enqueue.
- `verify_seal(certificate_id)` → returns **VERIFIED / NOT VERIFIED** + provenance (hash match, manifest check, OTS/Polygon status).

## Environment (read from .env)
TRUTHSEAL_ENV=dev
MILVUS_HOST=localhost:19530
POSTGRES_URL=postgres://postgres:password@localhost:5432/api
MINIO_ENDPOINT=localhost:9010
MINIO_ACCESS_KEY=minioadmin
MINIO_SECRET_KEY=minioadmin
PQC_MODE=placeholder        # real keys provisioned later via KMS/HSM

## Canonicalization & Hash (non-negotiable)
- Canonical JSON: **JCS** (RFC 8785 style rules).
- Digest: **SHA-256** of the canonical JSON bytes.

## Certificate JSON (returned by seal_data)
{
  "certificate_id": "<ulid/uuid>",
  "artifact_sha256": "<64-hex>",
  "policy_hash": "<active_policy_sha256>",
  "model_build_id": "<string>",
  "embedding_build_id": "<string>",
  "milvus_version": "v2.4.15-gpu",
  "pgvector_version": "pg16/pgvector",
  "acs": <float>,                    // Aim Coherence Score
  "ljc": <float>,                    // Logical Judgment Code
  "thresholds": { "ljc_min": 0.85 },
  "pqc_sig_type": "Dilithium-3 (placeholder)",
  "sig": "<base64-or-hex>",
  "ots_calendar_id": "<when enqueued>",
  "ots_tx": null,                    // fills when anchored
  "anchor_utc": null                 // fills when anchored
}

## Python (reference skeleton)
```python
import json, hashlib, uuid, datetime
from jcs import canonicalize  # use any JCS lib

def _sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def seal_data(record: dict) -> dict:
    canon = canonicalize(record).encode("utf-8")
    h = _sha256_bytes(canon)

    cert = {
        "certificate_id": str(uuid.uuid4()),
        "artifact_sha256": h,
        "policy_hash": os.getenv("ACTIVE_POLICY_SHA256", ""),
        "model_build_id": os.getenv("MODEL_BUILD_ID", ""),
        "embedding_build_id": os.getenv("EMBEDDING_BUILD_ID", ""),
        "milvus_version": "v2.4.15-gpu",
        "pgvector_version": "pg16/pgvector",
        "acs": compute_acs(record),   # stub → calls nemo-retriever
        "ljc": compute_ljc(record),   # stub → GPU path
        "thresholds": {"ljc_min": 0.85},
        "pqc_sig_type": "Dilithium-3 (placeholder)",
        "sig": pqc_placeholder_sign(h),
        "ots_calendar_id": enqueue_ots(h),  # optional queue stub
        "ots_tx": None,
        "anchor_utc": None,
    }
    store_certificate(cert)          # MinIO/postgres
    log_chain_of_custody(h, cert)    # append-only log
    return cert

def verify_seal(certificate_id: str) -> dict:
    cert = fetch_certificate(certificate_id)
    exists = cert is not None
    hash_ok = exists and hash_exists_in_manifest(cert["artifact_sha256"])
    anchor_ok = exists and check_ots_or_polygon(cert)
    verdict = exists and hash_ok and cert["ljc"] >= cert["thresholds"]["ljc_min"]
    return {
        "status": "VERIFIED" if (verdict and anchor_ok) else "NOT VERIFIED",
        "hash_ok": hash_ok,
        "anchor_ok": anchor_ok,
        "acs": cert.get("acs") if exists else None,
        "ljc": cert.get("ljc") if exists else None,
        "provenance": {
            "manifest_check": hash_ok,
            "ots_tx": cert.get("ots_tx"),
        }
    }
