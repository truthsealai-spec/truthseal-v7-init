# TruthSeal™ — Plans and Tiers v1.0
version: 1.0  
date_utc: 2025-12-01  
owner: TruthSeal™ — Dr. Nickolay Traykov (Prof. h.c.)  

scope: |
  Internal product baseline for TruthSeal service plans and tiers.
  Defines:
  - which metrics (ACS, TCS v0.1, CHS) are exposed in each plan,
  - which profiles (Finance, Philosophical, Noise Distiller) are included,
  - usage limits (per-day / per-month),
  - report / PDF / receipt features,
  - exclusions for medical and political use.
  This file is for internal product, engineering, and commercial teams.

---

## 1. Shared Invariants (all plans)

These apply to **every** plan (Free → Network).

- **Aim Coherence Score (ACS)** and **Traykov Coherence Score v0.1 (TCS v0.1)** are the primary internal metrics.
- **Coherence Score (CHS)** is the 4-band device/status indicator:
  - CHS/L (Low, Red)  
  - CHS/M (Medium, Yellow)  
  - CHS/H (High, Green)  
  - CHS/UH (Ultra High, Blue)
- All plans operate under:
  - LEI=1 (Law of Ethical Irreversibility),
  - Traykov Coherence Law / TruthSeal sovereign governance,
  - standard receipt schema `ts.receipt.v1`.
- **No clinical diagnosis or treatment decisions.**
  - TruthSeal does **not** certify medical prescriptions, clinical decisions, or individual patient treatment.
  - Health-related content may be analysed only as *information quality*, with clear “not medical advice” wording.
- **No election outcome scoring or political campaign optimisation.**
  - We may analyse *factual claims* (e.g. “GDP is X”), but we do not rate parties, candidates, or advise campaigns.
- **All serious outputs can be anchored.**
  - Plans differ in *how often* and *at which volume* receipts are anchored (OpenTimestamps/other ledgers), but the schema is the same.
- **Multilingual support.**
  - UI and reports localisable (e.g. EN, BG, DE, PL, HU + others).
  - Underlying metrics and thresholds remain identical across languages.

---

## 2. Plan Overview

Plans (v1.0):

1. **Free (Discovery)**
2. **Pro (Professional)**
3. **Enterprise**
4. **Network / Platform**

Prices are set in commercial documents and the ACS financial model; this spec only defines **capabilities and limits**.

---

## 3. Free Plan — “Discovery”

Purpose: let individuals and small teams experience TruthSeal without abuse.

Typical users:  
- Individual researchers, content creators, curious users.

Capabilities:

- **Input types:** URLs and text (general content).  
- **Metrics:**  
  - TCS v0.1 overall score + band (Baseline / Silver / Gold / Diamond).  
  - Basic explanation text from the TCS/ACS/CHS report template.  
- **Profiles included:**  
  - Core TCS v0.1  
  - Noise Distiller (TCS-ND v0.1) – summary only (no full coefficient table).
- **Limits:**  
  - 1 full report per **24 hours per IP** (anti-abuse).  
  - Max input length: moderate (e.g. single video/article).  
- **Reports:**  
  - On-screen report only (no branded PDF export, no email delivery).  
  - No custom branding, no white-label.
- **Receipts:**  
  - Lightweight receipt ID; **no guaranteed blockchain anchoring**.
- **Support:**  
  - Self-service docs + FAQ; no human SLA.

Exclusions:

- Finance, robotics, and enterprise integrations are **not** supported in Free.  
- No API access.

---

## 4. Pro Plan — “Professional”

Purpose: serve professionals and small businesses that need regular, high-quality coherence checks.

Typical users:  
- Analysts, small funds, media teams, risk/compliance analysts, senior creators.

Capabilities:

- **Input types:** URLs, text, and uploads within size limits.  
- **Metrics:**  
  - TCS v0.1 + band + percentage.  
  - ACS (where applicable, e.g. for agent runs).  
  - CHS band for eligible agent/robotic runs (read-only).  
- **Profiles included:**  
  - Core TCS v0.1  
  - Noise Distiller v0.1 (with sub-score block)  
  - Philosophical Profiles (Archimedes / Aristotle / Hippocrates) in summary form  
  - Finance Profile (TCS-Finance v0.1) for tagged financial content.
- **Limits:**  
  - Daily/monthly quota suitable for professional use (exact numbers set in billing config).  
  - Single-tenant account; manual project tagging.
- **Reports & PDFs:**  
  - Branded PDF exports using the standard TCS/ACS/CHS template.  
  - Optional scheduled email reports (controlled frequency to avoid spam).  
  - “Pro prompts” section included in every Silver/Gold/Diamond report.
- **Receipts:**  
  - JSON receipts via dashboard or download.  
  - Optional anchoring for a subset of reports (e.g. marked “critical”) per month.
- **Support:**  
  - Email support with reasonable response-time target (business hours).

Exclusions / guardrails:

- No formal **regulatory** certification wording (that is Enterprise-only).  
- No direct control of robots or CHS gating; CHS remains an informational metric.

---

## 5. Enterprise Plan

Purpose: for institutions that require integrated, auditable coherence and noise metrics, often with regulators watching.

Typical users:  
- Banks, insurers, listed companies, government departments, critical vendors.

Capabilities:

- Everything in **Pro**, plus:

- **Metrics & profiles:**  
  - Full TCS v0.1 breakdown (per-subscore where allowed).  
  - Full Noise Distiller coefficient table and hard ND0x sub-scores.  
  - Finance Profile (TCS-Finance) in full detail.  
  - Philosophical Profiles with per-profile sub-scores (Archimedes / Aristotle / Hippocrates).  
  - ACS telemetry feeds (where integrated with their systems).  
- **Usage & scale:**  
  - Higher or unlimited rated quotas per contract.  
  - Multi-user seats, SSO, audit logs of who requested which verdicts.
- **Reports & PDFs:**  
  - Fully branded PDFs with organisation name, case IDs, and legal disclaimers.  
  - Scheduled batch reports (e.g. daily risk digest).  
  - Export to internal archives and GRC systems.
- **Receipts & anchoring:**  
  - Full JSON receipts per request.  
  - Configurable anchoring policy (e.g. all “critical” reports auto-anchored via OpenTimestamps).  
  - Support for integration with internal ledgers and archives.
- **Robotics / CHS integration (optional module):**  
  - Read/write integration with ACS and CHS values for TS-R1/R2 compatible robots.  
  - Ability to require certain CHS bands for specific workflows (e.g. CHS/H or CHS/UH for certain tasks).  
  - Still subject to hardware-law specs and Failure Modes & Fallback Law.
- **Support & governance:**  
  - Named account manager.  
  - Commercial SLAs.  
  - Optional assistance for regulator-facing documentation and pilots.

Exclusions / guardrails:

- Medical use limited to **information quality auditing** (no clinical decision assurance).  
- No election campaign optimisation or candidate ranking.

---

## 6. Network / Platform Plan

Purpose: for platforms that want to offer TruthSeal-powered coherence checks to their own users as a feature.

Typical users:  
- AI platforms, cloud providers, marketplaces, robotics OEMs, large media or education platforms.

Capabilities:

- Everything in **Enterprise**, plus:

- **Multi-tenant integration:**  
  - API-level integration where each end-user gets their own receipts and PDFs under the platform’s umbrella.  
  - Per-tenant quotas and usage reporting.  
- **White-label options:**  
  - Co-branded or white-labelled reports (“Powered by TruthSeal™”).  
  - Custom URL patterns for verify pages.
- **Deep robotics integration (TS-R track):**  
  - Fleet-level CHS dashboards for TS-R2.  
  - Policy templates for CHS gating (e.g. default rules for CHS/L–M–H–UH).  
- **Economic model alignment:**  
  - Pricing and ROI modelling tied to the TS-R Economic Impact Note and ACS Financial Model.

Exclusions / guardrails:

- Same medical and political restrictions as Enterprise.  
- Extra due diligence on platform abuse risk (e.g. not enabling disallowed use-cases downstream).

---

## 7. Language and Localisation

- Launch languages: English first; additional languages can be turned on by region.  
- All numeric thresholds, bands, and CHS meanings remain identical across languages.  
- Translations must follow the canonical wording from:
  - `docs/internal/TCS_ACS_CHS_Baseline_v1.0.md`
  - this Plans & Tiers spec
  - the TCS/ACS/CHS report and receipt template.

---

## 8. Roadmap Notes (post-Christmas)

Not in this release, but explicitly on the roadmap:

- Dedicated **Medical Information Profile** (information-only, non-diagnostic), with separate legal review.  
- Household / safety robots CHS bundle (family mode, gas/fire/leak alerts, children & pets rules).  
- More granular sub-plans (e.g. “Robotics only”, “Content only”) derived from this v1.0 structure.

This document is the v1.0 baseline. Any change to plan capabilities or guardrails must be versioned here and reflected in pricing, marketing, and contracts.
