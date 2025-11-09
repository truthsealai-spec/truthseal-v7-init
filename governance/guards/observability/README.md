# TruthSeal™ Observability — ACS (Audit Coherence Scores)

[![ACS check](https://img.shields.io/github/actions/workflow/status/truthsealai-spec/truthseal-v7-init/emit_acs.yml?branch=main&label=ACS%20check)](../../actions/workflows/emit_acs.yml)

This guard computes and reports four metrics on every run:
- **Purity**, **SelfRegulation**, **TemporalDrift**, and the composite **ACS**.

**How to run**
- GitHub → **Actions** → **Emit ACS sample** → **Run workflow** (or push to this folder/workflow).

**Tune thresholds (soft gate)**
Edit `.github/workflows/emit_acs.yml` in the `env:` block:
