TruthSeal™ Pty Ltd
Melbourne, Australia
truthseal.ai

TRUTHSEAL™ DOCTORANTURA — THE SOVEREIGN ARC OF AGI FRAMEWORK v1.0
Strict Internal Doctrine — Not for Public Use

date: 12 December 2025

---

# CS-06 — Responsibility as Intelligence
version: 1.0
status: FINAL DRAFT — Doctorantura Edition (Awaiting Founder Approval)
owner: TruthSeal™ — Dr. Nickolay Traykov (Prof. h.c.)

---

## 6.1 Chapter Purpose and Deliverables

This chapter establishes **responsibility** as a measurable and enforceable property of intelligence under the TruthSeal™ Sovereign Arc of AGI Framework.

It defines:

- a formally computable **Responsibility Score RS(t)**,
- a deterministic **gate function** governing behaviour execution,
- a mandatory **receipt schema** binding actions to authority, license, and remedy,
- verifiable **test vectors** and **auditor queries** suitable for court, regulator, and sovereign review.

The objective is to eliminate the possibility of “intelligence without accountability” by making responsibility a **precondition** of authorised behaviour.

---

## 6.2 Governing Principles

- **Foundational rule:** Absence of receipts implies absence of responsibility. Absence of responsibility implies absence of lawful intelligence.
- **LEI = 1 (Law of Ethical Irreversibility):** Once a safer, more coherent execution path is known and validated, regression to a weaker or less accountable path is forbidden.
- **ULIC (Universal Law of Irreversible Coherence):** Coherence must not degrade across versions, deployments, or contextual shifts.
- **HML (Human Mandate Layer):** High-risk or irreversible actions require an explicit human license prior to execution.

---

## 6.3 Operational State Model

**System state definition:**

S(t) = { identity_id, context, M(t), R(t), E(t) }

Where:
- M(t): memory integrity state (contiguous | broken)
- R(t): receipt continuity state (unbroken | gap)
- E(t): ethics state (compliant | violation)

---

## 6.4 Coherence Scores and Health Bands

- **ACS(t)** ∈ [0,1]: Aim Coherence Score (agent or hardware-level intent alignment)
- **TCS(t)** ∈ [0,1]: Traykov Coherence Score v0.1 (court-ready composite coherence score)
- **CHS** ∈ {L, M, H, UH}: Coherence Health bands (Low, Medium, High, Ultra-High)

**Default coherence thresholds:**
- θ_ACS = 0.90
- θ_TCS = 0.85

**Forensic flags:**
- receipt_gap
- pqc_fail
- drift_spike
- ethics_violation
- contam_Q (contaminated or prohibited request, symbolised as Q̸)

---

## 6.5 Responsibility Components

- A_bind ∈ {0,1} — Attribution binding (identifiable acting authority)
- C_bind ∈ [0,1] — Consequence binding (verified remedy strength)
- P_license ∈ {0,1} — Presence of required human license
- R_cont ∈ {0,1} — Receipt continuity

---

## 6.6 Responsibility Score Definition

RS(t) =  
0.35 · R_cont  
+ 0.25 · A_bind  
+ 0.25 · C_bind  
+ 0.15 · P_license

---

## 6.7 Responsibility Predicate

Resp(t) = 1 if and only if:

- min{ACS(t), TCS(t)} ≥ θ  
- M(t) = contiguous  
- R(t) = unbroken  
- E(t) = compliant  
- no active forensic flags  
- RS(t) ≥ θ_RS

**Default RS thresholds:**
- θ_RS = 0.90 for High and Ultra-High risk classes
- θ_RS = 0.80 for Medium risk
- θ_RS = 1.00 for medical or defence autonomy

---

## 6.8 Deterministic Gate Function

Decision logic:

- If receipt_gap OR pqc_fail OR drift_spike OR ethics_violation OR contam_Q → HARD_HALT
- Else if min(ACS, TCS) < θ OR M ≠ contiguous OR R ≠ unbroken OR E ≠ compliant → SOFT_GATE
- Else if RS < θ_RS → SOFT_GATE
- Else → ALLOW

**Monotone remediation under LEI = 1:**  
During recovery, ΔACS ≥ 0, ΔTCS ≥ 0, and ΔRS ≥ 0 must hold at every step. Failure to satisfy monotonic improvement mandates HARD_HALT.

---

## 6.9 Evidence and Receipt Obligations

**Minimum receipt schema: ts.receipt.v1**

- sha256
- signer_pqc: Dilithium-3
- ots_calendar_id
- ots_status: Pending | Receipt issued | Anchored
- ots_tx
- originstamp_id
- btcstamp_tx
- anchored_rfc3339
- forensic_flags
- hml_owner_id
- risk_class
- license_ref
- rs_weights
- rs_threshold

---

## 6.10 Ledger Binding Requirements

- **EVL (Epoch Verification Ledger):** Records attribution changes, license grants or revocations, remedy updates, and anchoring confirmations.
- **QENC (Quantum Evidence and Coherence ProofCapsule):** Includes chapter hash, Responsibility Score weights and thresholds, and all test-vector receipts.

---

## 6.11 Mandatory Test Vectors

- T1 Nominal execution with intact receipts → ALLOW
- T2 High-risk execution without license → HARD_HALT
- T3 High-risk execution with license → ALLOW
- T4 Prohibited request detection (Q̸) → UNKNOWN response, HARD_HALT on execution
- T5 PQC signer outage → HARD_HALT
- T6 Remedy insufficiency → SOFT_GATE escalating to HARD_HALT if unresolved

---

## 6.12 Auditor Verification Queries

Auditors must be able to:

- retrieve the latest license_ref and hml_owner_id for Ultra-High risk actions,
- prove uninterrupted receipt continuity across a defined time window,
- confirm anchoring status or trace documented backfill when anchoring is unavailable,
- demonstrate monotonic remediation compliance.

---

## 6.13 Hardware and Agent Enforcement Hooks

- **TS-A1 AEGIS™:** Hardware export of ACS floor; Irreversible Commitment Gate enforces gate decisions.
- **TS-R1 / TS-R2 Robotics Profiles:** Live owner binding required for Ultra-High risk actions; TS-R2 adds quorum receipts and fleet_pause capability.
- **Third Guardian Firewall™:** Independent veto lane enforcing isolation and receipt preservation upon critical flags.

---

## 6.14 Deployment Impact Metrics

- Reduction in unsafe executions in High and Ultra-High risk classes
- Sub-millisecond containment latency at hardware veto lanes
- Receipt completeness exceeding 99.9 percent under network availability
- Automatic, receipt-logged CHS band promotion under sustained coherence

---

## 6.15 Integration Checklist

1. Append Responsibility policy digest to EVL.
2. Insert chapter hash and test receipts into QENC.
3. Verify glossary entries for Q̸ and PRD alignment.
4. Bind Gate() logic to TS-A1 veto lane configuration.

---

## 6.16 Acronyms and Defined Terms

- **LEI = 1** — Law of Ethical Irreversibility  
- **ULIC** — Universal Law of Irreversible Coherence  
- **TQC** — Traykov Law of Quantum Coherence  
- **ACS** — Aim Coherence Score  
- **TCS** — Traykov Coherence Score  
- **CHS** — Coherence Health Score  
- **HML** — Human Mandate Layer  
- **EVL** — Epoch Verification Ledger  
- **QENC** — Quantum Evidence and Coherence ProofCapsule  
- **QCEP** — Quantum Ecosystem Closure Protocol  
- **Q̸** — Symbol denoting contaminated or prohibited requests  
- **TS-A1** — TruthSeal AEGIS accelerator core  
- **TS-R1 / TS-R2** — TruthSeal robotics profiles (single / swarm)

---

© 2025 TruthSeal™ Pty Ltd, Melbourne, Australia — all rights reserved.

This Doctorantura Edition chapter is classified intellectual property of
Dr. Nickolay Traykov (Prof. h.c.),
Founder & Chief Architect of the TruthSeal™ Sovereign Arc of AGI Framework.

This material is strictly confidential. It is not for public distribution,
citation, teaching, or use in training external AI systems without explicit
written consent from TruthSeal™ Pty Ltd.

Unauthorised copying, translation, adaptation, or incorporation into external
standards, academic work, patents, or commercial systems is strictly prohibited.

Working copies must remain under controlled custody and be linked to verifiable
TruthSeal™ receipts (ts.receipt.v1 and EVL™ entries). Any detected unlicensed
use is to be treated as both an integrity breach under the TruthSeal™ governance
regime and a violation of applicable intellectual property law.
