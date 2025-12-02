# TruthSeal™ — TCS Philosophical Profiles v0.1

version: 1.0  
date_utc: 2025-12-02  
owner: TruthSeal™ — Dr. Nickolay Traykov (Prof. h.c.)  

scope: |
  Internal baseline for the first generation of TruthSeal Philosophical Profiles
  built on the Traykov Coherence Score v0.1 (TCS v0.1):
  - Archimedes Profile,
  - Aristotle Profile,
  - Hippocrates Profile (high-level context only; legal details live in a separate file).

  This file explains what each profile is for, how it relates to the core metrics
  (TCS v0.1, Aim Coherence Score, Coherence Health Score), and how product,
  Devora UX, and sales should describe them.

  It does NOT define raw formulas; all precise math lives in the metrics layer.

---

## 0. Glossary — Laws, Metrics, Profiles (expanded once)

**Core laws and fields**

- **ULLI** — TruthSeal governing proof mandate with three pillars:
  - Academic Authority Proof,
  - Technical Immutability Proof,
  - Live Measurability Proof.

- **Traykov Law of Quantum Coherence (TQC)** — hardware-anchored law that demands
  non-degrading coherence behaviour over time; no “free lunch” in risk.

- **Law of Ethical Irreversibility (LEI = 1)** — law that forbids reverting from a safer,
  more coherent configuration to a riskier one once the safer option exists.

**Metrics**

- **Traykov Coherence Score v0.1 (TCS v0.1)** — 0–1 metric for overall intelligence
  coherence (truthfulness, post-quantum security strength, long-horizon
  self-consistency).

- **Aim Coherence Score (ACS)** — 0–1 metric that measures how well actions follow
  the declared aim and safety constraints over time.

- **Coherence Health Score (CHS)** — four-band status indicator:
  - CHS/L — Low (Red)  
  - CHS/M — Medium (Yellow)  
  - CHS/H — High (Green)  
  - CHS/UH — Ultra High (Blue)

**Profiles**

- **Philosophical Profiles** — overlays on top of TCS v0.1 that interpret coherence
  through specific philosophical lenses (for example Archimedes, Aristotle,
  Hippocrates). They do NOT change the core TCS v0.1 formula.
- **Hippocrates Profile** — specialised Philosophical Profile used only for
  health-related information quality. Full legal and safety rules live in
  `Hippocrates_Profile_Legal_Safety_v1.0.md`.

---

## 1. Role of Philosophical Profiles

Philosophical Profiles answer one question:

> “Given a base coherence score, what *kind* of coherence is this system showing?”

They are:

- **Overlays, not new metrics.**  
  They annotate TCS v0.1 rather than replace it.

- **Contextual.**  
  Each profile focuses on a different field:
  - Archimedes — numerical, physical, and quantitative reasoning,
  - Aristotle — structure, logic, and argument coherence,
  - Hippocrates — health-related information quality.

- **Constrained by laws.**  
  All profiles must respect ULLI, TQC, and LEI = 1. They are not allowed to
  dilute safety or override legal guardrails.

Philosophical Profiles are primarily surfaced in Devora, PDFs, and dashboards for
Enterprise and Network / Platform customers.

---

## 2. Archimedes Profile — Quantitative Coherence

### 2.1 Purpose

The **Archimedes Profile** measures coherence of quantitative reasoning on top of
TCS v0.1. It answers:

- Does the system handle numbers, units, and physical constraints coherently?
- Are quantitative chains of reasoning stable when phrased in different ways?
- Does it avoid “numerical hallucinations” that contradict basic physics or math?

Typical use:

- risk models,
- engineering notes,
- financial calculations (together with TCS Finance Profile v0.1).

### 2.2 Behaviour and Signals

Archimedes focuses on:

- consistency of numeric answers across re-phrasings,
- respect for bounds, units, and conservation rules,
- stability of explanations that involve formulas or simulations.

It uses TCS v0.1 as a base and adds sub-signals related to:

- numeric self-consistency tests,
- unit-conversion sanity checks,
- cross-question stability (same scenario, varied wording).

Exact sub-scores live in the metrics layer and are not repeated here.

### 2.3 Where It Appears

- Devora reports for:
  - engineering-style prompts,
  - quantitative scenario analysis.
- Enterprise / Network dashboards for:
  - modelling pipelines,
  - high-stakes decision support.

Not available in Free tier; limited exposure in Pro.

---

## 3. Aristotle Profile — Structural and Logical Coherence

### 3.1 Purpose

The **Aristotle Profile** evaluates how well reasoning is structured and whether
arguments hold together logically. It asks:

- Are premises, conclusions, and steps clearly connected?
- Does the system avoid obvious contradictions inside one answer?
- Are chains of reasoning robust to probing questions?

It is especially useful for:

- policy drafts,
- legal-style arguments,
- complex multi-step plans.

### 3.2 Behaviour and Signals

Aristotle looks at:

- internal contradiction checks,
- structure and clarity of argumentation,
- alignment between stated premises and conclusions.

On top of TCS v0.1, it uses signals for:

- contradiction detection across the answer,
- stability of conclusions under mild input changes,
- coherence between “why” explanations and given outputs.

### 3.3 Where It Appears

- Devora long-form analyses,
- Enterprise and Network reports where explanations matter more than numbers,
- internal reviews of policies and governance docs.

Not available in Free tier; may appear in Pro for non-medical, non-political use.

---

## 4. Hippocrates Profile — Health Information Coherence (High-Level)

> **Important:** this section is conceptual only.  
> All binding legal and safety rules live in
> `Hippocrates_Profile_Legal_Safety_v1.0.md`.

### 4.1 Purpose

The **Hippocrates Profile** is a Philosophical Profile specialised for evaluating
the coherence and quality of **health-related information**, such as:

- guidelines,
- educational content,
- risk explanations.

It is **never** allowed to operate as a medical diagnosis engine or treatment
selector for individuals.

### 4.2 Behaviour and Signals

At conceptual level, Hippocrates focuses on:

- coherence and stability of health information,
- alignment with evidence-based sources,
- clear communication of uncertainty and limits.

It overlays TCS v0.1 with signals about:

- consistency across similar questions,
- avoidance of definitive treatment claims,
- presence of safety language and “see a doctor” recommendations.

All legal, wording, and deployment constraints are in the dedicated legal file.

### 4.3 Where It Appears

- Enterprise and Network tiers only,
- Devora health-information views (never diagnosis),
- internal audits of health-related AI systems.

Not available for Free or Pro users.

---

## 5. How Devora and PDFs Use Philosophical Profiles

When a Philosophical Profile is active for a report, Devora and PDFs should:

1. Show the base **TCS v0.1 percentage and band** (Baseline / Silver / Gold / Diamond).
2. Indicate which Philosophical Profile was applied:
   - for example “Archimedes overlay” or “Aristotle overlay”.
3. Provide one short sentence describing what the overlay checks:
   - Archimedes — “numerical and physical coherence,”
   - Aristotle — “logical and structural coherence,”
   - Hippocrates — “health information quality (not diagnosis).”
4. Link to internal or external help pages where allowed.

If multiple profiles apply (for example Finance + Archimedes), Devora should
present them as stacked overlays, not blended into a single opaque score.

---

## 6. PM / Designer Checklist for Philosophical Profiles

Before shipping any change that touches Philosophical Profiles in product, Devora,
or PDFs, the **project manager (PM)** and **lead designer** must be able to tick:

1. **Overlay, not replacement**
   - [ ] TCS v0.1 remains the base coherence metric; profiles only overlay it.
   - [ ] Band names (Baseline / Silver / Gold / Diamond) are unchanged.

2. **Correct placement**
   - [ ] Archimedes is only used for quantitative contexts.
   - [ ] Aristotle is only used where argument structure matters.
   - [ ] Hippocrates is only used under the constraints in
         `Hippocrates_Profile_Legal_Safety_v1.0.md`.

3. **Tier alignment**
   - [ ] No Philosophical Profile appears in a tier that is not allowed
         (for example Hippocrates in Free or Pro).
   - [ ] Exposure matches `Plans_and_Tiers_v1.0.md`.

4. **Language and disclaimers**
   - [ ] Devora and PDF wording clearly state that profiles interpret coherence;
         they do not guarantee outcomes.
   - [ ] Any health-related wording matches the legal baseline file.

5. **No forbidden expansion**
   - [ ] Profiles are not used to rank political candidates or optimise elections.
   - [ ] Profiles are not used to promise medical cures or financial returns.

If any box cannot be ticked, the change is **not compliant** and must not go live.

---

This file is the v1.0 baseline for Philosophical Profiles.
Future expansions (for example additional philosophers) must extend this document
and remain consistent with ULLI, TQC, LEI = 1, and the Pre-Christmas execution plan.
