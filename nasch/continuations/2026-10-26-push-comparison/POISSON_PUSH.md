# Earlier continuous-time pushing comparison

This is the first, weaker comparison from this run. The synchronous
comparison in [README.md](README.md), completed on 27 October, removes
its logarithmic factor and proves a dense-traffic asymptotic uniformly
over all nonbraking probabilities. The argument here remains valid and
is preserved with its original audit. Its statements about the dynamic
comparison are strengthened in DYNAMIC_REDUCTION.md.

26 October 2026, continuation 22, following commit
`146dab8e50d54298b2a2fe019871e7290905dc06`.

These are complete analytic results with exact finite audits. They are
AI-assisted, not independently peer-reviewed or formally certified.
The general stationary NaSch flow and unrestricted identification of its
first-order coefficient at fixed positive vacancy density remain open.

## 1. New results

Write epsilon=1-p for the probability of **nonbraking**, N for the number
of cars, H for the number of vacant cells, U for stationary mean velocity
per car, and `J=N U/(N+H)` for road current.

**Theorem 1 (pushing upper comparison).** For every N>=2, 1<=H<N,
0<epsilon<1, and every stationary law of the full parallel-update NaSch
model with maximum speed two,

\[
\boxed{U\le[-\log(1-\epsilon)]\,{H\over N-H+1}.}     \tag{1}
\]

Combining this with the previously proved one-speed lower comparison gives

\[
\boxed{
{\epsilon H\over N+H-1}\le U
 \le {[-\log(1-\epsilon)]H\over N-H+1}.}            \tag{2}
\]

In particular, at every fixed vacancy-to-car density eta<1 the velocity
is of order epsilon, uniformly in road size. The possibility
`U/epsilon->infinity`, previously requiring unusual moving blocks, is now
excluded throughout this density range. This is a bound, not the exact
first-order coefficient.

**Corollary 2 (an unrestricted dense-traffic asymptotic).** Let
`delta=H/(N+H)` be the vacancy fraction on the road. Along every sequence
with H>=1, `H/N->0`, and `epsilon->0`,

\[
\boxed{\quad {J\over\epsilon\delta}\longrightarrow1.\quad} \tag{3}
\]

There is no condition on epsilon N or epsilon H. This is a limit in
which vacancy density also tends to zero, not the remaining fixed-eta
problem. An explicit error bound is given below.

**Theorem 3 (unrestricted local dynamic reduction).** In the full
project range `N->infinity`, `H/N->eta in (0,2)`, `epsilon->0`, all
subsequential stationary local limits extend to local finite-dimensional
distributions in time: observing the gaps at discrete times
`floor(t/epsilon)` gives the continuous-time backchip process started
from the corresponding limiting gap law. No epsilon N restriction is
needed. The precise coupling and error estimate are proved in
[DYNAMIC_REDUCTION.md](DYNAMIC_REDUCTION.md).

Theorem 3 concerns bounded observations at finitely many car labels and
times. It is not convergence of unbounded displacement/current observables,
nor a claim of convergence in a path-space topology.

## 2. A monotone upper update for the original traffic rule

Use integer lifted heights with

\[
h_{i+1}-h_i=g_i,\qquad h_{i+N}=h_i+H.
\]

For a fresh Bernoulli(epsilon) mask xi, the original rule is

\[
h_i'=h_i+c_i+\xi_i\mathbf1_{\{g_i\ge1\}},\qquad
c_i=\mathbf1_{\{v_i>0,g_i\ge2\}}.
\]

Define a memoryless upper map A_xi by replacing c_i with
`1{g_i>=2}`. The original next height is at most A_xi(h), coordinatewise.
For fixed xi its coordinate map is

\[
(A_\xi h)_i=
\begin{cases}
\max\{h_i,\min(h_i+1,h_{i+1}-1)\},&\xi_i=0,\\
\min(h_i+2,h_{i+1}),&\xi_i=1.
\end{cases}                                        \tag{4}
\]

Each expression is nondecreasing in both input heights. Thus A_xi
preserves coordinatewise order on ordered lifts. No monotonicity of the
original process in its stored velocities is asserted or needed.

## 3. An exactly solvable pushing upper process

An auxiliary height profile y has binary gaps
`b_i=y_(i+1)-y_i in {0,1}` with sum H. Such profiles exist when H<N.
A push event at site i does nothing if b_i=0. If b_i=1, it moves one
unit to i-1, and recursively moves a unit from every overfull site to its
predecessor until a vacant binary site is filled. Equivalently, find the
consecutive run of ones starting at i and extending in the direction
i-1: all their heights increase by one. The final gap word remains binary.

At each site put a Poisson clock of rate

\[
\lambda=-\log(1-\epsilon)>0.
\]

The binary gap law uniform over the `binom(N,H)` words with H ones is
stationary for this process. Here is a direct proof. Every word has H
nontrivial outgoing marked-site events. For a target word, an incoming
event leaves a zero at its marked site i. The previous zero may have
been any site in the consecutive run of ones immediately preceding i.
The total lengths of those runs over target zero sites equal H. Thus
incoming and outgoing rates, counting multiplicities, both equal lambda H.
This proves uniform stationarity. It is the familiar homogeneous
drop-push process; the comparison with NaSch, not the auxiliary model's
existence, is the contribution here.

An event at a uniformly sampled site moves k heights if exactly k
consecutive ones are encountered before the first zero. Hence its mean
total height increment is

\[
\sum_{k=1}^{H}{(H)_k\over(N)_k}={H\over N-H+1}.      \tag{5}
\]

To verify the sum without an independence assumption, expose a uniformly
random permutation of H successes and N-H failures. The successes are
split into N-H+1 exchangeable runs before, between, and after the
failures. Their expected lengths all equal H/(N-H+1), and the first
run has the tail probabilities in (5).

There are N clocks of rate lambda. The stationary mean increase per
height per unit time is therefore

\[
V_{\rm push}=\lambda H/(N-H+1).                    \tag{6}
\]

## 4. Pathwise domination and proof of Theorem 1

Couple the original discrete mask on time step n to the auxiliary Poisson
events during (n,n+1]: set xi_i(n)=1 precisely when site i has at least
one event there. These masks are independent over sites and steps and
have exactly the required Bernoulli(epsilon) law.

Suppose the auxiliary profile y(n) dominates the full traffic profile
h(n). The upper map and (4) give

\[
h(n+1)\le A_\xi h(n)\le A_\xi y(n).
\]

Because y(n) has binary gaps,
`(A_xi y(n))_i=y_i(n)+xi_i b_i(n)`. The complete auxiliary event
sequence in (n,n+1] dominates this profile. Indeed, take a site with
xi_i=b_i(n)=1. If its height has already increased before its first
own event, the required increase has occurred. Otherwise its own height
is unchanged and its leader's height has not decreased, so its gap is
still at least one. Its own event then increases that height. This
argument holds for every site and for every ordering and multiplicity
of Poisson events. Therefore

\[
h(n+1)\le y(n+1).                                  \tag{7}
\]

To initialize the comparison, draw a binary gap word uniformly and
independently of the stationary full-model state. Choose lifts for both,
and translate the auxiliary heights upward until they dominate the full
heights. The difference of two lifts with the same total H is N-periodic,
so a finite vertical translation suffices. Its expected cost is finite
at fixed N,H. A vertical translation does not change the binary gaps or
their stationary law.

Iterate (7). Stationarity of the original velocities makes its expected
mean-height increase in n updates equal to nU. The pushing gap law is
stationary, so (6) makes the auxiliary expected mean-height increase
equal to n V_push. Divide the height inequality by n and let n tend to
infinity. The finite initial translation cost disappears, proving (1).

The lower half of (2) is exactly the previously established
[one-speed lower comparison](../2026-10-26-local-clusters/UNIFORM_LOWER_BOUND.md),
after converting road current to mean car velocity. It is not counted
as a new theorem here.

## 5. Uniform first-order control and the dense-traffic law

Write eta=H/N. Inequality (2) is equivalent to

\[
{1\over1+\eta-1/N}
\le {U\over\epsilon\eta}={J\over\epsilon\delta}
\le {\lambda/\epsilon\over1-\eta+1/N}.             \tag{8}
\]

For 0<epsilon<1,

\[
1\le{\lambda\over\epsilon}
\le1+{\epsilon\over2(1-\epsilon)},                 \tag{9}
\]

because the terms of `lambda-epsilon=sum_(k>=2) epsilon^k/k` are at
most those of `epsilon^2/[2(1-epsilon)]`. Thus, for eta<1,

\[
\boxed{
\left|{J\over\epsilon\delta}-1\right|
\le{\eta+\epsilon/[2(1-\epsilon)]\over1-\eta}.}    \tag{10}
\]

For the lower side, (8) gives a possible deficit at most eta; for the
upper side, use (9) and discard the positive 1/N in its denominator.
This proves (10) and Corollary 2.

At fixed eta in (0,1), (8) only supplies an interval for the coefficient.
For arbitrary joint size/noise sequences with H/N->eta,

\[
{\eta\over(1+\eta)^2}
\le\liminf {J\over\epsilon}
\le\limsup {J\over\epsilon}
\le {\eta\over(1+\eta)(1-\eta)}.                   \tag{11}
\]

It does not prove equality of the liminf and limsup. For eta<=R<1 and
epsilon<=1/2, (1) also gives

\[
U\le {2R\over1-R}\epsilon.                         \tag{12}
\]

The local-generator and dynamic-reduction errors from continuation 21
therefore improve from order epsilon^(1/3) to order epsilon in this
density range. The remaining range 1<=eta<2 is not covered by the
uniform first-order estimate. A binary auxiliary gap profile with mass
H>N cannot exist, so the same comparison cannot simply be extended there.

## 6. Audits, provenance, and remaining work

`verify_push.py` implements the original four traffic-update steps and
the pushing map independently. It passed 297,992 pathwise mask/order
comparisons, including 5,440 seeded larger event-order examples. Exact
incoming counts check 8,166 auxiliary binary states and 89,958 transitions;
66 rational identities verify (5). A separate 50-member family tests the
positive transport-amplification obstruction described in
[CLOSURE_ATTEMPTS.md](CLOSURE_ATTEMPTS.md).

The auxiliary drop-push model is established mathematics; for primary
context see Li and Saenz,
[*Contour Integral Formulas for PushASEP on the Ring*](https://arxiv.org/abs/2308.05372).
The proof above is self-contained and does not import a Bethe-ansatz
formula. No claim of priority for the comparison has been established.

The [dynamic theorem](DYNAMIC_REDUCTION.md) gives additional new results
and exact audits. The [audit](AUDIT.md) and [handoff](HANDOFF.md) preserve
the scope. The complete fixed-density stationary-flow problem, residual
phase/condensate alternatives, and unrestricted first-order interchange
are not claimed solved.
