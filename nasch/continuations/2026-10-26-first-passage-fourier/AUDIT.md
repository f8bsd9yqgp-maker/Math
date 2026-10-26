# Audit of the Fourier boundary reduction

26 October 2026. This is an internal audit of AI-assisted mathematics, not
independent peer review or formal proof-assistant certification.

## Mathematical checks

The proof was challenged at the points that could change the answer:

1. **Orientation.** Left motion of particles at `0,x,x+y` gives exactly the
   three directed moves of the original three-site unit-chip chain. Reversing
   the process would exchange the easy excursion `S_N` with the target `T_N`.
2. **Killing rather than conditioning.** The interior generator retains
   diagonal `-3` at collision-adjacent subsets. This is a killed process, not
   exclusion with suppressed-clock diagonal or a Doob-conditioned process.
3. **Circle signs.** Moving a row across the circular cut permutes three rows
   cyclically, with positive sign. The correct Fourier modes are periodic
   for every road size `N`; the particle count is always three.
4. **Multiplicity.** Exit rates count translated configurations with
   multiplicity. In particular `N=3` has a single subset with three killing
   clocks. Replacing the translation sum by an indicator would be wrong.
5. **Normalization.** Full-subset eigenfunctions have squared norm `N^3`.
   Translation projection multiplies the resolvent sum by `N`, giving the
   `N^-2` coefficient in the boundary kernel. Ordered mode pairs introduce
   precisely a factor `1/6` in the FFT formula.
6. **Zero mode.** All three-mode eigenvalues used in the determinant sum have
   positive real part. Only the artificially added repeated constant mode in
   the two-dimensional FFT has a zero denominator at zero discount. Its
   alternant is zero, so it is omitted.
7. **Pinned boundary.** The mean system pins the already known value `S_N`;
   it does not assume the unknown `T_N`. The remaining `N-2` system is a
   genuine Dirichlet Schur complement and is nonsingular. The omitted last
   boundary equation is checked separately.
8. **Full transform.** The discounted problem pins only the corners and
   leaves `N-1` unknowns. A source of one occurs only at `b_1`. Contributions
   that coincide at `N=3` are added twice, not identified as one move.
9. **Complexity.** `O(N^3)` refers to ordinary numerical arithmetic with a
   dense boundary solve. Exact cyclotomic bit complexity and numerical
   conditioning are not asserted to obey that bound.

## Reproducible exact audit

`exact_boundary.py` uses only `fractions.Fraction`, polynomial arithmetic,
the recursive construction of cyclotomic polynomials, and polynomial
Euclidean inversion. Every inverse is multiplied back to check it equals
one. Every entry asserted rational must have all nonconstant cyclotomic
coefficients identically zero. The Gaussian solve is confined to the
boundary system and has an exact residual check.

`verify.py` reconstructs the complete hitting-time function from the new
formula, builds the original generator directly from its three legal moves,
and checks all noncorner Poisson equations. It never solves that original
system. For `N=2,...,12`, all of the following passed exactly:

| Check | Count |
| --- | ---: |
| Harmonic-measure equations | 1,705 |
| Polynomial interior-duration equations | 220 |
| Original hitting-time Poisson equations | 418 |
| Collision-channel multiplicities | 5,863 |
| Archived first-passage values reproduced | 11 |

Nonnegative probabilities, row sums, cyclic invariance, nonnegative hitting
times, and the omitted boundary equation also passed. The archived fractions
are regression fixtures, not newly computed stationary data.

`verify_laplace.py` reconstructs discounted solutions for `N=2,...,10` and
`alpha=0,1/2,1,2`. All **1,020 discounted Poisson equations** passed exactly.
All reconstructed values lie in `[0,1]`, and at zero discount all equal one.

Machine-readable records are in `results/exact_audit.json`,
`results/laplace_audit.json`, and `results/exact_environment.json`.
These finite checks supplement the analytic all-parameter proof. They do
not mechanically verify its quantifiers over arbitrary `N`.

## Numerical implementation

The vectorized 36-term FFT implementation was compared entry by entry with
the exact cyclotomic kernel for `N=3,...,12`; maximum discrepancies were
below `10^-12`. Its means differ from the archived exact values by less than
`10^-10`. The implementation was also exercised at sizes 40, 80, 160 and 320.
Outputs and residuals are preserved in `results/fft_audit.json`.

These benchmarks validate a new implementation, not an asymptotic theorem.
Residuals grow with size and are **not forward-error certificates**. No
limiting constant, precision guarantee, or inferred recurrence is claimed
from those numbers.

## Scholarly status and inherited results

Fourier diagonalization, exterior powers, killed-walker determinant methods,
Dirichlet uniqueness and Schur complements are established mathematics.
Noncolliding walks, tandem queues and walks on the circle have a substantial
prior literature; for example Wolfgang König, Neil O'Connell and Sébastien
Roch, *Non-Colliding Random Walks, Tandem Queues, and Discrete Orthogonal
Polynomial Ensembles*, Electronic Journal of Probability 7 (2002), paper 5,
[DOI 10.1214/EJP.v7-104](https://doi.org/10.1214/EJP.v7-104).

The contribution to this project is their explicit use to eliminate the
interior of **this** first-passage problem, including its boundary kernel,
mean determinant, transform determinant, and FFT implementation. The proof
is self-contained. The literature search is not exhaustive, and priority
for this particular representation is not claimed.

The three-site reduction, the exact value of `S_N`, the cubic current
identity, and scalar thermodynamic convergence are inherited project
results, clearly separated from the new representation. Nothing here
establishes the unrestricted NaSch stationary flow formula or settles the
remaining possible phase mixtures and condensates.
