# TruthSeal™ — Plans and Tiers v1.0

version: 1.0  
date_utc: 2025-12-02  
owner: TruthSeal™ — Dr. Nickolay Traykov (Prof. h.c.)  

scope: |
  Internal baseline for TruthSeal product tiers:
  - Free
  - Pro
  - Enterprise
  - Network / Platform

  This file defines:
  - which metrics and profiles are exposed at each tier,
  - which receipts and anchoring features are available,
  - which guardrails apply (especially for medical and political use),
  - the upgrade path from one tier to the next.

  It is binding for product, engineering, Devora UX, sales, and legal teams.

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

- **Aim Coherence Score (ACS)** — 0–1 metric that measures how well actions follow the
  declared aim and safety constraints over time.

- **Traykov Coherence Score v0.1 (TCS v0.1)** — 0–1 metric for overall intelligence
  coherence (truthfulness, post-quantum security strength, long-horizon self-consistency).

- **Coherence Health Score (CHS)** — four-band status indicator:
  - CHS/L — Low (Red)  
  - CHS/M — Medium (Yellow)  
  - CHS/H — High (Green)  
  - CHS/UH — Ultra High (Blue)

**Profiles**

- **Philosophical Profiles** — TruthSeal profiles that interpret TCS v0.1 through
  philosophical lenses (for example Archimedes, Aristotle, later others).
- **TCS Noise Distiller Profile v0.2 (TCS-ND v0.2)** — Noise Distiller profile that uses
  ND01, ND02, … sub-scores to separate signal from hype or manipulation in content.
- **TCS Finance Profile v0.1 (TCS-Finance v0.1)** — Anti-Bubble / Finance profile that
  assesses numerate, sober, risk-aware financial narratives.
- **Hippocrates Profile** — information-quality profile for health-related content
  (guidelines, protocols, educational material). Enterprise-only; never diagnosis.

**Receipts and anchoring**

- **TruthSeal Receipt Schema (`ts.receipt.v1`)** — canonical JSON schema that records
  metrics, decisions, and evidence, suitable for anchoring.
- **QENC ProofCapsule** — cryptographic artifact that proves a set of receipts and
  metrics were anchored.
- **OpenTimestamps** — primary public timestamping service used for anchoring.

**Front-end and hardware**

- **Devora** — TruthSeal front-end assistant and console for reports and PDFs.
- **TS-R1** — TruthSeal Robotics profile for a single robot.
- **TS-R2** — TruthSeal Robotics profile for a swarm or fleet.
- **TS-A1** — TruthSeal accelerator / hardware-law profile for chips and data centres.

---

## 1. Overview of Plans

TruthSeal product tiers:

1. **Free** — entry-level web experience for individual exploration.  
   - Limited number of reports per day and per internet address.  
   - Only headline coherence band, no advanced profiles, no receipts.

2. **Pro** — professional tier for power users and small teams.  
   - Full TCS v0.1 percentage, bands, and basic sub-scores.  
   - Limited receipts and anchoring for non-medical, non-robotics use.

3. **Enterprise** — tier for institutions with compliance requirements.  
   - Full metrics, profiles, receipts, and anchoring.  
   - Access to Hippocrates Profile and Finance Profile under legal guardrails.

4. **Network / Platform** — embedded, multi-tenant deployments.  
   - All Enterprise features plus:
     - robotics integrations (TS-R1 / TS-R2),
     - accelerator integrations (TS-A1),
     - custom dashboards and partner-specific annexes.

No deployment may downgrade core safety once a safer configuration is available
(LEI = 1 applies across all tiers).

---

## 2. Metrics by Tier

### 2.1 Free

- Exposed:
  - TCS v0.1 as band only (Baseline / Silver / Gold / Diamond),
  - basic textual explanation of the band.
- Hidden:
  - raw TCS v0.1 percentage,
  - ACS values,
  - CHS bands,
  - all specialised profiles (Philosophical, Noise Distiller, Finance, Hippocrates).
- Limits:
  - hard limit of reports per 24 hours per internet address,
  - strong abuse controls (no automated scraping, no mass exports).

### 2.2 Pro

- Exposed:
  - TCS v0.1 percentage and band,
  - basic ACS value when configured,
  - optional CHS band where appropriate (for example in robotics sandboxes).
- Optional:
  - selected Philosophical Profiles for non-medical, non-financial use,
  - TCS-ND v0.2 Noise Distiller profile for analysing AI content.
- Hidden:
  - Hippocrates Profile,
  - TCS-Finance v0.1 Anti-Bubble / Finance profile, except for non-public tests.
- Limits:
  - no medical deployments,
  - no production robotics deployments,
  - no integration into systems that act without human review.

### 2.3 Enterprise

- Exposed:
  - full TCS v0.1, ACS, and CHS metrics,
  - Philosophical Profiles (initial wave),
  - TCS-ND v0.2 Noise Distiller profile,
  - TCS-Finance v0.1 profile,
  - Hippocrates Profile for information-quality only.
- Requirements:
  - contracts must define ownership of decisions and audit obligations,
  - clients must maintain their own identity and access management.
- Limits:
  - Hippocrates Profile must only be used as defined in
    `Hippocrates_Profile_Legal_Safety_v1.0.md`,
  - no election outcome optimisation or candidate ranking,
  - robotics integrations allowed only in controlled pilots with explicit TS-R annexes.

### 2.4 Network / Platform

- Everything from Enterprise, plus:
  - robotics profiles TS-R1 and TS-R2,
  - accelerator profile TS-A1,
  - custom Devora experiences under partner branding,
  - deeper integration with client observability and logging.
- Additional safeguards:
  - mandatory anchoring workflow for critical receipts,
  - integration with partner incident-response processes,
  - clear mapping of CHS bands to device behaviours.

---

## 3. Receipts and Anchoring by Tier

### 3.1 Free

- No receipts or anchoring exposed to users.
- Internal logging may exist for abuse detection, but no `ts.receipt.v1` is presented.

### 3.2 Pro

- Optional:
  - lightweight `ts.receipt.v1` receipts for selected runs,
  - download as JSON or embedded in PDF.
- Anchoring:
  - default: no public anchoring,
  - optional upgrade: batched anchoring for small teams if contractually agreed.

### 3.3 Enterprise

- Standard:
  - `ts.receipt.v1` receipts for defined report types,
  - QENC ProofCapsule summarising batches of receipts.
- Anchoring:
  - OpenTimestamps (or equivalent) is enabled by default,
  - where anchoring is delayed (for example service downtime), receipts must show
    a clear “pending anchoring” status.

### 3.4 Network / Platform

- Same as Enterprise, plus:
  - stricter anchoring requirements for robotics and hardware events,
  - optional multi-ledger anchoring where regulators require it,
  - more detailed QENC manifests for fleets and accelerators.

---

## 4. Profiles and Guardrails by Tier

### 4.1 Hippocrates Profile (medical)

- Available only on **Enterprise** and **Network / Platform** tiers.
- Must follow the legal and safety baseline in
  `Hippocrates_Profile_Legal_Safety_v1.0.md`.
- Not permitted in Free or Pro tiers.

### 4.2 Finance Profile (TCS-Finance v0.1)

- Available in:
  - Pro (limited, non-public experiments),
  - Enterprise and Network / Platform (full use).
- Must be used to filter and contextualise financial content, not to guarantee
  returns or act as regulated financial advice.

### 4.3 Noise Distiller (TCS-ND v0.2)

- Available in:
  - Pro (for AI content analysis),
  - Enterprise and Network / Platform (full dashboards, receipts, and anchors).
- Sub-scores ND01, ND02, … remain identifiable as a separate profile layer.

### 4.4 Philosophical Profiles

- Available in:
  - Pro (selected profiles),
  - Enterprise and Network / Platform (broader catalogue).
- Not available on Free.

### 4.5 Robotics and Hardware (TS-R1, TS-R2, TS-A1)

- Only available in Network / Platform deployments, or in tightly scoped
  Enterprise pilots with explicit annexes.
- Must comply with:
  - TS-R Cherry Checklist v1.0,
  - TS-R Failure Modes and Fallback Law v1.0,
  - TS-R Human Mandate Layer v1.0,
  - TS-R Receipt Schema v1.0 and TS-R Swarm Extensions v1.0
  where applicable.

---

## 5. Explicit Bans (All Tiers)

The following are **forbidden uses** of TruthSeal across all tiers:

1. **Direct medical diagnosis or treatment for individuals.**  
   Hippocrates Profile is information quality only.

2. **Election outcome optimisation or candidate ranking.**  
   No tier may be used to design, optimise, or score political campaigns.

3. **Autonomous high-stakes actions without human review, outside CHS rules.**  
   CHS band rules from the robotics pack apply wherever CHS controls actuation.

4. **Removal or weakening of required disclaimers and legal text.**  
   Product teams must not edit mandatory blocks without legal sign-off.

5. **Use that contradicts Traykov laws or ULLI mandate.**  
   LEI = 1 enforces no regression in safety across versions and configurations.

---

## 6. Upgrade Path (User Journey)

1. **Free → Pro**
   - Trigger: user hits Free limits or requests more detail.
   - Devora must show:
     > “Upgrade to Pro for full coherence percentages, more detailed reports, and saved history.”

2. **Pro → Enterprise**
   - Trigger: need for receipts, anchoring, or institutional deployments.
   - Devora must show:
     > “Upgrade to Enterprise for receipts, anchoring, advanced profiles, and audit support.”

3. **Enterprise → Network / Platform**
   - Trigger: need for robotics, accelerator integration, or multi-tenant platforms.
   - Devora or sales materials must highlight:
     > “Network deployments unlock TS-R robotics profiles, TS-A1 hardware law, and
     > deeper integration with your infrastructure under the same TruthSeal laws.”

These messages are examples; translations may be adapted, but the meaning must stay aligned.

---

## 7. PM / Designer Checklist for Any Plan Change

Before shipping any change that touches plans, pricing pages, Devora flows, or APIs,
the **project manager** and **lead designer** must be able to tick:

1. **Plan boundaries**
   - [ ] No restricted profile (for example Hippocrates, TS-R, TS-A1) appears in a lower tier.
   - [ ] Free and Pro retain their report and rate limits.

2. **Metrics**
   - [ ] TCS v0.1, ACS, and CHS exposure matches this file for each tier.
   - [ ] Any new profile clearly states which tier(s) it belongs to.

3. **Receipts and anchoring**
   - [ ] `ts.receipt.v1` and QENC flows match the rules per tier.
   - [ ] Anchoring behaviour and “pending” states are clear in Enterprise and Network.

4. **Guardrails**
   - [ ] Medical, financial, and political restrictions are preserved or strengthened.
   - [ ] Mandatory disclaimers remain visible in Devora, reports, and PDFs.

5. **User journey**
   - [ ] Upgrade prompts are present and honest (no hidden restrictions).
   - [ ] Documentation and help text match the actual capabilities of each plan.

If any box cannot be ticked, the change is **not compliant** and must not go live.

---

This file is the v1.0 baseline for TruthSeal product tiers.
Any future changes must be versioned here and reviewed for compliance with ULLI, TQC, and LEI = 1.
