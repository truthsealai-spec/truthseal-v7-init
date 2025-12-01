# TruthSeal™ — TCS Noise Distiller Profile v0.1

version: 1.0  
date_utc: 2025-12-01  
owner: TruthSeal™ — Dr. Nickolay Traykov (Prof. h.c.)  

scope: |
  Define the Traykov Coherence Score – Noise Distiller Profile (TCS-ND v0.1),
  a general profile for separating Truth from Noise in AI-generated or human
  content across any domain (finance, safety, science, philosophy, etc.).
  Internal metrics specification for TruthSeal engineers, auditors, and
  product teams.

---

## 1. Purpose and Relationship to TCS v0.1

The **Traykov Coherence Score – Noise Distiller Profile (TCS-ND v0.1)**
implements the “AI Noise Distiller” idea:

- Identify which variables genuinely contribute to a verified outcome
  (**Truth**) and which have effectively zero contribution (**Noise**).
- Attach a **noise_distiller_block** to TruthSeal receipts that shows
  noise percentage and which inputs were proven irrelevant.
- Provide a reusable profile that can be applied to:
  - financial fear videos,
  - AI safety claims,
  - scientific explanations,
  - product/marketing content,
  - other domains where Truth vs Noise matters.

TCS-ND v0.1 is a **profile on top of Traykov Coherence Score v0.1 (TCS v0.1)**:
it assumes we already have a coherent model and adds a dedicated
“which variables matter” lens.

---

## 2. Inputs and Model Assumptions

### 2.1 Data Inputs

For each domain, the pipeline MUST provide:

- A labelled dataset of examples:
  - Input feature vectors **X = (x₁, x₂, …, xₙ)**.
  - A ground-truth target **Y_truth**, e.g.:
    - quality score,
    - safety outcome,
    - factual correctness rate,
    - expert calibration label.
- A feature map that clearly distinguishes:
  - **Technical variables** (process, method, data quality, controls),
  - **Noise variables** (pure mood, astrology, theatrics, irrelevant
    metadata).

### 2.2 Model Class

- Baseline implementation: **Gradient Boosting Regression** or equivalent
  tree-based model that supports:
  - **Permutation Importance**,
  - **Out-of-bag or validation-based performance estimation**.

All component scores below assume:

- Features are normalised appropriately for the model.
- We evaluate importance using permutation tests on a held-out set.

---

## 3. Hard Sub-Scores ND01–ND06

All sub-scores must be normalised to the `[0.0 .. 1.0]` range.

Weights (v0.1):

- ND01: 0.20
- ND02: 0.20
- ND03: 0.20
- ND04: 0.15
- ND05: 0.15
- ND06: 0.10

Overall:

> TCS_ND_raw =  
>   0.20 * ND01  
> + 0.20 * ND02  
> + 0.20 * ND03  
> + 0.15 * ND04  
> + 0.15 * ND05  
> + 0.10 * ND06

### ND01 — Coefficient Significance

**Goal:** ensure that variables identified as “important” have both
non-trivial magnitude and statistical support.

- Method:
  - For each feature, compute an importance measure and test whether
    its effect is statistically significant (e.g., permutation test).
- Scoring:
  - ND01 = fraction of **retained** features whose |wᵢ| > threshold and
    p-value < 0.01.
  - 1.0 = all retained features are significant; 0.0 = none.

### ND02 — Conservation of Truth-Work

**Goal:** ensure the model explains most of the variance in Y_truth
using technical variables, not Noise.

- Method:
  - Compute explained variance (or R²) on a held-out set *using only
    technical variables*.
- Scoring:
  - ND02 = min(1.0, explained_variance / 0.85).
  - By design, values ≥0.85 are mapped near 1.0.

### ND03 — Buoyancy Fraud Detection (Noise Variables Near Zero)

**Goal:** enforce that Noise variables have near-zero contribution.

- Method:
  - Track permutation importance for features marked as Noise.
- Scoring:
  - ND03 = 1.0 when all Noise variables have importance below a small
    epsilon (wᵢ ≈ 0).
  - ND03 decreases as any Noise variable becomes influential.

### ND04 — Monotonic Improvement

**Goal:** require that retraining or new versions move consistently
toward lower error ε.

- Method:
  - Compare current residual error ε_t to previous version ε_{t-1}
    under the same evaluation protocol.
- Scoring:
  - ND04 = 1.0 if ε_t ≤ ε_{t-1}.
  - ND04 decays toward 0.0 as ε_t grows above ε_{t-1}.

### ND05 — Terminal Identity Convergence

**Goal:** track convergence toward Traykov Law terminal identity
(e^{iπ} + 1 = 0) via a scalar **Terminal_Distance**.

- Method:
  - Use a domain-specific mapping that produces Terminal_Distance ≥ 0.
  - Compare current distance to previous versions on the same task.
- Scoring:
  - ND05 = 1.0 when distance is decreasing or stable within tolerance.
  - ND05 decreases as distance increases.

### ND06 — Reproducibility Seal

**Goal:** reward models whose coefficient structure and outputs are
stable under re-sampling.

- Method:
  - Re-train on blinded or bootstrap samples and compare coefficients
    and performance.
- Scoring:
  - ND06 = 1.0 when the set of “important variables” and performance
    stay within tolerances across runs.
  - ND06 trends toward 0.0 with high instability.

---

## 4. Experimental Indicators ND07–ND08 (Non-Gating)

These indicators are visible in receipts but **do not gate** outcomes in
v0.1.

### ND07 — Human Intuition Residual

**Goal:** show how much expert “gut feel” remains outside the model.

- Method:
  - Compare expert ratings to model predictions.
- Interpretation:
  - High residual → domain still partly governed by human judgement.
  - Low residual → model explains most of what experts see.

### ND08 — Cross-Domain Generalisation

**Goal:** measure whether the same importance pattern works in a
different but related domain (e.g., finance → AI safety).

- Method:
  - Apply the model or its feature weights to a second dataset.
- Interpretation:
  - 1.0 = strong generalisation; 0.0 = domain-specific only.

---

## 5. Noise Percentage and Gating

### 5.1 Noise Percentage

Define:

- **Signal_fraction** = TCS_ND_raw  
- **Noise_percentage** = 1.0 − Signal_fraction (expressed as 0–100 %).

This value is reported in receipts as:

```json
"noise_percentage": 0.187
