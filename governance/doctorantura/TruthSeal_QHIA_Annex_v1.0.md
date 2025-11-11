TruthSeal™ — Quantum Hardware Integrity Annex (QHIA) v1.0
Classification: INTERNAL — Doctorantura. NOT for public distribution; do not link from public indexes.
Navigation: Operational Index → ../docs/STATUS_Phases_Index_v1.0.md • Chronology → ../docs/TruthSeal_Project_Chronology_v1.0.md
Stamped_utc: 2025-11-11T00:00:00Z

Purpose
Bridge TruthSeal’s ethical law (LEI=1, TQC) to real quantum hardware. Formalize guard-rails so any computation that touches the ledger is provably coherent.

Background (project summary)
• Mandate: TruthSeal Protocol; DEVORA dashboard as the operator interface.  
• Critical challenge: noisy / unstable quantum hardware → we need verifiable integrity before we trust outputs.  
• Solution: QHIA with three mandatory protocols: CIS-L, LQIP, QRS.  
• Scope: INTERNAL annex to Doctorantura; feeds ACS/Guards and operator UX (DEVORA).

QHIA Protocols (canonical)
1) CIS-L — Computational Integrity Sub-Layer
   Goal: Prove the target computation executed without integrity loss before committing to ledger.
   Mechanism: “Quantum Echoes” (repeatability / non-demolition checks, deterministic replay where applicable).
   Evidence artifact (ledger): cis_l_proof.json (inputs, outputs, echo-check stats, pass=true|false).
   Policy gate: If pass=false → block commit; raise ACS alert.

2) LQIP — Logical Qubit Integrity Protocol
   Goal: Only accept results computed on error-corrected logical qubits (or certified logical equivalence on simulators).
   Required fields: logical_depth, code_family, estimated_logical_error_rate, calibration_window_utc.
   Evidence artifact: lqip_attest.json (attestation bundle signed by provider or simulator).

3) QRS — QEC Readiness Scale
   Goal: Transparently state what apps are safe at current hardware maturity.
   Levels:
     • L1 — Scientific demo only (no production autonomy)
     • L2 — Research workloads with human review
     • L3 — Bounded utility; read-only analytics; no external actuation
     • L4 — Mission-critical with guard rails; requires CIS-L pass + LQIP attestation
     • L5 — Sovereign-grade autonomy; requires continuous attestation + post-facto audits
   Evidence artifact: qrs_status.json (level, issuer, expiry_utc).

DEVORA Dashboard mapping
D — Definition → Show active QRS level as the top KPI.  
E — Extension → New data streams must present LQIP attestation before ingestion.  
V — Volume → Throttle/route by QRS level; deny writes when CIS-L fails.  
O — Overview → ACS panel surfaces CIS-L failure rate and latest qrs_status.json.  
R — Remember → Tag every ledger record with qrs_level and attestation hashes.  
A — Automation → Actions only fire after cis_l_proof.pass=true and level≥policy_min.

Next actions (v1.0)
A1. Produce schema stubs: cis_l_proof.json, lqip_attest.json, qrs_status.json (governance/guards/schemas/).  
A2. Wire into ACS: add checks and a red FAIL banner when any guard is missing or false.  
A3. DEVORA UX: add QRS Level pill, CIS-L pass/fail badge, and Attestation panel.  
A4. Policy: add “QHIA required” note to Defence Checklist v1.0.

Notes
• INTERNAL only. Reference from STATUS_Phases_Index_v1.0.md (ACS/Guards), not from public indexes.  
• When hardware proofs are unavailable, run simulator with deterministic seed and record rationale in cis_l_proof.json.
