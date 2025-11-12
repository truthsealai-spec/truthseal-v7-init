# FSB/IMF — Non-Negotiable Mandates for Hardware-Attested Integrity (v1.0, Private)

**Purpose**  
Define three technology-neutral mandates that convert probabilistic safety into **structural certainty** using **hardware-attested integrity** and verifiable receipts.

**Scope**  
Systemically Important Financial Institutions (SIFIs) and critical national infrastructure using Artificial Intelligence for trading, risk, settlement, or supervisory control.

---

## Mandate 1 — Fiduciary ACS Disclosure

**Objective**  
Make integrity observable and auditable in real time via the **Aim Coherence Score (ACS)**.

**Regulatory Action**  
- Instrument ACS on all in-scope AI control paths.  
- Emit continuous ACS telemetry from a hardware root of trust.  
- Retain **signed ACS receipts** and report threshold crossings/incidents to supervisors.  
- Map ACS events to existing frameworks (Basel Operational Resilience, SR 11-7, EU DORA, ISO/IEC 42001).

**Minimum Capabilities (technology-neutral)**  
- Continuous ACS in \[0,1\] at 10–1000 Hz.  
- Monotonic counters (anti-rollback), device identity, secure boot attestation.  
- Post-quantum signature on every ACS event (see Mandate 3).  
- Policy ladder: T1 warn → T2 quarantine → T3 shutdown **enforced in hardware**.

---

## Mandate 2 — Hardware-Attested Integrity Control

**Objective**  
Enforce integrity **physically**, not only statistically.

**Regulatory Action**  
- Require a **vendor-neutral capability** equivalent to:  
  1) **LEI-gate** — hard constraint that forbids incoherent execution states.  
  2) **Coherence Sync Fabric** — low-latency synchronization lines ensuring subsystem coherence.  
  3) **Receipt Engine** — cryptographically signs ACS events and exposes regulator replay APIs.  
- Attestation must prove these capabilities are active, measured, and non-bypassable.

**Assurance Artifacts**  
- Attestation report (secure boot → measured firmware → capability manifest).  
- Proofs of policy application (quarantine/shutdown traces tied to ACS thresholds).  
- Independent replay tools for supervisors.

---

## Mandate 3 — Post-Quantum Receipts & Chain-of-Custody

**Objective**  
Ensure receipts remain verifiable for decades under future cryptanalysis.

**Regulatory Action**  
- Standardize **post-quantum signatures** (e.g., NIST ML-DSA class such as CRYSTALS-Dilithium) on every ACS event.  
- Require **monotonic counters**, **unique nonces**, and **public time anchoring** (e.g., OpenTimestamps-class services or equivalent) for each receipt.  
- Mandate immutable retention and regulator replay endpoints (export + verification CLI).

**Receipt Format (minimum fields)**  
`acs, ctx_hash, nonce, monotonic_counter, device_id, timestamp, pqc_sig, anchor_proof`

---

## 120-Day Pilot — Acceptance Criteria

1. **Risk evidence:** measurable reduction in incoherence incidents, model overrides, and control breaches versus baseline.  
2. **Latency & coverage:** ACS cadence covers the control loop; no blind spots.  
3. **Enforcement:** verified quarantine/shutdown triggers at policy thresholds.  
4. **Auditability:** supervisors successfully replay a random 10% sample of receipts (signatures, counters, anchors).  
5. **Neutrality:** solution is vendor-agnostic; capabilities are defined functionally.

---

## Supervisor Replay Checklist

- Verify PQC signatures against registered device keys.  
- Check counter monotonicity and nonce uniqueness (anti-replay).  
- Recompute `ctx_hash` for sampled events and match payloads.  
- Validate public time anchors (e.g., OpenTimestamps-class proof).  
- Confirm policy ladder actions for sub-threshold and breach cases.

---

## ACS Telemetry Schema (reference; technology-neutral)
```json
{
  "acs": 1.0,
  "ctx_hash": "SHA256(...)", 
  "nonce": "128-bit random",
  "monotonic_counter": 18446744073709551617,
  "device_id": "attested-hardware-id",
  "timestamp": "RFC3339/UTC",
  "pqc_sig": "ML-DSA signature (e.g., Dilithium)",
  "anchor_proof": "public-time-anchor (e.g., OpenTimestamps receipt)"
}
