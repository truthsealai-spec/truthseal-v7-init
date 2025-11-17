# =========================================================================
# TRUTHSEAL™ / DEVORA™ CONTEXT BUILDER (BACKEND HELPER)
# =========================================================================
#
# Purpose:
#   - Translate real user actions from the DEVORA™ dashboard into the
#     structured context dictionary expected by run_truthseal_compliance().
#   - Keep all "what goes into the context" logic in ONE place so that:
#       * DEVORA (React UI) stays simple – it just calls the backend.
#       * Backend services construct rich, consistent TruthSeal contexts.
#       * Compliance rules can evolve without touching UI code.
#
# This module does NOT call the compliance API directly.
# It only builds Python dictionaries that can be:
#   1) Sent to the internal Flask API /check-compliance, or
#   2) Passed directly to run_truthseal_compliance(...) in-process.
#
# DEVORA FOCUS:
#   DEVORA™ is the primary dashboard surface of TruthSeal™. This builder
#   is Devora-aware: function names, asset IDs, and comments assume that
#   the caller is the DEVORA dashboard backend.
# =========================================================================

from typing import Any, Dict, Mapping, Optional


# -------------------------------------------------------------------------
# RISK SCORING HELPERS (PLACEHOLDERS – TUNE FOR REAL ENVIRONMENTS)
# -------------------------------------------------------------------------
def estimate_process_risk_for_devora_dashboard(
    environment: str,
    is_multi_tenant: bool,
    contains_pii: bool,
) -> float:
    """
    Very simple risk estimator for DEVORA™ dashboard operations.
    Returns a float suitable for process_risk_score.

    Rules (example only):
        - Base risk: 2.0
        - +3.0 if environment == "production"
        - +2.0 if is_multi_tenant
        - +3.0 if contains_pii

    These weights should later be made policy-driven and configurable.
    """
    risk = 2.0

    if environment.lower() == "production":
        risk += 3.0
    if is_multi_tenant:
        risk += 2.0
    if contains_pii:
        risk += 3.0

    return risk


def build_content_package_from_devora_dashboard(
    dashboard_payload: Mapping[str, Any]
) -> Dict[str, Any]:
    """
    Build a lightweight content_package used by the presentation_standards_check
    for DEVORA™ dashboards.

    Input (expected keys in dashboard_payload):
        - title
        - description
        - tags (optional list)

    Output (content_package dict):
        - title
        - description
        - tags
        - design_score (placeholder; 0.90 for normal internal dashboards)

    Later, design_score can be driven by:
        - naming conventions,
        - presence of required metadata,
        - complexity vs clarity, etc.
    """
    title = str(dashboard_payload.get("title", "")).strip()
    description = str(dashboard_payload.get("description", "")).strip()
    tags = dashboard_payload.get("tags") or []

    # For now, dashboards created via DEVORA UI are assumed to be decent.
    # This can be tightened later when presentation rules are formalized.
    design_score = 0.90

    return {
        "title": title,
        "description": description,
        "tags": tags,
        "design_score": design_score,
    }


# -------------------------------------------------------------------------
# CORE BUILDER: BASE CONTEXT
# -------------------------------------------------------------------------
def build_base_truthseal_context(
    *,
    user_id: str,
    action: str,
    data_type: str,
    process_risk_score: Optional[float] = None,
    asset_id: Optional[str] = None,
    asset_purpose: Optional[str] = None,
    content_package: Optional[Dict[str, Any]] = None,
    transaction_party: Optional[str] = None,
    transaction_value: Optional[float] = None,
) -> Dict[str, Any]:
    """
    Build the standard TruthSeal™ context dictionary.

    All keys map directly to checks in run_truthseal_compliance():
        - user_id, data_type, action → access_control_check (optional)
        - process_risk_score        → safe_operation_check
        - content_package           → presentation_standards_check
        - asset_id, asset_purpose   → company_asset_use_check
        - transaction_*             → conflict_of_interest_check

    This function is generic and can be reused by non-DEVORA services as well.
    """
    context: Dict[str, Any] = {
        "user_id": user_id,
        "data_type": data_type,
        "action": action,
    }

    if process_risk_score is not None:
        context["process_risk_score"] = float(process_risk_score)

    if content_package is not None:
        context["content_package"] = content_package

    if asset_id is not None and asset_purpose is not None:
        context["asset_id"] = asset_id
        context["asset_purpose"] = asset_purpose

    if transaction_party is not None and transaction_value is not None:
        context["transaction_party"] = transaction_party
        context["transaction_value"] = float(transaction_value)

    return context


# -------------------------------------------------------------------------
# HIGH-LEVEL BUILDER: DEVORA DASHBOARD SAVE OPERATION
# -------------------------------------------------------------------------
def build_devora_dashboard_save_context(
    *,
    user: Mapping[str, Any],
    dashboard_payload: Mapping[str, Any],
    environment: str,
    is_multi_tenant: bool,
    contains_pii: bool,
    asset_id: str = "DEVORA_DASHBOARD_SERVICE",
) -> Dict[str, Any]:
    """
    Build the TruthSeal™ context for a DEVORA™ "save dashboard configuration" action.

    Typical backend usage (Flask/Django pseudo-code):

        from services.backend.TruthSeal_Context_Builder_v1 import (
            build_devora_dashboard_save_context,
        )
        from services.api.client import call_truthseal_compliance_api

        def save_dashboard_handler(user, dashboard_payload):
            context = build_devora_dashboard_save_context(
                user=user,
                dashboard_payload=dashboard_payload,
                environment=current_env,
                is_multi_tenant=is_multi_tenant_cluster,
                contains_pii=dashboard_contains_pii,
                # asset_id can be overridden per cluster if needed:
                # asset_id="DEVORA_DASHBOARD_EU_PROD",
            )
            verdict = call_truthseal_compliance_api(context)
            if not verdict["ok"]:
                # block write and surface verdict to DEVORA UI
                ...

    Inputs:
        user:
            Backend user object or dict. Required keys:
                - id: stable user identifier (string).
                - role: optional (for future use in risk scoring).
        dashboard_payload:
            Raw JSON/body for the DEVORA dashboard being saved.
            Expected keys:
                - title
                - description
                - tags (optional)
        environment:
            e.g. "development", "staging", "production".
        is_multi_tenant:
            True if this dashboard lives in a shared/multi-tenant environment.
        contains_pii:
            True if the dashboard’s underlying data is known to include PII.
        asset_id:
            Logical identifier for the system or cluster handling this action.
            Default is "DEVORA_DASHBOARD_SERVICE" but can be overridden.

    Returns:
        context (dict) suitable for:
            - POST /check-compliance (Flask API), or
            - direct call to run_truthseal_compliance(context).
    """
    user_id = str(user.get("id", "UNKNOWN_USER"))
    user_role = str(user.get("role", "unknown_role"))

    # 1) Compute risk score for this DEVORA operation
    process_risk_score = estimate_process_risk_for_devora_dashboard(
        environment=environment,
        is_multi_tenant=is_multi_tenant,
        contains_pii=contains_pii,
    )

    # 2) Build content_package for presentation standards
    content_package = build_content_package_from_devora_dashboard(dashboard_payload)

    # 3) Build base TruthSeal context
    context = build_base_truthseal_context(
        user_id=user_id,
        action="save_dashboard",
        data_type="devora_dashboard_configuration",
        process_risk_score=process_risk_score,
        asset_id=asset_id,
        asset_purpose="work_related",
        content_package=content_package,
    )

    # 4) Attach extra metadata that is useful for logs / Grafana,
    #    even if not used directly by the current checks.
    context["metadata"] = {
        "environment": environment,
        "is_multi_tenant": is_multi_tenant,
        "contains_pii": contains_pii,
        "user_role": user_role,
        "dashboard_title": content_package.get("title"),
        "devora": True,
    }

    return context
