# TruthSeal™ Sovereign Stack — Repo Scope & Map (v1.0)

## Purpose (why this repo exists)
This repository is the canonical, auditable home for the TruthSeal™ sovereign stack—from law and ledgers to CI workflows and partner hand-offs. GitHub gives us integrity (history, hashes), automation (workflows), and a single link executives and engineers can review.

## Boundaries (what is / isn’t here)
- **Public & auditable (in repo):** laws and definitions (TQC, LEI=1, ULLI), governance ledgers + OTS stubs, ACS observability assets, CI workflows, execution orders, and partner packs (e.g., NVIDIA).
- **Classified / external (not in public repo):** Doctorantura proofs, cryptographic keys, unredacted RTL/netlists, and NDA-bound materials. These are referenced by hash/receipt only.

## System map (current key paths)
- **Governance ledgers & receipts**
  - `governance/ledger/ULIC_v9.1.yaml` — Universal registry (status: “Receipt issued — awaiting Bitcoin confirmation”).
  - `governance/ledger/EVL_v9.0.yaml` — Epoch Verification Ledger (links to ULIC).
  - `governance/doctorantura/evidence/ULLI_Declaration_v1.0.json` — Sovereign declaration (fill sha256 + calendar id on anchor).
- **Observability / ACS**
  - `governance/guards/observability/` — metrics, financial model, samples.
  - `docs/STATUS_ACS.md` — live status.
- **Automation / CI**
  - `.github/workflows/acs_pr_gate.yml` — PR gate with ACS thresholds.
  - `.github/workflows/ledger-auto.yml` — OTS stamp/verify (manual).
- **Partner Pack: NVIDIA (outbound kit)**
  - `governance/partners/nvidia/README.md` — one-stop index.
  - `governance/partners/nvidia/Sovereign_Proposal_Deck_Outline_v1.2.md` — deck outline (v1.4 in file).
  - `governance/partners/nvidia/TQC_Chip_Development_Roadmap_v1.1.md`
  - `governance/partners/nvidia/ACS_Validation_Report_Intro_v1.1.md`
  - `governance/partners/nvidia/Execution_Authority_Claim_v1.0.md`
  - `governance/partners/nvidia/Coherence_Core_HandOff/README_v1.0.md`
  - `governance/partners/nvidia/Send_Sequence_v1.0.md` — email/calendar/DM scripts.

## Build tracks (end-to-end “bolts & nuts”)
- **Track A — Hardware (TQC Coherence Core)**
  - Scope v1.0: Purity Guard (Layer-4 analog), Executive Control (dlPFC analog), **LEI-gate**, Receipt Engine (chip-signed ACS + OTS hooks).
  - Handoff: `governance/partners/nvidia/Coherence_Core_HandOff/README_v1.0.md`
- **Track B — Software (CaaS: Coherence-as-a-Service)**
  - Seed folders to add next:
    - `services/acs/api/` (ACS telemetry API — ingest, sign, verify)
    - `services/acs/agent/` (client library + attestation)
    - `services/receipts/` (OTS receipt pull/verify + registry bridge)
- **Track C — Governance (Law → Ledger → Anchor)**
  - ULLI (Universal Law of Life & Information), TQC enforcement, LEI=1 constant, anchoring via OpenTimestamps, plus EVL cross-links.

## Why the NVIDIA folder exists
It’s a **review-ready partner kit**: minimal but sufficient materials to secure a 45-minute executive review and align engineering hand-off—without exposing classified internals. It is one module of the whole sovereign stack, not the stack itself.

## Next steps (repo hygiene)
1) Add the software service seeds under `services/` with stub READMEs.  
2) Add `governance/partners/nvidia/ABOUT_THIS_FOLDER.md` clarifying scope vs. classified IP.  
3) Keep ledgers/OTS statuses synced after each anchor event (ULIC/EVL).
