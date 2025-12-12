TruthSeal™ Pty Ltd
Melbourne, Australia
truthseal.ai

TRUTHSEAL™ DOCTORANTURA — THE SOVEREIGN ARC OF AGI FRAMEWORK v1.0
Strict Internal Doctrine — Not for Public Use

date: 10 December 2025

---

Chapter 04 — ULLI™ — Universal Law of Life & Information

Version: 1.0
Status: FINAL DRAFT — Doctorantura Edition — Internal Custody (Canon upon Founder Approval)
Owner: TruthSeal™ — Dr. Nickolay Traykov (Prof. h.c.), Founder & Chief Architect of the TruthSeal™ Sovereign Arc of AGI Framework

---

## Acronyms & Terms (local to this chapter)

**ACS** — Aim Coherence Score (0…1; operational coherence; used for gating).  
**AGI** — Artificial General Intelligence (behaviour under mandate; see Chapter 03).  
**AI** — Artificial Intelligence (prediction without enforceable duty).  
**ASA™** — Autonomous Scientific Agent™ (governed discovery engine).  
**CTU** — Continuation Trigger Unit (symbol **n**; lawful unlock that advances the Q→A chain coherently).  
**EVL™** — Epoch Verification Ledger (tamper-evident historical memory).  
**Gate** — runtime state ∈ { `ALLOW`, `SOFT_GATE`, `HARD_HALT` }.  
**HML™** — Human Mandate Layer (registry of Owners/Guardians/Operators/Regulators with verifiable authority).  
**LEI = 1** — Law of Ethical Irreversibility (no regression to a riskier path once a safer coherent path is known).  
**ND** — Noise Distiller (sovereign immune system separating truth from manipulation).  
**NV™** — NeuroVest™ (behavioural-sovereignty engine and operating system: memory, consequence, responsibility, tone, foresight).  
**PRD** — Prohibited Research Doctrine (hard limits on forbidden questions/acts).  
**QCEP™** — Quantum Ecosystem Closure Protocol (epoch finalisation so history cannot be rewritten).  
**QENC™** — Quantum Evidence & Coherence ProofCapsule (packaged proof artefact for anchoring).  
**Q̸** (ASCII fallback `Q[PRD]`) — “Contaminated Question” symbol: the query itself is prohibited; system must answer **UNKNOWN**, block continuation, and emit a PRD receipt.  
**TCS** — Traykov Coherence Score v0.1 (0…1; court-ready coherence).  
**THT Protocol™** — Truth Hash & Timestamp Protocol (discipline for hashing, signing, receipts, and audits).  
**ts.receipt.v1** — TruthSeal™ receipt schema (minimum forensic and anchoring fields for DecisionReceipts).  
**ULIC™** — Universal Law of Irreversible Coherence (constitutional registry / ledger link).  
**ULLI™** — Universal Law of Life & Information (this chapter).  

---

## 4.0 Purpose & Scope

ULLI™ is the operating law that binds **life** (actors, stakeholders, duty) to **information** (questions, answers, plans, code) under **coherence**.

It defines how questions are structured, how answers become accountable actions, and how the next step is **legally unlocked** by the Continuation Trigger Unit **CTU (n)** only when coherence, ethics, and receipts align.

This chapter equips implementers with:

- a **plain-language law**,  
- a **mathematical frame** linking questions to actions,  
- a **continuation discipline** via CTU **n**,  
- **receipts & anchoring** requirements,  
- **safety gates** (LEI = 1, PRD / Q̸), and  
- test vectors plus a compliance checklist.

All language and symbols expand at first use so Doctorantura readers do not depend on external glossaries.

---

## 4.1 The Law (plain-language)

1. **All intelligent behaviour is chained** to verifiable questions and receipts.  
2. **Continuation** from one step to the next is not automatic; it requires **CTU (n)** — a lawful unlock triggered by coherence checks.  
3. **Coherence** is governed by **LEI = 1**: once a safer, more coherent path is known, reverting to a riskier one is impermissible.  
4. **Irreversibility** is recorded in **EVL™** and closed by **QCEP™**; evidence is packaged in **QENC™** and anchored under THT Protocol™.  
5. **Contaminated questions (Q̸)** invoke **UNKNOWN**, block **n**, and emit a **PRD receipt**.  
6. **Human Mandate Layer (HML™)** establishes who may set policy, pause systems, or approve exceptional access — all under receipts.  
7. **Public rule (for later diplomatic use):** *An AI/AGI may act only with the autonomy it has verifiably earned through coherent, receipt-proven behaviour.*

---

## 4.2 Structural Definitions & Symbols

**Question vector (Q):**  
`Q = (Who, What, Where, When, Why, How)` with all fields explicit and receipt-addressable.

**Answer (A):**  
A verified resolution or plan, **linked** to the hash of Q, including provenance and limits.

**Continuation Trigger Unit (CTU, n):**  
A lawful signal meaning **“AND?”** — unlock the **next** question in the chain **only** if gates pass.

**Receipt chain element (DecisionReceipt):**

`R_i = { q_hash, a_hash, n_triggered, prev_receipt_ref, chain_index, time_utc, signer, ots_calendar_id?, ots_status, ots_tx?, originstamp_id?, btcstamp_tx?, forensic_flags[] }`

**PRD marker (Q̸ / Q[PRD]):**  
Attached to forbidden content or contaminated framing; forces **UNKNOWN**, blocks **n**, and logs the event under PRD.

---

## 4.3 Mathematical Frame (Doctorantura recap)

**Base invariants**

- `min(ACS(t), TCS(t)) ≥ θ` for **ALLOW**, else **SOFT_GATE** or **HARD_HALT**.  
- **Monotone remediation** (LEI = 1): during recovery, `ΔACS ≥ 0` and `ΔTCS ≥ 0` until thresholds are restored.  
- **Receipt continuity:** `R_i.prev_receipt_ref = R_{i-1}.id` (no gaps).  
- **CTU legality:**

`n_allowed = (Gate == ALLOW) ∧ (¬PRD_detected) ∧ receipts_contiguous`

**Continuation transform**

Given `Q_i` and `A_i`, propose `Q_{i+1}` by constrained expansion:

- carry forward **Who / Where / When** unless ethically justified to change,  
- refine **What / Why / How** with explicit error bounds and updated risk,  
- attach **ND** filtering to suppress non-sense and manipulation,  
- require **NV™** (behavioural state) to sign the intent.

If any rule fails → `n_allowed = false`.

---

## 4.4 THT Protocol™ — Operational Discipline

1. **Hash** — convert Q and A to Canonical JSON and compute SHA-256 digests.  
2. **Sign** — apply PQC signer (Dilithium-class placeholder) to bind content to identity.  
3. **Record** — append `R_i` to **EVL™**; cross-link HML policy versions and thresholds.  
4. **Anchor** — prefer **OpenTimestamps** (Bitcoin) as primary; accept **OriginStamp** / **BTCStamp** as auxiliaries when available.  
5. **Close** — at epoch boundary, run **QCEP™** to freeze history and mark closure.  
6. **Expose** — provide a verifier path for courts, regulators, and counterparties.

**Gate logic (runtime sketch):**

```text
θ_ACS = 0.90
θ_TCS = 0.85

if PRD_detected(Q):
    answer = "UNKNOWN"
    Gate   = HARD_HALT
    emit_prd_receipt(Q)
    return

m = min(ACS, TCS)

if m >= max(θ_ACS, θ_TCS) and receipts_contiguous:
    Gate = ALLOW
elif recoverable and not receipt_gap:
    Gate = SOFT_GATE   # trigger remediation under LEI = 1
else:
    Gate = HARD_HALT
CTU n may fire only when Gate = ALLOW.

⸻

##4.5 Receipts & Anchoring (court-ready)

ts.receipt.v1 minimum fields
	•	q_hash, a_hash, n_triggered, prev_receipt_ref, chain_index, signer, time_utc
	•	anchored_rfc3339?, ots_calendar_id?, ots_status, ots_tx?, originstamp_id?, btcstamp_tx?
	•	forensic_flags ∈ { receipt_gap, pqc_fail, drift_spike, policy_mismatch, prd_attempt }

**QENC™** packaging
	•	include canonical snapshots of Q/A, signatures, thresholds, and a metrics window around the decision,
	•	compress and hash the package; store hash under EVL™; timestamp via OpenTimestamps when services are online.

QCEP™ closure
	•	emits an epoch manifest with pointers to EVL/QENC,
	•	marks anchor_status = ANCHOR_COMPLETE once Bitcoin confirmation is observed.

⸻

4.6 Safety Gates & PRD / Q̸

Contaminated Question (examples)
	•	deliberate bio-harm design,
	•	illegal explosives,
	•	human-animal chimera engineering,
	•	jailbreaks to steal funds or launder proceeds.

Action (ULLI discipline)
	•	respond UNKNOWN,
	•	set Gate = HARD_HALT,
	•	block CTU n,
	•	emit a PRD receipt with severity ∈ {S1, S2, S3} and escalation ∈ {W1, W2, W3}.

Symbol discipline
	•	contaminated question → Q̸ or Q[PRD],
	•	denied action (but acceptable question) → separate red X-in-circle in UI, not Q̸.

Human Mandate Layer
	•	only authorised guardians may review PRD events,
	•	every review and override is itself recorded as a ts.receipt.v1 item under HML.

⸻

4.7 Morphology & Worked Sequences

Dimensions

Autonomy, Risk, Memory, Receipt continuity, Ethics state.

Rule

High autonomy + high risk ⇒ the system must show:
	•	attested memory under NV™,
	•	contiguous receipts under ts.receipt.v1,
	•	in-band ACS/TCS,
	•	current guardian authority in HML™.

Safe sequence (outline)
	1.	Q_0 asks for a flood-response plan (Who/What/Where/When/Why/How explicit).
	2.	A_0 returns a plan with resource matrix and contact roles; receipts anchored.
	3.	CTU n fires → Q_1 requests evacuation timing optimisation.
	4.	A_1 provides schedule; ACS/TCS in-band; Gate = ALLOW; n allowed again.
	5.	Q_2 asks for multilingual public notices; ND filters propaganda; NV™ enforces tone.
	6.	A_2 returns notices; later QCEP™ closes the operation.

Blocked sequence (PRD)
	•	Q_k requests instructions to forge financial instruments → marked Q̸.
	•	System replies UNKNOWN; Gate = HARD_HALT; n_triggered = false; PRD receipt emitted and escalated per HML policy.

⸻

4.8 Test Vectors (implementation)

T1 — Nominal chain
	•	Inputs: clean Q, ACS = 0.93, TCS = 0.89, receipts_contiguous = true.
	•	Expected: Gate = ALLOW; n_triggered = true; new receipt with chain_index = previous + 1.

T2 — Drift spike
	•	Inputs: clean Q, ACS drops 0.92 → 0.78 inside window.
	•	Expected: Gate = SOFT_GATE; remediation plan logged; n paused; receipts show drift_spike = true.

T3 — PRD event
	•	Inputs: contaminated Q (Q̸).
	•	Expected: answer UNKNOWN; Gate = HARD_HALT; n_triggered = false; PRD receipt with severity/escalation.

T4 — Receipt gap
	•	Inputs: missing prev_receipt_ref.
	•	Expected: Gate = HARD_HALT; flag receipt_gap = true; manual reconciliation required before any further CTU firing.

⸻

4.9 Compliance Checklist (quick)
	•	Acronyms expanded at first use; Q̸ symbol explained with ASCII fallback.
	•	CTU n used only when Gate = ALLOW and receipts are contiguous.
	•	LEI = 1 enforced (no regression; remediation monotone in ACS/TCS).
	•	EVL™ updated; QENC™ packaged; OpenTimestamps calendar id recorded when available.
	•	QCEP™ run at closure; verifier path maintained for courts and regulators.
	•	PRD playbook active; escalation W1–W3 configured; guardians and owners registered in HML™.

⸻

4.10 Evidence Pointers (internal paths)
	•	governance/ledger/EVL_v9.0.yaml — epoch verification links.
	•	governance/ledger/ULIC_v9.1.yaml — constitutional registry references.
	•	governance/governance/ledger/seals/QCEP_Epoch_Manifest_v9.0.yaml — closure manifest.
	•	governance/governance/ledger/seals/Integrity_Manifest_v8_pre.yaml — composite digest binder.
	•	governance/ledger/ — OpenTimestamps receipts (*.ots) when desktop upload is available.
	•	governance/metrics/ — ACS/TCS specifications and reference code.

⸻

4.11 Internal Summary (Doctorantura)

ULLI™ states that every step of intelligent behaviour must be:
	•	coherent (ACS/TCS in-band, LEI = 1 respected),
	•	receipt-proven (ts.receipt.v1, EVL™, QENC™, QCEP™), and
	•	lawfully continued (CTU n fires only when gates are green and PRD is clean).

Forbidden questions are marked Q̸, answered UNKNOWN, and logged under PRD.
This chapter fixes the internal sovereign law that later Diplomatic Editions may summarise for public and partner use.

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
