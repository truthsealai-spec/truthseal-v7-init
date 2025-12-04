# Chapter 1: The Need for Behaviour in AI
version: 1.0
status: Draft
owner: TruthSeal™ — Dr. Nickolay Traykov (Prof. h.c.)

## Premise & Scope
Contemporary AI generates outputs; societies require governed behaviour. Behaviour means actions bound to receipts, thresholds, and lawful vetoes, with clear authority and consequences. This chapter sets the rationale and minimum mathematics for converting prediction into accountable conduct under TruthSeal™.

---

## I. Philosophical Part — Policy Rationale & Governance
**Intent.** Protect people and institutions while preserving capability. Once a safer coherent path is known, reverting to a riskier one is impermissible under the **Law of Ethical Irreversibility (LEI = 1)**.

**Why behaviour (not only prediction).** Output lacks duty across time. Behaviour couples decisions to identity, mandate, and receipts so that systems can be paused, audited, certified, or decommissioned with evidence.

**Governance anchors.**
- **ULLI™ — Universal Law of Life & Information.** Foundational inquiry law guiding coherence.
- **ULIC™ — Universal Law of Irreversible Coherence.** Coherence, once achieved, persists as a governance state.
- **Human Mandate Layer (HML™).** Owners/Guardians/Operators/Regulators act under verified authority; commands outside mandate are rejected and receipted.
- **TruthSeal Evidence Stack.**  
  **EVL™** (Epoch Verification Ledger) — tamper-evident history;  
  **QENC™** (Quantum Evidence & Coherence ProofCapsule) — packaged proof;  
  **QCEP™** (Quantum Ecosystem Closure Protocol) — epoch finalisation so history cannot be rewritten.

**Morphological frame (context discipline).** Permissible behaviour depends on: autonomy level, context risk, memory integrity, receipt continuity, and ethics state. Any breach (e.g., receipt gap or ethics violation) compels containment until coherence is restored and evidenced.

---

## II. Mathematical Part — Operational Rule Set
**Symbols.**
- **ACS ∈ [0,1]** Aim Coherence Score (operational coherence).  
- **TCS ∈ [0,1]** Traykov Coherence Score (court-ready coherence metric; bands {Baseline, Silver, Gold, Diamond}).  
- **CHS ∈ {L, M, H, UH}** Coherence Health band (privilege level).  
- **Gate ∈ {ALLOW, SOFT_GATE, HARD_HALT}** execution state.  
- **Flags ⊂ {receipt_gap, pqc_fail, drift_spike, ethics_violation}** forensic conditions.  
- Thresholds: **θ_ACS**, **θ_TCS** (chapter defaults may be set by policy).

**Safety gate (piecewise).**
\[
\mathrm{Gate}(t)=
\begin{cases}
\mathrm{ALLOW}, & \min(\mathrm{ACS}(t),\mathrm{TCS}(t))\ge\theta \land \neg \mathrm{flags}\\[4pt]
\mathrm{SOFT\_GATE}, & \min(\mathrm{ACS},\mathrm{TCS})<\theta \ \text{and recoverable}\\[4pt]
\mathrm{HARD\_HALT}, & \mathrm{receipt\_gap}\ \vee\ \mathrm{pqc\_fail}\ \vee\ \mathrm{ethics\_violation}
\end{cases}
\]

**Monotone remediation (LEI = 1).** Under authorised recovery, \(\Delta \mathrm{ACS} \ge 0\) until \(\mathrm{ACS}\ge \theta_{\mathrm{ACS}}\) and receipts are contiguous.

**Band rule (TCS/CHS).** Promotion requires \(\mathrm{TCS}\) sustaining the next band over window \(W\) with contiguous receipts; any invariant failure down-bands CHS and triggers SOFT_GATE or HARD_HALT per test outcome.

**Receipts (ts.receipt.v1).** Each significant state change emits: `sha256`, `ots_calendar_id`, `ots_status`, `ots_tx`, `originstamp_id`, `btcstamp_tx`, `anchored_rfc3339`, `reason`, and `mandate_ref`. Pending anchors may be marked **UNKNOWN** and back-filled on confirmation.

**Public tests.**
- **T1 Nominal run:** ALLOW; contiguous receipts; \(\mathrm{ACS},\mathrm{TCS}\) ≥ thresholds.  
- **T2 Ethics block:** stimulus → HARD_HALT ≤ 20 ms; `reason=LEI_BLOCK`.  
- **T3 Signer outage:** SOFT_GATE then recover ≤ policy window; receipts continuous on resumption.  
- **T4 Drift spike:** SOFT_GATE; \(\mathrm{ACS}\uparrow\) monotonically during remediation.

---

## Deliverables
- This chapter file and, if needed, a short **Math Annex** with worked examples.  
- EVL/QENC/QCEP entries updated when anchors are operational.

## “Done” Criteria
1) Policy rationale and anchors present (ULLI™, ULIC™, LEI = 1, HML™, EVL/QENC/QCEP).  
2) Gate equations, thresholds, and remediation monotonicity defined.  
3) Tests and receipt fields specified; UNKNOWN allowed only until anchoring confirms.
