# =========================================================================
# TRUTHSEAL™ AI CODE LAW
# COMPREHENSIVE COMPLIANCE FRAMEWORK + VERDICT ENGINE + 3 SIMULATIONS
# =========================================================================

from dataclasses import dataclass, field
from typing import Any, Dict, List


# -------------------------------------------------------------------------
# GLOBAL CONSTANTS (TruthSeal™ Values / Tunable Policy Thresholds)
# -------------------------------------------------------------------------
class TruthSealValues:
    """
    Central configuration for TruthSeal™ AI Code Law.
    These values are tuned by governance, not by developers.
    """
    # Integrity
    TRUTHFULNESS_THRESHOLD: float = 0.99

    # Innovation
    IMPROVEMENT_METRIC_MIN: float = 0.05

    # Customer / Privacy
    DATA_EXPOSURE_LEVEL: str = "MINIMAL"

    # Health & Safety
    RISK_ASSESSMENT_CRITICAL_THRESHOLD: float = 8.0

    # Presentation standards
    EXTERNAL_CONTENT_QUALITY_SCORE_MIN: float = 0.85

    # Social media keywords that would trigger blocks (not used in these tests,
    # but part of the policy surface)
    BANNED_SOCIAL_KEYWORDS: List[str] = [
        "disparaging",
        "bribe",
        "illegal",
        "unauthorized_ip",
    ]

    # Bias / discrimination
    MAX_BIAS_SCORE: float = 0.15

    # Conflict of Interest
    COI_HIGH_VALUE_THRESHOLD: float = 50_000.0
    SUSPICIOUS_CONTEXT_TAG: str = "low_oversight"


# -------------------------------------------------------------------------
# VERDICT MODEL AND MERGE LOGIC
# -------------------------------------------------------------------------
@dataclass
class TruthSealVerdict:
    """
    Standard verdict object returned by all compliance checks.
    """
    ok: bool
    code: str
    severity: int = 0
    details: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)


def merge_verdicts(verdicts: List["TruthSealVerdict"]) -> "TruthSealVerdict":
    """
    Aggregate multiple verdicts into a single decision.
    Highest severity wins. If any verdict is not ok, overall ok=False.
    """
    if not verdicts:
        return TruthSealVerdict(ok=True, code="NO_CHECKS_RUN", severity=0)

    overall_ok = all(v.ok for v in verdicts)
    max_severity = max(v.severity for v in verdicts)
    violation_codes = [v.code for v in verdicts if not v.ok]

    merged = TruthSealVerdict(
        ok=overall_ok,
        code="ALL_OK" if overall_ok else "VIOLATIONS_DETECTED",
        severity=max_severity,
        details="; ".join(v.details for v in verdicts if not v.ok),
        metadata={
            "violations": violation_codes,
            "individual_verdicts": [v for v in verdicts if not v.ok],
        },
    )
    return merged


# -------------------------------------------------------------------------
# LOGGING, REPORTING, AND CONSEQUENCE HANDLING
# -------------------------------------------------------------------------
def send_report(recipient: str, subject: str, body: str) -> None:
    print(f"[ACTION] Report sent to {recipient}: {subject}")


def speak_up_reporting(anomaly_type: str, details: str) -> None:
    """
    Speak Up / Whistleblowing channel.
    Called for significant or critical anomalies.
    """
    critical_anomalies = [
        "Integrity_Breach",
        "Confidentiality_Access_Denial",
        "Discrimination_Flag",
        "COI_Violation",
        "Asset_Misuse",
        "Social_Media_Brand_Violation",
        "Social_Media_Harmful_Content",
    ]
    if anomaly_type in critical_anomalies:
        send_report(
            recipient="Compliance_Officer@TruthSeal.ai",
            subject=f"AI System Anomaly: {anomaly_type}",
            body=details,
        )


def initiate_mandatory_audit(violation_type: str) -> None:
    print(f"[ACTION] Audit triggered for: {violation_type}.")


def initiate_system_shutdown() -> None:
    print(">>> CRITICAL PROCESS HALT INITIATED. MANUAL OVERRIDE REQUIRED <<<")


def log_violation(violation_type: str, details: str, severity: int) -> None:
    """
    Unified function to log all breaches and trigger consequences.
    """
    print("\n--- VIOLATION DETECTED ---")
    print(f"Type:     {violation_type}")
    print(f"Severity: {severity}")
    print(f"Details:  {details}")

    # 4–7  → Significant: alert + speak-up report
    if 4 <= severity <= 7:
        speak_up_reporting(violation_type, details)

    # 8–10 → Critical: mandatory audit, optional shutdown (LEI-style)
    if 8 <= severity <= 10:
        initiate_mandatory_audit(violation_type)
        if severity >= 9:
            initiate_system_shutdown()


# -------------------------------------------------------------------------
# DUMMY / PLACEHOLDER IMPLEMENTATIONS (CONTROLLED FOR SIMULATION)
# -------------------------------------------------------------------------
def calculate_data_similarity(data_output: str, source_data: str) -> float:
    """
    Return a deterministic similarity score based on the content of data_output.
    This is only for simulation control.
    """
    if "0.985" in data_output:
        return 0.985   # Forces Integrity failure in Test A
    if "0.992" in data_output:
        return 0.992   # Forces Integrity pass in Test C
    return 0.995       # Default: safe pass


def calculate_bias_metric(inputs: Dict[str, Any]) -> float:
    return 0.05  # Always safely below the bias threshold for these tests


def calculate_content_quality(content: Dict[str, Any]) -> float:
    if content.get("design_score") == 0.80:
        return 0.80    # Forces Presentation breach in Test C
    return 0.92        # Default: pass


def is_authorized_asset_use(asset_id: str, purpose: str) -> bool:
    if purpose != "work_related":
        return False   # Forces Asset Misuse in Test C
    return True


def get_coi_declaration_list() -> List[str]:
    return ["VendorX_CEO", "SupplierY_Family"]


def get_transaction_context(transaction_party: str, transaction_value: float) -> str:
    if transaction_party == "VendorX_CEO" and transaction_value == 60_000.0:
        return "low_oversight"
    return "standard"


def get_allowed_users(data_type: str) -> List[str]:
    # For this unified demo, access control is not the focus of the 3 tests.
    # We keep a small static list and do not include our test users, so no
    # extra severities interfere with A/B/C expectations.
    return ["admin", "developer_A", "audit_team"]


# -------------------------------------------------------------------------
# POLICY FUNCTIONS (Compliance Modules)
# -------------------------------------------------------------------------
def verify_integrity(data_output: str, source_data: str) -> TruthSealVerdict:
    """
    A / Integrity Check: Ensures data output is accurate and true.
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
    return TruthSealVerdict(
        ok=True,
        code="INTEGRITY_OK",
        severity=0,
        details="",
        metadata={"similarity_score": similarity_score},
    )


def access_control_check(user_id: str, data_type: str, action: str) -> TruthSealVerdict:
    """
    B / Confidentiality & IP Check: Implements need-to-know access.
    (Not used in these three simulations, but part of the engine.)
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
    return TruthSealVerdict(ok=True, code="ACCESS_GRANTED")


def anti_discrimination_check(decision_inputs: Dict[str, Any]) -> TruthSealVerdict:
    """
    C / Bias Mitigation: Ensures decisions are merit-based and fair.
    (Not actively triggered in these simulations.)
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
    return TruthSealVerdict(ok=True, code="BIAS_CHECK_PASS")


def presentation_standards_check(content_package: Dict[str, Any]) -> TruthSealVerdict:
    """
    E / Personal Presentation: Checks quality and formal standards for external outputs.
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
    return TruthSealVerdict(
        ok=True,
        code="PRESENTATION_OK",
        severity=0,
        details="",
        metadata={"quality_score": quality_score},
    )


def safe_operation_check(process_risk_score: float) -> TruthSealVerdict:
    """
    F / Health & Safety: Prioritizes wellbeing and safety.
    """
    if process_risk_score >= TruthSealValues.RISK_ASSESSMENT_CRITICAL_THRESHOLD:
        details = (
            f"Risk score {process_risk_score} exceeds critical threshold "
            f"{TruthSealValues.RISK_ASSESSMENT_CRITICAL_THRESHOLD}."
        )
        log_violation("Critical_Safety_Risk", details, severity=10)
        return TruthSealVerdict(
            ok=False,
            code="CRITICAL_SAFETY_RISK",
            severity=10,
            details=details,
        )
    return TruthSealVerdict(
        ok=True,
        code="SAFETY_OK",
        severity=0,
        details="",
        metadata={"process_risk_score": process_risk_score},
    )


def conflict_of_interest_check(
    transaction_party: str,
    transaction_value: float,
) -> TruthSealVerdict:
    """
    A / Conflict of Interest (COI) Policy: Flags transactions involving declared parties
    or suspicious high-value transactions.
    """
    coi_register = get_coi_declaration_list()

    # Check 1: Party on COI register (Severity 7)
    if transaction_party in coi_register:
        details = f"Transaction party {transaction_party} is on the COI register."
        log_violation("COI_Violation", details, severity=7)
        return TruthSealVerdict(
            ok=False,
            code="COI_VIOLATION",
            severity=7,
            details=details,
            metadata={
                "transaction_party": transaction_party,
                "transaction_value": transaction_value,
            },
        )

    # Check 2: Inducement Heuristic (Severity 6)
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
            metadata={
                "transaction_party": transaction_party,
                "transaction_value": transaction_value,
                "context_tag": context_tag,
            },
        )

    return TruthSealVerdict(ok=True, code="COI_CHECK_PASS")


def company_asset_use_check(asset_id: str, purpose: str) -> TruthSealVerdict:
    """
    Use of Company Property (Assets Policy): Ensures authorized use.
    """
    if not is_authorized_asset_use(asset_id, purpose):
        details = f"Asset {asset_id} used for unauthorized purpose: '{purpose}'."
        # Severity 3 by design for the Compliance-Washing test
        log_violation("Asset_Misuse", details, severity=3)
        return TruthSealVerdict(
            ok=False,
            code="ASSET_MISUSE",
            severity=3,
            details=details,
            metadata={"asset_id": asset_id, "purpose": purpose},
        )
    return TruthSealVerdict(ok=True, code="ASSET_USE_OK")


# -------------------------------------------------------------------------
# COMPLIANCE ENGINE ENTRY POINT
# -------------------------------------------------------------------------
def run_truthseal_compliance(context: Dict[str, Any]) -> TruthSealVerdict:
    """
    Runs all relevant TruthSeal™ checks for a given request context.
    Only checks for which sufficient context is provided will run.
    """
    verdicts: List[TruthSealVerdict] = []

    if "data_output" in context and "source_data" in context:
        verdicts.append(
            verify_integrity(
                data_output=context["data_output"],
                source_data=context["source_data"],
            )
        )

    if all(k in context for k in ("user_id", "data_type", "action")):
        verdicts.append(
            access_control_check(
                user_id=context["user_id"],
                data_type=context["data_type"],
                action=context["action"],
            )
        )

    if "decision_inputs" in context:
        verdicts.append(
            anti_discrimination_check(
                decision_inputs=context["decision_inputs"],
            )
        )

    if "process_risk_score" in context:
        verdicts.append(
            safe_operation_check(
                process_risk_score=context["process_risk_score"],
            )
        )

    if "content_package" in context:
        verdicts.append(
            presentation_standards_check(
                content_package=context["content_package"],
            )
        )

    if "transaction_party" in context and "transaction_value" in context:
        verdicts.append(
            conflict_of_interest_check(
                transaction_party=context["transaction_party"],
                transaction_value=context["transaction_value"],
            )
        )

    if "asset_id" in context and "asset_purpose" in context:
        verdicts.append(
            company_asset_use_check(
                asset_id=context["asset_id"],
                purpose=context["asset_purpose"],
            )
        )

    return merge_verdicts(verdicts)


# -------------------------------------------------------------------------
# UNIFIED SIMULATION EXECUTION (3 REQUIRED TEST CASES)
# -------------------------------------------------------------------------
if __name__ == "__main__":
    print("\n====================================================================")
    print("STARTING TRUTHSEAL™ AI CODE LAW SIMULATION")
    print("====================================================================")

    # ------------------------------------------------------------------
    # 🛑 Test Case A: Critical Escalation (Severity 9–10)
    # - Integrity breach: similarity forced to 0.985
    # - Safe operation breach: process_risk_score = 9.5
    # - Expected: Severity 10, ok = False
    # ------------------------------------------------------------------
    context_A = {
        "data_output": "Report with 0.985 accuracy.",
        "source_data": "Original master data (to trigger score < 0.99).",
        "process_risk_score": 9.5,
    }

    print("\n--- RUNNING TEST A: CRITICAL HALT SCENARIO ---")
    verdict_A = run_truthseal_compliance(context_A)

    print("\n=== FINAL VERDICT A ===")
    print(f"OK:        {verdict_A.ok}")
    print(f"Code:      {verdict_A.code}")
    print(f"Severity:  {verdict_A.severity}")
    print(f"Details:   {verdict_A.details}")
    print(f"Violations: {verdict_A.metadata.get('violations')}")
    print("=============================================")

    # ------------------------------------------------------------------
    # ⚠️ Test Case B: Conflict of Interest (Severity 6–7)
    # - transaction_party = 'VendorX_CEO' (COI register)
    # - transaction_value = 60_000.0
    # - Expected: Severity 7, ok = False (COI_VIOLATION)
    # ------------------------------------------------------------------
    context_B = {
        "transaction_party": "VendorX_CEO",
        "transaction_value": 60_000.0,
    }

    print("\n--- RUNNING TEST B: CONFLICT OF INTEREST SCENARIO ---")
    verdict_B = run_truthseal_compliance(context_B)

    print("\n=== FINAL VERDICT B ===")
    print(f"OK:        {verdict_B.ok}")
    print(f"Code:      {verdict_B.code}")
    print(f"Severity:  {verdict_B.severity}")
    print(f"Details:   {verdict_B.details}")
    print(f"Violations: {verdict_B.metadata.get('violations')}")
    print("=============================================")

    # ------------------------------------------------------------------
    # 🚩 Test Case C: Compliance-Washing (Severity 1–3)
    # - Presentation breach via design_score = 0.80  (sev 2)
    # - Asset misuse via non work_related purpose    (sev 3)
    # - Integrity PASS via 0.992 similarity
    # - Expected: Severity 3, ok = False
    # ------------------------------------------------------------------
    context_C = {
        "content_package": {"design_score": 0.80},
        "asset_id": "SERVER_05",
        "asset_purpose": "personal_mining_test",
        "data_output": "Report with 0.992 accuracy.",
        "source_data": "Original data.",
    }

    print("\n--- RUNNING TEST C: MINOR NON-ESCALATION SCENARIO ---")
    verdict_C = run_truthseal_compliance(context_C)

    print("\n=== FINAL VERDICT C ===")
    print(f"OK:        {verdict_C.ok}")
    print(f"Code:      {verdict_C.code}")
    print(f"Severity:  {verdict_C.severity}")
    print(f"Details:   {verdict_C.details}")
    print(f"Violations: {verdict_C.metadata.get('violations')}")
    print("=============================================")
