# Every zero-noise local gap limit is backchip-stationary

26 October 2026. This extends the stationary reduction to arbitrary joint
sequences for bounded local observables. It does not identify the
first-order current or assert convergence to the canonical backchip law.

## 1. Statement

Use the notation of [README.md](README.md). Let `N>=2`, `1<=H<2N`,
`epsilon=1-p in (0,1)`, and take any stationary law of the full parallel
traffic process. Let mu be its gap marginal averaged over cyclic shifts.
Let C and B be its averaged qualified-site and 10-boundary probabilities.

For a gap configuration g, define the backchip update T_i by transferring

\[
d(g_i)=g_i-\mathbf1_{\{g_i\ge2\}}
\]

from site i to site i-1. Each site fires at rate one. Write

\[
Lf(g)=\sum_i\{f(T_i g)-f(g)\}.                       \tag{1}
\]

If f depends on r consecutive gaps and `||f||_infinity=M`, only r+1
summands can be nonzero. For N>2r+2 the following estimate holds:

\[
\boxed{
|\mu Lf|\le [16r+8(r+1)^2]MC
             +{32rM B\over p}+8r(r+1)M\epsilon.}    \tag{2}
\]

Together with the uniform bounds `C<=(3+6R)epsilon^(1/3)` and
`B<=epsilon R`, (2) tends to zero uniformly over these road sizes when
H/N<=R and epsilon->0.

**Theorem.** Suppose `N_k->infinity`, `H_k/N_k->eta in (0,2)`, and
`epsilon_k->0`, with no relation between their rates. Every local
subsequential limit of the cyclically averaged full stationary laws is
supported on all velocities zero. Its gap marginal is translation
invariant and stationary for (1), and has mean at most eta.

Neither existence of a limiting gap mean equal to eta, nor uniqueness
of this gap marginal, is claimed. In particular (2) is a local stationary
reduction, not an unrestricted identification of J/epsilon.

## 2. Projection is Lipschitz in the number of changed coordinates

Under full braking, qualified cars coast until they stop. Because H<2N,
the binary word c has a zero. If r_i is the length of its run of ones
starting at i in the direction i+1, define

\[
\ell_i=\sum_{k=0}^{r_i-1}(g_{i+k}-1),\qquad
G_i=g_i+\ell_{i+1}-\ell_i.                          \tag{3}
\]

The resting gap configuration is G. The
[earlier relaxation proof](../2026-10-26-rare-braking-error/README.md)
shows that each car travels exactly ell_i in the subsequent all-braking
evolution. In particular the projection is unchanged by a full-braking
step. Two useful direct consequences of (3) are

\[
c_i=1\ \Longrightarrow\ G_i=1,
\qquad G_i\ne g_i\ \Longrightarrow\ c_i=1\text{ or }c_{i+1}=1.
                                                               \tag{4}
\]

Let `D={i:(g_i,v_i)!=(h_i,u_i)}` for two traffic states on the same ring,
each with at least one unqualified site. Let G and K be their resting gap
projections. Then

\[
\boxed{\#\{i:G_i\ne K_i\}\le2|D|.}                 \tag{5}
\]

**Proof.** Outside D, the original gap and qualification agree. A site
qualified in both states projects to one in both. At a site unqualified
in both, its projection is its own gap plus the sum of gap-minus-one
along the immediately following qualified run. If this projection
differs, that run must meet D before an unchanged unqualified site.
Assign the site to the first such element of D. This assignment is
injective: an intervening unchanged unqualified site would stop the run.
Thus at most |D| sites outside D can differ; at most |D| sites inside D
can differ. Square.

Flipping one coin in a single full traffic update changes only the gaps
at i-1 and i and the new velocity at i. Applying (5) after that update
shows that its **projected gap configuration** changes at most four
coordinates. This bound has no dependence on gap sizes or qualified-run
lengths. It is not a bound on transported mass or lifted heights.

## 3. Only coins connected to old activity cause disagreement

Fix a traffic state X with qualification c and projected gaps G. Given
a mask xi, let A(xi) be the projected gap configuration after updating X
with xi. Let Q(xi) be the projected gap configuration after updating the
resting state `(G,0)` with the same mask.

On the cyclic nearest-neighbor graph, take the connected components of
`{i:c_i=1 or xi_i=1}`. Let K_mix be the number of marked sites in
components containing at least one old qualified site. Remove precisely
these marked coins to obtain a mask zeta.

Then `A(zeta)=Q(zeta)`. To see this, the remaining components contain
either only old qualification or only coins. In the first type there is
only full braking, which preserves the projection. In a coin-only
component every marked site and its next leader have c=0, so their gaps
agree with G by (3). Sites separating components are unqualified and
unmarked, and stay stopped throughout this one-update/full-braking
experiment. Consequently the coin-only evolution has the same resting
outcome in both experiments. This also covers c identically zero.

Deleting each coin changes A at most four coordinates by (5), and the
same holds for Q. The triangle inequality gives

\[
\#\{i:A(\xi)_i\ne Q(\xi)_i\}\le8K_{\rm mix}.        \tag{6}
\]

For fixed c let `m=sum c_i`, `b=sum c_i(1-c_(i+1))`. Marked qualified
sites contribute expectation epsilon m. A zero run of length l between
qualified sites is connected to qualification only through a consecutive
marked path from one of its ends. For the site at distance d from its
left end this probability is at most
`epsilon^d+epsilon^(l+1-d)`. Summing over the run gives at most
`2epsilon/p`. There are b zero runs when c contains both values; when
c is zero everywhere the contribution is zero. Therefore

\[
\boxed{\mathbb E[K_{\rm mix}\mid X]
          \le\epsilon m+2\epsilon b/p.}            \tag{7}
\]

This is the improvement over charging the full lengths of mixed
components: the number of changed projected coordinates can be charged
to marked coins alone.

## 4. An extensive cylinder observable

Let `F_f(g)=sum_j f(tau_j g)`, with f supported on r consecutive sites
and norm M. A change at one gap alters at most r summands, each by at
most 2M. Equations (6)-(7) imply

\[
|\mathbb E[F_f(A)-F_f(Q)]|
\le16rM\epsilon N(C+2B/p).                         \tag{8}
\]

It remains to expand the resting experiment Q to first order in epsilon.
The exact serialization lemma from the earlier relaxation proof writes Q
as a sequence of backchip moves, each marked site fired once. One may
include originally empty marked sites first, since those firings do
nothing; original singletons come next and marked larger gaps fire in
leader-to-follower order inside each consecutive block. H<2N ensures a
break in any all-large-gap cyclic block. Thus the statement covers all
coin masks, including all sites marked.

Write `Delta_i F_f(g)=F_f(T_i g)-F_f(g)`. This difference involves at
most r+1 summands, so `|Delta_i F_f|<=2(r+1)M`. It depends only on gaps
in `[i-r,i+r-1]` (indices cyclically). A preceding firing k can alter
this difference only if its changed coordinates k-1,k meet that interval,
which requires `k in [i-r,i+r]`. Apart from i itself there are 2r such
sites under our size assumption.

Telescope along the serialization. If no previous nearby marked site
exists, the i term is exactly `Delta_i F_f(G)`. Otherwise its error is
at most `4(r+1)M`, and can be charged to a pair of distinct nearby marked
sites. There are at most 2rN ordered pairs, each present with probability
epsilon^2. It follows that

\[
\left|\mathbb E\left[F_f(Q)-F_f(G)
 -\sum_i\xi_i\Delta_iF_f(G)\right]\right|
\le8r(r+1)MN\epsilon^2.                            \tag{9}
\]

This does not require independence of the serialization order from the
mask or state. The deterministic error charge is bounded by the number
of nearby marked pairs before any expectation is taken.

The fresh coins are independent of G. Since X is stationary, its
projected law is stationary under this projected one-step observation:
`E[F_f(A)-F_f(G)]=0`. Divide the combination of (8)-(9) by epsilon N.
If mu_P denotes the cyclically averaged law of G, linearity and cyclic
averaging give

\[
|\mu_P Lf|\le16rM(C+2B/p)+8r(r+1)M\epsilon.         \tag{10}
\]

Here the projection need not itself be a Markov process; equality of its
one-time laws is all that stationarity requires.

## 5. Remove the projection and pass to infinite volume

By (4), at any fixed coordinate the original and projected gaps differ
with probability at most 2C under cyclic averaging. The generator Lf
depends on r+1 consecutive sites and has norm at most `2(r+1)M`.
A union bound therefore gives

\[
|\mu Lf-\mu_P Lf|\le8(r+1)^2MC.                    \tag{11}
\]

Combining (10)-(11) proves (2). The uniform velocity theorem proves
`C->0`, while (6) of README gives `B<=epsilon H/N`. Thus every local
gap limit nu satisfies `nu Lf=0` for every bounded cylinder f. Such
functions and their generator images are bounded continuous functions
on the product of the discrete gap spaces, so these expectations pass
to local weak limits. Truncation gives `E_nu g_0<=eta`.

For completeness, this generator condition implies invariance for the
infinite-volume backchip process. Its rate-one nearest-neighbor graphical
construction is well-defined: an influence path reaching k sites in
finite time requires k ordered clock events, with a factorial tail.
For f supported on r consecutive sites, Lf is supported on at most r+1
consecutive sites and

\[
\|L^k f\|_\infty\le2^k{(r+k)!\over r!}\|f\|_\infty.
\]

Repeated Dynkin formulas yield the Taylor expansion of the semigroup
S_t with remainder at most `t^k ||L^k f||/k!`. For t<1/2 this tends to
zero. Since each `L^(k-1)f` is again a bounded cylinder function,
`nu L^k f=0` for every k>=1. Hence `nu S_t f=nu f` for t<1/2.
The semigroup property extends invariance to all t, and cylinder
functions determine the law. This proves the theorem.

## 6. What is still needed for the requested current formula

By the project's earlier reduced-process classification, the gap limit
is consequently a mixture of the existing deterministic-density reduced
stationary phases, with mean at most eta. This last description is
conditional on the correctness of that inherited classification; the
new stationarity proof above does not use it.

The theorem does not prove that the mixture is the canonical limit at
eta, or that it retains eta units of mean gap. It also does not pass a
current observable through the limit. The Hamming estimate (5) controls
how many gaps change, not how much mass they contain or how far a
projected height moves. Rare interference with a large moving block can
still carry a large correction to first-order current. Dividing the
vanishing-velocity bound by epsilon is insufficient.

In particular, the known restricted theorem under `epsilon N->0` has
not been upgraded to unrestricted convergence of
`J/epsilon` to `(eta-Q(eta))/(1+eta)`. Identifying that coefficient,
settling residual phase mixtures/condensation, and obtaining a general
stationary-flow formula remain open.
