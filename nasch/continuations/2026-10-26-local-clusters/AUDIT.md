# Audit of the local-cluster continuation

26 October 2026. Internally audited AI-assisted mathematics; not independent
specialist peer review or proof-assistant certification. Parent commit:
`9e7323bf9c323a581f4a304964cffb26614ba92d`.

## Results and inherited inputs

1. [README.md](README.md) gives an explicit traffic error at bounded
   vacancy density, of order `(1-p)N`, and proves the joint current
   coefficient when `(1-p)N->0`. It relies on the existing full-braking
   projection, monotone current corrector, comparison at rest, and reduced
   scalar thermodynamic limit. Those inherited inputs are linked there and
   are not independently re-proved in this continuation.
2. [UNIFORM_LOWER_BOUND.md](UNIFORM_LOWER_BOUND.md) proves a new project
   comparison with one-speed parallel traffic. For all N>=2, H>=1 and
   0<epsilon<1, `J/epsilon>=NH/[(N+H)(N+H-1)]`. It also gives an exact
   finite-size comparison formula and a sharper fixed-epsilon thermodynamic
   liminf. The one-speed invariant law is established mathematics and is
   also checked directly in the note; no literature-priority claim is made.
3. Neither result proves a fixed-epsilon full-model thermodynamic limit,
   a general exact stationary flow, the critical-density/condensate
   alternative, or unrestricted limit interchange.
4. [ACTIVE_BLOCK_GEOMETRY.md](ACTIVE_BLOCK_GEOMETRY.md) proves
   `E b+epsilon E m<=epsilon H` for qualified moving blocks without a
   size restriction. This forces sustained unscaled activity into long
   qualified blocks at small epsilon; it does not exclude those blocks.

## Checks and their meaning

* `verify.py`: 529,232 mixed-cluster support comparisons, 529,232 pair
  workload inequalities, 503,992 explicit two-firing domination words,
  25,240 full-ring fallbacks, 1,503 exact cluster-expectation checks, and
  9,996 exact moment/constant checks. Prior update and projection helpers
  are reused as fixtures. No old stationary or Poisson solver is run.
* `verify_independent.py`: 6,840 direct deterministic traffic/relaxation
  checks with an independent four-step implementation and fixed seed.
  These include 145 full-ring and 1,124 negative-projection cases.
* `verify_flow_fixtures.py`: eight exact Bernstein certificates against four
  archived rational full-model current formulas, over whole epsilon
  intervals. The archived formulas are fixtures, not newly solved examples.
* `verify_unit_lower.py`: 12,348 exact transition-weight checks of the
  one-speed stationary product construction and 470,240 ordered one-step
  height comparisons.
* `verify_unit_flow_fixtures.py`: four exact polynomial certificates for
  the stronger finite-size one-speed comparison, each over `0<=p<=1`.
* `verify_block_geometry.py`: 529,232 additional arbitrary-mask checks of
  the qualified-block drift and 55,716 exact conditional expectation checks.

The integer assertions check finite configurations only. The all-parameter
claims stand or fall with the analytic proofs and the explicitly inherited
theorems, not with numerical extrapolation.

## Important proof distinctions

* `c_i` counts *qualified* active cars, while `k` counts all cars with
  nonzero stored velocity. The mixed clusters use `c`; the workload moment
  bounds use `k`.
* The full dynamics is not ordered in its nonbraking coins. The proof
  compares the full relaxed projection to an auxiliary rest-started
  process under the **same** mask and charges their disagreements to
  reduced words. It never assumes full-model attractiveness.
* A disagreement component may cover the ring. The proof treats this case
  with the sup-norm corrector bound, not a nonexistent upstream endpoint.
* In the factorial-moment estimate, `B` contains the fresh coins; its
  correlations with `K` and `K(K-1)` are explicitly calculated.
* The general one-speed lower comparison is an ordered comparison with a
  different process. It does not imply monotonicity in the full-model coin
  sequence or solve the rare-event singular limit.
* A finite-volume `O(epsilon N)` error does not establish an error modulus
  uniform in N. The unrestricted interchange remains open.
