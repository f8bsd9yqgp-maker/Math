# Continue from the explicit Fourier boundary system

26 October 2026. Run 18. Parent before publication:
`83a55738ad2d542acc333d8407e81ec95b95f655`.

Read README.md, AUDIT.md and ATTEMPTS.md here. Do not restart the old scalar
thermodynamic convergence proof, phase-selection proof, or full-state
first-passage solves. Internally audited AI-assisted mathematics is not
independent peer review.

## Newly established

The original `T_N` is the corner hitting time of the three-site unit-chip
chain with total mass `N`, starting at `(N-1,0,1)`. Its interior is represented
by three left-moving walkers on the circle of `N` sites killed on collision.

For `X_a={0,a,N-1}`, define `D_k(X)=det[omega^(x_i k_j)]`,
`lambda_k=3-sum_j omega^(-k_j)`, `omega=exp(2*pi*i/N)`. Then

```text
K^(alpha)_(a,c) = N^(-2) sum_(k1<k2<k3, sum k = 0 mod N)
    D_k(X_a) conjugate(D_k(X_c)) / (alpha+lambda_k).
```

This is the discounted first interior-exit probability into the boundary
orbit `(c+1,N-c-1,0)`, from `(a,N-a-1,1)`. No orbit-multiplicity correction
may be dropped: at `N=3` there are three killing clocks at a single subset.
There is no interior exit into `(1,N-1,0)`.

For `n=N-2`, put `S=(N-1)(N+4)/6`, `K=K^(0)`,

```text
M_(a,b) = 2*1[a=b] - 1[b=a-1] - 1[b>=2]*K_(a,b-1),
w_a = 1 + a*(N-a-1)/N + K_(a,n)*S.
T_N = (M^(-1) w)_1 = det(M with column 1 replaced by w)/det(M).
```

The matrix is nonsingular by Dirichlet uniqueness. This is an explicit
linear-size system, not the old block-Schur recurrence in disguise: its
coefficients are already given by a finite spectral sum.

The whole Laplace transform also has a determinant formula, using `N-1`
boundary unknowns and `K^(alpha)`. See README.md equations (18)--(20).

A two-dimensional Fourier Green function and 36 signed lookups per entry
assemble `K` in `O(N^2 log N)` numerical arithmetic. The dense boundary
solve takes `O(N^3)` arithmetic and `O(N^2)` memory. No rational
bit-complexity or conditioning claim is made.

## Code and evidence

* `exact_boundary.py`: exact cyclotomic arithmetic, mean and transform.
* `verify.py`: exact `N=2,...,12` reconstruction checks; 1,705 harmonic
  equations, 220 duration identities, 418 original Poisson equations,
  5,863 exit-multiplicity checks, 11 archived means reproduced.
* `verify_laplace.py`: 1,020 exact discounted Poisson equations for
  `N=2,...,10`, discounts `0,1/2,1,2`.
* `fft_boundary.py`: vectorized numerical implementation. It is not an
  exact or certified-numerical implementation.
* `results/`: exact and numerical audit outputs. Old values are fixtures;
  old solvers were not rerun.

All exact checks passed. The small-N FFT kernel checks passed against exact
entries. These tests supplement the analytic proof; they do not prove a
thermodynamic theorem.

## What remains genuinely open

The spectral/determinant representation and a faster algorithm now satisfy
the original request for an improved finite-first-passage method. An
elementary scalar expression, fixed-order recurrence in N, and a rigorous
limit for T_N/N^2 are still absent.

The fixed-density pile probability Q(eta) already converges uniquely. Its
explicit value, full phase selection inside possible affine intervals,
and finiteness of the critical density remain open. A positive macroscopic
background does not justify replacing the Palm environment of a large pile
by the ordinary stationary background.

The general finite-braking NaSch stationary flow and the interchange of
rare-braking and thermodynamic limits are not solved. Do not write that the
whole traffic problem has been closed.

## Targeted next steps

Analyze the explicit boundary matrix rather than recomputing the triangle.
Possible targets are a boundary-potential-kernel limit, a structured matrix
factorization yielding a scalar recurrence, or controlled small-frequency
asymptotics. The first/last rows and columns of K coincide, but that symmetry
alone has not eliminated the boundary interaction.

For thermodynamic closure, the missing ingredients are still a proof of
phase selection in affine intervals, a controlled moving-head environment,
or a new exact stationary representation. Generic product-measure
condensation results do not apply to this nonproduct model.
