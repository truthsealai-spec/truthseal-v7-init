# TruthSeal™ — QENC Anchoring Playbook v1.0

version: 1.0  
date_utc: 2025-12-02  
owner: TruthSeal™ — Dr. Nickolay Traykov (Prof. h.c.)  

scope: |
  Internal playbook for anchoring the TruthSeal QENC ProofCapsule and
  updating the ledgers.
  This document explains:
    - which artifact is anchored (QENC_v1_0_ProofCapsule.json),
    - how to run the anchoring step (for example with OpenTimestamps),
    - how to update the Integrity Manifest and status docs,
    - which states are allowed (PENDING, RECEIPT_ISSUED, ANCHORED).
  It is for Commander Nick (founder), auditors, and engineering.

---

## 0. Glossary — Laws, Metrics, Artifacts (expanded once)

- **QENC** — Quantum Ecosystem Closure ProofCapsule. Cryptographic proof
  artifact that records a closed, coherent state of a TruthSeal epoch.
- **ULIC** — Universal Law of Infinite Coherence registry block. Lists the
  core laws and their anchored hashes.
- **EVL** — Epoch Verification Ledger. Records verification events (hashes,
  receipts, timestamps) for a given epoch.
- **Integrity Manifest** — TruthSeal manifest that binds together:
  ULIC, EVL, QENC, and other verified artifacts into a composite digest.
- **SHA-256** — Secure Hash Algorithm 256-bit digest, used as the core hash.
- **OpenTimestamps (OTS)** — Bitcoin-based timestamping protocol that proves
  a file existed before a certain time, without revealing the file content.
- **Receipt** — Serialized proof object (for example an “.ots” file) that
  can be verified later against the Bitcoin blockchain.
- **Anchor states** (for any artifact):
  - `PENDING` — file exists and hash is known, but no external receipt yet.
  - `RECEIPT_ISSUED` — OpenTimestamps (or equivalent) produced a receipt;
    Bitcoin confirmation may still be in progress.
  - `ANCHORED` — receipt is verifiable against the public ledger and the
    anchoring time is recorded in the Integrity Manifest.

---

## 1. Artifact — QENC ProofCapsule

1. **Canonical file path**

   - `governance/ledger/seals/QENC_v1_0_ProofCapsule.json`

   This is the single source of truth for the QENC artifact. All hashes
   and receipts MUST be computed from this file only.

2. **Hashing rule**

   - Hash function: `SHA-256`
   - Input: exact file bytes of `QENC_v1_0_ProofCapsule.json`
   - Output: 64-character hexadecimal digest.

   The current canonical digest is stored in the Integrity Manifest and MUST
   match the value produced when you hash the file again.

3. **Pre-anchoring checks**

   Before any new anchoring action:

   - Confirm the file exists at the canonical path.
   - Recompute `sha256(QENC_v1_0_ProofCapsule.json)` using a trusted tool.
   - Compare with the hash recorded in:
     - `governance/ledger/seals/Integrity_Manifest_v8_pre.yaml`
   - If there is any mismatch, STOP and record `UNKNOWN` in status docs
     until the discrepancy is resolved.

---

## 2. Anchoring Workflow (OpenTimestamps example)

This section describes a typical workflow using OpenTimestamps. Equivalent,
court-acceptable timestamping services may be added later, but they must not
weaken the guarantees.

### 2.1 Local preparation

1. Ensure you are on the correct git branch (usually `main`) with a clean
   working directory.
2. Verify the QENC SHA-256 digest as described above.
3. Save the digest in your notes for cross-checking during verification.

### 2.2 Produce an OpenTimestamps receipt

1. Use the OpenTimestamps client (command line or GUI) on
   `QENC_v1_0_ProofCapsule.json`. Typical command-line call:

   - `ots stamp governance/ledger/seals/QENC_v1_0_ProofCapsule.json`

2. The client will produce a receipt file, for example:

   - `QENC_v1_0_ProofCapsule.json.ots`

3. Store this receipt file under the canonical TruthSeal path:

   - `governance/ledger/seals/QENC_v1_0_ProofCapsule.ots`

4. At this moment the state becomes `RECEIPT_ISSUED` even if the Bitcoin
   transaction is not yet fully confirmed.

> If OpenTimestamps or the network is unavailable, record the state as
> `PENDING` and **do not** fabricate times or transaction IDs. Try again
> later; keep the Integrity Manifest honest.

### 2.3 Verify anchoring (once Bitcoin calendar is ready)

1. Use `ots verify` (or the equivalent verification command) on:

   - `governance/ledger/seals/QENC_v1_0_ProofCapsule.ots`

2. When verification succeeds, note:

   - the effective Bitcoin transaction identifier,
   - the anchoring time (UTC),
   - any calendar identifier provided by OpenTimestamps.

3. From this point, QENC is considered `ANCHORED` for TruthSeal purposes.

---

## 3. Updating the Integrity Manifest

Once a receipt is issued or verified, update:

- `governance/ledger/seals/Integrity_Manifest_v8_pre.yaml`

### 3.1 Fields to maintain

In the Integrity Manifest:

- Under the QENC entry:
  - `sha256` — must match the canonical SHA-256 digest.
  - `ots_receipt_path` — set to
    `governance/ledger/seals/QENC_v1_0_ProofCapsule.ots`
  - `ots_calendar_id` — calendar identifier from OpenTimestamps (if given).
  - `anchor_status` — one of:
    - `PENDING`
    - `RECEIPT_ISSUED — awaiting Bitcoin confirmation`
    - `ANCHORED — <UTC timestamp> (Bitcoin)`

- In the `composite_digest` section:
  - Recompute the composite digest if QENC is part of the composite set.
  - Document the recomputation time and tool in the `audit_trail` block.

### 3.2 Audit-trail entry

Every change to QENC anchoring MUST create a new audit entry in
`Integrity_Manifest_v8_pre.yaml`:

- date and time (UTC),
- actor (for example `Commander Nick`),
- action (`QENC receipt issued`, `QENC anchored`, etc.),
- short description (hash confirmed, receipt path set, transaction noted).

No previous entries are ever deleted.

---

## 4. Updating EVL and Status Documents

### 4.1 Epoch Verification Ledger (EVL)

When QENC is anchored for a given epoch, add a corresponding entry in:

- `governance/ledger/EVL_v9.0.yaml` (or the current EVL file).

The entry should include:

- QENC file path,
- SHA-256 digest,
- receipt path,
- anchor state,
- Bitcoin transaction identifier (once known).

### 4.2 Status snapshots

Update any active status or checklist docs, for example:

- `docs/internal/STATUS_PreChristmas_2025_v1.0.md`
- future status files (for example `STATUS_PostChristmas_2026_v1.0.md`)

Each status file should contain a short line such as:

- `QENC_v1_0_ProofCapsule.json — RECEIPT_ISSUED (OpenTimestamps, awaiting Bitcoin confirmation).`
- or
- `QENC_v1_0_ProofCapsule.json — ANCHORED (OpenTimestamps, tx=<id>, time=<UTC>).`

---

## 5. Allowed and Forbidden Actions

**Allowed**

- Recomputing SHA-256 for verification.
- Re-stamping QENC if a previous attempt failed and no valid receipt exists.
- Adding new receipts from additional, reputable timestamping services,
  as long as they do not contradict existing records.

**Forbidden**

- Editing `QENC_v1_0_ProofCapsule.json` after it has been declared canonical
  for this epoch. Any material change requires a **new** QENC version and a
  new Integrity Manifest entry.
- Fabricating anchor times, transaction IDs, or calendar IDs.
- Overwriting or deleting old audit-trail entries.

---

## 6. Quick Checklist (QENC Anchoring)

1. File verified:
   - [ ] `QENC_v1_0_ProofCapsule.json` exists at canonical path.
   - [ ] SHA-256 digest recomputed and matches Integrity Manifest.

2. Receipt created:
   - [ ] OpenTimestamps (or equivalent) receipt generated.
   - [ ] Receipt stored at `governance/ledger/seals/QENC_v1_0_ProofCapsule.ots`.
   - [ ] Integrity Manifest updated to `RECEIPT_ISSUED`.

3. Anchor confirmed:
   - [ ] `ots verify` (or equivalent) succeeded.
   - [ ] Bitcoin transaction ID and UTC time recorded.
   - [ ] Integrity Manifest updated to `ANCHORED — <UTC time>`.
   - [ ] EVL and status docs updated.

When all boxes are ticked, QENC anchoring for this epoch is complete.
