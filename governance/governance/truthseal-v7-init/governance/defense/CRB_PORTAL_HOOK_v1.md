**Signed-off-by:** Dr. Nickolay Traykov  
**Author:** Dr. Nickolay Traykov (Bulgarian–Australian)  
**Sovereign Authority:** TruthSeal™ Sovereign Framework | ULIC Continuum  
**Jurisdictional Proof:** Dual Citizenship Verification (BG–AU) | Sovereign ID Chain v1  
**Quantum Seal:** →000qB | The NT  

---

# CRB Portal Hook — v1 (Ratified)
## Crisis Response Bridge (CRB) Interface

**Scope:** Wire Phase 6 (Defense Continuum) to Phase 4 (Crisis Response Bridge) with verifiable, tamper-evident alerts.  
This hook is invoked by the ADC-6A Failsafe Mandate.

- Governance Chain: ULIC / PCD-ULIC-01a / ADC-6A  
- Integrity Standard: SHA256 + Ed25519 + OTS Mirror  

---

### 1) ENDPOINT & AUTHENTICATION
The alert endpoint is cryptographically secured to ensure the alert is authentic and untampered.

- **URL (placeholder):** `https://<CRB_HOST>/api/v1/alerts`  
- **Method:** `POST`  
- **Auth:** `HMAC-SHA256` (shared key id) + **Ed25519** signature of the payload body.  
- **mTLS:** Required (client cert pinned to the QCIM module).  
- **Replay Protection:** `nonce` + `exp` (≤ 60 s window).  

---

### 2) PAYLOAD STRUCTURE (JSON)

```json
{
  "schema": "CRB_PORTAL_HOOK_v1",
  "ts_utc": "<ISO8601>",
  "event_id": "<uuid>",
  "severity": "CRITICAL|MAJOR|ELEVATED|INFO",
  "source": {
    "module": "L_QC|TPM_SGX|VETO_AGENT|GRAFANA",
    "version": "<semver>",
    "host_id": "<attested host uuid>"
  },
  "verdict": {
    "state": "SELF_QUARANTINE|DEGRADED|RECOVERED",
    "reason": "<short code>",
    "detail": "<human readable detail of the failure>",
    "mandatory_resolution": "CRB_HUMAN_RATIFICATION_REQUIRED"
  },
  "proofs": {
    "sha256": "<hex_of_verdict_payload>",
    "ots_receipt": "OTS_PLACEHOLDER",
    "tpm_quote": "TPM_QUOTE_PLACEHOLDER",
    "sgx_report": "SGX_REPORT_PLACEHOLDER"
  },
  "links": {
    "ledger_ref": "governance/receipts/attestation_<file>.md",
    "defense_ref": "governance/governance/defense/ADC_6A_CHECKLIST.md",
    "audit_chain_ref": "ledger/audit/2025Q4.json"
  }
}
```
