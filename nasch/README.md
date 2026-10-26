# NaSch project: canonical limits and a quantitative full-model approximation

Research record updated on 26 October 2026. Earlier structural notes were
prepared from research runs 6–8 (20–21 October 2026).

**The fixed-density pile probability converges and is strictly positive.**
The [convergence proof](continuations/2026-10-24-thermodynamic-limit/README.md)
is followed by [uniform positivity and mass retention](continuations/2026-10-24-positive-occupancy/README.md)
and the new [phase-selection and macroscopic-background theorem](continuations/2026-10-25-affine-phase-selection/README.md).
The proof is AI-assisted, internally audited, and **not independently
peer-reviewed or formally certified**. No claim of publication priority is
made. Full stationary-measure convergence and the unrestricted NaSch flow
formula remain separate open questions.

The process studied here is the continuous-time backchip reduction used in
our Nagel–Schreckenberg `v_max = 2` project. A rate-one clock at site `i`
retains `1` unit if its mass is at least `2`, retains `0` otherwise, and sends
the rest to `i-1`. This is not the full discrete-time traffic process.

## Latest continuation: local clusters and a size-uniform lower bound

The [local-cluster proof](continuations/2026-10-26-local-clusters/README.md)
improves the full-model joint-limit condition from
`(1-p)N^(3/2)->0` to `(1-p)N->0`. When `epsilon=1-p`, `H/N<=R`,
`1<=H<2N`, and `epsilon*max(N,H)<=1/4`, its explicit bound is

```text
|J(1-epsilon)/epsilon - N*F/(N+H)|
  <= (5R/2+65R^2+20R^3)*epsilon*N.
```

The comparison with a rest-started auxiliary process changes only mixed
clusters of qualified cars and marked coins. A new pair-minimum workload
controls the second moment of the active-car count.

A separate [one-speed comparison](continuations/2026-10-26-local-clusters/UNIFORM_LOWER_BOUND.md)
gives, for all N>=2, H>=1, and 0<epsilon<1,

```text
J(1-epsilon)/epsilon >= N*H/[(N+H)(N+H-1)].
```

This lower bound does not require `epsilon N->0` and has a sharper
fixed-epsilon thermodynamic liminf in the proof. It does not provide the
matching upper bound. The full-model fixed-epsilon thermodynamic limit,
general flow, phase alternatives, and unrestricted interchange remain open.

The [qualified-block theorem](continuations/2026-10-26-local-clusters/ACTIVE_BLOCK_GEOMETRY.md)
also proves `E b+epsilon E m<=epsilon H`, uniformly in road size. It
describes the long moving blocks required for a nonzero unscaled current
at small epsilon; it does not rule out moving vacancy condensates.

The [audit](continuations/2026-10-26-local-clusters/AUDIT.md) records new
exact structural checks, independent direct-relaxation checks, and eight
polynomial interval certificates; the [handoff](continuations/2026-10-26-local-clusters/HANDOFF.md)
preserves the next target. No old stationary or Poisson solver was rerun.

## Previous continuation: quantitative full-model error and a joint limit

The [new 26 October proof](continuations/2026-10-26-rare-braking-error/SHARP_WORKLOAD_BOUND.md)
returns to the original parallel-update NaSch model. Write epsilon=1-p
and let F be the reduced backchip current. For N>=2, 1<=H<2N, H/N<=R
and epsilon*max(N,H)<=1/2, its strongest bound is

```text
|J(1-epsilon)/epsilon-N*F/(N+H)|
 <= (12R^2+3R)*epsilon*N + (6R^3+10R^2)*epsilon^2*N^3.
```

Consequently, for every sequence with N->infinity,
H/N->eta in (0,2), and epsilon*N^(3/2)->0,

```text
J_(N,H)(1-epsilon)/epsilon -> (eta-Q(eta))/(1+eta).
```

This is a restricted joint-limit theorem. It does not permit N->infinity
at fixed epsilon and does not solve unrestricted limit interchange or the
general stationary flow formula. No absence of condensates is assumed.

The proof uses an exact full-braking projection, serialization of simultaneous
triggers from rest, individual remaining workloads and their excess beyond
one, and the inherited current corrector. A random-order comparison improves
the rest-state error without changing the actual parallel model.
An explicit reachable family shows that one extra nonbraking event can reduce
eventual full-braking travel by N-5 at H=N, ruling out a proposed pathwise
acceleration comparison. It is not a stationary-current counterexample.

The [audit](continuations/2026-10-26-rare-braking-error/AUDIT.md) includes
529,232 exact update/shift checks, a new 529,232-mask workload audit,
18,572 serializations, and sixteen polynomial certificates against archived
full-model flow formulas (eight for the original and eight for the sharper
bound). The [zero-noise classification](continuations/2026-10-26-rare-braking-error/ZERO_NOISE_LIMITS.md)
identifies possible zeroth-order local limits without assuming their
spatial ergodicity. The
[handoff](continuations/2026-10-26-rare-braking-error/HANDOFF.md) and
[closure-attempt record](continuations/2026-10-26-rare-braking-error/CLOSURE_ATTEMPTS.md)
preserve the remaining gaps. No old stationary or Poisson solver was rerun.

## Previous continuation: Fourier boundary formula for the original T_N

The [26 October proof](continuations/2026-10-26-first-passage-fourier/README.md)
eliminates the two-dimensional interior of the original three-site unit-chip
first-passage problem. Three walkers killed on collision have an explicit
Fourier determinant Green function; projecting onto total momentum zero
gives every boundary exit probability with the correct multiplicities.

This gives an explicit `(N-2)`-dimensional system and determinant ratio for
`T_N`, and an `(N-1)`-dimensional determinant ratio for the entire first-passage
Laplace transform. A two-dimensional FFT assembles the boundary matrix,
giving `O(N^3)` ordinary numerical arithmetic and `O(N^2)` storage. This is a
spectral representation and algorithmic improvement, not an elementary
scalar formula, a fixed-order recurrence, or a proved limit of `T_N/N^2`.

The [exact audit](continuations/2026-10-26-first-passage-fourier/AUDIT.md)
reconstructs the full original functions and checks their Poisson equations,
without rerunning an old full-state solver. It includes 1,705 harmonic
equations, 418 mean equations, 5,863 collision-multiplicity checks, and 1,020
discounted equations, all passed with exact rational/cyclotomic arithmetic.
The [handoff](continuations/2026-10-26-first-passage-fourier/HANDOFF.md) preserves
the formulas, code and outstanding questions. The unrestricted NaSch flow
and the remaining phase/condensate questions are still open.

## Previous continuation: affine phase gaps and a positive background everywhere

The [25 October proof](continuations/2026-10-25-affine-phase-selection/README.md)
uses lower supporting contacts, now justified by preserved first moments,
to construct positive selected pure phases arbitrarily close to zero.
For every target eta>0 it constructs a selected density c_eta with

```text
2^(-22) min(eta^2,1) <= c_eta < eta/2.
```

Every canonical local limit at eta dominates that pure phase, so none has
a vacuum component. More strongly, for each fixed epsilon>0, with probability
tending to one, every cyclic arc of at least epsilon*N sites has positive
mass and pile densities bounded below by explicit constants depending on eta.
The longest pile-free arc is therefore o(N) in probability, at every positive
density. A condensate above a positive background is still not excluded.

The set of canonically selected pure-phase densities is closed and cofinal
below eta_c. Every gap in this set is an affine interval of Q with selected
endpoints. Consequently, every density where Q is not locally affine has
a unique pure canonical local limit along arbitrary road-size sequences.
Whether affine intervals exist, and selection inside any such interval,
remain unresolved; an affine interval is not asserted to cause nonconvergence.

The [audit](continuations/2026-10-25-affine-phase-selection/AUDIT.md),
[exact verifier](continuations/2026-10-25-affine-phase-selection/verify.py), and
[handoff](continuations/2026-10-25-affine-phase-selection/HANDOFF.md) preserve
the arguments and their scope. No old verifier or stationary solver was rerun.

## Previous continuation: positivity and critical mass retention

The new proof gives, for N>=3 and H>=2,

```text
q_(N,H) >= min(H/N,1)^3 / 1152,
Q(eta) >= min(eta,1)^3 / 1152 > 0.
```

It rules out a vacuum local canonical limit and complete condensation at
every positive density. A weighted empty-block generator identity and a
positive exponential-height function prove the bound without assuming
stationary tail estimates.

The companion [phase-selection theorem](continuations/2026-10-24-positive-occupancy/PHASE_SELECTION.md)
identifies every existing stationary phase's current with eta-Q(eta).
Selecting largest upper supporting-line contact points then proves:

* There is a critical endpoint eta_c>1/217, possibly infinite. Canonical
  masses are uniformly integrable at every finite eta<=eta_c, and the
  largest mass divided by N tends to zero in probability there.
* Q is strictly increasing up to eta_c. If eta_c is finite, Q is permanently
  constant above it, and the entire local canonical law at every eta>=eta_c
  converges to the critical phase of mean eta_c. Escaped mean is eta-eta_c.
* Thus absence of an order-N pile is unconditional at least on
  0<eta<=1/217. Finiteness of eta_c and arbitrary below-critical phase
  selection remain unresolved.

The [new audit](continuations/2026-10-24-positive-occupancy/AUDIT.md),
[verifier](continuations/2026-10-24-positive-occupancy/verify.py), and
[handoff](continuations/2026-10-24-positive-occupancy/HANDOFF.md) preserve the
proof and its boundaries. No explicit general Q or finite-braking NaSch
flow formula is claimed.

## Previously proved scalar convergence

For every finite R there is a limiting function Q such that

```text
sup_(0 <= eta <= R) |pi_(N,floor(eta*N))(g_0 >= 2) - Q(eta)|
    = O_R((log(4N)/N)^(1/4)).
```

Every sequence with N tending to infinity and H/N tending to a finite eta
has the same limiting pile probability Q(eta). A new averaged-height Doob
martingale bound, spatial monotonicity, and localization to auxiliary rings
prove the previously missing finite-time oscillation estimate. The resulting
cross-size error is summable over doublings. No stationary mass-tail or
condensate-exclusion assumption is needed.

The [complete proof](continuations/2026-10-24-thermodynamic-limit/README.md),
[internal audit](continuations/2026-10-24-thermodynamic-limit/AUDIT.md),
[new exact verifier](continuations/2026-10-24-thermodynamic-limit/verify_new_step.py),
and [handoff](continuations/2026-10-24-thermodynamic-limit/HANDOFF.md)
preserve the result and its scope. The convergence rate is an upper bound,
not a claimed sharp exponent or a closed formula for Q.

## Earlier structural results

[The self-contained proof](density_phases_proof.md) establishes:

1. Every translation-invariant stationary common-clock coupling is globally
   ordered, without a moment assumption (all coordinates must be finite).
2. If two stationary laws have finite first moments and deterministic
   almost-sure spatial densities `rho` and `sigma`, then any
   translation-invariant common-clock coupling satisfies
   `E|H_0(t)-G_0(t)| -> |sigma-rho|`. In particular, a stationary law at a
   specified deterministic density is unique **if it exists**.
3. Each such law is a measurable function of the past Poisson clocks, is
   spatially mixing, and has a temporally mixing stationary path law.
4. Every translation-invariant stationary law with finite mean is a mixture
   of these uniquely determined density phases. Its density is the only
   spatial ergodic mixture parameter.
5. The pile probability strictly distinguishes existing phases. This gives
   a bounded block-variance criterion for detecting phase mixtures and two
   explicitly conditional sufficient estimates for canonical convergence.

The proof includes the ordering prerequisite rather than asking the reader
to trust earlier reports. It explicitly distinguishes a deterministic
almost-sure spatial density from an expected density.

The [22 October continuation](continuations/2026-10-22/README.md) proves the
finite bound `q_(N,H) <= H(H-1)/[N(H+N-1)]`, with equality for `H = 1, 2`
and strict inequality for `H >= 3`, and proves that removing a site cannot
decrease current at fixed mass. It also proves that two explicitly stated
dilation comparisons, even with errors of order `1/N`, would imply the
full fixed-density limit. **Those comparisons remain unproved.** The note
includes exact verification code and separately labelled exploratory data.

The [current-corrector audit](continuations/2026-10-22-corrector-audit/README.md)
constructs monotone finite-ring current correctors and proves that a proposed
folding certificate fails for arbitrarily large rings, even when it uses the
exact small-ring corrector. It records an exact rounding identity and rational
checks of alternative certificates. It also gives a uniform fluctuation bound
for the corrected current, while proving that the correction to one-bond
current has an order-N worst-case oscillation. **This refutes one proof mechanism, not
the stationary comparison or the target limit.**

The [23 October continuation](continuations/2026-10-23-buffer-coupling/README.md)
proves an exact synchronized-cover construction at mass `k(H-1)+1` and a
comparison using finite core rings and buffer particles. It supplies a
rationally certified counterexample to monotonicity in clock correlations,
even at fixed size and mass. A proved two-block stationary loss bound has an
order-N reserve threshold. The stronger bound needed for sublinear reserves
**remains unproved**; a further exact counterexample refutes discarding its
loss-weighted correction term.
An error of order `N^(-1/2)` in the resulting two-prime comparisons would
already suffice for all-size convergence. Proofs, exact certificates, and
the unsuccessful closure attempts are preserved in that continuation.

The [capped-transfer continuation](continuations/2026-10-23-capped-bonds/README.md)
proves a uniform comparison: capping transfers at a fixed bond at `C`
increases reciprocal stationary current by at most `1/C`. For several caps
the bounds add. At density at most `rho`, `k` such caps change the
site-averaged pile probability by at most `k*rho^2/C`. An explicitly solved
auxiliary chain, obtained by subdividing oversized transfers into legal
chunks, proves the comparison. Consequently convergence for a single fixed
capped bond, for arbitrarily large caps, would imply the original limit.
**That fixed-cap convergence remains unproved.** The continuation preserves
full proofs, rational stationary certificates, the exact remaining targets,
and a separate flat-negative-pressure observation.

## Further finite-system results

The [24 October continuation](continuations/2026-10-24-sharp-drift/README.md)
proves the sharp uniform bound `q_(N,H) <= 5H/(17N)` for every `N >= 3`,
with equality at `N = H = 3`. An explicit bounded local potential supplies
an integer certificate, finite-time upper bounds and a finite-defect
corollary. A separate exact counterexample shows that negative dependence
of pile indicators is not preserved, even from a deterministic state.
It does not refute negative dependence of stationary laws.

The accompanying [support theorem and matrix obstructions](continuations/2026-10-24-sharp-drift/SUPPORT_AND_MATRIX_OBSTRUCTION.md)
identify the full recurrent class as the states with at least one mass
zero or one; in particular the chain is irreducible for `H < 2N`.
They exclude a common finite-dimensional trace formula for all canonical
systems, prove a linear dimension requirement for the specified local
cancellation ansatz, and give an exact counterexample to a rank-one
empty-site matrix. Infinite-dimensional and other stationary constructions
remain possible. **None of these results proves the thermodynamic limit.**

## Finite-time height comparison, 24 October 2026

The [height comparison](continuations/2026-10-24-height-comparison/README.md)
bounds stationary current differences across ring sizes by expected height
oscillations at a finite time, starting from balanced deterministic mass.
An explicit Poisson backward path controls the error from winding around a
ring. A uniform bound `E range <= C t^(1-delta)` for times of order `sqrt(N)`
was shown to imply convergence along every road-size sequence. That note
left the oscillation bound open; the latest continuation proves it and
obtains a stronger rate by using times proportional to road size. The proof
does not assume stationary mass uniform integrability or absence of condensates.

The same note identifies the exact Horton–Strahler rank update and constructs
an `N/4` failure of a maximum-envelope formula at `H=N`, even with initial
gaps in `{0,1,2}`. Exact audits and separately labelled finite-time simulations
are preserved. Neither the rank representation nor those simulations closes
the thermodynamic problem.

## Scope of the closure and remaining questions

For the canonical stationary law `pi_(N,H)` on an `N`-site ring, the target is

```text
lim_(N -> infinity) pi_(N,floor(eta*N))(g_0 >= 2),  0 < eta < 2.
```

Scalar convergence and positivity are proved. The critical-density
theorem proves mass preservation below an intrinsic endpoint eta_c and
selects the canonical law at upper supporting-line contact points and,
if eta_c is finite, at and above that endpoint. Complete condensation is
excluded at every density; an order-N pile is excluded at least for
0<eta<=1/217 and more generally for every finite eta<=eta_c.

The latest continuation also excludes vacuum mixture components and proves
a positive background on every macroscopic arc at every positive density.
Pure canonical selection holds wherever Q is not locally affine; gaps in
the selected set can occur only on affine intervals with selected endpoints.

Still open: whether eta_c is finite, exclusion of affine selection gaps or
selection within them, an explicit general Q or stationary traffic-flow formula,
the original first-passage quantity `T_N`, and interchange of rare-braking
and thermodynamic limits.

For the established rare-braking-first reduction, the thermodynamic current
coefficient therefore exists and equals `rho*(eta-Q(eta))`, with
`eta=(1-rho)/rho` and `rho>1/3`. This preserves the order of limits.

## Reproduce the exact finite checks

From the repository root, using Python 3.9 or later and its standard library:

```sh
python3 nasch/code/verify.py --output nasch/results/verification.json
```

The verifier checks capped-discrepancy algebra, cancellation and gathering
identities, boundary-current conservation, the two-service particle-lifetime
fact, and seven stationary finite chains in exact rational arithmetic.
It verifies all stationary equations, normalization, and nonnegativity for
each computed chain. It also reproduces a finite counterexample to a uniform
occupied-subset ansatz. These checks can find finite algebra or implementation
errors; they are not a proof by extrapolation from small systems.

- [Mathematical proof and remaining obstacle](density_phases_proof.md)
- [Audit record and provenance](AUDIT.md)
- [Verifier](code/verify.py)
- [Exact finite-ring solver](code/exact_support.py)
- [Recorded exact output](results/verification.json)
- [SHA-256 manifest](MANIFEST.json)

The earlier research packages remain historical records. This publication
contains the audited, self-contained argument for the results listed above;
it does not silently promote every earlier conjecture or numerical observation
to a theorem.
