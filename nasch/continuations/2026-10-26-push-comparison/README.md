# A synchronous pushing bound and a uniform dense-traffic law

Continuation 22, started 26 October and completed 27 October 2026.
Parent commit: `146dab8e50d54298b2a2fe019871e7290905dc06`.

These results have complete analytic proofs and exact finite audits.
They are AI-assisted, not independently peer-reviewed or formally
certified. The general stationary traffic-flow formula at fixed positive
vacancy density, the residual phase/condensate alternatives, and unrestricted
identification of the first-order current remain unresolved.

## 1. Main results

Let N be the number of cars, H the number of vacant road cells,
`epsilon=1-p` the probability of **nonbraking**, U the stationary mean
velocity per car, and `J=N U/(N+H)` the current per road cell. Write
`eta=H/N` and `delta=H/(N+H)`.

**Theorem 1 (synchronous pushing upper bound).** For every N>=2,
1<=H<N, 0<epsilon<1, and every stationary law of the original
parallel-update NaSch model with maximum speed two,

\[
\boxed{
U\le \epsilon\sum_{k=1}^{H}p^{k-1}{(H)_k\over(N)_k}
\le {\epsilon\eta\over1-p\eta}.}                 \tag{1}
\]

Here `(a)_k=a(a-1)...(a-k+1)` is a falling factorial. The first upper
bound is a finite polynomial, not a stationary-flow equality. It also
obeys

\[
U\le {\epsilon H\over N-H+1}.                     \tag{2}
\]

This improves the initially obtained
`[-log(1-epsilon)]H/(N-H+1)` bound, whose independent proof and checks
are preserved in [POISSON_PUSH.md](POISSON_PUSH.md).

Combining (1) with the inherited one-speed lower comparison gives

\[
\boxed{{\epsilon H\over N+H-1}\le U
       \le{\epsilon\eta\over1-p\eta}.}            \tag{3}
\]

In particular, for eta<=R<1, `U<=epsilon R/(1-R)` uniformly in N.
This rules out a divergent normalized current in this range. It does
not determine its exact fixed-density coefficient.

**Corollary 2 (dense traffic, uniformly over braking probability).**
Along every sequence with H>=1, H/N->0, and arbitrary
`epsilon in (0,1)`, even if epsilon varies with N,

\[
\boxed{{J\over\epsilon\delta}\longrightarrow1.}    \tag{4}
\]

No small-noise assumption or condition on epsilon N is needed. More
precisely, for every finite system in Theorem 1,

\[
\boxed{\left|{J\over\epsilon\delta}-1\right|
       \le{\eta\over1-\eta}.}                    \tag{5}
\]

This resolves a boundary-density regime, not fixed eta>0.

**Theorem 3 (local dynamic reduction).** Throughout eta in (0,2),
every subsequential stationary zero-noise local gap limit extends to
the finite-dimensional distributions of the continuous-time backchip
process on the time scale `t/epsilon`, with no epsilon N restriction.
The proof in [DYNAMIC_REDUCTION.md](DYNAMIC_REDUCTION.md) supplies a
coupling with local observation error of order `epsilon^(1/3)(1+T+T^2)`
at each observation time T, improved to `epsilon(1+T+T^2)` when eta<=R<1. Its proof uses a
one-sided discrepancy cone to obtain a polynomial, rather than
exponential, time dependence. The statement concerns bounded local
observations; it does not pass an unbounded displacement through a limit.

## 2. A monotone upper map for the full traffic update

Use lifted integer heights

\[
h_{i+1}-h_i=g_i,\qquad h_{i+N}=h_i+H.
\]

For a fresh independent Bernoulli(epsilon) mask xi, the original four
traffic steps give

\[
h_i'=h_i+c_i+\xi_i\mathbf1_{\{g_i\ge1\}},\qquad
c_i=\mathbf1_{\{v_i>0,g_i\ge2\}}.
\]

Replace c_i by `1{g_i>=2}` to define an upper map A_xi. Explicitly,

\[
(A_\xi h)_i=
\begin{cases}
\max\{h_i,\min(h_i+1,h_{i+1}-1)\},&\xi_i=0,\\
\min(h_i+2,h_{i+1}),&\xi_i=1.
\end{cases}                                        \tag{6}
\]

Each expression is nondecreasing in both input heights. Hence the
actual update is at most A_xi(h), and A_xi preserves coordinatewise
order. No monotonicity of the original stored-velocity dynamics is
assumed.

## 3. A synchronous pushing process with binary gaps

Let y have binary gaps `b_i=y_(i+1)-y_i in {0,1}`, with H ones and
N-H zeros. Since H<N every run of ones is bounded by zeros.

Use the same independent mask xi. In each run of ones, locate its
rightmost marked site j, if any. Increase by one all y_i from the
leftmost site of that run through j; leave all other y_i unchanged.
Write these increments as s_i. Equivalently, around the ring,

\[
s_i=b_i\max\{\xi_i,s_{i+1}\},\qquad s_i\in\{0,1\}.
                                                               \tag{7}
\]

The zeros make this recurrence unambiguous. The new gaps are
`b_i'=b_i+s_(i+1)-s_i`, still binary: if b_i=0 then s_i=0; if b_i=1,
then s_i>=s_(i+1). Total mass stays H. Moreover,

\[
y_i'=y_i+s_i\ge y_i+\xi_i b_i=(A_\xi y)_i.        \tag{8}
\]

This is one synchronous update, not a sequential list of all marked
pushes. Multiple marks in the same run do not cause multiple moves
of an individual height.

## 4. Exact uniform stationary law for the auxiliary process

We give a self-contained factorization proof. View the M=N-H zero
sites as cyclically ordered, labelled holes. Let L_j be the number of
ones between hole j and the next hole, so `sum_j L_j=H`. Hole j advances
K_j sites under (7). Conditional on the L_j, these movements are
independent because their marks lie in disjoint runs, and

\[
\Pr(K_j=k\mid L_j=L)=
\begin{cases}
p^L,&k=0,\\
\epsilon p^{L-k},&1\le k\le L.
\end{cases}                                        \tag{9}
\]

The gap update in these coordinates is
`L_j'=L_j-K_j+K_(j+1)`. Define `v(0)=1`, `v(k)=epsilon` for k>=1,
and `w(r)=p^r`. For every integer L>=0,

\[
\sum_{k=0}^L v(k)w(L-k)=p^L+\epsilon\sum_{r=0}^{L-1}p^r=1. \tag{10}
\]

If L is uniform over all weak compositions of H into M parts, its
joint weight with the chosen movements, writing `R_j=L_j-K_j`, is

\[
Z^{-1}\prod_j v(K_j)w(R_j),\qquad
Z=\binom{H+M-1}{M-1}.
\]

For a prescribed target composition L', sum this expression over
all decompositions `L_j'=R_j+K_(j+1)`. Reindex the product of v terms.
Equation (10) makes the result exactly `Z^(-1)` for every L'. Thus
the uniform composition law is invariant, including M=1.

To recover a stationary binary word, choose the position of labelled
hole 1 uniformly among the N sites, independently of L. After its
increment K_1 its position is still uniform and independent of L',
because the increment depends only on L and the relative marks, not
on this uniform position. Each binary word has exactly M possible
choices for labelled hole 1. Consequently the induced law is uniform
over the `binom(N,H)` binary words, and is invariant under (7).

This proves the auxiliary stationary law only. It is not a uniform or
product-law claim for the original NaSch gaps or reduced backchip gaps.

## 5. Its exact speed and pathwise domination

Under the uniform binary law, the probability that k prescribed
consecutive sites are all occupied equals `(H)_k/(N)_k`. At a given
site i, let R_i be the length of its run of ones in the direction
i,i+1,...; take R_i=0 when b_i=0. Given this run, its height increases
with probability `1-p^(R_i)`. Expanding the finite geometric sum gives

\[
\mathbb E s_i
=\epsilon\sum_{k=1}^H p^{k-1}\Pr(R_i\ge k)
=\epsilon\sum_{k=1}^H p^{k-1}{(H)_k\over(N)_k}.    \tag{11}
\]

Draw the auxiliary binary gap word in its uniform stationary law,
independently of the full stationary traffic state. Choose lifts with
the same slope H/N. Translate the auxiliary heights upward by a finite
integer until y>=h. This is possible because their difference is
N-periodic; with fixed N,H the required initial offset has a finite
expectation. In fact choose h_0=y_0=0 before translating: every coordinate
in a fundamental period lies between 0 and H, so translation by H
always suffices. It does not affect gap dynamics or stationarity.

Use the same fresh masks in both processes. Equations (6) and (8) give

\[
h(n+1)\le A_{\xi(n)}h(n)
\le A_{\xi(n)}y(n)\le y(n+1).
\]

Induction proves domination at every integer time. Expected mean-height
increments per step equal U for the full stationary law and (11) for
the auxiliary stationary law. Divide their accumulated height inequality
by n and send n to infinity. The initial offset disappears. This proves
the first part of (1), without assuming uniqueness of the full law.

For each k, `(H)_k/(N)_k<=eta^k`, since every successive factor is at
most H/N. Summing the geometric series proves the second part of (1).
Alternatively discard `p^(k-1)` and use
`sum_(k=1)^H (H)_k/(N)_k=H/(N-H+1)` to prove (2). The latter identity
is the expected length of the initial success run in a uniformly
permuted string with H successes and N-H failures.

## 6. The dense-traffic squeeze

The earlier [one-speed lower comparison](../2026-10-26-local-clusters/UNIFORM_LOWER_BOUND.md)
gives the lower bound in (3). Dividing (3) by epsilon eta gives

\[
{1\over1+\eta-1/N}
\le {U\over\epsilon\eta}={J\over\epsilon\delta}
\le {1\over1-p\eta}.                              \tag{12}
\]

Because H>=1, the lower denominator is at least one, and its possible
deficit from one is at most eta. The upper excess is
`p eta/(1-p eta)<=eta/(1-eta)`. This proves (5) and the uniform limit
(4). No interchange of a fixed-positive-density thermodynamic limit
with a rare-event limit is used in this argument.

For fixed eta in (0,1) and epsilon->0, arbitrary joint size/noise
sequences instead give only

\[
{\eta\over(1+\eta)^2}
\le\liminf {J\over\epsilon}
\le\limsup {J\over\epsilon}
\le{\eta\over(1+\eta)(1-\eta)}.                   \tag{13}
\]

The bounds need not coincide. The comparison also does not extend
directly to eta>=1: its auxiliary profile would need more than N
binary gap units, and the zero that terminates each pushing run is
essential.

## 7. Verification and exact remaining scope

The new `verify_parallel_push.py` passed 137,312 exhaustive original-rule
mask comparisons and 7,800 seeded larger cases. It checked uniform
stationarity in 2,026 binary states through 86,516 transition masks,
verifying all 11,188 Bernstein coefficients rather than sampled
probabilities. Another 180 rational identities checked the reward and
its geometric upper bound.

The [dynamic proof](DYNAMIC_REDUCTION.md), [audit](AUDIT.md),
[closure-attempt record](CLOSURE_ATTEMPTS.md), and [handoff](HANDOFF.md)
preserve the other results, exact checks, and failed shortcuts. The
auxiliary process belongs to the established pushing/mass-transport
framework; no literature-priority claim is made for this comparison.
All invariant-law and domination calculations needed here are supplied
above. No old full stationary or first-passage solver was rerun.

For the established factorization framework used in Section 4, see
Evans, Majumdar and Zia, [*Factorised Steady States in Mass Transport
Models*](https://arxiv.org/abs/cond-mat/0406524). Applying that framework
to this auxiliary model does not assert factorization for NaSch.
