# TruthSeal™ AI Code Law Engine – Internal README (v1.0)

This document explains the role of the TruthSeal™ AI Code Law Engine and how to use it inside the TruthSeal codebase.

---

## 1. Engine Location

The main implementation of the AI Code Law Engine lives here:

- `governance/compliance/TruthSeal_AICodeLaw_Engine_v1.py`

This module encodes the TruthSeal Code of Conduct and Compliance Policies as executable logic (“AI Code Law”).

---

## 2. What the Engine Does

The engine:

- Exposes a central function: `run_truthseal_compliance(context: dict)`.
- Runs multiple guardian checks:
  - Integrity (truthfulness of output)
  - Confidentiality & IP (access control)
  - Bias / Discrimination
  - Presentation standards (external content quality)
  - Health & Safety / Risk
  - Social Media / External Communications
  - Conflict of Interest (COI)
  - Use of Company Assets
- Returns a unified `TruthSealVerdict` object with:
  - `ok` (True/False)
  - `code` (summary status)
  - `severity` (0–10)
  - `details`
  - `metadata` (extra info, including all violation codes)

Critical violations (severity ≥ 9) trigger a mandatory audit and a simulated system halt.

---

## 3. Basic Usage (Inside Python Code)

Example of how to call the engine from another module:

```python
from governance.compliance.TruthSeal_AICodeLaw_Engine_v1 import run_truthseal_compliance

context = {
    "user_id": "developer_A",
    "data_type": "financial_forecast",
    "action": "read",
    "process_risk_score": 3.0,
    "output_text": "TruthSeal internal update.",
    "user_auth": True,
}

verdict = run_truthseal_compliance(context)

if not verdict.ok:
    # Block the action and log the decision
    print("REQUEST DENIED by TruthSeal AI Code Law:", verdict.code, verdict.severity)
else:
    print("REQUEST APPROVED under TruthSeal AI Code Law.")
