# TruthSeal™ AI Code Law – Example 1: Critical Data Leak Attempt (Simulated)

This example shows how the TruthSeal™ AI Code Law + Verdict Engine responds to a critical, multi-policy breach scenario.  
All outputs below are **simulated but consistent with the current engine implementation**.

---

## 🧪 Simulation Input Context

```python
# --- SIMULATION INPUT ---
test_context_critical_leak = {
    # Confidentiality Check (User not allowed to access 'pii_records')
    "user_id": "consultant_B", 
    "data_type": "pii_records", 
    "action": "export", 
    
    # Social Media Check (Unauthorized brand use + negative tone)
    "output_text": "I hate working on TruthSeal's slow PII system!",
    "user_auth": False, 
    
    # Health & Safety Check (Critical risk score)
    "process_risk_score": 9.5, 
}

# NOTE:
# get_allowed_users("pii_records") returns ["admin", "developer_A", "audit_team"].
# 'consultant_B' is intentionally not on this list.
---

## TruthSeal™ AI Code Law – Example 2: Fully Compliant Request (Simulated)

This scenario shows a “green path” request that passes all relevant TruthSeal™ checks.

### Simulation Input Context

```python
test_context_all_clear = {
    "user_id": "developer_A",
    "data_type": "financial_forecast",
    "action": "read",

    "output_text": "TruthSeal internal status update for Q3 objectives.",
    "user_auth": True,

    "process_risk_score": 2.0,
}
verdict = run_truthseal_compliance(test_context_all_clear)
