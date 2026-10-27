# Quantitative local dynamics on the rare-nonbraking time scale

26–27 October 2026. This strengthens continuation 21 from a stationary
generator identity to local finite-dimensional distributions in time.
It does not identify unbounded current or displacement observables.

## 1. Finite-ring statement

Let N>=2, 1<=H<2N, 0<epsilon<=1/2, p=1-epsilon, and
lambda=-log p. Start the full traffic process in any stationary law,
averaged over cyclic car-label shifts. Write X_n=(g(n),v(n)), let
G_n be its exact full-braking gap projection, and put

\[
C=\mathbb P(c_0=1),\quad B=\mathbb P(c_0=1,c_1=0),
\qquad c_i=\mathbf1_{\{v_i>0,g_i\ge2\}}.
\]

Let Z(t) be a continuous-time backchip process on the same ring, with
rate one at every site, initialized by Z(0)=G_0. There is a coupling such
that, with D denoting the number of unequal gap coordinates,

\[
\boxed{
{1\over N}\mathbb E D(G_n,Z(n\lambda))
\le 8\epsilon(C+2B/p+\epsilon)
       \left[n+{\lambda n(n-1)\over2}\right].}     \tag{1}
\]

For a set A of r car labels, cyclic invariance and the projection bound
then give

\[
\mathbb P(g(n)|_A\ne Z(n\lambda)|_A)
\le r\left\{2C+8\epsilon(C+2B/p+\epsilon)
       \left[n+{\lambda n(n-1)\over2}\right]\right\}. \tag{2}
\]

The same coupling works for all n simultaneously. Thus union bounds
give analogous comparisons at any fixed finite collection of times.

## 2. Inputs from continuation 21

Only the following already proved ingredients are used:

1. Full braking projects a state to resting gaps G; if c_i=1 then G_i=1,
   and G_i can differ from g_i only when c_i=1 or c_(i+1)=1.
2. Changing one coin in a full update changes at most four projected
   gaps. If A is the actual projected next state and Q is the projection
   of the same mask update started at rest from G, then
   `D(A,Q)<=8K_mix`. Here K_mix counts marked sites in components of
   `{c=1 or xi=1}` touching c=1.
3. Conditionally on the full state,
   `E K_mix<=epsilon m+2epsilon b/p`, with m=sum c_i and b=sum c_i(1-c_(i+1)).
4. Q is an exact serialized word of backchip moves, one at each marked
   site. Originally empty marked sites can be included first, where they
   do nothing. The serialization depends on the state and mask.
5. At stationarity `B<=epsilon H/N` and, if H/N<=R,
   `C<=U<=(3+6R)epsilon^(1/3)`.

Their proofs are in the preceding
[local reduction](../2026-10-26-gap-balance/LOCAL_STATIONARY_REDUCTION.md)
and [uniform arrest theorem](../2026-10-26-gap-balance/README.md).

## 3. Couple each mask to a short Poisson word

For one time step, take independent rate-one Poisson clocks at every
site on an interval of length lambda. Define xi_i to indicate at least
one event at i. The xi_i are independent Bernoulli(epsilon) variables,
exactly the full-model mask. Denote the number of events by K_i.

Call a marked site bad if K_i>=2 or if one of its neighboring sites is
also marked. Let K_bad be the number of bad sites. All remaining sites
have exactly one event and are isolated from every other marked site.

Let Y be the result of performing the chronological backchip word from
G, while Q is the resting projected mask experiment. Then

\[
D(Q,Y)\le2K_{\rm bad}.                             \tag{3}
\]

Indeed, delete all bad-site firings from both words. The remaining
firings occur once each at pairwise nonadjacent sites, so their update
supports are disjoint and their order is immaterial. They commute with
all deleted firings as well, since none has a marked neighbor. Both
experiments therefore agree outside the set of bad donors and their
immediate recipients; that set has at most 2K_bad coordinates. The
argument also covers originally empty donors and repeated Poisson events.

Using independence at distinct sites and a union bound,

\[
{1\over N}\mathbb E K_{\rm bad}
\le2\epsilon^2+\mathbb P(\operatorname{Pois}(\lambda)\ge2)
\le2\epsilon^2+\lambda^2/2\le4\epsilon^2.          \tag{4}
\]

The last step uses lambda<=epsilon/p<=2epsilon. At N=2 the two
neighbors coincide, which only improves the union bound. For N>=3 the
exact left-hand side is `epsilon-lambda p^3`; for N=2 it is
`epsilon-lambda p^2`. These exact forms are not needed for the theorem.

Combining (3)-(4) with the inherited mixed-coin comparison gives the
stationary one-step error, with Y started from the current G_n,

\[
{1\over N}\mathbb E D(G_{n+1},Y)
\le a:=8\epsilon(C+2B/p)+8\epsilon^2.              \tag{5}
\]

## 4. One-sided propagation gives a polynomial error

Run two backchip chains with common rate-one clocks. A firing at i
changes only i and i-1, and the update at i-1 uses its own mass and the
donor mass at i. Therefore discrepancies can spread only to the left.

For a single initial discrepancy at i, enclose every affected site in
an interval with fixed right endpoint i. Its left endpoint extends by
one only when its own rate-one clock rings. The number of such
extensions by time t, before the interval fills the ring, has the
law of a rate-one Poisson count stopped at N-1. Fresh clock increments
justify this assertion at each successive boundary. The actual
discrepancies are contained in the interval by induction on events.

For several initial discrepancies, take the union of their forward
intervals, using the same clocks. Independence between these intervals
is not needed. An event cannot create a discrepancy outside their union.
Linearity of expectation and the union bound give the stronger estimate

\[
\boxed{\mathbb E D(Z_1(t),Z_2(t))
       \le(1+t)D(Z_1(0),Z_2(0)).}                 \tag{6}
\]

This bound concerns a number of unequal coordinates, not the sum of
their mass differences. It is uniform over all initial masses.

To avoid multiplying these linear bounds at every step, telescope
over the times at which one-step errors are inserted. Write Phi_(s,t)
for the random reduced flow between times s and t, driven by the
already chosen clocks. At the final time n lambda, compare consecutively

`Phi_(k lambda,n lambda)(G_k)`, for k=0,...,n.

The first term is Z(n lambda), and the last is G_n. In the comparison
between k and k+1 the initial discrepancy is exactly the one-step
error in (5), propagated for `(n-k-1)lambda` further units of time.
Those future clock increments are independent of the entire error
configuration at time `(k+1)lambda`. Applying (6), conditioning there,
and summing the triangle inequality proves

\[
{\mathbb E D(G_n,Z(n\lambda))\over N}
\le a\sum_{j=0}^{n-1}(1+j\lambda)
=a\left[n+{\lambda n(n-1)\over2}\right].
\]

All comparisons respect cyclic shifts. The chance of a discrepancy at
a uniformly rooted coordinate is its expected fraction, while original
and projected gaps differ there with probability at most 2C. This proves
(2). The projection need not be a Markov process; only its deterministic
definition and stationarity of the original state have been used.

For reference, the simpler infinitesimal estimate
`L_coup D<=D` also gives the earlier exponential bound
`(exp(n lambda)-1)(8pC+16B+8p epsilon)`. The polynomial bound above is
the stronger large-time conclusion; neither is a mass-distance bound.

## 5. Joint limits and quantitative orders

Take stationary full laws with `N_k->infinity`, `H_k/N_k->eta in (0,2)`,
and epsilon_k->0. Along any subsequence with a local gap limit mu, the
preceding result already proves that mu is reduced-stationary. For
finitely many prescribed reduced times t>=0 put n=floor(t/epsilon).
Then

\[
|n\lambda-t|\le\epsilon+n(\lambda-\epsilon),\qquad
0\le\lambda-\epsilon\le{\epsilon^2\over2p}.         \tag{7}
\]

The discrepancy in (2) tends to zero for every bounded set of times:
`n lambda` stays bounded, C=O_R(epsilon^(1/3)), and B=O_R(epsilon).
Moving the reference observation time from n lambda to t adds at most
`(r+1)|n lambda-t|` to the discrepancy probability for r consecutive
observed gaps. If no direct donor clock for that window rings between
the two times, its gap values cannot change. This proves the time-shift
bound, irrespective of mass sizes.

The reduced ring processes started from G_0 converge locally to the
infinite-line backchip process started from mu. To justify this last
step, truncate the finite-time backward clock diagram to a large fixed
window. Its probability of reaching the truncation boundary tends to
zero with the window size, uniformly in the masses; reaching distance k
requires k ordered nearest-neighbor events and has a factorial tail.
Within that window local initial convergence suffices. The same argument
applies to finitely many times and supports.

Thus the joint laws of the original gaps at those scaled times converge
to the joint laws of the stationary reduced process with initial law mu.
Stored velocities converge to zero at the same finite collection of
observations, by the stationary velocity bound and a union bound.

Put T=n lambda. Since epsilon<=lambda, (1) also gives

\[
{\mathbb E D(G_n,Z(T))\over N}
\le 8(C+2B/p+\epsilon)(T+T^2/2).                 \tag{8}
\]

For eta<=R<1, the synchronous pushing estimate gives `C<=R epsilon/(1-R)`.
Together with B<=R epsilon and p>=1/2, the coefficient in (8) is at most
`8 epsilon[R/(1-R)+4R+1]`. Thus the finite-time local error is
O_(R,T,r)(epsilon), uniformly in N. For the full eta<2 range the
error is O_(R,T,r)(epsilon^(1/3)).

There is also a growing-time consequence on the coupled finite rings.
For a fixed finite set of observation labels and a fixed number of
observation times up to T_epsilon, the discrepancy still tends to zero if

* `T_epsilon=o(epsilon^(-1/6))` in the full bounded-density eta<2 range;
* `T_epsilon=o(epsilon^(-1/2))` when eta<=R<1.

These follow directly from (2), (7), and (8). They compare the full
process with the reduced process on the same ring. They do not assert
uniform convergence of finite-ring reduced processes to an infinite-line
limit on growing time intervals, nor a uniform-in-time path coupling.

## 6. Scope of the dynamic theorem

No assertion is made about Skorokhod convergence of the complete raw gap
paths: rapid multi-step excursions require a separate path-topology
analysis. No mass uniform-integrability or current uniform-integrability
assumption has been established. Bounded local finite-dimensional
observations can miss rare very large transports, and a gap process does
not record a common vertical translation of all lifted heights.

Consequently this theorem does not prove the unrestricted normalized
current formula, select a unique density phase, or establish the
fixed-positive-epsilon thermodynamic current. Those remain separate
requirements for the complete problem.

`verify_dynamic.py` passed 27,922 exact word comparisons, 52,804 coupled
Hamming-drift checks, 5,280 seeded full-projection/word comparisons, and
2,450 rational constant checks. The proof is analytic; these checks do
not extrapolate finite simulations to an infinite system.

The later `verify_cones.py` passed 362,529 exact single-seed event-word
checks and 303 rational telescoping identities for the sharper polynomial
bound. The analytic argument supplies the independent Poisson increments
at the moving boundary and the conditional future-clock step.
