# TruthSeal™ — TCS Noise Distiller Profile v0.2

version: 1.0  
date_utc: 2025-12-02  
owner: TruthSeal™ — Dr. Nickolay Traykov (Prof. h.c.)  

scope: |
  Internal metrics specification for the Traykov Coherence Score – Noise Distiller
  Profile (TCS-ND v0.2). This profile implements the “AI Noise Distiller” idea:
  separate variables that genuinely contribute to a verified outcome (Truth) from
  variables that mainly add distortion, hype, or manipulation (Noise).
  v0.2 extends v0.1 by:
    - standardising ND sub-score names as ND01, ND02, … (modular profile layer),
    - clarifying how TCS-ND overlays the Traykov Coherence Score v0.1 (TCS v0.1),
    - defining what appears in Devora UX and in each TruthSeal plan tier,
    - adding a simple audit checklist for engineers and reviewers.

  This file is for TruthSeal engineers, auditors, product teams, and partner
  integrators. It does NOT change the core TCS v0.1 formula; it adds an overlay
  that explains where the “noise” is coming from.

---

## 0. Glossary — Core Laws, Metrics, Profiles (expanded once)

This section expands the shorthand used in the spec. Each acronym is written
out once for first-time readers.

- **ULLI** – TruthSeal governing proof mandate with three proofs:
  Academic Authority Proof, Technical Immutability Proof, Live Measurability
  Proof. Full doctrinal detail lives in Doctorantura materials.

- **TQC – Traykov Law of Quantum Coherence**  
  Hardware-anchored law that demands AI and robotics systems show coherent,
  non-degrading behaviour over time; there is no “free lunch” in risk.

- **LEI = 1 – Law of Ethical Irreversibility**  
  Once a safer, more coherent, ethically superior behaviour is established,
  a system is not allowed to downgrade back to a worse, riskier option.

- **ACS – Aim Coherence Score**  
  0–1 metric that measures how well a system’s actions and outputs follow
  its declared aim and safety constraints over time.

- **TCS v0.1 – Traykov Coherence Score v0.1**  
  0–1 metric that measures overall intelligence coherence, combining:
  truthfulness (TruthScore), post-quantum security strength (PQC_Strength),
  and self-consistency on long-horizon prompts (Self_Consistency).

- **CHS – Coherence Health Score**  
  Four-band status indicator used on devices and dashboards:
  - CHS/L – Low (Red)  
  - CHS/M – Medium (Yellow)  
  - CHS/H – High (Green)  
  - CHS/UH – Ultra High (Blue)

- **TCS-Finance – Traykov Coherence Score – Finance Profile v0.1**  
  Specialised profile for financial content (anti-bubble / anti fear-porn).

- **TCS-Philosophical Profiles**  
  Profiles that view coherence through classical lenses:
  Archimedes (mechanical / quantitative integrity),  
  Aristotle (logical / argumentative integrity),  
  Hippocrates (do-no-harm and emotional integrity).

- **TCS-ND – Traykov Coherence Score – Noise Distiller Profile**  
  Governance profile defined in this file. It asks: “what fraction of this
  result is genuine signal, and what fraction is noise?” It never replaces
  TCS v0.1; it annotates it.

- **Devora – TruthSeal front-end assistant / console**  
  Web / app experience that shows coherence reports (TCS, ACS, CHS, profiles,
  receipts, and anchoring) using the UX baseline spec.

---

## 1. Purpose and Relationship to TCS v0.1

The Noise Distiller Profile answers three questions:

1. **Where is the noise coming from?**  
   Which variables or presentation choices inflate fear, hype, or confusion?

2. **How much of the result is signal vs noise?**  
   Is the coherence verdict being driven by solid evidence, or by noise?

3. **What can we change to reduce noise?**  
   Which levers can users or engineers pull to move towards cleaner signal?

Key principles:

- **TCS v0.1 remains the canonical coherence score.**  
  The core formula
  > TCS_v0.1(S) = 0.60 * TruthScore(S)  
  >            + 0.30 * PQC_Strength(S)  
  >            + 0.10 * Self_Consistency(S)  
  is NOT changed by this profile.

- **TCS-ND is an overlay.**  
  It uses the same evidence pipeline (claims, sources, model traces,
  behavioural tests) and decomposes it into **ND0x sub-scores** that show
  where noise is hiding.

- **Domain-agnostic, domain-aware.**  
  TCS-ND works across domains (finance, safety, philosophy, general media),
  but other profiles (TCS-Finance, Philosophical Profiles) may re-use ND0x
  sub-scores or add domain-specific thresholds.

---

## 2. Inputs and Evidence

TCS-ND reads from existing TruthSeal evaluation artefacts:

- Parsed claims (from text, video transcripts, code, or logs).
- Source graph (citations, references, cross-checks).
- Linguistic features (hedging, certainty, emotional tone, clickbait markers).
- Temporal context (does the narrative ignore obvious recent evidence?).
- Structural features (title vs body, thumbnail vs content, hook vs proof).
- TCS v0.1 components (TruthScore, PQC_Strength, Self_Consistency).

No new raw data sources are required; TCS-ND reuses the same inputs that
already feed TCS v0.1 and domain profiles.

---

## 3. ND Sub-Scores (ND01–ND05)

Sub-scores are deliberately named **ND0x** so they are clearly identifiable
as part of the Noise Distiller profile, not the core TCS v0.1 formula.

Each ND sub-score is a 0–1 value (higher is *better*, i.e. less noise).

### ND01 – Frame / Evidence Gap

- **Name:** ND01_FrameEvidenceGap  
- **Question:** How well does the framing (title, thumbnail, headline, hook)
  match the actual evidence presented?  
- **Examples of low ND01 (noisy):**
  - Catastrophic headlines with mild evidence.
  - Thumbnails or intros that promise one thing but deliver another.
- **Links to TCS components:** Mainly affects TruthScore; big frame/evidence
  gaps reduce trust in the claim set.

### ND02 – Verified Evidence Ratio

- **Name:** ND02_VerifiedEvidenceRatio  
- **Question:** What fraction of key claims are backed by verifiable sources
  (data, references, reproducible experiments) versus unsupported assertions?  
- **Examples of low ND02 (noisy):**
  - Long chains of claims with no links, numbers, or references.
- **Links to TCS components:** Feeds into TruthScore and Self_Consistency.

### ND03 – Emotional Amplification

- **Name:** ND03_EmotionalAmplification  
- **Question:** How much of the narrative is driven by emotional load
  (fear, greed, outrage, sensationalism) rather than grounded reasoning?  
- **Examples of low ND03 (noisy):**
  - Repeated “everything will collapse” language with few specifics.
- **Links to TCS components:** Affects Self_Consistency and indirectly
  TruthScore (claims are often exaggerated or cherry-picked).

### ND04 – Herd / Meme Reinforcement

- **Name:** ND04_HerdReinforcement  
- **Question:** Is the content mostly repeating memes, slogans, and
  trend phrases, or does it add new analysis and evidence?  
- **Examples of low ND04 (noisy):**
  - Copying talking points from viral threads without new checks.
- **Links to TCS components:** Affects Self_Consistency and robustness tests.

### ND05 – Manipulative Structure

- **Name:** ND05_ManipulativeStructure  
- **Question:** Is the structure optimised for understanding or for
  click-through, watch time, and sales only?  
- **Examples of low ND05 (noisy):**
  - Endless loops, manufactured suspense, or artificial scarcity tactics.
- **Links to TCS components:** Affects TruthScore (incentives), and ACS when
  the content obviously conflicts with the stated aim of “inform, not mislead”.

Additional ND0x indices can be added in later versions, but ND01–ND05 are
the v0.2 baseline.

---

## 4. Aggregate TCS-ND Index

TCS-ND exposes a single aggregate index **ND_Cleanliness** in the range
`0.00 – 1.00`:

> ND_Cleanliness = weighted_mean(ND01 … ND05)

Suggested default weights (can be tuned per domain, but must be documented):

- ND01 – Frame / Evidence Gap: 0.25  
- ND02 – Verified Evidence Ratio: 0.30  
- ND03 – Emotional Amplification: 0.20  
- ND04 – Herd / Meme Reinforcement: 0.15  
- ND05 – Manipulative Structure: 0.10  

Interpretation (internal defaults):

- `ND_Cleanliness < 0.5` → noise-heavy narrative.  
- `0.5 ≤ ND_Cleanliness < 0.75` → mixed; significant noise present.  
- `0.75 ≤ ND_Cleanliness ≤ 1.0` → predominantly signal; noise well-controlled.

These thresholds are for internal use and Devora explanations. They do NOT
introduce a new public “band” system; public bands remain the TCS v0.1
Baseline / Silver / Gold / Diamond structure.

---

## 5. How TCS-ND Appears in Devora & Reports

Devora and report UX use the following presentation rules:

1. **Free plan (Discovery):**
   - Show a short paragraph summary:
     - “Noise Distiller summary: ND_Cleanliness = {value}. This content is
       [noise-heavy / mixed / mostly signal] based on framing, evidence, and
       emotional load.”
   - No ND0x table, no raw scores, no JSON fields.

2. **Pro plan (Professional):**
   - Show **ND_Cleanliness** plus a compact table of ND01–ND05 with plain
     labels (Frame/Evidence, Evidence Ratio, Emotion, Herd, Structure).
   - Include 2–3 concrete suggestions:
     - e.g. “Tighten headline to match evidence”, “Add links to data”.

3. **Enterprise and Network plans:**
   - Show full ND0x table with weights and per-domain notes.
   - Expose ND0x and ND_Cleanliness in JSON receipts (`ts.receipt.v1`) for
     integration into clients’ dashboards and risk engines.
   - Allow domain profiles (Finance, Philosophical, Robotics) to reference
     ND0x fields in their own logic, without rewriting TCS v0.1.

All wording must align with the Devora & Report UX Baseline v1.0 document.

---

## 6. Interaction with Other Profiles

- **TCS-Finance Profile:**
  - May reuse ND01–ND05 directly, adding finance-specific interpretations
    (e.g. fear-based market narratives, bubble language).
  - Must not override ND0x names or invert the “higher is better” rule.

- **Philosophical Profiles (Archimedes / Aristotle / Hippocrates):**
  - Archimedes: focuses on how ND0x impacts quantitative integrity.
  - Aristotle: focuses on logical structure vs emotional amplification.
  - Hippocrates: focuses on harm from noise (panic, misinformation).

- **Robotics and CHS (TS-R1 / TS-R2):**
  - TCS-ND is normally used on **content**, not robot telemetry.
  - However, Devora explanations used by robots or control rooms may use
    ND0x to decide which information feeds are too noisy to trust.

---

## 7. Implementation Notes (for engineers)

- TCS-ND runs as a separate module after TCS v0.1 has been computed.
- It reads feature vectors from:
  - claim / evidence graphs,
  - linguistic analysis pipeline,
  - existing TCS v0.1 trace logs.
- ND0x values must be deterministic for a given input and model version.
- Any change to:
  - ND0x definition,
  - ND0x weights,
  - ND_Cleanliness thresholds
  must:
  - be versioned (v0.3, v0.4, …),
  - be recorded in EVL (Epoch Verification Ledger),
  - be reflected in Devora UX and Plans & Tiers specs.

---

## 8. Audit Checklist (TCS-ND v0.2)

Before shipping or certifying an integration that claims to use
“TCS Noise Distiller Profile v0.2”, auditors must verify:

1. **Naming and semantics**
   - ND01–ND05 names match this file exactly.
   - Higher ND0x always means “cleaner / less noise”.

2. **Relationship to TCS v0.1**
   - Core TCS v0.1 formula is unchanged.
   - TCS-ND is an overlay; no silent weighting of TCS by ND_Cleanliness.

3. **Devora and reports**
   - Free shows only the summary sentence (no ND0x table).
   - Pro shows ND_Cleanliness + compact ND0x table.
   - Enterprise / Network show full ND0x table + JSON fields.

4. **Receipts and ledgers**
   - Where enabled, receipts include ND0x and ND_Cleanliness fields.
   - Any change in ND0x definitions is versioned and logged in EVL.

5. **Documentation consistency**
   - This file is referenced from:
     - TCS / ACS / CHS Baseline v1.0,
     - Philosophical Profiles v0.1,
     - Plans and Tiers v1.0,
     - Devora & Report UX Baseline v1.0.

When all items above are satisfied, the integration can legitimately claim
“TCS Noise Distiller Profile v0.2 compliant”.
