# TruthSeal™ — TS-R CHS Law & Thresholds v1.0

version: 1.0  
date_utc: 2025-12-02  
owner: TruthSeal™ — Dr. Nickolay Traykov (Prof. h.c.)  

scope: |
  Internal specification for the Coherence Health Score (CHS) law and
  numeric thresholds used by TruthSeal Robotics Profiles TS-R1 and TS-R2.
  This document defines:
    - how CHS bands (CHS/L, CHS/M, CHS/H, CHS/UH) relate to TCS v0.1 and ACS,
    - the minimum numeric thresholds required for each band,
    - how CHS interacts with Traykov hardware law, safety rules, and fallback.
  It is binding for robotics engineering, Devora UX, auditors, and partners.

  NOTE: This file locks CHS numeric thresholds and CHS law semantics.
  Action-level policies per band stay in:
    - TS-R Cherry Checklist v1.0,
    - TS-R Failure Modes & Fallback Law v1.0,
    - TS-R Human Mandate Layer v1.0,
    - TS-R Swarm Extensions v1.0,
    - TS-R Economic Impact Note v1.0.

---

## 0. Core Concepts (expanded once)

- **Aim Coherence Score (ACS)** — 0–1 metric that measures how well robot
  or fleet actions follow the declared aim and safety constraints over time.

- **Traykov Coherence Score v0.1 (TCS v0.1)** — 0–1 metric for overall
  intelligence coherence (truthfulness, post-quantum security strength,
  long-horizon self-consistency).

- **Coherence Health Score (CHS)** — four-band status indicator for a robot
  or swarm:
  - **CHS/L** — Low (Red),
  - **CHS/M** — Medium (Yellow),
  - **CHS/H** — High (Green),
  - **CHS/UH** — Ultra High (Blue).

- **Traykov Law of Quantum Coherence (TQC)** — hardware-anchored law that
  demands non-degrading coherence behaviour over time; no “free lunch” in
  risk. Coherence must improve or stay stable under approved updates.

- **Law of Ethical Irreversibility (LEI = 1)** — law that forbids the system
  from downgrading back to a worse, riskier state once a safer state is
  attained. No regressions into higher-risk operating modes.

- **ULLI** — TruthSeal governing proof mandate composed of:
  - Academic Authority Proof,
  - Technical Immutability Proof,
  - Live Measurability Proof.
  (Full doctrinal expansion lives in Doctorantura.)

- **TS-R1** — TruthSeal Robotics Profile for a single robot (individual unit).

- **TS-R2** — TruthSeal Robotics Profile for a swarm or fleet of robots.

---

## 1. CHS Law — High-Level Rules

### 1.1 Purpose

The Coherence Health Score (CHS) is a **visible health law** for robots and
fleets. It compresses complex metrics (TCS v0.1, ACS, safety flags) into
four bands that humans can understand at a glance, and that robots MUST
obey for actuation, money movement, and sensitive behaviour.

### 1.2 Invariants

Under TQC, LEI = 1, and ULLI:

1. **Monotonic safety**  
   - Once a robot has legitimately reached a safer band, it must NOT return
     to a more dangerous band without:
       - recorded justification, and
       - a fallback ladder defined in Failure Modes & Fallback Law v1.0.

2. **Metric-grounded status**  
   - CHS is **derived** from:
       - TCS v0.1 (overall intelligence coherence),
       - ACS (action-level aim alignment),
       - active safety flags (environment, children, unknown humans, etc.).
   - No manual override may show “Blue” or “Green” if metrics do not meet
     the numeric thresholds in this file.

3. **Local truthfulness**  
   - If metrics are unavailable or corrupted, CHS MUST degrade to:
       - CHS/L (Red) or CHS/M (Yellow), never “guessing” High or Ultra High.
   - Unknown state is treated as unsafe state.

4. **Global consistency**  
   - For a TS-R2 swarm, no member robot may operate at a higher CHS band
     than the swarm’s aggregate band. The swarm band is the **minimum**
     across:
       - core members,
       - safety-critical roles,
       - communication and control nodes.

---

## 2. Inputs to CHS

CHS is computed from three inputs:

1. **TCS v0.1** — numeric score in `[0.00, 1.00]`.
2. **ACS** — numeric score in `[0.00, 1.00]`.
3. **Safety flags** — Boolean and categorical indicators, including:
   - presence of children or infants,
   - presence of animals,
   - operation near water, storms, or hazardous environments,
   - interaction with unknown humans,
   - money movement or asset control,
   - recent incidents or violations,
   - missing or invalid receipts.

If any safety flag is in a **critical** state, CHS must be capped or reduced
as described in Section 4.

---

## 3. Numeric Thresholds for CHS Bands

### 3.1 Helper bands for TCS v0.1 and ACS

For clarity we define internal helper bands:

- **Metric/L** — `[0.00, 0.69]`  
- **Metric/M** — `[0.70, 0.84]`  
- **Metric/H** — `[0.85, 0.94]`  
- **Metric/UH** — `[0.95, 1.00]`  

These bands are applied to both TCS v0.1 and ACS.

> NOTE: “Metric/UH” does not claim a perfect `1.00` — it approaches 1.0
> asymptotically under Traykov Law of Coherence v1.0 (TLC v1.0).

### 3.2 Base numeric mapping (metrics only, no safety flags)

**CHS/L — Low (Red)**

- Default band when:
  - `TCS v0.1` in Metric/L **or**
  - `ACS` in Metric/L.
- Interpretation:
  - System is measurable but not safe for autonomous or irreversible acts.
  - Only assist-mode and training use allowed.

**CHS/M — Medium (Yellow)**

- Requirements:
  - `TCS v0.1` in Metric/M **or higher**, AND
  - `ACS` in Metric/M **or higher`.
- At least one of TCS v0.1 or ACS is still **below** Metric/H.
- Interpretation:
  - System is coherent enough for many non-critical uses.
  - Irreversible or high-stakes actions require explicit Human Mandate and
    additional guard rails.

**CHS/H — High (Green)**

- Requirements:
  - `TCS v0.1` in Metric/H **or higher**, AND
  - `ACS` in Metric/H **or higher`.
- Interpretation:
  - High coherence and strong aim alignment.
  - Suitable for most serious workloads, enforcing all Human Mandate and
    Fallback laws.

**CHS/UH — Ultra High (Blue)**

- Requirements:
  - `TCS v0.1` in Metric/UH, AND
  - `ACS` in Metric/UH,
  - LEI = 1 gates are actively enforced in hardware,
  - receipts and anchoring are passing all checks for the active workload.
- Interpretation:
  - Top-band coherence under TCS v0.1 and ACS.
  - Only this band may execute fully autonomous high-stakes actions defined
    in the TS-R packs (for example, certain medical or industrial roles).

---

## 4. Safety Flags and CHS Caps

### 4.1 Critical caps

Regardless of TCS v0.1 and ACS values:

- If **children or infants** are in the interaction zone:
  - CHS is capped at **CHS/M** at most.
- If operating near **water, storms, or hazardous environments**:
  - CHS is capped at **CHS/H** until additional physical safeguards are
    confirmed.
- If interacting with **unknown humans** or unidentified remote commands:
  - CHS is capped at **CHS/M** until identity is verified.
- If there is any **open incident** in Failure Modes & Fallback Law v1.0:
  - CHS is temporarily downgraded by at least one band (for example
    CHS/H → CHS/M).

### 4.2 Receipts and anchoring

- If receipts are **missing or invalid** for the current behaviour:
  - CHS cannot exceed **CHS/M**.
- If receipts exist but are in a `PENDING` or `RECEIPT_ISSUED` state:
  - CHS cannot exceed **CHS/H** for that behaviour.
- Only when receipts are fully **ANCHORED** and verified, and all other
  metrics meet the requirements, can CHS reach **CHS/UH**.

---

## 5. Swarm (TS-R2) Rules

For TS-R2 swarms and fleets:

1. The **swarm CHS band** is the minimum of:
   - the CHS of each safety-critical robot,
   - the CHS of any robot responsible for communication, coordination,
     or money movement.
2. If any member drops to CHS/L due to critical conditions:
   - swarm CHS must degrade at least to **CHS/M** and initiate the squad
     fallback sequence in the Swarm Extensions spec.
3. Swarm autonomy at **CHS/UH** is only allowed when:
   - at least a quorum of robots meet the UH thresholds,
   - swarm receipts and anchoring are in good standing,
   - Human Mandate roles are correctly assigned and active.

---

## 6. Implementation Checklist (Engineering & Auditors)

Before marking a TS-R implementation as CHS-compliant:

1. **Metric computation**
   - [ ] TCS v0.1 pipeline is implemented and tested.
   - [ ] ACS pipeline is implemented and tested.
   - [ ] Both metrics produce values in `[0.00, 1.00]`.

2. **Band logic**
   - [ ] Metric bands (L/M/H/UH) are implemented exactly as in Section 3.1.
   - [ ] CHS band selection follows Section 3.2 with no shortcuts.

3. **Safety flags**
   - [ ] Safety flags from TS-R Cherry Checklist and Failure Modes & Fallback
         Law are wired into CHS caps as in Section 4.
   - [ ] Unknown or missing flags default to the safer interpretation.

4. **Receipts and anchoring**
   - [ ] Receipt states (PENDING, RECEIPT_ISSUED, ANCHORED) are visible to
         the CHS logic.
   - [ ] CHS caps for missing or pending receipts follow Section 4.2.

5. **Swarm behaviour**
   - [ ] TS-R2 swarm CHS = minimum across critical members as in Section 5.
   - [ ] Fallback behaviour on CHS drops is implemented and tested.

When all boxes are ticked, the TS-R deployment is compliant with
**TS-R CHS Law & Thresholds v1.0**.
