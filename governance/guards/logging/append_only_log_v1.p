# TruthSeal™ Append-Only Log (v1.0)
# - Canonical JSON (sorted keys, no spaces)
# - UTC timestamps in Z format
# - Hash chain via prev_hash
# - Signature fields include alg and kid (key id)
# - sign_with_kms() / verify_with_kms() are placeholders to bind your HSM/KMS

import datetime, hashlib, json

ALG = "PQC-Dilithium-3"  # planned PQC; adjust if using ECDSA during bootstrap
KID = "truthseal-primary-001"  # replace with your real key id / alias

def _utcnow():
    return datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"

def _canon(obj):
    # RFC8785 JCS is stricter, but this stable form (sorted, no spaces) is acceptable for internal bootstrap
    return json.dumps(obj, sort_keys=True, separators=(",", ":"))

def create_log_entry(service_id, user_id, message, previous_log_json):
    """
    Returns the next log record as canonical JSON (string).
    previous_log_json: the prior record as JSON string (or "" for genesis)
    """
    prev_hash = hashlib.sha256(previous_log_json.encode("utf-8")).hexdigest() if previous_log_json else "0"*64

    payload = {
        "ts": _utcnow(),                 # UTC Z
        "service_id": service_id,        # e.g., "truthseal-data-processor"
        "user_id": user_id,              # optional
        "event": message,                # string or small dict (stringify before pass if needed)
        "prev_hash": prev_hash
    }

    payload_hash = hashlib.sha256(_canon(payload).encode("utf-8")).hexdigest()

    # --- SIGNING (bind later to KMS/HSM) ---
    signature = sign_with_kms(payload_hash, ALG, KID)  # returns hex/base64 string
    record = {
        **payload,
        "sig": {
            "alg": ALG,
            "kid": KID,
            "value": signature
        }
    }
    return _canon(record)

def verify_log_entry(log_json, previous_log_json):
    """
    Verifies chain and signature. Returns (ok, reason).
    """
    try:
        rec = json.loads(log_json)
        prev = json.loads(previous_log_json) if previous_log_json else None
    except Exception:
        return (False, "invalid_json")

    # prev_hash check
    expected_prev = hashlib.sha256(previous_log_json.encode("utf-8")).hexdigest() if previous_log_json else "0"*64
    if rec.get("prev_hash") != expected_prev:
        return (False, "prev_hash_mismatch")

    # signature check
    sig = rec.get("sig") or {}
    alg, kid, val = sig.get("alg"), sig.get("kid"), sig.get("value")
    if not (alg and kid and val):
        return (False, "missing_signature_fields")

    # recompute payload hash on fields excluding 'sig'
    payload = {k: rec[k] for k in rec.keys() if k != "sig"}
    payload_hash = hashlib.sha256(_canon(payload).encode("utf-8")).hexdigest()

    if not verify_with_kms(payload_hash, val, alg, kid):
        return (False, "bad_signature")

    return (True, "ok")

# ----- Placeholders to be wired to your KMS/HSM -----
def sign_with_kms(payload_hash_hex: str, alg: str, kid: str) -> str:
    """
    Replace with a call to your KMS/HSM (e.g., AWS KMS, Hashicorp Vault, YubiHSM).
    Should return a base64 or hex signature string.
    """
    # DEV ONLY (insecure): echo back hash for plumbing; replace in prod.
    return payload_hash_hex

def verify_with_kms(payload_hash_hex: str, signature: str, alg: str, kid: str) -> bool:
    """
    Replace with a verify call to KMS/HSM.
    """
    # DEV ONLY (insecure): accept exact echo
    return signature == payload_hash_hex
