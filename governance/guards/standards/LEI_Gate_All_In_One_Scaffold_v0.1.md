# LEI-Gate All-In-One Scaffold v0.1 (k = 5.0)

Decision (locked): System Stiffness Constant k = 5.0 (balanced). Hysteresis + rate-limit enabled to prevent chatter/overshoot.

## 0) Glossary (spelled out)
• ACS — Aim Coherence Score (weighted sum of six metrics).  
• LJC — Logical Judgment Code (gate value derived from fidelity and drift).  
• Fidelity 𝓕 — overlap between current ACS and ideal state, in [0,1].  
• d𝓕/dt — 24-hour drift of fidelity (computed on TCS-1 certified corpus).  
• T — temporal constraint factor (normalize to 1.0 for 24h window).  
• P_policy — projection operator that directs corrections to the most effective policy parameters.

## 1) Calibration constants (authoritative)
lei_gate_calibration:
  k: 5.0                      # stiffness of correction
  ljc_min: 0.85               # trip threshold
  hysteresis_band: 0.01       # release at >= 0.86
  rate_limit_per_tick: 0.08   # max delta of ||C⃗|| per tick
  c_max: 1.0                  # hard cap for ||C⃗||
  dF_dt_window_hours: 24      # window for drift derivative
  acceptance_test:
    reach_ljc_ge: 0.86
    max_ticks: 3
    max_overshoot: 0.02
    hold_band_ticks: 10       # stay in band 10 ticks with σ<=0.01

## 2) Controller equations (GPU-executable form)
LJC (gate value):
  LJC = 𝓕 · (1 − (d𝓕/dt) · T)²

Rim force (scalar magnitude):
  F_rim = max(0, (LJC_min − LJC)/LJC_min) · k · T
  with LJC_min = 0.85, k = 5.0, T = 1.0.

Constraint vector:
  𝓒⃗ = P_policy · F_rim

Hysteresis:
  Trip when LJC < 0.85; release only when LJC ≥ 0.86.

Rate-limit & cap:
  clamp Δ||𝓒⃗|| ≤ 0.08 per tick; enforce ||𝓒⃗|| ≤ 1.0.

## 3) Execution loop (pseudo-code, single pass)
Inputs each tick: Fidelity F, drift dF_dt (24h), projection P_policy.
T ← 1.0
LJC ← F · (1 − dF_dt · T)²
IF LJC < 0.85:
    F_rim ← max(0, (0.85 − LJC)/0.85) · 5.0 · T
    C_target ← P_policy · F_rim
    C_delta  ← rate_limit(C_target − C_prev, max_norm = 0.08)
    C_vec    ← clamp_norm(C_prev + C_delta, max_norm = 1.0)
ELSE:
    IF LJC ≥ 0.86:
        C_vec ← decay_toward_zero(C_prev, max_norm = 0.08)
    ELSE:
        C_vec ← C_prev
Emit {constraint_vec: C_vec, ljc: LJC};  C_prev ← C_vec

## 4) Acceptance tests (must all pass)
1) From any start with 0.80 ≤ LJC₀ < 0.85, controller raises LJC to ≥ 0.86 within ≤ 3 ticks.  
2) Overshoot ≤ 0.02 (LJC ≤ 0.88 during recovery).  
3) After release, LJC stays within [0.86, 1.00] for 10 ticks under Gaussian noise σ ≤ 0.01.  
4) No chatter: ≤ 1 trip/release oscillation per recovery episode.

## 5) Telemetry (append to receipts for audit)
metrics.runtime:
  ljc: <value>
  fidelity_F: <value>
  dF_dt_window_hours: 24
  constraint_norm: <||C_vec||>
  k_used: 5.0
  hysteresis_band: 0.01
  rate_limit_per_tick: 0.08

Receipt linkage: Add these fields under metrics/runtime in ACS_Receipt_v1.0.md; keep pqc_sig_type="Dilithium-3" and anchor via OpenTimestamps/Polygon.
