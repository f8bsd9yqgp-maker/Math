# Audit: polynomial rare-braking error and restricted joint limit

26 October 2026. Internal audit of AI-assisted research, not independent
peer review or formal proof-assistant certification.

## Sharper result completed before publication

[SHARP_WORKLOAD_BOUND.md](SHARP_WORKLOAD_BOUND.md) supersedes the initial
sufficient exponent 3 below with 3/2. Its explicit current error is
`(12R^2+3R) epsilon N + (6R^3+10R^2) epsilon^2 N^3`, provided
`H/N<=R` and `epsilon max(N,H)<=1/2`. The proof tracks individual
remaining lifetimes and their excess beyond one, uses exact projected
word domination, and improves the rest-state corrector error by separating
isolated marks from adjacent ones. It does not assume monotonicity of the
full dynamics.

Additional exact audit, `verify_sharp_workloads.py`, passed:

* 529,232 mask projection upper bounds, first-workload inequalities,
  excess-workload inequalities, and necessary negative-coin conditions;
* 495,976 reduced words dominating the altered projected heights;
* 88,528 single-coin structural comparisons;
* 18,572 rest-state excess bounds and 14,510 isolated-word commutations;
* 5,394 rational checks of the final constants.

These assertions are new; the existing deterministic projection and original
update implementations were reused as fixtures, without repeating the old
stationary or Poisson solves. Results: `results/sharp_workloads.json`.

`verify_sharp_flow_bounds.py` supplies eight additional nonnegative exact
Bernstein-coefficient certificates for the two sharpened inequalities.
The full epsilon intervals end at `1/6,1/8,1/10,1/8` for the four archived
current fixtures. Results: `results/sharp_flow_certificates.json`.

The proof was checked especially for these pitfalls: `k` counts stored
nonzero velocities, while `c` also requires gap at least two; the all-marked
support case has no upstream ordering and is handled separately using
`H<=2NF`; fresh coins are correlated with their own summands in the
workload budget; and a negative projected increment requires a qualified
leader, not just a moving car somewhere else. The comparison with a
random firing order is an auxiliary argument, not an assumption that the
actual mask uses that order.

[ZERO_NOISE_LIMITS.md](ZERO_NOISE_LIMITS.md) separately proves a local
stationary classification at p=1 and a necessary condition for nonzero
unscaled current in an unrestricted joint limit. It does not prove that
the listed mixtures are selected at positive noise, and it does not
establish first-order interchange.

## What was proved in this continuation

For the full parallel-update NaSch `v_max=2` model with `N>=2` and
`1<=H<2N`, write `epsilon=1-p`, let `F_(N,H)` be the reduced backchip current,
and let `U` be full-model stationary mean velocity per car. If
`D=1-epsilon H(N-1)>0`,

```text
|U/epsilon - F| <= epsilon * [
    H*(N*(H+1)+F)/D + (N-1)^2*F
].
```

If `H/N<=R` and `epsilon H(N-1)<=1/2`, the stationary traffic current obeys

```text
|J(1-epsilon)/epsilon - N*F/(N+H)|
    <= (4R^2+3R)*epsilon*N^3.
```

Combined with the previously proved reduced thermodynamic limit, this
establishes the full-model joint limit for `epsilon N^3->0`. The new proof
also gives an exact relaxation map, a serialization of simultaneous
nonbraking triggers from rest, a global nonrest-probability bound, and an
order-N counterexample to pathwise acceleration under extra nonbraking.

## Audit of possible mathematical failure points

1. **Coin convention.** One is a nonbraking event, of probability epsilon.
   Zero is random braking, of probability p=1-epsilon. These are not reversed.
2. **Velocity memory.** Formula (2) is derived from the original four update
   steps. It uses the old activity, not the new activity, to decide whether
   a full-braking car continues. Gaps plus old activity are an exact quotient.
3. **Relaxation endpoint.** Stored velocity becomes zero one update after
   the last movement. The rest time is `1+max ell`, not `max ell`, unless
   the state is already at rest. This extra step is kept throughout.
4. **Density restriction.** `H<2N` prevents a cycle with all cars active and
   all gaps at least two. It is essential to the relaxation formula and to
   terminating the large-gap serialization blocks. No theorem at or below
   vehicle density one third is inferred.
5. **Simultaneous events.** Their relaxed effect is proved to equal a word
   of backchip updates. Singleton triggers are fired first; large-gap
   triggered blocks are processed upstream first. An arbitrary ordering is
   not asserted to work.
6. **Workload bound from rest.** Each car's eventual displacement is a sum
   over a triggered block, so its maximum is at most `sum xi_i*d(g_i)`.
   This is why the rest-state drift is bounded by `epsilon H` rather than
   the much weaker `epsilon N H`.
7. **Global versus local probability.** `A` denotes the probability that
   some car is moving anywhere. Its bound is not a bound uniform in road
   size and is not silently substituted for a local activity fraction.
8. **Corrector normalization.** For the inherited Phi, the sum of all
   corrected jump increments is the one-bond reduced current F, not N*F.
   The full-model drift of Psi equals mean velocity per car because its
   difference from average lifted height is a finite-state function.
9. **Nonrest signs.** Corrected projected increments can be negative. The
   proof uses their absolute bound H+1. The explicit counterexample shows
   that a monotone-event argument would be invalid.
10. **No mixing estimate.** The proof uses stationary bounded-function
    identities. It does not estimate convergence to stationarity of either
    model and does not replace finite-state mixing by an N-independent claim.
11. **Stationary law.** Every stationary full-model law satisfies the
    inequalities; no unproved uniqueness assertion is needed.
12. **Order of limits.** The all-sequence statement has the explicit
    hypothesis `epsilon_N N^3->0`. It cannot be applied after taking
    `N->infinity` at a fixed positive epsilon.

## Exact computational checks

`verify.py` has no third-party dependency. It compares the new expressions
with an independently coded accelerate/collision-brake/random-brake/move
update. It does not solve any stationary or Poisson system.

All 20 parameter pairs with `N=2,...,5` and `1<=H<min(2N,7)` passed:

| New check | Count |
| --- | ---: |
| Initial gap/activity states | 18,572 |
| Explicit relaxation steps | 38,146 |
| Rest-time descent identities | 18,572 |
| Projection invariance identities | 18,572 |
| Arbitrary-coin update comparisons | 529,232 |
| Projected-height shift bounds | 529,232 |
| Active workload perturbation bounds | 510,660 |
| Simultaneous-trigger serializations | 18,572 |
| Rest-state workload bounds | 18,572 |
| Local velocity-rule checks | 126 |
| Rational probability and constant checks | 4,495 |
| Explicit acceleration counterexamples | 101 |

These are overlapping classes of checks; their counts are not presented as
independent experimental observations. Previous finite-state generators and
verifiers were not rerun. The new finite audits support the algebra and the
combinatorial lemmas, while the all-N proof is given in README.md.

The first exploratory state search allowed arbitrary stored velocities.
Its earliest negative-displacement witness was not reachable in one step
from rest. The published counterexample repairs that issue: at H=N, each
specified initial state is reached from a stated resting configuration by
two nonbraking coins. That reachability is checked for all 101 instances.

## Independent checks using archived full-model formulas

`verify_flow_bounds.py` imports four previously recorded rational functions
for stationary traffic flow, at `(N,H)=(3,3),(4,3),(5,3),(3,4)`. It does not
rerun their derivation or claim them as new. Substituting
`epsilon=x/[2H(N-1)]` puts the interval under test at `0<=x<=1`.
The denominators of the archived functions are strictly positive there,
and the new bound has `D=1-x/2>0`.

After clearing those positive denominators, both error inequalities become
polynomial nonnegativity claims. Their exact Bernstein coefficients are
all nonnegative, giving **eight certificates over whole intervals**.
For a polynomial `sum_j a_j x^j` of degree m, the coefficients checked are
`b_k=sum_(j<=k) a_j*binom(k,j)/binom(m,j)`. The Bernstein basis functions
`binom(m,k)x^k(1-x)^(m-k)` are nonnegative and sum to one on this interval,
so the coefficient condition proves the stated inequalities. Results are
in `results/flow_bound_certificates.json`.

This tests the new bound against actual archived full-model stationary
currents, supplementing the structural audit. It does not verify arbitrary
N in place of the analytic proof.

## Inherited inputs and scholarly status

The reduced monotone current corrector is inherited from the 22 October
corrector note. Its pointwise generator identity, monotonicity and vertical
homogeneity are the precise properties imported. The reduced scalar limit
and its finite-size modulus are inherited from the 24 October convergence
note. This continuation does not count those results as new or rerun their
verifiers. Both remain subject to independent review along with this proof.

The conventional NaSch update and the nontriviality of the `v_max>1`
stationary problem are described in Andreas Schadschneider, *The
Nagel-Schreckenberg model revisited*,
[arXiv:cond-mat/9902170](https://arxiv.org/abs/cond-mat/9902170).
The arguments here derive directly from the update rule and do not import
an approximate closure from that paper. Literature priority for the new
quantitative estimate has not been established by the limited search.

No general stationary flow formula, full phase/condensate classification,
or unrestricted exchange of limits has been proved in this continuation.
