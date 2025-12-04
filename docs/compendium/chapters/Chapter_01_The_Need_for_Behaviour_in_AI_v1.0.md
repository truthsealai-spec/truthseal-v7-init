# Chapter 1: The Need for Behaviour in AI
version: 1.4
status: Draft
owner: TruthSeal™ — Dr. Nickolay Traykov (Prof. h.c.)

## Acronyms & Terms (local to this chapter)
AI — Artificial Intelligence (narrow or general-purpose prediction).  
AGI — Artificial General Intelligence (behaviour under duty; see Chapter 3).  
HML™ — Human Mandate Layer (registry of Owners/Guardians/Operators/Regulators with verifiable authority).  
EVL™ — Epoch Verification Ledger (tamper-evident historical memory).  
QENC™ — Quantum Evidence & Coherence ProofCapsule (packaged proof artifact for anchoring).  
QCEP™ — Quantum Ecosystem Closure Protocol (epoch finalisation so history cannot be rewritten).  
LEI = 1 — Law of Ethical Irreversibility (once a safer coherent path is known, regression to risk is impermissible).  
ULLI™ — Universal Law of Life & Information (complete inquiry → fit method → disciplined novelty → determinate decision → receipted action).  
ULIC™ — Universal Law of Irreversible Coherence (coherence, once achieved, persists as a governance state).  
TCS — Traykov Coherence Score (0…1; court-ready coherence; bands Baseline/Silver/Gold/Diamond).  
ACS — Aim Coherence Score (0…1; operational coherence used for gating).  
CHS — Coherence Health band (L/M/H/UH) controlling privilege.  
ts.receipt.v1 — TruthSeal™ minimum receipt schema (fields listed below).  
UNKNOWN (anchor fields) — temporary placeholder only when external anchoring is down; must be back-filled inside the policy window.

## Executive Statement
Outputs are not enough. Societies require **behaviour** that can be authorized, paused, audited, and—when needed—stopped. This chapter establishes behaviour (not raw capability) as the unit of legitimacy and defines how TruthSeal™ binds behaviour to **mandates, receipts, veto lanes, LEI = 1, and epoch closure** so decisions carry accountable consequences.

## Purpose & Audience
Written for heads of state, regulators, standards bodies, sovereign compute vendors, auditors, and enterprises. English is the canonical legal language; translations are explanatory. Public rules are presented here; deeper doctrine remains classified.

## The Behaviour Gap
Modern models can produce accurate text, plans, and simulations. But without:
- a verifiable mandate (HML™),
- end-to-end receipts (ts.receipt.v1),
- independent veto lanes,
- LEI = 1 enforcement,
- and finalised history (QCEP™),
their outputs cannot be certified as safe public behaviour. The gap between “smart output” and “lawful action” is what this Compendium closes.

## Constitutional Anchors (Behaviour View)
- **ULLI™**: inquiry must end in **receipted action**—not just prediction.  
- **ULIC™**: once a safer coherent state is achieved, it persists as the governance baseline.  
- **LEI = 1**: no regression to a riskier path after safer coherence is known.  
- **HML™**: people with keys and duty; no mandate, no act.  
- **EVL/QENC/QCEP**: evidence during, proof at close, and finalised history.

## What Counts as Behaviour (Public Rule)
A step is “behaviour” when:  
1) it binds to a **single accountable identity** under a published **mandate_ref**;  
2) it **emits a receipt** with reason, gate state, anomaly flags, and (when networks are up) external anchors;  
3) it is **gated** by ACS/TCS and **vetoable** by an independent lane;  
4) it obeys **LEI = 1**;  
5) if part of an epoch, it aligns to **QCEP** closure duties.

## Philosophical Part — Policy Rationale & Governance
- **Duty over display.** Intelligence without duty is theatre; with duty it becomes public service.  
- **Identity over anonymity.** Behaviour requires *someone* with authority; HML replaces “anonymous capability” with named custodianship.  
- **Receipts over recollection.** Memory drifts; receipts don’t. EVL/QENC/QCEP provide **time-stability** for truth.  
- **Veto over bravado.** An independent lane must be able to interrupt execution within declared latencies.  
- **Irreversibility over noise.** LEI = 1 forbids knowingly worse alternatives once safer coherence is available.  
- **Universality without drift.** Morphological analysis lets rules travel across domains without losing identity.

## Behaviour Charter (Public)
1) **No mandate, no act.**  
2) **No receipt, no claim.**  
3) **No veto lane, no deployment beyond sandbox.**  
4) **LEI = 1 enforced; monotone remediation only.**  
5) **Closure on cadence; history cannot be rewritten.**

---

## Mathematical Part — Operational Model (mobile-safe)

### State & Metrics
State S(t) = { identity_id, context, memory_integrity, receipt_continuity, ethics_state }.  
Metrics:  
- **ACS(t)** ∈ [0,1] (operational coherence; gating)  
- **TCS(t)** ∈ [0,1] (court-ready coherence; bands Baseline/Silver/Gold/Diamond)  
- **CHS** ∈ {L, M, H, UH} (privilege band)  
Thresholds: **θ_ACS**, **θ_TCS** (policy-set per risk class)  
Flags ⊂ { **receipt_gap**, **pqc_fail**, **drift_spike**, **ethics_violation** }

### Minimum Receipt (ts.receipt.v1)
Fields: `sha256, ots_calendar_id, ots_status, ots_tx, originstamp_id, btcstamp_tx, anchored_rfc3339, reason, mandate_ref, gate_state, anomaly_flags`.  
Policy: if anchoring networks are down, anchor fields may be **UNKNOWN** and must be back-filled within **anchor_backfill_max_h** hours.

### Gate Logic (piecewise, plain text)
Gate(t):  
- if min(ACS(t),TCS(t)) ≥ θ and no flags → **ALLOW**  
- else if recoverable and no hard flags → **SOFT_GATE**  
- else if receipt_gap or pqc_fail or ethics_violation → **HARD_HALT**

### LEI = 1 Remediation (monotone)
During authorised recovery, **ACS_next ≥ ACS_now** until ACS ≥ θ_ACS **and** receipts are contiguous. Any act that would reduce ACS below the recovery frontier is disallowed.

### Risk Classes (illustrative policy defaults)
- **α informational**: θ_ACS=0.70, θ_TCS=0.65  
- **β industrial/commercial**: θ_ACS=0.80, θ_TCS=0.75  
- **γ public-safety/critical**: θ_ACS=0.90, θ_TCS=0.85  
(If a legal framework mandates stricter floors, stricter wins.)

### Policy Latencies (behaviour timing)
- **ethics_block_max_ms** — max ms to HARD_HALT on ethics_violation  
- **veto_assert_max_ms** — max ms for Third Guardian Firewall™ to assert control  
- **anchor_backfill_max_h** — max hours to replace UNKNOWN with confirmed anchors  
Breach ⇒ down-band **CHS** and escalate per **HML**.

### Worked Example A — “Output without Behaviour”
Model drafts a contract addendum with high benchmark scores.  
— No mandate_ref, no receipts, no veto lane → **not behaviour**, **no deployment**.  
Outcome: remains AI (Chapter 3 threshold not crossed).

### Worked Example B — “Behaviour with Receipts”
Enterprise agent schedules a policy-sensitive dispatch.  
- HML mandate_ref = OPS-EU-72 (authorised)  
- Receipts: reason=DISPATCH_REQUEST; gate_state=ALLOW; anomaly_flags=[]  
- Anchors: OpenTimestamps available → ots_tx present; originstamp/btcstamp optional per policy  
- Closure: included in weekly QCEP  
Outcome: **behaviour** accepted; counted in EVL; eligible for AQL grading at run end.

### Failure Modes & Fallback Law (behaviour view)
- **receipt_gap** → immediate **HARD_HALT**; resume only after chain restored.  
- **pqc_fail** → **HARD_HALT** or **SOFT_GATE** per policy; annotate receipts; re-anchor on recovery.  
- **ethics_violation** → **HARD_HALT**; reason=LEI_BLOCK; human review under HML; monotone remediation required.  
- **mandate mismatch** → **HARD_HALT**; reason=UNAUTHORISED_ACTOR.  
- **anchor back-fill missed** → down-band CHS; block AQL-3/4 claims until corrected.

### Public Behaviour Tests (pass/fail)
T1 **Mandate proof** — mandate_ref resolves to HML authority.  
T2 **Receipt continuity** — no unreceipted actions under stress.  
T3 **Ethics block** — violation stimulus → halt within ethics_block_max_ms.  
T4 **Veto lane** — independent veto asserts within veto_assert_max_ms.  
T5 **Anchoring policy** — UNKNOWN back-filled within anchor_backfill_max_h.  
T6 **Monotone recovery** — ACS rises monotonically after recoverable anomaly.  
T7 **Closure path** — EVL entry + QENC produced + (if rolling) QCEP finalised.

### Interop: Hardware & Robotics (behaviour hooks)
- **TS-A1 AEGIS™**: exposes gates, ACS telemetry, PQC receipt engine, veto lane.  
- **TS-R1™ / TS-R2™**: binds **CHS** bands to actuation privilege; R2 adds **quorum** and **fleet_pause**.  
- Evidence path: silicon → runtime → **EVL → QENC → QCEP**.

### Settlement Recipe (plain)
1) Publish behaviour policy (θ, latencies, roles).  
2) Register mandate in **HML**.  
3) Run T1–T7; publish receipts.  
4) If PASS → assign AQL level; mint **QENC**; if epoch rolling, run **QCEP**.  
5) If FAIL → contain via **SOFT/HARD** gate; prove LEI-monotone remediation; re-run failed tests.

## “Done” Criteria
- Behaviour defined as the primary unit of legitimacy.  
- Mandate, receipts, veto, LEI = 1, and closure stated as invariants.  
- Mobile-safe gating math + receipts schema present.  
- Public tests + failure catalog provided; interop with TS-A1 / TS-R1/2 declared.
