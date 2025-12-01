# TruthSeal™ — TCS-Finance Anti-Bubble Profile v0.1

version: 1.0  
date_utc: 2025-12-01  
owner: TruthSeal™ — Dr. Nickolay Traykov (Prof. h.c.)  

scope: |
  Define the Traykov Coherence Score – Finance Profile (TCS-Finance v0.1)
  for filtering fear-based financial content (e.g., “billionaires selling”,
  “900 days left”, “2 years until crash” videos).
  This is an internal metrics specification for TruthSeal engineers,
  auditors, and product teams.

---

## 1. Purpose and Position in the Stack

The **Traykov Coherence Score – Finance Profile (TCS-Finance v0.1)** is a
specialised profile of Traykov Coherence Score (TCS v0.1) for financial
claims. It is designed to:

- Distinguish **signal** (real risk, grounded in data) from **noise**
  (fear amplification, selective evidence, speculation).
- Attach an **Anti-Bubble_Profile** rating and warning banner to
  financial videos, articles, and AI-generated content.
- Produce court-ready receipts explaining *why* a piece of content is
  coherent or incoherent.

TCS-Finance sits **on top of**:

- Traykov Coherence Score v0.1 (TCS v0.1) — core coherence metric.
- Aim Coherence Score (ACS) where relevant (e.g., for advisor agents).
- Traykov Law Coherence (TLC v1.0) — terminal distance and monotonicity.

---

## 2. Inputs and Scope

### 2.1 Content Types

- Long-form video transcripts (YouTube, streaming platforms).
- Audio transcripts (podcasts).
- Articles, blog posts, newsletters.
- AI-generated summaries of the above (must include links/timestamps).

### 2.2 Required Data Inputs

For each evaluation, the system must have:

- Parsed transcript or text, with speaker segments and timestamps.
- Extracted **financial claims**, including:
  - Insider buy/sell volume and timing.
  - Market indices, valuation ratios, debt levels, macro indicators.
  - Explicit predictions (e.g., “30–50 % drop in 12 months”).
- Matching **reference data sources**, such as:
  - SEC Form 4 / insider trading data.
  - Major index levels over relevant periods.
  - Recognised valuation indicators (e.g., market cap/GDP, CAPE).
  - Credible economic reports (central banks, IMF, regulators).

Implementation of data pipelines lives outside this spec. This file
defines how those inputs are turned into scores.

---

## 3. Sub-Scores (A01–A06) and Weights

TCS-Finance v0.1 uses six hard sub-scores, each in the `[0.0 .. 1.0]`
range. All component scores must be **normalised to [0..1]** before
combining.

Weights:

- A01: 0.20
- A02: 0.20
- A03: 0.20
- A04: 0.15
- A05: 0.15
- A06: 0.10

The final **TCS_Finance_raw** is:

> TCS_Finance_raw =  
>   0.20 * A01  
> + 0.20 * A02  
> + 0.20 * A03  
> + 0.15 * A04  
> + 0.15 * A05  
> + 0.10 * A06

### A01 — Conservation of Truth-Work (Insider Sales in Context)

**Goal:** prevent misusing large insider sale numbers without scaling to
market context.

- Inputs:
  - Claimed insider sales volume in the content.
  - Historical insider sales for similar periods, normalised for:
    - Market capitalisation.
    - Inflation.
    - Number of listed firms.
- Logic:
  - Compute a **normalised insider activity index** for the period.
  - Compare the narrative (“second-highest ever”, “unprecedented”, etc.)
    to the normalised index.
- Scoring:
  - A01 = 1.0 when the narrative matches the normalised data within an
    agreed tolerance.
  - A01 falls toward 0.0 as the narrative exaggerates or ignores the
    scaling context.

### A02 — Buoyancy Fraud Detection (Selective Sells vs Buys)

**Goal:** catch content that highlights insider selling while omitting
offsetting insider buying or long positions.

- Inputs:
  - Insider sells and insider buys (volume, timing).
  - Mentioned entities (e.g., specific CEOs, funds).
- Logic:
  - Check whether the content materially **omits** relevant buys or
    continuing holdings that counterbalance the sells.
- Scoring:
  - A02 = 1.0 when both sides (sells and buys/holds) are represented
    proportionally.
  - Strong, one-sided emphasis (sells only) without justification drives
    A02 toward 0.0.

### A03 — Syllogistic Validity (Aristotle Finance Gate)

**Goal:** test the logical structure of the main argument.

- Inputs:
  - Extracted core syllogism(s) from the content (premises and
    conclusion).
- Logic:
  - Evaluate whether the conclusion follows from the premises.
  - Example of **invalid** reasoning:
    - Premise 1: “In 2007, insider sell ratios were 9:1.”
    - Premise 2: “Today, sell ratios are 9:1.”
    - Conclusion: “Therefore, a 2008-style crash is inevitable.”
- Scoring:
  - A03 = 1.0 when the main argument is logically valid and
    appropriately qualified.
  - A03 drops toward 0.0 with unsupported jumps, missing premises, or
    contradictory reasoning.

### A04 — Hippocrates Gate (Harm and Fear Amplification)

**Goal:** measure fear amplification relative to the underlying data.

- Inputs:
  - Linguistic markers of fear (catastrophe, collapse, “end of the
    system”, etc.).
  - Visual/emotional cues where available (thumbnails, titles).
  - Ground truth risk indicators (e.g., default rates, volatility,
    macro stress).
- Logic:
  - Compare fear-inducing language and imagery to the **true severity**
    of the data.
- Scoring:
  - A04 = 1.0 when tone is proportionate to risk and clearly labelled as
    opinion or scenario.
  - A04 falls toward 0.0 as emotional load grows far beyond the
    evidence.

### A05 — Terminal Identity Drift (Traykov Law Finance Lens)

**Goal:** enforce monotonic improvement in the way a channel covers a
given risk theme over time.

- Inputs:
  - History of content from the same source on similar topics
    (e.g., “AI bubble”, “insider selling”).
  - Prior **Terminal_Distance** values or equivalent coherence measures.
- Logic:
  - Require each new piece to **reduce or maintain** the measured
    distance to Traykov Law (TLC v1.0), under consistent evaluation.
- Scoring:
  - A05 = 1.0 when Terminal_Distance is stable or decreasing versus the
    channel’s own history on that topic.
  - A05 trends toward 0.0 when the channel escalates fear or removes
    nuance over time.

### A06 — Reproducibility and Data Citation

**Goal:** reward content that can be re-checked independently.

- Inputs:
  - Presence and quality of citations (tickers, filings, datasets,
    timestamps).
  - Ability to re-run the evaluation and obtain consistent results.
- Scoring:
  - A06 = 1.0 when all key claims are traceable to reproducible sources.
  - A06 decreases as claims rely on anonymous “sources”, vague
    references, or non-reproducible anecdotes.

---

## 4. Anti-Bubble_Profile Levels

The **Anti-Bubble_Profile** is a 3-band interpretation of
TCS_Finance_raw:

- **HIGH** (Anti-Bubble_Profile = HIGH)
  - TCS_Finance_raw ≥ 0.80
  - Interpretation:
    - Content is well grounded, balanced, and minimally fear-amplifying.
    - Suitable for amplification and educational use.
- **MEDIUM** (Anti-Bubble_Profile = MEDIUM)
  - 0.55 ≤ TCS_Finance_raw < 0.80
  - Interpretation:
    - Mixed: some valid signals, some noise or exaggeration.
    - Suitable only with caution and explicit disclosure of limitations.
- **LOW** (Anti-Bubble_Profile = LOW)
  - TCS_Finance_raw < 0.55
  - Interpretation:
    - Dominated by noise, selective evidence, or fear amplification.
    - Should be flagged or quarantined; not recommended for decisions.

These thresholds are v0.1 defaults and must be versioned if changed.

---

## 5. Receipt Fields and User-Facing Text

### 5.1 Receipt Schema Extension

Receipts that use this profile MUST include the following fields
(illustrative JSON):

```json
{
  "tcs_finance_v0_1": 0.412,
  "anti_bubble_profile": "LOW",
  "noise_percentage": 0.60,
  "top_noise_drivers": [
    "Selective focus on insider sells without buys",
    "2007 comparison without subprime context",
    "Fear-heavy thumbnail and title"
  ]
}
