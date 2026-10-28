# Audit of the frozen-anchor current theorem

27 October 2026. Internally audited AI-assisted mathematics; not formal
certification or independent peer review. Parent commit:
`ae78d6f3897ef3560518ac38690d8346ede37273`.

## Analytic claims checked

1. Initial c_j=0 suffices to freeze car j under its own all-braking mask.
   It need not have stored velocity zero if its initial gap is below two.
2. A Poisson-empty interval at j produces exactly that mask and also
   makes the reduced integrated current at j zero.
3. Summed gap conservation gives current differences with the signs
   stated in README (own motion decreases its gap).
4. The first Poisson-empty candidate is independent of the initial full
   state. After cyclic averaging its qualification probability is exactly
   C times the candidate-existence probability, not L*C.
5. Endpoint gap errors are charged by a union bound; no conditional
   independence is used between them and the chosen anchor.
6. Only L<N distinct candidate sites are used in the finite-ring bound.
7. The infinite-line current depends on finitely many initial integer
   gaps in a finite backward clock diagram almost surely. This proves
   distributional continuity, not convergence of its expectation.
8. The limiting reduced stationary current has finite mean because its
   transfer d(g) is at most g and the limiting gap mean is at most eta.
9. The lower mean bound uses nonnegativity and truncation. Equality is
   explicitly conditional on uniform integrability of integrated currents.
10. Convergence of means plus convergence in distribution implies that
    uniform integrability by the truncation proof in README, rather than
    by an assumed moment bound.

## New exact computational audit

Run from this directory:

```bash
python3 verify.py
```

Only the Python standard library is required. The verifier implements
the original four-step traffic rule and the reduced firing rule directly;
it imports no earlier solver or projection implementation.

| Check | Passed |
| --- | ---: |
| Original-rule two-step histories | 300,608 |
| Frozen full anchor and reconstructed-current checks | 196,472 |
| Reduced event words | 27,922 |
| Reduced frozen-anchor identities | 27,200 |
| Exact rational candidate-anchor probability identities | 1,548 |

Full histories exhaust N=2,3,4, masses 1<=H<min(2N,5), all binary
stored-velocity flags, and every pair of coin masks. Positive stored
velocities 1 and 2 have identical one-step acceleration outcomes for
v_max=2, so the two flags cover the needed cases. Reduced words include
all donor words of length at most four for these masses and sizes.

The probability audit averages each binary qualification word over all
rotations, enumerates every absence mask in candidate windows L<N,
and checks exact rational probabilities for three absence parameters.
This tests the candidate-selection calculation, not a stationary full
traffic law.

No old stationary or first-passage solve was rerun. Counts of reduced
words coincide with a previous audit's size because the same finite
domain is convenient; the assertions here are new current-conservation
and anchor assertions, not repeated Poisson-word comparison tests.

## Inherited inputs and scope

The quantitative projected-gap coupling, arrest bound, and synchronous
upper bound are taken from continuation 22 and its stated dependencies.
They are not re-counted as new. No density-phase classification or
canonical reduced-measure selection is needed for the current anchor
theorems themselves; reduced stationarity and a finite limiting mean
suffice for the lower mean bound.

The general fixed-positive-noise stationary flow, unrestricted normalized
mean-current formula, phase selection, and condensate alternatives are
not established. The exact tail criterion is a proved equivalence, not
a claim that its unproved condition holds.
