TruthSeal™ Pty Ltd · Melbourne, Australia · truthseal.ai · 8 December 2025
TRUTHSEAL™ SOVEREIGN COMPENDIUM · DOCTORANTURA EDITION v1.0

CHAPTER 42 — SCORING PRIMITIVES FOR THE METAMODULE ENGINE™
STS™ · SCS™ · MCS™ (NON-COMPENSATORY TRIAD)

⸻

42.1 Definition
This chapter defines the scoring primitives that quantify the integrity and system-state coherence of TruthSeal™ metamodule snapshots. These primitives are designed to be readable by first-time readers and operationally enforceable by the stack.

The triad is:
	•	STS™ — Source Trust Score™
	•	SCS™ — System Coherence Score™
	•	MCS™ — Metamodule Coherence Score™

These scores operate on the B-VSS™ (Bounded, Versioned System State) and produce a disciplined, receipt-compatible measurement basis for governance actions.

⸻

42.2 Why It Exists
A sovereign system cannot rely on narrative trust. It requires measurable, repeatable, auditable scoring that:
	•	identifies weak links early,
	•	prohibits compensatory masking of failures,
	•	binds corrective action to receipts and ledgers.

This triad exists to ensure that TruthSeal™ remains a system of measured integrity, not stylistic confidence.

⸻

42.3 Position in the Stack
The scoring primitives sit inside the metamodule governance loop and interact with:
	•	HML™ (Human Mandate Layer™) for authority and override legitimacy,
	•	TGF™ (Third Guardian Firewall™) for veto and safe-stop pathways,
	•	EVL™ (Epoch Verification Ledger™) for continuity of scored states,
	•	THT Protocol™ (Truth Handling & Timestamping Protocol™) for sealing and anchoring.

They are designed to remain fully compatible with the established core metrics:
	•	TCS™ (Traykov Coherence Score™) — court-grade coherence metric,
	•	ACS™ (Aim Coherence Score™) — trajectory and alignment metric,
	•	CHS™ (Coherence Health Score™) — operational health banding.

This chapter does not redefine TCS™ or ACS™.

⸻

42.4 STS™ — Source Trust Score™
STS™ measures ingestion integrity of B-VSS inputs at the point of entry. It evaluates whether the source is trustworthy enough to be allowed into sovereign processing.

STS™ evaluates (minimum set):
	•	Source Integrity — canonical origin trust and audit history.
	•	Temporal Integrity — recency of evidence relative to the active epoch.
	•	Signature Integrity — cryptographic authenticity and non-repudiation receipts.
	•	Corpus Correlation — consistency against the ledger-aligned baseline corpus.
	•	Metadata Integrity — completeness and format compliance.

Weighting:
Weights may be used for reporting, but are initial defaults and may be tuned per domain under HML™ authority.

Sovereign rule:
STS™ is informative, but cannot override a min-gate violation in any critical factor.

⸻

42.5 SCS™ — System Coherence Score™
SCS™ measures architectural and policy-state coherence of the active B-VSS against the deployed TruthSeal™ operating posture.

It evaluates whether the system-state is aligned with the mandated governance environment.

SCS™ evaluates (minimum set):
	•	Policy Compliance — adherence to active HML™ policies and validation contracts.
	•	Environmental Congruence — alignment with mandated security posture baselines.
	•	Control Integrity — successful execution and auditability of required controls.
	•	Sequencing Integrity — chronological validity within EVL™ continuity.

Acronym hygiene note:
SCS™ is intentionally named to avoid collision with ACS™ (Aim Coherence Score™).

⸻

42.6 MCS™ — Metamodule Coherence Score™
MCS™ is a composite reporting score that aggregates STS™ and SCS™ into a single metamodule snapshot indicator.

Purpose of MCS™:
	•	provide a readable summary for oversight dashboards,
	•	support trend analysis across epochs,
	•	feed higher-level governance summaries.

Non-authoritative nature:
MCS™ is not the pass/fail determinant when integrity is at stake. It is an aggregate signal that must remain subordinate to min-gate enforcement.

⸻

42.7 Non-Compensatory Coherence (Min-Gate Rule)
TruthSeal™ enforces non-compensatory integrity. This means:
A strong overall score must never conceal a critical weakness.

Minimum Gate Thresholds are defined as:
	•	T_min — the minimum allowable integrity threshold per critical factor.
	•	I_i — any scored integrity factor within STS™ or SCS™.

Operational rule:
If any critical I_i < T_min, the metamodule declares a hard integrity breach condition regardless of MCS™ magnitude.

Sovereign principle:
The authority of the whole is governed by the weakest critical link.

⸻

42.8 Consequence Tier (CT) Assignment
To preserve the doctrinal separation between health/maturity and consequence severity, TruthSeal™ assigns consequences using a distinct scale:
	•	CT-1 (Low) — calibration-level remediation.
	•	CT-2 (Medium) — soft correction.
	•	CT-3 (High) — hard correction with mandatory human review.
	•	CT-4 (Critical) — quarantine / safe-stop mandate.

CT is derived from min-gate severity, not from CHS™.
CT may trigger CHS down-banding as an outcome, but it is not defined by CHS.

⸻

42.9 Interaction with CHS™ and Core Metrics
CHS™ (Coherence Health Score™) remains the operational health and maturity banding system:
	•	CHS/L — Low
	•	CHS/M — Medium
	•	CHS/H — High
	•	CHS/UH — Ultra High

CHS/UH stands for Ultra High Coherence Mode.

Rules of interaction:
	•	A CT-4 outcome triggers TGF™ veto and forces restrictive operational posture.
	•	CHS may be down-banded after a CT breach to prevent unsafe execution.
	•	TCS™ and ACS™ remain authoritative at their respective scopes and are not altered by this chapter.

⸻

42.10 Receipts and Ledger Binding
When a scoring event occurs, the metamodule must emit receipts consistent with THT and EVL continuity.
Each scored snapshot must be traceable to:
	•	B-VSS identifier,
	•	STS™ component readings,
	•	SCS™ component readings,
	•	MCS™ composite reading,
	•	CT assignment (if any),
	•	CHS impact (if triggered),
	•	HML authority context (when overrides exist).

This ensures auditability without narrative dependence.

⸻

42.11 Canonical Statement
The scoring primitives of TruthSeal™ — STS™, SCS™, and MCS™ — define the measurable integrity and system-state coherence of metamodule snapshots.
They are non-compensatory, receipt-bound, and ledger-continuous.
They exist to ensure that no system can claim sovereign integrity unless it can prove it at the level of its weakest critical link.
TRUTHSEAL™ SOVEREIGN COMPENDIUM · DOCTORANTURA EDITION v1.0
TruthSeal™ Pty Ltd · Melbourne, Australia · truthseal.ai
8 December 2025

Dr. Nickolay Traykov (Prof. h.c.)
Founder & Sovereign Architect
TruthSeal™ Pty Ltd


— End of Chapter 42 —
