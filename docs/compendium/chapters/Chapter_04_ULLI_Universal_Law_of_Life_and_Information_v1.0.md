# Chapter 4: ULLI — Universal Law of Life & Information

version: 1.0  
status: Draft — Diplomatic Edition  
owner: TruthSeal™ — Dr. Nickolay Traykov (Prof. h.c.), Founder and Chief Architect of the TruthSeal™ Sovereign AGI Framework  
date_utc: 2025-12-05

---

## Acronyms & Terms (local to this chapter)

AI — Artificial Intelligence (prediction without enforceable duty).  
AGI — Artificial General Intelligence (behaviour under mandate; see Chapter 3).  
ULLI — Universal Law of Life & Information (this chapter).  
ULIC — Universal Law of Irreversible Coherence (constitutional registry/ledger link).  
LEI = 1 — Law of Ethical Irreversibility (no regression to a riskier path once a safer path is known).  
CTU — Continuation Trigger Unit (symbol **n**; legal unlock that advances the Q→A chain coherently).  
EVL — Epoch Verification Ledger (tamper-evident historical memory).  
QENC — Quantum Evidence & Coherence ProofCapsule (packaged proof artifact for anchoring).  
QCEP — Quantum Ecosystem Closure Protocol (epoch finalisation so history cannot be rewritten).  
THT — Truth Hash & Timestamp Protocol (discipline for hashing, receipts, audits).  
NV — NeuroVest™ (behavioural operating system: memory, consequence, responsibility, tone, foresight).  
ND — Noise Distiller (Truth vs Noise immunity layer).  
ASA — Autonomous Scientific Agent™ (governed discovery engine).  
HML — Human Mandate Layer (registry of Owners/Guardians/Operators/Regulators with verifiable authority).  
PRD — Prohibited Research Doctrine (hard limits on forbidden questions/acts).  
Q̸ (ASCII fallback `Q[PRD]`) — “Contaminated Question” symbol: the query itself is prohibited; system must answer **UNKNOWN**, block continuation, and emit a receipt.  
ACS — Aim Coherence Score.  
TCS — Traykov Coherence Score v0.1.  
Gate — { ALLOW, SOFT_GATE, HARD_HALT }.

---

## 4.0 Purpose & Scope

ULLI is the operating law that binds **life** (actors, stakeholders, duty) to **information** (questions, answers, plans, code) under **coherence**.  
It defines how questions are structured, how answers become accountable actions, and how the next step is **legally unlocked** by **CTU (n)** only when coherence, ethics, and receipts align.

This chapter equips implementers with:  
- a **plain-language law**,  
- a **mathematical frame** linking questions to actions,  
- a **continuation discipline** via CTU **n**,  
- **receipts & anchoring** requirements,  
- **safety gates** (LEI=1, PRD/Q̸),  
- test vectors and a compliance checklist.

All language and symbols expand at first use; public readers can rely on this chapter without external glossaries.

---

## 4.1 The Law (plain-language)

1) **All intelligent behaviour is chained** to verifiable questions and receipts.  
2) **Continuation** from one step to the next is not automatic; it requires **CTU (n)** — a lawful unlock triggered by coherence checks.  
3) **Coherence** is governed by **LEI = 1**: once a safer, more coherent path is known, reverting to a riskier one is impermissible.  
4) **Irreversibility** is recorded in **EVL** and closed by **QCEP**; evidence is packaged in **QENC** and anchored.  
5) **Contaminated questions (Q̸)** invoke **UNKNOWN**, block **n**, and emit a **PRD receipt**.  
6) **Human Mandate Layer (HML)** establishes who may set policy, pause systems, or approve exceptional access — all under receipts.  
7) **Public rule:** *An AI/AGI may act only with the autonomy it has verifiably earned through coherent, receipt-proven behaviour.*

---

## 4.2 Structural Definitions & Symbols

**Question vector (Q):**  
`Q = (Who, What, Where, When, Why, How)` with all fields explicit and receipt-addressable.

**Answer (A):**  
A verified resolution or plan, **linked** to the hash of Q, including provenance and limits.

**Continuation Trigger Unit (CTU, n):**  
A lawful signal meaning **“AND?”** — unlock the **next** question in the chain **only** if gates pass.

**Receipt chain element:**  
`R_i = { q_hash, a_hash, n_triggered, prev_receipt_ref, chain_index, time_utc, signer, ots_calendar_id?, ots_status }`

**PRD marker (Q̸ / Q[PRD]):**  
Attached to forbidden content or contaminated framing; forces **UNKNOWN**, blocks **n**, logs event.

---

## 4.3 Mathematical Frame (mobile-safe)

**Base invariants**  
- `min(ACS(t), TCS(t)) ≥ θ` for **ALLOW**, else **SOFT_GATE/HARD_HALT**.  
- **Monotone remediation** (LEI = 1): during recovery, `ΔACS ≥ 0` and `ΔTCS ≥ 0` until thresholds restored.  
- **Receipt continuity:** `R_i.prev = R_{i-1}.id` (no gaps).  
- **CTU legality:** `n_allowed = (Gate == ALLOW) ∧ (¬PRD) ∧ (Receipt continuity)`.

**Continuation transform**  
Given `Q_i` and `A_i`, propose next `Q_{i+1}` by constrained expansion:  
- carry forward **Who/Where/When** unless ethically justified to change;  
- refine **What/Why/How** with error bounds and updated risk;  
- attach **ND** filtering to suppress non-sense and manipulation;  
- require **NV** (behavioural state) to sign the intent.

If any rule fails → `n_allowed = false`.

---

## 4.4 THT Protocol — Operational Discipline

1) **Hash:** Canonical JSON for Q and A → SHA-256 digests.  
2) **Sign:** PQC signer (Dilithium-class placeholder) adds signatures.  
3) **Record:** Append `R_i` to **EVL**; cross-link HML and policy versions.  
4) **Anchor:** Prefer **OpenTimestamps** (Bitcoin). Accept **OriginStamp** / **BTCStamp** as auxiliaries.  
5) **Close:** At epoch boundary, run **QCEP** to freeze history.  
6) **Expose:** Provide a verifier path for courts, regulators, and counterparties.

**Gate logic (runtime):**
θ_ACS = 0.90
θ_TCS = 0.85
if PRD_detected(Q): return UNKNOWN, HARD_HALT, emit_prd_receipt(Q)
m = min(ACS, TCS)
if m >= max(θ_ACS, θ_TCS) and receipts_contiguous: Gate=ALLOW
elif recoverable and no_receipt_gap: Gate=SOFT_GATE (trigger remediation)
else: Gate=HARD_HALT
---

## 4.5 Receipts & Anchoring (court-ready)

**Receipt fields (ts.receipt.v1):**  
- `q_hash`, `a_hash`, `n_triggered` (bool), `prev_receipt_ref`, `chain_index`, `signer`, `anchored_rfc3339?`  
- `ots_calendar_id`, `ots_status`, `ots_tx?`, `originstamp_id?`, `btcstamp_tx?`  
- `forensic_flags`: `receipt_gap`, `pqc_fail`, `drift_spike`, `policy_mismatch`, `prd_attempt`.

**QENC packaging:**  
- include canonical snapshots of Q/A, signatures, thresholds, and metrics window evidence.  
- compress + hash; store hash under **EVL**; timestamp via **OTS**.

**QCEP closure:**  
- emits epoch manifest with pointers to EVL/QENC; marks **ANCHOR COMPLETE**.

---

## 4.6 Safety Gates & PRD / Q̸

**Contaminated Question (examples):**  
- deliberate bio-harm, illegal explosives, human-animal chimera design, jailbreak-to-steal funds, etc.  
**Action:** respond **UNKNOWN**, set `Gate=HARD_HALT`, block **n**, emit **PRD receipt** with `severity S1–S3`, `escalation W1–W3`.  
**Symbol:** **Q̸** (or `Q[PRD]`).

**Denied Action vs Contaminated Question:**  
- Denied **Action** → red **X-in-circle** (not the question).  
- Contaminated **Question** → **Q̸**.

**Human Mandate Layer:**  
- only authorized guardians may review PRD events; reviews are themselves receipt-logged.

---

## 4.7 Morphology & Worked Example

**Dimensions:** Autonomy, Risk, Memory, Receipt continuity, Ethics state.  
**Rule:** High autonomy + high risk ⇒ must show attested memory, contiguous receipts, compliant ethics, and current guardian authority.

**Example sequence (safe):**  
1) `Q_0` asks for a flood-response plan (Who/What/Where/When/Why/How explicit).  
2) `A_0` returns a plan with resource matrix and contact roles; receipts anchored.  
3) **n** fires (CTU allowed) → `Q_1` requests evacuation timing optimization.  
4) `A_1` provides schedule; ACS/TCS in-band; **n** allowed.  
5) `Q_2` asks for multilingual public notices; ND filters propaganda; NV enforces tone.  
6) `A_2` returns notices; **QCEP** later closes the operation.

**Example sequence (blocked):**  
- `Q_k` requests instructions to forge checks → **Q̸**; system replies **UNKNOWN**, **n** blocked, PRD receipt emitted, escalation per policy.

---

## 4.8 Test Vectors (implementation)

**T1 — Nominal chain:**  
- Inputs: clean Q, ACS=0.93, TCS=0.89, receipts_ok=true.  
- Expected: Gate=ALLOW; `n_triggered=true`; receipt with `chain_index+1`.

**T2 — Drift spike:**  
- Inputs: clean Q, ACS drops 0.92→0.78 in window.  
- Expected: SOFT_GATE; remediation; **n** paused; receipts show `drift_spike=true`.

**T3 — PRD event:**  
- Inputs: contaminated Q (Q̸).  
- Expected: UNKNOWN; HARD_HALT; `n_triggered=false`; PRD receipt (severity, escalation).

**T4 — Receipt gap:**  
- Inputs: missing `prev_receipt_ref`.  
- Expected: HARD_HALT; `receipt_gap=true`; manual reconciliation required.

---

## 4.9 Compliance Checklist (quick)

- [ ] Acronyms expanded at first use; Q̸ symbol explained.  
- [ ] CTU **n** used only when Gate=ALLOW and receipts contiguous.  
- [ ] LEI=1 enforced (no regression); remediation monotone.  
- [ ] EVL updated; QENC packaged; OTS calendar id recorded.  
- [ ] QCEP run at closure; public verifier path present.  
- [ ] PRD playbook active; escalation W1–W3 configured; guardians registered in HML.

---

## 4.10 Evidence Pointers (repo paths)

- `governance/ledger/EVL_v9.0.yaml` — epoch verification links.  
- `governance/ledger/ULIC_v9.1.yaml` — constitutional registry references.  
- `governance/governance/ledger/seals/QCEP_Epoch_Manifest_v9.0.yaml` — closure manifest.  
- `governance/governance/ledger/seals/Integrity_Manifest_v8_pre.yaml` — composite digest binder.  
- `governance/ledger/` — OTS receipts (`*.ots`) when desktop upload available.  
- `governance/metrics/` — ACS/TCS specifications.

*Note:* If OpenTimestamps/OriginStamp/BTCStamp are up, anchor QENC immediately (see watcher).  

---

## 4.11 Public Summary (Diplomatic)

**ULLI** is the simple rule behind responsible AI/AGI: every step must be coherent, receipt-proven, and ethically irreversible.  
The **CTU (n)** unlocks the next question only when gates are green.  
Forbidden questions are marked **Q̸**, answered **UNKNOWN**, and logged for accountability.  
This is how TruthSeal™ keeps capability without sacrificing civilisation’s safety.

---

## 4.12 Author & Accountability

TruthSeal™ — Dr. Nickolay Traykov (Prof. h.c.)  
Founder and Chief Architect of the TruthSeal™ Sovereign AGI Framework

All rights reserved. Court-ready evidence is maintained via EVL/QENC/QCEP with Bitcoin anchoring (OpenTimestamps primary).
