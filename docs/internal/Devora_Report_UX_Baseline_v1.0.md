# TruthSeal™ — Devora & Report UX Baseline v1.0

version: 1.0  
date_utc: 2025-12-02  
owner: TruthSeal™ — Dr. Nickolay Traykov (Prof. h.c.)  

scope: |
  Internal UX baseline for:
    - Devora (TruthSeal front-end assistant / console),
    - web reports,
    - PDF exports.
  This file defines the standard layout and language for coherence reports
  built on:
    - Aim Coherence Score (ACS),
    - Traykov Coherence Score v0.1 (TCS v0.1),
    - Coherence Score bands (CHS/L, CHS/M, CHS/H, CHS/UH),
    - profiles (Finance, Philosophical, Noise Distiller, future profiles),
    - receipts and anchoring (ts.receipt.v1, QENC, ledgers).
  Plans (Free / Pro / Enterprise / Network) may show or hide sections,
  but the structure and wording in this baseline must remain consistent.

---

## 0. Glossary — Laws, Metrics, Artifacts (expanded once)

This section expands the core shorthand used in the UX spec.
If a detail is not yet fully defined in code or doctrine, Devora must treat it
as `UNKNOWN` rather than guessing.

### 0.1 Laws and fields

- **ULLI** — TruthSeal governing proof mandate with three proofs:  
  **Academic Authority Proof**, **Technical Immutability Proof**,  
  **Live Measurability Proof**. Full doctrinal expansion lives in Doctorantura files.

- **Traykov Law of Quantum Coherence (TQC)** — hardware-anchored law that demands
  non-degrading coherence behaviour over time; “no free lunch” in risk.

- **Law of Ethical Irreversibility (LEI = 1)** — once a safer, more coherent,
  ethically superior option exists, the system is not allowed to downgrade back
  to a worse one.

### 0.2 Metrics

- **Aim Coherence Score (ACS)** — 0–1 metric that measures how well actions
  follow the declared aim and safety constraints over time.

- **Traykov Coherence Score v0.1 (TCS v0.1)** — 0–1 metric for overall
  intelligence coherence (truthfulness, post-quantum security strength,
  long-horizon self-consistency). Exact formula is defined in  
  `governance/metrics/Traykov_Coherence_Score_v0.1.md`.

- **Coherence Score (CHS)** — four-band status indicator for a system or device:
  - **CHS/L** — Low (Red)  
  - **CHS/M** — Medium (Yellow)  
  - **CHS/H** — High (Green)  
  - **CHS/UH** — Ultra High (Blue)  
  CHS is derived from TCS v0.1, ACS, and safety signals. Exact thresholds live in
  the TS-R robotics and safety-law documents.

### 0.3 Ledgers and proofs

- **ULIC** — Universal Law of Infinite Coherence registry block.  
- **EVL** — Epoch Verification Ledger (links proofs, metrics, and receipts).  
- **Integrity Manifest** — composite digest and anchor summary for an epoch.  
- **QENC ProofCapsule (QENC)** — cryptographic proof artifact linked from the
  Integrity Manifest.  
- **ts.receipt.v1** — canonical JSON receipt schema for TruthSeal decisions.

### 0.4 Hardware and profiles

- **TS-A1** — TruthSeal hardware-law profile for accelerators / GPUs.  
- **TS-R1** — TruthSeal Robotics profile for a single robot.  
- **TS-R2** — TruthSeal Robotics profile for a swarm / fleet of robots.  

- **TCS-Finance** — Traykov Coherence Score – Finance Profile (anti-bubble).  
- **TCS-ND** — Traykov Coherence Score – Noise Distiller Profile.  
- **Philosophical Profiles** — Archimedes, Aristotle, Hippocrates profiles as
  defined in `governance/metrics/TCS_Philosophical_Profiles_v0.1.md`.

### 0.5 Services and agents

- **Devora** — TruthSeal front-end assistant / console for running coherence
  checks, viewing reports, and exporting PDFs and receipts.

- **ASA** — Autonomous Scientific Agent layer used for internal analysis,
  never for unilateral deployment; all ASA outputs must be tied to receipts.

---

## 1. UX Goals & Audience

Devora and all TruthSeal reports must:

1. **Explain coherence at a glance**  
   - First-time users should immediately see:
     - overall TCS v0.1 percentage and band,
     - ACS status if relevant,
     - CHS band (if robotics / device-linked),
     - whether the result is anchored or anchor-ready.

2. **Keep Traykov laws visible without overwhelming**  
   - Laws (ULLI, TQC, LEI = 1) must be mentioned once in plain language,
     then referenced by short name.

3. **Make receipts and anchors tangible**  
   - Users should always see a clear path:
     - **“View receipt” → “Verify anchor / ledger entry”**.

4. **Support multiple plans without fragmenting UX**  
   - Free, Pro, Enterprise, and Network plans use the same page structure.
   - Sections that are not available in a plan are shown as greyed / locked,
     never removed in a way that breaks mental models.

Primary audiences:

- Everyday users and small teams (Free / Pro),
- Enterprise risk / compliance teams,
- Regulators and auditors,
- Robotics and hardware partners (TS-A1, TS-R1, TS-R2).

---

## 2. Standard “TruthSeal Coherence Report” Layout

Any Devora run that produces a full report (web or PDF) must use the layout
below. Plans may hide or lock some blocks, but not reorder them.

### 2.1 Above-the-fold summary (top of page)

Elements, from top to bottom:

1. **Case header bar**
   - Case title (user-provided or auto-generated),
   - organisation / user name (if available),
   - UTC timestamp,
   - unique case ID.

2. **Coherence overview band** (two columns on desktop, stacked on mobile)
   - Left side:
     - **TCS v0.1** as percentage (e.g. “87 %”),  
     - **TCS band** (Baseline / Silver / Gold / Diamond) with colour and canonical
       wording from `docs/internal/TCS_ACS_CHS_Baseline_v1.0.md`.
   - Right side:
     - **ACS status** (numeric + short text, if applicable),  
     - **CHS band** (if CHS is in scope) with colour and label  
       (CHS/L, CHS/M, CHS/H, CHS/UH).

3. **Anchoring badge**
   - One of:
     - “Receipt generated — anchoring pending”,
     - “Anchored via OpenTimestamps — view proof”,
     - “Lightweight receipt only — no blockchain anchoring for this plan”.
   - Link to receipt view (JSON and human-readable) where allowed.

4. **Plan and language strip**
   - Plan: Free / Pro / Enterprise / Network.  
   - Language: e.g. “Report language: English (canonical thresholds identical
     across languages).”

### 2.2 Secondary summary bar (below the fold start)

Short bullets:

- Content type analysed (e.g. “Finance video transcript”, “Policy article”),
- Profiles used (Finance, Noise Distiller, Philosophical, others),
- Any critical constraints (e.g. “No robotics integration in this report”).

---

## 3. Detailed Blocks

### 3.1 Case & context

Mandatory block with:

- Case description (free text, short),
- Source details (URL, uploaded file name, or manual text),
- User-supplied tags (optional).

### 3.2 Metrics detail

Sub-sections:

1. **Traykov Coherence Score v0.1 (TCS v0.1)**  
   - Show:
     - final score (0–1 and percentage),
     - band (Baseline / Silver / Gold / Diamond),
     - canonical band text from the TCS baseline file,
     - brief explanation of what dominated this result
       (truthfulness, security, consistency).

2. **Aim Coherence Score (ACS)** (if applicable)  
   - Show:
     - current ACS value and qualitative label (weak / partial / strong),
     - simple trend indicator if historical data is present
       (up arrow, flat, down arrow).

3. **Coherence Score (CHS) bands** (if applicable)  
   - Show:
     - current CHS band (CHS/L, CHS/M, CHS/H, CHS/UH),
     - clear language on what that means for:
       - physical actuation,
       - money movement,
       - interaction with people and children,
       - safe-stop behaviour.
   - Text must follow the TS-R Cherry Checklist and TS-R safety-law specs.

### 3.3 Profiles section

Show each active profile with a consistent pattern:

- **Finance Profile (TCS-Finance)**  
  - High-level verdict (e.g. “Exaggerated crash risk”, “Balanced risk wording”),  
  - short explanation of bubble / anti-bubble assessment.

- **Noise Distiller Profile (TCS-ND)**  
  - Short summary: proportion of signal vs noise,
  - key ND0x sub-scores (names only or full table depending on plan).

- **Philosophical Profiles**  
  - For each profile (Archimedes, Aristotle, Hippocrates):
    - 0–1 score,
    - short label (e.g. “mechanical / quantitative integrity”),
    - one-sentence practical explanation.

Plans may restrict which profiles appear or how detailed they are:

- Free: summaries only for Noise Distiller; no Finance or medical-sensitive detail.
- Pro: summaries + limited sub-scores.
- Enterprise / Network: full details as defined in the metrics specs.

### 3.4 Recommendations & prompts

At the end of the metrics and profiles section:

- Show the **locked recommendation sentence** from the TCS baseline:  
  “We highly recommend using these prompts to push toward Diamond and reduce residual risk.”
- Below it, show **3–5 concrete prompt suggestions** tailored to:
  - moving from Baseline → Silver,
  - Silver → Gold,
  - Gold → Diamond.

Prompt suggestions must be visible on screen and included in PDFs for Pro,
Enterprise, and Network plans.

### 3.5 Receipts & anchoring view

A dedicated block with:

- Receipt status (generated / pending / anchored),
- Short description of which artifacts exist:
  - `ts.receipt.v1` JSON,
  - QENC ProofCapsule reference (if present),
  - ledger links (ULIC, EVL, Integrity Manifest paths).
- **All receipts are signed using a post-quantum cryptography (PQC) scheme
  (Dilithium-class) and, where enabled, anchored via OpenTimestamps or an
  equivalent Bitcoin-anchored timestamping service.**
- Buttons or links:
  - “View human-readable receipt”,
  - “View JSON receipt”,
  - “Verify on ledger / OpenTimestamps” (where anchoring is enabled).

### 3.6 Legal guardrails

Mandatory text (some parts plan-dependent, but always visible):

- **Medical**  
  - “TruthSeal does not provide diagnosis, treatment, or clinical decisions.
    Reports evaluate information quality only.”
  - Hippocrates-style profiles are Enterprise-only and must be described as
    *information integrity* checks.

- **Politics**  
  - “TruthSeal does not optimise election campaigns, rank candidates,
    or predict election outcomes. Only factual claims may be evaluated.”

- **Robotics**  
  - “CHS bands and TS-R profiles are safety layers, not permission to ignore
    local laws or basic safety rules.”

---

## 4. Devora Interaction Pattern

Devora must follow this flow for any coherence run:

1. **Input step**
   - User selects input type (URL, text, upload) and chooses:
     - content domain (e.g. finance, general, safety),
     - whether robotics / CHS is in scope.

2. **Preview step**
   - Devora shows:
     - detected language,
     - estimated length / complexity,
     - which metrics and profiles will run for the current plan.

3. **Execution step**
   - Devora runs metrics and profiles,
     - shows progress clearly (never “hangs silently”),
     - records telemetry needed for receipts.

4. **Results step**
   - Shows the standard “TruthSeal Coherence Report” layout
     described in Section 2 and 3.

5. **Export & follow-up**
   - If the plan allows:
     - “Download PDF” (using standard template),
     - “Download JSON receipt”,
     - “Copy anchor / verification link”.
   - Devora offers next-step prompts:
     - re-run with modified content,
     - schedule recurring checks (Enterprise / Network),
     - open TS-R robotics dashboards (where applicable).

---

## 5. Multi-Language Behaviour

- English is the **canonical** language for thresholds and canonical band text.
- Other languages (BG, DE, PL, HU, etc.):
  - must keep the **same numeric thresholds and CHS meanings**,
  - may translate descriptions and recommendations,
  - must not alter or soften legal guardrails.
- Devora must always allow switching back to:
  - “View original English wording” for any legal or band text.

---

## 6. Plan-Specific UX Rules

This section defines how plans change **visibility**, not meaning.

### 6.1 Free

- Shows:
  - TCS v0.1 percentage + band + canonical band text,
  - minimal explanation of ACS (if applicable),
  - no CHS or TS-R sections.
- No PDF export, no JSON receipts, no anchoring links.
- Receipts block shows:
  - “Lightweight internal receipt only — anchoring not included in Free plan.”
- **Upsell line:** clearly display  
  “Upgrade to Pro to unlock JSON receipts, PDF export, and blockchain anchoring for critical reports.”

### 6.2 Pro

- Shows:
  - TCS v0.1, ACS, and CHS (if relevant),
  - summaries for Finance, Noise Distiller, and Philosophical profiles.
- PDF export enabled using the standard report template.
- Receipts:
  - JSON receipts downloadable for a subset of runs,
  - anchoring buttons may be available for “critical” cases only.

### 6.3 Enterprise

- Shows full detail:
  - all metrics,
  - all profiles (within legal constraints),
  - TS-R and CHS integrations where configured.
- Full PDF export (organisation branding), JSON receipts, and anchoring.
- Extra UI hooks:
  - audit logs,
  - regulator-facing export bundles.

### 6.4 Network / Platform

- Same as Enterprise but multi-tenant:
  - per-tenant branding where allowed,
  - per-tenant receipts and verification links.
- Devora may run as:
  - embedded widget,
  - white-label interface,
  - or central console for operators.

---

## 7. PM / Designer Checklist (Devora & Reports)

Before shipping any new Devora screen or report change, confirm:

1. TCS v0.1, ACS, and CHS acronyms are expanded once for first-time readers.  
2. TCS bands and text exactly match `TCS_ACS_CHS_Baseline_v1.0.md`.  
3. CHS band labels and colours (L/M/H/UH) match the TS-R safety specs.  
4. Laws (ULLI, TQC, LEI = 1) are referenced correctly and not renamed.  
5. Receipts and anchoring paths are visible wherever they exist.  
6. Free / Pro / Enterprise / Network differences only hide or lock sections;
   they do not change meanings or thresholds.  
7. Medical and political guardrails are present and unmodified.  
8. Multi-language views keep the same thresholds and CHS meanings.  
9. All exports (PDF, JSON) use the same structure as the on-screen report.  
10. Any missing detail is treated as `UNKNOWN` rather than guessed, in line with
    TruthSeal’s Zero-Guess discipline.

If any checklist item fails, the feature is **not** TruthSeal-ready and must
not be released under ULLI / TQC / LEI = 1.
