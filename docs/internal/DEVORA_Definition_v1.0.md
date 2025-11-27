# DEVORA™ Definition – v1.0 (Internal)

Author: Dr. Nickolay Traykov (Prof. h.c.)
Project: TruthSeal™
File: docs/internal/DEVORA_Definition_v1.0.md
Status: Internal reference – not for public release

## 1. Canonical Definition

DEVORA™ is TruthSeal’s sovereign command center: the governance dashboard and control brain for high-risk artificial intelligence (AI) and emerging artificial general intelligence (AGI) systems, where telemetry, receipts, policies, and automations are managed in one place. DEVORA coordinates what is being governed, how it is being observed, and which actions are allowed, quarantined, or escalated.

DEVORA does not replace the hardware law (TS-A1) or the Integrity Manifest. It sits above them as the operator’s cockpit and memory.

## 2. Name Meaning (Acronym)

Internally, DEVORA is defined as:

- **Definition** – register each governed system: models, policies, hardware cores (for example, TS-A1 governance processing cores), and environments.
- **Extension** – connect new guards, workflows, external systems, and data streams without rewriting the core.
- **Volume** – monitor load, traffic, and risk exposure across many models, accelerators, and tenants at once.
- **Overview** – present a clear, real-time view of Aim Coherence Score (ACS), Law of Ethical Irreversibility (LEI = 1) gates, receipts, alerts, and drift.
- **Remember** – keep a history of runs, verdicts, and receipts for audits, incident reviews, and regulatory reports.
- **Automation** – run controlled playbooks that can pause, quarantine, reroute, or certify workloads, always leaving a verifiable receipt.

This acronym is for internal use. Public-facing documents may use “DEVORA™ Command Center” without expanding the letters.

## 3. Role in the TruthSeal Stack

DEVORA coordinates several layers:

- **Hardware law (TS-A1)** – the AEGIS TS-A1 hardware law enforces minimum non-negotiable rules in silicon for high-risk AI and AGI workloads, including receipts and veto lanes.
- **Integrity Manifest and receipts** – every critical run must produce a cryptographic receipt that can be checked against the Integrity Manifest and external timestamping.
- **Post-quantum cryptography (PQC)** – receipts and proofs are designed to be secured with post-quantum cryptography so that they remain verifiable in a future quantum environment.
- **Aim Coherence Score (ACS)** – DEVORA reads ACS and related observability signals to decide when to keep operating normally, when to raise alerts, and when to trigger gates.

DEVORA is not just a page or a single user interface. It is the control layer that knows which workloads exist, how they are governed, and what actions are allowed under LEI = 1.

## 4. DEVORA and Local Controllers

Files such as `demos/devora/DEVORA_App.html` implement a local DEVORA-style coherence gate controller. These views:

- show how ACS and LEI-based gating behave on a single system; and
- produce example receipts and decisions for demonstrations and tests.

These local controllers are **views into DEVORA’s role**, not the whole DEVORA system. The canonical definition in this document is the source of truth for what DEVORA means inside TruthSeal.

## 5. Usage Guidelines

- The first time DEVORA is mentioned in any internal document, use the canonical sentence from Section 1 or a direct paraphrase that preserves its meaning.
- In technical and partner-facing material, pair DEVORA with the broader stack: TS-A1 hardware law, Integrity Manifest, receipts, ACS, and PQC.
- Avoid describing DEVORA as “just a demo.” Use “DEVORA ACS controller” or “local DEVORA view” when referring to a single page or simulator.
