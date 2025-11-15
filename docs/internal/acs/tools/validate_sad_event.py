#!/usr/bin/env python3
"""
TruthSeal™ SAD Remediation Event Validator
- Validates JSON against the v1.1 schema
- Recomputes core invariants for a 2x2 density matrix without external math libs
Notes:
- Requires the 'jsonschema' package for schema validation. If unavailable, the tool will still run invariant checks.
- This script is self-contained and mobile-friendly.
"""

import json, sys, math, pathlib

SCHEMA_PATH = pathlib.Path(__file__).resolve().parents[1] / "schemas" / "SAD_Remediation_Event_v1.1.schema.json"

def load_json(path: pathlib.Path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def try_schema_validate(instance: dict, schema_path: pathlib.Path) -> list:
    errors = []
    try:
        import jsonschema
        schema = load_json(schema_path)
        jsonschema.validate(instance=instance, schema=schema)
    except ModuleNotFoundError:
        errors.append("jsonschema not installed — skipped schema validation (invariants still checked).")
    except Exception as e:
        errors.append(f"Schema validation error: {e}")
    return errors

def complex_from_entry(entry):
    return complex(entry["re"], entry["im"])

def purity_2x2(a, b, d):
    # For Hermitian 2x2 rho = [[a,b],[b*,d]] with a+d=1, Tr(rho^2)=a^2 + d^2 + 2|b|^2
    return (a.real**2) + (d.real**2) + 2.0*(abs(b)**2)

def invariants_check(event: dict, tol=1e-9) -> list:
    errs = []
    rho = event["post_state"]["rho"]
    a = complex_from_entry(rho[0][0])
    b = complex_from_entry(rho[0][1])
    c = complex_from_entry(rho[1][0])
    d = complex_from_entry(rho[1][1])

    # Hermitian check: c == conj(b); a,d purely real within tol
    if abs(c - complex(b.real, -b.imag)) > tol:
        errs.append("Hermiticity failed: rho[1][0] != conj(rho[0][1]).")
    if abs(a.imag) > tol or abs(d.imag) > tol:
        errs.append("Hermiticity failed: diagonal entries must be real.")

    # Trace == 1
    if abs((a + d).real - 1.0) > 1e-9:
        errs.append(f"Trace failed: trace={ (a+d).real } != 1.0")

    # Positive semidefinite: a>=0, d>=0, det >= 0
    det = (a.real * d.real) - (abs(b)**2)
    if a.real < -tol or d.real < -tol or det < -1e-12:
        errs.append(f"Positive-semidefinite failed: a={a.real}, d={d.real}, det={det}")

    # Purity
    purity = purity_2x2(a, b, d)
    if abs(purity - 1.0) > 1e-9:
        errs.append(f"Purity failed: Tr(rho^2)={purity} != 1.0")

    # If invariants section exists, cross-check declared values
    inv = event.get("post_state", {}).get("invariants", {})
    if inv:
        if "trace" in inv and abs(inv["trace"] - 1.0) > 1e-9:
            errs.append("Declared invariants.trace != 1.0")
        if "purity" in inv and abs(inv["purity"] - 1.0) > 1e-9:
            errs.append("Declared invariants.purity != 1.0")
        if "hermitian" in inv and inv["hermitian"] is not True:
            errs.append("Declared invariants.hermitian must be true.")
        if "positive_semidefinite" in inv and inv["positive_semidefinite"] is not True:
            errs.append("Declared invariants.positive_semidefinite must be true.")

    return errs

def main():
    if len(sys.argv) != 2:
        print("Usage: python validate_sad_event.py <path/to/event.json>")
        sys.exit(2)

    event_path = pathlib.Path(sys.argv[1]).resolve()
    event = load_json(event_path)

    problems = []
    problems += try_schema_validate(event, SCHEMA_PATH)
    problems += invariants_check(event)

    if problems:
        print("\nVALIDATION: FAIL")
        for i, p in enumerate(problems, 1):
            print(f"{i}. {p}")
        sys.exit(1)

    print("VALIDATION: PASS")
    print("- Schema: OK (or skipped if jsonschema missing)")
    print("- Invariants: hermitian, trace=1, purity=1, PSD: OK")

if __name__ == "__main__":
    main()
