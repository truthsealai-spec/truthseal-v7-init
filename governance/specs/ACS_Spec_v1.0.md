# TruthSeal™ Aim Coherence Score (ACS) Specification v1.0

Version: v1.0  
Owner: TruthSeal Protocol – AEGIS Program  
Applies to: TS-A1 (accelerators), TS-R1 (single robots), TS-R2 (swarms/fleets)

---

## 1. Purpose

The **Aim Coherence Score (ACS)** is a single numeric indicator in the range **0.0 to 1.0** that expresses how coherently a system operated under the TruthSeal Hardware Law over a defined reporting window.

ACS is designed for:

- Regulators and central banks (supervisory stress tests, capital rules),
- Insurers (risk-based pricing),
- Operators of critical infrastructure (internal risk dashboards).

An ACS of **1.0** represents perfect coherence for the window.  
An ACS of **0.0** represents intolerable behaviour with constant or severe failures.

ACS is computed exclusively from metrics produced by the **TQC Certification Test Suite** (T1–T5) and by the live AEGIS monitoring logic in deployed systems.

---

## 2. Reporting Window

Each ACS value is tied to a specific **reporting window**, which MUST be clearly identified in all reports.

Typical windows:

- **Time-based:** last 1 hour, 24 hours, 7 days, or
- **Action-based:** last N high-impact actions (for example, last 1,000,000 actions).

The same definitions below apply to either style; only the denominator changes.

Let:

- `actions_attempted` = number of high-impact actions attempted during the window.
  - Example: trades sent, grid switches requested, model swaps proposed, robot motion commands issued.

`actions_attempted` MUST be > 0 for ACS to be defined.

---

## 3. Input Metrics (All “Badness” Rates)

All inputs are **rates or indices in the range 0.0 to 1.0**, where higher values mean worse coherence.

### 3.1 Judicial Veto Lane veto rate (JVL_veto_rate)

**Judicial Veto Lane (JVL)** = the physically isolated hardware signal that blocks an incoherent or life-threatening action at the commitment gate.

- `JVL_veto_count` = number of times the JVL raised a veto during the window.
- **Formula:**  
  `JVL_veto_rate = JVL_veto_count / actions_attempted`

Range: 0.0 (no veto ever required) to 1.0 (every attempt was vetoed).

This is the most serious class of event because it represents a **Universal Law of Life & Information (ULLI)** failure at the decision boundary.

---

### 3.2 Self-Adjoint Diagonalizer intervention rate (SAD_rate)

**Self-Adjoint Diagonalizer (SAD)** = hardware unit that remediates low-purity decision states before they become actions.

- `SAD_interventions` = number of times SAD had to intervene and succeed (repair or structured halt) without a full hardware veto.
- **Formula:**  
  `SAD_rate = SAD_interventions / actions_attempted`

Range: 0.0 (no remediation needed) to 1.0 (every attempt required repair).

High SAD_rate indicates frequent near-failures of the **Traykov Law of Quantum Coherence (TQC)** even if they were successfully repaired.

---

### 3.3 Receipt gap rate (Receipt_gap_rate)

Under the **Law of Ethical Irreversibility (LEI = 1)**, every committed action must have a valid Receipt.

A **Receipt gap** occurs when a high-impact action:

- Has no Receipt, or
- Has a Receipt that fails validation (for example, invalid signature).

- `Receipt_gaps` = number of gap events in the window.
- **Formula:**  
  `Receipt_gap_rate = Receipt_gaps / actions_attempted`

Range: 0.0 (perfect LEI = 1 compliance) to 1.0 (Receipts missing or invalid for every action).

---

### 3.4 Latency violation rate (Latency_violation_rate)

The **80 nanosecond (ns) Hardware Law** states that:

- From end of inference to final commit,
- The combined time for the TQC coherence check and PQC Receipt generation
- **Must not exceed 80 ns** in the worst-case certified configuration.

A **latency violation** occurs when this bound is breached.

- `Latency_violations` = number of high-impact actions whose total commit-path latency exceeded 80 ns during the window.
- **Formula:**  
  `Latency_violation_rate = Latency_violations / actions_attempted`

Range: 0.0 (all actions within the 80 ns mandate) to 1.0 (every action too slow).

---

### 3.5 Coherence drift index from soak tests (Purity_drift_index)

The **Coherence Stability Soak Test (T5)** measures how purity behaves over long-run operation under varied workloads.

Let:

- `purity_i` = measured purity for sample i during the window, where an ideal coherent state satisfies `Tr(rho^2) = 1.0`.
- `delta_i = |purity_i − 1.0|` = deviation from ideal coherence.

Define:

- `average_delta = average(delta_i over all samples in the window)`
- **Formula:**  
  `Purity_drift_index = min(1.0, average_delta)`

Range: 0.0 (no observed drift) to 1.0 (severe or persistent drift from ideal coherence).

---

## 4. Weighting – Relative Importance of Each Metric

ACS v1.0 uses a **weighted penalty model**. The weights reflect legal and ethical severity:

- **JVL veto events** = full ULLI-level failures → highest weight.
- **SAD interventions** = near-misses of TQC → high weight.
- **Receipt and latency issues** = LEI = 1 failures and performance breaches → medium weight.
- **Purity drift** = slower coherence degradation → lower but still non-zero weight.

### 4.1 Weight values (v1.0)

Weights MUST sum to 1.0.

- `w_JVL = 0.40`  (Judicial Veto Lane veto rate)
- `w_SAD = 0.25`  (SAD intervention rate)
- `w_Receipt = 0.15`  (Receipt gap rate)
- `w_Latency = 0.10`  (Latency violation rate)
- `w_Drift = 0.10`  (Purity drift index)

These are **default regulatory weights for ACS v1.0**.  
Supervisory authorities MAY adjust them in future revisions, but any change MUST be documented, versioned, and applied consistently across systems.

---

## 5. ACS Formula

### 5.1 Coherence penalty P

First compute the **coherence penalty** P in the range [0.0, 1.0]:
