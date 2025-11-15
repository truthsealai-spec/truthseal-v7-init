{
  "process": "TruthSeal SAD Remediation v1.1",
  "pre_state": {
    "bloch": {"rx": 0.3, "ry": 0.4, "rz": 0.0, "r_magnitude": 0.5},
    "eigenvalues": [0.75, 0.25],
    "purity": 0.625
  },
  "selection": {
    "rule": "argmax_eigenvalue",
    "selected": "lambda1"
  },
  "post_state": {
    "rho": [
      [ { "re": 0.5, "im": 0.0 }, { "re": 0.3, "im": -0.4 } ],
      [ { "re": 0.3, "im": 0.4 }, { "re": 0.5, "im": 0.0 } ]
    ],
    "invariants": {
      "hermitian": true,
      "trace": 1.0,
      "purity": 1.0,
      "positive_semidefinite": true
    }
  },
  "tqc_enforcement": {
    "purity_check": "Tr(rho^2) == 1",
    "temporal_stability": "d(rho)/dt == 0 at commit",
    "status": "PASSED"
  },
  "lei_enforcement": {
    "non_unitary_hash_spec": "ICH v1.0 (PQC hash + time-cost)",
    "proof_handles": {
      "pqc_hash": "<H_PQC>",
      "ich": "<ICH_FINAL>"
    }
  },
  "metadata": {
    "commitment_id": "<GUID>",
    "timestamp_epoch": "<UTC seconds>",
    "agent_signature": "SCA_1001",
    "entanglement_refs": []
  }
}
