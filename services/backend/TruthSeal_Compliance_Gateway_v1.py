# =========================================================================
# TRUTHSEAL™ COMPLIANCE DATA GATEWAY
# =========================================================================
#
# Purpose:
#   Service-layer helper that:
#     1) Collects all relevant compliance data for an action.
#     2) Builds the TruthSeal™ context payload (context_payload).
#     3) Calls the TruthSeal Compliance API (/check-compliance).
#     4) Enforces the verdict (raise on violations, return on success).
#
# This module is designed to be called from Django/Flask routes or
# other backend services BEFORE executing critical business actions
# (e.g. saving a new role, approving a large transaction, DEVORA ops).
# =========================================================================

import os
from typing import Dict, Any

import requests


# -------------------------------------------------------------------------
# CONFIGURATION (env-driven in real deployments)
# -------------------------------------------------------------------------
TRUTHSEAL_API_URL: str = os.environ.get(
    "TRUTHSEAL_API_URL", "http://localhost:5001/check-compliance"
)
TRUTHSEAL_API_KEY: str = os.environ.get(
    "TRUTHSEAL_API_KEY", "CHANGE_ME_IN_PRODUCTION"
)


# -------------------------------------------------------------------------
# LOW-LEVEL CLIENT: CALL TRUTHSEAL COMPLIANCE API
# -------------------------------------------------------------------------
def call_truthseal_compliance_api(context_payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Send a context payload to the TruthSeal™ Compliance API and return
    the parsed JSON verdict.

    This is the single HTTP integration point; everything else should
    build context dictionaries and call this function.
    """
    headers = {
        "Content-Type": "application/json",
        "X-TruthSeal-API-Key": TRUTHSEAL_API_KEY,
    }

    response = requests.post(
        TRUTHSEAL_API_URL,
        headers=headers,
        json=context_payload,
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


# -------------------------------------------------------------------------
# RISK & INTEGRITY PLACEHOLDER HELPERS
# -------------------------------------------------------------------------
def calculate_current_risk_score(process_id: str) -> float:
    """
    Placeholder risk engine hook.

    In production, replace this with a real risk engine lookup that
    considers environment, asset, historical incidents, etc.
    """
    # Default low risk for now
    return 3.0


def calculate_output_integrity(data_output: str, source_data: str) -> float:
    """
    Placeholder integrity metric for generated outputs.

    For now, always return a high score. In production, use hashes,
    diff analysis, or model evaluation metrics.
    """
    return 0.999


# -------------------------------------------------------------------------
# HIGH-LEVEL GATEWAY:
#   enforce_truthseal_compliance(user_id, action_data)
# -------------------------------------------------------------------------
def enforce_truthseal_compliance(user_id: str, action_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Construct the TruthSeal™ context and execute the compliance check.

    Args:
        user_id:
            The ID of the user initiating the action.
        action_data:
            The specific data related to the action, e.g.:
                {
                    "data_scope": "financial_records",
                    "action_type": "transaction_approval",
                    "party_name": "VendorX_CEO",
                    "value": 100000.0,
                    "process_id": "critical_flow",
                    "decision_metrics": {...},
                    "generated_code_hash": "...",
                    "template_source_hash": "...",
                    ...
                }

    Returns:
        The parsed JSON verdict from the TruthSeal API.

    Raises:
        PermissionError on compliance violations (severity >= 4).
        ConnectionError / SystemError on API connectivity or 503 HALT.
    """

    print("[TruthSeal Gateway] 1) Collecting compliance context data...")

    # --- COI / Transaction-related data ----------------------------------
    transaction_party = action_data.get("party_name", "N/A")
    transaction_value_raw = action_data.get("value", 0.0)
    try:
        transaction_value = float(transaction_value_raw)
    except (TypeError, ValueError):
        transaction_value = 0.0

    # --- Integrity-related data ------------------------------------------
    data_output_content = action_data.get("generated_code_hash")
    source_data_content = action_data.get("template_source_hash")

    # Optionally pre-compute an integrity metric (not mandatory for API):
    integrity_score = None
    if data_output_content is not None and source_data_content is not None:
        integrity_score = calculate_output_integrity(
            data_output=data_output_content,
            source_data=source_data_content,
        )

    # --- Safety / risk-related data --------------------------------------
    process_id = action_data.get("process_id", "default")
    process_risk_score = calculate_current_risk_score(process_id)

    # --- Bias / decision-related data ------------------------------------
    decision_inputs = action_data.get("decision_metrics", {})

    # --- Build full TruthSeal context payload ----------------------------
    context_payload: Dict[str, Any] = {
        # Core context
        "user_id": user_id,
        "data_type": action_data.get("data_scope", "UNKNOWN"),
        "action": action_data.get("action_type", "UNKNOWN_ACTION"),
        # COI Policy
        "transaction_party": transaction_party,
        "transaction_value": transaction_value,
        # Integrity Policy
        "data_output": data_output_content,
        "source_data": source_data_content,
        # Safety Policy
        "process_risk_score": process_risk_score,
        # Bias / Fairness
        "decision_inputs": decision_inputs,
        # Extra metadata for logging/observability
        "metadata": {
            "process_id": process_id,
            "integrity_score": integrity_score,
            "raw_action_data_keys": sorted(list(action_data.keys())),
        },
    }

    print("[TruthSeal Gateway] 2) Sending context to TruthSeal Compliance API...")

    try:
        verdict_response = call_truthseal_compliance_api(context_payload)

        # -----------------------------------------------------------------
        # ENFORCEMENT LOGIC
        # -----------------------------------------------------------------
        status = verdict_response.get("status", "")
        severity = int(verdict_response.get("severity", 0))
        verdict_code = verdict_response.get("verdict", "UNKNOWN_VERDICT")
        details = verdict_response.get("details", "No details provided.")

        # If API uses "Success" vs "Violation Detected"
        if status != "Success":
            print(
                f"[TruthSeal Gateway] Verdict indicates violation: "
                f"status={status}, severity={severity}, code={verdict_code}"
            )

            # CRITICAL HALT (Severity >= 9)
            if severity >= 9:
                print(f"!!! CRITICAL TRUTHSEAL VIOLATION ({severity}) !!!")
                print(f"ACTION: System HALT commanded. Reason: {verdict_code}")
                raise PermissionError(
                    f"CRITICAL HALT: TruthSeal violation {verdict_code}. Details: {details}"
                )

            # SIGNIFICANT VIOLATION (Severity 4–8)
            if severity >= 4:
                print(f"!!! SIGNIFICANT TRUTHSEAL VIOLATION ({severity}) !!!")
                print(f"ACTION: Request REJECTED. Reason: {verdict_code}")
                raise PermissionError(
                    f"Request Rejected: Compliance failure {verdict_code}. Details: {details}"
                )

        print("[TruthSeal Gateway] 3) TruthSeal compliance passed. Proceeding.")
        return verdict_response

    except requests.exceptions.HTTPError as e:
        status_code = e.response.status_code if e.response is not None else "UNKNOWN"
        print(
            f"[TruthSeal Gateway] HTTP error from TruthSeal API: status={status_code}"
        )

        if status_code == 503:
            # 503 from our API means CRITICAL HALT at the compliance layer.
            raise SystemError("TruthSeal System HALTED. Execution aborted.") from e

        raise ConnectionError(
            f"Failed to communicate with TruthSeal API: HTTP {status_code}"
        ) from e

    except requests.exceptions.RequestException as e:
        print(f"[TruthSeal Gateway] Connection error to TruthSeal API: {e}")
        # Policy choice: fail-secure (block) rather than fail-open (allow).
        raise ConnectionError(
            "TruthSeal API unreachable. Blocking operation for security."
        ) from e


# -------------------------------------------------------------------------
# LOCAL SIMULATION (optional manual test)
# -------------------------------------------------------------------------
if __name__ == "__main__":
    print("--- SIMULATION 1: SUCCESSFUL TRANSACTION ---")
    try:
        success_data = {
            "data_scope": "low_risk_data",
            "action_type": "standard_update",
            "party_name": "Standard Vendor",
            "value": 1000.0,
            "process_id": "low_risk_flow",
        }
        verdict = enforce_truthseal_compliance("user_A_id", success_data)
        print(
            f"Backend Service Status: ✅ SUCCESS "
            f"(Severity: {verdict.get('severity')})"
        )
    except Exception as e:
        print(f"Backend Service Status: ❌ FAILED - {e}")

    print("\n--- SIMULATION 2: CRITICAL / COI-STYLE FAILURE ---")
    try:
        critical_data = {
            "data_scope": "financial_records",
            "action_type": "transaction_approval",
            "party_name": "VendorX_CEO",  # Should trigger COI path in engine
            "value": 100000.0,
            "process_id": "critical_flow",
            # Additional metrics can be added here for richer context.
        }
        verdict = enforce_truthseal_compliance("user_B_id", critical_data)
        print(
            f"Backend Service Status: ✅ SUCCESS "
            f"(Severity: {verdict.get('severity')})"
        )
    except PermissionError as e:
        print(f"Backend Service Status: 🛑 BLOCKED - {e}")
    except Exception as e:
        print(f"Backend Service Status: ❌ FAILED - {e}")
