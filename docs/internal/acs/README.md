# TruthSeal™ ACS / SAD Internal Tools

This folder contains internal tools for TruthSeal’s **Architectural Coherence Specification (ACS)** stack, focused on the **Self-Adjoint Diagonalizer (SAD)** remediation flow.

These tools are **internal only** (Doctorantura / engineering use). They demonstrate how a single remediation event is checked against the Traykov Law of Quantum Coherence and **LEI = 1 (Law of Ethical Irreversibility)**.

---

## Files in this module

- `examples/SAD_Remediation_Event_v1.1.*`  
  Canonical SAD remediation event example. The file uses JSON structure with:

  - `pre_state` — Bloch vector, eigenvalues, and purity before remediation.  
  - `selection` — Rule used to pick the eigenstate (e.g. `argmax_eigenvalue`).  
  - `post_state` — Remediated density matrix `rho` and invariants.  
  - `tqc_enforcement` — Checks for  
    - `Tr(rho^2) == 1` (purity)  
    - `d(rho)/dt == 0` at commit (temporal stability)  
  - `lei_enforcement` — Handles the **Irreversible Commitment Hash (ICH)**:
    - `pqc_hash` — post-quantum hash of the event payload  
    - `ich` — final non-unitary irreversibility proof
  - `metadata` — `commitment_id`, `timestamp_epoch`, `agent_signature`, `entanglement_refs`, etc.

  > Note: In your repo the file extension may be `.json` or `.js`. Use the actual extension when running the validator.

- `tools/validate_sad_event.py`  
  TruthSeal™ SAD Remediation Event Validator.

  Responsibilities:

  1. **JSON load & schema check**
     - Loads the event from disk.
     - If the `jsonschema` package is installed, validates the instance against the v1.1 schema.

  2. **Invariant recomputation**
     - Rebuilds the `2×2` density matrix from `post_state["rho"]`.
     - Recomputes:
       - Trace
       - Purity `Tr(rho^2)`
       - Hermiticity
       - Positive semidefiniteness

  3. **TQC / LEI checks**
     - Confirms purity is `≈ 1.0` within tolerance.
     - Confirms temporal stability at commit.
     - Reports any failures as explicit error messages.

---

## Quick start (local run)

From the repo root:

```bash
python3 docs/internal/acs/tools/validate_sad_event.py \
  docs/internal/acs/examples/SAD_Remediation_Event_v1.1.json
