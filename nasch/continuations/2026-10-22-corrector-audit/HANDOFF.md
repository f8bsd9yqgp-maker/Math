# Continue here: the canonical limit is still OPEN

This is a focused continuation of `../2026-10-22/`, not a restart of the
NaSch project. Read this note and its `README.md` before making a new claim.

## Precise target and inherited route

Show existence and uniqueness of
`lim_N q_(N,floor(eta*N))` for `0 < eta < 2`, for the continuous-time
backchip reduction. The original traffic model and interchange of the
rare-braking and thermodynamic limits require additional arguments.

The prior run proved that uniform upper comparisons under doubling and
tripling, with error `C_R/N`, suffice. This note proves that one may use
either population `kH` or `k(H-1)+1`: they differ by at most `4/(9N)` in q.
Neither comparison is proved. Do not turn the conditional convergence theorem
into an unconditional result.

## What this continuation establishes

1. A monotone, vertically homogeneous height corrector Phi satisfies
   `L Phi = F_(N,H)` exactly. The proof uses the common-clock gathering word.
   Its height oscillation bound has constant one, independent of N and H.
2. Subtracting average height gives a Poisson bias with a precise bound for
   relocating one particle. The finite-state Poisson equation itself is
   standard; the order bound is established specifically for this dynamics.
   Corrector jumps are nonnegative and sum to F at each state, so each is
   at most F. The compensated corrector has variance at most F^2*t and the
   exponential-moment bound of F times a compensated rate-one Poisson process.
   The correction between this martingale and one-bond current has exact
   oscillation H*(N-1)/N. Thus the worst-case order-N bias remains.
3. Common-threshold rounding commutes with the min/max height update. This
   gives an exact real-height interpolation and permits rational evaluation
   of half-integer folded heights.
4. Raw column sorting can change the retention count by N-1 at density one.
5. The stronger folded-corrector candidate fails as a pointwise certificate
   with an error of order 1/N. For every odd N, the state (5.4) gives large-ring
   drift exactly half the true small-ring current. Its necessary error
   constant exceeds N/4-1/2. This is an all-N proof, not an extrapolation.

Item 5 does NOT refute the stationary dilation conjecture. It rules out the
specific lower-drift certificate in equation (5.3). Stationary averaging of
the same potential remains conceivable, but requires a new estimate.

## Direct attempts beyond that candidate

Fractional offsets, and cyclic minimum/maximum/average envelopes of the
folded potential, were tested with exact rational arithmetic. No proof of
a size-uniform bound was obtained. The cyclic mean has the best of these
tested bounds in several cases, but it is not justified to extrapolate that
observation. The exact finite outputs are in `results/envelope_probe.json`.

The particle-spacing representation was also reconsidered. Its one-site
level balances reproduce the already known spacing relations, so it is not
being announced as a new solution. Neither a product stationary law nor an
applicable general homogenization theorem was established.

## Verification and numerical caution

`verify.py` uses standard-library rational arithmetic. It checks 20 finite
chains using both full and rotationally lumped solvers, 451 generator
equations, 28,029 corrector order comparisons, 1,300 rounding identities,
412 half-integer resets, 412 interpolated generator equations, and finite
instances of the two general counterexample constructions.
It also checks 451 martingale jump/quadratic bounds and the exact bond-current
bias oscillation in all 20 audited chains.

A solver bug encountered during the audit was corrected before publication:
when a finite chain has transient states, replacing an arbitrary Poisson
equation by the centering equation can produce a singular system. The solver
now drops a row with strictly positive stationary probability and then checks
every original equation. The full and quotient centered solutions agree in
all 20 audited cases. Earlier probe cases at H=N did not encounter the bug.

These checks support, but do not independently peer-review, the written proofs.
No claimed convergence interval or condensate exclusion was obtained.

## The next proof obligation

Either construct a different current potential on the doubled and tripled
rings with the required uniform generator lower bound, or prove an averaged
bound for the defect. A pointwise argument based on simply averaging the two
sorted small-ring harmonic correctors is ruled out by Theorem 4.

The other still-open route is control of escaped mean mass and spatial phase
mixtures in the canonical limits. Previous infinite-volume ordering and
uniqueness results only identify a phase once its deterministic density and
existence have been justified.
