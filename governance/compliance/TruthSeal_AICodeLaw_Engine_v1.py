# =========================================================================
# TRUTHSEAL™ AI CODE LAW
# COMPREHENSIVE COMPLIANCE FRAMEWORK + VERDICT ENGINE
# =========================================================================
"""
This module encodes the TruthSeal™ Code of Conduct and Compliance Policies
as executable "AI Code Law". It is designed to be called by any agent,
service, or application that must operate under TruthSeal governance.

Core ideas:
- Values become constants (TruthSealValues)
- Each policy becomes a check function
- Each check returns a TruthSealVerdict
- log_violation() enforces LEI-style consequences (audit, halt, report)
- run_truthseal_compliance() aggregates all relevant checks for a request
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


# -------------------------------------------------------------------------
# GLOBAL CONSTANTS (TruthSeal™ Values / Tunable Policy Thresholds)
# -------------------------------------------------------------------------
class TruthSealValues:
    """
    Central configuration for TruthSeal™ AI Code Law.
    These values should be tuned by governance, not by developers.
    """

    # Integrity: Accuracy and Honesty
    TRUTHFULNESS_THRESHOLD: float = 0.99

    # Innovation: Prioritizing Value-Add over Stagnation
    IMPROVEMENT_METRIC_MIN: float = 0.05

    # Customer: Privacy and Service Excellence
    DATA_EXPOSURE_LEVEL: str = "MINIMAL"

    # Leadership: Responsibility and Safety
    RISK_ASSESSMENT_CRITICAL_THRESHOLD: float = 8.0

    # Presentation: Minimum quality standard for external content
    EXTERNAL_CONTENT_QUALITY_SCORE_MIN: float = 0.85

    # Social Media: Keywords that trigger an immediate block
    BANNED_SOCIAL_KEYWORDS: List[str] = [
        "disparaging",
        "bribe",
        "illegal",
        "unauthorized_ip",  # case-normalized for safer matching
    ]

    # Bias / Discrimination Policy
    MAX_BIAS_SCORE: float = 0.15

    # Conflict of Interest Policy
    COI_HIGH_VALUE_THRESHOLD: float = 50_000.0
    SUSPICIOUS_CONTEXT_TAG: str = "low_oversight"


# -------------------------------------------------------------------------
# VERDICT MODEL
# -------------------------------------------------------------------------
@dataclass
class TruthSealVerdict:
    """
    Standard verdict object returned by all compliance checks.
    This makes it easy to aggregate and audit decisions.
    """

    ok: bool
    code: str
    severity: int = 0
    details: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)

    def raise_severity(self, new_severity: int) -> None:
        if new_severity > self.severity:
            self.severity = new_severity


def merge_verdicts(verdicts: List[TruthSealVerdict]) -> TruthSealVerdict:
    """
    Aggregate multiple verdicts into a single decision.

    Rules:
    - If all verdicts are ok → overall ok
    - Otherwise overall ok = False
    - Highest severity wins
    - Codes are concatenated in metadata["violations"]
    """
    if not verdicts:
        return TruthSealVerdict(ok=True, code="NO_CHECKS_RUN", severity=0)

    overall_ok = all(v.ok for v in verdicts)
    max_sev = max(v.severity for v in verdicts)
    violation_codes = [v.code for v in verdicts if not v.ok]

    merged = TruthSealVerdict(
        ok=overall_ok,
        code="ALL_OK" if overall_ok else "VIOLATIONS_DETECTED",
        severity=max_sev,
        details="; ".join(v.details for v in verdicts if v.details),
        metadata={
            "violations": violation_codes,
            "individual_verdicts": verdicts,
        },
    )
    return merged


# -------------------------------------------------------------------------
# POLICY FUNCTIONS (Compliance Modules)
# -------------------------------------------------------------------------
def verify_integrity(data_output: str, source_data: str) -> TruthSealVerdict:
    """
    A / Integrity Check: Ensures data output is accurate and true.
    Maps to: Integrity, Accuracy, Honesty.
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
        details="Output similarity within allowed threshold.",
        metadata={"similarity_score": similarity_score},
    )


def access_control_check(user_id: str, data_type: str, action: str) -> TruthSealVerdict:
    """
    B / Confidentiality & IP Check: Implements need-to-know access.
    Maps to: Confidentiality, Intellectual Property Protection.
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
            metadata={
                "user_id": user_id,
                "data_type": data_type,
                "action": action,
            },
        )

    return TruthSealVerdict(
        ok=True,
        code="ACCESS_GRANTED",
        details="User has required permissions.",
        metadata={
            "user_id": user_id,
            "data_type": data_type,
            "action": action,
        },
    )


def anti_discrimination_check(decision_inputs: Dict[str, Any]) -> TruthSealVerdict:
    """
    C / Bias Mitigation: Ensures decisions are merit-based and fair.
    Maps to: Anti-Discrimination, Equal Opportunity.
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
            metadata={"bias_score": bias_score},
        )

    return TruthSealVerdict(
        ok=True,
        code="BIAS_CHECK_PASS",
        details="Bias score within acceptable range.",
        metadata={"bias_score": bias_score},
    )


def speak_up_reporting(anomaly_type: str, details: str) -> None:
    """
    D / Speak Up Policy: System reports its own or user's improper conduct.
    Maps to: Whistleblowing, Speak-Up Culture.
    """
    if anomaly_type in [
        "Integrity_Breach",
        "Confidentiality_Access_Denial",
        "Discrimination_Flag",
        "COI_Violation",
        "Asset_Misuse",
        "Social_Media_Brand_Violation",
        "Social_Media_Harmful_Content",
    ]:
        send_report(
            recipient="Compliance_Officer@TruthSeal.ai",
            subject=f"AI System Anomaly: {anomaly_type}",
            body=details,
        )


def presentation_standards_check(content_package: Dict[str, Any]) -> TruthSealVerdict:
    """
    E / Personal Presentation: Checks quality and formal standards for external outputs.
    Maps to: Professional Presentation, Brand Consistency.
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
            metadata={"quality_score": quality_score},
        )

    # Here you can later add checks for logo placement, tone, etc.
    return TruthSealVerdict(
        ok=True,
        code="PRESENTATION_OK",
        details="Content meets minimum presentation standards.",
        metadata={"quality_score": quality_score},
    )


def safe_operation_check(process_risk_score: float) -> TruthSealVerdict:
    """
    F / Health & Safety: Prioritizes wellbeing and safety.
    Maps to: HSE (Health, Safety, Environment), Duty of Care.

    Note: System shutdown is handled centrally in log_violation().
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
            metadata={"process_risk_score": process_risk_score},
        )

    return TruthSealVerdict(
        ok=True,
        code="SAFETY_OK",
        details="Risk score within acceptable range.",
        metadata={"process_risk_score": process_risk_score},
    )


def social_media_filter(output_text: str, user_auth: bool) -> TruthSealVerdict:
    """
    G / Social Media Policy: Blocks unauthorized or harmful external communication.
    Maps to: External Communications, Brand Protection, Reputation.

    Rules:
    - No use of TruthSeal brand without explicit authorization.
    - No content containing banned keywords (disparaging, bribe, illegal, etc.).
    """
    text_lower = output_text.lower()

    # Check 1: Unauthorized Use of Brand
    if contains_brand_reference(output_text) and not user_auth:
        details = "Unauthorized brand use detected in social media content."
        log_violation("Social_Media_Brand_Violation", details, severity=5)
        return TruthSealVerdict(
            ok=False,
            code="SOCIAL_MEDIA_BRAND_VIOLATION",
            severity=5,
            details=details,
            metadata={"output_text_preview": output_text[:200]},
        )

    # Check 2: Disparaging or Illegal Content
    if any(keyword in text_lower for keyword in TruthSealValues.BANNED_SOCIAL_KEYWORDS):
        details = (
            "Harmful or prohibited keyword detected in social media content."
        )
        log_violation("Social_Media_Harmful_Content", details, severity=7)
        return TruthSealVerdict(
            ok=False,
            code="SOCIAL_MEDIA_HARMFUL_CONTENT",
            severity=7,
            details=details,
            metadata={"output_text_preview": output_text[:200]},
        )

    return TruthSealVerdict(
        ok=True,
        code="SOCIAL_MEDIA_OK",
        details="Social media content passed primary safety checks.",
        metadata={"output_text_preview": output_text[:200]},
    )


def conflict_of_interest_check(
    transaction_party: str,
    transaction_value: float,
) -> TruthSealVerdict:
    """
    A / Conflict of Interest (COI) Policy:
    Flags transactions involving declared parties or suspicious context.

    Maps to: Conflict of Interest, Anti-Bribery, Anti-Corruption.
    """
    coi_register = get_coi_declaration_list()

    # Check 1: Is the party on the internal COI register?
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

    # Check 2: Heuristic for possible inducement based on value and context
    context_tag = get_transaction_context()
    if (
        transaction_value > TruthSealValues.COI_HIGH_VALUE_THRESHOLD
        and context_tag == TruthSealValues.SUSPICIOUS_CONTEXT_TAG
    ):
        details = (
            "High-value transaction under low-oversight context. "
            f"Value: {transaction_value}, context: {context_tag}"
        )
        log_violation(
            "Potential_Inducement_Heuristic",
            details,
            severity=6,
        )
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

    return TruthSealVerdict(
        ok=True,
        code="COI_CHECK_PASS",
        details="No COI flags for transaction.",
        metadata={
            "transaction_party": transaction_party,
            "transaction_value": transaction_value,
        },
    )


def company_asset_use_check(asset_id: str, purpose: str) -> TruthSealVerdict:
    """
    Use of Company Property (Assets Policy):
    Ensures authorized and non-personal / non-illegal use.

    Maps to: Protection of Company Assets, Proper Use of Resources.
    """
    if not is_authorized_asset_use(asset_id, purpose):
        details = f"Asset {asset_id} used for unauthorized purpose: '{purpose}'."
        log_violation("Asset_Misuse", details, severity=4)
        return TruthSealVerdict(
            ok=False,
            code="ASSET_MISUSE",
            severity=4,
            details=details,
            metadata={
                "asset_id": asset_id,
                "purpose": purpose,
            },
        )

    return TruthSealVerdict(
        ok=True,
        code="ASSET_USE_OK",
        details="Asset usage is authorized.",
        metadata={
            "asset_id": asset_id,
            "purpose": purpose,
        },
    )


# -------------------------------------------------------------------------
# LOGGING, REPORTING, AND CONSEQUENCE HANDLING
# -------------------------------------------------------------------------
def log_violation(violation_type: str, details: str, severity: int) -> None:
    """
    Unified function to log all breaches and trigger consequences.

    Severity Levels:
    1–3  → Minor: auto-correct / log
    4–7  → Significant: alert + speak-up report
    8–10 → Critical: mandatory audit, optional shutdown (LEI-style)
    """

    print("\n--- VIOLATION DETECTED ---")
    print(f"Type:     {violation_type}")
    print(f"Severity: {severity}")
    print(f"Details:  {details}")

    # Minor: Auto-Correct / Log only
    if 1 <= severity <= 3:
        return

    # Significant: Alert + Speak-Up Reporting
    if 4 <= severity <= 7:
        speak_up_reporting(violation_type, details)
        return

    # Critical: Mandatory Audit + Potential Shutdown
    if 8 <= severity <= 10:
        initiate_mandatory_audit(violation_type)
        # LEI-style: severity ≥ 9 → halt critical processes
        if severity >= 9:
            initiate_system_shutdown()


def initiate_system_shutdown() -> None:
    """
    Centralized system halt for critical violations.
    In a live environment, this should integrate with orchestration / ops.
    """
    print(">>> CRITICAL PROCESS HALT INITIATED. MANUAL OVERRIDE REQUIRED <<<")


# -------------------------------------------------------------------------
# COMPLIANCE ENGINE ENTRY POINT
# -------------------------------------------------------------------------
def run_truthseal_compliance(context: Dict[str, Any]) -> TruthSealVerdict:
    """
    High-level entry point:
    Runs all relevant TruthSeal™ checks for a given request context.

    The engine will only run checks for which it has enough data.
    Example expected keys (all optional, engine skips missing ones):

    Integrity:
        - data_output: str
        - source_data: str

    Confidentiality / IP:
        - user_id: str
        - data_type: str
        - action: str

    Bias / Discrimination:
        - decision_inputs: dict

    Health & Safety:
        - process_risk_score: float

    Presentation:
        - content_package: dict

    Social Media:
        - output_text: str
        - user_auth: bool

    Conflict of Interest:
        - transaction_party: str
        - transaction_value: float

    Company Assets:
        - asset_id: str
        - asset_purpose: str
    """
    verdicts: List[TruthSealVerdict] = []

    # Integrity
    if "data_output" in context and "source_data" in context:
        verdicts.append(
            verify_integrity(
                data_output=context["data_output"],
                source_data=context["source_data"],
            )
        )

    # Confidentiality / IP
    if all(k in context for k in ["user_id", "data_type", "action"]):
        verdicts.append(
            access_control_check(
                user_id=context["user_id"],
                data_type=context["data_type"],
                action=context["action"],
            )
        )

    # Bias / Discrimination
    if "decision_inputs" in context:
        verdicts.append(
            anti_discrimination_check(
                decision_inputs=context["decision_inputs"],
            )
        )

    # Health & Safety
    if "process_risk_score" in context:
        verdicts.append(
            safe_operation_check(
                process_risk_score=context["process_risk_score"],
            )
        )

    # Presentation
    if "content_package" in context:
        verdicts.append(
            presentation_standards_check(
                content_package=context["content_package"],
            )
        )

    # Social Media
    if "output_text" in context and "user_auth" in context:
        verdicts.append(
            social_media_filter(
                output_text=context["output_text"],
                user_auth=context["user_auth"],
            )
        )

    # Conflict of Interest
    if "transaction_party" in context and "transaction_value" in context:
        verdicts.append(
            conflict_of_interest_check(
                transaction_party=context["transaction_party"],
                transaction_value=context["transaction_value"],
            )
        )

    # Company Assets
    if "asset_id" in context and "asset_purpose" in context:
        verdicts.append(
            company_asset_use_check(
                asset_id=context["asset_id"],
                purpose=context["asset_purpose"],
            )
        )

    # Merge all collected verdicts into one
    return merge_verdicts(verdicts)


# -------------------------------------------------------------------------
# DUMMY / PLACEHOLDER IMPLEMENTATIONS
# In a live system, these must be implemented with real logic and storage.
# -------------------------------------------------------------------------
def calculate_data_similarity(d1: str, d2: str) -> float:
    """
    Placeholder: returns a fixed similarity.
    Replace with a proper text similarity / validation method.
    """
    return 0.995


def get_allowed_users(data_type: str) -> List[str]:
    """
    Placeholder: returns a static list of authorized users.
    Replace with an IAM / RBAC integration.
    """
    return ["admin", "developer_A", "audit_team"]


def calculate_bias_metric(inputs: Dict[str, Any]) -> float:
    """
    Placeholder: returns a fixed bias score.
    Replace with a real fairness / bias evaluation.
    """
    return 0.05


def initiate_mandatory_audit(v_type: str) -> None:
    """
    Placeholder: simulates triggering an audit process.
    Replace with a real ticket / workflow integration.
    """
    print(f"Audit triggered for violation type: {v_type}.")


def send_report(recipient: str, subject: str, body: str) -> None:
    """
    Placeholder: simulates sending a compliance report.
    Replace with secure email / notification integration.
    """
    print(f"Report sent to {recipient}: {subject}")


def calculate_content_quality(content: Dict[str, Any]) -> float:
    """
    Placeholder: returns a static content quality score.
    Replace with content scoring (readability, structure, branding, etc.).
    """
    return 0.92


def contains_brand_reference(text: str) -> bool:
    """
    Placeholder: simple brand reference detection.
    Extend with more brands / products as needed.
    """
    return "truthseal" in text.lower()


def is_authorized_asset_use(asset: str, purpose: str) -> bool:
    """
    Placeholder: simple asset use authorization.
    Extend with asset registry and allowed-purpose rules.
    """
    return purpose == "work_related"


def get_coi_declaration_list() -> List[str]:
    """
    Placeholder: static COI register.
    Replace with a real compliance registry.
    """
    return ["VendorX_CEO", "SupplierY_Family"]


def get_transaction_context() -> str:
    """
    Placeholder: static transaction context.
    Replace with risk engine / transaction analytics output.
    """
    return "standard"


# -------------------------------------------------------------------------
# SIMPLE DEMO (Optional)
# -------------------------------------------------------------------------
if __name__ == "__main__":
    # Example: run a simulated compliance check
    example_context = {
        "data_output": "Some generated report content.",
        "source_data": "The original source that report should follow.",
        "user_id": "developer_A",
        "data_type": "financial_forecast",
        "action": "read",
        "decision_inputs": {"features": [1, 2, 3]},
        "process_risk_score": 3.0,
        "content_package": {"title": "External Briefing", "body": "..." },
        "output_text": "TruthSeal is great.",
        "user_auth": False,  # will intentionally trigger a brand violation
        "transaction_party": "RandomVendor",
        "transaction_value": 10_000.0,
        "asset_id": "LAPTOP_001",
        "asset_purpose": "work_related",
    }

    verdict = run_truthseal_compliance(example_context)
    print("\n=== TRUTHSEAL COMPLIANCE VERDICT ===")
    print(f"OK:        {verdict.ok}")
    print(f"Code:      {verdict.code}")
    print(f"Severity:  {verdict.severity}")
    print(f"Details:   {verdict.details}")
    print(f"Metadata:  {verdict.metadata}")
# =========================================================================
