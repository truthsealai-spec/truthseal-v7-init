=== CLASSIFICATION: INTERNAL — CONFIDENTIAL ===
Title: TQC Coherence Core — Technical Hand-Off (v0.2, QC/PQC explicit)
Distribution: Restricted (Owner + named counterparties under NDA)
=== END CLASSIFICATION HEADER ===

# TQC Coherence Core — Technical Hand-Off
(v0.2) The hardware implementation targets high-risk artificial intelligence (AI) and emerging artificial general intelligence (AGI) systems and is governed by the AEGIS TS-A1 Hardware Law v1.0. TS-A1 defines the minimum non-negotiable rules for the governance processing core: every high-risk run must emit a verifiable receipt, the system must expose a real-time veto lane, and all receipts must be checkable against the Integrity Manifest and external timestamping, secured with post-quantum cryptography (PQC).
## 1) Purpose
Define a **small, integrable IP block** providing hardware-enforced coherence with **post-quantum** receipts, suitable for inclusion in an Nvidia platform variant (e.g., DPU/accelerator).

## 2) Block diagram (logical)
- **LEI-Gate (hard constraint):** blocks incoherent actions; programmable policy table but non-bypassable final gate.  
- **ACS Unit:** computes Aim Coherence Score from (Purity, Drift, Attestation) signals.  
- **Receipt Engine:** packages `{ACS, monotonic counter, timestamp source, PQC signature}`; optional external anchoring hook.  
- **CSF (Coherence Sync Fabric):** deterministic sync lines between Layer-4 input and executive control (dlPFC analogue) to eliminate split-brain paths.  
- **Attestation Interface:** secure boot/TPM feeds; failing attestation forces quarantine path.

## 3) Signals (minimal set)
- Inputs: `purity[0..1]`, `drift[0..1]`, `attest_ok`, `policy`, `clk`, `rst_n`.  
- Outputs: `acs[0..1]`, `coherence_ok`, `receipt_out`, `quarantine_irq`.

## 4) Receipts (QC/PQC)
- **Signature:** PQC (NIST lattice family, e.g., Dilithium class).  
- **Counter:** 64-bit monotonic (non-rollback).  
- **Time:** internal monotonic + hook for secure time source.  
- **Format:** CBOR/JSON; streaming or ring-buffered MMIO.

## 5) SDK (minimal)
- `read_acs()`, `read_receipt()`, `verify_receipt(pubkey)`; kernel driver optional; user-space example included.

## 6) Verification strategy
- **Unit tests:** ACS math, LEI-Gate policy, receipt formatting.  
- **Formal checks:** non-bypass of LEI-Gate; liveness of quarantine.  
- **Side-channel notes:** constant-time signing; key isolation.  
- **Throughput:** target sub-microsecond ACS update; amortized signing per event window.

## 7) Integration
- **Clock/Power:** low-power island; no timing violations into exec plane.  
- **Reset:** LEI-Gate defaults to **deny** until attestation passes.  
- **Debug:** JTAG-gated; receipt path never exposes private key.

## 8) Security notes
- **Key custody:** device-unique PQC keys in secure element.  
- **Anchoring:** optional external timestamp (OpenTimestamps) via host, not in core.  
- **Telemetry privacy:** ACS is scalar; no PII flows through the core.

## 9) Deliverables (Phase I)
- RTL for LEI-Gate, ACS Unit, Receipt Engine, CSF.  
- Testbenches + vectors; SDK sample; integration notes.

— END —
