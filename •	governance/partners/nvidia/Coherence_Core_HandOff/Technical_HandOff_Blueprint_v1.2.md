# TQC Coherence Core — Technical Hand-Off Blueprint (v1.2, Private)

Purpose: High-level engineering brief for integrating the TQC Coherence Core IP into NVIDIA architectures (Blackwell / successor). The Core enforces LEI = 1 in hardware and emits verifiable ACS telemetry with cryptographic receipts.

Scope: Functional mandate, interfaces and register map, state machine, trust boundary, threat model, verification plan, deliverables, and open sizing items. No RTL included.

Terminology guardrail (authoritative):
- ULLI (principle): Universal Law of Life & Information. Not a hardware block.
- CSF (hardware): Coherence Sync Fabric — the physical, low-latency sync layer that upholds the principle.
- LEI: Law of Ethical Irreversibility (constant enforced by silicon gating).
- ACS: Aim Coherence Score (Q16.16, sampled and attested).

Language hygiene: avoid “monopoly” phrasing. Prefer integrity-grade, regulator-verifiable, exclusive integrity class where needed.

---

## 1) Three-Point Engineering Mandate

| Component | Engineering Function | Strategic Necessity |
|---|---|---|
| (1) LEI-gate | Synchronous, bounded-latency constraint in the Executive Control / Scheduler path. Inputs: attest_ok, acs_q16_16, policy_pins. Output: ALLOW / QUARANTINE / COUNTER-RECEIPT-REQUIRED. | Makes incoherent execution non-admissible at point of action. Silicon enforcement of LEI = 1. |
| (2) Receipt Engine | Signs gating outcomes plus ACS with PQC (ML-DSA/Dilithium default); sequences with monotonic counter and time bind; exposes sideband Receipt Port and memory-mapped buffer. | Provides auditable evidence without touching customer payloads; regulator-ready integrity trail. |
| (3) Coherence Sync Fabric (CSF) | Low-latency fabric between Input Validation (Layer-4 analog) and Executive Control ensuring attest_ok and ACS are sampled before state-changing actions. | Eliminates split-brain/race; maintains a single coherent state under load. ULLI remains the governing principle. |

---

## 2) Interfaces and Register Map (AXI4-Lite)

Base: 0x4000_0000 (to be assigned)

| Offset | Name | Width | R/W | Description |
|---:|---|---:|:---:|---|
| 0x00 | CONTROL | 32 | RW | [0] enable, [2:1] mode (00 normal, 01 observe, 10 counter-receipt, 11 rsvd), [6:3] policy_pins, [7] soft_reset |
| 0x04 | STATUS | 32 | RO | bit0 attested, bit1 lei_gate_ok, bit2 receipt_ok, bit3 csf_ok, bit4 quarantine, bit5 observe_mode |
| 0x08 | ACS_Q16_16 | 32 | RO | Latest ACS sample (Q16.16) |
| 0x0C | MONO_CNT_LO | 32 | RO | Monotonic counter (lo) |
| 0x10 | MONO_CNT_HI | 32 | RO | Monotonic counter (hi) |
| 0x14 | TIME_BIND_0 | 32 | RO | Time bind (word 0) |
| 0x18 | TIME_BIND_1 | 32 | RO | Time bind (word 1) |
| 0x1C | TIME_BIND_2 | 32 | RO | Time bind (word 2) |
| 0x20 | TIME_BIND_3 | 32 | RO | Time bind (word 3) |
| 0x24 | BOOT_HASH_0 | 32 | RO | Boot measurement hash (0) |
| 0x28 | BOOT_HASH_1 | 32 | RO | Boot measurement hash (1) |
| 0x2C | BOOT_HASH_2 | 32 | RO | Boot measurement hash (2) |
| 0x30 | BOOT_HASH_3 | 32 | RO | Boot measurement hash (3) |
| 0x34 | OUTCOME | 32 | RO | 0=ALLOW, 1=QUARANTINE, 2=COUNTER_RECEIPT_REQUIRED |
| 0x38 | INTR_MASK | 32 | RW | Interrupt enables (receipt_ready, quarantine, attest_fail) |
| 0x3C | INTR_STATUS | 32 | RC | Sticky status; clear on read |

Sideband Receipt Port:
- receipt_valid / receipt_ready
- receipt_frame = { outcome, acs_q16_16, mono_counter, time_bind[127:0], device_id[127:0], boot_hash[127:0], signature[...] }

---

## 3) State Machine and Timing

States: IDLE -> SAMPLE -> DECIDE -> EMIT_RECEIPT -> ENFORCE -> IDLE  
Bounded latency: decision within N cycles of ACS sample (N to be jointly fixed; nominal 8–16 cycles).  
Precedence: attest_ok = 0 => QUARANTINE regardless of ACS/policy.  
Observe-only: mode = 01; gating inhibited; full receipts emitted for A/B validation.

---

## 4) Trust Boundary

- Inside Core: ACS sampling, attestation check, LEI-gate decision, sequencing and signature.
- Outside Core: App/model logic, remediation (halt/rollback/notify).
- Data minimization: Receipts contain metadata only; no user payloads.

---

## 5) Threat Model and Mitigations

| Threat | Mitigation |
|---|---|
| Replay of receipts | Monotonic counter and verifier rejects duplicates; counter included in signature. |
| Key exfiltration | Keys live in RoT; Receipt Engine uses on-die KDF; debug/test fuses lock PQC key paths. |
| Fault injection or clock glitch | CSF cross-checks; decision falls to QUARANTINE on timing anomaly; optional glitch detectors. |
| Boot forgery | boot_measurement_hash latched from RoT; compared in verifier. |
| Debug abuse | JTAG/scan gated behind authenticated test mode; status bits expose debug enable; receipts mark test mode. |
| Side-channel leakage | Constant-time signing; masked PQC operations; receipt throttling if power/EM profile anomaly. |

Compliance posture: FIPS 140-3 readiness; ISO/IEC 15408 evaluation target; supply-chain anchors via device attestation.

---

## 6) Verification and Validation

Acceptance (must pass):
1. Decision latency <= N cycles (configurable in constraints pack).
2. Every non-IDLE transition => signed receipt with strictly increasing counter.
3. attest_ok = 0 => QUARANTINE (receipt shows reason).
4. Observe-only emits identical receipts with outcome = ALLOW_OBS.
5. Receipt verifier (host tool) validates PQC signature plus counter plus boot/time binds.

Artifacts:
- Host Verifier reference (CLI and lib).
- Stimulus generator for ACS/attest waveforms.
- Golden logs for ALLOW / QUARANTINE / COUNTER-RECEIPT-REQUIRED.
- Formal properties pack (LEI-gate safety/liveness).

---

## 7) Telemetry and Example Receipt

Sampling cadence: fixed (e.g., 1 kHz) or event-driven at exec boundary (partner choice).  
Precision: ACS in Q16.16.

Example (CBOR/JSON over sideband):
```json
{
  "v": 1,
  "outcome": "ALLOW",
  "acs_q16_16": 65536,
  "mono_counter": "00000000000007D1",
  "time_bind": "7B9C...A2F1",
  "boot_hash": "A1B2...C3D4",
  "device_id": "9E10...44AA",
  "sig": "MLDSA3:ABCD...EF01"
}
