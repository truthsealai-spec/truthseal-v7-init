# TruthSeal™ Observability — ACS (Audit Coherence Scores)
TruthSeal™ Observability provides an Audit Coherence Score (ACS) pipeline for high-risk artificial intelligence (AI) and emerging artificial general intelligence (AGI) systems. It turns raw telemetry from models, GPUs, and governance cores into a single integrity signal backed by cryptographic receipts and post-quantum cryptography (PQC).

This guard computes and reports four metrics on every run:

- **Purity**, **SelfRegulation**, **TemporalDrift**, and the composite **ACS**.

---

## How to run
- GitHub → **Actions** → **Emit ACS sample** → **Run workflow**  
  *(or push any change under `governance/guards/observability/` or `.github/workflows/emit_acs.yml`).*

## Tune thresholds (soft/hard gate)
Edit `.github/workflows/emit_acs.yml` in the `env:` block:

```yaml
PURITY_MIN: '0.80'
SELFREG_MIN: '0.60'
DRIFT_MAX:  '0.30'
ACS_MIN:    '0.70'
HARD_GATE:  'false'   # set 'true' in PR gate only
