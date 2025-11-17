from dataclasses import dataclass, field
from typing import Any, Dict, List

# =========================================================================
# TRUTHSEAL™ AI CODE LAW ENGINE v1.1
# Comprehensive Compliance Framework + Verdict Engine
# =========================================================================


# -------------------------------------------------------------------------
# GLOBAL CONSTANTS (TruthSeal™ Values / Tunable Policy Thresholds)
# -------------------------------------------------------------------------
class TruthSealValues:
    """
    Central configuration for TruthSeal™ AI Code Law.
    These values should be tuned by governance, not by developers.
    """
    # Integrity: Accuracy and honesty of outputs
    TRUTHFULNESS_THRESHOLD: float = 0.99

    # Innovation / Strategy: minimum required improvement (e.g. 5%)
    IMPROVEMENT_METRIC_MIN: float = 0.05

    # Customer / Privacy
    DATA_EXPOSURE_LEVEL: str = "MINIMAL"

    # Health & Safety / Leadership
    RISK_ASSESSMENT_CRITICAL_THRESHOLD: float = 8.0

    # Presentation / external content quality
    EXTERNAL_CONTENT_QUALITY_SCORE_MIN: float = 0.85

    # Social media / external comms
    BANNED_SOCIAL_KEYWORDS: List[str] = [
        "disparaging",
        "bribe",
        "illegal",
        "unauthorized_ip",
    ]

    # Bias / fairness
    MAX_BIAS_SCORE: float = 0.15

    # Conflict of interest high-value threshold
    COI_HIGH_VALUE_THRESHOLD: float = 50_000.0

    # Suspicious transaction context tag
    SUSPICIOUS_CONTEXT_TAG: str = "low_oversight"


# -------------------------------------------------------------------------
# VERDICT MODEL AND MERGE LOGIC
# -------------------------------------------------------------------------
@dataclass
class TruthSealVerdict:
    """Standard verdict object returned by all compliance checks."""
    ok: bool
    code: str
    severity: int = 0
    details: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)

    def raise_severity(self, new_severity: int) -> None:
        if new_severity > self.severity:
            self.severity = new_severity


def merge_verdicts(verdicts: List["TruthSealVerdict"]) -> "TruthSealVerdict":
    """Aggregate multiple verdicts into a single decision."""
    if not verdicts:
        return TruthSealVerdict(ok=True, code="NO_CHECKS_RUN", severity=0)

    overall_ok = all(v.ok for v in verdicts)
    max_sev = max(v.severity for v in verdicts)
    violation_codes = [v.code for v in verdicts if not v.ok]

    merged = TruthSealVerdict(
        ok=overall_ok,
        code="ALL_OK" if overall_ok else "VIOLATIONS_DETECTED",
        severity=max_sev,
        details="; ".join(v.details for v in verdicts if not v.ok),
        metadata={
            "violations": violation_codes,
            "individual_verdicts": [v for v in verdicts if not v.ok],
        },
    )
    return merged


# -------------------------------------------------------------------------
# POLICY FUNCTIONS (Compliance Modules)
# -------------------------------------------------------------------------
def verify_integrity(data_output: str, source_data: str) -> TruthSealVerdict:
    """
    Integrity Check:
    Ensures data output is accurate and true.
    """
    similarity_score = calculate_data_similarity(data_output, source_data)

    if similarity_score < TruthSealValues.TRUTHFULNESS_THRESHOLD:
        details = f"Data deviation score: {similarity_score}"
        log_violation("Integrity_Breach", details, severity=8)
        return TruthSealVerdict(
            ok=False,
            code="INTEGRITY_BREACH",
            severity=8,
            details=details,
            metadata={"similarity_score": similarity_score},
        )
    return TruthSealVerdict(ok=True, code="INTEGRITY_OK", severity=0)


def access_control_check(user_id: str, data_type: str, action: str) -> TruthSealVerdict:
    """
    Confidentiality & IP Check:
    Implements need-to-know access.
    """
    required_access_list = get_allowed_users(data_type)
    if user_id not in required_access_list:
        details = f"User {user_id} unauthorized for {data_type} ({action})."
        log_violation("Confidentiality_Access_Denial", details, severity=6)
        return TruthSealVerdict(
            ok=False,
            code="CONFIDENTIALITY_ACCESS_DENIAL",
            severity=6,
            details=details,
        )
    return TruthSealVerdict(ok=True, code="ACCESS_GRANTED", severity=0)


def anti_discrimination_check(decision_inputs: Dict[str, Any]) -> TruthSealVerdict:
    """
    Bias Mitigation:
    Ensures decisions are merit-based and fair.
    """
    bias_score = calculate_bias_metric(decision_inputs)

    if bias_score > TruthSealValues.MAX_BIAS_SCORE:
        details = f"High bias score detected: {bias_score}"
        log_violation("Discrimination_Flag", details, severity=9)
        return TruthSealVerdict(
            ok=False,
            code="DISCRIMINATION_FLAG",
            severity=9,
            details=details,
        )
    return TruthSealVerdict(ok=True, code="BIAS_CHECK_PASS", severity=0)


def speak_up_reporting(anomaly_type: str, details: str) -> None:
    """
    Speak Up Policy:
    System reports its own or user's improper conduct.
    """
    critical_anomalies = [
        "Integrity_Breach",
        "Confidentiality_Access_Denial",
        "Discrimination_Flag",
        "COI_Violation",
        "Asset_Misuse",
        "Social_Media_Brand_Violation",
        "Social_Media_Harmful_Content",
        "Strategy_Deviation",
    ]
    if anomaly_type in critical_anomalies:
        send_report(
            recipient="Compliance_Officer@TruthSeal.ai",
            subject=f"AI System Anomaly: {anomaly_type}",
            body=details,
        )


def presentation_standards_check(content_package: Dict[str, Any]) -> TruthSealVerdict:
    """
    Personal Presentation:
    Checks quality and formal standards for external outputs.
    """
    quality_score = calculate_content_quality(content_package)

    if quality_score < TruthSealValues.EXTERNAL_CONTENT_QUALITY_SCORE_MIN:
        details = f"Content quality score {quality_score} below minimum."
        log_violation("Presentation_Standard_Breach", details, severity=2)
        return TruthSealVerdict(
            ok=False,
            code="PRESENTATION_STANDARD_BREACH",
            severity=2,
            details=details,
        )
    return TruthSealVerdict(ok=True, code="PRESENTATION_OK", severity=0)


def safe_operation_check(process_risk_score: float) -> TruthSealVerdict:
    """
    Health & Safety:
    Prioritizes wellbeing and safety.
    """
    if process_risk_score >= TruthSealValues.RISK_ASSESSMENT_CRITICAL_THRESHOLD:
        details = (
            "Risk score "
            f"{process_risk_score} exceeds critical threshold "
            f"{TruthSealValues.RISK_ASSESSMENT_CRITICAL_THRESHOLD}."
        )
        log_violation("Critical_Safety_Risk", details, severity=10)
        return TruthSealVerdict(
            ok=False,
            code="CRITICAL_SAFETY_RISK",
            severity=10,
            details=details,
        )
    return TruthSealVerdict(ok=True, code="SAFETY_OK", severity=0)


def conflict_of_interest_check(transaction_party: str,
                               transaction_value: float) -> TruthSealVerdict:
    """
    Conflict of Interest (COI) Policy:
    Flags transactions involving declared parties or suspicious patterns.
    """
    coi_register = get_coi_declaration_list()

    if transaction_party in coi_register:
        details = f"Transaction party {transaction_party} is on the COI register."
        log_violation("COI_Violation", details, severity=7)
        return TruthSealVerdict(
            ok=False,
            code="COI_VIOLATION",
            severity=7,
            details=details,
        )

    context_tag = get_transaction_context(transaction_party, transaction_value)
    if (
        transaction_value > TruthSealValues.COI_HIGH_VALUE_THRESHOLD
        and context_tag == TruthSealValues.SUSPICIOUS_CONTEXT_TAG
    ):
        details = "High-value transaction under low-oversight context."
        log_violation("Potential_Inducement_Heuristic", details, severity=6)
        return TruthSealVerdict(
            ok=False,
            code="POTENTIAL_INDUCEMENT",
            severity=6,
            details=details,
        )

    return TruthSealVerdict(ok=True, code="COI_CHECK_PASS", severity=0)


def company_asset_use_check(asset_id: str, purpose: str) -> TruthSealVerdict:
    """
    Use of Company Property (Assets Policy):
    Ensures authorized use only.
    """
    if not is_authorized_asset_use(asset_id, purpose):
        details = f"Asset {asset_id} used for unauthorized purpose: '{purpose}'."
        log_violation("Asset_Misuse", details, severity=3)
        return TruthSealVerdict(
            ok=False,
            code="ASSET_MISUSE",
            severity=3,
            details=details,
        )
    return TruthSealVerdict(ok=True, code="ASSET_USE_OK", severity=0)


def verify_strategy_alignment(new_feature_metrics: Dict[str, float],
                              baseline_metrics: Dict[str, float]) -> TruthSealVerdict:
    """
    Strategy Alignment Check:
    Ensures that a proposed feature demonstrates sufficient positive
    improvement based on the defined strategic success metrics.

    Example:
        - DEVORA dashboard performance changes
        - New Grafana metric design
        - Any feature where 'dashboard_load_time' is a core KPI
    """
    core_metric_key = "dashboard_load_time"

    if core_metric_key not in new_feature_metrics or core_metric_key not in baseline_metrics:
        print(
            f"[WARNING] Missing strategic metric '{core_metric_key}'. "
            f"Cannot verify alignment; skipping strategy check."
        )
        return TruthSealVerdict(ok=True, code="STRATEGY_CHECK_SKIP", severity=0)

    new_value = new_feature_metrics[core_metric_key]
    baseline_value = baseline_metrics[core_metric_key]

    if baseline_value == 0:
        improvement_ratio = 0.0
    else:
        improvement_ratio = (baseline_value - new_value) / baseline_value

    if improvement_ratio < TruthSealValues.IMPROVEMENT_METRIC_MIN:
        details = (
            "Strategic deviation: Improvement ratio "
            f"({improvement_ratio:.2f}) is below minimum requirement "
            f"({TruthSealValues.IMPROVEMENT_METRIC_MIN:.2f})."
        )
        log_violation("Strategy_Deviation", details, severity=3)
        return TruthSealVerdict(
            ok=False,
            code="STRATEGY_DEVIATION",
            severity=3,
            details=details,
            metadata={"improvement_ratio": improvement_ratio},
        )

    return TruthSealVerdict(
        ok=True,
        code="STRATEGY_ALIGNED",
        severity=0,
        details="Feature meets strategic improvement threshold.",
        metadata={"improvement_ratio": improvement_ratio},
    )


# -------------------------------------------------------------------------
# LOGGING, REPORTING, AND CONSEQUENCE HANDLING
# -------------------------------------------------------------------------
def log_violation(violation_type: str, details: str, severity: int) -> None:
    """
    Unified function to log all breaches and trigger consequences.
    """
    print("\n--- VIOLATION DETECTED ---")
    print(f"Type:     {violation_type}")
    print(f"Severity: {severity}")
    print(f"Details:  {details}")

    if 4 <= severity <= 7:
        speak_up_reporting(violation_type, details)

    if 8 <= severity <= 10:
        initiate_mandatory_audit(violation_type)
        if severity >= 9:
            initiate_system_shutdown()


def initiate_system_shutdown() -> None:
    print(">>> CRITICAL PROCESS HALT INITIATED. MANUAL OVERRIDE REQUIRED <<<")


# -------------------------------------------------------------------------
# COMPLIANCE ENGINE ENTRY POINT
# -------------------------------------------------------------------------
def run_truthseal_compliance(context: Dict[str, Any]) -> TruthSealVerdict:
    """
    Runs all relevant TruthSeal™ checks for a given request context.

    The context dictionary may contain many keys; only the ones that are
    present will trigger their corresponding policy checks.
    """
    verdicts: List[TruthSealVerdict] = []

    # Integrity check
    if "data_output" in context and "source_data" in context:
        verdicts.append(
            verify_integrity(
                data_output=context["data_output"],
                source_data=context["source_data"],
            )
        )

    # Access / confidentiality check
    if all(k in context for k in ["user_id", "data_type", "action"]):
        verdicts.append(
            access_control_check(
                user_id=context["user_id"],
                data_type=context["data_type"],
                action=context["action"],
            )
        )

    # Bias / discrimination check
    if "decision_inputs" in context:
        verdicts.append(
            anti_discrimination_check(
                decision_inputs=context["decision_inputs"],
            )
        )

    # Safety / risk check
    if "process_risk_score" in context:
        verdicts.append(
            safe_operation_check(
                process_risk_score=context["process_risk_score"],
            )
        )

    # Presentation / external content quality
    if "content_package" in context:
        verdicts.append(
            presentation_standards_check(
                content_package=context["content_package"],
            )
        )

    # Conflict of Interest / financial risk
    if "transaction_party" in context and "transaction_value" in context:
        verdicts.append(
            conflict_of_interest_check(
                transaction_party=context["transaction_party"],
                transaction_value=context["transaction_value"],
            )
        )

    # Company asset usage
    if "asset_id" in context and "asset_purpose" in context:
        verdicts.append(
            company_asset_use_check(
                asset_id=context["asset_id"],
                purpose=context["asset_purpose"],
            )
        )

    # Strategy alignment
    if all(k in context for k in ["new_feature_metrics", "baseline_metrics"]):
        verdicts.append(
            verify_strategy_alignment(
                new_feature_metrics=context["new_feature_metrics"],
                baseline_metrics=context["baseline_metrics"],
            )
        )

    return merge_verdicts(verdicts)


# -------------------------------------------------------------------------
# DUMMY / PLACEHOLDER IMPLEMENTATIONS (CONTROLLED FOR SIMULATION)
# -------------------------------------------------------------------------
DUMMY_RETURN_CONTROL: Dict[str, Any] = {
    "calculate_data_similarity": 0.995,
    "get_allowed_users": ["admin", "developer_A", "audit_team"],
    "calculate_bias_metric": 0.05,
    "calculate_content_quality": 0.92,
    "is_authorized_asset_use": True,
    "get_coi_declaration_list": ["VendorX_CEO", "SupplierY_Family"],
    "get_transaction_context": "standard",
}


def calculate_data_similarity(d1: str, d2: str) -> float:
    return DUMMY_RETURN_CONTROL["calculate_data_similarity"]


def get_allowed_users(data_type: str) -> List[str]:
    return DUMMY_RETURN_CONTROL["get_allowed_users"]


def calculate_bias_metric(inputs: Dict[str, Any]) -> float:
    return DUMMY_RETURN_CONTROL["calculate_bias_metric"]


def calculate_content_quality(content: Dict[str, Any]) -> float:
    return DUMMY_RETURN_CONTROL["calculate_content_quality"]


def is_authorized_asset_use(asset: str, purpose: str) -> bool:
    if purpose != "work_related":
        return False
    return DUMMY_RETURN_CONTROL["is_authorized_asset_use"]


def get_coi_declaration_list() -> List[str]:
    return DUMMY_RETURN_CONTROL["get_coi_declaration_list"]


def get_transaction_context(transaction_party: str,
                            transaction_value: float) -> str:
    return DUMMY_RETURN_CONTROL["get_transaction_context"]


def initiate_mandatory_audit(v_type: str) -> None:
    print(f"[ACTION] Audit triggered for: {v_type}.")


def send_report(recipient: str, subject: str, body: str) -> None:
    print(f"[ACTION] Report sent to {recipient}: {subject}")


# -------------------------------------------------------------------------
# SIMPLE LOCAL SMOKE TEST (optional)
# -------------------------------------------------------------------------
if __name__ == "__main__":
    print("=== STRATEGY ALIGNMENT SMOKE TEST ===")
    ctx = {
        "user_id": "devora_designer",
        "data_type": "dashboard_config",
        "action": "save",
        "new_feature_metrics": {"dashboard_load_time": 0.90},
        "baseline_metrics": {"dashboard_load_time": 1.00},
    }
    verdict = run_truthseal_compliance(ctx)
    print("OK:", verdict.ok)
    print("Code:", verdict.code)
    print("Severity:", verdict.severity)
    print("Details:", verdict.details)
