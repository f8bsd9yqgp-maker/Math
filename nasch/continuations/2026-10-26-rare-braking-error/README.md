# A quantitative near-certain-braking theorem for the full NaSch model

26 October 2026, research run 19. AI-assisted mathematics with complete
arguments and exact finite audits below. Independent specialist review and
publication-priority verification remain outstanding.

**Sharper continuation completed in this run.**
[SHARP_WORKLOAD_BOUND.md](SHARP_WORKLOAD_BOUND.md) strengthens the error to
`O_R(epsilon*N + epsilon^2*N^3)` and the sufficient joint-limit condition to
`epsilon*N^(3/2)->0`. Its proof and new exact audits are complete. The
initial cubic bound below remains valid and supplies the projection and
corrector definitions used in the sharper argument. Start with the sharper
note for the strongest current result.

The supplementary [zero-noise classification](ZERO_NOISE_LIMITS.md)
identifies the possible zeroth-order stationary local limits and explains
why spatial ergodicity cannot simply be assumed when exchanging limits.

**New result.** For the original parallel-update `v_max=2` traffic model,
the finite-road rare-braking error has an explicit polynomial size bound.
Consequently the reduced thermodynamic coefficient is the true stationary
traffic coefficient along every simultaneous limit satisfying

$$
N\longrightarrow\infty,\qquad H/N\longrightarrow\eta\in(0,2),
\qquad \epsilon N^3\longrightarrow0,
\qquad\epsilon=1-p>0.                              \tag{1}
$$

This is a restricted joint-limit theorem. It does **not** establish the
thermodynamic-first iterated limit, a size-uniform error as `epsilon->0`,
or the general stationary formula at fixed braking probability. The
remaining phase/condensate alternatives are also not settled by it.

The new ingredients are an exact deterministic relaxation map, an exact
serialization of simultaneous triggers from rest, and a full-model
stationary workload estimate. They are combined with the project's existing
monotone current corrector and scalar thermodynamic limit. An explicit
counterexample also shows why extra nonbraking events cannot simply be
treated as pathwise acceleration of the relaxed process.

## 1. Definitions and the quantitative statement

There are `N>=2` cars and `1<=H<2N` vacant cells, so the road length is `N+H`.
Index cars cyclically, with `i+1` ahead of `i`. Let `g_i` be the number of
vacancies ahead of car `i`, and `v_i` its previous velocity, in `{0,1,2}`.
Let `xi_i` be independent Bernoulli variables of parameter `epsilon`, freshly
sampled at every update. A one means **no random braking**.

The conventional accelerate/collision-brake/random-brake/move rule is exactly

$$
w_i=\mathbf1_{\{v_i>0,\ g_i\ge2\}}
       +\xi_i\mathbf1_{\{g_i\ge1\}},\qquad
g_i'=g_i+w_{i+1}-w_i,\qquad v_i'=w_i.               \tag{2}
$$

Indeed the attempted speed is `min(v_i+1,2,g_i)`; subtracting one if positive
gives the first indicator in (2), and omitting that subtraction adds the
second. Thus previous velocities one and two have the same future effect:
gaps plus activity indicators form an exact Markov quotient. This observation
is used for the audit, not claimed as a general stationary solution.

Let `U_(N,H)(epsilon)` denote mean velocity per car under **any** stationary
law of this finite chain, and let

$$
J_{N,H}(1-\epsilon)=\frac{N}{N+H}U_{N,H}(\epsilon).  \tag{3}
$$

Uniqueness of the full-model stationary law is not needed for the estimate.
Every stationary law obeys it. For the reduced backchip chain define

$$
d(m)=m-\mathbf1_{\{m\ge2\}},\qquad
F=F_{N,H}=H/N-\pi_{N,H}(g_0\ge2).                  \tag{4}
$$

The reduced chain fires each site at rate one and sends `d(g_i)` units to
`i-1`. Its finite stationary law is unique, as established previously.

**Theorem 1 (explicit error).** If

$$D=1-\epsilon H(N-1)>0,$$

then

$$
\boxed{\left|\frac{U_{N,H}(\epsilon)}{\epsilon}-F\right|
\le \epsilon\left[
 \frac{H\{N(H+1)+F\}}{D}+(N-1)^2F\right].}        \tag{5}
$$

The right side times `N/(N+H)` bounds the corresponding error for `J/epsilon`.
In particular, if `H/N<=R` and `epsilon H(N-1)<=1/2`,

$$
\left|\frac{J_{N,H}(1-\epsilon)}\epsilon
      -\frac{N}{N+H}F_{N,H}\right|
\le (4R^2+3R)\epsilon N^3.                         \tag{6}
$$

No stationary mass-tail estimate, mixing-time estimate, or exclusion of
condensates is used. The cubic power in (6) is an upper bound from this
argument; its optimality is not asserted.

## 2. Exact full-braking relaxation

Use integer lifted heights

$$h_{i+1}-h_i=g_i,\qquad h_{i+N}=h_i+H.$$

They are car positions minus the car index, so a traffic update changes
`h_i` to `h_i+w_i`. Put

$$c_i=\mathbf1_{\{v_i>0,\ g_i\ge2\}}.$$

Not all `c_i` can be one, since that would imply `H>=2N`. For each `i`, let
`r_i` be the length of the consecutive run of ones in `c` starting at `i`
and continuing through `i+1,i+2,...`; it is zero if `c_i=0`. Define

$$
\ell_i=\sum_{k=0}^{r_i-1}(g_{i+k}-1).              \tag{7}
$$

**Lemma 2 (relaxation formula).** If all future `xi` are zero, the total
displacement of car `i` in the next `t` updates is

$$\min\{t,\ell_i\}.$$

The eventual resting heights are

$$\mathcal P(h,v)=h+\ell,$$

and the exact number of updates until all stored velocities vanish is

$$
\mathcal R(g,v)=
\begin{cases}
0,&v_i=0\text{ for every }i,\\
1+\max_i\ell_i,&\text{otherwise}.
\end{cases}                                      \tag{8}
$$

In particular `0<=R<=H`. A full-braking update decreases `R` by exactly one
when `R>0` and leaves the projection `P` unchanged.

**Proof.** If `c_i=0`, car `i` stops at the next full-braking update and can
never restart under full braking. If `c_i=1`, (7) satisfies

$$\ell_i=g_i-1+\ell_{i+1}.$$

Assume the stated displacement formulas up to time `t`. The gap then is

$$g_i(t)=g_i+\min(t,\ell_{i+1})-\min(t,\ell_i).$$

For `c_i=1` and `t<ell_i`, this is at least two: it equals `g_i>=2` before
the leader stops, and subsequently equals `ell_i+1-t>=2`. Thus car `i`
moves one unit. At `t=ell_i` its gap is one, so the next update stops it
permanently. This proves the displacement formulas by induction. The extra
update after the final movement is necessary to reset the stored velocity;
it gives (8), including an initially moving car with gap zero or one.

Every nonempty run in (7) has `ell_i<=H-r_i<=H-1`. This proves `R<=H`.
Deleting the first deterministic update from a trajectory proves both the
descent of `R` and invariance of its final projection. $\square$

This improves the earlier qualitative finite-road absorption argument to
an explicit formula and the bound `H`.

## 3. Exact serialization of simultaneous triggers from rest

Start with every velocity zero. Fix any set of nonbraking coins, and set
`alpha_i=xi_i 1_{g_i>=1}`. Perform that one stochastic update, then full
braking until rest. Let `D_i` be each car's total displacement in this
entire operation, including the first update.

**Lemma 3 (serialization).** The resulting lifted heights are obtained by
performing each triggered nonempty backchip update **exactly once**, in the
following order:

1. Fire all triggered sites whose original gap is one, in any order.
2. In each maximal consecutive block of triggered sites whose original
   gaps are at least two, fire from the upstream end toward the downstream
   end, so `i+1` fires before `i`.

Moreover, for the state just after the first stochastic update,

$$
\mathcal R(g',v')=\max_i D_i
\le\sum_i\xi_i d(g_i).                            \tag{9}
$$

The equality includes the case with no nonempty trigger, when both sides
are zero.

**Proof.** Nontriggered cars remain stopped throughout, so `D_i=0` there.
A triggered original singleton moves once. Its gap immediately afterward
is `alpha_(i+1)<=1`, so it stops at the next full-braking update and
`D_i=1`.

For a triggered site with original gap at least two, Lemma 2 applied after
the first update gives

$$D_i=g_i-1+D_{i+1}.                              \tag{10}$$

For the only borderline case, `g_i=2` and `alpha_(i+1)=0`, it simply gives
`D_i=1`. Otherwise the site remains active after the first update, and
substitution of `g_i'=g_i+alpha_(i+1)-1` into (7) proves (10).

Triggered original singleton firings in step 1 send one unit even if they
have already received one unit from another such singleton: their mass is
then two, which still sends one. No larger triggered gap has fired yet.
Step 2 then has every upstream displacement already delivered when a site
fires. Its donor contains `g_i+D_(i+1)>=2`, and the backchip move sends
exactly `g_i-1+D_(i+1)`, as in (10). The blocks do not form a full cycle,
since all `g_i>=2` is excluded by `H<2N`. This proves the serialization.

Recursing in (10) expresses each nonzero `D_i` as a sum of `d(g_j)` over a
consecutive block of triggered large gaps, possibly followed by a triggered
singleton contributing one. It is therefore bounded by the sum in (9).
After the first update, `D_i=alpha_i+ell_i'`; any nonzero `ell_i'` has
`alpha_i=1`. Formula (8) gives `R(g',v')=max_i D_i`. $\square$

## 4. A stationary bound on being away from rest

Let `A` be the stationary probability that **at least one car** has a
nonzero stored velocity. It is a global event, not the mean fraction of
moving cars. Let `K=sum_i xi_i`, with `K~Binomial(N,epsilon)`.

At a nonrest state, the full-braking update decreases `R` by one. If at
least one nonbraking coin occurs, the new value is at most `H`. Hence

$$
\mathbb E[\Delta\mathcal R\mid g,v]
\le -1+H\Pr(K\ge1)\le-1+\epsilon NH
\quad\text{on nonrest states}.                   \tag{11}
$$

At rest, Lemma 3 gives the sharper bound

$$
\mathbb E[\Delta\mathcal R\mid g,0]
\le\epsilon\sum_i d(g_i)\le\epsilon H.            \tag{12}
$$

This counts simultaneous triggers correctly, rather than charging every
trigger the worst possible relaxation time. Since `R` is a bounded function
on the finite state space, stationary expectation of its increment is zero.
Equations (11)--(12) imply

$$
0\le\epsilon H-A[1-\epsilon H(N-1)].
$$

Consequently, whenever `D>0`,

$$\boxed{A\le\frac{\epsilon H}{1-\epsilon H(N-1)}.} \tag{13}
$$

This is a bound on global rest probability and deteriorates as size grows.
It must not be treated as a size-uniform mixing or local-rest theorem.

## 5. Transfer the reduced current corrector to the full model

The previous [monotone-corrector theorem](../2026-10-22-corrector-audit/README.md)
supplies a function `Phi` of lifted heights with

$$
\Phi(h+c\mathbf1)=\Phi(h)+c,\qquad
\min_i(h_i-z_i)\le\Phi(h)-\Phi(z)\le\max_i(h_i-z_i),\tag{14}
$$

and, for reduced backchip height updates `T_i`,

$$
a_i(h):=\Phi(T_i h)-\Phi(h)\ge0,\qquad
\sum_i a_i(h)=F.                                 \tag{15}
$$

In particular every single corrected backchip increment lies in `[0,F]`,
regardless of how much mass is transferred. These facts concern the reduced
chain only. We do not assume a monotone full-model height evolution.

For clarity, existence of this corrector requires no stationary tail
estimate: all reduced height updates are monotone and commute with common
vertical shifts. The word that double-fires sites `N-1,...,1` gathers every
gap configuration at site zero. Under common Poisson clocks that word
eventually couples any two finite-ring configurations up to a vertical
shift. Taking the limit of expected height minus stationary linear growth
constructs `Phi` and gives (14). The finite-state Poisson equation gives
`sum_i a_i=F`, while monotonicity gives `a_i>=0`. The linked note gives all
details. This is an inherited lemma, not a new claim of this continuation.

Define on full-model lifted states

$$\Psi(h,v)=\Phi(\mathcal P(h,v)).                  \tag{16}$$

The quantity `Psi(h,v)-bar h`, where `bar h=N^(-1)sum_i h_i`, depends only
on the finite state `(g,v)` and is bounded for fixed `N,H`. Under any full
stationary law,

$$\mathbb E\Delta\Psi=\mathbb E\Delta\bar h=U.      \tag{17}$$

This is stationarity of a bounded correction to average displacement, not
an assertion that the lifted heights themselves are stationary.

### Drift at a rest state

A single nonbraking coin at site `i` changes the relaxed height by exactly
`T_i`; its corrected increment is `a_i(h)`. On a mask with `K>=2`, Lemma 3
and (15) show that the entire corrected increment lies in `[0,KF]`.
If `b=(1-epsilon)^(N-1)`, it follows that

$$
\epsilon bF\le
\mathbb E[\Delta\Psi\mid h,0]
\le\epsilon bF+NF\epsilon(1-b).                  \tag{18}
$$

Here `E[K 1_{K>=2}]=N epsilon(1-b)`. Since
`1-b<=(N-1)epsilon`, and `N>=2`,

$$
\left|\mathbb E[\Delta\Psi\mid h,0]-\epsilon F\right|
\le (N-1)^2\epsilon^2F.                          \tag{19}
$$

No stationary distribution of resting configurations occurs in this bound;
the first-order corrected drift is the same for every one of them.

### Drift at any nonrest state

If no coin occurs, Lemma 2 gives `Delta Psi=0`. For an arbitrary mask,
both pre-update and post-update future displacements lie in `[0,H-1]`,
while a traffic update moves a car by at most two. Thus coordinatewise

$$
-(H-1)\le w_i+\ell_i'-\ell_i\le H+1.
$$

The order bound (14) yields `|Delta Psi|<=H+1`. Consequently

$$
\left|\mathbb E[\Delta\Psi\mid h,v]\right|
\le\epsilon N(H+1)\quad\text{on nonrest states}.   \tag{20}
$$

Negative increments are allowed and genuinely occur; they have not been
silently dropped.

### Finish the proof of Theorem 1

Split the stationary expectation (17) between rest and nonrest states.
Using (19)--(20),

$$
|U-\epsilon F|
\le (N-1)^2\epsilon^2F
    +\epsilon\{N(H+1)+F\}A.                      \tag{21}
$$

Substitute (13) and divide by `epsilon`. This is (5). If `D>=1/2`,
`F<=H/N<=R` and `H<=RN`, its right side is at most

$$
\epsilon\{2R^2N^3+3RN^2+2R^2N\}
\le (4R^2+3R)\epsilon N^3.
$$

Multiplying by `N/(N+H)<=1` proves (6). $\square$

## 6. A simultaneous thermodynamic/rare-braking limit

The already proved reduced scalar limit states, uniformly on bounded
density intervals,

$$
\pi_{N,\lfloor\theta N\rfloor}(g_0\ge2)\to Q(\theta),
\qquad
\sup_{0\le\theta\le R}|\pi_{N,\lfloor\theta N\rfloor}(g_0\ge2)-Q(\theta)|
=O_R((\log(4N)/N)^{1/4}).                          \tag{22}
$$

It also establishes continuity of `Q`. This is the inherited
[thermodynamic-limit theorem](../2026-10-24-thermodynamic-limit/README.md),
not reproved or counted as a new result here.

**Corollary 4 (joint limit).** For any sequence in (1), and any choices of
stationary full-model laws at its finite parameters,

$$
\boxed{\frac{J_{N,H}(1-\epsilon)}{\epsilon}
\longrightarrow\frac{\eta-Q(\eta)}{1+\eta}.}       \tag{23}
$$

**Proof.** Condition (1) eventually implies `epsilon H(N-1)<=1/2`, since
`H/N` stays bounded. Equation (6) makes the difference from
`[N/(N+H)]F_(N,H)` tend to zero. Equation (22), continuity of `Q`, and
`H/N->eta` identify the latter limit as (23). $\square$

For `H=floor(eta N)`, the resulting quantitative error is

$$
O_R\!\left(\epsilon N^3+
       (\log(4N)/N)^{1/4}+N^{-1}\right).           \tag{24}
$$

Thus this is more than an unspecified diagonal subsequence obtained from
finite-volume convergence: it gives a stated algebraic relation between
noise and size, with an explicit finite-model error. It remains restricted.
Taking `N->infinity` at a fixed `epsilon>0` violates the hypotheses and
makes the bound unusable. That order of limits is not covered.

## 7. One extra acceleration can reduce eventual travel by order N

**Theorem 5 (pathwise obstruction).** At vacancy density exactly one and
every `N>=6`, there is a state reachable in one update from a resting state
such that replacing one braking decision by a nonbraking decision reduces
one car's eventual full-braking displacement by exactly `N-5`. Every other
car has the same eventual displacement.

**Proof.** Put `M=N-3`, and take

$$
g=(1,2,M,0,\ldots,0),\qquad v=(0,1,1,0,\ldots,0).
$$

Here `H=N<2N`. The state is reached from the resting gaps
`(0,2,M+1,0,...,0)` by nonbraking at sites 1 and 2, with zero-based indices.
Under full braking forever, (7) gives future displacements

$$\ell_1=M,\qquad \ell_2=M-1,$$

and all others zero. Instead allow just site 1 not to brake in the next
update. It moves two, while site 2 moves one. Site 1's new gap is one, so
it stops on the following update and never restarts. Its total displacement
is now two. Site 2 still travels a total of `M-1`, and all other cars remain
stopped. The loss at site 1 is `M-2=N-5`. $\square$

This refutes monotonicity of the relaxed trajectory in the nonbraking coins
and rules out a road-size-independent additive displacement bound for this
coupling. It does **not** refute stationary current monotonicity, a better
averaged comparison, or unrestricted interchange of limits.

It also permits a strictly negative corrected increment in (20). Indeed
`Phi` is strictly increasing between distinct coordinatewise ordered lifted
profiles: choose a coordinate with a strict height difference and a
positive-probability gathering word that leaves that coordinate unchanged.
At the end of that word the two height fields differ by that positive
constant everywhere. Subsequent common-clock updates preserve it, whereas
all other clock realizations preserve nonnegative order. The limiting-shift
construction of `Phi` in (14) therefore gives a strictly positive difference.
The two projected profiles in Theorem 5 are ordered with a strict difference
at site 1, so the extra-coin projected corrected increment is negative.

## 8. Verification and exact scope

Run `python3 verify.py`; it requires only the standard library. The new
audit compares the explicit relaxation and serialized maps against a
separate implementation of all four NaSch update rules. It checks 20
parameter pairs with `N=2,...,5` and `1<=H<min(2N,7)`:

* 18,572 initial gap/activity states and 38,146 explicit relaxation steps;
* 18,572 simultaneous-trigger serializations and their workload bounds;
* 529,232 arbitrary-coin updates and projected-height shift bounds;
* 510,660 active-state workload perturbation bounds;
* 4,495 rational probability/constant checks;
* 101 members of the order-`N` acceleration counterexample family.

The audit also checks the activity quotient against the original local
velocity rule, projection invariance, and the exact rest-time descent.
Results are in `results/verified.json`. No old stationary solver or Poisson
solver was rerun. These finite checks supplement the analytic proofs; they
do not replace the all-parameter arguments or independently validate every
inherited theorem.

The separate standard-library command `python3 verify_flow_bounds.py`
checks the new inequality against four archived exact full-model rational
current functions. Eight nonnegative Bernstein-coefficient certificates
prove both inequalities over the whole intervals
`0<=epsilon<=1/[2H(N-1)]` for `(N,H)=(3,3),(4,3),(5,3),(3,4)`.
This reuses the old formulas as regression fixtures; it does not recompute
them or count them as new stationary solutions.

This continuation proves a quantitative bridge to the **full traffic
model** in a specified joint regime. It does not provide an explicit
general `Q`, remove possible affine phase intervals, decide finiteness of
the critical density, prove a thermodynamic stationary current at fixed
`p`, or justify thermodynamic-first rare-braking interchange. Those remain
open within this project.
