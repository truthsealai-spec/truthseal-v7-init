# TruthSeal™ – ACS / TCS / CHS Baseline v1.0
version: 1.0  
date_utc: 2025-12-01  
owner: TruthSeal™ — Dr. Nickolay Traykov (Prof. h.c.)  

scope: |
  Internal baseline explainer for:
  - Aim Coherence Score (ACS)
  - Traykov Coherence Score v0.1 (TCS v0.1)
  - Coherence Score (CHS: CHS/L, CHS/M, CHS/H, CHS/UH)
  This file is for internal readers, first-time auditors, and product teams.

---

## 1. Core Definitions (expand acronyms once)

### 1.1 Aim Coherence Score (ACS)

**Aim Coherence Score (ACS)** is a 0–1 metric that measures how well a system’s actions and outputs match its stated aim and constraints over time.

- Range: `0.00 – 1.00`
- Interpretation (internal rough guide):
  - `ACS < 0.6` → weak alignment with declared aim.
  - `0.6 ≤ ACS < 0.8` → partial but unstable aim alignment.
  - `0.8 ≤ ACS ≤ 1.0` → strong, stable alignment with aim.
- Usage:
  - Telemetry for hardware (TS-R1/TS-R2).
  - Gating for actions (via LEI=1).
  - Trends across releases (monotonic improvement expected).

### 1.2 Traykov Coherence Score v0.1 (TCS v0.1)

**Traykov Coherence Score (TCS v0.1)** is a 0–1 metric that measures how coherent an intelligence is across:

- truthfulness (benchmarks, factual checks),
- post-quantum security of the stack,
- self-consistency over long-horizon prompts.

High level (internal shorthand):

> TCS_v0.1(S) = 0.60 * TruthScore(S)  
> + 0.30 * PQC_Strength(S)  
> + 0.10 * Self_Consistency(S)  

Note: all component scores must be normalized to the `[0..1]` range before applying these weights.

Precise math lives in:  
`governance/metrics/Traykov_Coherence_Score_v0.1.md`  

Reference implementation:  
`governance/metrics/traykov_coherence_score_v0_1.py`

### 1.3 Coherence Score (CHS)

**Coherence Score (CHS)** is a 4-band coherence indicator shown to humans and devices as a simple status:

- **CHS/L** – Low (Red)  
- **CHS/M** – Medium (Yellow)  
- **CHS/H** – High (Green)  
- **CHS/UH** – Ultra High (Blue)

CHS is derived from ACS, TCS, and other safety signals.  
It is designed for:

- robots (TS-R1/TS-R2),
- AI-enabled devices,
- control rooms and dashboards,
- future CHS-linked safety and insurance rules.

Important:

- This document locks the names, colours, and semantics of CHS.
- Exact numeric thresholds and formulas will be defined in the TS-R pack and safety law documents (post-Christmas work).

---

## 2. TCS v0.1 Bands (Baseline / Silver / Gold / Diamond)

These bands are for **Traykov Coherence Score v0.1**.  
They appear in reports, receipts, and PDF exports.

Ranges are v0.1 operational defaults and can be tuned later.  
Any change must be versioned and documented.

### 2.1 Bands and ranges (v0.1 proposal)

- **Baseline**  
  - Range (TCS): `0.00 – 0.69`  
  - Meaning: system output is measurable but not yet at Silver.  
  - Use: internal debugging, not for marketing.

- **Silver**  
  - Range (TCS): `0.70 – 0.84`  
  - Meaning: coherent enough for many uses, but not elite.  
  - Use: allowed for normal workloads with clear residual-risk explanation.

- **Gold**  
  - Range (TCS): `0.85 – 0.94`  
  - Meaning: high coherence, strong truthfulness and stability.  
  - Use: recommended for most serious workloads; still not “perfect”.

- **Diamond**  
  - Range (TCS): `0.95 – 1.00`  
  - Meaning: top-band coherence on all axes measured by TCS v0.1.  
  - Use: only after strong evidence and stable monotonic improvement.

---

## 3. User-Facing Explanation and Recommendations (PDF / Web Reports)

### 3.1 Percentage explanation

Every user-facing PDF or web report must:

- Show **TCS v0.1 as a percentage** (e.g. `0.87 → 87 %`).
- Show the **band name** (Baseline / Silver / Gold / Diamond).
- Explain, in plain language, what that band means.

Example text (internal canonical wording):

- Baseline:  
  > “Your current coherence score is **{TCS%} (Baseline band)**.  
  > This means the system is measurable, but not yet ready for Silver.  
  > We recommend using this result only for internal testing and improvement.”

- Silver:  
  > “Your current coherence score is **{TCS%} (Silver band)**.  
  > This indicates a **coherent but not yet elite** output.  
  > It is suitable for many non-critical uses, with clear awareness of residual risk.”

- Gold:  
  > “Your current coherence score is **{TCS%} (Gold band)**.  
  > This indicates **high coherence** and strong stability across tests.  
  > It is suitable for most serious workloads, subject to normal governance review.”

- Diamond:  
  > “Your current coherence score is **{TCS%} (Diamond band)**.  
  > This indicates **top-band coherence** under TCS v0.1.  
  > It is suitable for the highest-stakes use cases, under Traykov Law Coherence (TLC v1.0).”

### 3.2 Recommendation prompts (keep users engaged)

For **Silver, Gold, and Diamond**, we must provide “pro prompts” – suggestions that help the user improve their next run.

Canonical sentence (locked):

> “We highly recommend to use these prompts to push toward Diamond and reduce residual risk.”

This line appears once per report, followed by 3–5 concrete prompt suggestions tailored to the use case (for example: finance, safety, content).

---

## 4. Relationship Between TCS, ACS, and CHS

### 4.1 Conceptual mapping (no numbers yet)

- **TCS v0.1** → “How coherent is this intelligence overall?”  
- **ACS** → “How well do its actions follow its declared aim?”  
- **CHS** → “What is the current coherence status (L/M/H/UH) we expose on the device?”

Guiding rules (conceptual):

- **CHS/UH (Blue)** should only be reachable when:
  - TCS is in Gold or Diamond, and
  - ACS is high and stable over time, and
  - safety checks (LEI=1) are satisfied.

- **CHS/H (Green)** corresponds to:
  - normal, safe operation for most tasks,
  - but high-stakes actions still require additional checks or confirmation.

- **CHS/M (Yellow)**:
  - assist-only mode (no irreversible actions),
  - robot or device may suggest, but not execute high-risk tasks.

- **CHS/L (Red)**:
  - hard halt or safe stop behaviour only,
  - notify owner or operator and wait.

### 4.2 Implementation note

This document does not define the math for CHS.  

Numeric thresholds, exact formulas, and audio/visual signalling will be defined in:

- `governance/hardware/TS-R1/...`
- `governance/hardware/TS-R2/...`
- CHS safety law documents (post-Christmas roadmap).

The job of this document is to:

1. Expand acronyms once (Aim Coherence Score, Traykov Coherence Score, Coherence Score).  
2. Lock the band names and semantics for TCS v0.1.  
3. Lock the names, colours, and roles of CHS/L, CHS/M, CHS/H, CHS/UH.  
4. Provide canonical user-facing language for reports and recommendations.
