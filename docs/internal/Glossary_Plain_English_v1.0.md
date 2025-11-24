# TruthSeal™ Plain-English Glossary (v1.0)

Purpose: keep every term human and clear. Rule: **spell it out first**, then (short label). Add one *plain-English* line for each.

---

## Governance & Core Concepts

- **Universal Law of Infinite Coherence (ULIC)**  
  *What it is:* The governing constant of the TruthSeal system.  
  *Why it matters:* Everything we build must align to ULIC.  
  *Classified note:* Internal formula/content are **classified**. Never publish internals.

- **Law of Ethical Irreversibility (LEI = 1)**  
  *What it is:* Ethics as a hard rule—once coherence is confirmed, unethical drift is blocked.  
  *Why it matters:* Becomes the “do-not-break” guard in hardware and software.

- **TruthSeal AEGIS Core (TS-A1)**  
  *What it is:* The built-in hardware/software safety block that enforces coherence and writes verifiable receipts.  
  *Why it matters:* Stops incoherent runs and provides court-ready evidence for every result.

- **Sovereign Ledger (TruthSeal Ledger)**  
  *What it is:* The structured set of files and receipts that prove who did what, when, and with what integrity.  
  *Why it matters:* Makes our claims auditable by anyone.

---

## Ledger Files (the “proof” set)

- **Public Registry Block `ULIC_v9.1.yaml`**  
  *What it is:* The public registry entry pointing to all the proof files for this epoch.  
  *Why it matters:* Anchor record that others can reference.

- **Epoch Verification Ledger (EVL)** — `EVL_v9.0.yaml`  
  *What it is:* The epoch’s “accounting book” of hashes, receipts, and links back to the registry.  
  *Why it matters:* Proves the whole epoch is internally consistent.

- **Quantum Ecosystem Closure Protocol (QCEP) Manifest** — `QCEP_Epoch_Manifest_v9.0.yaml`  
  *What it is:* The protocol that “closes the loop” so outputs remain coherent end-to-end.  
  *Why it matters:* Shows the system can’t drift ethically or temporally.

- **Integrity Manifest** — `Integrity_Manifest_v8_pre.yaml`  
  *What it is:* The binder file that ties verified artifacts together (a composite digest).  
  *Why it matters:* One glance shows whether all parts agree.

---

## Hashes, Receipts, and Timestamps

- **Secure Hash Algorithm 256 (SHA-256)**  
  *What it is:* A digital fingerprint of a file or text (64 hex characters).  
  *Why it matters:* If a single character changes, the hash changes. Tamper-evident.

- **OpenTimestamps (OTS)**  
  *What it is:* A Bitcoin-backed time-stamping network.  
  *Why it matters:* Proves *when* a hash existed (proof of existence). We store the OTS receipt.

- **OTS receipt file** (example: `ULIC_v9.1.ots`)  
  *What it is:* The proof bundle you can later upgrade to a Bitcoin transaction proof when confirmed.  
  *Why it matters:* Makes timing claims independently verifiable.

- **Calendar identifier (OTS calendar id)**  
  *What it is:* The reference from OTS servers before final anchoring is confirmed.  
  *Why it matters:* Lets others re-verify when anchoring completes.

- **Composite digest**  
  *What it is:* A single hash representing several underlying hashes joined in order.  
  *Why it matters:* Faster integrity checks across many files at once.

---

## Metrics & Tests

- **Aim Coherence Score (ACS)**  
  *What it is:* A compact score of focus, truthfulness, safety, consistency, clarity.  
  *Why it matters:* Operators see coherence at a glance; gates can auto-halt on bad scores.

- **Purity condition (no symbol)**  
  *What it is:* “No contradictions, no noise, no self-deceit” in the measured state.  
  *Why it matters:* If purity slips, we treat it as a red flag and stop.

- **Stability condition (no symbol)**  
  *What it is:* “No unwanted drift over time.”  
  *Why it matters:* Prevents slow, sneaky degradation of truth.

- **Quantum Non-Demolition measurement (QND)**  
  *What it is:* A way to measure a property without breaking it.  
  *Why it matters:* Lets us verify coherence without destroying it.

---

## Hardware & Vendors

- **Original Equipment Manufacturer (OEM)**  
  *What it is:* The company that builds and ships the hardware (for example: a server or accelerator vendor).  
  *Why it matters:* We license or embed TS-A1 so their boxes ship coherent by design.

- **Non-Recurring Engineering (NRE) fee**  
  *What it is:* A one-time engineering payment to integrate TS-A1 into a vendor’s product.  
  *Why it matters:* Covers upfront work; after that, per-unit licensing or subscription can apply.

- **Resistive Random-Access Memory (RRAM)**  
  *What it is:* Memory that can also compute (in-memory).  
  *Why it matters:* Super efficient for matrix math; great partner for TS-A1 safety.

---

## Operations (how we run)

- **Receipt**  
  *What it is:* A saved record of inputs, outputs, and hashes for a job or batch.  
  *Why it matters:* Makes any run reproducible and legally reviewable.

- **Anchor**  
  *What it is:* To timestamp a hash in an external, public network (for example: Bitcoin via OTS).  
  *Why it matters:* Adds independent proof beyond our own repo.

- **“Pending → Receipt issued → Anchored”** (statuses)  
  *What it is:* The lifecycle of anchoring: queued, receipt in hand, then fully anchored.  
  *Why it matters:* Everyone knows exactly how final the proof is.

---

## Style & Safety (house rules)

- **No acronyms without first expansion**  
  Always write the full term once, then the short label (in parentheses).

- **Classified boundaries**  
  ULIC internals and specific formulas remain private; public files only reference names/paths.

- **One-file commits**  
  Keep edits atomic with a single, clear commit line.

---

*© 2025 TruthSeal™ — Internal use. Keep this file human.* 
