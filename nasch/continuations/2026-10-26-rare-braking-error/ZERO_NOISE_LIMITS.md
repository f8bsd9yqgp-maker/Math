# Classification of possible zeroth-order full-model limits

26 October 2026, continuation of run 19. This note gives a complete local
classification at `p=1` and states precisely what it does and does not imply
for stationary limits with `p` approaching one. It does not assume that the
full-model stationary laws converge to the reduced laws.

## 1. Stationary laws at certain braking

Consider the full `v_max=2` gap/velocity process on the integer car-label
line. Gaps are finite nonnegative integers. Write `a_i=1{v_i>0}`. At
`epsilon=1-p=0`, the update is

\[
w_i=a_i\mathbf1_{\{g_i\ge2\}},\qquad
g_i'=g_i+w_{i+1}-w_i,\qquad v_i'=w_i.                 \tag{1}
\]

**Proposition 1.** Every translation-invariant stationary probability law
for (1) is a mixture of the following two classes:

* all cars resting, with an arbitrary translation-invariant gap law;
* all velocities equal to one, with an arbitrary translation-invariant
  gap law supported on `g_i>=2` at every site.

No first-moment assumption is needed. The mixture weight of the second
class is exactly the stationary mean velocity.

**Proof.** The activity update satisfies `a_i'<=a_i`. Stationarity of this
bounded indicator implies `a_i'=a_i` almost surely. Start a stationary
trajectory and intersect these probability-one events over all sites and
all nonnegative integer times. On that event, activity is constant in
time, `w_i(t)=a_i(0)`, and

\[
g_i(t)=g_i(0)+t\{a_{i+1}(0)-a_i(0)\}.               \tag{2}
\]

The pattern `(a_i,a_{i+1})=(1,0)` is impossible, since (2) would eventually
make the finite gap negative. Translation invariance gives

\[
\Pr(a_i=0,a_{i+1}=1)-\Pr(a_i=1,a_{i+1}=0)
   =\mathbb E a_{i+1}-\mathbb E a_i=0.
\]

Thus `(0,1)` is impossible too. Activity is consequently a single random
constant across the whole line. On its zero event, all velocities are
zero. On its one event, (1) and stationarity give `v_i=1` and `g_i>=2`
at every site. Conditional gap laws are translation invariant, because
the two conditioning events are translation invariant. Conversely, each
of the two displayed classes is stationary: all gaps and velocities are
unchanged by (1). The mean velocity is zero or one in the respective
classes, which proves the last assertion. Square.

## 2. Consequences for simultaneous stationary limits

Let `N_j->infinity`, `H_j/N_j->eta<infinity`, and `epsilon_j->0`. Take any
stationary full-model law on each ring and average it over cyclic car-label
translations if necessary. Averaging preserves its mean velocity and mass.
Extend it periodically to the integer line. Use the notation `U_j` and
`J_j=N_j U_j/(N_j+H_j)` from the main proof.

**Proposition 2.** These gap/velocity laws have local subsequential limits.
Every such limit has the form in Proposition 1 and mean gap at most `eta`.
Along a subsequence converging locally to a law whose moving-class weight
is `alpha`,

\[
U_j\longrightarrow\alpha,\qquad
J_j\longrightarrow\frac{\alpha}{1+\eta},\qquad
0\le\alpha\le\min(1,\eta/2).                       \tag{3}
\]

If `eta<2` and the limiting law is spatially ergodic, then `alpha=0`.

**Proof.** The one-site means are `H_j/N_j`, which are bounded, and
velocities belong to a finite set. Markov's inequality and a union bound
give tightness on each finite set of labels; a diagonal extraction gives
local subsequential limits. Truncation of `g_0` gives limiting mean at most
`eta`.

For a bounded cylinder observable, its one-step update uses only finitely
many sites and coins, independent of road size once the road is long
enough. The probability that any of those coins is nonbraking is at most
their number times `epsilon_j`. Consequently its transition expectation
converges uniformly to the `epsilon=0` transition expectation. Passing
stationarity to the local limit proves invariance under (1). Translation
invariance also passes to the limit. Proposition 1 now applies.

The observable `v_0` is bounded and local, so `U_j` converges to its limiting
expectation, namely `alpha`. This proves the two current limits in (3).
In the moving class `g_0>=2`, so the mean bound gives `2 alpha<=eta`.
Finally, spatial ergodicity makes the translation-invariant moving-class
event have probability zero or one. Its probability cannot be one when
the mean is less than two. Square.

## 3. The limit-exchange gap is not removed

For `eta<2`, a spatially ergodic zero-noise local limit must be resting.
However, finite-ring ergodicity does not prove spatial ergodicity of a
subsequential infinite-volume limit. Proposition 2 therefore does not
establish `U_j->0` along every unrestricted joint sequence, and certainly
does not identify the first-order coefficient `U_j/epsilon_j`.

A nonzero limiting *unscaled* current would require a moving-class
component in this classification. This is a necessary condition, not an
existence proof for such a component. Arbitrary mixtures listed in
Proposition 1 have not been shown to be limits of positive-noise canonical
stationary laws. No counterexample to interchange is claimed.

Even ruling out that component would be only a zeroth-order result. The
user's interchange question requires control on the smaller `epsilon`
scale. The main theorem supplies that control when `epsilon N^3->0`; its
removal still needs a uniform local estimate or another substantive
argument.

This classification is an analytic argument. The local velocity identity
(1) is already included in the new run-19 integer audit; no prior
stationary solver was rerun. Neither this note nor the main theorem has
received independent specialist peer review.
