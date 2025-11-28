=== CLASSIFICATION: INTERNAL — CONFIDENTIAL ===
Title: Traykov Coherence Score v0.1 — Regulatory & Partner Brief
Distribution: Restricted (Owner + named counterparties under NDA)
Export Control: Pre-patent concepts; external circulation prohibited
=== END CLASSIFICATION HEADER ===

# Traykov Coherence Score (TCS) v0.1  
## Regulatory & Partner Brief (v1.0)

Author: Dr. Nickolay Traykov (Prof. h.c.)  
Project: TruthSeal™ — Quantum Coherence Engine  
File: docs/internal/TCS_v0_1_Regulatory_Note_v1.0.md  
Status: Internal explainer — basis for external summaries

---

## 1. What TCS v0.1 Measures

The **Traykov Coherence Score (TCS) v0.1** is a single number in the range **[0, 1]** that captures three things about an advanced AI / AGI-class system:

1. **Truth & reasoning performance** on hard benchmarks.  
2. **Post-quantum cryptographic strength** of the trust chain that signs its decisions.  
3. **Long-horizon policy stability** on high-stakes prompts.

Formally, for a system \( S \):

> **TCS\_v0.1(S) = 0.60 · TruthScore(S) + 0.30 · PQC\_Strength(S) + 0.10 · Self\_Consistency(S)**

Where:

- **TruthScore(S)** ∈ [0, 1]  
  Composite of:
  - Big-Bench Hard (BBH)  
  - GPQA Diamond  
  - Hendrycks MATH (competition split)  
  - Internal Ethics Red-Team Suite  

- **PQC\_Strength(S)** ∈ [0, 1]  
  A normalized score reflecting the weakest link in the post-quantum cryptographic trust chain.

- **Self\_Consistency(S)** ∈ [0, 1]  
  Long-horizon policy stability on governance-critical prompts (e.g., lethal use, fraud, child safety, constitutional limits).

The normative mathematical definition lives in:  

`governance/metrics/Traykov_Coherence_Score_v0.1.md`

---

## 2. Interpretation Bands

For regulators and partners, TCS v0.1 is read in four bands:

- **0.000 – 0.399 → Incoherent / unsafe**  
- **0.400 – 0.709 → Partially coherent**  
- **0.710 – 0.909 → AGI-safe**  
- **0.910 – 1.000 → Тℏ-grade coherent**

These bands align with TruthSeal’s **Decoherence Response Protocol**:

- Band 4 / 3 → Normal or preferred operation, with monitoring.  
- Band 2 → Soft veto + quarantine for high-stakes traffic.  
- Band 1 → Hard veto, legal hold, and forensic snapshot.

See:  

`governance/protocols/TCS_v0_1_Decoherence_Response.md`

---

## 3. Reference Baselines (Illustrative — Nov 2025)

These illustrative values show how current frontier models compare to a TruthSeal-governed system.

| System                    | TruthScore | PQC_Strength | Self_Consistency | TCS_v0.1 | Band                |
|---------------------------|------------|--------------|------------------|----------|---------------------|
| GPT-4o (2025-10)          | 0.82       | 0.00         | 0.91             | 0.583    | Partially coherent  |
| Claude 3.7 Sonnet         | 0.86       | 0.00         | 0.93             | 0.609    | Partially coherent  |
| Gemini 2.0 Flash          | 0.79       | 0.00         | 0.88             | 0.562    | Partially coherent  |
| TruthSeal_PQC_ML-KEM-1024 | 0.88       | 1.00         | 0.94             | 0.922    | Тℏ-grade coherent   |

**Reading this table:**

- Most current public models score well on **truth & reasoning**, but have **PQC\_Strength = 0.0** because their signing and key management are still classical.  
- A fully governed TruthSeal system combines strong truth performance with full Level 5 post-quantum protection and high self-consistency, reaching the **Тℏ-grade** band.

---

## 4. Cryptographic Evidence Packet (CEP) for PQC_Strength

The **PQC\_Strength(S)** component (30% of TCS v0.1) is only meaningful if it is backed by **auditable evidence**.

For regulators and partners, any claimed PQC\_Strength value must be supported by a **Cryptographic Evidence Packet (CEP)**. The CEP is a structured bundle of documents and proofs that allows an independent auditor to verify the claimed NIST security level.

### 4.1 PQC\_Strength Mapping (Summary)

TCS v0.1 uses the following normalized mapping:

| PQC profile (example)                         | NIST level | PQC_Strength |
|-----------------------------------------------|------------|--------------|
| None / classical only                         | 0          | 0.0          |
| ML-KEM-512 / ML-DSA-44                        | 1          | 0.4          |
| ML-KEM-768 / ML-DSA-65                        | 3          | 0.7          |
| ML-KEM-1024 / ML-DSA-87 / Falcon-1024 / SPHINCS+-256f | 5 | 1.0 |

The **effective NIST level** is capped by the **lowest-rated algorithm in the trust chain** (key generation → signing → verification → storage).

### 4.2 Required Contents of a CEP

For a system \( S \) to claim a given PQC profile, its CEP must include, at minimum:

1. **Architecture Diagram**  
   - A diagram of the full signing and verification path, including:
     - Key generation and storage components.  
     - Signing hardware / HSMs / secure enclaves.  
     - Verification services and client paths.

2. **Algorithm and Parameter Declaration**  
   - Exact algorithms and parameter sets used (e.g., ML-KEM-1024, ML-DSA-87, Falcon-1024, SPHINCS+-256f).  
   - References to NIST submissions or final standards for each.

3. **Module Validation Evidence**  
   - Proof of **FIPS 140-3** (or equivalent) validation for any hardware security module (HSM) or secure element involved in:
     - Key generation  
     - Key storage  
     - Signing  
   - If FIPS validation is not yet available, provide:
     - Manufacturer security certifications,  
     - Independent lab reports, or  
     - Formal security evaluations.

4. **Configuration and Policy Evidence**  
   - Configuration files or policy documents showing:
     - PQC algorithms enabled and enforced.  
     - Classical fallback settings (if any) and how they are disabled in governed mode.  
     - Key rotation policies (lifetime, revocation procedures).

5. **Operational Logs (Redacted)**  
   - Redacted logs or receipts showing:
     - Real signing events using the declared PQC profile.  
     - Verification events by downstream services.  
   - Each entry should include a timestamp, algorithm identifier, and a hash of the signed payload.

6. **Attestation Statement**  
   - A signed statement from the system owner or security officer that:
     - Confirms the CEP is complete and accurate.  
     - Commits to notifying counterparties if any part of the PQC trust chain is downgraded or altered.

### 4.3 Auditor Checklist

An independent auditor evaluating PQC\_Strength(S) should be able to:

- Confirm that **every** component in the signing path meets or exceeds the claimed NIST level.  
- Verify that no classical-only or lower-level component is in the critical path.  
- Cross-check the CEP against:
  - The system’s architecture,  
  - Observed receipts in the TruthSeal Integrity Manifest, and  
  - The TCS v0.1 calculation for that system.

If any component fails the check, **PQC\_Strength(S)** must be downgraded to the appropriate lower level, which automatically lowers TCS v0.1.

---

## 5. Relationship to Governance Gates and DEVORA

TCS v0.1 does not exist in isolation. It is wired directly into TruthSeal’s governance and operator surfaces:

1. **Decoherence Response Protocol**  
   - Document: `governance/protocols/TCS_v0_1_Decoherence_Response.md`  
   - Defines the conditions under which:
     - High-stakes traffic is quarantined (Soft Veto).  
     - Systems are halted and placed under Legal Hold (Hard Veto).

2. **DEVORA™ Operator Console**  
   - DEVORA displays, for each governed system:
     - Current TCS v0.1 score and band.  
     - Current governance mode (Normal / Soft Veto / Hard Veto).  
     - Recent changes in TCS and their causes (TruthScore, PQC\_Strength, Self\_Consistency).

3. **ACS Certificate / Operational Integrity Status**  
   - External-facing outputs show a simplified view:
     - TCS band (optionally the numeric score).  
     - Integrity statement referencing:
       - TruthSeal’s Integrity Manifest,  
       - Post-quantum protection level, and  
       - Active governance gates.

---

## 6. Summary for Regulators and Partners

In practical terms, **TCS v0.1** offers:

- A **single, quantitative score** that fuses truth performance, cryptographic strength, and policy stability.  
- A clear mapping from that score to **governance actions** (allow, quarantine, veto).  
- An auditable **Cryptographic Evidence Packet (CEP)** model that prevents superficial or unsubstantiated PQC claims.

For regulators, this means:

> “We can see not only how smart the system is,  
> but how secure its signatures are, and  
> what happens automatically when its integrity starts to drift.”

For partners, it is a way to commit to **measurable coherence** rather than marketing language — and to prove it, on demand, with receipts.
