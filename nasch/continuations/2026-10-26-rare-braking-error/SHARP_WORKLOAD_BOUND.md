# A sharper full-model bound from individual remaining workloads

26 October 2026, continued run 19. This strengthens the cubic size condition
in README.md. All notation refers to the full parallel NaSch model and the
already constructed reduced current corrector `Phi` in that file.

Put `epsilon=1-p`, `N>=2`, `1<=H<2N`, and

\[
F=H/N-\pi_{N,H}(g_0\ge2),\qquad
C_N=(5N-1)/2,\qquad
M_*={\epsilon H\{1+(N-1)\epsilon\}\over1-\epsilon H}.
\]

**Theorem.** If `epsilon H<1`, every stationary full-model mean velocity
`U` obeys the following two bounds:

\[
{U\over\epsilon}-F
 \le C_N\epsilon F+4FM_*+3\epsilon F N(N-1)M_*,       \tag{1}
\]
\[
F-{U\over\epsilon}
 \le F\{M_*+(N-1)\epsilon\}
 +(H-1)\{2\epsilon H M_*+\epsilon^2H(N-1)\}.          \tag{2}
\]

In particular, when `H/N<=R` and `epsilon max(N,H)<=1/2`,

\[
\boxed{\left|{J_{N,H}(1-\epsilon)\over\epsilon}
       -{N\over N+H}F\right|
 \le(12R^2+3R)\epsilon N
       +(6R^3+10R^2)\epsilon^2N^3.}                  \tag{3}
\]

Thus, using the inherited reduced scalar convergence, for **every** sequence

\[
N\to\infty,\quad H/N\to\eta\in(0,2),\quad
\epsilon>0,\quad\epsilon N^{3/2}\to0,
\]

\[
{J_{N,H}(1-\epsilon)\over\epsilon}
 \longrightarrow {\eta-Q(\eta)\over1+\eta}.          \tag{4}
\]

This supersedes the sufficient condition `epsilon N^3->0` in the initial
run-19 argument. It remains a restricted joint limit. It is not a uniform
thermodynamic-first interchange theorem or an explicit formula for `Q`.

## 1. Projection comparisons for an arbitrary coin mask

Let `a_i=1{v_i>0}`, `c_i=a_i 1{g_i>=2}`, and let `ell_i` be the exact
remaining full-braking displacement from README.md. Put

\[
P=h+\ell,\quad G_i=P_{i+1}-P_i=g_i+\ell_{i+1}-\ell_i,
\quad k=\sum_i a_i,\quad K=\sum_i\xi_i,
\quad B=\sum_i\xi_i d(G_i).
\]

Here `P` is a lifted height profile; `G` is its gap configuration and has
total mass `H`. In particular `sum_i d(G_i)<=H`. When `c_i=1`, `G_i=1`.

Apply the arbitrary mask `xi` for one update, then brake forever. Write
`w_i` for that update's velocity, `ell_i'` for its remaining displacement,
`x_i=w_i+ell_i'`, and `delta_i=x_i-ell_i`. The new projected profile is
`P'=P+delta`. Let `c_i'=1{w_i>0,g_i'>=2}`.

If `c_i'=1`, the exact relaxation recurrence gives

\[
x_i=g_i-1+x_{i+1}.                                 \tag{5}
\]

If `c_i'=0`, then `x_i=w_i`. Consequently:

* if `c_i=c_i'=1`, then `delta_i=delta_(i+1)`;
* if `c_i=0,c_i'=1`, then `xi_i=1`, `G_i>=2`, and
  `delta_i=d(G_i)+delta_(i+1)`;
* if `c_i'=0`, then `delta_i<=xi_i d(G_i)`.

For the second statement, a newly moving site has `g_i>=1`. If `g_i=1`,
the condition `g_i'>=2` forces `w_(i+1)=2`, hence `c_(i+1)=1` and
`G_i=1+ell_(i+1)>=2`. If `g_i>=2`, the assertion is immediate.
For the third statement, an old qualified car has `ell_i>=1`, `G_i=1`,
and `w_i=1+xi_i`; an unqualified car has `ell_i=0` and
`w_i=xi_i 1{g_i>=1}`. These give the claimed bounds.

Not all `c_i'` are one, because the new gaps still sum to `H<2N`.
Following (5) to the first zero of `c'` therefore proves

\[
\boxed{\delta_i\le B\quad\hbox{for every }i.}        \tag{6}
\]

This is a one-sided bound. Large negative changes remain possible.

We also need a bound in corrector units. If
`S={i:c_i=1 or xi_i=1}` is not the entire ring, fire every site in `S`
once in the reduced process, from upstream to downstream in each block.
Let `D_i` be its height increments; then `D_i=0` off `S` and
`D_i=d(G_i+D_(i+1))` on `S`. Backward induction gives `D_i>=delta_i`:
at an old qualified site `G_i=1` and
`d(1+D_(i+1))=max(1,D_(i+1))`; at a triggered unqualified site with
`G_i>=2` use (5); with `G_i<=1` it is unqualified after the update and
`delta_i<=1` (zero if `G_i=0`). These are all cases.

Each reduced update increases `Phi` by at most `F`, and the word has
length at most `k+K`. If `S` is the whole ring, (6) instead gives
`Phi(P')-Phi(P)<=H`. The deterministic inequality
`pi(g_0>=2)<=H/(2N)` implies `F>=H/(2N)`, and `k+K>=N` in this case.
We have therefore proved, for every mask with `K>=1`,

\[
\boxed{\Delta\Psi\le2(k+K)F.}                       \tag{7}
\]

For `K=0` the increment is exactly zero.

## 2. First and excess activity bounds

Define the individual remaining stored-velocity lifetimes

\[
r_i=a_i+\ell_i,\qquad V=\sum_i r_i,
\qquad W=\sum_i r_i-\max_i r_i.
\]

Under a full-braking step, `r_i` becomes `ell_i=(r_i-1)_+`.
Thus `V` decreases by `k`, and `W` decreases by `(k-1)_+`.
For an arbitrary mask,

\[
r_i'-\ell_i=\delta_i-\mathbf1_{\{w_i=2\}}\le\delta_i.
\]

Only sites with `w_i>0` can have a positive increase relative to `ell_i`;
there are at most `k+K` of them. Equation (6) implies

\[
\sum_i(r_i'-\ell_i)_+\le(k+K)B.                     \tag{8}
\]

The function `W(r)` is coordinatewise increasing and 1-Lipschitz in each
coordinate: it is the minimum of the sums omitting one coordinate.
Hence its increase over the full-braking outcome is also at most (8).
At rest a sharper bound is available: at most `K` lifetimes are nonzero,
each is at most `B`, so `W(r')<=(K-1)_+ B`.

Conditional on the current state, the coins are independent and

\[
\mathbb E B\le\epsilon H,\qquad
\mathbb E(KB)\le\epsilon H\{1+(N-1)\epsilon\},
\qquad
\mathbb E[(K-1)_+B]\le\epsilon^2H(N-1).              \tag{9}
\]

The last identity uses `B=0` when `K=0`; each summand in `B` is correlated
with its own coin, so that correlation has explicitly been included.

Let `M=E k`, `A=Pr(k>0)`, and `L=E(k-1)_+` in any stationary law.
The potentials are bounded on the finite state space. Stationarity of `V`
and (8)-(9) give

\[
M\le\epsilon H\{M+1+(N-1)\epsilon\},
\qquad\boxed{M\le M_*}.                            \tag{10}
\]

For `W`, use (8) on nonrest states and the sharper rest bound in (9).
The terms involving `(N-1)epsilon` combine exactly to give

\[
L\le\epsilon H M+\epsilon H A+\epsilon^2H(N-1)
 \le\boxed{2\epsilon H M+\epsilon^2H(N-1)}.           \tag{11}
\]

These estimates concern the mean *number* of active cars and its excess
beyond one, not just the probability that the whole road is away from rest.

## 3. When a corrected decrement can occur

The recurrences in Section 1 show that a negative `delta` requires a
negative terminal value at a site with `c_i'=0`. Such a site must satisfy

\[
c_i=c_{i+1}=1,\qquad g_i=2,\qquad\xi_i=1.           \tag{12}
\]

Indeed, if `xi_i=0`, the condition `g_i+w_(i+1)-1<=1` forces
`g_i=2,w_(i+1)=0`, hence `ell_i=1` and `delta_i=0`. If `xi_i=1`, then
`g_i+w_(i+1)<=3`. The cases `g_i=3,w_(i+1)=0` and
`g_i=2,c_(i+1)=0` again have nonnegative terminal displacement. The only
remaining possibility is (12). This proves necessity, not sufficiency.

There are at most `(k-1)_+` candidate sites in (12), since `c` has at least
one zero and the number of edges inside its one-blocks is at most
`sum c_i-1`. A union bound on their fresh coins and the deterministic
bound `delta_i>=-(H-1)` give

\[
\mathbb E[\Delta\Psi\mid g,v]
 \ge-\epsilon(H-1)(k-1)_+.                          \tag{13}
\]

In particular, there is no negative projected increment from a state
with at most one active car, even under a mask with several coins.

## 4. Improve the rest-state error to linear size

At rest the actual relaxed mask is the serialized backchip word of
README.md. Compare it with firing every marked site once in a uniformly
random order, including marks at originally empty sites.

Conditional on `K`, that comparison word is an ordered sample without
replacement of length `K`. After `m` firings the next site is uniform
among the `N-m` unused sites. For the current corrector increments
`a_i(P)`, we have `0<=a_i<=F` and `sum a_i=F`. The average over unused
sites differs from `F/N` by at most `mF/N`: the full uniform distribution
is a mixture with weight `m/N` on the used sites, and both averages lie
in `[0,F]`. Summing and averaging over the binomial `K` shows that this
random-order word has expected corrected increment within
`(N-1)epsilon^2 F/2` of `epsilon F`.

Call a marked site bad if either cyclic neighbor is marked, and let `Z`
be the number of bad sites. Every other marked site is isolated. Reduced
height updates at nonadjacent sites commute, so in both words all isolated
firings can be moved to the beginning. An originally empty isolated
firing is the identity. The two words therefore have the same intermediate
profile after these isolated firings. Each remaining word has at most
`Z` firings, all with corrected increments in `[0,F]`; their two final
corrector values differ by at most `ZF`. Finally,

\[
\mathbb E Z\le2N\epsilon^2.
\]

This bound also holds for `N=2`, when the two cyclic neighbors coincide.
We conclude

\[
\boxed{\left|\mathbb E[\Delta\Psi\mid h,0]
                       -\epsilon F\right|
        \le C_N\epsilon^2F.}                        \tag{14}
\]

The earlier single-coin lower bound also remains valid:
`E[Delta Psi|h,0]>=epsilon(1-epsilon)^(N-1)F`.

## 5. A single-coin drift bound at an active state

For a single coin at an unqualified site `j` (`c_j=0`), a nonempty trigger
increases the relaxed heights by some common amount
`0<D<=d(G_j)` at `j` and at the consecutive old qualified block immediately
behind it, and changes no other projected heights. This follows directly
from (5); an original singleton trigger travels only once. Unless this
support is the whole ring, the increase is dominated by firing `j` and
then that block in upstream-first order. Its corrected increment is at
most `a_j(P)` plus `F` times that block's length.

A single coin at a qualified site has no positive projected increment
unless `g_j=2,c_(j+1)=0`. In that case it increases by one the projected
heights on its qualified block behind and including `j`. Firing that
block once gives exactly this increase. These assertions also follow by
checking `g_j+w_(j+1)-2`: if `g_j>=3` the eventual increment is zero;
if `g_j=2,c_(j+1)=1` the increment is nonpositive.

For all these nonexceptional words, sum their first increments using
`sum_i a_i(P)=F`. Each qualified site is in at most one unqualified
trigger's block and one positive qualified trigger's block. The sum of
single-coin increments is therefore at most `(1+2k)F`.

The only exceptional case has `N-1` qualified sites and the coin at the
sole unqualified site. Its increment is at most `H<=2NF<=2(k+1)F` by
(6). All other positive single-coin words together have at most `k`
firings. Since `k>=1`, their total together with the exception is at most
`(3k+2)F<=(1+4k)F`. Thus, in every case,

\[
\sum_{j=0}^{N-1}\Delta\Psi(\hbox{only coin }j)
 \le(1+4k)F.                                       \tag{15}
\]

Using (7) for masks with `K>=2`, together with
`Pr(K>=2)<=N(N-1)epsilon^2/2` and
`E[K 1{K>=2}]<=N(N-1)epsilon^2`, now gives

\[
\mathbb E[\Delta\Psi\mid g,v]
 \le\epsilon(1+4k)F
       +\epsilon^2 F N(N-1)(k+2).                  \tag{16}
\]

## 6. Complete the stationary bounds

The bounded-corrector stationarity identity from README.md is
`E Delta Psi=U`. Apply (14) at rest and (16) on its complement. Since
`A<=M`,

\[
U/\epsilon-F
 \le C_N\epsilon F+4FM
      +\epsilon F N(N-1)(M+2A)
 \le C_N\epsilon F+4FM+3\epsilon F N(N-1)M.
\]

Substitution of (10) proves (1). For the lower bound use the single-coin
rest lower bound and (13) elsewhere:

\[
U/\epsilon\ge(1-A)(1-\epsilon)^{N-1}F-(H-1)L.
\]

Since `1-(1-epsilon)^(N-1)<=(N-1)epsilon`, (10)-(11) prove (2).

Under the hypotheses of (3), `M_*<=3epsilon H`, `F<=R`, and `H<=RN`.
The upper error in (1) is at most

\[
(12R^2+5R/2)\epsilon N+9R^2\epsilon^2N^3;
\]

the lower error in (2) is at most

\[
(3R^2+R)\epsilon N+(6R^3+R^2)\epsilon^2N^3.
\]

Both are bounded by (3), after multiplying by `N/(N+H)<=1` for traffic
current. Along (4), both errors vanish and the smallness hypotheses hold
eventually. The previously proved reduced scalar limit identifies the
limit in (4). This completes the argument.

## 7. Scope and audit

The proof uses no new stationary solver, mass-tail assumption, or
thermodynamic ergodicity assumption. The mean-activity and excess-activity
potentials, the mask projection comparison, and the linear rest error
are the additional ingredients beyond the initial run-19 theorem.

`verify_sharp_workloads.py` checks the new finite inequalities and word
comparisons with integer arithmetic. The asymptotic conclusion uses the
analytic proof above and the inherited reduced limit; finite enumeration
does not certify either infinite-volume result. This is AI-assisted
mathematics and has not been independently peer-reviewed.

The exponent `3/2` is a sufficient condition from this argument, not a
claimed threshold. Fixed positive `epsilon` followed by `N->infinity`
still lies outside the estimate. The general stationary formula, remaining
reduced phase/condensate alternatives, and unrestricted interchange remain
unresolved.
