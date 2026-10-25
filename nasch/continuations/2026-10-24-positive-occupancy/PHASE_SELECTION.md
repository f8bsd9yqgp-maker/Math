# Stationary phase currents and a critical-density alternative

24 October 2026. New continuation of the scalar convergence proof and the
[positive pile-density theorem](README.md). These are complete internally
audited arguments, not independent peer review or a solution of the full
finite-braking NaSch model.

## 1. Statements

Write Q(eta)=lim q_(N,floor(eta*N)) and F(eta)=eta-Q(eta). The preceding
work proves that Q is continuous and nondecreasing on [0,infinity), with
Q(0)=0. The positive-occupancy theorem proves Q(eta)>0 for eta>0.

**Theorem A (phase-current identification).** Every translation-invariant
stationary law nu with deterministic finite spatial density r satisfies

\[
\nu(g_0\ge2)=Q(r),\qquad \mathbb E_\nu d(g_0)=F(r).           \tag{1}
\]

The assertion is conditional on the phase existing; its proof does not
assume existence at all densities.

For a>0 define the largest maximizer

\[
r(a)=\max\operatorname*{argmax}_{r\ge0}\{Q(r)-ar\},
\qquad \eta_c=\lim_{a\downarrow0}r(a)\in(0,\infty].         \tag{2}
\]

The maximum is attained because Q is continuous and bounded and a>0.

**Theorem B (critical-density alternative).**

1. At every positive density r(a), the entire canonical sequence converges
   locally to the unique deterministic-density stationary phase nu_(r(a)).
   The one-site masses are uniformly integrable.
2. At every fixed 0<=eta<=eta_c (every finite eta if eta_c=infinity),
   canonical one-site masses are uniformly integrable. In particular,
   max_i g_i/N tends to zero in probability at those densities.
3. If eta_c<infinity, then Q is constant on [eta_c,infinity), and eta_c is
   the smallest density from which it is permanently constant. The entire
   canonical local law converges at every eta>=eta_c to one stationary
   phase nu_(eta_c), whose mean is exactly eta_c. The escaped mean at
   eta>eta_c is exactly eta-eta_c.
4. Q is strictly increasing on [0,eta_c] (on all finite densities if
   eta_c=infinity). Thus a flat interval can occur only in its final
   saturation plateau.
5. Unconditionally eta_c>=1/217. Therefore uniform integrability and
   absence of an order-N pile are proved for every 0<eta<=1/217.

All canonical statements also hold along arbitrary N_j->infinity and
H_j/N_j->eta. Uniform integrability in item 2 is **not** by itself a claim
of full local-law convergence at every eta<eta_c. That phase-selection
problem remains open. Nor is finiteness or infiniteness of eta_c settled.

## 2. Imported results, with exact scope

We use the following already proved statements; none is newly claimed here.

* [Scalar convergence and height oscillations](../2026-10-24-thermodynamic-limit/README.md):
  q_(N,H)->Q(eta) whenever H/N->eta, uniformly on compact density intervals;
  from balanced heights and times t with 4t<=N, expected height range is
  O_R(t^(3/4)*log(2N)^(1/4)) plus an exponentially small error.
* [Height comparison](../2026-10-24-height-comparison/README.md): the rightmost
  backward dependency path has Z_t~Poisson(t); the complete dependency
  diagram is contained in sites 0,...,Z_t. The height maps preserve order
  and integer vertical shifts. A ring's finite-time expected height speed
  differs from F_(N,H) by at most its expected height range divided by t.
* [Stationary density classification](../../density_phases_proof.md): local
  canonical limits are stationary and translation invariant, have mean at
  most eta, and decompose into unique stationary phases indexed by their
  deterministic finite density. Such phases are spatially mixing. Two
  stochastically ordered stationary translation-invariant laws with the
  same pile probability are identical, even without first moments.
* The [unit-service comparison](../2026-10-22/README.md) gives
  \(Q(r)\le r^2/(1+r)\). Coordinatewise attractiveness gives monotonicity
  of finite canonical laws in total mass.

Standard bounded-cylinder weak convergence, truncation, monotone coupling,
and the spatial ergodic theorem are used explicitly below.

## 3. Flat infinite-line speed

Let h^flat start on the infinite line from h_j(0)=floor(r*j), with h_0(0)=0.
We first prove

\[
\lim_{t\to\infty}t^{-1}\mathbb E h^{\rm flat}_0(t)=F(r).    \tag{3}
\]

Take N=ceil(8t) and H=floor(r*N), so theta_N=H/N differs from r by at most
1/N. Couple the line with the balanced ring on physical sites 0,...,N-1.
Before its rightmost dependency reaches N, the full diagrams agree, and
initial leaf heights differ by at most Z_t/N+1. Monotonicity and vertical
shift invariance give the same bound on the output-height difference.
On the winding event, the respective path bounds are r*Z_line and
 theta_N*Z_ring. The two path counts separately are Poisson(t), and the
winding event is their common event of reaching N. Thus

\[
|\mathbb E h^{\rm flat}_0(t)-\mathbb E h^{N,H}_0(t)|
\le t/N+1+(r+\theta_N)t\Pr(\operatorname{Pois}(t)\ge N-1).
\]

Divide by t. The Poisson error vanishes. The ring current bracket and
oscillation bound show that its finite-time speed differs from F_(N,H)
by O_r((log(t)/t)^(1/4)), which tends to zero. Scalar convergence gives
F_(N,H)->F(r). This proves (3). The case r=0 is immediate.

## 4. Replacing the initial profile by any finite-mean stationary phase

In fact a stationary initial time law is unnecessary in this step. Let the
initial gaps have a translation-invariant law with finite mean r and
almost-sure spatial density r. Define h_0(0)=0 and
h_j(0)=sum_(i=0)^(j-1) g_i for j>=1. Write

\[
D_n=\max_{0\le j\le n}|h_j(0)-\lfloor rj\rfloor|.
\]

The ergodic theorem gives D_n/n->0 almost surely. This convergence also
holds in L1. To check the necessary uniform integrability, D_n/n is bounded
by n^(-1) sum_(i=0)^(n-1) g_i+r+1/n. Averages of identically distributed
integrable nonnegative variables are uniformly integrable without any
independence assumption. Indeed, for X_i with that common law, truncate at
K, write the average as a bounded part <=K plus a tail part of mean
E[X_0 1{X_0>K}], and on an event where the average exceeds M>2K bound its
expected contribution by (1+K/(M-K)) times that tail mean. First choose K,
then M. This proves the assertion and hence E D_n=o(n).

Run the random initial profile and the flat profile with the same future
clocks, independent of the initial configuration. The dependency diagram
and height order give

\[
|h_0(t)-h^{\rm flat}_0(t)|\le D_{Z_t}.                     \tag{4}
\]

Z_t depends only on future clocks and is independent of the initial gaps.
For every epsilon>0 there is a finite C_epsilon such that
E D_n<=epsilon*n+C_epsilon for all n. Therefore
E D_(Z_t)<=epsilon*t+C_epsilon. Equations (3)-(4) yield

\[
\lim_{t\to\infty}t^{-1}\mathbb E h_0(t)=F(r).             \tag{5}
\]

For a time-stationary initial law nu, the compensator gives exactly
E h_0(t)=t E_nu d(g_0)=t(r-nu(g_0>=2)). Its expectation is finite because
0<=d(g_0)<=g_0. Comparing with (5) proves Theorem A.

In particular, if mu is any local canonical limit at density eta and R is
its random spatial density, the earlier density decomposition now gives

\[
\mathbb E R\le\eta,\qquad \mathbb E Q(R)=Q(\eta).          \tag{6}
\]

This strengthens the previous representation by identifying each phase's
pile probability with the same function Q obtained from finite rings.
Equation (6) alone does not force R to be constant.

## 5. Selection at upper supporting-line contact points

Fix a>0, put r_*=r(a), and b=max_(r>=0)(Q(r)-ar). The supporting-line
inequality is

\[
Q(r)\le ar+b\quad(r\ge0),\qquad Q(r_*)=ar_*+b.            \tag{7}
\]

Take any subsequential local canonical limit at density r_*. Apply (6):

\[
0=Q(r_*)-\mathbb E Q(R)
 =a(r_*-\mathbb E R)+\mathbb E[aR+b-Q(R)].                \tag{8}
\]

Both terms on the last line are nonnegative. Consequently E R=r_* and
R is supported on the maximizers in (2). By choice of the **largest**
maximizer, every such R is at most r_*. A bounded-above variable with mean
r_* must equal r_* almost surely. Thus every limit is the unique phase
nu_(r_*), and this argument also establishes that the phase exists.
Tightness and uniqueness identify the whole canonical sequence.

Its first moments converge to the limiting first moment r_*. For each K,

\[
\mathbb E(g_0-K)_+=H/N-\mathbb E\min(g_0,K).
\]

Bounded-cylinder convergence followed by K->infinity proves uniform
integrability (use x*1{x>2K}<=2(x-K)_+). This proves item 1.

## 6. The critical endpoint and uniform integrability below it

For 0<a<b, the two maximizing inequalities imply r(a)>=r(b). Thus the
limit eta_c in (2) exists, possibly infinite. The nonnegative function Q
is bounded and strictly positive at positive density. Moreover,
Q(r)/r->0 at zero by the unit-service upper bound, and Q(r)/r->0 at infinity
by boundedness. Its positive maximum M is therefore attained at a compact
nonempty set of positive densities. At slope a=M, the maximizers of
Q(r)-Mr include zero and that set; their largest member is positive.
Thus eta_c>0.

If eta<eta_c, choose a>0 with r(a)>eta. For all sufficiently large N,
canonical masses at density eta are stochastically dominated by canonical
masses at density r(a). The latter are uniformly integrable by Section 5.
Hence so are the former. This proves item 2 away from a finite endpoint.

Suppose eta_c<infinity. Choose a_j down to zero with r_j=r(a_j) increasing
to eta_c. Couple the finite canonical configurations at masses H_N and
floor(r_j*N) in order whenever H_N is larger. The exact difference of
one-site means is H_N/N-floor(r_j*N)/N. The function (x-K)_+ is increasing
and 1-Lipschitz, so for any H_N/N->eta_c,

\[
\limsup_N\mathbb E_{N,H_N}(g_0-K)_+
\le\limsup_N\mathbb E_{N,\lfloor r_jN\rfloor}(g_0-K)_+
                  +\eta_c-r_j.                          \tag{9}
\]

If the order is reversed for a finite or infinite set of N, domination
alone gives the same estimate with the positive part of the mass difference;
the displayed limit bound is unchanged. First let K->infinity, using the
uniform integrability at r_j, and then let j->infinity. This proves uniform
integrability at eta_c too.

For any density where uniform integrability holds, the union bound gives

\[
\Pr(\max_i g_i\ge\varepsilon N)
 \le N\Pr(g_0\ge\varepsilon N)
 \le\varepsilon^{-1}\mathbb E[g_0\mathbf1_{\{g_0\ge\varepsilon N\}}]
 \longrightarrow0.                                      \tag{10}
\]

This excludes an order-N pile at those densities, not just complete
condensation.

## 7. Canonical law at a finite critical endpoint and above it

Continue with eta_c finite. The phases nu_(r_j) are stochastically ordered:
pass the finite canonical order to their known limits. An ordered coupling
of the countable family exists, by finite ordered couplings and compactness.
Its coordinatewise increasing limit has a law nu_c with

\[
\mathbb E_{\nu_c}g_0=\lim_j r_j=\eta_c.                  \tag{11}
\]

This is monotone convergence in that coupling, not an unsupported exchange
of first moments under weak convergence. The limit is stationary and
translation invariant by the Feller property, and its pile probability is
lim Q(r_j)=Q(eta_c).

It is also spatially mixing. For any bounded cylinder f with k observed
sites, the ordered coupling gives

\[
\Pr(\text{one of those coordinates differs between }\nu_c
                    \text{ and }\nu_{r_j})
 \le k(\eta_c-r_j).
\]

The same bound holds after any spatial shift. Approximate both factors of a
bounded-cylinder correlation of nu_c by their counterparts in nu_(r_j),
use mixing of nu_(r_j), and then let j->infinity. The uniform error tends
to zero. Cylinder approximation extends this to all bounded measurable
observables. Thus nu_c is ergodic, has deterministic density eta_c, and is
the unique phase nu_(eta_c).

Every local canonical limit at density eta_c stochastically dominates
each nu_(r_j), hence nu_c. It has the same pile probability Q(eta_c).
The previously proved strict pile-detection theorem for ordered stationary
laws makes that limit equal to nu_c. This proves full canonical convergence
at eta_c.

For any r>=0 the maximizing property gives

\[
Q(r)-a_j r\le Q(r_j)-a_j r_j.
\]

Let j->infinity. It follows that Q(r)<=Q(eta_c) for every r. Since Q is
nondecreasing, it is constant on [eta_c,infinity). Conversely, if Q is
permanently constant from some r_0 onward, no maximizer of Q(r)-ar for a>0
can exceed r_0; hence eta_c<=r_0. This proves the asserted minimality.

Finally, at eta>eta_c, every local canonical limit stochastically dominates
nu_c and has pile probability Q(eta)=Q(eta_c). Strict pile detection again
identifies it with nu_c. Its mean is eta_c, so its escaped mean relative to
the finite canonical means is precisely eta-eta_c. This proves item 3.
It does not identify the number or geometry of the piles carrying that
escaped mass.

## 8. Strict increase below the critical endpoint

Suppose 0<=eta_1<eta_2<=eta_c and Q(eta_1)=Q(eta_2). Couple their
finite canonical laws in order and extract a joint local subsequence.
The two limiting marginal laws are ordered, stationary, and have equal
pile probability. Strict pile detection makes them identical. But uniform
integrability from Section 6 preserves their respective means eta_1 and
eta_2, a contradiction. Thus Q is strictly increasing below and including
a finite endpoint. Combined with Section 7 this proves item 4.

## 9. An explicit interval without macroscopic piles

The positive-occupancy bound (17) has a useful exact specialization at
theta=1, ell=3 and lambda=log(21/20). In that case

\[
\beta=1/420,\quad m_3=1,\quad B_3=22/63,\qquad
\frac{A_1+\beta B_3}{1-\beta}=\frac{1282}{26397}.
\]

The alternating logarithm series gives

\[
\log(21/20)\ge \frac1{20}-\frac1{800}+\frac1{24000}
                         -\frac1{640000}
 =\frac{93677}{1920000}.
\]

Therefore, for every N>=3,

\[
q_{N,N}\ge 1-\frac{1282/26397}{93677/1920000}
 =\frac{3783923}{824263923}>\frac1{218}.                   \tag{12}
\]

In particular M=max Q(r)/r>=Q(1)>1/218. Let r_* be its largest positive
maximizer. The inherited upper bound Q(r)<=r^2/(1+r) implies

\[
\frac{r_*}{1+r_*}\ge M>\frac1{218},\qquad r_*>\frac1{217}.
\]

Since r_*=r(M)<=eta_c, item 5 follows. This explicit interval is small;
it must not be reported as all 0<eta<2. A sharper choice of parameters can
improve constants, but the critical-density theorem itself is not a
numerical extrapolation.

## 10. Exact remaining boundaries

The scalar limit is proved and is strictly positive. Complete condensation
is excluded at every positive density. Mass uniform integrability is now
proved below the intrinsic critical endpoint eta_c, including at least
0<eta<=1/217; if eta_c is finite, the local canonical law and lost density
are completely identified at and above that endpoint.

What is not established is whether eta_c is finite (a saturation plateau)
or infinite, the exact function Q, and full canonical phase selection at
arbitrary densities below eta_c. No closed T_N formula or unrestricted
finite-braking NaSch current formula is supplied. These are substantive
remaining problems, not steps implicitly covered by Theorems A or B.
