# Height comparison, site removal, and a finite-size convergence criterion

**22 October 2026. Research continuation 9.**

**The fixed-density thermodynamic limit is not proved.** This note proves a
new-to-this-project finite-current bound, its strict version, monotonicity of
current under removal of sites, an exact FIFO departure recurrence, and a
conditional convergence theorem. The missing hypothesis of that theorem is
stated as a conjecture, not inferred from computation. These are AI-assisted,
internally audited arguments, not independently peer-reviewed results. No
literature-priority claim is made.

This continues the [density-phase proof](../../density_phases_proof.md).
It neither replaces that proof nor assumes the missing uniform integrability
or phase-selection estimates in it.

## 1. Model, notation, and status

There are $N\ge2$ sites and $H\ge0$ units of mass. Each site $i$ has a
rate-one Poisson clock. At a ring of that clock it retains

$$r(g_i)={\bf1}_{\{g_i\ge2\}}$$

and transfers $d(g_i)=g_i-r(g_i)$ units to $i-1$, with cyclic indices.
Write $\pi_{N,H}$ for its unique stationary law and

$$q_{N,H}=\pi_{N,H}(g_0\ge2),\qquad
F_{N,H}=\frac HN-q_{N,H}.$$

Here $F$ is the mass current across one bond, not the traffic current per road
site. The uniqueness assertion follows without full irreducibility: a finite
word of clocks gathers all mass at a fixed site, so every state reaches the
same state and there is exactly one closed communicating class. Null clock
rings are included throughout.

The target is convergence of $q_{N,\lfloor\eta N\rfloor}$ along **all**
integers $N\to\infty$, for $0<\eta<2$.

The principal unconditional conclusions here are

$$\boxed{q_{N,H}\le \frac{H(H-1)}{N(H+N-1)}}\qquad(H\ge1),\tag{1.1}$$

with equality for $H=1,2$ and strict inequality for $H\ge3$, and

$$\boxed{F_{N,H}\le F_{N-1,H}}\qquad(N\ge3).\tag{1.2}$$

The second statement concerns current at **fixed mass**. It does not state
that $q$ is monotone along a fixed-density sequence.

The new sufficient condition for convergence is the following pair of
inequalities, whose validity is **unresolved**:

$$q_{kN,k(H-1)+1}\le q_{N,H}+\frac{C_R}{N},
\qquad k\in\{2,3\},\quad H/N\le R.\tag{1.3}$$

For each finite $R$, the constant $C_R$ must be independent of $N,H$.
Proving (1.3) would settle the requested limit, even without first proving
absence of condensates. No such proof is supplied here.

## 2. A monotone cumulative-height representation

Represent a configuration by integer heights on the lifted ring:

$$h_{i+1}-h_i=g_i,\qquad h_{i+N}=h_i+H.$$

A ring of clock $i$ updates all its lifts by

$$h_i\leftarrow B(h_i,h_{i+1}),\qquad
B(a,b)=b-{f1}_{\{b-a\ge2\}},\quad a\le b.$$

The exact identity

$$\boxed{B(a,b)=\min\{b,\max(a+1,b-1)\}}\tag{2.1}$$

shows that the map is nondecreasing in both coordinates and commutes with
addition of an integer constant. It also satisfies $a\le B(a,b)\le b$.
Consequently common-clock evolution preserves coordinatewise order of
heights with the same $N,H$.

This is height order, not coordinatewise order of the masses. They must not
be interchanged. The height increments at site $i$ count exactly the mass
transported from $i$ to $i-1$.

### A finite-time certificate

Start the heights at $a_i=\lfloor Hi/N\rfloor$. For every $t>0$,

$$\left|\frac{\mathbb E h_0(t)}t-F_{N,H}\right|\le\frac Ht.\tag{2.2}$$

To prove this, choose stationary gaps $G\sim\pi_{N,H}$ and their cumulative
heights $z_0=0$, $z_i=\sum_{j=0}^{i-1}G_j$ for $0\le i\le N$.
Both $z_i$ and $a_i$ lie in $[0,H]$ on this interval. Extend them with the
same helical boundary condition. Then $a-H\le z\le a+H$ everywhere.
Height monotonicity preserves these inequalities. Stationarity and the
compensator of clock zero give $\mathbb E z_0(t)=tF_{N,H}$, proving (2.2).

This certificate does not exchange the limits $t\to\infty$ and
$N\to\infty$. At fixed density its error is of order $N/t$.

### An envelope obstruction

Although $B$ is monotone, it does not preserve coordinatewise minima or
maxima. The two admissible pairs $(0,3)$ and $(2,2)$ both have image $2$.
Their coordinatewise minimum $(0,2)$ has image $1$; their coordinatewise
maximum $(2,3)$ has image $3$. Thus a proposed proof that simply commutes the
evolution with a minimum or maximum of height profiles is invalid.

## 3. A solvable comparison and a strict current bound

Consider the unit-service zero-range process on the same ring: at each clock
ring it transfers one unit if the departure site is nonempty. Its height
update is

$$U(a,b)=\min(a+1,b).$$

For every admissible integer pair,

$$B(a,b)\ge U(a,b).\tag{3.1}$$

Both maps are monotone. Starting from identical heights and using the same
clocks therefore gives $h_i^{\rm backchip}(t)\ge h_i^{\rm unit}(t)$ for all
$i,t$. Dividing height increments by time and applying the finite-state
ergodic theorem yields

$$F_{N,H}\ge F^{\rm unit}_{N,H}.\tag{3.2}$$

The unit-service process has the uniform stationary law on the
$\binom{H+N-1}{N-1}$ weak compositions of $H$. For any configuration, the
number of incoming unit-rate transitions equals the number of its positive
coordinates, which is also the outgoing rate. This proves stationarity;
irreducibility proves uniqueness. Counting compositions with $g_0>0$ gives

$$F^{\rm unit}_{N,H}
=\frac{\binom{H+N-2}{N-1}}{\binom{H+N-1}{N-1}}
=\frac H{H+N-1}.$$

Subtracting (3.2) from $H/N$ proves (1.1). For $H=1,2$, every possible mass
is at most two, and the two processes coincide. In particular,

$$q_{N,1}=0,\qquad q_{N,2}=\frac{2}{N(N+1)}.$$

### Quantitative strictness for every $H\ge3$

Set $\ell=2H(N-1)+1$. Then

$$\boxed{
F_{N,H}-\frac H{H+N-1}
\ge\frac{H-2}{\ell N^{\ell-1}}>0.
}\tag{3.3}$$

This deliberately conservative constant is a proof certificate, not a useful
estimate at large $N$.

**Proof.** For an ordered pair of backchip and unit-service heights, let

$$m=\min_{0\le i<N}(h_i^{\rm backchip}-h_i^{\rm unit}).$$

By monotonicity, (3.1), and commutation with constants, $m$ cannot decrease
at a common clock ring.

Let $G$ denote the clock word consisting of $H$ rings at site $N-1$, then
$H$ at site $N-2$, and so on through site $1$, with no ring at site zero.
This gathers every unit at site zero in both processes. Indeed, when a site
is being served its upstream neighbour is held fixed; $H$ services empty it
under either rule. At the end both gap configurations equal $(H,0,\ldots,0)$,
so their height difference is a constant $c\ge m$.

Now ring clock zero once. The backchip process transfers $H-1$ units and the
unit-service process transfers one. Thus the height difference at zero
increases by $H-2$. Apply $G$ again. At each served coordinate both heights
are brought to their respective upstream heights. The increased difference
is copied successively through sites $N-1,N-2,\ldots,1$. Both configurations
again have all mass at zero, and the height difference is now the constant
$c+H-2$.

The word $G,0,G$ therefore increases $m$ by at least $H-2$, whatever the
initial ordered pair. Its length is $\ell$. In the embedded chain the clock
types are independent uniform choices from $N$ sites. Disjoint blocks of
$\ell$ events equal this word with frequency $N^{-\ell}$ almost surely.
All other blocks have nonnegative increments of $m$.

The total clock-event rate is $N$. The long-time growth rate of $m$ is the
difference of the two stationary currents: each height coordinate has the
corresponding current as its growth rate, and the minimum involves only
finitely many coordinates. The resulting lower bound is
$(N/\ell)(H-2)N^{-\ell}$, proving (3.3). $\square$

### Consequences and their limits

For any fixed $\eta>0$, every subsequential limit of
$q_{N,\lfloor\eta N\rfloor}$ satisfies

$$0\le q\le\frac{\eta^2}{1+\eta}.\tag{3.4}$$

For $\eta<1$, this improves the elementary bound $q\le\eta/2$. It is an
upper bound. It supplies no positive lower bound on occupancy, and it is
compatible with complete loss of mean mass in a local limit.

In the already-derived finite-ring rare-braking expansion, the coefficient
of $\epsilon=1-p$ is $F_{N,H}/(1+H/N)$. For $H<2N$, (3.2) therefore gives
the rigorous coefficient bound

$$\frac{F_{N,H}}{1+H/N}
\ge\frac{NH}{(N+H)(N+H-1)}.\tag{3.5}$$

This uses the existing fixed-$N,H$ reduction. It gives no control of its
$O_{N,H}(\epsilon^2)$ remainder uniformly in $N$.

## 4. Increasing a clock rate and removing a site

Give each site a strictly positive rate $v_i$. Its unique stationary current
is the same across every bond, by stationary mass balance:

$$F(v)=v_i\,\mathbb E_v d(g_i).$$

**Clock-rate monotonicity.** Increasing any subset of the rates cannot
decrease $F(v)$.

Indeed, use common Poisson clocks at the smaller rates and additional
independent clocks for the increases. Each additional height update is
nondecreasing, since $B(a,b)\ge a$. Common updates preserve height order.
The long-time current comparison follows as in Section 3.

**Site-removal theorem.** For $N\ge3$, $H\ge0$,

$$F_{N,H}\le F_{N-1,H}.$$

**Proof.** Keep all rates at one except site zero, whose rate is $v\ge1$.
Stationary mass balance and $d(g_1)\le H$ give

$$v\,\mathbb E_v d(g_0)=\mathbb E_v d(g_1)\le H,
\qquad \Pr_v(g_0>0)\le H/v.\tag{4.1}$$

Collapse site zero into its downstream neighbour $N-1$: remove coordinate
zero and replace the last coordinate by $g_{N-1}+g_0$. Denote this map by
$P$. It maps to an $(N-1)$-site ring of mass $H$ and is exactly unchanged
by a clock-zero transition, for every configuration.

For any function $f$ on the reduced finite state space, stationarity gives

$$0=\mathbb E_v L_v(f\circ P)
=\mathbb E_v\sum_{i\ne0}
\bigl[f(P(T_i g))-f(Pg)\bigr].\tag{4.2}$$

Take a subsequential limit as $v\to\infty$. The original finite state space
is compact, and (4.1) forces $g_0=0$ in the limit. On this set, the remaining
terms in (4.2) are exactly the generator of the $(N-1)$-site backchip ring:
in particular, a transfer from site one into the removed site is collapsed
directly into site $N-1$. Therefore every projected limit is stationary for
the reduced chain and must equal $\pi_{N-1,H}$.

Using the rate-one bond at site one,
$F(v)=\mathbb E_v d(g_1)\to F_{N-1,H}$.
Clock-rate monotonicity gives $F_{N,H}\le F(v)$, proving the claim.
$\square$

Iteration gives, for $2\le M\le K$ and any fixed $H$,

$$\boxed{
q_{M,H}\le q_{K,H}+H\left(\frac1M-\frac1K\right).
}\tag{4.3}$$

This is the unconditional cross-size comparison used below. When $K/M\to1$
and $H/M$ stays bounded, its error tends to zero. It does not compare rings
whose masses are scaled with their sizes.

## 5. The finite density bound used in the convergence argument

For completeness, the previously obtained density Lipschitz bound has the
following short finite-state proof:

$$0\le q_{N,H+k}-q_{N,H}\le\frac{2k}{3N}.\tag{5.1}$$

Because $r$ and $d$ are nondecreasing, the common-clock mass coupling
preserves $g\le h$. Start with total masses $H,H+1$; a stationary,
rotation-invariant joint law is obtained by time averaging and averaging
over rotations. Its marginal laws are the respective canonical laws.
There is exactly one extra unit, at a random site $X$.

At site zero put

$$R={\bf1}_{\{X=0,g_0=1\}},\qquad
B_0={\bf1}_{\{X=0,g_0=0\}},\qquad
W={\bf1}_{\{X=0,g_0\ge2\}}.$$

Then $R+B_0+W={\bf1}_{\{X=0\}}$ and
$\mathbb E R=q_{N,H+1}-q_{N,H}$. Define

$$A={\bf1}_{\{X=1,g_0=0,g_1=0\}},\qquad
C={\bf1}_{\{X=0,g_0=0,g_1=0\}}.$$

The only clocks affecting $B_0$ are zero and one. Clock zero creates $B_0$
from $R$, and destroys it from $B_0$. Clock one creates it from $A$, and
destroys it from $B_0$ unless $g_1=0$. Therefore

$$L B_0=R-2B_0+A+C.$$

Stationarity implies $2\mathbb E B_0\ge\mathbb E R$. Since rotation
invariance gives $\Pr(X=0)=1/N$,

$$\frac1N=\mathbb E(R+B_0+W)\ge\frac32\mathbb E R.$$

This proves (5.1) for $k=1$, and telescoping proves it for every $k$.
The proof applies also to $H=0$ and $N=2$.

## 6. A sufficient comparison at just two dilation factors

**Conditional convergence theorem.** Assume that for every finite $R>0$
there is a finite $C_R\ge0$ such that (1.3) holds for all $N\ge2$, $H\ge1$
with $H/N\le R$, and for $k=2,3$. Then for every $\eta>0$ the limit

$$q(\eta)=\lim_{M\to\infty}q_{M,\lfloor\eta M\rfloor}$$

exists. In particular, the requested limit exists on $0<\eta<2$.
The limit is nondecreasing and $2/3$-Lipschitz.

**Proof.** Fix $\eta>0$ and an integer $n\ge2$. Set

$$h=\lfloor\eta n\rfloor+2,\qquad
\alpha=\frac{h-1}{n}>\eta.$$

All repeated dilations of $(n,h)$ have the form

$$K=sn,\qquad L=s(h-1)+1,\qquad s=2^a3^b,\quad a,b\ge0.$$

Their mass densities do not exceed $h/n\le\eta+1$, so choose a fixed
$R>\eta+1$ and apply (1.3) successively. At each step the size increases by
at least a factor two. Thus the sum of all error terms is at most

$$\frac{C_R}{n}\left(1+\frac12+\frac14+\cdots\right)
=\frac{2C_R}{n},$$

and

$$q_{K,L}\le q_{n,h}+\frac{2C_R}{n}.\tag{6.1}$$

For each large $M$, one can choose $s=2^a3^b$ so that
$K=sn\ge M$ and $K/M\to1$ as $M\to\infty$. Here is the needed elementary
number-theoretic fact. Since $\log3/\log2$ is irrational, the fractional
parts of its nonnegative multiples are dense in the circle. For each
$\varepsilon>0$, some finite initial set meets every circular interval of
length $\varepsilon$.
For every sufficiently large $x=\log_2(M/n)$, choose an exponent $b$ from
this finite set whose fractional part lies just above that of $x$, modulo
one. Choosing the corresponding integer $a\ge0$ gives

$$x\le a+b\log_2 3<x+\varepsilon.$$

Hence $1\le K/M<2^\varepsilon$. Letting $\varepsilon$ decrease along a
sequence, with the associated thresholds on $M$, gives the assertion.

Put $H_M=\lfloor\eta M\rfloor$. Since $L=\alpha K+1>\eta M$, mass
monotonicity, (4.3), and (6.1) give

$$\begin{aligned}
q_{M,H_M}
&\le q_{K,H_M}+H_M\left(\frac1M-\frac1K\right)\\
&\le q_{K,L}+\eta\left(1-\frac MK\right)\\
&\le q_{n,h}+\frac{2C_R}{n}
   +\eta\left(1-\frac MK\right).
\end{aligned}$$

Consequently

$$\limsup_{M\to\infty}q_{M,\lfloor\eta M\rfloor}
\le q_{n,\lfloor\eta n\rfloor}
  +\frac{4}{3n}+\frac{2C_R}{n},\tag{6.2}$$

where (5.1) accounts for the extra two units. Choose $n\to\infty$ along a
subsequence attaining the liminf. Equation (6.2) proves limsup equals
liminf. Passing (5.1) to the limit proves the stated monotonicity and
Lipschitz bound. $\square$

### Exact comparison conjecture and a variational formula

The strongest simple candidate tested here is

$$\boxed{q_{kN,k(H-1)+1}\le q_{N,H},\qquad k=2,3.}\tag{6.3}

It is **unproved**. If it holds, the preceding theorem applies with $C_R=0$.
Moreover the same proof gives the exact, but still conditional, formula

$$\boxed{
q(\eta)=\inf_{\substack{n\ge2,\ h\ge1\\(h-1)/n>\eta}}q_{n,h}.
}\tag{6.4}$$

For each admissible $(n,h)$, the preceding dilation and site-removal argument
gives $q(\eta)\le q_{n,h}$. Conversely choose
$h=\lfloor\eta n\rfloor+2$ and use (5.1) and convergence; these terms
approach $q(\eta)$. This proves (6.4) under (6.3).

The stronger joining conjecture

$$q_{N+M,H+K-1}\le\max(q_{N,H},q_{M,K})\tag{6.5}$$

would imply (6.3) by repeated joining. The version with $N+M-1$ sites also
survived the finite tests, but neither version has been proved. Ordinary
joining without the lost unit is false: joining two one-particle systems
produces $q_{N+M,2}>0$, while both original pile probabilities are zero.

The loss of one unit per additional block is therefore substantive, not an
arbitrary rounding choice. No pathwise gluing or independence assertion is
being assumed to justify (6.3).

## 7. An exact FIFO passage-time recurrence

At a single queue, label customers in arrival order, allow simultaneous
batch arrivals, and serve the earliest customers first. At a service epoch,
remove all but the newest customer when at least two are present; remove
the sole customer when only one is present. This realizes exactly the
backchip count dynamics.

Let $A_n$ be the nondecreasing arrival times. The service times are a locally
finite increasing sequence unbounded above, with no arrival-service ties.
Let $S^+(t)$ be the first service time strictly greater than $t$.
For an initially empty queue, set $D_0=-\infty$. Then the departure times
satisfy the exact recurrence

$$\boxed{
D_n=S^+\!\left(\min\{A_{n+1},\max(A_n,D_{n-1})\}\right).
}\tag{7.1}$$

For a finite list of arrivals set $A_{m+1}=+\infty$ at the last customer.

**Proof.** Customer $n$ leaves at a service epoch $s$ once either (i)
customer $n+1$ has already arrived, so $n$ is not the newest customer, or
(ii) customer $n$ has arrived and every earlier customer has departed
strictly before $s$, so it is either alone or again not the newest.
In the second case the condition on earlier departures is equivalent to
$D_{n-1}<s$, by FIFO. These alternatives say exactly

$$s>A_{n+1}\quad\text{or}\quad s>\max(A_n,D_{n-1}).$$

Before customer $n$ departs, the first service satisfying either condition
must remove it. Conversely a service removing it satisfies one of the two
conditions. Taking the first such service proves (7.1). Simultaneous
departures are allowed through the first alternative; the strict successor
in the second alternative prevents incorrectly serving the retained
customer twice at the same epoch. $\square$

This recurrence exposes a precise min-max passage structure. It is not a
closed recurrence for the original three-site first-passage quantity $T_N$,
and no infinite tandem fixed point or stationary traffic formula is deduced
from it.

## 8. Verification, failed shortcuts, and provenance

Run the exact audit from the repository root:

```sh
python3 nasch/continuations/2026-10-22/verify.py
```

It uses Python's standard library and the existing exact finite-ring solver.
The recorded output is [results/verified.json](results/verified.json).
It checks ordered height maps, the strictness word on 79,594 initial pairs,
14,752 FIFO arrival/service patterns, and 48 stationary chains in exact rational
arithmetic. All stationary equations, normalization, and nonnegativity are
checked. Four separate full-state solves validate the rotation quotient.

The same 48 chains give 212 exact checks of (6.5), 374 of its $N+M-1$
variant, and 12 exact checks of (6.3). A stronger exploratory ordering by
$(H-1)/(N-1)$ passes 1,008 exact comparisons. These finite statements are
verified; their universal extensions are conjectures.

The separate SciPy probe solves 174 rotation-quotient chains, with at most
50,000 unquotiented compositions, $N\le12$, $H\le24$. It finds no violation
in 3,405 checks of (6.5), 4,830 checks of the $N+M-1$ variant, and 12,890
checks of the stronger ratio ordering. It checks stationary residuals and
nonnegativity numerically. These are floating-point observations, not
rational certificates. Both the script and its full output are preserved.

To reproduce that larger exploratory run with NumPy and SciPy installed:

```sh
python3 nasch/continuations/2026-10-22/cross_size_probe.py --max-n 12 --max-h 24 --max-compositions 50000
```

A simulation of pile covariances at $H=N$ is also preserved. Its observed
negative values are **not** a proof of negative association, a mixing-time
bound, or a condensation theorem. It has no certified burn-in or uncertainty
estimate and is not used in any proof above.

The investigation also checked two tempting literature shortcuts against
their hypotheses:

* Bahadoran, Guiol, Ravishankar and Saada, *Euler hydrodynamics of
  one-dimensional attractive particle systems* (2006),
  [primary text](https://arxiv.org/pdf/math/0609605), works in its stated
  setup with a finite maximum occupation per site. That theorem cannot
  simply be quoted for this unbounded batch-transfer model.
* Rafferty, Chleboun and Grosskinsky, *Monotonicity and Condensation in
  Homogeneous Stochastic Particle Systems*,
  [primary preprint](https://arxiv.org/abs/1505.02049), imposes stationary
  product-measure assumptions for its condensation results. The present
  process has no such product law available.

The underlying backchip dynamics predates this project: Whitehouse, Costa,
Blythe and Evans, *Maintenance of order in a moving strong condensate*
(2014), [author manuscript](https://arxiv.org/abs/1407.1668). The comparison
arguments here make no claim to have solved that paper's stationary model.

## 9. Precisely what remains unresolved

1. Prove (1.3), or establish a different valid all-size comparison. At present
   the conditional convergence proof has an unproved hypothesis.
2. Alternatively, prove the canonical mass tightness and phase-purity
   estimates in the previous report. The new upper bound (3.4) does not
   supply them. Moving condensates remain neither excluded nor demonstrated
   at fixed $0<\eta<2$.
3. An explicit stationary law, a closed form for $T_N$, and an unrestricted
   stationary Nagel-Schreckenberg traffic formula remain unresolved.

There is no stationary counterexample to the requested limit in this run.
There is also no complete proof of that limit. The new unconditional bounds
and the proved implication in Section 6 should be retained without promoting
the comparisons tested in Section 8 to theorems.
