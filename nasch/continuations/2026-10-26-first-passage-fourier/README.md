# An explicit Fourier boundary reduction for the original first-passage problem

26 October 2026. AI-assisted research with a complete proof below and exact
finite audits. Independent specialist review and publication-priority
verification remain outstanding.

**New result.** The original three-hole first-passage mean `T_N` is determined
by an explicit `(N-2)`-dimensional boundary system. Its coefficients are finite
Fourier sums, with no unknown interior probabilities. A two-dimensional FFT
assembles the coefficients, giving `O(N^3)` ordinary numerical arithmetic and
`O(N^2)` storage. The same construction gives the **entire first-passage
Laplace transform** through an `(N-1)`-dimensional boundary system.

This improves the project's previous block-Schur algorithm, which eliminated
`O(N)` dense blocks of width `O(N)`. It is an explicit spectral/determinant
representation, not an elementary scalar formula or a fixed-order recurrence
in `N`. It does not solve the unrestricted stationary NaSch traffic formula,
the remaining phase-selection questions, or interchange of limits. The
fixed-density scalar convergence theorem was already obtained in a previous
continuation and is not counted as a new result here.

## 1. The precise first-passage problem

For `N>=2`, let `Z_t` have generator `Q_0` on triples of nonnegative
integers with `x+y+z=N`. Its three possible moves, each at rate one, are

$$
(x,y,z)\longrightarrow
(x-1,y+1,z),\quad(x,y-1,z+1),\quad(x+1,y,z-1),
\tag{1}
$$

with a move suppressed when its donor coordinate is zero. Let `tau` be the
first hitting time of the three corners `(N,0,0),(0,N,0),(0,0,N)`, and write

$$
T_N=\mathbb E_{(N-1,0,1)}\tau,\qquad
S_N=\mathbb E_{(N-1,1,0)}\tau
   =\frac{(N-1)(N+4)}6.                            \tag{2}
$$

This is the original `T_N` from the three-vacancy reduction. It is not the
different problem of three backchip sites with arbitrary mass.

The chain is finite and irreducible: individual chips can be routed around
the directed three-site cycle to transform any composition into any other.
All hitting times considered here therefore have finite means. The formula
for `S_N` is inherited; a short justification is included for completeness.
Uniform measure on the `binom(N+2,2)` compositions is stationary, since the
number of incoming edges equals the number of nonzero coordinates, which
also equals the number of outgoing edges. Corner excursions have a mean-one
corner holding time and mean `S_N` time away. Cyclic symmetry identifies the
three corner types. Consequently `1/(1+S_N)=3/binom(N+2,2)`, giving (2).

We work modulo cyclic rotation of coordinates. Define boundary representatives

$$
b_a=(a,N-a,0),\qquad 1\le a\le N-1,
$$

and `t_a=E_{b_a} tau`, with `t_0=0`. Then `t_1=T_N` and `t_{N-1}=S_N`.
For `1<=a<=N-2`, put

$$
g_a=(a,N-a-1,1),\qquad X_a=\{0,a,N-1\}\subset\mathbb Z/N\mathbb Z.
\tag{3}
$$

## 2. Explicit harmonic measure of the interior

Assume `N>=3`. Let `sigma` be the first exit from the strictly positive
triples. For an interior triple `g=(x,y,z)`, write

$$
X(g)=\{0,x,x+y\},\qquad \omega=e^{2\pi i/N}.
$$

For a strictly increasing triple of modes `k=(k_1,k_2,k_3)` in
`{0,...,N-1}`, define

$$
D_k(X)=\det[\omega^{x_i k_j}]_{i,j=1}^3,
\qquad \lambda_k=3-\sum_{j=1}^3\omega^{-k_j},       \tag{4}
$$

where the sites of `X` are written in increasing order. For `alpha>=0`, set

$$
H_c^{(\alpha)}(g)=\frac1{N^2}
\sum_{\substack{0\le k_1<k_2<k_3<N\\
                 k_1+k_2+k_3\equiv0\pmod N}}
\frac{D_k(X(g))\overline{D_k(X_c)}}{\alpha+\lambda_k},
\quad 1\le c\le N-2.                               \tag{5}
$$

**Theorem 1 (explicit exit kernel).** For every interior triple,

$$
H_c^{(\alpha)}(g)
=\mathbb E_g[e^{-\alpha\sigma}
      \mathbf1_{\{Z_\sigma\text{ is a cyclic rotation of }b_{c+1}\}}].
\tag{6}
$$

In particular all values in (5) are real and nonnegative; at `alpha=0`
they sum to one over `c`. There is no
interior exit into the orbit of `b_1`.

### Proof: three walkers killed at collision

Put three particles on the circle of `N` sites. Each moves one site to the
left at rate one. Kill the process when a move lands on an occupied site.
The cyclic positive spacings between the particles obey exactly (1) until
their first zero spacing. For example, for positions `0,x,x+y`, moving the
middle particle left changes the spacings to `(x-1,y+1,z)`; the other two
moves give the other two transitions in (1).

For unmarked particles, changing the marked starting particle cyclically
rotates the spacings. Thus the chain on positive triples modulo cyclic
rotation is exactly the chain on three-particle subsets modulo spatial
translation. We only use rotation-invariant functions of the triples, so
this identification loses no information needed here.

Let `L` be the killed generator on three-element subsets. Its diagonal is
`-3`, including attempted moves which cause killing. Its off-diagonal entries
count allowed one-step left moves. Determinants in (4) vanish when two rows
coincide, so collision moves contribute zero. A particle passing from site
zero to site `N-1` requires a cyclic reordering of three rows, of sign
`(-1)^2=+1`. There is therefore **no antiperiodic boundary correction**, for
either even or odd `N`. Expanding the determinant gives

$$
L D_k=-\lambda_k D_k.                              \tag{7}
$$

The normalized one-particle Fourier matrix is unitary. Its third exterior
power is unitary as well; equivalently, Cauchy--Binet gives

$$
\sum_{|X|=3}\overline{D_k(X)}D_\ell(X)=N^3\mathbf1_{\{k=\ell\}}.
\tag{8}
$$

There are `binom(N,3)` such vectors, so they form a complete orthogonal
basis. Moreover `Re(lambda_k)>0`: equality would require all three distinct
modes to equal zero modulo `N`, which is impossible. Hence the discounted
Green function of the killed chain is

$$
R_\alpha(X,Y)=\int_0^\infty e^{-\alpha t}e^{tL}(X,Y)\,dt
 =\frac1{N^3}\sum_{k_1<k_2<k_3}
 \frac{D_k(X)\overline{D_k(Y)}}{\alpha+\lambda_k}.     \tag{9}
$$

For fixed `c`, the exit rate from a subset `Y` into the boundary orbit
`b_{c+1}` is

$$
E_c(Y)=\sum_{u=0}^{N-1}\mathbf1_{\{Y=X_c+u\}}.       \tag{10}
$$

To check multiplicities, in a translated configuration
`{u,u+c,u-1}` it is the particle at `u` that collides by moving left; the
third particle determines `c` uniquely. Conversely each collision with this
boundary orbit determines such a `u`. Thus (10) is a bijective count of
**moves**, not just a count of distinct translated subsets. At `N=3`, for
example, all three translates are the same subset and there are three
collision clocks. The factor three must be retained.

Every collision starts with a positive spacing equal to one. The next
spacing increases by one, hence the corresponding `b` index is at least
two; this proves the assertion about `b_1`.

The discounted exit probability is `sum_Y R_alpha(X,Y) E_c(Y)`, by integrating
the pre-killing distribution against its exit rates. Spatial translation
satisfies

$$
D_k(X_c+u)=\omega^{u(k_1+k_2+k_3)}D_k(X_c).
$$

Again, cyclic row reordering has positive sign. Summing over `u` projects
onto total momentum zero and contributes a factor `N`. Substituting (9) and
(10) therefore gives exactly (5). This proves (6), including the normalization
and all special-period multiplicities. The sums are finite throughout.
$\square$

## 3. Eliminate the entire interior for the mean

Let

$$
K_{a,c}=H_c^{(0)}(g_a),\qquad 1\le a,c\le N-2.       \tag{11}
$$

**Lemma.** The mean time to leave the interior, from `(x,y,z)`, is `xyz/N`.

**Proof.** Direct expansion of the three increments in (1) gives
`Q_0(xyz)=-(x+y+z)=-N` in the interior. The polynomial vanishes on the
boundary. The finite Dirichlet problem for the killed chain has a unique
solution, so `xyz/N=E sigma`. $\square$

The strong Markov property and Theorem 1 consequently give

$$
\mathbb E_{g_a}\tau=
\frac{a(N-a-1)}N+\sum_{c=1}^{N-2}K_{a,c}\,t_{c+1}.   \tag{12}
$$

The first-step equations on the boundary are

$$
2t_a-t_{a-1}-\mathbb E_{g_a}\tau=1,
\quad 1\le a\le N-2,                               \tag{13}
$$

and

$$
2t_{N-1}-t_{N-2}-t_1=1.                            \tag{14}
$$

Set `n=N-2` and define the explicit `n` by `n` matrix and vector

$$
M_{a,b}=2\mathbf1_{\{a=b\}}-\mathbf1_{\{b=a-1\}}
        -\mathbf1_{\{b\ge2\}}K_{a,b-1},             \tag{15}
$$

$$
w_a=1+\frac{a(N-a-1)}N+K_{a,n}\frac{(N-1)(N+4)}6,
\qquad 1\le a,b\le n.                              \tag{16}
$$

**Theorem 2 (mean and determinant formula).** `M` is nonsingular, and

$$
\boxed{T_N=e_1^{\mathsf T}M^{-1}w
       =\frac{\det M[1\leftarrow w]}{\det M}},
\qquad N\ge3,                                    \tag{17}
$$

where `M[1 <- w]` replaces the first column of `M` by `w`. Also `T_2=1`.
Every coefficient of (15)--(17) is specified by the finite sum (5).

**Proof.** Pin the boundary values at all corners to zero and at the orbit
of `b_{N-1}` to `S_N`, whose value is known from (2). The remaining finite
Dirichlet problem is uniquely solvable: the irreducible chain hits this
nonempty pinned set with finite mean. Eliminating its interior coordinates
using their killed Green function yields (12). Equations (13) then give
`M(t_1,...,t_n)^T=w`. This also proves nonsingularity directly, since a
solution of the homogeneous boundary system would extend to a solution of
the homogeneous full Dirichlet problem, which is zero by the maximum
principle. Equivalently, `M` is a nonsingular M-matrix Schur complement.
The actual hitting-time function has the pinned values, so its boundary
values are this unique solution. Cramer's rule proves the determinant
identity. For `N=2`, the two noncorner types are cyclic rotations, and
absorption occurs at rate one, giving `T_2=1`. $\square$

Equation (14) is not used to solve (17); it is an independent residual check.
The apparent complex coefficients in (5) are rational at `alpha=0`: they
solve a finite Dirichlet system with integer coefficients. Our exact audit
also checks rationality directly in `Q(omega)` rather than discarding an
imaginary or algebraic remainder numerically.

## 4. The full first-passage Laplace transform

Let `alpha>=0`, put `K^(alpha)_{a,c}=H_c^(alpha)(g_a)`, and define the
`(N-1)` by `(N-1)` matrix `A(alpha)` by the following equations for `f`:

$$
(A(\alpha)f)_a=(\alpha+2)f_a
 -\mathbf1_{\{a\ge2\}}f_{a-1}
 -\sum_{c=1}^{N-2}K^{(\alpha)}_{a,c}f_{c+1},
\quad 1\le a\le N-2,                              \tag{18}
$$

$$
(A(\alpha)f)_{N-1}
=(\alpha+2)f_{N-1}-f_{N-2}-f_1.                    \tag{19}
$$

When two indices in (19) coincide, their contributions are both retained.

**Theorem 3 (first-passage law).** `A(alpha)` is nonsingular for `alpha>=0`,
and

$$
\boxed{\mathbb E_{(N-1,0,1)}e^{-\alpha\tau}
 =e_1^{\mathsf T}A(\alpha)^{-1}e_1
 =\frac{\det A(\alpha)_{\widehat1,\widehat1}}
        {\det A(\alpha)}}.                        \tag{20}
$$

For `N=2` the transform is `1/(1+alpha)`. The convention for a zero-order
determinant is one, though the displayed `A` construction is for `N>=3`.

**Proof.** Give the corners value one. In the interior the discounted
Markov property and (6) reconstruct the transform as
`sum_c H_c^(alpha)(g) f_{c+1}`. On `b_a`, a first rate-two jump occurs after
an exponential holding time, so multiplying its discounted first-step
equation by `alpha+2` gives (18). The corner jump from `b_1` contributes the
sole source term, one. Both jumps from `b_{N-1}` land on boundary orbits,
giving (19). The full discounted Dirichlet problem is uniquely solvable;
the maximum principle for `alpha-Q_0` proves uniqueness for `alpha>0`, and
absorption proves it at zero. Its Schur complement `A(alpha)` is therefore
nonsingular, and `A(alpha)f=e_1`. The inverse cofactor identity gives (20).
For `N=2`, the hitting time is exponential of rate one. $\square$

Thus the representation specifies more than just the first moment. It does
not require unknown Bethe roots, a stationary-measure ansatz, or a solve on
the full triangle. For rational `alpha`, its boundary entries and transform
are rational, despite their Fourier form. Derivatives at zero determine all
moments; no large-`N` limit is inferred from differentiating this finite
formula.

## 5. FFT assembly and computational scope

For `u,v` modulo `N`, define

$$
G_N^{(\alpha)}(u,v)=\frac1{N^2}
\sum_{\substack{0\le k,\ell<N\\(k,\ell)\ne(0,0)}}
\frac{\omega^{ku+\ell v}}
 {\alpha+3-\omega^{-k}-\omega^{-\ell}-\omega^{k+\ell}}.
\tag{21}
$$

The constant mode is set to zero. At zero discount it is the only vanishing
denominator; at positive discount it can still be omitted because the
alternants below annihilate it.

For each `a`, permute the three entries of `(0,a,-1)`. For a permutation
`p`, let

$$
u_{a,p}=x_{p(1)}-x_{p(3)},\quad
v_{a,p}=x_{p(2)}-x_{p(3)},\quad s_p=\operatorname{sgn}(p).
$$

Then

$$
\boxed{K^{(\alpha)}_{a,c}=\frac16
 \sum_{p,q\in S_3}s_p s_q\,
 G_N^{(\alpha)}(u_{a,p}-u_{c,q},\,v_{a,p}-v_{c,q}).} \tag{22}
$$

**Proof.** Replace the unordered momentum-zero triples in (5) by ordered
`(k,ell,-k-ell)` triples. Each distinct-mode triple appears six times.
Repeated-mode determinants vanish, so they may be included without changing
the sum. Expanding both determinants yields the 36 signed terms in (22),
with the exponent differences displayed there. Their zero-frequency term
vanishes as well. Formula (21) is exactly the inverse two-dimensional
discrete Fourier transform of its stated reciprocal eigenvalues. $\square$

A two-dimensional FFT computes (21) in `O(N^2 log N)` operations; (22)
takes 36 lookups and signed additions per matrix entry. A dense boundary
solve then takes `O(N^3)` operations and `O(N^2)` storage. These are conventional
real/complex arithmetic counts. They are not claims about rational bit
complexity, uniform numerical conditioning, or a lower bound on other
possible algorithms. The old dense block-Schur implementation has
`O(N^4)` ordinary arithmetic under ordinary dense block elimination.

`fft_boundary.py` implements (21)--(22) and the mean system. Its residuals
are diagnostics, not certified forward-error bounds. `exact_boundary.py`
implements (5) with rational polynomial arithmetic modulo the cyclotomic
polynomial, then solves only the rational boundary system. The latter is a
small-size exact reference implementation, not an optimized large-`N`
bit-complexity algorithm.

## 6. Exact audit and scope of the conclusion

Run:

```sh
python3 verify.py
python3 verify_laplace.py
python3 exact_boundary.py 12
python3 fft_boundary.py 40 80 160 320
```

The first three commands need only the Python standard library; the last
needs NumPy. The exact mean audit checks `N=2,...,12`, including:

* 1,705 harmonic-measure equations, with exact rationality, nonnegativity and
  normalization;
* 220 interior polynomial equations;
* 418 original noncorner hitting-time Poisson equations on the reconstructed
  full function;
* 5,863 collision-channel multiplicity checks, including `N=3`;
* every archived `T_N` value in this range, as regression fixtures for the
  **new** formula.

The discounted audit checks all original discounted Poisson equations for
`N=2,...,10` at `alpha=0,1/2,1,2`: 1,020 exact equations. It also checks all
reconstructed values lie in `[0,1]`. These computations supplement the
all-`N` proofs; they do not replace them. No previous stationary solver,
full-triangle Poisson solver, or old theorem verifier was rerun.

The original finite-three-vacancy current is consequently computable by
substituting (17) into the already proved identity

$$
c_N=\lim_{p\uparrow1}\frac{J_{N,3}(p)}{1-p}
=\frac{3N}{(N+2)(N+3)}
 \left[1+\frac{2}{(N+1)(1+T_N)}\right].             \tag{23}
$$

The reduction to (23), the cubic identity, and the quadratic bounds on `T_N`
are inherited results, not proved anew here. The new formula does **not**
establish existence or a value of `lim T_N/N^2`. It does not determine the
function `Q(eta)`, decide the possible critical density, eliminate affine
phase gaps, or justify interchanging the thermodynamic and rare-braking
limits. These remain the specific barriers to the broader project.
