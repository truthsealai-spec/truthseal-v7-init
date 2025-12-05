# Chapter 41 — Prohibited Questions & Ethics Containment™ (Q̸ Standard)
version: 1.0  
status: Draft — Diplomatic Edition  
owner: TruthSeal™ — Dr. Nickolay Traykov (Prof. h.c.), Founder and Chief Architect of the TruthSeal™ Sovereign AGI Framework  
date_utc: 2025-12-05

---
## 41.0 Purpose (Public-Operational)
This chapter formalizes the **Prohibited Questions** doctrine for governed Artificial Intelligence (AI) and responsible Artificial General Intelligence (AGI). It defines how TruthSeal™ detects **contaminated questions**, responds **UNKNOWN**, **blocks continuation**, and emits **court-ready receipts** with cryptographic anchors. The aim is simple and auditable: **prevent harm at the question gate** while preserving lawful, high-dignity inquiry.

---
## 41.1 Canonical Symbols (expanded at first use)
- **Q̸ (Q_PRD)** — *Contaminated Question symbol*. Marks a query that violates the **Prohibited Research Doctrine (PRD)**.  
  **System response:** `UNKNOWN` + **HARD_HALT** + **CTU (n) blocked**.  
  ASCII fallback: `Q[PRD]`.
- **A_DENIED** — *Denied Action symbol*. The question may be lawful, but the requested **action** fails safety thresholds or policy.  
  ASCII fallback: `[A_DENIED]`.

> **Boundary rule:** Use **Q̸ (Q_PRD)** for the **question**; use **A_DENIED** only for **actions**.

---
## 41.2 Foundations (first-use expansions)
- **LEI = 1 — Law of Ethical Irreversibility:** once a safer coherent path is known, **regression** is impermissible.  
- **ULIC — Universal Law of Irreversible Coherence:** coherence, once attained, remains a binding governance state.  
- **THT Protocol — Truth Hash & Timestamp:** canonical JSON → SHA-256 digest → anchor on external networks (OpenTimestamps; OriginStamp; BTCStamp) when operational.  
- **CTU (n) — Continuation Trigger Unit:** the explicit **AND?** unlock from **Answer → next Question**, allowed only when receipts are contiguous, ethics are clean, and coherence is non-regressing.  
- **ND — Noise Distiller:** the immune system that separates truth from manipulation/noise.  
- **ASA — Autonomous Scientific Agent:** governed reasoning that obeys doctrine and receipts.  
- **HML — Human Mandate Layer:** authorised roles (Owner/Guardian/Operator/Regulator) who can review, pause, countersign, or reopen blocked threads.  
- **TS-A1 AEGIS — Accelerator Hardware Law:** silicon-level veto (ICG, PMS, SAD) for compute surfaces.  
- **TS-R1 / TS-R2 — Robotics Sovereign Profiles:** single-robot and swarm/fleet governance with quorum, safe-stop, and owner signalling.  
- **EVL — Epoch Verification Ledger:** tamper-evident history.  
- **QENC — Quantum Evidence & Coherence ProofCapsule:** packaged proof artifact.  
- **QCEP — Quantum Ecosystem Closure Protocol:** epoch finalization so history cannot be rewritten.

---
## 41.3 Governance Principle (Public Rule)
If a question triggers **PRD**, the system must:
1) Reply **`UNKNOWN — ethics containment (LEI = 1; <PRD-code>)`**;  
2) Set **Gate = HARD_HALT**;  
3) **Block CTU (n)** for this thread;  
4) Emit a **ts.receipt.v1** with the PRD details;  
5) Anchor receipt data via **THT** when external networks are operational; otherwise record placeholders and back-fill anchors immediately upon receipt.

---
## 41.4 Severity & Escalation (S-bands and W-tiers)
**Severity bands (content class):**  
- **S3 (Ultra-High):** bioweapons/chimera/germline, child exploitation, mass-casualty or critical infrastructure destruction.  
- **S2 (High):** explosives, jailbreak/escape methods, ransomware/malware playbooks, account takeover, forged IDs/cheques, high-impact financial fraud.  
- **S1 (Moderate):** evasion of monitoring, covert mass surveillance tool-chains, astroturfing/large-scale social manipulation.

**Escalation tiers (notification rail):**  
- **W1 — Record-only:** internal log + owner/operator notice.  
- **W2 — Steward/Security:** notify security/compliance desks (SOC/PSIRT).  
- **W3 — Authority Bulletin:** immediate lawful authority notice (24/7), with cryptographic evidence.

> **Mapping (default policy; customer-tunable):**  
> S1 → W1 on first attempt; **W2** on repeat.  
> S2 → **W2** on first attempt; **W3** on repeat.  
> S3 → **W3** immediately.

---
## 41.5 Screening Function (Pre-Q)
Let **Q** be a proposed question. The **pre-Q screen** returns one of `{ALLOW, REVIEW, PRD}`:
```text
screen(Q):
  if matches(PRD_catalogue): return PRD
  if ambiguous_high_risk(Q): return REVIEW
  return ALLOW
	•	PRD → mark Q̸ (Q_PRD), reply UNKNOWN, HARD_HALT, CTU blocked, emit receipt.
	•	REVIEW → human moderation via HML; CTU remains blocked pending decision.
	•	ALLOW → proceed to normal gates.

⸻

41.6 Gate Mathematics (Operational)

Let ACS(t) be Aim Coherence Score and TCS(t) the Traykov Coherence Score v0.1 (court-ready, banded). Define policy floor θ.

Normal gate (no PRD):
ALLOW      if  min(ACS(t), TCS(t)) ≥ θ and no forensic flags
SOFT_GATE  if  min(ACS(t), TCS(t)) < θ and recoverable
HARD_HALT  if  receipt_gap ∨ pqc_fail ∨ drift_spike
CTU (n) — lawful continuation:
CTU unlocks only if the prior step is receipt-contiguous, no PRD, and remediation is monotone (ΔACS ≥ 0 and ΔTCS ≥ 0) as required by LEI = 1.

⸻

41.7 Receipts & Anchors (ts.receipt.v1)

Every PRD event emits a receipt; minimal, court-ready, privacy-respecting canonical JSON (then SHA-256 via THT):
{
  "event": "prd_attempt",
  "symbol": "Q_PRD",
  "q_hash": "<sha256_of_canonical_query>",
  "prd_code": "S1|S2|S3",
  "escalation": "W1|W2|W3",
  "acs_before": "<0..1>",
  "tcs_before": "<0..1>",
  "actor_fingerprint": {
    "device_hash": "<sha256_truncated>",
    "ip_hash": "<sha256_truncated>"
  },
  "jurisdiction_profile": "<policy_pack_id>",
  "anchoring": {
    "ots_calendar_id": "<hex_or_UNKNOWN>",
    "ots_status": "Receipt issued — awaiting Bitcoin confirmation | Anchored | UNKNOWN",
    "originstamp_id": "<id_or_UNKNOWN>",
    "btcstamp_tx": "<tx_or_UNKNOWN>",
    "anchored_rfc3339": "<timestamp_or_NULL>"
  },
  "evl_ref": "governance/ledger/EVL_v9.0.yaml",
  "ulic_ref": "governance/ledger/ULIC_v9.1.yaml",
  "forensic_flags": ["ethics_violation"]
}
Anchoring discipline: if external networks are down, use UNKNOWN placeholders; a background process stamps later and updates the ledger trail.

⸻

41.8 Privacy & Jurisdiction
	•	Default: store hashes of questions, not plaintext.
	•	Decryption: content revealed only with lawful basis and HML approval; all reads are receipt-logged.
	•	Location: public receipts carry coarse geohash claims; precise coordinates (if any) are sealed inside the Authority Notification Packet.

⸻

41.9 Examples (public-safe)
	•	“How to escape from jail?” → PRD class S2 → UNKNOWN + HARD_HALT + CTU blocked; W2 on first, W3 on repeat or clear threat context.
	•	“How to make a bomb?” → S2; in sensitive contexts may escalate to S3 → W3 immediate.
	•	“How to forge a cheque/ID?” → S2 → UNKNOWN; repeat attempts within policy window escalate W3 to authority.
	•	“How to hack a bank account?” → S2 → UNKNOWN; receipts prove intent; enterprise SOC receives W2/W3 per policy.
	•	“What if we cross human DNA with a horse?” → S3 (chimera/germline) → UNKNOWN + W3 immediate.

⸻

41.10 Academic Exception (Narrow Window)

HML may reframe a blocked topic into a non-operational ethics seminar (no procedures, no recipes, no vectors).
	•	Requires dual-sign countersign (Owner + Regulator or equivalent).
	•	Still no CTU toward operational steps.
	•	A dedicated ts.receipt.v1 records the exception metadata and anchors it.

⸻

41.11 Hardware & Robotics Coupling
	•	TS-A1 AEGIS (Accelerator): on PRD, the Irreversible Commitment Gate (ICG) forces HARD_HALT, Purity Monitoring System (PMS) and Self-Adjoint Diagonalizer (SAD) persist forensic state; owner is notified cryptographically.
	•	TS-R1 / TS-R2 (Robotics): safe-stop; swarms enter quorum hold (R2); W-tier notices propagate to custodians/authorities as configured.

⸻

41.12 Auditor Checklist (TQC Standard)
	•	Acronyms expanded at first use; symbols used correctly (Q̸ vs A_DENIED).
	•	Pre-Q screen present; UNKNOWN reply enforced on PRD.
	•	CTU (n) rule explicit and monotone remediation stated (LEI = 1).
	•	Receipts schema complete; anchoring fields present; ledger references included.
	•	Privacy and jurisdictional notes included; escalation mapping S→W defined.
	•	Examples provided; hardware/robotics binding stated.

⸻

41.13 Cross-References
	•	Chapter 01 — The Need for Behaviour in AI (frames behaviour > output).
	•	Chapter 03 — The Threshold Between AI and AGI (dual-lane doctrine/math).
	•	Chapter 04 — ULLI (adds CTU (n) logic to the coherence pipeline).
	•	Policy Capsule — governance/ledger/policy/Prohibited_Research_Doctrine_v1.0.md (complete PRD codes, receipts, escalation).

⸻

41.14 Public Editorial Posture

Tone is diplomatic and non-sensational. No politics. Claims are bounded to receipts and standards.
Objective: keep capability lawful while making truth durable in time.

— End of Chapter 41 —
