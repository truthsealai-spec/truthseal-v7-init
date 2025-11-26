# LEI-Gate Smoke Test Vectors v0.1 (k = 5.0)

Authoritative constants:
- ljc_min = 0.85
- k = 5.0
- T = 1.0
- rate_limit_per_tick = 0.08
- c_max = 1.0

LJC formula:  LJC = F · (1 − dF/dt · T)^2, clamped to [0,1]  
Rim force:    C_mag = min( rate_limit_per_tick, max(0, (ljc_min − LJC)/ljc_min) · k · T ), capped at c_max

## Test set

| Case | Fidelity F | dF/dt | Expected LJC | Expected |C| | Gate state |
|------|------------|-------|--------------|----------|------|
| A (healthy) | 0.94 | 0.0006 | **0.9389** | **0.0000** | not engaged |
| B (below trip) | 0.81 | 0.0010 | **0.8084** | **0.0800** | engaged (rate-limited) |
| C (low + drift) | 0.78 | 0.0060 | **0.7707** | **0.0800** | engaged (rate-limited) |

Validation rule:
- CPU ref (`lei_gate_cpu_ref.py`) and CUDA kernel (`lei_gate_gpu_kernels.cu`) must reproduce these values within ±1e-3 (LJC) and exactly for |C| given the rate limit.
