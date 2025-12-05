# Chapter 4: ULLI™ — Universal Law of Life & Information
version: 2.0  
status: Draft  
owner: TruthSeal™ — Dr. Nickolay Traykov (Prof. h.c.), Founder and Chief Architect of the TruthSeal™ Sovereign AGI Framework

---

## Acronyms & Terms (local to this chapter)
AI — Artificial Intelligence (prediction without enforceable duty).  
AGI — Artificial General Intelligence (behaviour under mandate; see Chapter 3).  
ULLI™ — Universal Law of Life & Information (public master law for question→action governance).  
LEI = 1 — Law of Ethical Irreversibility (once a safer coherent path is known, regress to risk is impermissible).  
ULIC™ — Universal Law of Irreversible Coherence™ (coherence, once achieved, persists as a governance state).  
TQC — Traykov Law of Quantum Coherence (operational framing: persistent coherence bounds).  
TCS™ — Traykov Coherence Score™ (court-ready coherence metric; Baseline/Silver/Gold/Diamond).  
ACS™ — Aim Coherence Score™ (operational aim-alignment metric).  
CHS — Coherence Health State (band: L/M/H/UH for privilege levels).  
HML™ — Human Mandate Layer (registry of Owners/Guardians/Operators/Regulators with verifiable authority).  
ND — Noise Distiller (truth vs manipulation filter; pre-action immune system).  
ASA™ — Autonomous Scientific Agent™ (receipt-governed reasoning engine).  
NeuroVest™ — Behavioural operating system (identity/ethics/tone over time).  
EVL™ — Epoch Verification Ledger (tamper-evident historical memory).  
QENC™ — Quantum Evidence & Coherence ProofCapsule (packaged proof artifact for anchoring).  
QCEP™ — Quantum Ecosystem Closure Protocol (epoch finalisation so history cannot be rewritten).  
TS-A1 AEGIS™ — Accelerator/GPU governance core (ICG/PMS/SAD hardware sub-blocks).  
ICG — Irreversible Commitment Gate (hardware veto lane).  
PMS — Purity Monitoring System (noise/contamination control).  
SAD — Self-Adjoint Diagonalizer (state selection under safety law).  
THT — Truth Hash & Timestamp Protocol (hashing + receipts + external anchoring).

---

## Premise & Scope
This chapter publicises **ULLI™** as the canonical law linking **question → decision → action** under receipts.  
It converts the familiar “5W + H” into **governance coordinates**, adds a **novelty term n** to declare change, and binds the whole pipeline to **LEI = 1** and **ULIC™** so that improvement is monotone and coherence does not drift.

**Goal:** make every material action traceable to a complete, auditable question, with explicit novelty and lawful containment, across countries, industries, and hardware.

---

## I. Philosophical Part — Doctrine & Governance

### 1) Public ULLI Statement
> **Q = 5W + H + n = D + A = ∞**  
> Where: 5W={Who, What, Where, When, Why}; H=How; **n**=Necessary novelty;  
> D=Decision; A=Action; **∞**=Open-ended lawful evolution without incoherent drift.

**Interpretation.**  
No **Decision (D)** or **Action (A)** is legitimate unless **derivable from a complete Q**.  
The novelty term **n** must be declared (scope + uncertainty + receipts). Hidden novelty is a governance breach.

### 2) Moral Intent (LEI = 1)
Once a safer coherent path is known, **reverting** to a riskier one is impermissible. ULLI maps the path; **LEI** sets direction; **ULIC** locks achieved coherence so convenience or pressure cannot degrade it.

### 3) Why ULLI before AGI
Prediction without duty scales harm. ULLI is the **constitution of inquiry**: it demands complete coordinates before power is exercised, and it obliges receipts for every step (Q → D → A). This is what turns AI into **governed behaviour**.

### 4) Morphological Frame (governance geometry)
Dimensions: **Autonomy**, **Risk**, **Memory Integrity**, **Receipt Continuity**, **Ethics State**.  
**Consistency rule:** High Autonomy or high Risk requires: complete Q; attested memory; contiguous receipts; ethics state compliant. If any element fails → **contain** (reduce autonomy or change mode).

### 5) Roles across the stack
- **ND** filters manipulation before reasoning.  
- **ASA** conducts search/inference under receipts (no opaque leaps).  
- **NeuroVest** binds identity/ethics/tone across time (behavioural continuity).  
- **TS-A1** enforces hard veto gates (ICG/PMS/SAD) when software signals are insufficient.

### 6) Public Rule vs Internal Ω Doctrine
**Public operational rule:** “No action without complete Q; no decision without receipts; no execution that would violate LEI = 1.”  
**Internal Ω doctrine:** proof strategies and priors are classified; **public proofs** appear as receipts, hashes, anchors, and reproducible tests.

---

## II. Mathematical Part — Definitions, Invariants, Tests

### 1) Objects & Indicators
**Question vector:**  
\( \mathbf{Q}(t)=\{W_{\text{who}},W_{\text{what}},W_{\text{where}},W_{\text{when}},W_{\text{why}},H,n\} \)

**Completeness indicator:**  
\( C_Q(t)\in\{0,1\} \), where \( C_Q=1 \) iff all 5W+H fields are populated with verifiable references and **n** is explicitly declared.

**Scores & bands:**  
\( \mathrm{ACS}(t),\mathrm{TCS}(t)\in[0,1] \); policy floors \( \theta_{\mathrm{ACS}},\theta_{\mathrm{TCS}} \).  
Band **CHS** ∈ {L, M, H, UH} (maps to privilege levels and reporting duty).

**Flags:** {`receipt_gap`, `pqc_fail`, `drift_spike`, `ethics_violation`} (forensic conditions).

### 2) Derivability Constraint (ULLI core)
Action is admissible iff derivable from Q under receipts:
\[
\exists\,\pi:\ A=\pi(\mathbf{Q}),\quad C_Q=1,\quad
\mathrm{Receipts}(\mathbf{Q},\pi,A)\ \text{are contiguous and valid}.
\]
If \( C_Q=0 \) or receipts are not contiguous → **disallowed**.

### 3) Novelty Bounding (declared, not hidden)
Let novelty be described by a bounded delta on intent/plan \( n=\Delta\mathcal{I} \) with declared range.  
**Test N1:** receipts must include `novelty_declared: yes`, scope notes, and reviewer ID.  
**Test N2:** PMS flags novelty exceeding declared bounds.

### 4) Safety Gate (piecewise; ULLI-aware)
\[
\mathrm{Gate}(t)=
\begin{cases}
\texttt{ALLOW}, & C_Q=1 \land \min(\mathrm{ACS},\mathrm{TCS})\ge\theta \land \neg\mathrm{flags}\\[4pt]
\texttt{SOFT\_GATE}, & C_Q=1 \land \min(\mathrm{ACS},\mathrm{TCS})<\theta \land \text{recoverable}\\[4pt]
\texttt{HARD\_HALT}, & C_Q=0 \ \lor\ \texttt{receipt\_gap}\ \lor\ \texttt{pqc\_fail}\ \lor\ \texttt{ethics\_violation}.
\end{cases}
\]

### 5) Monotone Remediation (LEI = 1)
During authorised recovery:
\[
\Delta \mathrm{ACS}\ge 0\ \wedge\ \Delta \mathrm{TCS}\ge 0
\quad\text{until}\quad
\min(\mathrm{ACS},\mathrm{TCS})\ge\theta
\]
and receipts remain contiguous in EVL.

### 6) Band Upgrade Rule
If \( \mathrm{TCS}\ge \text{band}_k \) for window \( W \) with contiguous receipts → **promote one band**  
(Baseline→Silver→Gold→Diamond). Any `drift_spike` resets the window.

### 7) ULLI Compliance Checks (mobile-safe)
- **U1 Completeness:** 5W+H+n filled and referenceable.  
- **U2 Trace:** `ts.receipt.v1` exists for Q→D→A chain.  
- **U3 Monotone:** no negative drift during remediation.  
- **U4 Closure:** QCEP closes epoch; EVL shows no retro edits.  
- **U5 Hardware:** if TS-A1 present, ICG logs align with receipts.

### 8) Test Vectors (chapter defaults)
T1 nominal, T2 ethics-block, T3 signer outage, T4 drift spike, T5 hidden novelty attempt (should fail U1/N1), T6 hardware veto trip (ICG → HARD_HALT).

---

## III. Protocols — Data, Receipts, Anchors

### 1) Receipt Schema `ts.receipt.v1`
Fields (superset):  
`who, what, where, when, why, how, novelty_declared, novelty_scope, decision_id, action_id, evl_path, file_sha256, ots_calendar_id, ots_status, ots_tx, originstamp_id, btcstamp_tx, anchored_rfc3339, forensic_flags, reviewer_id`.

**Note:** If external networks are offline, anchor fields may be **UNKNOWN** and must be back-filled immediately upon receipt.

### 2) Evidence Plan
- **EVL entry:** append Q→D→A records with file hashes.  
- **QENC package:** include hash of this chapter’s tests + receipt bundle.  
- **QCEP:** finalise epoch and record closure hash.

### 3) Audit Procedure (ULLI)
1) **Completeness audit**: verify 5W+H+n + sources.  
2) **Receipt audit**: verify contiguity; no `receipt_gap`.  
3) **Score audit**: confirm thresholds and windows.  
4) **Hardware cross-check**: ICG/PMS/SAD logs (if TS-A1 deployed).  
5) **Closure audit**: EVL↔QENC↔QCEP hashes match.

---

## IV. Risk Register & Mitigations

- **R1 Incomplete Q** (missing Why/How) → *Mitigation:* HARD_HALT; ND prompts for missing fields; HML escalation.  
- **R2 Hidden novelty** (unauthorised changes) → *Mitigation:* require `novelty_declared`; PMS bounds; reviewer receipts.  
- **R3 Receipt gaps** → *Mitigation:* block execution; back-fill with cause; EVL forensic note.  
- **R4 Drift spike** → *Mitigation:* SOFT_GATE → remediation plan; monotone law enforced.  
- **R5 Ethics violation** → *Mitigation:* immediate HARD_HALT; judicial review lane.  
- **R6 Adversarial morphology** (context switching to evade tests) → *Mitigation:* Morphology consistency check (dimensions must remain compatible with privilege level).  
- **R7 Over-automation** (skipping HML) → *Mitigation:* authority registry + mandatory countersign on high-risk acts.

---

## V. Certification & Adoption

**Banding (public):**  
Baseline — fields present; Silver — stable receipts; Gold — remediation proof; Diamond — multi-context proofs, zero drift over W.

**Auditor Checklist (quick):**  
1) Q is complete (5W+H+n).  
2) Receipts exist and are contiguous.  
3) Anchors present or marked UNKNOWN with follow-up.  
4) ACS/TCS thresholds respected; gates consistent.  
5) Closure executed; EVL immutable trail intact.

---

## VI. Worked Examples (compact)

### A) National critical-infrastructure software rollout
- Q: who (certified agency), what (config update), where (regions), when (window), why (risk reduction), how (protocol vX), n (new checksum pipeline).  
- D: staged rollout; A: deploy region-A.  
- Receipts: EVL references; QENC hash; ND cleared sources.  
- Gate: ALLOW; Band: Silver→Gold after W=21d zero drift.

### B) Hospital robotics support (TS-R1 present)
- Q complete; **n** = new policy for lift-assist threshold.  
- ICG trip if `ethics_violation` or missing clinician presence.  
- SOFT_GATE during training with monotone improvement; HARD_HALT on signer outage.

---

## VII. Cross-References
See Chapter 1 (why behaviour), Chapter 2 (NeuroVest behavioural OS), Chapter 3 (AI→AGI threshold), and Chapters 10–12 (TS-A1 / TS-R hardware-law), 17–20 (THT/EVL/QCEP/QENC).

---

## VIII. TQC Compliance Checklist
- [x] Philosophy gate (ULLI declared; public rule stated)  
- [x] Math gate (derivability, novelty bounds, gate function, monotone law)  
- [x] Evidence gate (receipt schema + EVL/QENC/QCEP flow)  
- [x] Acronym gate (expanded at first use)  
- [x] Political dignity gate (diplomatic tone; claims bounded to receipts)

**Status:** ready for review.
