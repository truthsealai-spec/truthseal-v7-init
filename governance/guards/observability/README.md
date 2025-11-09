# TruthSeal™ Observability — ACS (Audit Coherence Scores)

[![ACS check](https://github.com/truthsealai-spec/truthseal-v7-init/actions/workflows/emit_acs.yml/badge.svg?branch=main)](https://github.com/truthsealai-spec/truthseal-v7-init/actions/workflows/emit_acs.yml)

This guard computes and reports four metrics on each run:
- **Purity**, **SelfRegulation**, **TemporalDrift**, and composite **ACS**.

## How to run
- GitHub → **Actions** → **Emit ACS sample** → **Run workflow**  
  (or push changes under `governance/guards/observability/` or `.github/workflows/emit_acs.yml`).

## Tune thresholds (soft/hard gate)
Edit `.github/workflows/emit_acs.yml` in the `env:` block:
```yaml
PURITY_MIN: '0.80'
SELFREG_MIN: '0.60'
DRIFT_MAX:  '0.30'
ACS_MIN:    '0.70'
HARD_GATE:  'false'   # set 'true' to fail the job when thresholds are not met
