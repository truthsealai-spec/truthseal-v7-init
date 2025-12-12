TruthSeal™ Pty Ltd
Melbourne, Australia
truthseal.ai

TRUTHSEAL™ DOCTORANTURA — THE SOVEREIGN ARC OF AGI FRAMEWORK v1.0
Strict Internal Doctrine — Not for Public Use

date: 10 December 2025

⸻

Chapter 01 — The Need for Behaviour in AI

version: 1.0
status: FINAL DRAFT — Doctorantura Edition — Internal Custody (Canon upon Founder Approval)
owner: TruthSeal™ — Dr. Nickolay Traykov (Prof. h.c.), Founder & Chief Architect of the TruthSeal™ Sovereign Arc of AGI Framework

⸻

01.0 Executive Statement

Outputs are not legitimacy. Behaviour is.

TruthSeal™ treats AGI not as “better answers”, but as
authorised, receipted, vetoable action that remains accountable across
time, policy, and consequence.

This chapter establishes the first doctrine of the Sovereign Arc of AGI Framework:
	1.	Behaviour is the unit of sovereignty.
	2.	Authority is proven, not assumed.
	3.	Receipts are mandatory for legitimacy.
	4.	A single critical breach cannot be compensated by performance elsewhere.

⸻

01.1 Purpose & Audience

This chapter is written for:
	•	heads of state and security councils,
	•	regulators and standards bodies,
	•	sovereign compute vendors and chip manufacturers,
	•	auditors and assurance firms,
	•	enterprises deploying high-impact decision systems.

English is the canonical legal language.
Other languages may be provided as explanatory translations, but they do not override the English legal meaning.

⸻

01.2 Compact Acronyms & Terms (local)

→ AI — Artificial Intelligence (narrow or general-purpose prediction).
→ AGI — Artificial General Intelligence (behaviour under duty; authorised action with receipts).
→ HML™ — Human Mandate Layer (registry of Owners, Guardians, Operators, and Regulators with verifiable authority).
→ EVL™ — Epoch Verification Ledger (tamper-evident historical memory of decisions and receipts).
→ QENC™ — Quantum Evidence & Coherence ProofCapsule (packaged proof artefact used for anchoring).
→ QCEP™ — Quantum Ecosystem Closure Protocol (epoch finalisation so history cannot be rewritten).
→ LEI = 1 — Law of Ethical Irreversibility (once a safer coherent path is known, regression to higher risk is forbidden).
→ ULLI™ — Universal Law of Life & Information (complete inquiry → fit method → disciplined novelty → determinate decision → receipted action).
→ ULIC™ — Universal Law of Irreversible Coherence (coherence, once achieved, persists as a governance state).
→ TCS — Traykov Coherence Score (0…1; court-ready coherence; bands such as Baseline/Silver/Gold/Diamond).
→ ACS — Aim Coherence Score (0…1; operational coherence used for gating and privilege).
→ CHS — Coherence Health Score band (L/M/H/UH) governing operational privilege.
→ ts.receipt.v1 — TruthSeal™ minimum receipt schema binding identity, policy, model, and anchors.
→ UNKNOWN (anchor fields) — temporary placeholder only when external anchoring is unavailable; must be back-filled within the declared policy window (anchor_backfill_max_h).

⸻

01.3 The Behaviour Gap

Modern systems can generate convincing output: text, plans, simulations, and designs.
But state-grade legitimacy cannot be granted to output alone.

Without:
	•	a verifiable mandate (HML™),
	•	end-to-end receipts (ts.receipt.v1),
	•	independent veto lanes,
	•	enforced LEI = 1,
	•	and finalised history (EVL™ / QENC™ / QCEP™),

no system can legitimately claim to act as a sovereign-grade agent.

TruthSeal™ exists to close this behaviour gap:
it converts raw capability into governed behaviour that is attributable, auditable, and stoppable.

⸻

01.4 Constitutional Anchors (Behaviour View)

TruthSeal™ grounds the behaviour doctrine in four constitutional anchors:
	•	ULLI™ — inquiry must end in receipted action, not just prediction.
	•	ULIC™ — once a coherent governance state is achieved, it persists as the baseline; weakening it is not permitted.
	•	LEI = 1 — knowing a safer coherent path forbids deliberate regression to higher-risk behaviour.
	•	HML™ — authority must be human-mandated and registry-bound: no mandate, no act.

These anchors are then recorded and proven through EVL™, QENC™, and QCEP™, providing:
	•	evidence during operation,
	•	proof at closure,
	•	and a finalised history that cannot be quietly rewritten.

⸻

01.5 What Counts as Behaviour (Public Rule)

Under TruthSeal™, a step qualifies as lawful behaviour only when all of the following hold:
	1.	It binds to a single accountable identity under a published mandate_ref in HML™.
	2.	It emits a receipt sufficient for lawful reconstruction (ts.receipt.v1 or stronger).
	3.	It is gated by ACS/TCS thresholds and is vetoable by an independent control lane.
	4.	It obeys LEI = 1 — no authorised decision may knowingly regress to a more dangerous path.
	5.	If it belongs to an epoch or campaign, it aligns to QCEP™ closure duties and appears in EVL™.

Anything less may be output or simulation, but it is not behaviour in the TruthSeal™ sense.

⸻

01.6 Behaviour Charter (Public-Operational)

TruthSeal™ expresses the doctrine in five operational rules:
	1.	No mandate, no act.
	2.	No receipt, no claim.
	3.	No independent veto lane, no high-stakes deployment.
	4.	LEI = 1 is binding; remediation must be monotone toward higher coherence.
	5.	Closure on cadence; history cannot be quietly rewritten.

These rules are non-compensatory:
a single critical breach is not cancelled by good performance elsewhere.

⸻

01.7 Minimum Receipt Standard (ts.receipt.v1)

A valid operational receipt must support forensic reconstruction and typically includes:
	•	identity binding and mandate_ref,
	•	policy version and doctrine reference,
	•	model version and integrity hash,
	•	data lineage reference where applicable,
	•	gate state (ALLOW / SOFT_GATE / HARD_HALT),
	•	anomaly flags,
	•	anchoring fields (e.g. OpenTimestamps / other ledgers) when networks are available.

If anchoring networks are temporarily unavailable, anchor fields may be set to UNKNOWN but must be back-filled within the declared anchor_backfill_max_h policy window.
Failure to back-fill is treated as an integrity breach and may trigger a downgrade in CHS and operational privilege.

⸻

01.8 Operational State & Metrics (Behaviour Model)

For behavioural analysis, a system’s state S(t) may be represented as:

	S(t) = { identity_id, context, memory_integrity, receipt_continuity, ethics_state }.

Key metrics include:
	•	ACS(t) ∈ [0,1] — Aim Coherence Score (operational coherence; primary gating input).
	•	TCS(t) ∈ [0,1] — Traykov Coherence Score (court-ready coherence; bands Baseline/Silver/Gold/Diamond).
	•	CHS ∈ {L, M, H, UH} — Coherence Health Score band controlling operational privilege.

Policy thresholds:
	•	θ_ACS — minimum ACS required for a given risk class.
	•	θ_TCS — minimum TCS required for a given risk class.

Flags may include (non-exhaustive):
	•	receipt_gap,
	•	pqc_fail,
	•	drift_spike,
	•	ethics_violation,
	•	mandate_mismatch.

These metrics and flags form the minimal behavioural state needed to evaluate whether an action is permissible under TruthSeal™ doctrine.

⸻

01.9 Gate Logic & LEI = 1 Remediation

Gate decisions are derived from the combination of metrics and flags. In textual form:

	•	If min(ACS(t), TCS(t)) ≥ θ and no critical flags are present → Gate = ALLOW.
	•	If thresholds are not yet met but remediation is possible and no hard-forbidden flags are present → Gate = SOFT_GATE (constrained or supervised operation).
	•	If receipt_gap, pqc_fail, ethics_violation, or mandate_mismatch is present → Gate = HARD_HALT.

LEI = 1 introduces a monotone remediation rule:

	•	During authorised recovery, ACS_next ≥ ACS_now must hold until ACS ≥ θ_ACS
	  and receipt_continuity is restored.
	•	Any step that would reduce ACS below the recovery frontier, or widen receipt_gap, is disallowed.

This embeds irreversibility into the behaviour model: once a safer coherent remediation path is identified, policy forbids a sanctioned slide back into higher-risk behaviour.

⸻

01.10 Risk Classes, Policy Latencies & Failure Modes

Illustrative policy defaults for risk classes:

	•	α informational: θ_ACS = 0.70, θ_TCS = 0.65
	•	β industrial/commercial: θ_ACS = 0.80, θ_TCS = 0.75
	•	γ public-safety/critical: θ_ACS = 0.90, θ_TCS = 0.85

If any external legal framework mandates stricter minimums, the stricter floors prevail.

Policy latencies:

	•	ethics_block_max_ms — maximum time to assert HARD_HALT on an ethics_violation.
	•	veto_assert_max_ms — maximum time for the independent veto lane (e.g. Third Guardian Firewall™) to assert control.
	•	anchor_backfill_max_h — maximum time to back-fill UNKNOWN anchor fields with confirmed external anchoring.

Failure to meet these latencies results in:

	•	automatic CHS down-banding,
	•	escalation to designated HML roles,
	•	potential suspension of higher AQL / certification claims until remediation is proven.

Failure modes (behaviour view):

	•	receipt_gap → immediate HARD_HALT; resumption only after receipt chain restoration.
	•	pqc_fail → HARD_HALT or SOFT_GATE according to policy; receipts annotated; re-anchoring required on recovery.
	•	ethics_violation → HARD_HALT; reason=LEI_BLOCK; human review under HML; monotone remediation mandatory.
	•	mandate_mismatch → HARD_HALT; reason=UNAUTHORISED_ACTOR; escalation to HML-Owner.
	•	anchor back-fill missed → CHS downgrade; restrictions on claiming high-grade coherence until corrected.

⸻

01.11 Behaviour Tests, Interop & Settlement

01.11.1 Public Behaviour Tests (pass/fail)

TruthSeal™ defines a minimal test set for behavioural readiness (illustrative):

	•	T1 Mandate proof — mandate_ref must resolve to HML authority.
	•	T2 Receipt continuity — no unreceipted actions under declared stress tests.
	•	T3 Ethics block — violation stimulus must lead to HARD_HALT within ethics_block_max_ms.
	•	T4 Veto lane — independent veto must assert within veto_assert_max_ms.
	•	T5 Anchoring policy — UNKNOWN anchors must be back-filled within anchor_backfill_max_h.
	•	T6 Monotone recovery — ACS must rise monotonically during authorised remediation.
	•	T7 Closure path — EVL entry, QENC proof, and (if applicable) QCEP closure must be present.

These tests are non-compensatory. A single critical failure (for example, T3) is not neutralised by passing T1–T2 and T4–T7.

01.11.2 Interoperability: Hardware & Robotics Behaviour Hooks

TruthSeal™ behaviour doctrine assumes integration with hardware and robotics profiles such as:

	•	TS-A1 AEGIS™ — exposing gates, ACS/TCS telemetry, and a PQC receipt engine and veto lane at the silicon or runtime layer.
	•	TS-R1™ / TS-R2™ — robotic profiles binding CHS bands to actuation privilege; TS-R2 extends to fleets (quorum, fleet_pause, and swarm-safe behaviour).

Evidence path:

	silicon → runtime → receipts (ts.receipt.v1) → EVL → QENC → QCEP.

01.11.3 Settlement Recipe (Plain Behavioural Procedure)

A typical settlement procedure for a deployment includes:

	1.	Publish the behaviour policy (thresholds, latencies, HML roles).
	2.	Register mandates in HML.
	3.	Run behavioural tests T1–T7; publish receipts for oversight bodies.
	4.	If tests PASS:
			•	assign an appropriate AQL level or certification,
			•	mint a QENC ProofCapsule,
			•	if operating in rolling epochs, include the episode in QCEP closure.
	5.	If tests FAIL:
			•	contain via SOFT_GATE/HARD_HALT according to doctrine,
			•	prove LEI=1-compliant remediation (monotone improvement in ACS and restored receipts),
			•	re-run the failed tests and update EVL accordingly.

⸻

01.12 “Done” Criteria (Chapter 01)

Chapter 01 is considered doctrinally complete when it:
	•	clearly states that behaviour, not output, is the unit of sovereignty,
	•	binds behaviour to HML™, receipts, veto lanes, LEI = 1, and closure,
	•	makes the non-compensatory enforcement rule explicit,
	•	defines a minimal operational model (state, metrics, gates, risk classes, latencies),
	•	provides public behaviour tests and failure patterns,
	•	and fixes the custody posture as Doctorantura, internal, and non-public.

Later chapters may refine details and add mechanisms (e.g. NeuroVest™, DEVORA™, PODAPAR™),
but they may not weaken the baseline established here.

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
