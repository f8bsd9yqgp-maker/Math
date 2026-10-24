# Discovery calculations, not additional theorems

The mathematical certificate is `../certificate.json`, verified using
integer arithmetic by `../verify.py`. These files document how candidates
were found and which other possibilities were tested.

`drift_lp.py K` uses NumPy/SciPy to optimize a clipped pair/triple drift
certificate. Recorded K=2,3,4 runs have floating arithmetic. The K=3 and
K=4 searches suggest coefficient 17/5; the separately audited integer
certificate proves that coefficient.

`integer_drift_search.py D` was used with D=5 and D=10. Use only these
recorded multiples of five: the exploratory script forms 17*D//5.
The D=5 output becomes the main certificate after the potential gauge
u(a)-u(b), u=(11,0,0,0). The claimed optimizer optimum is not needed by
the proof. Sharpness comes from the exact N=3,H=3 example.

`block_drift_lp.py K length` explores a different bounded-block potential
ansatz. Some outputs suggest larger coefficients with longer blocks.
Their validity for unbounded masses, ring-size restrictions, and rational
certification have not been completed; they are not proved improvements.

`transient_dependence_probe.py` uses exact integer generator powers to
search for positive small-time covariance. Its one import path was adapted
to this repository layout. The N=4,H=7 example was converted into the
independent short-word proof and verifier in the main note.

`rayleigh_exploration.json` records several exact finite stationary
generating-polynomial searches that found no witness against a Rayleigh
inequality at the tested fields. This does not prove real stability or
negative association. `rayleigh_probe.py` reproduces that search.

`zero_renewal_probe.json` records the unequal weights at (N,H)=(6,6).
That discovery was subsequently promoted to an exact, fully certified
counterexample in `../SUPPORT_AND_MATRIX_OBSTRUCTION.md`; its full 462-state
certificate is in the parent results directory.

Optimizer versions and outputs are reproducibility aids, not proof inputs.
No Monte Carlo result is used in this continuation.
