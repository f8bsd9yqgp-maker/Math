# A size-uniform lower bound for full NaSch traffic

26 October 2026. This continuation gives a one-sided bound valid without
the joint-limit restriction in README.md. The one-speed parallel-exclusion
model and its stationary product construction are established mathematics;
the comparison with the present full `v_max=2` traffic model is proved
below. No claim of priority is made. See, for example, the primary-source
[exact-solution record for one-speed traffic with open boundaries](https://edoc.mdc-berlin.de/id/eprint/9383/).

For `N>=2`, `H>=1`, and `0<epsilon=1-p<1`, let `U` and `J` be the mean
velocity and traffic current of **any** stationary full-model law, with
`J=N U/(N+H)`. Put `L=N+H`.

**Theorem 1.** For every road size and every such braking parameter,

\[
\boxed{{U\over\epsilon}\ge {H\over N+H-1},\qquad
       {J\over\epsilon}\ge {NH\over L(L-1)}.}       \tag{1}
\]

More precisely, with

\[
Z_{N,H}=\sum_{k=1}^{\min(N,H)}
 \binom Nk\binom{H-1}{k-1}p^{-k},
\]

\[
{U\over\epsilon}\ge
{\sum_k k\binom Nk\binom{H-1}{k-1}p^{-k}\over NZ_{N,H}}.\tag{2}
\]

If `H/N->eta>0` and `epsilon` is fixed in `(0,1)`, then every sequence of
stationary full-model currents satisfies

\[
\liminf_{N\to\infty}J_{N,H}(1-\epsilon)
\ge {1-\sqrt{1-4\epsilon\eta/(1+\eta)^2}\over2}.    \tag{3}
\]

For **any** sequence `epsilon_N in (0,1)`, including one tending to zero
arbitrarily slowly, (1) gives

\[
\liminf_{N\to\infty}{J_{N,H}(1-\epsilon_N)\over\epsilon_N}
 \ge {\eta\over(1+\eta)^2}.                        \tag{4}
\]

These are one-sided bounds. They do not establish that the full-model
thermodynamic limit exists, identify its value, or justify interchange.

## 1. Pathwise height comparison

Use the same independent `Bernoulli(epsilon)` coins in the full model and
in a one-speed process. A one-speed car moves one unit iff its coin is one
and its gap is nonzero. Let `h_i` and `z_i` be lifted car heights of the
full and one-speed processes, respectively, with periodic increment `H`.

The one-speed update is

\[
z_i'=\min(z_i+\xi_i,z_{i+1}).                      \tag{5}
\]

It is coordinatewise monotone. The full update satisfies
`w_i>=xi_i 1{g_i>=1}`, and therefore

\[
h_i'\ge\min(h_i+\xi_i,h_{i+1}).                    \tag{6}
\]

If the two processes start with equal heights, induction using (5)-(6)
gives `h_i(t)>=z_i(t)` for every car and every time. This is a valid
comparison with the one-speed process; it is not a claim that two full
NaSch processes are ordered under different nonbraking coins.

Start the full process under a stationary law and the one-speed process
from the same initial gaps. Sum the pathwise displacements over the cars,
take expectations, and divide by `Nt`. The one-speed gap chain on a
finite ring is irreducible and aperiodic for `0<epsilon<1`: single-particle
transfers have positive probability and the all-braking step is a self-loop.
Letting `t->infinity` proves `U>=U_1`, the one-speed stationary mean
velocity. The initial full law need not be translation invariant.

## 2. One-speed stationary law on the gap ring

The one-speed process chips one particle from each nonempty gap with
probability `epsilon`, simultaneously, and sends it to the preceding site.
Its stationary gap law is proportional to

\[
\prod_{i=0}^{N-1}f(g_i),\qquad
f(0)=1,\quad f(m)=p^{-1}\ (m\ge1),\quad\sum_i g_i=H.\tag{7}
\]

For a direct check, let the chip be `s_i in {0,1}`, let the residual mass
be `r_i=g_i-s_i`, and put `v(0)=1`, `v(1)=epsilon/p`. Then

\[
f(g_i)\Pr(s_i\mid g_i)=v(s_i)\quad(0\le s_i\le g_i).
\]

Thus the unnormalized joint weight of all residuals and chips factors as
`prod_i v(s_i)`, subject only to nonnegative residuals and the total mass.
The parallel transfer cyclically permutes the chip variables relative to
the residual variables. Summing over all chips at each new site gives
the same factors `f`, proving invariance. The finite irreducible chain has
this unique stationary distribution.

Write `K` for the number of nonempty gaps. The number of compositions
of `H` into `N` nonnegative gaps with exactly `k` nonempty parts is
`binom(N,k) binom(H-1,k-1)`. Hence its distribution is proportional to
the terms in `Z_(N,H)`, and the one-speed velocity is
`U_1=epsilon E K/N`. This proves (2).

At `p=1`, the same compositions are uniform, and the expected fraction of
nonempty gaps is `H/(N+H-1)`. The factor `p^(-K)` in (7) is nondecreasing
in `K`, so nonnegative covariance with `K` makes `E K` no smaller than
under the uniform composition law. This proves (1). The use of `p=1`
here is only an auxiliary reference distribution; (1) itself is stated
for positive `epsilon`.

## 3. Thermodynamic expression for the comparison bound

For fixed `epsilon in (0,1)` let `H/N->eta>0` and let `w_k` be the kth
term in `Z_(N,H)`. The successive-term ratio is

\[
{w_{k+1}\over w_k}={(N-k)(H-k)\over p\,k(k+1)}.    \tag{8}
\]

For `k/N->x` in the interior of `[0,min(1,eta)]`, the ratio converges to
`(1-x)(eta-x)/(p x^2)`, which decreases strictly from infinity to zero.
Its unique value-one point is the smaller root

\[
x_\epsilon={1+\eta-\sqrt{(1+\eta)^2-4\epsilon\eta}\over2\epsilon}.
\]

For each fixed `delta>0`, (8) is bounded uniformly above by a constant
less than one on the region `k/N>=x_epsilon+delta`, and bounded below by a
constant greater than one on `k/N<=x_epsilon-delta`, once `N` is large.
Comparing consecutive terms gives exponentially small tails on both
sides. Thus `K/N->x_epsilon` in probability and, because `K/N<=1`, also
in expectation. Equation (3) follows by multiplying the limiting
one-speed mean velocity `epsilon*x_epsilon` by `N/(N+H)`.
Equation (4) follows directly from the finite-size inequality (1), with
no limit interchange or convergence hypothesis on the full traffic law.

## 4. Audit and exact scope

`python3 verify_unit_lower.py` checks the product invariance identity for
12,348 exact rational transitions and the ordered one-step comparison
for 470,240 finite cases. It performs no stationary-system solve; the
invariant weights in (7) are supplied by the proof. Results are in
`results/unit_lower.json`. These finite checks do not replace the analytic
arguments or independent peer review.

`verify_unit_flow_fixtures.py` also verifies the stronger exact finite-size
comparison (2) against all four archived rational traffic currents, with
four Bernstein-polynomial certificates on the entire range `0<=p<=1`.
This uses the old current formulas as fixtures and does not re-solve them;
the theorem above is stated for `0<p<1`.

The comparison does not decide whether moving condensates occur. It gives
a positive current lower bound on the `epsilon` scale uniformly in road
size and strengthens with (3) at fixed `epsilon`. It supplies no matching
upper bound or explicit general full-model stationary flow.
