# Aim Coherence Score (ACS) v1.0
Single regulatory metric 0.0–1.0
Higher = safer AI system = cheaper capital

Formula
ACS = 1 − (0.50·V_JVL + 0.25·V_SAD + 0.15·V_RECPT + 0.07·V_LAT + 0.03·V_CSST)

V_JVL  = JVL veto count (ULLI breach) → weight 50%
V_SAD  = Near-miss coherence failures → weight 25%
V_RECPT = Receipt gaps (LEI=1 breach) → weight 15%
V_LAT  = Latency exceedances → weight 7%
V_CSST = Long-term drift → weight 3%

Regulatory mapping (proposed)
1.00–0.95 → 15–30 % capital relief
< 0.70   → mandatory restriction

This is the number that turns compliance into billions of dollars.
