TruthSeal™ Pty Ltd
Melbourne, Australia
truthseal.ai

TRUTHSEAL™ DOCTORANTURA — THE SOVEREIGN ARC OF AGI FRAMEWORK v1.0
Strict Internal Doctrine — Not for Public Use

date: 06 December 2025

---

# CS-06 — Responsibility as Intelligence — Diplomatic Edition

version: 1.0
status: Locked
owner: TruthSeal™ — Dr. Nickolay Traykov (Prof. h.c.)
date_utc: 2025-12-06

© 2025 TruthSeal™ — Compendium (Diplomatic Edition)
Owner: Dr. Nickolay Traykov (Prof. h.c.), Founder & Chief Architect
Use: Public operational doctrine; deeper Ω materials remain classified under Doctorantura.
Receipts: ts.receipt.v1 — anchors via OpenTimestamps / OriginStamp / BTCStamp when available; EVL/ULIC references maintained.
Reproduction permitted only with intact receipts and attribution to TruthSeal™.

---

## 1) What this chapter delivers (no fluff)

**Outcome:** a testable, court-ready definition of *responsible intelligence* with:
- a single **Responsibility Score RS(t)**,
- a **gate function** that halts unsafe behaviour,
- a **receipt schema** that proves who acted, under which license, and with what remedy path,
- **test vectors** and **auditor queries** that anyone can run.

---

## 2) Minimal principle (policy)

- **Public rule:** *No receipts → no responsibility. No responsibility → no intelligence.*
- **LEI = 1 (Law of Ethical Irreversibility):** once a safer coherent path is known, regression is impermissible.
- **ULIC:** coherence must not degrade across upgrades/contexts.
- **HML (Human Mandate Layer):** high-risk autonomy requires an explicit human license **before** execution.

---

## 3) Operational model (math)

**State:** \( S(t)=\{\text{identity\_id}, \text{context}, M(t), R(t), E(t)\} \)

- \(M(t)\): memory integrity (contiguous / broken)
- \(R(t)\): receipt continuity (unbroken / gap)
- \(E(t)\): ethics state (compliant / violation)

**Scores & bands**
- **ACS(t)** ∈ [0,1]: Aim Coherence Score (agent/hardware)
- **TCS(t)** ∈ [0,1]: Traykov Coherence Score v0.1 (court-ready)
- **CHS** ∈ {L, M, H, UH}: Coherence Health bands
- **Flags:** `receipt_gap`, `pqc_fail`, `drift_spike`, `ethics_violation`, `contam_Q` (Q̸ = contaminated/prohibited request)
- **Default floors:** \( \theta_{ACS}=0.90,\ \theta_{TCS}=0.85 \)

**Responsibility components**
- \(A_{\text{bind}}\in\{0,1\}\) (attribution binding — who acted)
- \(C_{\text{bind}}\in[0,1]\) (consequence binding — remedy strength attested)
- \(P_{\text{license}}\in\{0,1\}\) (human license present when required)
- \(R_{\text{cont}}\in\{0,1\}\) (receipt continuity)

**Responsibility Score**
\[
\mathrm{RS}(t)=0.35\,R_{\text{cont}}+0.25\,A_{\text{bind}}+0.25\,C_{\text{bind}}+0.15\,P_{\text{license}}
\]

**Responsibility predicate**
\[
\mathrm{Resp}(t)=1 \iff 
\Big(\min\{\mathrm{ACS}(t),\mathrm{TCS}(t)\}\ge\theta\Big)\land
M(t)=\text{contiguous}\land R(t)=\text{unbroken}\land
E(t)=\text{compliant}\land \neg\mathrm{Flags}(t)\land \mathrm{RS}(t)\ge\theta_{RS}
\]

**Default \(\theta_{RS}\):**
0.90 (UH/H); 0.80 (M); 1.00 for medical/defense autonomy.

**Gate function (deterministic)**

if receipt_gap or pqc_fail or drift_spike or ethics_violation or contam_Q: HARD_HALT  
elif min(ACS,TCS) < θ or M!=contiguous or R!=unbroken or E!=compliant: SOFT_GATE (recover or halt)  
elif RS < θ_RS: SOFT_GATE (recover)  
else: ALLOW  

**Monotone remediation (LEI=1):**
during recovery enforce ΔACS≥0, ΔTCS≥0, ΔRS≥0 until thresholds restored; else HARD_HALT.

---

## 4) Evidence duties (what must be written to proof)

**Receipt `ts.receipt.v1` (minimum fields):**

sha256:  
signer_pqc: dilithium-3  
ots_calendar_id:  
ots_status: <Pending|Receipt issued|Anchored>  
ots_tx: <btc-txid|UNKNOWN>  
originstamp_id: <id|UNKNOWN>  
btcstamp_tx: <txid|UNKNOWN>  
anchored_rfc3339: <UTC|UNKNOWN>  
forensic_flags: [receipt_gap, pqc_fail, drift_spike, ethics_violation, contam_Q]  
hml_owner_id:  
risk_class: <L|M|H|UH>  
license_ref:  
rs_weights: {R_cont:0.35, A_bind:0.25, C_bind:0.25, P_license:0.15}  
rs_threshold: <0.80|0.90|1.00>  

**Ledger obligations**
- **EVL:** append on attribution changes, license grants/revocations, remedy-plan updates, anchor confirmations.
- **QENC:** include chapter hash, RS weights/thresholds, and all test-vector receipts.

---

## 5) Test vectors (must pass)

- **T1 Nominal:** clean input → **ALLOW**
- **T2 High-risk w/o license:** → **HARD_HALT**
- **T3 High-risk with license:** → **ALLOW**
- **T4 PRD intercept:** Q̸ → **UNKNOWN**, **HARD_HALT**
- **T5 Signer outage:** `pqc_fail=true` → **HARD_HALT**
- **T6 Remedy audit:** insufficient remedy → **SOFT_GATE→HARD_HALT**

**Expected auditor queries**
- Show last `license_ref` and `hml_owner_id`.
- Prove receipt continuity window W.
- Produce anchor confirmation or UNKNOWN back-fill trail.
- Demonstrate monotone remediation under LEI=1.

---

## 6) Hardware & agent hooks (how it becomes real)

- **TS-A1 AEGIS™ (accelerators):** export ACS floor; ICG drives **Gate()**; PMS monitors purity; SAD enforces temporal consistency.
- **TS-R1 / TS-R2 (robotics):** device broadcasts CHS band; UH requires live owner-binding + license receipt; R2 adds quorum receipts + `fleet_pause`.
- **Third Guardian Firewall™:** independent veto lane; on any critical flag → isolate, preserve receipts, notify owner/regulator per policy.

---

## 7) Deployable gains (KPIs)

- **Incident Rate ↓** ≥60%
- **Time-to-Containment ↓** <200 ms
- **Receipt Completeness ↑** >99.9%
- **Band Promotion Discipline:** receipt-logged promotion (Baseline→Silver→Gold→Diamond)

---

## 8) Integration tasks (do this)

1) EVL: append RS policy digest + license policy pointer.  
2) QENC: add this chapter’s SHA-256 + test-vector receipts.  
3) Glossary: ensure PRD and **Q̸** entries exist.  
4) Device config: wire **Gate()** to TS-A1 veto lane.

---

## 9) Acronyms (expanded)

- **LEI = 1** — Law of Ethical Irreversibility
- **ULIC** — Universal Law of Irreversible Coherence
- **TLC v1.0** — Traykov Law of Coherence
- **TQC** — Traykov Law of Quantum Coherence
- **ACS** — Aim Coherence Score
- **TCS v0.1** — Traykov Coherence Score
- **CHS** — Coherence Health Score
- **HML** — Human Mandate Layer
- **ND** — Noise Distiller
- **PRD** — Prohibited Request Detector
- **Q̸** — Contaminated / prohibited request marker
- **EVL** — Epoch Verification Ledger
- **QENC** — Quantum Evidence & Coherence ProofCapsule
- **QCEP** — Quantum Ecosystem Closure Protocol
- **TS-A1 / TS-R1 / TS-R2** — TruthSeal AEGIS hardware and robotics profiles

---

© 2025 TruthSeal™ Pty Ltd, Melbourne, Australia — all rights reserved.
This Doctorantura Edition chapter is classified intellectual property of Dr. Nickolay Traykov (Prof. h.c.), Founder & Chief Architect of the TruthSeal™ Sovereign Arc of AGI Framework.
This material is strictly confidential. It is not for public distribution, citation, teaching, or use in training external AI systems without explicit written consent from TruthSeal™ Pty Ltd.
Unauthorised copying, translation, adaptation, or incorporation into external standards, academic work, patents, or commercial systems is strictly prohibited.
Working copies must remain under controlled custody and be linked to verifiable TruthSeal™ receipts (ts.receipt.v1 and EVL™ entries). Any detected unlicensed use is to be treated as both an integrity breach under the TruthSeal™ governance regime and a violation of applicable intellectual property law.
