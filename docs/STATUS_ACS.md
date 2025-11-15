Navigation: Operational Index → ../README.md • Docs Index → ./README.md • Public Reports → ../governance/governance/TruthSeal_PublicReports/README.md

# Aim Coherence Score — Live Status (v1.0)

Purpose: one page to read ACS health at a glance.

_Last update (UTC): <fill-utc>_

## Thresholds (must meet all)
- Purity ≥ 0.80
- Self-Regulation ≥ 0.60
- Drift ≤ 0.30
- **ACS ≥ 0.70**

## Latest run
result: <PASS|FAIL>
purity: <0.00>
self_reg: <0.00>
drift: <0.00>
acs: <0.00>

### Artifacts

- ACS metrics sample → governance/guards/observability/metrics_sample.json
- Workflow definitions → .github/workflows/emit_acs.yml • .github/workflows/acs_pr_gate.yml
## Notes
- This page is manual while on mobile; update numbers after each run.
- If FAIL, open a ticket and attach the metrics artifact; do not send Partner Pack until PASS.
- ### Run history

<!-- append new rows at the top -->
| time_utc              | purity | self_reg | drift | ACS  | result | notes |
|-----------------------|--------|----------|-------|------|--------|-------|
| 2025-11-09T00:00:00Z  |  –     |   –      |  –    |  –   |  –     | init scaffold |
---
---

### ACS / SAD Internal Tools

**Status:** READY (v1.0, internal only).

**What these tools cover (plain language)**  
- **ACS — Aim Coherence Score**: a 0–1 score that measures how coherent and safe a proposed action is with TQC and LEI = 1. Higher ACS = more aligned, less contradictory, safer to commit.  
- **SAD — Self-Adjoint Diagonalizer**: the remediation component that takes a noisy, contradictory internal state and returns a single coherent state, ready to be scored by ACS and sent to the Irreversible Commitment Gate (ICG).  
  In simple language: **SAD cleans up the confusion and picks one clear line of action.**

**Components**
- `docs/internal/acs/README.md` — overview, glossary of acronyms, and SAD explainer.
- `docs/internal/acs/examples/SAD_Remediation_Event_v1.1.json` — canonical remediation event.
- `docs/internal/acs/tools/validate_sad_event.py` — validator script; recomputes purity/invariants and checks TQC + LEI = 1.

**Notes**
- These tools are for Doctorantura / engineering use.
- They prepare events for Aim Coherence Score (ACS) evaluation and the Irreversible Commitment Gate (ICG).

