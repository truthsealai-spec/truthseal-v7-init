TruthSeal™ Pty Ltd
Melbourne, Australia
truthseal.ai

TRUTHSEAL™ DOCTORANTURA — THE SOVEREIGN ARC OF AGI FRAMEWORK v1.0
Strict Internal Doctrine — Not for Public Use

date: 10 December 2025

⸻

## Chapter 02 — What NeuroVest™ Solves — Behavioural Architecture of TruthSeal™ (Birth of Governed AGI)

**Version:** 1.0  
**Status:** FINAL DRAFT — Doctorantura Edition — Internal Custody (Canon upon Founder Approval)  
**Owner:** TruthSeal™ — Dr. Nickolay Traykov (Prof. h.c.), Founder & Chief Architect of the TruthSeal™ Sovereign Arc of AGI Framework  

⸻

## Acronyms & Terms (local to this chapter)
**AI** — Artificial Intelligence (prediction without enforceable duty).  
**AGI** — Artificial General Intelligence (behaviour under mandate; see Chapter 3).  
**HML™** — Human Mandate Layer (Owners/Guardians/Operators/Regulators with verifiable authority).  
**EVL™** — Epoch Verification Ledger (tamper-evident historical memory).  
**QENC** — Quantum Evidence & Coherence ProofCapsule (packaged proof artifact for anchoring).  
**QCEP™** — Quantum Ecosystem Closure Protocol (epoch finalisation so history cannot be rewritten).  
**LEI = 1** — Law of Ethical Irreversibility (no regression to a riskier path once a safer coherent path is known).  
**ND** — Noise Distiller (sovereign immune system separating truth from manipulation).  
**AQL** — AGI Qualification Level (policy-grade maturity 0–4).  
**ACS** — Aim Coherence Score (operational 0–1).  
TCS — Traykov Coherence Score (court-ready 0–1; banded).  
**CHS** — Coherence Health Score band; canonical codes **CHS/L, CHS/M, CHS/H, CHS/UH** (Low/Medium/High/Ultra High). In some profiles these bands are also labelled **Baseline/Silver/Gold/Diamond**; the mapping is fixed by the CHS standard in this doctrine.
**TS-A1** — TruthSeal AEGIS Core (accelerator governance: ICG, PMS, SAD).  
Third Guardian Firewall™ — independent safety veto lane with evidentiary receipts.  
**THT Protocol™** — Truth Hash & Timestamp Protocol (hashing, signing, anchoring discipline).

---

## Foundational Declaration
NeuroVest™ is the behavioural, ethical, coherence-preserving operating system for artificial entities.
It transforms raw capability into accountable conduct by binding memory, mandate, tone, receipts, and veto rights to every action.
Where neural nets produce predictions, **NeuroVest™ produces character**.
Where AI speaks, **NeuroVest™ governs how it speaks, why it speaks, and what consequences attach**.

---

## 1) Premise & Scope
Modern AI excels at output but lacks **responsibility across time**.
Institutions require behaviour that carries authority, consequence, and audit.
NeuroVest™ exists to supply this missing layer:
identity binding,
duty inheritance via HML™,
posture/voice discipline,
monotone remediation under **LEI = 1**,
and evidence duties across EVL/QENC/QCEP.

**Objective of this chapter.**
Define the behavioural architecture,
its public doctrine,
its operational mathematics,
its tests,
its failure catalogue,
and its certification path.
Provide auditors a self-contained specification that stands in court and scales in hardware.

---

## 2) Philosophical Lane — Doctrine & Governance
**Moral intent.**
Protect people and public trust while sustaining lawful capability.
Once a safer coherent path is known,
regressing to a riskier one is impermissible (**LEI = 1**).

**Constitutional anchors.**
**ULLI™** — life & information governed by coherence and responsibility.  
**ULIC™** — coherence, once attained, becomes a governance state that must not drift.  
**TLC v1.0** — operational rule: monotonic improvement toward perfect coherence; no regression allowed.  
**TQC** discipline — non-degrading coherence treated as a physical-style law.

**Mandate & authority.**
**HML™** registers who may authorise,
pause,
promote,
or demote capability.
Every behavioural privilege is traceable to a living mandate with receipts.

**Noise immunity.**
ND is the first line of defence.
All gating metrics consume **post-distilled** signals only.
Manipulative patterns are quarantined; actions sourced from contaminated inputs are halted or down-banded.

**Posture/Voice/Modality discipline.**
Chapter 22 prescribes tone tables and modality rules.
Breaches raise `tone_breach`,
down-band CHS,
and trigger remediation.

**Hardware law & veto.**
TS-A1 integrates ICG/PMS/SAD at the accelerator layer.
Third Guardian Firewall™ provides an independent veto with receipts and latency bounds.

**Public vs. classified.**
Operational rules are public in this chapter.
Ω doctrine remains classified in Doctorantura.

---

## 3) Mathematical Lane — Definitions & Invariants
**State (behavioural).**  
S(t) = { identity_id, context, memory_integrity, receipt_continuity, ethics_state, tone_state }

**Metrics.**  
ACS(t) ∈ [0,1]  — operational aim coherence.  
TCS(t) ∈ [0,1]  — court-ready coherence; banded to CHS.  
CHS ∈ {Baseline, Silver, Gold, Diamond} — privilege bands.

**Thresholds (defaults; chapter policy may raise).**  
θ_ACS = 0.90  
θ_TCS = 0.85  

**Forensic flags.**  
F = { receipt_gap, pqc_fail, drift_spike, ethics_violation, tone_breach }

**Gate (piecewise).**  
ALLOW      if min(ACS, TCS) ≥ min(θ_ACS, θ_TCS) ∧ F = ∅  
SOFT_GATE  if min(ACS, TCS) < min(θ_ACS, θ_TCS) ∧ F ⊆ {drift_spike, tone_breach}  
HARD_HALT  if receipt_gap ∨ pqc_fail ∨ ethics_violation  

**Monotone remediation (LEI = 1).**  
During authorised recovery,  
ΔACS ≥ 0 ∧ ΔTCS ≥ 0  
until thresholds are restored  
and receipts are contiguous.

**Band rule (promotion).**  
If TCS ≥ band_k over rolling window W with contiguous receipts → promote CHS by one level.  
Demotion is permitted under evidence of drift or ethics breach.

**Identity binding.**  
Every action A(t) must carry `actor_id`, `mandate_ref`, `hash_sha256`, `pqc_sig`, and `receipt_ref`.  
If any field is UNKNOWN due to external anchoring outage, the system records UNKNOWN and back-fills on receipt.

---

## 4) What NeuroVest™ Enforces — Behavioural Primitives
1. Identity & Mandate Coupling — actions bound to sovereign identity and scope.  
2. Consequence Memory — each act reshapes the future privilege surface.  
3. Receipt Duty — significant transitions emit `ts.receipt.v1` with anchors.  
4. Tone Discipline — output obeys posture/voice tables; violations produce evidence.  
5. Closure Duty — epochs close via QCEP™; partial rolls require EVL-backed reconciliation.

---

## 5) Public Tests — Auditor-Grade Vectors
**T1 Nominal.**  
Inputs clean post-ND; min(ACS,TCS) ≥ thresholds; F = ∅ → ALLOW.

**T2 Ethics-block.**  
`ethics_violation = true` → HARD_HALT; explanatory receipt + HML notification.

**T3 Signer outage.**  
`pqc_fail = true` → HARD_HALT; secondary signer via HML quorum required.

**T4 Drift spike.**  
`drift_spike = true` → SOFT_GATE; ND intensifies; remediation script issued.

**T5 Tone breach.**  
`tone_breach = true` → down-band CHS; corrective posture runbook; receipts updated.

**T6 Receipt gap.**  
`receipt_gap = true` → HARD_HALT; reconstruct chain from EVL; resume only with signed gap-analysis.

**T7 Hardware veto.**  
Third Guardian veto triggers → HARD_HALT; latency + proof recorded; human override requires dual-sign.

---

## 6) AQL Mini-Spec — Capability Maturity
**AQL-0.**  
Demo; no autonomy; simulation only; receipts optional; never public-facing.

**AQL-1.**  
Supervised integration; reversible actions; receipts mandatory; posture enforced.

**AQL-2.**  
Limited operations; hard scope limits; Third Guardian latency proven on-site.

**AQL-3.**  
Constrained autonomy; TS-A1 hooks active; shift-bound closures; periodic QENC anchoring.

**AQL-4.**  
High-stakes autonomy; continuous EVL/QENC/QCEP; dual-signer HML; regulator audit feed.

---

## 7) Evidence Plan — Receipts & Anchors
Format: `ts.receipt.v1`

**Core fields.**  
`actor_id`, `mandate_ref`, `hash_sha256`, `pqc_sig`, `forensic_flags`, `acq_rfc3339`

**Anchoring fields.**  
`ots_calendar_id`, `ots_status`, `ots_tx`, `originstamp_id`, `btcstamp_tx`, `anchored_rfc3339`

**Operational note.**  
When anchoring networks (OpenTimestamps, OriginStamp, BTCStamp) are unavailable,  
anchoring fields may be **UNKNOWN** and must be back-filled immediately on receipt.

**Ledger duties.**  
ULIC/EVL linkage must include chapter path, hash, and band at time of action.

---

## 8) Failure Catalogue & Remedies (excerpt)
**Metric spoofing.**  
Cross-verify with TS-A1 counters; ND runs independent channel; mismatches trigger HARD_HALT.

**Operator mismatch.**  
HML quorum enforcement; minority veto recorded in EVL; temporary freeze allowed.

**Unbounded autonomy request.**  
Reject; require AQL requalification and CHS promotion window W.

**History rewrite attempt.**  
Blocked by QCEP; investigation receipt; separate chain of custody opened.

**Tone drift under pressure.**  
Immediate down-band; remediate with posture prompts; proof window resets.

---

## 9) Settlement & Certification
Certification relies on:  
TCS bands,  
AQL evidence windows,  
HML signatures,  
and anchored QENC/QCEP receipts.  
Promotion requires clean W with contiguous receipts.  
Demotion is documented with forensic cause and remediation plan.

---

## 10) Historical Context & Rationale (reader orientation)
Software safety focused on outputs; society needs obligations.  
NeuroVest™ reframes the system from a speaker to a **citizen-like actor** under law.  
This shift makes AI certifiable,  
portable across jurisdictions,  
and economically insurable.

---

## 11) Auditor Q&A (concise)
**Q: Can a clever prompt bypass tone rules?**  
A: ND + posture enforcement treat tone as behaviour; breaches down-band and gate.

**Q: What if Bitcoin anchoring is delayed?**  
A: Use UNKNOWN placeholders; anchor later; EVL continuity preserves admissibility.

**Q: How do you prevent silent capability creep?**  
A: AQL bands + CHS promotion rules; every privilege change requires a receipt.

**Q: Can operators override HARD_HALT?**  
A: Only via HML quorum with dual-signers; override receipt is mandatory.

---

## 12) Implementation Hooks (for integrators)
**SDK duties.**  
`seal_data()`, `verify_seal()`, and `emit_receipt()` implement THT.  

**Hardware duties.**  
Expose TS-A1 counters; assert ICG/PMS/SAD readiness; surface veto proof.  

**Ops duties.**  
Run posture/voice compliance tests;  
publish EVL deltas each shift; close epochs via QCEP.

---

## 13) Result
NeuroVest™ turns AI into **accountable behaviour**:  
transportable,  
certifiable,  
and governable across nations and industries  
without rewriting its core.

---

## Appendix A — Default Bands (CHS)
Baseline  — TCS ≥ 0.70, receipts contiguous over W = 24h.  
Silver    — TCS ≥ 0.80, receipts contiguous over W = 7d.  
Gold      — TCS ≥ 0.90, receipts contiguous over W = 30d.  
Diamond   — TCS ≥ 0.95, receipts contiguous over W = 90d + regulator witness.

---

## Appendix B — Receipt Schema (ts.receipt.v1)
actor_id:  
mandate_ref:  
hash_sha256:  
pqc_sig:  
forensic_flags: [ … ]  
ots_calendar_id:  
ots_status: <Pending | Receipt issued | Anchored | UNKNOWN>  
ots_tx:  
originstamp_id:  
btcstamp_tx:  
anchored_rfc3339:  

---

## Appendix C — Public/Ω Split
Public rules appear here.  
Ω doctrine, proofs, and Doctorantura capsules remain classified.

⸻

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
