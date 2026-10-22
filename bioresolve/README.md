# BioResolve — conditional mathematical proof and software

**Date:** 22 October 2026  
**Status:** Proof of a *conditional* mathematical inference problem; internally tested and not independently peer-reviewed. This is not a claim of a new mathematical theorem or a universal solution to gene-expression measurement reconciliation.

## Files

- [PROOF.md](PROOF.md) — complete statements and proofs: closed-interval coverage set, exact finite-sample Poisson and A/B ratio confidence sets under bounded calibration, and an impossibility theorem under unconstrained assay efficiencies.
- [finite_sample_reconciliation.py](finite_sample_reconciliation.py) — reference Python implementation using SciPy's exact Poisson/binomial confidence-limit quantiles and an O(n log n) interval sweep.
- [test_finite_sample_reconciliation.py](test_finite_sample_reconciliation.py) — 17 tests, including 4,000 randomized comparisons of the interval sweep against brute-force coverage, zero-count handling, endpoint cases, and numerical confidence-coverage checks.

## Run locally

Python 3.10+:

~~~bash
python -m pip install scipy pytest
python -m pytest -q bioresolve/test_finite_sample_reconciliation.py
~~~

Or from this folder:

~~~bash
python -m unittest -q test_finite_sample_reconciliation.py
~~~

The tests passed locally on 22 October 2026. Test success checks the mathematical implementation; it **does not** verify that any biological laboratory supplied valid gene-specific calibration bounds.

## Example

~~~python
from finite_sample_reconciliation import CountMeasurement, reconcile

instruments = [
    CountMeasurement(count=100, exposure=50, gain_min=0.95, gain_max=1.05),
    CountMeasurement(count=103, exposure=50, gain_min=0.95, gain_max=1.05),
    CountMeasurement(count=0,   exposure=50, gain_min=0.95, gain_max=1.05),
]
answer = reconcile(instruments, max_faults=1, error_probability=0.05)
print(answer["feasible_set"])
~~~

The code returns a possibly disconnected *confidence set*, not a forced unique answer. It tolerates one instrument violating the model, **provided at least two instruments really satisfy the stated Poisson and gain-bound assumptions**.

## Why this is not the full biology problem

Measured counts alone cannot always distinguish unknown endogenous concentration from unknown assay efficiency. The impossibility argument in the proof shows the exact ambiguity. Independent, gene-specific calibration or a justified invariance model is required to move from this mathematical conditional result to physical truth.

This material is part of the broader BioResolve AI-assisted research project, which additionally examined external SEQC/ERCC data. Those experimental comparisons are not mathematical verification of the calibration assumptions used here.

Please treat this as an auditable technical note suitable for independent critique, **not a peer-reviewed discovery or publication-priority claim**.
