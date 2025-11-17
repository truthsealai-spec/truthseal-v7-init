# =========================================================================
# TRUTHSEAL™ COMPLIANCE API SERVICE (FLASK ENDPOINT)
# =========================================================================
#
# This file exposes the TruthSeal™ AI Code Law as a network-accessible API.
# It accepts a JSON "context" payload, runs run_truthseal_compliance(context),
# and returns a structured verdict.
#
# IMPORTANT:
# - This is a minimal service shell. In production, secrets must come from
#   environment variables / secret manager, not hard-coded.
# - Network exposure should be restricted (internal network / VPN / mTLS).
# =========================================================================

from flask import Flask, request, jsonify
import os

# Import the TruthSeal™ AI Code Law engine
# Adjust the import path if your module structure differs.
from governance.compliance.TruthSeal_AICodeLaw_Engine_v1 import (
    run_truthseal_compliance,
    TruthSealVerdict,
)

app = Flask(__name__)

# --- SECRETS AND CONFIGURATION -------------------------------------------

# In real use, this MUST come from env or secret manager:
#   export TRUTHSEAL_API_KEY="some-long-random-value"
API_KEY_SECRET = os.environ.get("TRUTHSEAL_API_KEY", "CHANGE_ME_IN_PRODUCTION")


# -------------------------------------------------------------------------
# HELPER: STANDARD ERROR RESPONSE
# -------------------------------------------------------------------------
def error_response(message: str, code: str, http_status: int):
    return jsonify(
        {
            "status": "Error",
            "error": message,
            "code": code,
        }
    ), http_status


# -------------------------------------------------------------------------
# API ENDPOINT: /check-compliance
# -------------------------------------------------------------------------
@app.route("/check-compliance", methods=["POST"])
def check_compliance_endpoint():
    """
    Accepts an operational context in JSON and returns the TruthSeal verdict.
    """
    # 1. SECURITY CHECK (Simple API key auth)
    api_key_header = request.headers.get("X-TruthSeal-API-Key")
    if not API_KEY_SECRET or API_KEY_SECRET == "CHANGE_ME_IN_PRODUCTION":
        # Misconfigured server-side secret
        return error_response(
            message="Server misconfigured: TRUTHSEAL_API_KEY not set.",
            code="SERVER_CONFIG_ERROR",
            http_status=500,
        )
    if api_key_header != API_KEY_SECRET:
        return error_response(
            message="Missing or invalid X-TruthSeal-API-Key.",
            code="AUTH_DENIED",
            http_status=401,
        )

    # 2. INPUT VALIDATION
    if not request.is_json:
        return error_response(
            message="Invalid request format. Expected JSON payload.",
            code="INVALID_FORMAT",
            http_status=400,
        )

    context_data = request.get_json()

    # Optional core checks (these can be relaxed or extended later)
    if not isinstance(context_data, dict):
        return error_response(
            message="Invalid payload. Expected a JSON object (dictionary).",
            code="INVALID_PAYLOAD",
            http_status=400,
        )

    # Example minimal core keys (can be expanded per policy):
    # If you want stricter enforcement, uncomment this block:
    #
    # required_keys = ["user_id", "action"]
    # missing = [k for k in required_keys if k not in context_data]
    # if missing:
    #     return error_response(
    #         message=f"Missing core context keys: {', '.join(missing)}",
    #         code="MISSING_CONTEXT",
    #         http_status=400,
    #     )

    try:
        # 3. RUN THE TRUTHSEAL™ AI CODE LAW
        final_verdict: TruthSealVerdict = run_truthseal_compliance(context_data)

        # 4. MAP VERDICT TO HTTP STATUS
        if final_verdict.severity >= 9:
            # Critical: tell caller to halt operation
            http_status = 503  # Service Unavailable (System Halted / Blocked)
            status_text = "Critical Violation"
        elif not final_verdict.ok:
            http_status = 403  # Forbidden (Policy violation)
            status_text = "Violation Detected"
        else:
            http_status = 200  # OK
            status_text = "Success"

        # 5. RETURN STRUCTURED VERDICT
        response_body = {
            "status": status_text,
            "ok": final_verdict.ok,
            "verdict": final_verdict.code,
            "severity": final_verdict.severity,
            "details": final_verdict.details,
            "metadata": final_verdict.metadata,
        }

        return jsonify(response_body), http_status

    except Exception as e:
        # 6. SAFETY NET: INTERNAL SERVER ERROR
        # In production, route this to a proper logger / SIEM.
        print(f"[TruthSeal API] ERROR processing request: {e}")
        return error_response(
            message="Internal server error.",
            code="INTERNAL_ERROR",
            http_status=500,
        )


# -------------------------------------------------------------------------
# SERVICE ENTRY POINT
# -------------------------------------------------------------------------
if __name__ == "__main__":
    # In production, you would typically run this behind gunicorn/uwsgi
    # and not enable debug mode.
    port = int(os.environ.get("TRUTHSEAL_API_PORT", "5001"))
    app.run(host="0.0.0.0", port=port, debug=False)
