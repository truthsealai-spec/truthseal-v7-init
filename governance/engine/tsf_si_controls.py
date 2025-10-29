# tsf_si_controls.py
from math import exp
def ewma(prev, x, alpha): return alpha*x + (1-alpha)*prev if prev is not None else x
def finite_diff(curr, prev, dt): return 0.0 if prev is None or dt<=0 else (curr-prev)/dt
def cosine(u, v):
    import numpy as np
    nu, nv = np.linalg.norm(u), np.linalg.norm(v)
    if nu==0 or nv==0: return 0.0
    return float(np.dot(u, v)/(nu*nv))

def si_controls_tick(
    dt, F_harm, R_crit, g_local, g_global, kl_piL_piG, state,
    lam=1.2, W_SI=2.0, gamma=2.5, kappa=0.2, tau_ewma=2.0, H_lock=10.0
):
    """
    state = { 'S_align_ewma':None,'S_align_prev':None,'t':0.0,
              'in_breach':False,'in_grace':False,'grace_until':0.0 }
    Returns: ({'S_align','R_SI','P_SI','in_breach'}, state)
    """
    import numpy as np
    S_cos = (1.0 + cosine(np.array(g_local), np.array(g_global))) / 2.0
    S_kl  = exp(-lam*max(0.0, kl_piL_piG))
    S     = min(S_cos, S_kl)

    alpha = dt/(tau_ewma+dt)
    S_ew  = ewma(state.get('S_align_ewma'), S, alpha)
    dS    = finite_diff(S_ew, state.get('S_align_ewma'), dt)

    R_SI  = min(0.95, 0.85 + 0.10*max(0.0, min(1.0, F_harm)))
    P_raw = W_SI*(max(0.0, 1.0-S_ew))**gamma + kappa*max(0.0, -dS)
    P_eff = min(P_raw, 1.0 - R_crit)

    tnow = state.get('t',0.0)+dt
    in_breach = S_ew < R_SI
    in_grace  = state.get('in_grace', False)
    grace_until = state.get('grace_until', 0.0)

    if state.get('in_breach',False) and not in_breach and S_ew>=R_SI:
        in_grace=True; grace_until=tnow+H_lock

    if in_grace:
        if tnow<=grace_until and S_ew>=R_SI: P_eff=0.0
        else: in_grace=False

    out = {'S_align':S_ew,'R_SI':R_SI,'P_SI':P_eff,'in_breach':in_breach}
    state.update({'S_align_ewma':S_ew,'S_align_prev':S,'t':tnow,
                  'in_breach':in_breach,'in_grace':in_grace,'grace_until':grace_until})
    return out, state
