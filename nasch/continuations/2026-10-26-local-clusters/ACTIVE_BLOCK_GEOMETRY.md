# A size-uniform bound on moving-car block geometry

26 October 2026. This is an additional full-NaSch result from the local
cluster continuation. It applies uniformly in road size and does not
assume the restricted joint limit. It characterizes a necessary geometry
for sustained activity; it does not show that this geometry occurs or
exclude a moving mass condensate.

## 1. Statement

On a ring with `N>=2`, `1<=H<2N`, write `epsilon=1-p in (0,1)`,
`a_i=1{v_i>0}`, and

\[
c_i=a_i\mathbf1_{\{g_i\ge2\}},\quad
m=\sum_i c_i,\quad
b=\sum_i c_i(1-c_{i+1}).                            \tag{1}
\]

Since `H<2N`, the `c` configuration is not identically one; `b` is the
number of cyclic blocks of qualified cars. Expectations are taken under
any stationary full-model law.

**Theorem 1 (block drift).**

\[
\boxed{\mathbb E b+\epsilon\mathbb E m\le\epsilon H.} \tag{2}
\]

In particular, the mean number of qualified blocks per car is at most
`epsilon H/N`, uniformly in N. If the stationary law is invariant under
cyclic car-label shifts, let `L_0` be the length of the qualified block
containing car zero, on the event `c_0=1`. For any integer `s>=1`,

\[
\boxed{\Pr(c_0=1,\,L_0\le s)
 \le s\epsilon\left({H\over N}-\mathbb E c_0\right)
 \le s\epsilon{H\over N}.}                         \tag{3}
\]

Any stationary law may be averaged over cyclic shifts without changing
its mean velocity or the bound (2).

For `j=0,...,N-1`, writing `dist_N(j,0)=min(j,N-j)`, shift invariance
also gives the explicit local phase-coherence estimate

\[
\Pr(c_0\ne c_j)\le
2\,\mathrm{dist}_N(j,0)\,\epsilon
 \left({H\over N}-\mathbb E c_0\right).              \tag{3a}
\]

Thus qualified activity is constant with probability tending to one over
any label distance `j=o(1/epsilon)`, provided `H/N` stays bounded. This
does not say which constant is selected or imply full-law ergodicity.

The stationary mean velocity per car satisfies

\[
U=\mathbb E m/N+\epsilon\,\mathbb E\#\{i:g_i\ge1\}/N,
\quad\text{so}\quad 0\le U-\mathbb E m/N\le\epsilon.\tag{4}
\]

Consequently, along any sequence of translation-invariant stationary
laws with `epsilon->0`, bounded `H/N`, and `U>=u>0`, a positive fraction
of cars must lie in qualified blocks whose lengths are at least of order
`1/epsilon`. More explicitly, for every integer `s>=1`,

\[
\Pr(c_0=1,L_0>s)\ge U-\epsilon-s\epsilon H/N.       \tag{5}
\]

For example, if `H/N<=R`, `U>=u`, and `s=floor(u/(2epsilon R))`, the
right side is at least `u/2-epsilon`. These are blocks of moving car
labels, not necessarily macroscopic vacancy piles. A length of order
`1/epsilon` can be much smaller than the road size.

## 2. Proof of the drift inequality

Use the full-model exact rule

\[
w_i=c_i+\xi_i\mathbf1_{\{g_i\ge1\}},\quad
g_i'=g_i+w_{i+1}-w_i,\quad v_i'=w_i,               \tag{6}
\]

with independent fresh `Bernoulli(epsilon)` nonbraking coins `xi_i`.
Define the bounded nonnegative work

\[
W(g,v)=\sum_i c_i(g_i-1)\le H.
\]

If every coin is zero, an old qualified car moves one cell. If its leader
is also qualified, its gap and work contribution stay unchanged. If its
leader is not qualified, its gap decreases by one; its contribution
decreases by exactly one, including when a gap of two drops to one and
the site ceases to be qualified. Old unqualified cars do not move or
become qualified. Therefore

\[
W_{\rm brake}'-W=-b.                                 \tag{7}
\]

For an arbitrary mask, compare each contribution to the all-braking
outcome. At an old qualified site `i`, `w_i>0`, so the new contribution is
`(g_i'-1)_+`. Relative to full braking, its leader can move at most one
extra cell, and the car's own coin can only decrease its new gap. The
positive-part map is 1-Lipschitz; the contribution therefore increases
by at most `xi_(i+1)`.

At an old unqualified site, the all-braking contribution is zero. It can
have a nonzero new contribution only if `xi_i=1` and `g_i>=1`, in which
case it moves exactly one and the leader moves at most two. Hence
`(g_i'-1)_+<=g_i`; its new contribution is at most `xi_i g_i`.
Summing and conditioning on the current state gives

\[
\mathbb E[W'-W\mid g,v]
 \le-b+\epsilon\left(m+\sum_{i:c_i=0}g_i\right).
\]

Every qualified site has gap at least two, so
`m+sum_(c_i=0) g_i<=H-m`. At stationarity `E(W'-W)=0`, since `W` is
bounded. This proves (2).

## 3. From block count to long-block necessity

For a cyclic configuration, the number of qualified cars belonging to
blocks of length at most `s` is at most `s b`. Under a shift-invariant
law, its expected fraction is the left side of (3). Combine this with
(2) to prove (3).

Shift invariance also gives `Pr(c_0=1,c_1=0)=E b/N` and
`Pr(c_0=0,c_1=1)=E b/N`: the difference of these probabilities is
`E(c_0-c_1)=0`. A union bound along a shortest cyclic path from 0 to `j`,
followed by (2), proves (3a).

Equation (4) follows directly from (6), independence of the fresh coins,
and stationarity of the velocity distribution. Subtract (3) from
`Pr(c_0=1)=E m/N` and apply (4); this proves (5).

If `U` has a positive lower limit as `epsilon->0`, (5) forces qualified
block lengths to diverge along a positive fraction of car labels. The
argument allows such large blocks and says nothing by itself about their
existence, their spatial distribution on the road scale, or the mean mass
seen by a moving condensate. In particular, (2)-(5) do not determine the
first-order coefficient `U/epsilon`.

## 4. Exact audit and scope

`python3 verify_block_geometry.py` checks the new all-braking block drift,
the arbitrary-mask perturbation bound, and the conditional expectation
with exact rational coin probabilities. It passed 529,232 mask checks and
55,716 rational conditional-drift checks for 20 `(N,H)` pairs. It reuses
the original-rule update as a fixture and solves no stationary system.
Results: `results/block_geometry.json`.

The theorem is a finite-size analytic argument, not an inference from the
checks. It has not received independent specialist peer review. The
general flow formula, a matching upper bound on the rare-braking scale,
the moving-condensate alternative, and unrestricted interchange remain
unresolved.
