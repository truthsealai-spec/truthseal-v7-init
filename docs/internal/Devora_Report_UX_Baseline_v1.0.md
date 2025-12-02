# TruthSeal™ — Devora & Report UX Baseline v1.0

version: 1.0  
date_utc: 2025-12-02  
owner: TruthSeal™ — Dr. Nickolay Traykov (Prof. h.c.)  

scope: |  
  Internal user experience baseline for:  
  - Devora (TruthSeal front-end assistant / console),  
  - web coherence reports,  
  - PDF exports.  
  This file defines the standard layout and wording for coherence reports that are built on:  
  - Aim Coherence Score (ACS),  
  - Traykov Coherence Score v0.1 (TCS v0.1),  
  - Coherence Health Score (CHS) bands (CHS/L, CHS/M, CHS/H, CHS/UH),  
  - profiles (Finance, Philosophical, Noise Distiller, future profiles),  
  - receipts and anchoring (ts.receipt.v1, QENC, ledgers).  
  Plans (Free / Pro / Enterprise / Network) may show or hide sections, but the structure and wording in this baseline must remain consistent.

---

## 0. Glossary — Laws, Metrics, Artifacts (expanded once)

This section expands the core shorthand used in the UX specification. If a detail is not yet fully defined in code or doctrine, Devora must treat it as **informational only**, not as a new law.

### 0.1 Core laws and fields

- **ULLI** – TruthSeal governing proof mandate with three proofs:  
  - **Academic Authority Proof**,  
  - **Technical Immutability Proof**,  
  - **Live Measurability Proof**.  
  (Full doctrinal text lives in Doctorantura files.)

- **Traykov Law of Quantum Coherence (TQC)** – hardware-anchored law that demands artificial intelligence systems remain in a non-degrading coherence state over time; no “free lunch” in risk.

- **Law of Ethical Irreversibility (LEI = 1)** – law that states once a safer, more coherent and ethically superior path is reached, the system is not allowed to downgrade back to a worse, riskier one.

- **Law of TruthSeal Cognitive Coherence (LTCC)** – law that defines how cognitive coherence is measured and bounded inside TruthSeal.

- **Traykov Law of Coherence v1.0 (TLC v1.0)** – law that defines how close a system is allowed to get to the ideal coherence limit; exact value 1.00 is not claimed and monotonic improvement is required over time.

- **Quantum-Ethical Field of Infinite Coherence (UQE-FIC)** – field-level construct that ties physical reality, legal structures, and coherence metrics into one governance field.

### 0.2 Metrics

- **Aim Coherence Score (ACS)** – 0–1 metric that measures how well actions follow the declared aim and safety constraints over time.

- **Traykov Coherence Score v0.1 (TCS v0.1)** – 0–1 metric for overall intelligence coherence (truthfulness, post-quantum security strength, long-horizon self-consistency).

- **Coherence Health Score (CHS)** – four-band status indicator shown to humans or devices:  
  - **CHS/L** – Low (Red)  
  - **CHS/M** – Medium (Yellow)  
  - **CHS/H** – High (Green)  
  - **CHS/UH** – Ultra High (Blue)  

- **TCS Noise Distiller Profile v0.2 (TCS-ND v0.2)** – profile that separates variables that genuinely contribute to a verified outcome (Signal) from variables that mainly add hype, fear, or manipulation (Noise). Uses sub-scores **ND01, ND02, …** and a composite **ND_Cleanliness** score.

- **TCS Finance Profile v0.1 (TCS-Finance v0.1)** – Anti-Bubble / Finance profile that evaluates financial narratives against fundamentals, risk disclosure, macro grounding, bubble pressure, and time-horizon discipline (sub-scores F01–F05, plus Finance_Coherence).

### 0.3 Profiles, ledgers, artifacts

- **Philosophical Profiles** – Archimedes, Aristotle, Hippocrates profiles from `TCS_Philosophical_Profiles_v0.1.md`.

- **TruthSeal ledgers** –  
  - **ULIC** – Universal Law of Infinite Coherence registry block,  
  - **EVL** – Epoch Verification Ledger,  
  - **Integrity Manifest**,  
  - **QENC ProofCapsule** – cryptographic capsule used in the Integrity Manifest.

- **TS-R1 / TS-R2** – TruthSeal Robotics profiles for single robots (TS-R1) and swarms/fleets (TS-R2).

- **ts.receipt.v1** – generic TruthSeal receipt schema, extended by the TS-R robotics schema when robots are involved.

- **QENC** – Quantum Ecosystem Closure ProofCapsule; used as part of anchoring and integrity proofs.

Devora must **not invent new meanings** for any of these acronyms. If something is unclear, it should surface an internal “UNKNOWN – requires doctrinal update” flag rather than guess.

---

## 1. Overall Layout — Three Layers

Devora and all TruthSeal coherence reports follow the same three-layer structure:

1. **Layer A — Summary Stripe (above the fold)**  
   - TCS v0.1 percentage and band (Baseline / Silver / Gold / Diamond),  
   - short ACS status,  
   - CHS band (if applicable),  
   - single-sentence recommendation.

2. **Layer B — Detail Panels (scroll area)**  
   - TCS / ACS breakdown,  
   - CHS and robotics panel (when relevant),  
   - profiles: Philosophical, Noise Distiller, Finance, future profiles,  
   - contextual text that explains what the numbers mean.

3. **Layer C — Receipts & Anchors (bottom or side panel)**  
   - receipt summary,  
   - JSON receipt download,  
   - anchoring status (OpenTimestamps or equivalent),  
   - verification instructions.

Plans differ mainly in **which panels are visible**, **how many details are shown**, and whether the user can download receipts or PDFs.

---

## 2. Summary Stripe (Layer A)

### 2.1 Elements

Above the fold, Devora must always show:

- **Title** – human readable, e.g. “Coherence Report — Uploaded article” or “Coherence Report — Finance video transcript”.  
- **TCS v0.1 score and band** – displayed as `87 % — Gold band` using the canonical wording from the TCS / ACS / CHS baseline.  
- **Short ACS status** – e.g. “Aim Coherence Score: high and stable across test prompts.”  
- **CHS indicator (when applicable)** – e.g. “CHS/H — High (Green) — safe for normal operation; high-stakes actions still gated by LEI = 1.”  
- **Single recommendation line** – always includes the locked sentence:  
  > “We highly recommend using these prompts to push toward Diamond and reduce residual risk.”

The summary stripe must **never** imply clinical diagnosis, election outcome predictions, or investment advice.

---

## 3. Detail Panels (Layer B)

Layer B is composed of several panels stacked in a predictable order.

### 3.1 Core Coherence Panel (TCS v0.1 + ACS)

Purpose: Explain the main coherence verdict.

Content:

- TCS v0.1 as a percentage, band, and one-paragraph explanation (using the canonical text from the ACS / TCS / CHS baseline).  
- High-level drivers: TruthScore, post-quantum security strength, and self-consistency over long prompts.  
- ACS as a short paragraph describing whether the system’s actions actually follow its declared aim over time.

Examples (template text):

- *Gold example*:  
  “Your Traykov Coherence Score v0.1 is **0.88 (Gold band)**. This indicates high coherence and strong stability across tests. It is suitable for most serious workloads, subject to normal governance review.”

- *Silver example*:  
  “Your Traykov Coherence Score v0.1 is **0.74 (Silver band)**. This indicates a coherent but not yet elite output. It is suitable for many non-critical uses, with clear awareness of residual risk.”

Devora should fill in the numbers and band automatically but keep the wording fixed.

---

### 3.2 CHS and Robotics Panel (when applicable)

Visible only when the report is attached to a robot, fleet, or CHS-linked system.

Content:

- CHS band, colour name, and one sentence on what it means for physical actions (CHS/L → safe stop, CHS/M → assist-only, CHS/H → normal operation with safeguards, CHS/UH → allowed for approved high-stakes flows).  
- Link to TS-R Cherry Checklist and Failure Modes & Fallback Law for deeper reading.

No Anti-Bubble content lives here.

---

### 3.3 Noise Distiller Panel (TCS-ND v0.2)

Purpose: Show how much of the content is signal versus hype / noise.

Content:

- ND_Cleanliness (0–1 or 0–100 %) with a short scale:  
  - `ND_Cleanliness < 0.4` → noise-heavy,  
  - `0.4–0.7` → mixed,  
  - `> 0.7` → signal-dominant.  
- Short explanation of what kinds of variables counted as Noise (irrelevant buzzwords, unsupported claims, emotional exaggeration) versus Signal (grounded evidence, verifiable numbers, clear causal reasoning).  
- 2–3 bullet hints on how to reduce Noise (e.g. “replace vague phrases with concrete numbers,” “separate opinion from data”).

Devora must **never** show the internal ND0x sub-score names to Free users; those stay Pro and above.

---

### 3.4 Anti-Bubble / Finance Panel (TCS-Finance v0.1)

This is the **tightened finance / Anti-Bubble section**.

#### 3.4.1 When this panel appears

- Only when the content is tagged as **financial**: markets, assets, portfolios, macro commentary, or similar.  
- For non-financial content, Devora hides this panel completely.

#### 3.4.2 What the panel shows

- **Finance_Coherence score** as a percentage (e.g. `Finance Coherence: 81 %`).  
- A simple band label derived from internal ranges (e.g. “sober”, “mixed”, “bubble-prone”) — these labels are *descriptive*, not trading signals.  
- A compact table of the **F01–F05** sub-scores (Pro and above):

  - **F01 — Fundamentals Coherence**  
  - **F02 — Risk Disclosure Coherence**  
  - **F03 — Macro and Policy Grounding**  
  - **F04 — Bubble Pressure Discipline**  
  - **F05 — Time-Horizon and Scenario Coherence**

- **ND_Cleanliness** for the same content (reused from the Noise Distiller panel).

Devora must always include a small disclaimer at the top of this panel:

> “This section evaluates **narrative quality**, not whether an investment will go up or down. It is **not investment advice**.”

#### 3.4.3 Tight Anti-Bubble examples (template text)

Devora uses these as templates; it fills in numbers and bands but keeps the tone.

**Example A — Bubble-prone narrative**

> “The financial narrative shows **low coherence against fundamentals**.  
> Finance_Coherence is **{FC%} — bubble-prone band**.  
> - Fundamentals (F01) and Risk Disclosure (F02) are weak: key numbers are missing or cherry-picked.  
> - Bubble Pressure (F04) is high: language leans heavily on hype, slogans, and fear of missing out.  
> - ND_Cleanliness is low, indicating a large amount of emotional or promotional Noise.  
> We recommend treating this narrative as **high-risk marketing**, not as a reliable decision input.”

**Example B — Fear-driven / panic narrative**

> “The narrative is **dominated by fear-based framing** rather than balanced risk analysis.  
> Finance_Coherence is **{FC%} — fear-biased band**.  
> - Risk Disclosure (F02) emphasises worst-case scenarios without proportional discussion of likelihood.  
> - Macro and Policy Grounding (F03) are thin or distorted.  
> - Bubble Pressure (F04) is high, but in the direction of panic and doom rather than optimism.  
> We recommend re-checking underlying data and consulting calmer, more balanced sources before acting.”

**Example C — Sober, Anti-Bubble narrative**

> “The narrative is **sober and numerate**.  
> Finance_Coherence is **{FC%} — disciplined band**.  
> - Fundamentals (F01) reference concrete numbers and sources.  
> - Risk Disclosure (F02) clearly separates base, bull, and bear scenarios with rough probabilities.  
> - Bubble Pressure (F04) is low: there is no exaggerated fear or hype.  
> ND_Cleanliness is high, meaning the narrative is dominated by verifiable Signal, not Noise.  
> This style of narrative is **well-suited for long-term decision documents and board-level discussion**, subject to normal governance.”

Devora should use the closest template, then add a short paragraph with **actionable prompts** such as:

- “Ask the author to add concrete revenue and cost assumptions.”  
- “Request explicit downside scenarios with numbers.”  
- “Remove emotionally charged phrases and replace them with neutral descriptions.”

Templates must **never** reference specific tickers, funds, or currencies automatically.

#### 3.4.4 Plan-specific visibility

- **Free** – shows a short paragraph only (like Example A/B/C) plus whether the narrative is “bubble-prone”, “fear-biased”, or “disciplined”. No Finance_Coherence percentage, no F01–F05 table, no downloads.  
- **Pro** – shows Finance_Coherence percentage, F01–F05 table, and 2–3 improvement prompts. PDF reports include the Anti-Bubble paragraph and prompts.  
- **Enterprise / Network** – full detail, JSON export, and configuration options for organisation-specific thresholds. Devora can show side-by-side comparisons across documents, but must keep the wording from this baseline.

---

### 3.5 Philosophical Profiles Panel

Purpose: present Archimedes / Aristotle / Hippocrates scores in a way that is readable for humans, not only auditors.

Content:

- Short explanation of what each profile means (mechanical / quantitative integrity for Archimedes, logical / argumentative integrity for Aristotle, do-no-harm and emotional integrity for Hippocrates).  
- A compact table of profile scores and 1–2 sentence hints for improvement.  
- No medical claims; Hippocrates here is about **ethics and emotional integrity**, not healthcare.

---

## 4. Receipts & Anchoring Panel (Layer C)

This panel ties the report back to TruthSeal’s verification layer.

### 4.1 What users see

- Receipt ID and schema version (always `ts.receipt.v1` for general reports).  
- High-level status:  
  - “Receipt issued — anchoring in progress (OpenTimestamps).”  
  - or “Anchored — proof available.”  
- Link or instructions to verify the receipt against the public anchor.

### 4.2 What changes by plan

- **Free** – no downloadable JSON, may see a simple “Receipt available in paid plans” teaser.  
- **Pro** – can download JSON receipt; some reports flagged as “critical” may be anchored depending on configuration.  
- **Enterprise / Network** – full receipts, anchoring policy per contract, export to internal archives and compliance tools.

Devora must emphasise that **anchoring proves what was said and when**, not whether a decision based on the report will succeed.

---

## 5. PDF Export Rules

- PDFs must follow the same order as the Devora web report: summary stripe → TCS / ACS panel → CHS (if present) → Noise Distiller → Anti-Bubble / Finance (when relevant) → Philosophical profiles → receipts.  
- Each PDF carries:  
  - plan type (Free / Pro / Enterprise / Network),  
  - a short disclaimer that the document evaluates content quality and coherence, not clinical outcomes or guaranteed financial returns.  
- PDF exports for Free plan may display a watermark such as “TruthSeal Free – Narrative Quality Only”.

---

## 6. Guardrails for Devora

- No medical diagnosis or treatment advice.  
- No election outcome predictions, party scoring, or campaign optimisation.  
- No direct trading signals or portfolio recommendations.  
- If a user asks for something outside these bounds, Devora responds with a polite refusal plus a suggestion to use the coherence report only as **information quality feedback**.

This UX baseline is **version 1.0**. Any change to structure, wording, or Anti-Bubble behaviour must be versioned here and mirrored in the relevant metrics and plans specifications.

---

## 7. PM & Designer Checklist (Devora / Reports)

This section keeps Devora, reports, and PDFs aligned with TruthSeal doctrine.

### 7.1 Product manager checklist

Before shipping a new Devora flow or report template, the PM confirms:

- The page is using **this Devora UX baseline v1.0** and the **TCS / ACS / CHS Baseline v1.0**; no ad-hoc wording for bands or scores.  
- Plan-specific visibility is correct:  
  - Free: no PDFs, no JSON receipts, Anti-Bubble panel in paragraph-only mode.  
  - Pro: PDFs and JSON receipts enabled, Finance and Noise panels visible where content is tagged.  
  - Enterprise / Network: full panels, exports, and anchoring options.  
- Anti-Bubble / Finance panel is shown **only** for content explicitly tagged as financial.  
- Every Anti-Bubble panel instance includes the **“not investment advice”** sentence.  
- Receipts panel always references schema `ts.receipt.v1` and surfaces anchoring status (Pending / Anchored) correctly.  
- Guardrails are enforced: Devora cannot be used for medical diagnosis, election outcome prediction, or direct trading calls.

### 7.2 Designer checklist

Before sign-off, the designer confirms:

- The **summary stripe** (TCS % + band + ACS + CHS + recommendation line) is fully visible **above the fold on mobile**.  
- CHS colours exactly match the canonical mapping:  
  - CHS/L → red, CHS/M → yellow, CHS/H → green, CHS/UH → blue,  
  and these colours are not reused for unrelated UI states.  
- Band labels (Baseline / Silver / Gold / Diamond) and their paragraphs use the canonical text; no rephrasing in UI copy.  
- Anti-Bubble / Finance panel uses clear, calm typographic hierarchy; Bubble-prone / Fear-biased / Disciplined labels are easy to scan but not sensational.  
- PDFs visually mirror the web report structure (order of sections, headings, disclaimers) and remain readable when printed in black and white.  
- All abbreviations (ACS, TCS, CHS, ND, Finance profile labels) have at least one **expanded first mention** somewhere visible in the flow.

If any item fails these checklists, the PM / designer must either fix it or record an explicit deviation note linked to this file.
