# Uniform zero-noise arrest and an unrestricted local stationary reduction

26 October 2026, continuation 21. Complete analytic arguments are supplied,
with exact finite audits. These are AI-assisted research results, not
independently peer-reviewed or formally certified. Priority is unverified.

**New results.** The original parallel-update NaSch model with maximum
speed two has the size-uniform stationary bound

\[
\boxed{U\le(3+6R)(1-p)^{1/3}}                       \tag{1}
\]

whenever `N>=2`, `H/N<=R`, and `0<1-p<=1/2`. Here U is mean car velocity.
There is no assumption relating road size to `1-p`, and this bound does not
require `H<2N`. The same bound holds for every translation-invariant
infinite-volume stationary law with mean gap at most R.

In the project's range `0<eta<2`, every local subsequential limit of
stationary full-model laws with `N->infinity`, `H/N->eta`, and `p->1`
has all velocities zero, **and its gap marginal is stationary for the
continuous-time backchip reduction**. The second assertion is proved in
[LOCAL_STATIONARY_REDUCTION.md](LOCAL_STATIONARY_REDUCTION.md). It also has
no restriction on `(1-p)N` and assumes neither spatial ergodicity nor gap
uniform integrability.

This closes the possible positive-velocity component of the zero-noise
local limit and establishes the reduced stationarity of every such local
gap limit. It does **not** determine its density mixture, recover escaped
gap mass, or identify the current after division by `1-p`. The general
stationary-flow formula and unrestricted first-order interchange remain
open. The exponent `1/3` is an upper-bound exponent, not a proposed true
scaling exponent.

## 1. Model and a sharper finite-parameter bound

There are N cars and H vacant cells on a road of length N+H. Car i+1 is
ahead of i. Gaps are nonnegative integers with sum H, and stored
velocities are in `{0,1,2}`. Set

\[
\epsilon=1-p,\qquad
c_i=\mathbf1_{\{v_i>0,\ g_i\ge2\}},\qquad
o_i=\mathbf1_{\{g_i\ge1\}}.
\]

With fresh independent Bernoulli(epsilon) coins `xi_i`, the exact update is

\[
w_i=c_i+\xi_i o_i,\quad
g_i'=g_i+w_{i+1}-w_i,\quad v_i'=w_i.                \tag{2}
\]

A coin of one means **no random braking**. Thus the limit here is
near-certain braking, or rare nonbraking, not the conventional p->0 limit.

For a finite-ring stationary law, define the spatial averages

\[
\eta=H/N,\quad C={1\over N}\mathbb E\sum_i c_i,
\quad B={1\over N}\mathbb E\sum_i c_i(1-c_{i+1}).   \tag{3}
\]

No cyclic invariance of that law is needed. For an infinite-volume
translation-invariant stationary law, use `eta=E g_0<infinity`, `C=E c_0`,
and `B=E[c_0(1-c_1)]` instead. In either setting

\[
U=C+\epsilon\mathbb E_{\rm av}o_0\le C+\epsilon,
\qquad J={U\over1+\eta}                            \tag{4}
\]

for the finite-ring road current; the mean-velocity identity also holds
on the infinite line. The notation `E_av` means cyclic averaging on a ring.

**Theorem 1.** For every integer M>=2 and 0<epsilon<1,

\[
\boxed{
U\le \epsilon+(M-1)\epsilon\eta
 +{\epsilon(1+2\eta)M(M-1)\over2(1-\epsilon)}
 +{\eta\over M+1}.}                                \tag{5}
\]

Consequently (1) holds under its stated conditions. If H=0, the
stationary velocity is zero and the assertion is immediate. The
assumption N>=2 matters: the two adjacent coins used below must be
independent. A single isolated car with gap at least two has stationary
mean speed `1+epsilon`, so the N=1 extension would be false.

## 2. A block-work inequality at every finite density

The previous [block-work argument](../2026-10-26-local-clusters/ACTIVE_BLOCK_GEOMETRY.md)
was stated for H<2N. Its drift proof actually works for all finite H;
the restriction was needed only to interpret B as a count of noncyclic
qualified blocks. We give the proof here, including infinite volume.

Put `W=sum_i c_i(g_i-1)`. Under full braking, an old qualified site with
a qualified leader keeps its contribution. With an unqualified leader,
its contribution falls by exactly one, including the case where a gap
of two drops to one. An unqualified site contributes zero before and
after. Thus the all-braking drift is `-sum_i c_i(1-c_(i+1))`.

With arbitrary coins, an old qualified site's contribution exceeds its
all-braking value by at most `xi_(i+1)`: only the leader's extra motion
can increase the gap, and the positive-part function is 1-Lipschitz.
At an old unqualified site, a new contribution requires `xi_i=1`; the
car moves one and the leader at most two, giving a contribution at most
`xi_i g_i`. Conditional expectation therefore gives

\[
\mathbb E[W'-W\mid g,v]
\le-\sum_i c_i(1-c_{i+1})
 +\epsilon\left(\sum_i c_i+\sum_{i:c_i=0}g_i\right)
\le-\sum_i c_i(1-c_{i+1})+\epsilon(H-\sum_i c_i).
\]

Stationarity and boundedness of W on a finite ring imply

\[
\boxed{B+\epsilon C\le\epsilon\eta.}               \tag{6}
\]

On the infinite line use the single-site integrable variable
`c_0(g_0-1)` instead of the sum. The same comparison gives
`0<=-B+epsilon E[c_0+(1-c_0)g_0]`, and `g_0 c_0>=2c_0`
again gives (6). Its expectation is well-defined because the gap mean is
finite. No second moment is used.

## 3. Adjacent-pair threshold balance

For j>=2 define

\[
S_j=\mathbb P_{\rm av}(c_0=c_1=1,g_0=j),\quad S_1=0,
\qquad R_j=\mathbb P_{\rm av}(c_0=1,g_0=j).
\]

Consider the bounded threshold indicator

\[
A_i^{(j)}=c_i c_{i+1}\mathbf1_{\{g_i\ge j\}}.
\]

Stationarity equates its expected births and losses. If the old pair is
11, both cars move `1+xi`, so `g_i'=g_i+xi_(i+1)-xi_i`.
The event `g_i=j`, `xi_i=1`, `xi_(i+1)=0` therefore forces a loss of A,
with conditional probability epsilon p. A birth from an old 11 pair
requires `g_i=j-1`, `xi_i=0`, `xi_(i+1)=1`; it has probability at most
epsilon p. For j=2 this source is absent.

A birth from an old 01 or 10 pair requires the unqualified car's coin
to be one, and hence has probability at most epsilon. A birth from 00
requires both independent coins, with probability at most epsilon^2.
On a ring, 01 and 10 occur equally often in every cyclic binary word.
On the infinite line they have equal probability by translation
invariance. Each has averaged probability B. Dropping other losses and
bounding the probability of 00 by one yields

\[
\epsilon p S_j\le\epsilon p S_{j-1}
                       +2\epsilon B+\epsilon^2.
\]

Iterating from S_1=0 proves

\[
S_j\le{(j-1)(2B+\epsilon)\over p},\qquad
R_j\le B+{(j-1)(2B+\epsilon)\over p}.                \tag{7}
\]

The second inequality adds the possible 10 pair at site zero.
This argument uses neither pair independence in the stationary law nor
an approximation to the update rule. Only the fresh coins are independent.

## 4. Mean gap excludes a positive limiting moving fraction

Sum (7) over j=2,...,M. A qualified car with gap greater than M is bounded
by the ordinary gap tail, whose probability is at most `eta/(M+1)`.
Together with (6), this gives

\[
C\le(M-1)B+{(2B+\epsilon)M(M-1)\over2p}
                  +{\eta\over M+1}
\le(M-1)\epsilon\eta
 +{\epsilon(1+2\eta)M(M-1)\over2p}+{\eta\over M+1}.
\]

Equation (4) proves (5). For epsilon<=1/2 let
`x=epsilon^(1/3)` and `M=ceil(1/x)>=2`. Then

\[
M-1\le x^{-1},\quad M(M-1)\le x^{-2}+x^{-1},
\quad(M+1)^{-1}\le x,\quad(2p)^{-1}\le1.
\]

If eta<=R, substitution in (5) gives

\[
U\le(1+3R)x+(1+3R)x^2+x^3\le(3+6R)x.
\]

This completes the proof. No extrapolation from finite audits is involved.

## 5. Uniform local arrest and unscaled limit interchange

Take any finite-ring stationary laws with `N_k->infinity`, bounded
`H_k/N_k`, and `epsilon_k->0`, and average over cyclic car-label shifts.
The one-site gap means are bounded, so Markov's inequality and diagonal
extraction give local subsequential limits on the integer label line.

For a fixed finite set A of labels, stationarity, integer nonnegative
velocities, and (1) give

\[
\mathbb P(\exists i\in A:v_i>0)
\le |A|U\le |A|(3+6R)\epsilon^{1/3}\longrightarrow0. \tag{8}
\]

Every local limit is therefore entirely resting. This excludes the
moving component permitted by the previous
[classification at p=1](../2026-10-26-rare-braking-error/ZERO_NOISE_LIMITS.md),
without assuming that a local limit is spatially ergodic. That earlier
classification of all p=1 invariant laws remains valid; its moving class
cannot be selected by these bounded-density positive-noise limits.

In particular `J->0` along every joint sequence with epsilon->0 and
bounded vacancy density. Even if a fixed-epsilon thermodynamic current
has not been shown to exist, its limsup tends to zero as epsilon->0.
Whenever both unscaled iterated limits are defined, they equal zero.
This is an **unscaled** statement: dividing (1) by epsilon gives a
diverging bound, so it does not justify the interchange needed for J/epsilon.

No conclusion about vacancy-mass uniform integrability follows from
(8). A vanishing fraction of cars can have very large gaps, and a traffic
jam can occupy a macroscopic road fraction while almost every car label
is resting. Thus this theorem is not a no-condensation theorem.

## 6. Audits and next result

`verify.py` passed 12,900,352 exact threshold checks, representing 529,232
small state/mask cases, and 44,091 rational constant checks.
`verify_local_reduction.py` implements the original four update steps
independently. It also checks 291,452 threshold inequalities and 5,280
block drifts, including H>=2N, in seeded larger examples.
`verify_flow_fixtures.py` supplies 20 exact polynomial certificates against
four archived stationary current formulas on the whole interval
`0<=epsilon<=1/2`. It does not rerun the earlier stationary solvers.

The stronger gap-law conclusion and its quantitative cylinder-generator
estimate are proved in [LOCAL_STATIONARY_REDUCTION.md](LOCAL_STATIONARY_REDUCTION.md).
The [audit](AUDIT.md), [closure-attempt record](CLOSURE_ATTEMPTS.md), and
[handoff](HANDOFF.md) identify what is proved and what remains open.
