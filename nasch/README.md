# NaSch project: canonical pile-probability convergence

Research record updated on 24 October 2026. Earlier structural notes were
prepared from research runs 6–8 (20–21 October 2026).

**The fixed-density limit of the canonical pile probability is proved in the
[latest continuation](continuations/2026-10-24-thermodynamic-limit/README.md).**
The proof is AI-assisted, internally audited, and **not independently
peer-reviewed or formally certified**. No claim of publication priority is
made. Full stationary-measure convergence and the unrestricted NaSch flow
formula remain separate open questions.

The process studied here is the continuous-time backchip reduction used in
our Nagel–Schreckenberg `v_max = 2` project. A rate-one clock at site `i`
retains `1` unit if its mass is at least `2`, retains `0` otherwise, and sends
the rest to `i-1`. This is not the full discrete-time traffic process.

## Latest theorem

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

The latest continuation proves this scalar limit and its independence from
the road-size sequence. It does not prove convergence of the entire local
canonical law, existence of every infinite-volume density phase, absence of
condensation or escaped mean mass, or an explicit stationary traffic-flow
formula. The original first-passage quantity `T_N` also remains open.
No interchange of rare-braking and thermodynamic limits is established.

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
