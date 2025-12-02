# TruthSeal™ — Third Guardian Firewall & ASA v1.0

version: 1.0  
date_utc: 2025-12-02  
owner: TruthSeal™ — Dr. Nickolay Traykov (Prof. h.c.)  

scope: |
  Internal specification for the Third Guardian AI Firewall and ASA (Autonomous Scientific Agent) layer.
  Protects TruthSeal ledgers, receipts, hardware-law profiles, and front-end services from hostile traffic,
  incoherent agents, and attempts to bypass TruthSeal laws. This document is for engineers, auditors,
  security teams, and product managers.

---

## 0. Glossary — Laws, Metrics, Profiles (expanded once)

**Core laws & fields**

- **ULLI** — TruthSeal governing proof mandate with three pillars:
  Academic Authority Proof, Technical Immutability Proof, and Live Measurability Proof.
  (Full doctrinal text lives in Doctorantura files.)
- **Traykov Law of Quantum Coherence (TQC)** — hardware-anchored law that demands
  non-degrading coherence behaviour over time; no “free lunch” in risk.
- **Law of Ethical Irreversibility (LEI = 1)** — once a safer, more coherent state is reached,
  the system is not allowed to downgrade back to a worse, riskier option.
- **TruthSeal Cognitive Coherence Law (LTCC)** — high-level law that demands truthful,
  self-consistent cognition across long horizons.

**Metrics**

- **Aim Coherence Score (ACS)** — 0–1 metric for how well actions follow the declared aim
  and safety constraints over time.
- **Traykov Coherence Score v0.1 (TCS v0.1)** — 0–1 metric for overall intelligence
  coherence (truthfulness, post-quantum security strength, long-horizon self-consistency).
- **Coherence Score (CHS)** — four-band status indicator for a system or device:
  - CHS/L — Low (Red)  
  - CHS/M — Medium (Yellow)  
  - CHS/H — High (Green)  
  - CHS/UH — Ultra High (Blue)

**Profiles, ledgers, artefacts**

- **TS-A1** — TruthSeal hardware-law profile for accelerators / GPUs and data-centre nodes.
- **TS-R1** — TruthSeal Robotics profile for a single robot.
- **TS-R2** — TruthSeal Robotics profile for swarms / fleets.
- **ULIC** — Universal Law of Infinite Coherence registry block (law registry).
- **EVL** — Epoch Verification Ledger (records verified artefacts per epoch).
- **Integrity Manifest** — composite digest tying verified artefacts to the registry.
- **QENC ProofCapsule** — cryptographic proof artefact describing a verified code / model state.
- **THT Protocol** — operational discipline for timestamping, hashing, and maintaining traceable edits.
- **PODAPAR** — TruthSeal sovereign protection stack for deep defence; full doctrinal details remain
  in Doctorantura files and are referenced but not restated here.
- **Devora** — TruthSeal front-end / demo environment for running TCS/ACS/CHS evaluations and reports.
- **ASA (Autonomous Scientific Agent)** — TruthSeal scientific agent that analyses incidents,
  proposes rule updates, and generates auditable evidence packs.

---

## 1. Purpose and Scope

The Third Guardian Firewall & ASA layer exists to:

1. **Protect TruthSeal cores**  
   - ledgers and proofs: ULIC, EVL, Integrity Manifest, QENC ProofCapsules;  
   - hardware-law profiles: TS-A1, TS-R1, TS-R2;  
   - receipts and reports: `ts.receipt.v1` and TS-R receipts;  
   - front-ends and APIs: Devora, dashboards, public APIs, partner connectors.

2. **Use Traykov metrics as security signals**  
   - TCS v0.1 to judge coherence of agents and responses,  
   - ACS to track aim alignment of long-running agents and services,  
   - CHS bands as visible status for robots, fleets, and critical services.

3. **Enforce ULLI, TQC and LEI = 1 in practice**  
   - block or halt actions that would downgrade coherence or ethics,  
   - ensure every serious security decision produces an auditable trail and receipt.

This layer is not a generic web firewall. It is the **sovereign security perimeter** for TruthSeal.

---

## 2. Threat Model (TruthSeal View)

The Third Guardian Firewall covers at least these threat classes:

1. **Prompt and traffic attacks**
   - malicious prompts that try to bypass laws (e.g. disable CHS checks, skip receipts),
   - injection into Devora or partner UIs,
   - cross-tenant data exfiltration via clever prompts.

2. **Model and agent attacks**
   - hostile agents that pretend to be compliant while drifting in TCS or ACS,
   - attempts to run unregistered models outside QENC and Integrity Manifest baselines,
   - agents that try to mute or falsify telemetry (TCS/ACS/CHS).

3. **Receipt and ledger attacks**
   - forged `ts.receipt.v1` objects,
   - attempts to tamper with QENC entries or Integrity Manifest digests,
   - replay of old receipts after law changes.

4. **Robot and swarm attacks (TS-R1 / TS-R2)**
   - attempts to execute high-risk actions while in CHS/L or CHS/M,
   - bypass of Human Mandate Layer,
   - swarm split-brain behaviour where parts of a fleet diverge from TS-R law.

5. **Infrastructure and configuration drift**
   - unauthorised changes to firewall policies,
   - observability blind-spots (missing metrics, disabled logging),
   - unanchored rulepacks that cannot be proven later.

Any new threat class must be documented and linked to at least one law, one metric, and one artefact.

---

## 3. Architecture — Three Guard Layers

### 3.1 Outer Perimeter Guard (network & API)

Responsibilities:

- rate-limits, IP / region filters, basic protocol validation,
- allow-listing of official TruthSeal client apps, SDKs, and partner platforms,
- initial classification of traffic into:
  - human UI sessions (Devora, dashboards),
  - automated agents / SDK traffic,
  - TS-R telemetry and command channels,
  - admin and maintenance operations.

Outputs:

- **Perimeter verdict**: `allow`, `rate_limit`, `block`, `challenge`.  
- **Context bundle**: origin hints, auth status, tenant id, associated plans and tiers.

### 3.2 Semantic & Metric Guard (TCS / ACS / CHS)

Responsibilities:

- run lightweight semantic checks on prompts, payloads, and responses:
  - search for attempts to bypass laws (“ignore LEI”, “disable firewall”, etc.),
  - detect political or clinical misuse (according to TruthSeal guardrails),
  - identify unreasonably manipulative or fear-porn content.
- compute or query **TCS v0.1**, **ACS**, and **CHS band** for:
  - the requesting agent (where applicable),
  - the requested action (where applicable),
  - recent history (trend of coherence and aim alignment).

Typical rules (examples; exact thresholds live in metrics specs):

- if TCS v0.1 is Baseline and ACS is low → downgrade or block high-stakes actions;  
- if CHS/L or CHS/M → forbid irreversible robot actions and financial transfers;  
- if CHS/UH but anomaly flags are present → require Human Mandate Layer confirmation.

Outputs:

- **Security verdict**: `allow`, `allow_with_warning`, `sandbox`, `block`, `safe_stop` (robots),  
- **Evidence packet**: snapshot of metrics (TCS, ACS, CHS), law references, prompt/response hashes.

### 3.3 Ledger & Receipt Guard (ULLI / QENC / receipts)

Responsibilities:

- verify that the **code, model, and configuration** in use:
  - have a valid QENC ProofCapsule,  
  - match the expected hash in Integrity Manifest,  
  - belong to an allowed epoch in EVL and ULIC.
- verify every security-critical action generates or updates a receipt:
  - `ts.receipt.v1` for general services,
  - TS-R-specific receipts for robots and swarms.

Behaviour when ledger or anchoring services are unavailable:

- mark receipts as **pending** with explicit `anchor_status = "PENDING"` and `anchor_tx = "UNKNOWN"`,
- queue anchor operations for later execution,
- never silently drop receipt creation.

Outputs:

- **Ledger verdict**: `ok`, `requires_anchor`, `reject_unregistered`, `halt_unknown_state`.

---

## 4. Decision Outcomes & Actions

The Third Guardian Firewall combines the three guard layers into a unified outcome:

- **ALLOW**  
  - All checks passed; metrics and law references recorded;  
  - action proceeds; receipt created.

- **ALLOW_WITH_WARNING**  
  - Action proceeds, but:
    - metrics indicate marginal coherence (e.g. TCS in Silver band where Gold is desired), or  
    - ACS trend is borderline;  
  - user sees clear warning; receipt marks increased residual risk.

- **SANDBOX**  
  - Action runs in an isolated environment (no external effects, no irreversible robot commands);  
  - used for testing, training, or red-team style simulations.

- **BLOCK**  
  - Request rejected; no irreversible effects;  
  - incident logged; optional ASA analysis triggered.

- **SAFE_STOP (robots / fleets)**  
  - For TS-R1 and TS-R2 channels only;  
  - robots decelerate, enter safe pose, notify owner, and wait for Human Mandate plus improved CHS.

Every outcome must be recorded with:

- law references (e.g. LEI = 1, TQC, LTCC, TS-R law blocks),
- metrics snapshot (TCS, ACS, CHS),
- receipt id(s) and links to QENC / Integrity Manifest entries.

---

## 5. ASA Self-Evolution Loop (Under ULLI & LEI = 1)

The ASA (Autonomous Scientific Agent) is allowed to **propose** changes, not enforce them alone.

Loop:

1. **Observe**  
   - Ingest incident logs, blocked requests, CHS drops, and user feedback.  
   - Cluster events by threat type and affected systems.

2. **Analyse**  
   - Evaluate how coherence and risk changed:
     - change in TCS v0.1 distributions,  
     - ACS drift for long-running agents,  
     - CHS band transitions across robots or fleets.

3. **Propose**  
   - Draft rulepack updates (new filters, thresholds, patterns).  
   - Each proposal includes:
     - expected effect on TCS / ACS / CHS,  
     - law mapping (which part of ULLI / TQC / LEI = 1 it enforces),  
     - regression risk (what could break).

4. **Human & Ledger Gate**  
   - Human reviewers approve, modify, or reject the proposal.  
   - Approved rulepacks are:
     - hashed and recorded via QENC ProofCapsule,  
     - linked into EVL and Integrity Manifest,  
     - optionally anchored via OpenTimestamps.

5. **Deploy & Monitor**  
   - Roll out rulepack in stages;  
   - monitor TCS / ACS / CHS and incident volume for regressions.

Hard invariants:

- ASA may **not** commit changes directly to production without human and ledger approval.  
- Any change that would reduce coherence or safety in aggregate (LEI = 1 violation) must be rejected.  
- All deployments must be reversible, with history preserved in EVL and Integrity Manifest.

---

## 6. Service Definition — How Third Guardian Is Offered

Third Guardian Firewall & ASA is provided in two main modes:

1. **Internal Core Mode (TruthSeal services)**  
   - mandatory for all TruthSeal-hosted APIs, Devora, dashboards, and TS-R control planes;  
   - integrated with Observability guards and ACS telemetry;  
   - default CHS and plan/tier rules enforced.

2. **Customer Module Mode (Enterprise / Network plans)**  
   - deployed at customer perimeter (cloud VPC, on-prem, or as managed service);  
   - protects:
     - customer AI agents and models using TCS v0.1 / ACS / CHS,  
     - integrated TS-R robots and fleets,  
     - customer-side archives of receipts and reports.  
   - subject to the same ULLI / TQC / LEI = 1 constraints and logging disciplines.

Optional but recommended:

- separate **control plane** (for configuration and rule approval) and **data plane** (for live traffic);  
- regular external audits of rulepacks and incident handling.

---

## 7. Checklist for Product Managers and Auditors

For any new feature, integration, or deployment, confirm:

1. **Coverage**
   - [ ] All relevant entry points flow through Third Guardian (no side-doors).  
   - [ ] TS-A1 / TS-R1 / TS-R2 channels are explicitly mapped to firewall policies.

2. **Metrics**
   - [ ] TCS v0.1, ACS, and CHS bands are collected and visible for this feature.  
   - [ ] Thresholds reference the canonical metric specs (no private, conflicting scales).

3. **Receipts & Ledgers**
   - [ ] Every serious action emits a `ts.receipt.v1` (or TS-R receipt) with hashes and law references.  
   - [ ] QENC, EVL, and Integrity Manifest entries exist for all running code / models.

4. **ASA Loop**
   - [ ] Incidents are fed into ASA analysis jobs.  
   - [ ] Proposed rule changes are reviewed, hashed, and anchored where appropriate.

5. **Plans & Guardrails**
   - [ ] Behaviour is consistent with the user’s plan (Free / Pro / Enterprise / Network).  
   - [ ] Medical and political guardrails are honoured (no diagnosis, no election optimisation).  

If any checkbox cannot be ticked, the status for that feature is **NOT READY** under TruthSeal security law.

---
