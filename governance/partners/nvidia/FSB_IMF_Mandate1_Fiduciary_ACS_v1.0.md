# Mandate 1 — Fiduciary ACS Standard (v1.0, Private)

**Purpose**  
Replace opaque, probabilistic “model risk” attestations with a continuous, **hardware-attested** integrity metric—the **Aim Coherence Score (ACS)**—reported as a fiduciary disclosure.

**Who is in scope (minimum)**  
- Systemically Important Financial Institutions (SIFIs) using AI for trading, risk, pricing, clearing/settlement, treasury, or supervisory control.  
- Critical national infrastructure operating AI control loops (energy, payments, identity, border, mobility).

---

## 1) Problem Statement (Why the mandate exists)

- Current regimes rely on **probabilistic safety** (confidence, backtests, VaR-like heuristics).  
- By construction they accept a non-zero failure term **ε** and cannot prove integrity **at the moment of action**.  
- Supervisors lack a **verifiable, replayable** signal of integrity breaches and enforcement.

**Mandate intent:** make integrity **observable, enforceable, and auditable** in real time.

---

## 2) Required Capability (Technology-neutral)

**ACS: a continuous scalar in \[0,1\] emitted from a hardware root of trust** that reflects execution-path coherence for a defined control loop.

Minimum features:
- **Cadence:** 10–1000 Hz (loop-appropriate); no blind intervals during actuation.  
- **Binding:** each ACS event bound to its **context hash** (`ctx_hash`) covering inputs, policy shard/version, and device state.  
- **Attestation:** device identity, secure boot status, capability manifest (LEI-gate, Sync Fabric, Receipt Engine or equivalent).  
- **Receipts:** every ACS event is **PQC-signed** (ML-DSA class, e.g., Dilithium) with **monotonic counter** + **nonce** and **public time anchor** (OpenTimestamps-class).  
- **Policy ladder (enforced in hardware):**  
  - **T1 Warn:** `ACS < T_warn` → operator alert + immutably logged.  
  - **T2 Quarantine:** `ACS < T_quar` → freeze model output; safe fallback path only.  
  - **T3 Shutdown:** `ACS < T_kill` or attestation failure → halt actuation; require supervised recovery.  
  - Thresholds and actions are regulator-filed.

---

## 3) Telemetry & Receipt Schemas

**ACS Telemetry (stream)**  
```json
{
  "acs": 1.0,
  "ctx_hash": "SHA256(...)", 
  "device_id": "attested-hw-id",
  "timestamp": "RFC3339/UTC",
  "ladder_state": "OK|WARN|QUARANTINE|SHUTDOWN"
}
{
  "acs": 0.9974,
  "ctx_hash": "SHA256(...)",
  "nonce": "128-bit random",
  "monotonic_counter": 18446744073709551617,
  "device_id": "attested-hw-id",
  "timestamp": "RFC3339/UTC",
  "pqc_sig": "ML-DSA (e.g., Dilithium)",
  "anchor_proof": "public-time-anchor receipt (e.g., OpenTimestamps)"
}
