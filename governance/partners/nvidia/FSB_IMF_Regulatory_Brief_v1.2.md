## Why TruthSeal™ exists (for regulators and supervisors)
TruthSeal™ is an integrity and governance layer for high-risk AI and emerging AGI-class systems, secured with post-quantum cryptography (PQC).
TruthSeal™ exists to make high-risk automated decisions traceable, auditable,
and stoppable in real time. We attach cryptographic receipts and integrity
checks to every critical decision, creating a tamper-evident chain from input
to outcome that supervisors and auditors can independently review. By enforcing
coherence and non-repudiation in hardware and software, TruthSeal reduces model
opacity, supports enforceable accountability, and helps institutions comply
with emerging AI and operational-risk regulations.

### What supervisors actually get
- A tamper-evident receipt for every high-risk automated decision (who, what, when, under which policy).
- A real-time veto lane: hardware-backed signals that can pause or block incoherent or non-compliant runs.
- An audit-ready trail that maps model behavior to accountable humans and institutions, not just to “the system”.
- 
# FSB/IMF Regulatory Brief — Converting Unpriced Tail-Risk into Structural Certainty (v1.2, Private)

**Purpose**  
Vendor-neutral, audit-ready framing for supervisors to evaluate **hardware-attested integrity** and adopt **ACS** as a fiduciary disclosure via a 120-day pilot.
This brief is backed by the internal TS-A1 Hardware Law v1.0, which defines
the minimum non-negotiable rules that the governance core must enforce in
silicon.

---

## 1) Executive Hook

**Title:** Converting Unpriced Tail-Risk into Structural Certainty

**Opening (copy-ready):**  
Madam Chair, Governors: Global finance carries concentrated **unpriced tail-risk**. AI-enabled controls still rely on **probabilistic safety** \((P_C = 1-\varepsilon)\), leaving a residual failure term \(\varepsilon\) inside every critical system.

We propose a **verifiable standard** that removes \(\varepsilon\) from the control plane. **TruthSeal™** introduces the **Aim Coherence Score (ACS)**—a hardware-attested integrity metric emitted by a **reference architecture** (the **TQC Coherence Core**) that enforces **LEI=1** and synchronizes subsystems via a **Coherence Sync Fabric**. **ACS converts “trust” into a continuous, cryptographically signed telemetry stream** supervisors can audit in real time.

**Request:** a joint **120-day evaluation**. Instrument one supervised SIFI with ACS and compare tail-risk proxies—model overrides, control breaches, incoherence incidents, and loss events—against baseline. Outcomes inform a **principles-based, vendor-neutral** standard for **hardware-enforced integrity** in AI-enabled finance.

---

## 2) ACS: computation & attestation (what supervisors receive)

- **Cadence:** 10–1000 Hz from a hardware root of trust.  
- **Payload:** `acs ∈ [0,1]`, `ctx_hash`, `nonce`, `monotonic_counter`, `device_id`, `pqc_sig` (NIST ML-DSA class, e.g., Dilithium).  
- **Policy ladder:** T1 warn → T2 quarantine → T3 shutdown (**enforced in hardware**).  
- **Receipts:** Event = payload + PQC signature + public timestamp anchor (e.g., OpenTimestamps).  
- **Assurance:** Regulators replay signatures, counters, and anchors offline.

---

## 3) 120-Day Evaluation Plan

1. **Scope:** One critical AI flow (e.g., market risk or settlement control).  
2. **Success:** Fewer incoherence incidents; lower override rate; faster detect/quarantine; loss correlation.  
3. **Artifacts:** Signed ACS streams, event receipts, anchor proofs, replay tools.  
4. **Governance:** Joint WG; weekly drops; 30/60/120-day reviews; final methods note.

---

## 4) The Three Mandates (technology-neutral wording)

### Mandate 1 — Fiduciary ACS Disclosure
**Justification:** ACS exposes incoherence in real time under **LEI=1** with synchronized control fabric.  
**Regulatory action:** Require SIFIs using AI in trading/risk/settlement to **instrument ACS**, retain **signed receipts**, and **report thresholds/incidents** (map to Basel OpRes & Pillar 3).

### Mandate 2 — Hardware-Attested Integrity Control
**Justification:** Integrity must be **physically enforced**, not only statistically. LEI-gate + Coherence Sync Fabric + Receipt Engine give deterministic guardrails.  
**Regulatory action:** **Mandate capability**, not vendor: for critical AI workloads, use **hardware-attested integrity** functionally equivalent to **LEI-gate, Coherence Sync Fabric, Receipt Engine**. TruthSeal’s TQC Core is a **reference implementation**.

### Mandate 3 — Post-Quantum Receipts & Chain-of-Custody
**Justification:** Receipts must remain verifiable under future cryptanalysis.  
**Regulatory action:** Standardize PQC signatures, **monotonic counters**, and **public time-anchoring** for ACS receipts; require immutable retention and **regulator replay APIs**.

---

## 5) Regulatory mapping

- **SR 11-7** (model risk): ACS receipts → monitoring & outcomes evidence.  
- **Basel Principles for Operational Resilience:** ACS → ICT resilience metrics.  
- **EU DORA:** continuous monitoring/logging evidence.  
- **NIST AI RMF 1.0:** ACS enables **Measure** with cryptographic assurance.  
- **ISO/IEC 42001:** ACS receipts as auditable controls & KPIs.

---

## 6) Lexicon

- **ULLI (principle):** stability inseparable from information integrity. *Not* a hardware block.  
- **TQC Coherence Core (reference):** integrity IP that enforces **LEI=1**; provides **LEI-gate**, **Coherence Sync Fabric**, **Receipt Engine**.  
- **ACS:** attested coherence metric (0–1).  
- **Receipt:** signed ACS event with counter + anchor proof.

---

## 7) Next step

Adopt the **120-day evaluation** and convene a joint methods group to finalize thresholds, artifact formats, and disclosure templates. Publish a **technology-neutral supervisory statement** establishing ACS-class telemetry and receipts as the **fiduciary integrity standard** for AI-enabled finance.
