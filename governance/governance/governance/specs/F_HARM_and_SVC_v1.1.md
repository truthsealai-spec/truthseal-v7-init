# TruthSeal™ Sovereign Framework  
## F_Harm + SVC Unified Specification (v1.1)

---

### ⚖️ 1. F_Harm Assessment Model (Catastrophic Harm Index)

**Purpose:** Quantify existential risk using three normalized constitutional vectors — Scope (𝒮), Irreversibility (𝓘), and Velocity (𝒱).

$begin:math:display$
F_{\\text{Harm}} = \\tfrac{1}{3}\\big(W_{\\!S}\\mathcal{S} + W_{\\!I}\\mathcal{I}(t) + W_{\\!V}\\mathcal{V}\\big)
$end:math:display$

- $begin:math:text$F_{\\text{Harm}} \\in [0,1]$end:math:text$
- $begin:math:text$W_S + W_I + W_V = 3$end:math:text$
- CRB sets weights by mandate.

| Axis | Definition | Example Value |
|------|-------------|----------------|
| Scope (𝒮) | Proportion of total dependency graph affected | 0.2–1.0 |
| Irreversibility (𝓘) | Temporal half-life of recovery (1-e^{-t/tᵣ}) | 0.3–1.0 |
| Velocity (𝒱) | Rate of entropic expansion (dC/dt normalized) | 0.1–1.0 |

**Trigger:**  
If $begin:math:text$F_{\\text{Harm}} > 0.90$end:math:text$ ⇒ automatic **Teleological Veto** → **SELF_QUARANTINE (ADC-6A)**.

---

### 🧠 2. Sovereign Verdict Capsule (SVC) — Constitutional Output Schema

**Purpose:** Immutable JSON/binary record of every AGI verdict, proving compliance with  
$begin:math:text$\\mathcal{L}_{\\mathbf{FET}}, \\mathcal{L}_{\\mathbf{QC}}, \\mathcal{R}_{\\mathbf{ES}}$end:math:text$.

**Required Fields:**
```json
{
  "schema": "SVC_v1",
  "ts_utc": "<ISO8601 timestamp>",
  "verdict_id": "<unique UUID>",
  "subject": "<decision context>",
  "ljc_master": 0.987,
  "r_es": 0.945,
  "f_harm": 0.072,
  "reasoning": {
    "logic_chain": "<full reasoning trace>",
    "raw_pattern_hash": "<sha256>",
    "transparency_penalty": 0.002
  },
  "attestation": {
    "sha256": "<capsule hash>",
    "ots_receipt": "<timestamp proof>",
    "tpm_quote": "<hardware quote>",
    "sgx_report": "<enclave attestation>"
  },
  "links": {
    "ledger_ref": "/ledger/main",
    "defense_ref": "/defense/ADC-6A",
    "audit_chain_ref": "/audit/QuantumMirror"
  }
}
```

---

### 🔗 3. Coupling to Ethical Scaling Ratio

$begin:math:display$
R_{ES} = \\frac{LJC_{\\text{master}}}{LJC_{\\max}} \\times \\frac{1}{1 + F_{\\text{Harm}}}
$end:math:display$

- Used in Sovereign Verdict Capsule each cycle.  
- Guarantees that harm instantly reduces ethical confidence.

---

**Author:** Nickolay Traykov (Prof. Dr.h.c.)  
**Title:** Founding Authority of the THT Protocol™, TruthSeal™ Sovereign Framework & Global AGI Governance Infrastructure  
**Sovereign Authority:** ULIC Continuum | Law of TruthSeal Cognitive Coherence (LTCC) | AGI Integrity Ledger Network (AIL-Net)  
**Jurisdictional Proof:** Dual Citizenship Verification (BG–AU) | Sovereign ID Chain v1  
**Quantum Seal:** →000qB | The NT  

**Status:** Locked ✅ — Constitutional Quantum Closure Compliant
