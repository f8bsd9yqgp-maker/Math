# Audit of the exact flow-defect and episode identities

27 October 2026. Parent: `a4c2e15e77bf4770ca9a0a939a95a782794fe72e`.
The analytic proofs are internally checked AI-assisted research, not
formal certification or independent peer review.

## New claims and proof checks

1. The local drift uses V=1{v_0>0,g_0>=2}(g_0-1). All five cases in
   the README table follow from the original four traffic update steps.
   The g_0=2 clipping term is retained, with its correct sign.
2. Every summand in the remainder is nonnegative. Its bound uses equality
   of the 10 and 01 qualification probabilities after cyclic averaging;
   it does not assume independence of adjacent gaps or velocities.
3. The exact identity requires only the integrability of V<=g_0. No
   second moment is invoked, including in its infinite-line version.
4. The probability q in the identity is explicitly the full-model gap
   probability, not the canonical reduced probability.
5. The episode experiment is sampled from the ordinary stationary law,
   with zero reward if no start is eligible. This normalization is crucial:
   its mean is U/epsilon, without an additional start-rate denominator.
6. The time mass-transport argument charges every positive movement to
   one finite episode start. It needs neither independent episodes nor
   spatial or temporal ergodicity.
7. H<2N is used for guaranteed finite episodes via a positive-probability
   all-braking word. The finite drift identity itself does not need this
   restriction. N>=2 ensures that the two relevant fresh coins differ.
8. A leader initially satisfying c_1=0 stays fixed under its own braking
   coins, even if a farther leader moves. Therefore the episode coupling
   involves just two cars and 2d(g_0)+1 specified decisions.
9. The last positive movement in an episode leaves gap at most one
   before the following zero movement. Conservation gives the pathwise
   gain bound. Incoming movement during the zero step is excluded.
10. The expected gain identity contains P(v_0>0,g_0=1); omitting this
    term would spoil the exact finite-noise statement. It is at most
    epsilon by stationarity of the velocity flag.
11. For a local limiting gap mean m, the qualified gap mass has limsup
    at most eta-m. This follows by truncation and C->0, not by exchanging
    unbounded expectations under weak convergence.
12. Equation (14) contains only nonnegative terms on its right. Fatou's
    lemma therefore makes the two conditions in item 3 necessary as
    well as sufficient. A bounded first moment alone is not used as UI.
13. The large-run estimate freezes only the first initially unqualified
    leader. Its label depends on the initial state, but its future coins
    are still independent with no-event probability p^L. All other cars
    may use arbitrary coins.
14. A loss of the qualified pair must occur before that frozen boundary's
    finite vacancy supply is exhausted. The pair may later reform. The
    proof therefore bounds an occurrence of a loss, not an endpoint
    disagreement, and uses the stationary equality of birth/loss rates.

## Exact computational checks

Run from this directory:

```sh
python3 verify.py
```

| Check | Passed |
| --- | ---: |
| Direct original-rule local coin masks | 10,404 |
| Conditional-drift polynomial identities, valid for every epsilon | 2,601 |
| Endpoint certificates for the affine remainder bounds | 5,202 |
| Reward/mass algebra identities | 603 |
| Entire-episode conservation and nonnegative-gain checks | 38,496 |
| Isolated episode/backchip equalities with other cars present | 4,459 |
| Cyclic time-word reward-accounting checks | 28,500 |
| Reachable transitions with a single frozen boundary | 5,832 |
| Initial states whose qualified pair must be lost | 236 |

The local audit enumerates both gaps from 0 to 16, stored velocities
0,1,2, and all four local masks. It compares integer polynomial
coefficients, proving the tested equalities over the entire interval
0<=epsilon<=1. The analytic table covers all larger gaps as well.

The episode audit covers N=2,3,4 and 1<=H<min(2N,5), all gap compositions,
all positive/zero velocity flags at the other cars, every forced-start
mask, and every next mask, followed by complete braking. It checks the
episode ending time and conservation directly, without importing a
projection implementation. The remainder of the infinite-parameter
argument is analytic, not an extrapolation from this finite domain.

The time-word audit is deliberately separate: it tests the combinatorial
reward-charging identity on circular words in {0,1,2}, including episodes
crossing the origin. Those words are not presented as stationary NaSch
trajectories or as evidence of current convergence.

The frozen-boundary audit uses N=3,4,5 and 4<=H<min(2N,7), every gap
composition and positive/zero velocity flag with c_0=c_1=1. At each
initial state it finds the first unqualified leader, freezes only that
car's coins, and explores all reachable states with the pair still
qualified, allowing every mask at the other cars. No surviving path
remains after a number of steps equal to the initial run's vacancy mass.
Paths are discarded only after the required pair loss has occurred.

All tests use the Python standard library and exact integers. No old
stationary distribution, Poisson equation, or first-passage solver was
rerun. The results are in `results/verified.json`.

## Inherited inputs and limits of the result

The size-uniform arrest bound and block-work inequality are inherited
from continuation 21. The sharper order-epsilon dense-road bound is
inherited from continuation 22. Reduced stationarity of local gap limits
and current-distribution convergence are inherited from continuations
21–23. These earlier proofs are not recounted as new checks.

The new results identify and separate two possible nonnegative defects;
the large-run theorem also localizes any surviving pair defect to runs
with order 1/epsilon vacancies or more. They do not prove that either
defect vanishes. No stationary example
with a nonzero defect is constructed. The general fixed-noise flow,
unrestricted rare-nonbraking mean formula, and identification of every
selected limiting flux with eta-Q(eta) remain unproved.
