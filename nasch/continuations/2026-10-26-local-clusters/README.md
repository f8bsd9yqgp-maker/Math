# Local cluster comparison and an improved full-model joint limit

26 October 2026, continuation from commit
`9e7323bf9c323a581f4a304964cffb26614ba92d`. This is AI-assisted mathematics
with the analytic proof and finite exact checks below. It has not received
independent specialist peer review, proof-assistant certification, or a
literature-priority determination.

The previous [full-model error theorem](../2026-10-26-rare-braking-error/SHARP_WORKLOAD_BOUND.md)
proved the desired traffic coefficient along joint limits satisfying
`epsilon*N^(3/2)->0`, where `epsilon=1-p`. The present argument proves it
when the larger quantity `epsilon*N` tends to zero. **It does not prove
the thermodynamic-first limit or solve the general flow formula.**

## 1. Statement

For `N>=2` cars and `1<=H<2N` vacancies, let `U` be the stationary mean
velocity per car in the full parallel-update NaSch model and

\[
J_{N,H}(1-\epsilon)={N\over N+H}U,\qquad
F_{N,H}={H\over N}-\pi_{N,H}(g_0\ge2),
\]

where `pi_(N,H)` is the unique stationary law of the continuous-time
rate-one backchip reduction. The full-model statements hold for **every**
stationary law; uniqueness of the full-model law is not assumed.

**Theorem 1.** If `0<epsilon*max(N,H)<=1/4` and `H/N<=R`, then

\[
\boxed{
\left|{J_{N,H}(1-\epsilon)\over\epsilon}
   -{N\over N+H}F_{N,H}\right|
\le \left({5R\over2}+65R^2+20R^3\right)\epsilon N.} \tag{1}
\]

In particular, `H<2N` and `epsilon*N<=1/8` give the universal bound
`425 epsilon N`.

With the previously proved reduced scalar limit `Q`, it follows that
for every sequence

\[
N\to\infty,\qquad H/N\to\eta\in(0,2),\qquad
\epsilon>0,\qquad\epsilon N\to0,
\]

\[
\boxed{
{J_{N,H}(1-\epsilon)\over\epsilon}
  \longrightarrow {\eta-Q(\eta)\over1+\eta}.}       \tag{2}
\]

This improves a sufficient joint-limit condition. No optimality is claimed.
The condition still excludes taking `N->infinity` with fixed positive
`epsilon`, so (2) is not an unrestricted interchange of limits.

## 2. Inputs from the previous proof

Let `g_i` be the gap ahead of car `i`, `a_i=1{v_i>0}`, and let the fresh
independent `Bernoulli(epsilon)` coins `xi_i` mean **no random braking**.
The full update is

\[
w_i=c_i+\xi_i\mathbf1_{\{g_i\ge1\}},\quad
c_i=a_i\mathbf1_{\{g_i\ge2\}},\quad
g_i'=g_i+w_{i+1}-w_i,\quad v_i'=w_i.               \tag{3}
\]

The assumption `H<2N` implies that `c` has at least one zero. Let
`ell_i` be the total future displacement of car `i` if every later coin
is zero. If `c_i=0`, `ell_i=0`; if `c_i=1`,

\[
\ell_i=g_i-1+\ell_{i+1}.                           \tag{4}
\]

With lifted heights `h_(i+1)-h_i=g_i`, `h_(i+N)=h_i+H`, define the exact
full-braking projection `P=h+ell` and its projected gaps
`G_i=P_(i+1)-P_i`. Their sum is `H`, and `G_i=1` whenever `c_i=1`.
For the current mask, put `K=sum_i xi_i`, `k=sum_i a_i`, and

\[
d(m)=m-\mathbf1_{\{m\ge2\}},\qquad
B=\sum_i\xi_i d(G_i).                               \tag{5}
\]

The previous proof establishes the following exact ingredients, which we
use with their stated scope:

1. If `P'` is the projection after the full update, then
   `P'_i-P_i<=B` for every `i`. Also `P'_i-P_i>=-(H-1)`.
2. Let `T_i` be a reduced backchip height update. A monotone, vertically
   homogeneous corrector `Phi` satisfies
   `0<=Phi(T_i P)-Phi(P)<=F_(N,H)` and the sum of these increments over
   all sites is exactly `F_(N,H)`. Consequently `Phi` obeys the
   sup-norm order bound.
3. Let `P^0` be the projected profile obtained by starting from rest at
   profile `P`, using the **same mask** `xi`, then braking to rest. It is
   a serialized word of reduced updates. Uniformly in `P`,

   \[
   \big|\mathbb E[\Phi(P^0)-\Phi(P)\mid P]-\epsilon F_{N,H}\big|
       \le {5N-1\over2}\epsilon^2F_{N,H}.           \tag{6}
   \]

   This is a comparison process used in the proof; it does not change the
   full model.
4. For `r_i=a_i+ell_i`, a full-braking update changes `r_i` to `ell_i`.
   With `r_i'` the post-update value,

   \[
   \sum_i(r_i'-\ell_i)_+\le(k+K)B.                  \tag{7}
   \]

The referenced notes contain the all-parameter proofs and their audits.
The present continuation derives new consequences; it does not rerun or
replace the old stationary or Poisson solvers.

## 3. The disagreement is confined to mixed clusters

For a fixed current state and mask, call a site **marked** if `xi_i=1`.
On the cyclic graph of car labels, form the set `{i:c_i=1 or xi_i=1}`.
Let `S` be the union of its connected components containing both a
qualified site (`c_i=1`) and a marked site. These components may cover
the whole ring.

**Lemma 2.** For every site outside `S`, the two projected profiles agree:

\[
P'_i=P_i^0\quad(i\notin S).                        \tag{8}
\]

**Proof.** At a site outside the union `{c=1} union {xi=1}`, both the old
remaining displacement and the first-step velocity are zero. Thus neither
projected height changes there.

Consider a component containing marks but no qualified site. All its sites
have `c_i=0`, and its two boundary neighbors, if present, have both
`c=0` and `xi=0`. An inside site also has `c_(i+1)=0`; hence both
`ell_i` and `ell_(i+1)` are zero, so `G_i=g_i`. On this component, (3)
gives the same first-step velocities as the comparison started from rest at
`P`. The boundary neighbors do not move in either calculation. Therefore
the updated gaps and future full-braking displacements agree throughout
the component. This includes the case that the component is the whole ring.

Finally, consider a component containing qualified sites but no marks.
Both boundary neighbors, if any, have `c=xi=0`. The actual first step and
its subsequent relaxation on the component are identical to the
all-braking trajectory, whose projection remains `P`; the comparison
started at rest has no marked site in the component and likewise leaves
its heights at `P`. If the component is the whole ring, it would have
`c_i=1` at every site, contrary to `H<2N`. These cases prove (8). Square.

**Lemma 3.** For every mask,

\[
|\Phi(P')-\Phi(P^0)|\le4F_{N,H}|S|.                 \tag{9}
\]

**Proof.** Both projected profiles are ordered lifts with the same total
gap `H`. Their coordinatewise minimum `W=P' wedge P^0` and maximum
`V=P' vee P^0` are also ordered lifts of the same total gap. They agree
outside `S` by Lemma 2.

If `S` is not the full ring, start from `W`. In each component of `S`,
visit sites from upstream to downstream, meaning that `i+1` is processed
before `i`, and fire each site twice. Two backchip updates set its height
to its current leader's height. By induction the processed height is at
least its target value in `V`: the already processed leader, or the
unchanged boundary leader, is at least `V_(i+1)>=V_i`. Outside heights
are unchanged. At most `2|S|` reduced firings thus produce a profile
dominating `V`. Monotonicity of `Phi` and its single-update increment
bound give `Phi(V)-Phi(W)<=2F_(N,H)|S|`, which proves (9) in this case.

If `S` is the whole ring, no upstream endpoint need exist. The old
projection comparison gives `-(H-1)<=P'_i-P_i<=H`; the rest serialization
gives `0<=P_i^0-P_i<=H`. The corrector sup-norm bound yields
`|Phi(P')-Phi(P^0)|<=2H`. Since `2 q_(N,H)<=H/N`,
`F_(N,H)>=H/(2N)`, so `2H<=4NF_(N,H)=4F_(N,H)|S|`. Square.

## 4. Expected size of the disagreement set

Fix the state and let `m=sum_i c_i<=k`. If `m=0`, `S` is empty.
Otherwise decompose the qualified sites into cyclic one-blocks with lengths
`l_1,...,l_b`. A qualified block can belong to `S` only if it contains a
mark or one of its two adjacent sites is marked. Its contribution to
`E|S|` is thus at most `epsilon*l_j*(l_j+2)`. Summing and using
`sum l_j=m` bounds the qualified contribution by `epsilon(m^2+2m)`.

For an unqualified site to belong to `S`, it and a consecutive string of
unqualified sites connecting it to a qualified block must all be marked.
In each unqualified gap between two qualified blocks, a union bound from
its two ends gives a total expected contribution at most
`2epsilon/(1-epsilon)`. There are at most `m` such gaps. Consequently,
for `epsilon<=1/2`,

\[
\boxed{\mathbb E[|S|\mid g,v]
 \le\epsilon\left(k^2+6k\right).}                  \tag{10}
\]

This is a conditional bound; no independence between the stationary state
and its corrector is assumed. The fresh coins are independent of the state.

## 5. Second factorial moment of the number of active cars

Let expectations below be under any stationary full-model law, and put
`M=E k` and `f=E[k(k-1)]`. By (7), the finite potential `sum_i r_i`
has a full-braking decrement `k` and a perturbation at most `(k+K)B`.
Writing `b0=1+(N-1)epsilon` and using independent fresh coins,

\[
\mathbb E[B\mid g,v]\le\epsilon H,\qquad
\mathbb E[KB\mid g,v]\le\epsilon H b_0.
\]

Stationarity gives the previous first-moment bound

\[
M\le M_*:={\epsilon H b_0\over1-\epsilon H}.       \tag{11}
\]

For the second moment use the new bounded potential

\[
V_2(r)=\sum_{0\le i<j<N}\min(r_i,r_j).
\]

Under an all-braking step it decreases by `k(k-1)/2`. The support of the
coordinatewise maximum of the all-braking lifetimes and the actual
post-update lifetimes has at most `k+K` sites: the former are supported
on old active cars, and the latter on cars with `w_i>0`. The pair minimum
is coordinatewise monotone and 1-Lipschitz in each argument. Therefore
(7) bounds the increase relative to all braking by

\[
(k+K-1)_+\sum_i(r_i'-\ell_i)_+
 \le (k+K)(k+K-1)B.                                \tag{12}
\]

In the last expression `k+K` is a nonnegative integer, so its product
with `k+K-1` is also nonnegative. For each summand of `B`, conditioning
on its own coin being one leaves `N-1` independent coins. This gives

\[
\mathbb E[K(K-1)B\mid g,v]
 \le\epsilon H\{2(N-1)\epsilon+(N-1)(N-2)\epsilon^2\}.\tag{13}
\]

Together with `E B` and `E KB`, bounded-potential stationarity yields,
whenever `2epsilon H<1`,

\[
f\le
{4\epsilon H b_0 M+4\epsilon^2H(N-1)
 +2\epsilon^3H(N-1)(N-2)\over1-2\epsilon H}.       \tag{14}
\]

Under `epsilon*max(N,H)<=1/4`, (11) gives `M<=2epsilon H`, and (14)
gives

\[
\boxed{f\le20\epsilon^2H^2+9\epsilon^2HN.}         \tag{15}
\]

For example, use `b0<=5/4`, `(1-2epsilon H)^(-1)<=2`, and
`epsilon N<=1/4`. These are bounds on global active-car moments and are
not asserted to be uniform at fixed `epsilon` as `N` grows.

## 6. Proof of the current bound

Set `Psi(h,v)=Phi(P(h,v))`. Its difference from mean lifted height is a
bounded function of the finite gap/velocity state, so stationarity gives
`E Delta Psi=U`. Lemmas 2-3, (6), and (10) imply

\[
\left|{U\over\epsilon}-F_{N,H}\right|
\le F_{N,H}\left[{5N-1\over2}\epsilon
       +4\mathbb E(k^2+6k)\right].                  \tag{16}
\]

The comparison is made conditionally on the full current state and then
averaged. No independence of `k` and `Phi` is needed. Since
`E(k^2+6k)=f+7M`, (11) and (15) give

\[
\left|{U\over\epsilon}-F_{N,H}\right|
\le F_{N,H}\left[
 \left({5N\over2}+56H\right)\epsilon
 +80\epsilon^2H^2+36\epsilon^2HN\right].          \tag{17}
\]

Use `F_(N,H)<=H/N<=R`, `H<=RN`, and `epsilon N<=1/4` to bound the
right side by `(5R/2+65R^2+20R^3)epsilon N`. Multiplication by
`N/(N+H)<=1` proves (1).

If `H/N->eta in (0,2)` and `epsilon N->0`, all the hypotheses hold for
large `N`, and the right side of (1) tends to zero. The previously proved
scalar canonical convergence gives `F_(N,H)->eta-Q(eta)`, establishing
(2). Square.

## 7. Exact audit and limits of the result

`python3 verify.py` uses the earlier independently implemented traffic
update and deterministic projection as fixtures; it does not solve a
stationary distribution or Poisson equation. Its new exact assertions
checked:

* 529,232 mixed-cluster support comparisons and 529,232 pair-workload
  inequalities;
* 503,992 explicit two-firing domination words and 25,240 full-ring cases;
* 1,503 exact rational cluster-expectation inequalities;
* 9,996 exact rational checks of the moment and final constants.

`python3 verify_flow_fixtures.py` additionally gives eight exact
Bernstein-coefficient certificates for (17) against four archived rational
full-model current formulas over their whole epsilon intervals. The old
stationary formulas are used only as recorded fixtures. Results are in
`results/`.

`python3 verify_independent.py` implements the original four NaSch rules
and repeated full braking independently of the reused fixtures. With a
fixed seed, 6,840 direct cases passed, including 145 full-ring disagreement
sets and 1,124 negative projected-displacement cases. These are additional
finite checks, not a proof of the limit.

The separate [size-uniform lower bound](UNIFORM_LOWER_BOUND.md) compares the
full model to one-speed parallel exclusion. It applies with no restriction
of the form `epsilon N->0`; it is one-sided and does not close interchange.

The separate [active-block theorem](ACTIVE_BLOCK_GEOMETRY.md) proves the
size-uniform inequality `E b+epsilon E m<=epsilon H`, where `m` counts
qualified moving cars and `b` their cyclic blocks. If unscaled current
stays positive as `epsilon->0`, a positive fraction of car labels must be
in qualified blocks of length at least order `1/epsilon`. This does not
exclude long blocks or moving vacancy condensates.

Finite checks support the deterministic lemmas and arithmetic; the proof
above and the inherited reduced scalar-limit proof carry the all-size
claim. No explicit `Q`, general fixed-p stationary current, decision of
the critical-density/condensate alternative, or thermodynamic-first
limit interchange is obtained.
