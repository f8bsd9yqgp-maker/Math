# Audit: synchronous pushing and local dynamic reduction

Completed 27 October 2026. Parent commit:
`146dab8e50d54298b2a2fe019871e7290905dc06`.

The proofs are analytic. These finite checks test their structural
ingredients exactly; they are not numerical extrapolation, independent
specialist peer review, or formal proof-assistant certification.

## New claims and dependencies

| Claim | New proof | Inherited inputs |
| --- | --- | --- |
| Exact synchronous-push upper speed | README, Sections 2–5 | Original NaSch rule only |
| U<=epsilon eta/(1-p eta), H<N | Same pathwise comparison | No reduced stationary classification |
| J/(epsilon delta)->1 uniformly in epsilon as eta->0 | README, Section 6 | Previously proved one-speed lower bound |
| Finite-dimensional rare-event reduction, all eta<2 | DYNAMIC_REDUCTION | Exact full-braking projection, serialization, mixed-coin Hamming bound, C and B bounds from continuation 21 |
| Polynomial dependence on observation time | DYNAMIC_REDUCTION, Section 4 | One-sided reduced update and fresh rate-one clocks |
| Positive projected-travel amplification | CLOSURE_ATTEMPTS, Section 2 | Explicit full-braking distance formula; also checked with the original four-step update |

The previous scalar thermodynamic theorem, spacing/pile results,
first-passage formulas, reduced phase classification, and restricted
current limit are not counted as new. The upper pushing proof does not
depend on them. No full stationary or old first-passage solver was rerun.

## Exact computation results

The four scripts use the Python standard library. Integer arithmetic and
fractions.Fraction are used for all asserted comparisons. Seeded cases
are separately identified; their arithmetic is exact but their selection
is not exhaustive.

| Script | Check | Passed |
| --- | --- | ---: |
| verify_parallel_push.py | Original-rule mask domination, exhaustive N=2,...,5, H<N | 137,312 |
| same | Seeded domination, N=2,...,79 | 7,800 |
| same | Uniform binary states, N=2,...,10, H<N | 2,026 |
| same | Auxiliary transition masks | 86,516 |
| same | Uniform-invariance Bernstein coefficients | 11,188 |
| same | Exact reward and geometric-bound identities | 180 |
| verify_push.py | Earlier Poisson-word domination checks, including seeded cases | 297,992 |
| same | Seeded event-order subset of preceding count | 5,440 |
| same | Uniform auxiliary binary states, N=2,...,12 | 8,166 |
| same | Incoming transition counts, including null events | 89,958 |
| same | Exact continuous-time reward identities | 66 |
| same | Positive-amplification family members, ell=1,...,50 | 50 |
| verify_dynamic.py | Rest-projected versus Poisson-word comparisons | 27,922 |
| same | Common-clock Hamming-drift inequalities | 52,804 |
| same | Seeded full-projection/word comparisons | 5,280 |
| same | Rational constant checks | 2,450 |
| verify_cones.py | Single-seed discrepancy containment for finite event words | 362,529 |
| same | Exact telescoping identities | 303 |

The synchronous invariant-law test groups incoming transitions by the
number k of marked occupied sites. Each target word has exactly
`binom(H,k)` incoming masks in this group. Hence the test checks the
coefficients of every `epsilon^k p^(H-k)`, not selected values of epsilon.
Zeros need no coins for this test because the auxiliary update ignores
them. The general proof in README covers all sizes, including N-H=1.

The cone audit checks containment after every event, not just at the
terminal time. Poisson front speeds, stationarity, conditioning on past
errors, and the infinite-volume limiting argument are justified
analytically, not certified by these finite event words.

## Manual proof checkpoints

1. The original four-step rule is exactly
   `w_i=1{v_i>0,g_i>=2}+xi_i 1{g_i>=1}`; the memoryless upper map is
   monotone in heights despite the original velocity memory.
2. The synchronous update is not sequential pushing: only the rightmost
   mark of a one-run determines the moved prefix. Every height moves at
   most once in this auxiliary step.
3. Labelling a uniform zero converts uniform binary words into uniform
   compositions plus a uniform anchor. The factorization proof includes
   the anchor after its displacement, so it does not mistake a Palm
   distribution for an unrooted stationary law.
4. The initial dominating height translation has finite expected cost
   at each fixed N,H. Only after taking the long-time stationary speed
   inequality is the bound applied uniformly over sizes. No size-uniform
   bound on that offset is asserted.
5. The local dynamic coupling uses the same future Poisson clocks for
   every reference flow. The current full state is independent of fresh
   intervals. One-step errors need not form a Markov process.
6. Polynomial error is obtained by telescoping errors at their insertion
   times and propagating each once. Iterating a one-step linear bound
   multiplicatively would not prove the stated polynomial bound.
7. Clock dependency cones depend on event locations and times, not mass
   magnitudes. This validates local process convergence without a gap-tail
   assumption, but gives no control of transported mass.
8. The positive-amplification family is only a pointwise obstruction. No
   stationary occurrence probability or full-model recurrent-class claim
   is attached to it.
9. The dense-traffic limit takes eta->0. It must not be restated as
   unrestricted interchange at a fixed positive eta.

## Reproduction

From this directory in the repository, run:

```bash
python3 verify_parallel_push.py
python3 verify_push.py
python3 verify_dynamic.py
python3 verify_cones.py
```

verify_parallel_push.py imports basic functions from verify_push.py.
verify_dynamic.py imports the direct projection and original-rule update
from the preceding `2026-10-26-gap-balance/verify_local_reduction.py`;
it does not run that earlier script's main program. Keep the repository
directory structure when reproducing. Results are the four JSON files
under results/. The manifest records bytes and SHA-256 hashes.

## Established literature versus project deductions

The factorized parallel mass-transport framework is established:
Evans, Majumdar and Zia,
[*Factorised Steady States in Mass Transport Models*](https://arxiv.org/abs/cond-mat/0406524).
Pushing exclusion models are also established; one primary reference is
Li and Saenz,
[*Contour Integral Formulas for PushASEP on the Ring*](https://arxiv.org/abs/2308.05372).
The present notes supply every invariant-law calculation used, rather
than importing a different model's stationary law into NaSch.

The comparison, dynamic coupling, and precise uniform-limit deductions
are new within this project. No exhaustive literature-priority claim has
been established. The unrestricted full-model problem remains open in
this research record.
