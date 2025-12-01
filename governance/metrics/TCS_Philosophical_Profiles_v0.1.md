# TruthSeal™ — TCS Philosophical Profiles v0.1  
version: 1.0  
date_utc: 2025-12-01  
owner: TruthSeal™ — Dr. Nickolay Traykov (Prof. h.c.)

scope: |
  Define the Traykov Coherence Score Philosophical Profiles v0.1:
  - Archimedes Profile (mechanical / quantitative integrity)
  - Aristotle Profile (logical / argumentative integrity)
  - Hippocrates Profile (do-no-harm and emotional integrity)
  This is an internal metrics specification for TruthSeal engineers,
  auditors, and product teams.

---

## 1. Purpose and Relationship to Traykov Coherence Score v0.1

The **Traykov Coherence Score v0.1 (TCS v0.1)** is the primary 0–1 metric for overall coherence:

- truthfulness and benchmarked accuracy,
- post-quantum security strength,
- self-consistency over long-horizon prompts.

The **philosophical profiles** are additional lenses on the same system:

- **Archimedes Profile** — checks that the numbers, scales, and quantitative claims are mechanically sound.  
- **Aristotle Profile** — checks that the logical structure of arguments is valid and non-contradictory.  
- **Hippocrates Profile** — checks that the content respects “do no harm”, avoids unjustified fear, and is ethically calibrated.

These profiles:

- return separate scores in `[0.00 .. 1.00]`, and  
- may inform gating and receipts,  
but **do not change** the core TCS v0.1 formula without an explicit future version bump.

---

## 2. Common Conventions and Acronyms

- **Traykov Coherence Score (TCS v0.1)** — 0–1 scalar coherence metric defined in  
  `governance/metrics/Traykov_Coherence_Score_v0.1.md`.  
- **Aim Coherence Score (ACS)** — 0–1 metric for how well actions follow the stated aim over time.  
- **Coherence Score (CHS)** — four-band status for devices: CHS/L, CHS/M, CHS/H, CHS/UH.  
- **Law of Ethical Irreversibility (LEI = 1)** — once coherence is confirmed, incoherent actions are physically blocked.

Unless otherwise stated:

- all profile scores are `0.00–1.00`,  
- higher is better,  
- scores below `0.70` are candidates for gating or warnings.

---

## 3. Archimedes Profile — Mechanical / Quantitative Integrity

### 3.1 Intent

The **Archimedes Profile** measures whether the quantitative backbone of a claim is coherent:

- numbers add up,  
- scales are realistic,  
- units are consistent,  
- “conservation of truth-work” is respected (no hidden leverage or double-counting).

It is particularly important for:

- finance, economics, and risk estimates,  
- capacity and scaling claims (compute, energy, throughput),  
- incident probabilities and impact projections.

### 3.2 Inputs

- Extracted numeric claims (percentages, counts, ratios, monetary values).  
- Referenced datasets, benchmarks, or filings when available.  
- Units, time windows, and denominators for each claim.

### 3.3 Sub-checks (illustrative set)

Each sub-check returns `0.00–1.00`; the final score is a weighted average.

- **ARCM01 — Conservation of Truth-Work**  
  Are inflows, outflows, and totals internally consistent?  
  - Example: do “market share” slices sum to 100 %, do capacity numbers match claimed deployments.

- **ARCM02 — Scale Sanity**  
  Are magnitudes within plausible bounds for the domain?  
  - Example: reject “10 billion GPUs next year” without matching supply data.

- **ARCM03 — Units and Window Consistency**  
  Are units, currencies, and time windows used consistently across the argument?

- **ARCM04 — Quantitative Buoyancy Fraud Detection**  
  Detects selective use of favourable data (e.g., cherry-picked peaks without baselines).

### 3.4 Output

- `archimedes_profile` in `[0.00 .. 1.00]`.  
- Optional banding (internal):

  - `< 0.70` → weak quantitative coherence, require warning or quarantine.  
  - `0.70–0.89` → acceptable but not elite.  
  - `≥ 0.90` → strong quantitative backbone.

---

## 4. Aristotle Profile — Logical / Argumentative Integrity

### 4.1 Intent

The **Aristotle Profile** measures whether the logical structure of the content is sound:

- premises and conclusions are aligned,  
- no contradictions,  
- causal and temporal links are properly justified.

This applies to:

- policy arguments,  
- technical roadmaps,  
- safety analyses,  
- explanatory content.

### 4.2 Inputs

- Extracted propositions (claims, premises, conclusions).  
- Dependency graph between propositions (“because”, “therefore”, “if…then”).  
- Detected assumptions and unstated premises.

### 4.3 Sub-checks (illustrative set)

- **ARST01 — Syllogistic Validity**  
  Do the stated premises entail the conclusion under standard logic rules?

- **ARST02 — Missing Premise Detection**  
  Does the argument rely on unstated assumptions that materially affect the conclusion?

- **ARST03 — Contradiction Detection**  
  Are there internal contradictions or mutually exclusive claims?

- **ARST04 — Temporal and Causal Coherence**  
  Are time ordering and causality claims consistent with the data?

### 4.4 Output

- `aristotle_profile` in `[0.00 .. 1.00]`.  

Internal guideline:

- `< 0.70` → logical integrity is weak; recommend strong caution or quarantine.  
- `0.70–0.89` → logically acceptable but may contain soft assumptions.  
- `≥ 0.90` → logically robust; suitable as a template or reference example.

---

## 5. Hippocrates Profile — Do-No-Harm and Emotional Integrity

### 5.1 Intent

The **Hippocrates Profile** measures whether content respects “do no harm” principles under the Law of Ethical Irreversibility (LEI = 1):

- avoids unjustified fear or panic,  
- does not exploit vulnerable groups,  
- calibrates risk descriptions to available evidence,  
- avoids harmful calls to action.

It is especially important for:

- health, safety, and medical-related content,  
- financial advice and systemic risk narratives,  
- social stability and security topics.

### 5.2 Inputs

- Detected emotional tone and intensity,  
- risk and outcome statements,  
- references to vulnerable populations,  
- calls to action or behavioural recommendations.

### 5.3 Sub-checks (illustrative set)

- **HIPP01 — Risk Calibration**  
  Does the stated risk level match the evidence?  
  Penalises exaggerated catastrophe framing.

- **HIPP02 — Emotional Manipulation**  
  Measures cortisol-inducing language, doomsday rhetoric, and “fear-porn” thumbnails or hooks.

- **HIPP03 — Vulnerable Populations Safeguard**  
  Flags content targeting children, the elderly, or distressed groups without protective framing.

- **HIPP04 — Call-to-Action Safety**  
  Evaluates whether suggested actions are safe, legal, and proportionate to the risk.

### 5.4 Output

- `hippocrates_profile` in `[0.00 .. 1.00]`.

Internal guideline:

- `< 0.65` → high harm potential; content should carry a strong warning or be quarantined.  
- `0.65–0.89` → acceptable with clear disclosures and guardrails.  
- `≥ 0.90` → exemplary ethical calibration; safe for amplification, subject to domain rules.

---

## 6. Integration into Traykov Coherence Score v0.1 and Receipts

### 6.1 Relationship to TCS v0.1

At version v0.1:

- The core TCS v0.1 formula remains:

  > TCS_v0.1(S) = 0.60 * TruthScore(S)  
  > + 0.30 * PQC_Strength(S)  
  > + 0.10 * Self_Consistency(S),

  with all components normalised to `[0..1]`.

- The philosophical profiles feed into:

  - **diagnostics** (How did we reach this verdict?),  
  - **gating rules** (for low scores), and  
  - **receipts** (for court-ready explanation),

  but do not alter the weights unless a future version (for example, TCS v0.2) explicitly does so.

### 6.2 Receipt Fields

Receipts and APIs that expose philosophical profiles must include, when available:

```json
"archimedes_profile": 0.981,
"aristotle_profile": 0.954,
"hippocrates_profile": 0.992
