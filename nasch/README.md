# NaSch project: proved structure of the reduced backchip process

Research note prepared for GitHub on 22 October 2026, from research runs 6–8
(20–21 October 2026).

**The fixed-density thermodynamic-limit problem remains open in this
project.** This directory supplies mathematical proofs of more limited
structural theorems, with exact finite checks. The proofs are AI-assisted,
internally audited, and **not independently peer-reviewed**. No claim of
publication priority is made. The computations do not certify the
infinite-volume measure-theoretic arguments.

The process studied here is the continuous-time backchip reduction used in
our Nagel–Schreckenberg `v_max = 2` project. A rate-one clock at site `i`
retains `1` unit if its mass is at least `2`, retains `0` otherwise, and sends
the rest to `i-1`. This is not the full discrete-time traffic process.

## What is proved

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

## What is not proved

For the canonical stationary law `pi_(N,H)` on an `N`-site ring, the target is

```text
lim_(N -> infinity) pi_(N,floor(eta*N))(g_0 >= 2),  0 < eta < 2.
```

This directory does not prove that limit, construct a counterexample, prove
existence of infinite-volume phases at every positive density, exclude
condensation or escaped mean mass, or give a general exact stationary traffic
flow formula. The original first-passage quantity `T_N` also remains open.
No interchange of rare-braking and thermodynamic limits is established here.

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
