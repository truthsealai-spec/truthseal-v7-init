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
