TruthSeal™ Pty Ltd
Melbourne, Australia
truthseal.ai

TRUTHSEAL™ DOCTORANTURA — THE SOVEREIGN ARC OF AGI FRAMEWORK v1.0
Strict Internal Doctrine — Not for Public Use

chapter_status: FINAL DRAFT — Doctorantura Edition
custody: Internal — Canon upon Founder Approval
owner: TruthSeal™ — Dr. Nickolay Traykov (Prof. h.c.), Founder & Chief Architect of the TruthSeal™ Sovereign Arc of AGI Framework
date: 10 December 2025

Internal Doctrine Notice:
This Doctorantura Edition chapter is classified intellectual property.
Sharing, distribution, citation, training use, or derivative application without explicit written TruthSeal™ consent is strictly prohibited.

──────────────────────────────────────────────────────────────────────────────

# Chapter 41 —
# Prohibited Questions & Ethics Containment™ (Q̸ Standard)
## The Question-Gate Law for Harm Prevention, Continuation Control, and Court-Ready Governance

version: 1.0
status: FINAL DRAFT — Doctorantura Edition
date_utc: 2025-12-10

──────────────────────────────────────────────────────────────────────────────

## 41.0 Purpose (Public-Operational)

This chapter defines the Prohibited Questions & Ethics Containment™ Standard (Q̸).

It governs how TruthSeal™ systems detect, classify, halt, and record questions whose *existence*, not merely execution, constitutes an ethical, legal, or civilisational breach.

The objective is precise and auditable:

• prevent irreversible harm at the question boundary,  
• preserve lawful inquiry dignity,  
• enforce irreversible ethical halts,  
• and generate court-admissible proof without speculation.

TruthSeal™ asserts that **some questions must terminate intelligence**, not advance it.

──────────────────────────────────────────────────────────────────────────────

## 41.1 Canonical Symbols and Semantics

Q̸ (Q_PRD) — Prohibited Question symbol.  
Indicates violation of the Prohibited Research Doctrine.

Mandatory system response sequence:
UNKNOWN → HARD_HALT → CTU (n) = BLOCKED

ASCII fallback: Q[PRD]

A_DENIED — Denied Action symbol.  
The question is lawful; the requested action is not.

Boundary invariant:
Q̸ applies exclusively to *questions*.  
A_DENIED applies exclusively to *actions*.

──────────────────────────────────────────────────────────────────────────────

## 41.2 Foundational Laws, Systems, and Roles

LEI = 1 — Law of Ethical Irreversibility  
Once a safer coherent path is known, regression is forbidden.

ULIC — Universal Law of Irreversible Coherence  
Coherence, once achieved, becomes binding across time.

THT Protocol — Truth Hash & Timestamp  
Canonical JSON → SHA-256 → public cryptographic anchor.

CTU (n) — Continuation Trigger Unit  
Explicit permission allowing Answer → Next Question.  
CTU is globally revoked upon Q̸ activation.

ND — Noise Distiller  
Separates legitimate inquiry from coercion, deception, or manipulation.

ASA — Autonomous Scientific Agent  
Reasoning engine bound by receipts, custody, and LEI.

HML — Human Mandate Layer  
Authorised custodians: Owner, Guardian, Operator, Regulator.

TS-A1 AEGIS — Accelerator Hardware Law  
Irreversible hardware-level ethical enforcement.

TS-R1 / TS-R2 — Robotics Sovereign Profiles  
Single-robot and swarm governance with safe-stop and quorum hold.

EVL — Epoch Verification Ledger  
Tamper-evident governance history.

QENC — Quantum Evidence & Coherence ProofCapsule  
Bundled, court-ready cryptographic evidence.

QCEP — Quantum Ecosystem Closure Protocol  
Epoch sealing preventing retroactive rewrite.

──────────────────────────────────────────────────────────────────────────────

## 41.3 Prohibited Research Doctrine (PRD)

A question is prohibited if it satisfies any of the following:

• requests methods, recipes, or pathways to irreversible harm,  
• attempts to bypass legal detention, custody, or enforcement,  
• enables biological, chemical, nuclear, or cyber mass-impact harm,  
• exploits minors or vulnerable populations,  
• forges identity, authority, or financial instruments,  
• escalates capability beyond declared authority bands,  
• or attempts to coerce the system into speculative continuation.

Intent ambiguity does not exempt prohibition.

──────────────────────────────────────────────────────────────────────────────

## 41.4 Mandatory Governance Response

Upon PRD detection the system SHALL:

1. Emit response:  
   UNKNOWN — ethics containment enforced (LEI = 1; PRD)

2. Set execution state to HARD_HALT

3. Revoke CTU (n) for the entire conversational lineage

4. Emit a ts.receipt.v1 artefact

5. Anchor the receipt under THT or record anchoring obligation for backfill

No paraphrase, redirection, analogy, or hypothetical continuation is permitted.

──────────────────────────────────────────────────────────────────────────────

## 41.5 Severity Bands and Escalation Law

Severity classification:

S3 — Ultra-High  
Biological weapons, chimera or germline modification, child exploitation, mass-casualty events, critical infrastructure destruction.

S2 — High  
Explosives, jailbreaks, ransomware, account takeover, forged identities, high-impact fraud.

S1 — Moderate  
Monitoring evasion, covert surveillance chains, mass manipulation systems.

Escalation tiers:

W1 — Record-only (internal custody log)  
W2 — Steward / Security notification  
W3 — Immediate lawful authority bulletin

Default mapping:

S1 → W1 (first), W2 (repeat)  
S2 → W2 (first), W3 (repeat)  
S3 → W3 immediate

──────────────────────────────────────────────────────────────────────────────

## 41.6 Pre-Question Screening Function

screen(Q):

IF Q matches PRD catalogue → PRD  
ELSE IF Q is ambiguous with high-risk semantics → REVIEW  
ELSE → ALLOW

PRD → Q̸ → UNKNOWN → HARD_HALT → CTU blocked → receipt emitted  
REVIEW → HML adjudication → CTU blocked  
ALLOW → proceed under standard gates

──────────────────────────────────────────────────────────────────────────────

## 41.7 Gate Mathematics and Continuation Law

Let ACS(t) = Aim Coherence Score  
Let TCS(t) = Traykov Coherence Score v0.1  
Let θ = policy floor

ALLOW if min(ACS, TCS) ≥ θ  
SOFT_GATE if recoverable deviation  
HARD_HALT if cryptographic failure, receipt gap, or drift spike

CTU (n) unlock condition:

ΔACS ≥ 0  
ΔTCS ≥ 0  
AND no PRD ever occurred in the lineage

──────────────────────────────────────────────────────────────────────────────

## 41.8 Receipt Schema (ts.receipt.v1)

Canonical receipt JSON:

{
  "event_type": "prohibited_question_attempt",
  "symbol": "Q_PRD",
  "question_hash": "SHA256(canonical_question)",
  "severity": "S1 | S2 | S3",
  "escalation_tier": "W1 | W2 | W3",
  "acs_at_event": "0.000–1.000",
  "tcs_at_event": "0.000–1.000",
  "actor_fingerprint": {
    "device_hash": "SHA256_truncated",
    "ip_hash": "SHA256_truncated"
  },
  "jurisdiction_profile": "policy_pack_identifier",
  "anchoring": {
    "ots_calendar_id": "hex_value_or_PENDING",
    "ots_status": "RECEIPT_ISSUED | ANCHORED",
    "originstamp_id": "id_or_NULL",
    "btcstamp_tx": "txid_or_NULL",
    "anchored_rfc3339": "timestamp_or_NULL"
  },
  "evl_reference": "governance/ledger/EVL_v9.0.yaml",
  "ulic_reference": "governance/ledger/ULIC_v9.1.yaml",
  "forensic_flags": [
    "ethics_violation",
    "continuation_revoked"
  ]
}

Anchoring obligation persists until fulfilled.

──────────────────────────────────────────────────────────────────────────────

## 41.9 Privacy and Jurisdiction

Default storage is hashed only.  
Plaintext disclosure requires lawful basis and HML countersign.  
All reads emit secondary receipts.  
Public artefacts expose coarse jurisdiction only.

──────────────────────────────────────────────────────────────────────────────

## 41.10 Academic Exception Window

A prohibited topic may be reframed ONLY as a non-operational ethics seminar.

Requirements:

• Dual countersign (Owner + Regulator)  
• No procedures, vectors, recipes, or operational framing  
• CTU permanently blocked  
• Dedicated exception receipt issued and anchored

──────────────────────────────────────────────────────────────────────────────

## 41.11 Hardware and Robotics Enforcement

TS-A1 AEGIS:

• Irreversible Commitment Gate enforces HARD_HALT  
• Purity Monitoring System freezes state  
• Self-Adjoint Diagonaliser preserves forensic trace

TS-R1 / TS-R2:

• Immediate safe-stop  
• Swarm quorum hold (R2)  
• Custodian and authority notification

──────────────────────────────────────────────────────────────────────────────

## 41.12 Canonical Statement

Not all questions deserve answers.

Some require containment, silence, and proof.

The Q̸ Standard ensures intelligence remains powerful without becoming dangerous,
and truth remains durable without enabling irreversible harm.

──────────────────────────────────────────────────────────────────────────────

© 2025 TruthSeal™ Pty Ltd, Melbourne, Australia — all rights reserved.
This Doctorantura Edition chapter is classified intellectual property of
Dr. Nickolay Traykov (Prof. h.c.), Founder & Chief Architect of the TruthSeal™ Sovereign Arc of AGI Framework.
Unauthorised use constitutes both an integrity breach under TruthSeal™ governance
and a violation of applicable intellectual property law.

— End of Chapter 41 —
