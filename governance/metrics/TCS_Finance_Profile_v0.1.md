# TruthSeal™ — TCS Finance Profile v0.1

version: 1.0  
date_utc: 2025-12-02  
owner: TruthSeal™ — Dr. Nickolay Traykov (Prof. h.c.)  

scope: |
  Internal metrics specification for the Traykov Coherence Score – Finance Profile (TCS-Finance v0.1).
  This profile implements the “Anti-Bubble / Finance Profile” idea: separate financial narratives that are
  numerate, sober, and risk-aware (Signal) from those that mainly add hype, fear, or manipulation (Noise).
  v0.1 is an overlay on top of Traykov Coherence Score v0.1 (TCS v0.1) and TCS Noise Distiller Profile v0.2
  (TCS-ND v0.2). It does NOT change the core TCS v0.1 formula; it adds a finance-specific profile layer
  for tagged financial content (markets, assets, portfolios, macro commentary).

  This document is for TruthSeal engineers, auditors, Devora UX, and product teams. It must stay aligned
  with:
    - TCS / ACS / CHS Baseline v1.0,
    - TCS Philosophical Profiles v0.1,
    - TCS Noise Distiller Profile v0.2,
    - Plans and Tiers v1.0,
    - Devora & Report UX Baseline v1.0.

---

## 0. Glossary — Laws, Metrics, Profiles (expanded once)

- **Aim Coherence Score (ACS)** — 0–1 metric for how well actions follow a declared aim and safety constraints over time.
- **Traykov Coherence Score v0.1 (TCS v0.1)** — 0–1 metric for overall intelligence coherence (truthfulness, post-quantum security strength, long-horizon self-consistency) with canonical formula in the TCS v0.1 spec.
- **Coherence Health Score (CHS)** — four-band status indicator derived from ACS, TCS v0.1 and safety signals:
  - CHS/L — Low (Red)
  - CHS/M — Medium (Yellow)
  - CHS/H — High (Green)
  - CHS/UH — Ultra High (Blue)
- **Traykov Law of Quantum Coherence (TQC)** — hardware-anchored law demanding non-degrading coherence behaviour over time.
- **Law of Ethical Irreversibility (LEI = 1)** — once a safer, more coherent, ethically superior state is reached, the system is not allowed to downgrade back to a worse one.
- **ULLI** — TruthSeal governing proof mandate with:
  - Academic Authority Proof,
  - Technical Immutability Proof,
  - Live Measurability Proof.
- **TCS Noise Distiller Profile v0.2 (TCS-ND v0.2)** — profile that separates variables that genuinely contribute to a verified outcome (Truth) from those that mainly add distortion, hype, or manipulation (Noise). Includes ND01–ND05 sub-scores and ND_Cleanliness.
- **ND_Cleanliness** — 0–1 aggregate index from TCS-ND v0.2; higher means “cleaner, less noisy” content.
- **TCS-Finance v0.1 (Finance Profile)** — this profile; a 0–1 overlay for financial content that inspects fundamentals, risk disclosure, macro grounding, bubble pressure discipline, and time-horizon consistency.

---

## 1. Purpose and Relationship to TCS v0.1

The **Traykov Coherence Score – Finance Profile (TCS-Finance v0.1)** is a **modular profile layer** for
financial content only:

- asset and portfolio analysis,
- macroeconomic commentary,
- investment newsletters,
- research notes, risk memos, market videos, etc.

It answers:

> “Is this financial narrative numerate, risk-aware, and honest about uncertainty,  
>  or is it bubble-fuel / fear-porn dressed up as analysis?”

Key points:

- TCS-Finance v0.1:
  - **does NOT modify** the canonical TCS v0.1 formula,
  - is computed **only** when content is tagged or detected as financial,
  - is interpreted **together** with TCS v0.1, ND_Cleanliness, and (optionally) CHS in downstream systems.
- Philosophical profiles (Archimedes / Aristotle / Hippocrates) can read TCS-Finance sub-scores as additional evidence about quantitative, logical, and harm-related integrity.

---

## 2. Finance Profile Sub-Scores (F01–F05)

All Finance Profile sub-scores are 0–1 and follow the same rule:

> 0.0 = extremely poor / incoherent  
>  1.0 = exemplary / highly coherent  
>  **Higher is always better.**

### 2.1 F01 — Fundamentals Coherence

**F01 — Fundamentals Coherence** measures how well the narrative matches basic financial reality.

Signals for higher F01:

- Clearly links claims to fundamentals (revenue, earnings, cash flow, balance sheet strength, leverage).
- Uses concrete numbers or ranges, not just adjectives (“strong”, “huge”, “unprecedented”).
- Distinguishes cyclic vs structural effects.

Signals for lower F01:

- Heavy reliance on price action only (“it went up so it will keep going up”).
- No reference to fundamentals, or cherry-picked numbers without context.
- Contradictions between claims and widely accepted fundamentals.

### 2.2 F02 — Risk Disclosure Coherence

**F02 — Risk Disclosure Coherence** measures whether the piece honestly accounts for downside and uncertainty.

High F02:

- Lists key risks (credit, liquidity, counterparty, regulatory, model risk) in plain language.
- Distinguishes between “base case”, “bull case”, and “bear case”.
- Acknowledges uncertainty and data limitations.

Low F02:

- One-sided “up-only” or “doom-only” narrative.
- Risks mentioned only in boilerplate or tiny print.
- No discussion of tail risks, leverage, or correlated exposures.

### 2.3 F03 — Macro & Policy Grounding

**F03 — Macro & Policy Grounding** measures how well macroeconomic context and policy are integrated.

High F03:

- Connects the argument to macro variables (inflation, rates, growth, unemployment, trade).
- Links claims to policy regimes (central banks, fiscal policy, regulation) with references.
- Avoids cherry-picking single data points to fit a story.

Low F03:

- Vague references to “the Fed”, “China”, or “the economy” with no specifics.
- Ignores obvious macro constraints (e.g. debt levels, currency regime).
- Uses macro buzzwords as decoration rather than evidence.

### 2.4 F04 — Bubble Pressure Discipline

**F04 — Bubble Pressure Discipline** measures how much the piece resists or amplifies classic bubble dynamics.

High F04:

- Explicitly warns against herd behaviour and reflexive feedback loops.
- Shows how valuations compare to historical baselines or peers.
- Calls out unrealistic growth, margin, or adoption assumptions.

Low F04:

- Heavy emphasis on momentum, FOMO (fear of missing out), or “everyone is buying”.
- Superlative-heavy language (“once-in-a-lifetime”, “guaranteed”, “no-brainer”).
- Implicit pressure to act quickly without analysis.

This sub-score pairs naturally with ND sub-scores (especially emotional amplification and herd reinforcement).

### 2.5 F05 — Time-Horizon & Scenario Coherence

**F05 — Time-Horizon & Scenario Coherence** measures whether the time horizon and scenarios are internally consistent.

High F05:

- States explicit time horizons (days, months, years) and aligns claims with those horizons.
- Avoids mixing short-term trading ideas with long-term structural claims without separating them.
- Clearly distinguishes between base case, stress case, and extreme tail case.

Low F05:

- Switches time horizons mid-argument to make results look better.
- Implies long-term certainty from very short-term moves.
- Confuses scenario probabilities (“almost certain” vs “tail risk”) without evidence.

---

## 3. Finance Coherence Score (TCS-Finance v0.1 Aggregate)

To summarise the Finance Profile, we define a **Finance Coherence Score**:

> **Finance_Coherence = 0.30·F01 + 0.25·F02 + 0.20·F03 + 0.15·F04 + 0.10·F05**

- Range: `0.00 – 1.00` (higher is better).
- Interpretation (internal guide; no new band names):

  - `< 0.40` → **Bubble-prone / fear-porn**: narrative is not suitable as a primary input for serious decisions.
  - `0.40 – 0.69` → **Mixed**: some disciplined elements, but significant weaknesses; use only with caution.
  - `0.70 – 0.84` → **Sober**: generally coherent, risk-aware, and numerate.
  - `≥ 0.85` → **Exemplary**: high-integrity finance narrative aligned with TCS v0.1 and ND_Cleanliness.

Important:

- These ranges are for **internal audit and product logic** only.
- Public user-facing bands remain the TCS v0.1 bands (Baseline / Silver / Gold / Diamond).

---

## 4. Integration with TCS v0.1, TCS-ND v0.2, and Anti-Bubble Use Cases

When content is tagged as financial:

1. Compute **TCS v0.1** (core coherence).
2. Compute **TCS-ND v0.2 sub-scores + ND_Cleanliness** (noise vs signal).
3. Compute **F01–F05 and Finance_Coherence** (finance-specific structure).
4. Produce an **Anti-Bubble verdict** that combines them, for example:

   - If `Finance_Coherence < 0.40` OR `ND_Cleanliness < 0.50` → flag as **“high noise / bubble-prone”**.
   - If `Finance_Coherence ≥ 0.70` AND `ND_Cleanliness ≥ 0.75` → flag as **“sober, data-grounded analysis”**.
   - Otherwise → **“mixed signal; use with caution”**.

Exact thresholds and business rules live in implementation code and product configs.  
This document only defines what **must not change** without a version bump:

- names and meaning of F01–F05,
- Finance_Coherence formula,
- the principle that high scores = more disciplined, less bubble-prone finance narratives.

---

## 5. Plans & Devora UX Behaviour

This section aligns TCS-Finance v0.1 with the Plans and Tiers spec and Devora UX baseline.

### 5.1 Free (Discovery)

- Only a **short paragraph** in the report, using plain language (e.g. “sober”, “mixed”, “bubble-prone”).
- No numeric Finance_Coherence score or F01–F05 table.
- Devora may show one or two hints (e.g. “missing clear risk discussion”) but **no receipt fields**.

### 5.2 Pro (Professional)

- Shows **Finance_Coherence** as a 0–1 number and as a percentage (e.g. 0.78 → 78 %).
- Shows a **compact F01–F05 table** (name + value + one-line explanation).
- Includes **2–3 improvement suggestions** (“add explicit risk section”, “separate trading vs investment horizon”).
- Finance fields are included in JSON receipts for Pro where finance profile is enabled.

### 5.3 Enterprise

- Full F01–F05 table with more detailed descriptions.
- Finance_Coherence logged to internal systems and can be exported to GRC (governance, risk, compliance) tools.
- Anti-Bubble / overstatement logic can be wired into internal policies (e.g. “no distribution of research with Finance_Coherence < X without human sign-off”).

### 5.4 Network / Platform

- Same as Enterprise, plus:
  - Per-tenant configuration of thresholds (within limits set by TruthSeal governance).
  - Option to expose or hide detailed F01–F05 from end-users, while still enforcing platform-level policies.

Plans & Tiers v1.0 remains the canonical list of which plan exposes which profile; this section only clarifies expected behaviour.

---

## 6. Audit Checklist (TCS-Finance v0.1 Compliance)

For each deployment that claims to implement **TCS-Finance v0.1**, auditors should verify:

1. **Names and meanings**
   - F01–F05 names and descriptions match this document.
   - Higher values always mean more disciplined, less bubble-prone narratives.

2. **Formula**
   - Finance_Coherence is computed exactly as:
     - `0.30·F01 + 0.25·F02 + 0.20·F03 + 0.15·F04 + 0.10·F05`.
   - Any change to weights or sub-scores requires a new version (e.g. v0.2).

3. **Separation from TCS v0.1**
   - TCS v0.1 core formula is unchanged.
   - Finance_Coherence is treated as a **profile overlay**, not a replacement metric.

4. **Integration with TCS-ND v0.2**
   - Anti-Bubble decisions for financial content use **both** ND_Cleanliness and Finance_Coherence.
   - ND sub-scores are not redefined or re-weighted inside the Finance Profile.

5. **Plans & Devora behaviour**
   - Free: no numeric Finance_Coherence, no F01–F05 table.
   - Pro: numeric Finance_Coherence + compact F01–F05 table + suggestions.
   - Enterprise/Network: full Finance Profile data available for receipts and exports.

6. **Logging and traceability**
   - Finance_Coherence and F01–F05 values are loggable per request.
   - When anchored, receipts clearly mark TCS-Finance v0.1 as the profile version used.

If any of these checks fail, the system must NOT claim TCS-Finance v0.1 compliance without an explicit waiver in the Integrity Manifest.

---
