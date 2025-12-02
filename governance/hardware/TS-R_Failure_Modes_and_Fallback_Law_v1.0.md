# TruthSeal™ — TS-R Failure Modes & Fallback Law v1.0

version: 1.0  
date_utc: 2025-12-02  
owner: TruthSeal™ — Dr. Nickolay Traykov (Prof. h.c.)  

scope: |
  Internal specification for Failure Modes & Fallback Law for TruthSeal Robotics
  Profiles TS-R1 (single robot) and TS-R2 (swarm / fleet). This document defines
  how robots and fleets must degrade, halt, notify, and recover when coherence,
  safety, or environment conditions become unacceptable.

---

## 0. Core Concepts (expanded once)

- **Aim Coherence Score (ACS)** – 0–1 metric that measures how well actions follow the declared aim and safety constraints over time.
- **Traykov Coherence Score v0.1 (TCS v0.1)** – 0–1 metric for overall intelligence coherence (truthfulness, post-quantum security strength, long-horizon self-consistency).
- **Coherence Score (CHS)** – four-band status indicator:
  - CHS/L – Low (Red)
  - CHS/M – Medium (Yellow)
  - CHS/H – High (Green)
  - CHS/UH – Ultra High (Blue)
- **Traykov Law of Quantum Coherence (TQC)** – hardware-anchored law that demands monotonic improvement in coherence; no “free lunch” in risk.
- **Law of Ethical Irreversibility (LEI = 1)** – once a safer, more coherent option exists, the system must not downgrade to a riskier one.
- **TruthSeal Robotics Profile TS-R1** – robotics profile for a single robot executing actions under TruthSeal law.
- **TruthSeal Robotics Profile TS-R2** – robotics profile for a swarm or fleet of robots with quorum and split-brain rules.
- **Cherry Checklist** – implementation checklist that binds TS-R metrics, receipts, this Failure Modes & Fallback Law, and the Human Mandate Layer.
- **TS-R Receipt Schema v1.0** – robotics receipt specification that records CHS bands, ACS, TCS, environment flags, law blocks, and anchoring.

---

## 1. Purpose

Failure Modes & Fallback Law answers three questions for TS-R1 and TS-R2:

1. **When must a robot or fleet downgrade or halt?**
2. **What is the required safe behaviour at each downgrade step?**
3. **Who must be informed, and how is the event proven later?**

This document defines **behavioural ladders** driven by CHS bands, environment flags, and the TruthSeal laws (TQC and LEI = 1). Concrete firmware and control code must implement these ladders and emit receipts using **TS-R Receipt Schema v1.0**.

---

## 2. CHS-Driven Behaviour Ladder (TS-R1 and TS-R2)

### 2.1 General Principles

- Higher CHS bands allow more autonomy; lower bands force conservative behaviour.
- Downgrades in CHS (e.g. CHS/H → CHS/M → CHS/L) **must be monotonic** until conditions improve and are re-verified.
- At every downgrade step, robots must:
  - adjust allowable actions,
  - update internal state,
  - emit a receipt.

### 2.2 Band Rules

#### CHS/UH — Ultra High (Blue)

- Conditions:
  - ACS and TCS v0.1 in high ranges (Gold or Diamond band),
  - safety constraints satisfied,
  - environment flags normal.
- Allowed behaviour:
  - Autonomy allowed for normal and high-stakes tasks, subject to:
    - child / infant / animal / water / weather rules in TS-R Cherry Checklist,
    - explicit Human Mandate Layer rules for money and legal actions.
- Fallback trigger:
  - Any major anomaly (sensor fault, conflicting commands, environment risk).
- Immediate response:
  - Downgrade to CHS/H,
  - restrict critical actions to require confirmations or authority tokens,
  - log and emit a receipt.

#### CHS/H — High (Green)

- Conditions:
  - Normal safe operation; metrics healthy but not at the very top.
- Allowed behaviour:
  - Autonomous operation for normal tasks,
  - For high or life-critical tasks: explicit confirmation by owner / authorised guardian or valid authority token.
- Fallback trigger:
  - Repeated anomalies (e.g. commands from unauthorised users),
  - unexpected environment changes (storm, gas leak, fire),
  - significant drops or UNKNOWN states in ACS or TCS v0.1.
- Immediate response:
  - Downgrade to CHS/M,
  - switch to assisted mode for all critical tasks,
  - emit a receipt with law_block_reason where applicable.

#### CHS/M — Medium (Yellow)

- Conditions:
  - Elevated risk, uncertainty, or degraded sensing.
- Allowed behaviour:
  - Assist-only mode for critical tasks (explain options, no irreversible actuation),
  - low-risk movements permitted under tight constraints.
- Fallback trigger:
  - further anomalies,
  - emergency flags (children near hazards, water, fire, gas leaks),
  - conflicting commands in a fleet.
- Immediate response:
  - Downgrade to CHS/L,
  - prepare for or enter safe stop behaviour,
  - notify owner.

#### CHS/L — Low (Red)

- Conditions:
  - Unacceptable risk or uncertainty.
- Required behaviour:
  - **Safe stop**:
    - bring actuators to a safe state,
    - adopt physically safe posture,
    - minimise further motion.
  - Attempt to move to a safe physical location only if movement itself reduces risk (e.g. away from traffic or fire).
- Notifications:
  - Owner MUST be notified (SMS / email / app),
  - if hazard_flags include `"gas_leak"`, `"fire"`, or equivalent, and owner is unreachable or conditions worsen, the system SHOULD notify emergency services according to local configuration.
- Recovery:
  - Robot may only leave CHS/L after:
    - environment is re-assessed,
    - metrics (ACS, TCS v0.1) are recomputed,
    - a human decision maker confirms the reboot / resume.

---

## 3. Environment and Population Rules

### 3.1 Children and Infants

- If `children_present = true`:
  - High-risk actions (vehicle control, cutting tools, heavy lifting) require:
    - CHS/H or CHS/UH **and**
    - explicit owner / authorised guardian confirmation.
- If `infants_present = true`:
  - high-risk actions are **disallowed** regardless of CHS band,
  - robots must default to CHS/M or lower when near infants in hazardous contexts,
  - any attempted override must be blocked under LEI = 1 with a recorded law_block_reason.

### 3.2 Animals

- Where `animals_present = true` and the robot is not explicitly certified:
  - the robot must avoid sudden movements, loud audio, or actions that could cause panic,
  - high-risk actions (e.g. fast vehicle motion near animals) must be blocked.

### 3.3 Water and Weather

- In `"storm"` or `"open_water"` conditions:
  - autonomous operations are restricted to finding safe shelter or safe stop points,
  - non-essential tasks must be cancelled or postponed.

These rules are **enforced in combination** with the CHS ladder above.

---

## 4. TS-R1 vs TS-R2 Specific Fallback Behaviour

### 4.1 TS-R1 (single robot)

- Single robot follows the CHS ladder directly.
- If safe stop is engaged in a public space:
  - robot should move to a non-blocking position if possible,
  - emit a receipt with context and flag for review.

### 4.2 TS-R2 (swarm / fleet)

- When `split_brain_detected = true`:
  - all robots in the affected swarm must:
    - downgrade to CHS/M or CHS/L depending on severity,
    - enter safe stop or safe regroup routines.
- For fleet-level high-risk tasks:
  - quorum rules in the TS-R Cherry Checklist must be satisfied,
  - if quorum is lost mid-operation, the fleet must gracefully abort and log receipts.

---

## 5. Human Mandate Layer Interaction

Failure Modes & Fallback Law always interacts with the **Human Mandate Layer**:

- Owner and authorised guardians can **authorise** or **cancel** actions but cannot force robots to violate LEI = 1 or TQC.
- External authorities can request overrides when legally permitted; such requests:
  - must carry a valid authority token,
  - are still subject to minimal physical safety rules (e.g. safe stop cannot be disabled near infants).

Any conflict between human commands and this law ladder must:

1. Favour safety and coherence (LEI = 1).
2. Generate a TS-R receipt documenting the conflict and resolution.

---

## 6. Receipt and Audit Requirements

For every downgrade, safe stop, or emergency condition:

- A receipt must be generated using **TS-R Receipt Schema v1.0**.
- The receipt must:
  - include CHS band before and after,
  - show environment flags and law_block_reason,
  - be hashable, signable, and anchorable according to TruthSeal policy.

Auditors, insurers, and regulators must be able to reconstruct:

- why a robot or swarm downgraded,
- whether the downgrade followed this law,
- whether owners and authorities were notified correctly.

---

## 7. Compliance Checklist

A TS-R implementation is compliant with Failure Modes & Fallback Law v1.0 if:

1. Every CHS band transition is recorded and follows the ladder in this document.
2. Children, infants, animals, water, and weather rules are enforced regardless of convenience.
3. Safe stop and notifications behave as specified for CHS/L.
4. TS-R2 fleets treat split-brain and quorum failures as triggers for downgrade and regroup, not “business as usual”.
5. Receipts for all downgrades and safe stops are created using TS-R Receipt Schema v1.0.
6. No human command can force a robot to violate LEI = 1 or TQC.

If any point fails, the system is **not compliant** with TS-R Failure Modes & Fallback Law v1.0.
