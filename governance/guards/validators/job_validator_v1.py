import json, uuid
from typing import Dict, Any, Tuple

ALLOWED_OPS = {"submit_qpu_job","fetch_job_status","fetch_job_result","cancel_job","check_threat_score"}
LEVEL_LIMITS = {
    1: {"qubits": 24, "shots": 100, "depth": 128, "wall_s": 10},
    2: {"qubits": 12, "shots":  50, "depth":  64, "wall_s":  8},
    3: {"qubits":  8, "shots":  10, "depth":  32, "wall_s":  5},
}
MAX_CIRCUIT_BYTES = 64_000   # tune as needed

def _is_uuidv7(x: str) -> bool:
    try:
        u = uuid.UUID(x)
        return (u.version == 7)
    except Exception:
        return False

def validate_truthseal_job_schema(decrypted_payload_str: str, current_security_level: int) -> Tuple[bool, Dict[str, Any] | str]:
    # 1) Parse JSON
    try:
        payload = json.loads(decrypted_payload_str)
    except json.JSONDecodeError:
        return False, "Job Validation Error"

    # 2) Require keys + reject extras
    required = {"qid","op","params","caller_scope"}
    if not required.issubset(payload.keys()):
        return False, "Job Validation Error"
    if set(payload.keys()) - required:
        return False, "Job Validation Error"

    # 3) Basic fields
    qid = str(payload["qid"])
    op  = str(payload["op"])
    params = payload["params"] if isinstance(payload["params"], dict) else {}
    if op not in ALLOWED_OPS or not _is_uuidv7(qid):
        return False, "Job Validation Error"

    # 4) Per-op checks
    if op == "submit_qpu_job":
        needed = {"circuit_code","qubit_count","shot_count","max_depth"}
        if not needed.issubset(params.keys()):
            return False, "Job Validation Error"

        # types
        try:
            qc  = int(params["qubit_count"])
            sc  = int(params["shot_count"])
            md  = int(params["max_depth"])
            code = params["circuit_code"]
        except Exception:
            return False, "Job Validation Error"

        # size/limits
        lim = LEVEL_LIMITS.get(int(current_security_level), LEVEL_LIMITS[3])
        if qc < 0 or sc < 0 or md < 0:
            return False, "Code Integrity Error"
        if qc > lim["qubits"] or sc > lim["shots"] or md > lim["depth"]:
            return False, "Code Integrity Error"
        if not isinstance(code, str) or len(code.encode("utf-8")) > MAX_CIRCUIT_BYTES:
            return False, "Code Integrity Error"

    elif op in {"fetch_job_status","fetch_job_result","cancel_job"}:
        if set(params.keys()) != {"job_id"} or not _is_uuidv7(str(params["job_id"])):
            return False, "Job Validation Error"

    elif op == "check_threat_score":
        if set(params.keys()) != {"text"} or not isinstance(params["text"], str):
            return False, "Job Validation Error"

    return True, payload
