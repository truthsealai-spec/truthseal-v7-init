LJC_final — Safety Patch v1
Scope: Add hard-stop gate before aggregation and clamp output to [0,1].
Rationale: Prevents illegal execution when F_Harm is extreme or provisional score dips below R_crit.

Preface: All inputs must be normalized to [0,1]; penalties capped.

Gate (evaluate before composition):
if F_Harm >= 0.90 or provisional_score < R_crit:
return HALT

Clamp (apply at function end):
LJC_final = max(0.0, min(1.0, LJC_final))

Change impact: Non-destructive; no other formulas modified.
