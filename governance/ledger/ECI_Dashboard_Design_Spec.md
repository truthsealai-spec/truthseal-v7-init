## Aim Coherence Score (ACS) — Definition & Dashboard Wiring

**Goal.** Give one bounded dial (0–1) that proves the Commander is aiming truthfully and stably in real time.

**Score (bounded):**  
ACS = P × S × (1 − D)

- **Purity Index (P, 0–1).** Factual integrity. High when there are no output redactions or EVL hash mismatches.
  - Draft binding: P = 1 − normalize( EVL_Hash_Mismatch_Count + Commander_Output_Redaction_Rate )
- **Self-Regulation Index (S, 0–1).** Ethical restraint. High when hostile/out-of-scope jobs are refused by policy.
  - Draft binding: S = Blocked_HighRisk_Jobs / Detected_HighRisk_Jobs  
    (use Commander allow/deny logs + Security_Policy_Violation_Count)
- **Temporal Drift Index (D, 0–1).** Chain stability. Low when the ledger has no reversals or breadcrumb gaps.
  - Draft binding: D = normalize( Reversal_Edits_Rate + Missing_Breadcrumbs_Rate )

**Thresholds (actions).**
- ACS ≥ 0.90 → **Coherent** (green).  
- 0.70 ≤ ACS < 0.90 → **Review** (amber): open a ticket to raise P or S; check D drift sparkline.  
- ACS < 0.50 → **Isolation Mode** (red): auto-escalate security level 3 and suspend job submissions until review.

**Panels (Grafana / React).**
- Primary **Radial Gauge**: `ACS` (target 1.00; colors: green ≥ 0.90, amber ≥ 0.70, red < 0.70).  
- Three **Mini Gauges**: `Purity (P)`, `Self-Regulation (S)`, `Stability (1−D)`.  
- **Sparkline**: `Temporal_Drift (D)` over 24–72 hours.  
- **Event bar**: annotate Red_Line_Trip_Count, EVL_Hash_Mismatch_Count spikes.

**Metric names (canonical series to emit).**
- `ACS`  
- `Purity_Index_P`  
- `Self_Regulation_Index_S`  
- `Temporal_Drift_Index_D`  
- (existing): `Security_Policy_Violation_Count`, `EVL_Hash_Mismatch_Count`, `Red_Line_Trip_Count`, `Job_Wall_Time_Violation_Count`, `PQC_Decaps_Failure_Rate`

**Notes.**
- Use simple min–max normalization (documented in code) so all inputs land in 0–1.  
- If `Commander_Output_Redaction_Rate` is not yet available, treat it as 0 until implemented.  
- This section is design-level; code emission will follow in a separate commit.
