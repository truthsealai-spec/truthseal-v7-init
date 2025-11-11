# TruthSeal™ Sovereign Stack — Repo Scope & Map (v1.0)

## Purpose (why this repo exists)
This repository is the canonical, auditable home for the TruthSeal™ sovereign stack—covering laws and definitions (TQC, LEI=1, ULLI), governance ledgers with OTS stubs, ACS observability assets, CI workflows, execution orders, and partner hand-offs. GitHub provides integrity (history, hashes), automation via CI workflows, and a single link executives and engineers can review.

## Boundaries (what is / isn’t here)
- **Public & auditable (in repo):** laws/definitions (TQC, LEI=1, ULLI), governance ledgers + OTS placeholders, ACS observability assets, CI workflows, execution orders, and partner packs (e.g., NVIDIA).
- **Classified / external (not in public repo):** Doctorantura proofs, cryptographic keys, unredacted RTL/netlists, and NDA-bound materials. These are referenced here **by hash/receipt only**.

## Directory map
## Receipts & anchoring discipline
- **OpenTimestamps (Bitcoin):** keep `ots_calendar_id` in each ledger; when anchored, append TX id and UTC time.
- **Hash discipline:** SHA-256 every governed artifact; cross-reference in EVL; surface live status in `docs/Anchoring_Status_v9.1.md`.
- **Public vs classified:** NDA-bound artifacts (e.g., unredacted RTL) are *not stored* here; reference by SHA-256 and, when available, external receipt.

## Change control
- **One file per commit.** Commit line: `<path>: <crisp change>`.
- **Versioning:** `vX.Y` — bump **minor** for content changes; bump **major** for structure.
