# TruthSeal™ ACS / SAD Internal Tools

This folder contains internal tools for TruthSeal’s **Aim Coherence Score (ACS)** stack, focused on the **Self-Adjoint Diagonalizer (SAD)** remediation flow.

These tools are **internal only** (Doctorantura / engineering use). They demonstrate how a single remediation event is checked against the Traykov Law of Quantum Coherence (TQC) and **LEI = 1 (Law of Ethical Irreversibility)**.

---

## What Does SAD Stand For?

**SAD = Self-Adjoint Diagonalizer.**

It is the remediation component that takes a noisy, contradictory internal state and returns a **single coherent state** that is ready to be evaluated by Aim Coherence Score (ACS) and then passed to the Irreversible Commitment Gate (ICG).

In simple language: **SAD cleans up the confusion and picks one clear line of action.**

---

## Glossary of Acronyms

- **ACS — Aim Coherence Score**  
  A 0–1 score that measures how coherent a proposed action or decision is with TQC and LEI = 1. A higher ACS means the action is more aligned, less contradictory, and safer to commit.

- **SAD — Self-Adjoint Diagonalizer**  
  The remediation step that takes a **mixed state** (internally conflicted) and collapses it to a **pure state** (internally consistent) using eigenvalue decomposition.

- **PMS — Purity Monitoring System**  
  The checker that detects when the internal state is mixed. If purity is below 1 (Tr(ρ²) < 1), PMS blocks commitment and triggers SAD.

- **ICG — Irreversible Commitment Gate**  
  The gate that only accepts coherent states (Tr(ρ²) = 1, stable at commit time) and attaches an **Irreversible Commitment Hash (ICH)** so the action becomes ledger-grade and non-reversible.

- **TQC — Traykov Law of Quantum Coherence**  
  The coherence law that requires purity and temporal stability for admissible decisions.

- **LEI — Law of Ethical Irreversibility (LEI = 1)**  
  Once a coherent decision is committed with a receipt, it is treated as ethically and operationally irreversible. Incoherent decisions must never pass the gate.

---

## 1. Initial State: The Mixed State ρ

**What it is**

- The initial internal condition is represented by a **density matrix** \( \rho \), built from the **Bloch vector** \( \mathbf{r} = (r_x, r_y, r_z) \) that comes from the inputs `rx`, `ry`, and `rz`.
- Mathematically, when \( \text{Tr}(\rho^2) < 1 \), the state is **mixed**.

**What it means (conceptual)**

- In TruthSeal / AGI terms, a mixed state is an **internally contradictory or uncertain system**.
- The AI is holding multiple incompatible possibilities, conflicting data points, or unverified claims at once.
- This is a higher-entropy, noisy condition: the system has not yet decided which reality it will actually commit to.

**Special case**

- If \( \mathbf{r} = 0 \) (i.e., `rx = ry = rz = 0`), we are at the **maximally mixed** state:
  - \( \rho = I / 2 \)  
  - This is the most uncertain state possible — maximum internal ambiguity.

---

## 2. Remediation: Eigenvalue Decomposition

**What it is**

- SAD takes the mixed state \( \rho \) and performs an **eigenvalue decomposition**.
- This decomposes \( \rho \) into its fundamental components: the **pure eigenstates** and their **probabilities**.

Concretely:

- There are two pure candidate states, \( |\psi_1\rangle \) and \( |\psi_2\rangle \).
- The decomposition gives two eigenvalues (probabilities):
  - \( \lambda_1 \) — probability of the most likely coherent outcome \( |\psi_1\rangle \).
  - \( \lambda_2 \) — probability of the less likely coherent outcome \( |\psi_2\rangle \).

**What it means**

- The mixed state is understood as a **mixture of pure possibilities**.
- The system is not “mysterious”: it is a weighted combination of a small number of clean, understandable options.

---

## 3. Final Action: SAD Collapse to ρ_final

**What it is**

- The SAD stage then performs a **deterministic collapse**:
  - It selects the eigenstate with the **highest probability**.
  - In TruthSeal, this is the “TruthSeal rule”: always pick the most coherent, most supported state.

Formally:

- Choose \( |\psi_1\rangle \) corresponding to \( \lambda_1 \) (where \( \lambda_1 \ge \lambda_2 \)).
- Construct the final density matrix:
  - \( \rho_{\text{final}} = |\psi_1\rangle \langle \psi_1| \)
  - This satisfies \( \text{Tr}(\rho_{\text{final}}^2) = 1 \) — **pure state**.

**What it means in AGI context**

- The system resolves internal conflict and **commits to a single coherent plan or statement**.
- No decision is allowed to pass to the **Irreversible Commitment Gate (ICG)** while the state is still mixed.
- Only once SAD has produced \( \rho_{\text{final}} \) with:
  - \( \text{Tr}(\rho^2) = 1 \), and
  - Acceptable temporal stability at commit,

  can the ICG attach an **Irreversible Commitment Hash (ICH)** and move the decision into a ledger-grade, irreversible action.

---

## 4. Files in This Module

- `examples/SAD_Remediation_Event_v1.1.*`  
  Canonical SAD remediation event example. The file uses JSON structure with:

  - `pre_state` — Bloch vector, eigenvalues, and purity before remediation.  
  - `selection` — Rule used to pick the eigenstate (e.g. `argmax_eigenvalue`).  
  - `post_state` — Remediated density matrix `rho` and invariants.  
  - `tqc_enforcement` — Checks for  
    - `Tr(rho^2) == 1` (purity)  
    - `d(rho)/dt == 0` at commit (temporal stability).  
  - `lei_enforcement` — Handles the **Irreversible Commitment Hash (ICH)**:
    - `pqc_hash` — post-quantum hash of the event payload.  
    - `ich` — final non-unitary irreversibility proof.  
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

## 5. Quick Start (Local Run)

From the repo root:

```bash
python3 truthseal-v7-init/docs/internal/acs/tools/validate_sad_event.py \
  truthseal-v7-init/docs/internal/acs/examples/SAD_Remediation_Event_v1.1.json
