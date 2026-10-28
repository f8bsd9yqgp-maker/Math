# Frozen anchors identify the local integrated-current limit

27 October 2026. Continuation 23, following commit
`ae78d6f3897ef3560518ac38690d8346ede37273`.

This addresses the gap between the local dynamic reduction and current.
It proves convergence of finite-time integrated-current distributions,
not only gap distributions. It also gives a lower bound on every
subsequential normalized mean current and an exact uniform-integrability
criterion for passing to the mean. The general stationary flow formula
is **not** closed: the required mean-current tail estimate and stationary
law selection are not proved.

These are analytic, AI-assisted proofs with exact structural audits;
independent peer review and publication-priority review remain pending.

## 1. Notation and inherited inputs

Use N>=2 cars, 1<=H<2N vacancies, epsilon=1-p in (0,1/2], and
`lambda=-log p`. The full process starts in a stationary law averaged
over cyclic car-label shifts. Its gap and velocity at step k are g(k),
v(k). Write

\[
c_i(k)=\mathbf1_{\{v_i(k)>0,g_i(k)\ge2\}},\qquad
C=\mathbb P(c_0=1),\quad B=\mathbb P(c_0=1,c_1=0).
\]

Fresh Bernoulli(epsilon) coins give movements

\[
w_i(k)=c_i(k)+\xi_i(k)\mathbf1_{\{g_i(k)\ge1\}},\qquad
g_i(k+1)-g_i(k)=w_{i+1}(k)-w_i(k).
\]

The integrated full current at car i is its nonnegative displacement

\[
I_i(n)=\sum_{k=0}^{n-1}w_i(k).
\]

Let G_k be the exact full-braking gap projection of the full state.
Couple to the rate-one continuous-time backchip process Z(t), with
Z(0)=G_0, as in the preceding
[dynamic theorem](../2026-10-26-push-comparison/DYNAMIC_REDUCTION.md).
Its integrated current K_i(t) is the sum of all amounts
`d(Z_i)=Z_i-1{Z_i>=2}` transferred at the clock of i by time t.

For each full step, the nonbraking coin at i records whether its reduced
Poisson clock rang at least once in a corresponding interval of length
lambda. Consequently fresh masks have exactly the right distribution.

The inherited coupling gives

\[
{\mathbb E D(G_n,Z(n\lambda))\over N}\le\Delta_n,
\quad
\Delta_n=8\epsilon(C+2B/p+\epsilon)
             \left[n+{\lambda n(n-1)\over2}\right],           \tag{1}
\]

where D counts unequal gaps. At any site,
`P(g_i(0)!=G_i(0))<=2C` and
`P(g_i(n)!=Z_i(n lambda))<=2C+Delta_n`.
For H/N<=R, the existing arrest theorem gives
`C=O_R(epsilon^(1/3))`, `B<=R epsilon`. The new pushing bound improves
this to `C<=epsilon R/(1-R)` when R<1.

## 2. A frozen-anchor lemma

**Lemma.** Suppose c_j(0)=0 and the coin at j is braking in each of
steps 0,...,n-1. Then I_j(n)=0, irrespective of all other cars.

**Proof.** The first movement is zero by the displayed full update.
Its new velocity is therefore zero. At every later step a zero velocity
and a braking coin again give zero movement, regardless of the gap.
Induction proves the assertion. This includes an initially positive
stored velocity if its initial gap is less than two. Square.

If the reduced Poisson clock at j has no event in [0,n lambda], then
K_j(n lambda)=0 as well. Integrating the two conservation equations gives

\[
I_i(n)-I_j(n)=\sum_{a=i}^{j-1}\{g_a(0)-g_a(n)\},
\quad
K_i(t)-K_j(t)=\sum_{a=i}^{j-1}\{Z_a(0)-Z_a(t)\}.   \tag{2}
\]

Thus equality of endpoint gaps between i and a common frozen anchor
forces equality of the two integrated currents at i. There is no need
to resolve the rapid intermediate coasting steps.

## 3. Quantitative finite-ring current coupling

**Theorem 1.** For every integer 1<=L<N, the coupling above satisfies

\[
\boxed{
\mathbb P\{I_0(n)\ne K_0(n\lambda)\}
\le (1-e^{-n\lambda})^L+C+L(4C+\Delta_n).}          \tag{3}
\]

This controls the total-variation distance between these two integer
current distributions. It compares to the reduced process started from
G_0, not to its canonical stationary law.

**Proof.** Look at the distinct sites 1,...,L. Select the first j whose
Poisson clock has no event in [0,n lambda], if one exists. The probability
that no candidate exists is `(1-exp(-n lambda))^L`, because the clocks
are independent at these sites.

The candidate selection depends only on future clocks and is independent
of the initial full state. Cyclic stationarity therefore gives

\[
\mathbb P(j\hbox{ exists and }c_j(0)=1)
=C\,\mathbb P(j\hbox{ exists})\le C.               \tag{4}
\]

If a candidate exists and is initially unqualified, the lemma freezes
both currents at j. A union bound over the L gaps at sites 0,...,L-1,
using the two endpoint estimates after (1), bounds the probability of
any endpoint disagreement by `L(4C+Delta_n)`. On the complementary
event, (2) proves I_0(n)=K_0(n lambda). Summing these failure probabilities
proves (3). No independence of the endpoint gap errors is assumed.
Square.

For finitely many labels and times, apply (3) at each requested pair
and use a union bound. All use the same underlying coupling. One can
also use a candidate with no clock event up to the largest time to
freeze every requested earlier interval at once.

## 4. Unrestricted current-distribution reduction

**Theorem 2.** Let N_k->infinity, H_k/N_k->eta in (0,2), and
epsilon_k->0, with no condition on epsilon_k N_k. Along a subsequence
where the full stationary gaps have a local limit mu, the joint laws
of the full gaps and integrated currents at any finite set of car
labels and times `floor(t/epsilon_k)` converge to those of the stationary
backchip process with initial law mu and its integrated currents.

The gap marginal mu is the reduced-stationary law supplied by the
preceding dynamic theorem. It need not have mean eta or be a canonical
limit at eta.

**Proof.** For fixed bounded t, take n=floor(t/epsilon). The times n lambda
stay bounded. From (1), C+Delta_n tends to zero uniformly in road size.
Choose L tending to infinity slowly enough that L<N and
`L(C+Delta_n)->0`. Such a choice is possible for every joint sequence.
All three terms on the right of (3) then vanish.

Replacing n lambda by t in the reduced current adds a discrepancy
probability at most `|n lambda-t|`, because its current changes only
when its own rate-one clock rings. The elementary bound

\[
|n\lambda-t|\le\epsilon+n{\epsilon^2\over2p}
\]

shows this probability tends to zero.

The reduced currents from G_0 converge locally to those started from
mu. Here is the needed continuity argument. In a bounded time interval
there are finitely many clock events at each observed donor. Their
pre-event masses depend on a finite backward clock diagram almost
surely. The probability that this diagram reaches distance m tends to
zero with m, uniformly in all masses, by the ordered nearest-neighbor
clock bound. Inside a fixed diagram, current is a deterministic function
of finitely many integer initial gaps and finitely many events. Local
weak convergence on this discrete state space suffices for convergence
of every bounded function of its terminal current. Truncate the diagram
first, then remove the truncation. The same reasoning handles finitely
many donors and times, together with their gap observations. Square.

For the finite-ring comparison at a fixed bounded time, the rate in (3)
can be made explicit. If H/N<=R<2, put alpha=1/3; if R<1, put alpha=1.
There are constants depending on R and the time bound such that the
error is at most

\[
O_{R,T}\bigl(\epsilon^\alpha\log(1/\epsilon)\bigr)
       +\exp\{-e^{-2T}(N-1)\}.                  \tag{5}
\]

Indeed n lambda<=2T; use
`(1-exp(-n lambda))^L<=exp(-exp(-2T)L)` and choose L as the minimum
of N-1 and a sufficiently large constant times log(1/epsilon).
This rate compares to the finite reduced chain initialized by G_0;
it includes no asserted rate for convergence of initial laws to mu.

## 5. What now follows about stationary mean current

Write

\[
m=\mathbb E_\mu g_0\le\eta,\quad
q=\mu(g_0\ge2),\quad F_\mu=m-q.
\]

Since mu is stationary and has finite mean, the rate-one compensated
current formula, or direct conditioning on a clock event, gives
`E_mu K_0(t)=t F_mu`.

Let U_k denote full stationary mean velocity. Stationarity gives exactly
`E I_0(floor(t/epsilon_k))=floor(t/epsilon_k) U_k`.
The currents are nonnegative. Theorem 2 and truncation therefore prove

\[
\boxed{\liminf_k {U_k\over\epsilon_k}\ge F_\mu,
\qquad
\liminf_k {J_k\over\epsilon_k}
       \ge{m-q\over1+\eta}.}                    \tag{6}
\]

In particular, a mean-current defect relative to the limiting local
stationary law can only be nonnegative. This does not equate m with eta
or q with Q(eta).

There is also an equivalent statement about qualification. The exact
one-step identity is `U_k=C_k+epsilon_k P(g_0>=1)`. The latter bounded
probability converges locally, so (6) gives

\[
\boxed{\liminf_k {C_k\over\epsilon_k}
       \ge\mathbb E_\mu(g_0-2)^+.}               \tag{7}
\]

The identity `d(g)-1{g>=1}=(g-2)^+` verifies the right side. Equation
(7) is a lower bound, not equality of the active-car occupation time
with a reduced avalanche workload.

## 6. An exact criterion for the missing mean passage

**Theorem 3.** Along the local-limit subsequence in Theorem 2, for any
one fixed t>0, the following are equivalent:

1. `U_k/epsilon_k -> F_mu`.
2. The nonnegative random variables
   `I_0(floor(t/epsilon_k))` are uniformly integrable.

**Proof.** Theorem 2 supplies convergence in distribution to K_0(t),
whose mean is t F_mu. Uniform integrability then gives convergence of
the expectations, which is equivalent to item 1 since
`epsilon_k floor(t/epsilon_k)->t`.

Conversely suppose item 1. For every M, bounded continuous truncation
of these integer-valued variables gives
`E min(I_k,M)->E min(K_0(t),M)`. Their full means converge to E K_0(t),
so `lim_k E(I_k-M)^+=E(K_0(t)-M)^+`. This last expression tends to
zero as M->infinity. The inequality
`I_k 1{I_k>2M}<=2(I_k-M)^+` controls the tails for all sufficiently
large k, and finitely many earlier integrable variables cause no
problem. This proves uniform integrability. Square.

The variables in this criterion are **integrated displacements over
t/epsilon updates**, not instantaneous velocities divided by epsilon.
The latter converge to zero in probability in the arrest regime and
generally cannot be uniformly integrable if their means stay positive.

To obtain the proposed fixed-density formula from these results, one
still needs both the mean passage above and identification
`F_mu=eta-Q(eta)` for every selected subsequence. A sufficient, stronger
identification would be `m=eta` and `q=Q(eta)`. Neither condition is
proved here for arbitrary full-model joint limits.

The earlier warning that gap observations alone leave a common height
translation undetermined is overcome **in distribution** by the frozen
anchors. The remaining obstruction is now specifically the expectation
of rare large displacements, together with stationary law selection.
No unrestricted first-order interchange or general stationary-flow
equality is claimed.

See [AUDIT.md](AUDIT.md), [ATTEMPTS.md](ATTEMPTS.md), and
[HANDOFF.md](HANDOFF.md) for verification and the exact remaining task.
