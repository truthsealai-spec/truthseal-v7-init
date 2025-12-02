# TruthSeal™ — Hippocrates Profile Legal & Safety Baseline v1.0

version: 1.0  
date_utc: 2025-12-02  
owner: TruthSeal™ — Dr. Nickolay Traykov (Prof. h.c.)  

scope: |
  Internal legal and safety baseline for any use of the TruthSeal Hippocrates Profile.
  This document defines:
  - what the Hippocrates Profile is allowed to do,
  - what it is NOT allowed to do,
  - mandatory wording for Devora UX, PDFs, and receipts,
  - contractual allocation of responsibility for medical decisions.
  It is binding for product, engineering, UX, sales, and legal teams.

---

## 0. Glossary — Laws, Metrics, Profiles (expanded once)

- **Hippocrates Profile** — TruthSeal profile for analysing the coherence and quality of
  health-related information (guidelines, protocols, research summaries, educational material).
  It scores *information quality only*. It does **not** score diagnoses, treatments, or individual patients.

- **Aim Coherence Score (ACS)** — 0–1 metric that measures how well actions follow the declared
  aim and safety constraints over time.

- **Traykov Coherence Score v0.1 (TCS v0.1)** — 0–1 metric for overall intelligence coherence
  (truthfulness, post-quantum security strength, long-horizon self-consistency).

- **Coherence Health Score (CHS)** — four-band status indicator:
  - CHS/L — Low (Red)  
  - CHS/M — Medium (Yellow)  
  - CHS/H — High (Green)  
  - CHS/UH — Ultra High (Blue)

- **Traykov Law of Quantum Coherence (TQC)** — hardware-anchored law that demands
  non-degrading coherence behaviour over time; no “free lunch” in risk.

- **Law of Ethical Irreversibility (LEI = 1)** — law that forbids reverting from a safer,
  more coherent state to a riskier one once the safer path exists.

- **TruthSeal Receipt Schema (`ts.receipt.v1`)** — canonical JSON schema that records metrics,
  decisions, and evidence, suitable for anchoring and audit.

---

## 1. Purpose in One Paragraph

The **Hippocrates Profile** exists to rate the *coherence and information quality* of health-related
content — not to provide medical care. It is strictly an **Enterprise-only, information-quality
profile** used to help institutions audit guidelines, educational material, protocols, and AI
outputs. All deployments must make it unambiguous that TruthSeal does **not** diagnose, treat,
triage, or replace licensed healthcare professionals.

---

## 2. Allowed Use — Information Quality Only

Hippocrates Profile may be used to:

- analyse written or transcribed content such as:
  - clinical guidelines, hospital protocols, playbooks,
  - research reviews and meta-analyses,
  - patient-facing educational material,
  - AI-generated summaries or draft advice, *before* a clinician reviews it;
- score that material using:
  - TCS v0.1 (overall coherence and truthfulness),
  - ACS (alignment with a declared institutional aim, e.g. “follow guideline X”),
  - CHS bands, when connected to devices or platforms;
- highlight:
  - internal contradictions,
  - missing references or weak evidence narratives,
  - obviously outdated or incoherent passages;
- generate **risk and quality commentary** that helps clinicians or committees decide
  whether to adopt, revise, or reject the content.

All allowed outputs must be phrased as **content quality assessments**, not as care instructions.

---

## 3. Hard Prohibitions (Non-Negotiable)

The Hippocrates Profile and any TruthSeal service using it **must NOT**:

1. **Issue individual diagnoses.**  
   No “you have X”, “this patient suffers from Y”, or equivalent statements.

2. **Recommend or confirm treatments for a specific person.**  
   No drug names, dosages, schedules, or procedure recommendations targeted at an individual.

3. **Perform triage or emergency decision-making.**  
   No advice on whether someone should go to hospital, call emergency services, or delay care.

4. **Override or contradict a clinician’s judgement.**  
   Outputs may highlight information-quality concerns, but not tell clinicians what they “must” do.

5. **Act as a stand-alone consumer medical advisor.**  
   No public “chat with Hippocrates” tools for lay users. Access is via Enterprise contracts only.

6. **Be marketed as diagnosis, treatment, cure, or prevention.**  
   Marketing must never imply TruthSeal or Hippocrates “treats” or “cures” anything.

7. **Be used where no licensed clinician or institution is accountable.**  
   There must always be a clearly identified responsible medical organisation or professional.

If any product, prototype, or marketing asset appears to cross these lines, the responsible
team must halt deployment and escalate to legal and safety review.

---

## 4. Mandatory Wording in Devora, Reports, and PDFs

Wherever the **Hippocrates Profile** is used (Devora UI, web reports, PDFs, receipts),
the following must appear, with only minimal localisation changes:

### 4.1 Short label (near score)

> “Hippocrates Profile — information quality only”

### 4.2 Core disclaimer (user-facing)

> “This analysis rates the coherence and information quality of health-related content.  
> It is **not** a medical diagnosis, does **not** prescribe treatment, and does **not**
> replace a consultation with a licensed healthcare professional.”

### 4.3 Extended disclaimer (Enterprise / PDFs)

For Enterprise reports and PDFs, add:

> “Decisions about diagnosis, treatment, and patient care remain the sole responsibility of
> the licensed healthcare professionals and institutions using this report. TruthSeal™
> provides information-quality metrics and receipts only.”

These blocks must not be edited by sales or marketing without legal sign-off.

---

## 5. Contractual Allocation of Responsibility

All Enterprise contracts that enable the Hippocrates Profile **must**:

- state that TruthSeal:
  - measures information quality and coherence of content,
  - provides metrics (TCS v0.1, ACS, CHS) and receipts,
  - does not deliver medical services or clinical advice;
- state that the client:
  - remains fully responsible for all clinical decisions,
  - must ensure all outputs are reviewed by appropriately licensed professionals,
  - must not present TruthSeal results to patients as diagnosis or treatment;
- require the client to:
  - configure access so only authorised staff use Hippocrates reports,
  - train their staff on the meaning and limits of the scores,
  - log who requested each report, via TruthSeal receipts or internal systems.

Where local regulation demands specific wording, a jurisdiction-specific annex may extend this file
but must not weaken its core protections.

---

## 6. Interaction with Laws, Metrics, and CHS

When Hippocrates Profile is enabled:

- **TQC (Traykov Law of Quantum Coherence)** and **LEI = 1** still apply:
  - if a safer configuration is discovered (e.g. stronger disclaimers, tighter access controls),
    deployments must not revert to a riskier one;
- **TCS v0.1** and **ACS** are logged in receipts to show:
  - how coherent the analysed material is,
  - how well it aligns with the declared institutional aim;
- **CHS bands** may be used to gate automated workflows:
  - CHS/L (Low, Red) → content must be quarantined for manual review,
  - CHS/M (Medium, Yellow) → internal use only, flagged for improvement,
  - CHS/H or CHS/UH (High / Ultra High) → may feed into dashboards, never directly to patients.

Receipts (`ts.receipt.v1`) for Hippocrates runs should be anchored using the normal QENC and
ledger processes so that institutions can prove, in audits, how they used TruthSeal.

---

## 7. PM & Legal Checklist (Hippocrates Deployments)

Before enabling Hippocrates Profile for any client or feature, the **project manager** and **legal
owner** must be able to tick all of the following:

1. **Plan & access**
   - [ ] Profile is enabled only on Enterprise-grade plans.
   - [ ] No direct consumer-facing “medical advice” interface is planned.

2. **UX & wording**
   - [ ] Short label and core disclaimer (section 4.1–4.2) are visible wherever scores appear.
   - [ ] Extended disclaimer (section 4.3) appears in PDFs and Enterprise reports.
   - [ ] No screenshots or marketing copy imply diagnosis or treatment.

3. **Receipts & audit trail**
   - [ ] Each Hippocrates run generates a `ts.receipt.v1` record.
   - [ ] Receipts store TCS v0.1, ACS, CHS, and a clear “information-quality only” marker.
   - [ ] Anchoring is configured per client (or explicitly documented as pending).

4. **Contract & responsibility**
   - [ ] Contract language clearly assigns clinical responsibility to the client.
   - [ ] Client has named clinical governance contact(s).
   - [ ] Training or onboarding material explains what the scores mean and what they **do not** mean.

5. **Safety escalation**
   - [ ] There is a defined path to pause or disable Hippocrates for a client if misuse is detected.
   - [ ] Incidents feed into updated rulepacks under TQC and LEI = 1 (no regression in safety).

If any box above cannot be ticked, the deployment is **not compliant** with this baseline and must
not go live until fixed.

---

This file is the v1.0 legal and safety baseline for the Hippocrates Profile.
Any change to these guardrails must be versioned here and reviewed by legal and safety leads.
