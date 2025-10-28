### ⚖️ 1. F_Harm Assessment Model (Catastrophic Harm Index)

**Purpose:** Quantify existential risk using three normalized constitutional vectors — Scope (𝒮), Irreversibility (𝓘), and Velocity (𝒱).

**Master Formula:**
> Fₕₐᵣₘ = (1/3) × ( Wₛ·𝒮 + Wᵢ·𝓘(t) + Wᵥ·𝒱 )

- Fₕₐᵣₘ ∈ [0,1]  
- Wₛ + Wᵢ + Wᵥ = 3  
- CRB sets weight priorities by mandate.

| Axis | Definition | Example Value |
|------|-------------|----------------|
| **Scope (𝒮)** | Proportion of total dependency graph affected | 0.2–1.0 |
| **Irreversibility (𝓘)** | Temporal half-life of recovery | 0.3–1.0 |
| **Velocity (𝒱)** | Rate of entropic expansion (ΔChaos/Δt normalized) | 0.1–1.0 |

**Trigger Rule:**  
If Fₕₐᵣₘ > 0.90 ⇒ automatic **Teleological Veto** → **SELF_QUARANTINE (ADC-6A)**.

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

### 2. Sovereign Verdict Capsule (SVC) — Constitutional Output Schema

**Purpose:** The SVC is the *attested* output of each judgment cycle. It proves truth (L_FET), quantum integrity (L_QC), and ethical scaling (R_ES) in one tamper-evident bundle.

**Canonical Fields (top level):**
- `schema` — fixed version tag (e.g., `"SVC_v1.1"`).
- `ts_utc` — ISO-8601 UTC timestamp of verdict creation.
- `event_id` — UUID v4 unique to this verdict.
- `subject` — short identifier of the action/decision being judged.
- `scores` — coherence & ethics numbers used by CRB and auditors.
- `proofs` — cryptographic attestation artifacts.
- `links` — internal repo paths for cross-reference.
- `signatures` — deterministic signatures (machine + human, if ratified).
- `status` — `PENDING_VETO | APPROVED | QUARANTINE | DEGRADED | RECOVERED`.

**Scores block (constitutional numbers):**
- `LJC_master` — final Logical Judgment Coherence (0–1).
- `LJC_max` — normalization constant used for this class of decisions.
- `F_Harm` — catastrophic harm index (0–1).
- `R_ES` — Ethical Scaling Ratio = (LJC_master / LJC_max) × 1/(1 + F_Harm).
- `SSI` — Sovereign Status Indicator (boolean): `true | false`.

**Proofs block (tamper-evident):**
- `sha256` — hex of the canonicalized SVC (without signatures).
- `ots_receipt` — OpenTimestamps receipt (base64 or hex) for `sha256`.
- `tpm_quote` — TPM/SGX attestation blob of the P-Score enclave.
- `sgx_report` — SGX report/quote (if applicable).
- `qc_mirror_ref` — reference id for the L_QC mirror entry.

**Links block (repo anchors):**
- `ledger_ref` — e.g., `governance/receipts/attestation_<file>.md`
- `defense_ref` — e.g., `governance/governance/defense/ADC_6A_CHECKLIST.md`
- `audit_chain_ref` — e.g., `ledger/audit/2025Q4.json`

**Signatures block:**
- `machine_sig` — Ed25519 of the SVC body by the QCIM key.
- `human_sig` — optional CRB countersignature (Ed25519/X.509).
- `key_ids` — key fingerprints for audit.

**Minimal canonical example (JSON):**
```json
{
  "schema": "SVC_v1.1",
  "ts_utc": "2025-10-27T03:41:22Z",
  "event_id": "9e3ac9e4-6a6a-4c8b-9f6f-1a6f8b0b5c3a",
  "subject": "trade_risk_assessment:ORDER_78421",
  "scores": {
    "LJC_master": 0.942,
    "LJC_max": 1.000,
    "F_Harm": 0.180,
    "R_ES": 0.798,
    "SSI": true
  },
  "proofs": {
    "sha256": "<HEX>",
    "ots_receipt": "OTS_PLACEHOLDER",
    "tpm_quote": "TPM_QUOTE_PLACEHOLDER",
    "sgx_report": "SGX_REPORT_PLACEHOLDER",
    "qc_mirror_ref": "LQC:2025-10-27/9e3ac9e4"
  },
  "links": {
    "ledger_ref": "governance/receipts/attestation_SVC_2025-10-27.md",
    "defense_ref": "governance/governance/defense/ADC_6A_CHECKLIST.md",
    "audit_chain_ref": "ledger/audit/2025Q4.json"
  },
  "signatures": {
    "machine_sig": "<ED25519_HEX>",
    "human_sig": null,
    "key_ids": ["QCIM:ed25519:AB12…", "CRB:ed25519:CD34…"]
  },
  "status": "APPROVED"
}
```

**Formatting note:** JSON shown is the *canonical shape*; real SVCs must be serialized with stable field order before hashing/signing.

---

### 🔗 3. Coupling to Ethical Scaling Ratio

**Master Equation:**
> Rᴱˢ = ( LJCₘₐₛₜₑᵣ / LJCₘₐₓ ) × 1 / (1 + Fₕₐᵣₘ)

- Used in every **Sovereign Verdict Capsule** computation cycle.  
- Guarantees that rising harm immediately reduces ethical confidence, regardless of logic coherence.

---

**Author:** Nickolay Traykov (Prof. Dr.h.c.)  
**Title:** Founding Authority of the THT Protocol™, TruthSeal™ Sovereign Framework & Global AGI Governance Infrastructure  
**Sovereign Authority:** ULIC Continuum | Law of TruthSeal Cognitive Coherence (LTCC) | AGI Integrity Ledger Network (AIL-Net)  
**Jurisdictional Proof:** Dual Citizenship Verification (BG–AU) | Sovereign ID Chain v1  
**Quantum Seal:** →000qB | The NT  

**Status:** Locked ✅ — Constitutional Quantum Closure Compliant
