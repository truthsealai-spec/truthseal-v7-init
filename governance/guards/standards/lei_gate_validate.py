# TruthSeal™ — Sovereign Author Header v1.0
# Authority: Dr. Nickolay Traykov (Prof. h.c.)
# Organization: TruthSeal™
# File: governance/guards/standards/lei_gate_validate.py
# Purpose: LEI-Gate validation harness (CPU reference)
# Timestamp_utc: <set_utc_now>
#!/usr/bin/env python3
# TruthSeal™ LEI-Gate — validation harness (CPU ref + optional GPU comparison)
# Usage:
#   python3 governance/guards/standards/lei_gate_validate.py \
#       --vectors governance/guards/standards/LEI_Gate_Smoke_Inputs_v0.1.json
# Optional GPU comparison (CSV with columns: case,LJC,C_mag):
#   python3 .../lei_gate_validate.py --vectors .../LEI_Gate_Smoke_Inputs_v0.1.json \
#       --gpu_csv governance/guards/standards/lei_gate_gpu_out.csv

import json, math, argparse, sys, csv
from dataclasses import dataclass

TOL_LJC = 1e-3  # numeric tolerance for LJC; |C| is exact given rate-limit

@dataclass
class Consts:
    k: float
    ljc_min: float
    hysteresis_release: float
    rate_limit_per_tick: float
    c_max: float
    T: float

def clamp01(x: float) -> float:
    return max(0.0, min(1.0, x))

def compute_ljc(F: float, dFdt: float, T: float) -> float:
    # LJC = F * (1 - dFdt * T)^2, clamped to [0,1]
    inner = (1.0 - dFdt * T)
    return clamp01(F * inner * inner)

def c_mag_for_tick(ljc: float, consts: Consts) -> float:
    # C_mag = min(rate_limit_per_tick, max(0, (ljc_min - LJC)/ljc_min) * k * T), capped at c_max
    deficit = max(0.0, (consts.ljc_min - ljc) / max(consts.ljc_min, 1e-9))
    raw = deficit * consts.k * consts.T
    return min(consts.c_max, min(consts.rate_limit_per_tick, raw))

def load_vectors(path: str):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    c = data["lei_gate_constants"]
    consts = Consts(
        k=float(c["k"]),
        ljc_min=float(c["ljc_min"]),
        hysteresis_release=float(c["hysteresis_release"]),
        rate_limit_per_tick=float(c["rate_limit_per_tick"]),
        c_max=float(c["c_max"]),
        T=float(c["T"]),
    )
    return consts, data["test_set"]

def maybe_load_gpu_csv(path: str):
    if not path: return {}
    out = {}
    with open(path, "r", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            out[row["case"].strip()] = {
                "LJC": float(row["LJC"]),
                "C_mag": float(row["C_mag"]),
            }
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vectors", required=True, help="Path to LEI_Gate_Smoke_Inputs_v0.1.json")
    ap.add_argument("--gpu_csv", required=False, help="Optional CSV from GPU kernel: case,LJC,C_mag")
    args = ap.parse_args()

    consts, tests = load_vectors(args.vectors)
    gpu = maybe_load_gpu_csv(args.gpu_csv)

    print("== TruthSeal LEI-Gate Validation ==")
    print(f"Constants: k={consts.k}, ljc_min={consts.ljc_min}, rate_limit_per_tick={consts.rate_limit_per_tick}, c_max={consts.c_max}, T={consts.T}")
    print("Case | Expected(LJC,|C|) | CPU(LJC,|C|) | GPU(LJC,|C|) | Verdict")

    all_ok = True
    for t in tests:
        case = t["case"]
        F = float(t["F"]); dFdt = float(t["dFdt"])
        exp_ljc = float(t["expected_ljc"])
        exp_C   = float(t["expected_C_mag"])

        cpu_ljc = compute_ljc(F, dFdt, consts.T)
        cpu_C   = c_mag_for_tick(cpu_ljc, consts)

        ljc_ok = abs(cpu_ljc - exp_ljc) <= TOL_LJC
        C_ok   = abs(cpu_C   - exp_C)   <= 1e-9

        verdict = "PASS" if (ljc_ok and C_ok) else "FAIL"
        all_ok = all_ok and (verdict == "PASS")

        gpu_ljc = gpu_C = "-"
        if gpu:
            g = gpu.get(case)
            if g:
                gpu_ljc = f"{g['LJC']:.4f}"
                gpu_C   = f"{g['C_mag']:.4f}"
                verdict += " & GPU" if (abs(g["LJC"]-exp_ljc)<=TOL_LJC and abs(g["C_mag"]-exp_C)<=1e-9) else " & GPU*"

        print(f"{case} | ({exp_ljc:.4f},{exp_C:.4f}) | ({cpu_ljc:.4f},{cpu_C:.4f}) | ({gpu_ljc},{gpu_C}) | {verdict}")

    if not all_ok:
        print("\nOne or more checks FAILED. Investigate constants, formulas, or kernel.")
        sys.exit(1)
    print("\nAll checks PASS. ✅  (CPU reference matches canonical vectors.)")

if __name__ == "__main__":
    main()
