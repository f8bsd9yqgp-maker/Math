# Order, synchronization, and density phases for the unit-rate backchip process

AI-assisted mathematical research; internal proof audit completed
22 October 2026. Independent specialist review and publication-priority
verification remain outstanding.

**Scope.** This note proves structural statements for the explicitly defined
continuous-time process below. It does **not** prove the arbitrary-size
fixed-density canonical limit, and it does not solve the unrestricted
Nagel–Schreckenberg traffic model. All model-specific arguments needed for
the stated theorems are supplied here. Standard probability tools used are
the ergodic and martingale convergence theorems, regular conditional laws on
standard Borel spaces, tightness, the Poisson compensator, and Fatou's lemma.
The finite computations accompanying this note are audits, not substitutes
for these proofs.

## 1. Model and conventions

The state space is $X=\mathbb N_0^{\mathbb Z}$, with the product of the
discrete topologies. Every coordinate is finite. At each site $i$, an
independent rate-one Poisson clock performs the update

$$
(g_i,g_{i-1})\longmapsto(r(g_i),g_{i-1}+d(g_i)),\qquad
r(n)=\mathbf1_{\{n\ge2\}},\quad d(n)=n-r(n).                 \tag{1}
$$

Write $T_i$ for this map. Since both $r$ and $d$ are nondecreasing,
applying the same clocks to two ordered configurations preserves their order.
This is the **common-clock coupling**. Its fresh future clocks are independent
of the initial pair.

“Stationary” means invariant under time evolution; “translation invariant”
means invariant under integer spatial shifts. All couplings called
translation invariant are invariant under simultaneous shifts of the pair.

The graphical process is defined on all of $X$. For a finite set of sites
and a fixed finite time interval, dependence on the initial configuration
can extend $k$ sites upstream only if a time-ordered sequence of clocks
crosses those $k$ sites. For any fixed sequence of $k$ distinct adjacent
sites, the expected number of such ordered event sequences in an interval
of length $t$ is $t^k/k!$. A union bound over the finitely many observation
sites bounds the probability of a dependency reaching distance $k$ by a
constant times this quantity. The dependency is therefore finite almost
surely, uniformly in the initial mass values. This constructs the process
as a consistent limit of finite dependency regions. It also gives
nonexplosive, cadlag coordinate paths and one-sided dependence: site $i$
uses only initial states and clocks at sites $j\ge i$.

For almost every fixed clock realization, convergence of initial states in
the product topology gives convergence of all terminal coordinates, because
each depends on finitely many initial coordinates. Bounded convergence then
shows that the Markov semigroup maps bounded continuous functions to bounded
continuous functions. Thus the process, and its common-clock coupling, are
Feller. The same dependency estimate gives uniformly accurate finite-site
approximations of the semigroup on bounded cylinder functions.

For a translation-invariant law with $\mathbb E g_0<\infty$, define

$$
\mathcal R(g)=\lim_{L\to\infty}\frac1L\sum_{i=0}^{L-1}g_i.    \tag{2}
$$

The spatial ergodic theorem gives this limit almost surely and in $L^1$.
It is the conditional expectation of $g_0$ given the spatial invariant
sigma field. **Deterministic spatial density $\rho$** in this note means
both $\mathbb E g_0<\infty$ and $\mathcal R=\rho$ almost surely.
Consequently $\mathbb E g_0=\rho$. Merely specifying the mean does not
specify a deterministic spatial density.

For a law $\mu$ write

$$
q(\mu)=\mu(g_0\ge2),\qquad
F(\mu)=\mathbb E_\mu d(g_0)=\mathbb E_\mu g_0-q(\mu),       \tag{3}
$$

where the expression for $F$ will be used only at finite mean.

## 2. Stationary common-clock couplings are globally ordered

**Theorem 1.** Suppose the joint law of $(g,h)$ is translation invariant and
stationary for the common-clock process on $X\times X$. Then

$$
g\le h\quad\text{or}\quad h\le g\qquad\text{almost surely}. \tag{4}
$$

No integrability hypothesis is required.

**Proof.** Define, coordinatewise,

$$
\delta=h-g,\quad R=r(h)-r(g),\quad D=d(h)-d(g).
$$

Monotonicity gives

$$
\delta_i=R_i+D_i,\quad R_iD_i\ge0,\quad |R_i|\le1,
\quad |\delta_i|=|R_i|+|D_i|.                              \tag{5}
$$

For an integer $M\ge1$ put

$$
f_M(x)=\min(|x|,M),\qquad
c_M(x,y)=f_M(x)+f_M(y)-f_M(x+y)\ge0.
$$

The last inequality is subadditivity. Equation (5) gives the exact identity

$$
f_M(R_i)+f_M(D_i)-f_M(\delta_i)
=\mathbf1_{\{|R_i|=1,\ |D_i|\ge M\}}.                    \tag{6}
$$

Only clocks 0 and 1 alter $\delta_0$. Stationarity applied to the bounded
cylinder $f_M(\delta_0)$ yields

$$
0=\mathbb E[f_M(R_0)-f_M(\delta_0)
            +f_M(\delta_0+D_1)-f_M(\delta_0)].
$$

Translation invariance and (6) therefore give

$$
\mathbb E c_M(\delta_0,D_1)
=\Pr(|R_0|=1,|D_0|\ge M).                                \tag{7}
$$

The right side tends to zero because the coordinates are finite. Fatou's
lemma applies to the nonnegative left-side integrands and implies

$$
\mathbb E\big[|\delta_0|+|D_1|-|\delta_0+D_1|\big]=0.       \tag{8}
$$

This is the expectation of one nonnegative variable, not a subtraction of
possibly infinite expectations. Its integrand equals

$$
2\min(|\delta_0|,|D_1|)\mathbf1_{\{\delta_0D_1<0\}}.
$$

Thus the probability of an opposite-sign incoming and receiving discrepancy
is zero. Stationarity and the Poisson compensator, applied to the indicator
of that event at each site, show that almost surely no clock ever performs
such a cancellation in a bounded space-time window. Countably many windows
and sites cover all nonnegative times and all clocks.

Suppose both discrepancy signs occurred somewhere with positive probability.
Some fixed finite interval $[a,b]$ would contain both signs with positive
probability. Freeze clocks $a$ and $b+1$ and prescribe the finite word

$$
T_b^2,T_{b-1}^2,\ldots,T_{a+1}^2.                          \tag{9}
$$

Also silence all unwanted clocks in this interval. These requirements have
positive probability in a fixed time interval, independently of the initial
pair. Two consecutive firings empty any donor: its first residual is either
0 or 1 and its second residual is 0. Hence (9) gathers all interval mass
at $a$, separately in the two configurations.

The total absolute discrepancy on the interval changes from
$\sum_{a}^{b}|\delta_i|$ to $|\sum_{a}^{b}\delta_i|$, which is strictly
smaller when both signs are present. Each donor split preserves absolute
discrepancy by (5). Only opposite-sign addition at a destination can decrease
it, and no mass crosses the frozen boundaries. The word must therefore
produce a cancellation, contradicting (8). This proves (4). $\square$

## 3. Synchronization and uniqueness at deterministic density

**Theorem 2.** Let $\mu,\nu$ be translation-invariant stationary laws with
deterministic spatial densities $\rho,\sigma$, as defined in Section 1.
Starting from any translation-invariant coupling, use common clocks. Then

$$
\lim_{t\to\infty}\mathbb E|H_0(t)-G_0(t)|=|\sigma-\rho|.    \tag{10}
$$

In particular, there is at most one such stationary law at each finite
density. At equal density the coupled copies synchronize locally in $L^1$.
Existence at every density is not asserted.

**Proof.** Let $a(t)=\mathbb E|\delta_0(t)|$, with the notation of (5).
The donor clock changes $|\delta_0|$ by $-|D_0|$; the incoming clock changes
it by $|\delta_0+D_1|-|\delta_0|$. All these increments are integrable:
their absolute values are bounded by donor discrepancies, which in turn are
bounded by the sum of the two corresponding masses. The stationary marginals
have fixed finite first moments. The Poisson compensator and translation
invariance give

$$
a(t)=a(0)-2\int_0^t
\mathbb E\left[
\min(|\delta_0(s)|,|D_1(s)|)
\mathbf1_{\{\delta_0(s)D_1(s)<0\}}
\right]ds.                                                \tag{11}
$$

Pre-event values are understood in this integral. Thus $a$ is nonincreasing
and $a(t)\ge|\sigma-\rho|$.

Let $\lambda_t$ be the joint law and
$\overline\lambda_T=T^{-1}\int_0^T\lambda_t\,dt$. Their marginals are
the fixed laws $\mu,\nu$, so this family of couplings is tight. Any weak
limit of $\overline\lambda_T$, along $T\to\infty$, is translation
invariant and stationary for the coupled process. Indeed, for its semigroup
$P_s^c$ and bounded continuous $f$,

$$
|\overline\lambda_T P_s^c f-\overline\lambda_T f|
\le 2s\|f\|_\infty/T,
$$

and Feller continuity passes this identity to the limit.

By Theorem 1, the limiting coupling is globally ordered. To identify its
direction, partition it into the two disjoint translation-invariant events
$A=\{g\le h\}$ and $B=\{h\le g,\ g\ne h\}$, ignoring a null set.
On either event of positive probability, the conditional marginals remain
translation invariant, integrable, and have almost-sure densities
$\rho,\sigma$. The spatial ergodic theorem makes their conditional means
$\rho,\sigma$. An order opposite to their density difference is impossible.
If the densities agree, any ordered discrepancy has zero mean and hence is
zero at all sites almost surely. In all cases the limiting coupling has
expected one-site absolute discrepancy $|\sigma-\rho|$.

This expectation passes to every weak limit: for every coupling with the
fixed marginals, $|h_0-g_0|\le g_0+h_0$, and

$$
(g_0+h_0)\mathbf1_{\{g_0+h_0>K\}}
\le2g_0\mathbf1_{\{g_0>K/2\}}+
   2h_0\mathbf1_{\{h_0>K/2\}}.                            \tag{12}
$$

The right-side expectations tend to zero uniformly over these couplings.
This proves uniform integrability. Therefore the Cesaro mean of $a(t)$
tends to $|\sigma-\rho|$; monotonicity of $a$ proves (10).

At equal density and for a bounded cylinder $f$ involving $k$ sites,

$$
|\mu f-\nu f|\le\operatorname{osc}(f)
\Pr(\text{some observed coordinates differ})
\le\operatorname{osc}(f)\,k\,a(t).
$$

The last step uses integer-valued discrepancies and translation invariance.
Letting $t\to\infty$ proves equality of the laws. $\square$

**Important scope of (12).** Both marginal distributions are fixed. This
does not prove uniform integrability for canonical laws whose road sizes
and total masses vary.

## 4. Representation by the clocks and mixing

**Theorem 3.** Every stationary law with deterministic finite spatial density
has the following properties:

1. Its time-zero state is a spatially equivariant measurable function of the
   past independent Poisson clocks. Coordinate $g_i(0)$ uses only clocks at
   sites $j\ge i$ and times at most zero.
2. Its full stationary path is a space-time equivariant measurable function
   of the two-sided Poisson field.
3. The spatial law and the time-stationary path law are mixing under their
   respective shifts. The upstream spatial tail is trivial.

All measurability and tail assertions are up to completion. No finite coding
radius or quantitative convergence rate is asserted.

**Proof.** Construct a two-sided stationary graphical process with marginal
law $\mu$. On any bounded time interval this is obtained by sampling $\mu$
at its left endpoint and independent clocks thereafter. Invariance of $\mu$
makes these distributions consistent under restriction, providing the
two-sided extension with fresh clocks independent of the state at each
deterministic starting time.

Let $\mathcal F_T$ be the sigma field of all site clocks in $(-T,0]$.
Given these clocks, the terminal state is obtained by evolving an independent
$\mu$-distributed seed at $-T$. Two conditionally independent terminal
states therefore have exactly the law of independent stationary seeds run
for time $T$ under common clocks. For a bounded function $f$ of coordinate
zero, conditional variance gives

$$
\mathbb E\operatorname{Var}(f(G_0(0))\mid\mathcal F_T)
=\tfrac12\mathbb E[(f(G_0^{(T)})-f(H_0^{(T)}))^2]\to0.      \tag{13}
$$

The convergence follows from (10), because a nonzero discrepancy has
magnitude at least one. Apply the increasing-sigma-field martingale theorem
along integer $T$. Equation (13) says that each indicator
$\mathbf1_{\{G_i(0)=n\}}$ equals its conditional expectation given all
past clocks. Countably many sites and integer values then give a measurable
representation of the state.

For finite $T$, conditional expectation over the independent initial seed
uses only the clocks at $j\ge i$, by one-sided dependence. Its martingale
limit has the same measurability. Translation invariance allows the same
conditional-expectation construction at every site, so versions can be
chosen spatially equivariant. Apply the construction at all rational times
and use the cadlag coordinate paths to recover the whole path. Uniqueness of
conditional expectations and space-time stationarity give equivariance
under space and time translations (modulo null sets for each shift).

Complete clock histories are independent and identically distributed across
sites. Their spatial shift is mixing: approximate any two bounded measurable
observables in $L^2$ by observables involving finitely many sites; far enough
spatial shifts make these approximations independent. The Poisson field is
also mixing under time shifts, by approximation with observables involving
finitely many sites and bounded time windows; disjoint windows are
independent. Equivariant measurable factors inherit both mixing statements.
For example, for bounded state observables $f,h$,

$$
\lim_{k\to\infty}\mathbb E_\mu[f(g)h(\theta^k g)]
=\mu(f)\mu(h).                                            \tag{14}
$$

Finally, $\sigma(g_i(0):i\ge n)$ is contained in the sigma field of past
clocks at $j\ge n$. The intersection of these independent-coordinate tail
sigma fields is trivial. This proves the state-tail assertion. $\square$

**Corollary 3.1.** For any countable collection of existing deterministic
finite-density stationary laws, their stationary translation-invariant
common-clock joining is unique and ordered by density.

**Proof.** Realize each marginal as the clock function just constructed on
the same Poisson field. This gives a stationary joining. In any other
stationary common-clock joining, the marginal conditional-variance proof
forces the same clock functions, so the joint law is the same. Theorem 1
orders each pair and the conditional-mean argument in Theorem 2 fixes the
direction. Countability permits simultaneous versions. $\square$

## 5. All finite-mean stationary laws decompose by density

**Theorem 4.** Let $\mu$ be translation invariant and stationary, with
$\mathbb E_\mu g_0<\infty$. Let $\kappa$ be the distribution of
$\mathcal R$ in (2). Then

$$
\mu=\int\nu_\rho\,\kappa(d\rho),                          \tag{15}
$$

where, for $\kappa$-almost every $\rho$, $\nu_\rho$ is the unique
stationary law with deterministic spatial density $\rho$. Each is mixing
as in Theorem 3. This is the spatial ergodic decomposition. In a stationary
graphical realization, the density is conserved in time, independent of all
Poisson clocks, and together with the clocks determines the whole path.

**Proof.** Let $J_i(t)$ be the mass sent from $i$ to $i-1$ during $(0,t]$.
For each $L$, conservation gives the pathwise identity

$$
\sum_{i=0}^{L-1}(g_i(t)-g_i(0))=J_L(t)-J_0(t).              \tag{16}
$$

The Poisson compensator and stationarity give
$\mathbb E J_i(t)=tF(\mu)<\infty$. The $L^1$ distance between the two
block averages in (16) is at most $2tF(\mu)/L$. Passing to their $L^1$
limits yields, for each fixed $t$,

$$
\mathcal R(g(t))=\mathcal R(g(0))\quad\text{almost surely}. \tag{17}
$$

Disintegrate $\mu$ by $\mathcal R=\rho$. Shift invariance of
$\mathcal R$ implies translation invariance of the conditional laws.
For bounded $f,\psi$, the Markov property, stationarity, and (17) give

$$
\mathbb E[\psi(\mathcal R(G_0))P_t f(G_0)]
=\mathbb E[\psi(\mathcal R(G_t))f(G_t)]
=\mathbb E[\psi(\mathcal R(G_0))f(G_0)].
$$

Use rational $t\ge0$ and a countable determining family of cylinder
indicators. Outside one $\kappa$-null set, each conditional law is invariant
at all such times; stochastic continuity extends invariance to every time.
Moreover,

$$
\mathbb E[g_0\mid\mathcal R]=\mathcal R,
$$

by the conditional-expectation formulation of the spatial ergodic theorem.
The conditional laws thus have finite mean $\rho$ and deterministic density
$\rho$. Theorems 2 and 3 identify them as unique mixing laws $\nu_\rho$.
Mixing implies spatial ergodicity, so (15) is the spatial ergodic
decomposition.

For the assertion about noise, fix any finite time window $[a,b]$. The
density at time zero equals that at $a$ almost surely, by the shifted form
of (17). The latter is independent of the fresh clocks in $(a,b]$. Taking
finite clock-cylinder events and then a monotone class shows that
$\mathcal R$ is independent of the entire two-sided clock field. Applying
(13) conditional on $\mathcal R$ makes its expected conditional variance
tend to zero at $\kappa$-almost every density; bounded convergence permits
integration over $\kappa$. The martingale theorem now gives a jointly
measurable state and path representation from $(\mathcal R,\text{clocks})$.
This avoids choosing unrelated versions at uncountably many densities.
$\square$

**Corollary 4.1.** The upstream spatial tail of a finite-mean stationary law
is exactly $\sigma(\mathcal R)$, up to completion.

**Proof.** The density is recovered by block averages starting arbitrarily
far upstream, so it belongs to the state tail. Conversely, one-sidedness of
the conditional representation puts the state at sites $i\ge n$ inside
$\sigma(\mathcal R,\omega_j:j\ge n)$, with iid past clock histories
$\omega_j$ independent of $\mathcal R$. The intersection of the latter
sigma fields is $\sigma(\mathcal R)$. This follows from reverse martingale
convergence: first check conditional expectations of functions depending on
$\mathcal R$ and finitely many $\omega_j$, then approximate bounded
measurable functions in $L^1$. $\square$

## 6. Pile probability strictly detects ordered stationary laws

**Theorem 5.** Let $\mu\le_{\rm st}\nu$ be translation-invariant
stationary laws on $X$. If $q(\mu)=q(\nu)$, then $\mu=\nu$.
No first-moment assumption is required.

**Proof.** Start from an ordered coupling. Average its spatial shifts and
take a weak limit to obtain a translation-invariant ordered coupling: fixed
marginals ensure tightness, and order is closed. Evolve it by common clocks,
take time averages and a weak limit. As in Theorem 2, this gives a stationary,
translation-invariant ordered coupling.

Under this coupling $R_i=r(h_i)-r(g_i)\ge0$. Equality of $q$ implies
$R_i=0$ almost surely for every site. Stationarity gives this conclusion
at every fixed time.

Suppose a strict discrepancy occurs with positive probability. First
consider the event that the lower configuration contains some positive mass.
A finite interval contains both a strict discrepancy and a positive lower
mass with positive probability. The gathering word (9) produces the pair
$(n,n+D)$ at its left endpoint $a$, for some $n\ge1,D\ge1$, and empties
the rest of the interval. Choose fixed values of these integers on an event
of positive probability. If $n=1$, the residuals already differ. If $n>1$,
freeze the pile, clear sites $a-1,\ldots,a-(n-1)$ by descending double
firings, and move the pile left through this empty corridor using one firing
per site. Each move leaves one unit in both configurations. After $n-1$
moves the traveling pair is $(1,1+D)$, whose residuals differ.

The remaining event has $g\equiv0$ and $h\not\equiv0$. Conditional on
this translation-invariant event, the upper law is translation invariant.
A translation-invariant nonzero configuration cannot have positive finite
total mass with positive probability. To see this, condition further on
$1\le\sum_i h_i\le K$. The expected number of occupied sites in any
block of length $L$ is at most $K$, while translation invariance makes it
$L\Pr(h_0>0)$. Letting $L\to\infty$ forces every site to be empty,
a contradiction. Take the union over finite $K$. Thus the upper total mass
is infinite on the event in question. A finite interval containing at least
two upper units can be gathered, producing residuals 0 and 1.

All constructions use finitely many clocks. If the word or its length
depends on an initial integer value, choose one such value and word from the
countable collection on an event of positive probability. Prescribe its
events in disjoint subintervals of a fixed time interval, silence all other
clocks in the affected region and at its incoming boundary, and silence them
until the endpoint. This is a positive-probability clock event independent
of the initial pair. At that deterministic endpoint a specified residual
differs with positive probability, contradicting stationary equality of the
residuals. The coupling is diagonal. $\square$

**Corollary 5.1.** Existing deterministic finite-density phases are ordered
by density, and $q(\nu_\rho)$ is strictly increasing on their set of
densities.

**Proof.** A stationary common-clock coupling exists by time averaging.
Theorem 1 and the conditional-mean argument give the order according to
density. Distinct densities give distinct laws; Theorem 5 makes their $q$
values different. $\square$

For the mixture (15), write
$\overline r_L=L^{-1}\sum_{i=0}^{L-1}\mathbf1_{\{g_i\ge2\}}$.
The ergodic theorem within each phase and bounded convergence imply

$$
\lim_{L\to\infty}\operatorname{Var}_\mu(\overline r_L)
=\operatorname{Var}_\kappa(q(\nu_\rho)).                  \tag{18}
$$

By Corollary 5.1, this limit is zero exactly when $\kappa$ is a point mass.
The measurable map $\rho\mapsto q(\nu_\rho)$ here is supplied on the
support of $\kappa$ by the regular conditional laws in (15); no existence
of phases outside that set is being assumed.

## 7. What this proves, and does not prove, about finite rings

On a ring of $N\ge2$ sites with total mass $H$, the finite chain has a
unique stationary law $\pi_{N,H}$. Indeed, descending double firings at
$N-1,\ldots,1$ take every composition of $H$ to the state with all mass
at site 0. Every closed recurrent class must contain that state, so there
is exactly one such class. Uniqueness also implies cyclic translation
invariance. Put

$$
q_{N,H}=\pi_{N,H}(g_0\ge2).
$$

Suppose $H_N/N\to\eta<\infty$. The one-site means equal $H_N/N$.
Markov's inequality, translation invariance, and a countable-coordinate
tightness construction give subsequential local limits of the periodically
extended laws. Each local limit $\mu$ is translation invariant and has
$\mathbb E_\mu g_0\le\eta$ by truncation and Fatou's lemma.

Each limit is stationary for the infinite-line dynamics. To check this,
fix a bounded cylinder $f$ and a time $t$. Couple the ring and line clocks
in a large neighborhood of its support. They give the same local evolution
unless a backward dependency reaches the periodically identified boundary.
The factorial dependency bound in Section 1 makes this probability tend to
zero uniformly in masses as $N\to\infty$. Approximate $P_t f$ by the
resulting bounded finite-site function and pass finite-ring stationarity
to the local limit. Then $\mu P_t f=\mu f$; cylinder functions determine
the law.

Theorem 4 now gives

$$
\mu=\int\nu_\rho\,\kappa(d\rho),\qquad
\int\rho\,\kappa(d\rho)\le\eta,\qquad
\lim_j q_{N_j,H_{N_j}}=\int q(\nu_\rho)\,\kappa(d\rho).    \tag{19}
$$

The mean inequality concerns the average over phases; it does not bound
each component density by $\eta$. A local limit can lose mean through
increasingly rare large masses, and the current argument does not select
its mixing distribution $\kappa$.

**Conditional canonical convergence criterion.** Fix $\eta>0$ and
$H_N=\lfloor\eta N\rfloor$. If both

$$
\lim_{M\to\infty}\sup_{N\ge2}
\mathbb E_{\pi_{N,H_N}}[g_0\mathbf1_{\{g_0>M\}}]=0         \tag{20}
$$

and

$$
\lim_{L\to\infty}\limsup_{N\to\infty}
\operatorname{Var}_{\pi_{N,H_N}}
\left(\frac1L\sum_{i=0}^{L-1}\mathbf1_{\{g_i\ge2\}}\right)=0             \tag{21}
$$

hold, then the entire canonical sequence converges locally to the unique
phase $\nu_\eta$, and $q_{N,H_N}\to q(\nu_\eta)$.

**Proof.** Tightness gives a subsequential limit. Condition (20) preserves
its mean $\eta$. For each fixed $L$, the block variable and its square
are bounded cylinders, so their variances pass to the limit. Equations
(21) and (18) force its mixing law $\kappa$ to be a point mass. Its density
must then be $\eta$. Theorem 2 identifies all subsequential limits, proving
convergence and, under these hypotheses, existence of $\nu_\eta$.
$\square$

**Neither (20) nor (21) is proved here.** Mixing of each fixed phase gives no
uniform rate over road sizes. A function of all finite-system clocks can
develop additional global randomness in a local limit; endogeny alone does
not exclude that. Conditions (20)–(21) are sufficient for the stronger
conclusion of mean-preserving convergence to one phase, not claimed
necessary for convergence of the single bounded number $q_{N,H_N}$.

The unresolved task is to show that every subsequence in (19) gives the
same integral of $q$, or to construct stationary canonical subsequences
for which it does not. No such proof or counterexample is supplied here.
No general formula for the original NaSch stationary flow, first-passage
quantity $T_N$, or uniform rare-braking error follows from this note.

## Appendix A. Short individual residence does not erase mass memory

Label particles in order of arrival, with a fixed tie-breaking rule. At a
service retain the newest particle if at least two are present, and send
all others; send a singleton. This implements (1). Every particle leaves
by the second service after its arrival: if the first service retains it,
the second either sends it as a singleton or retains a newer arrival.
At an arrival stopping time, fresh rate-one service increments therefore
give

$$
\Pr(\tau>t\mid\text{history at arrival})\le(1+t)e^{-t},
\qquad \mathbb E[\tau\mid\text{history at arrival}]\le2.    \tag{22}
$$

This bounds neither batch sizes nor dependence on the initial residue.
If exactly one particle arrives before every service, post-service residues
started at 0 and 1 remain respectively 0 and 1, since
$r(0+1)=0$ and $r(1+1)=1$. The particle carrying the extra unit changes,
so (22) is not a contraction argument for a tandem of queues.

## Appendix B. Exact finite counterexample to uniform occupied subsets

For $N=4,H=3$, exact rational stationary linear algebra gives

$$
\Pr((\mathbf1_{g_i>0})_{i=0}^3=1100)=\frac7{76},\qquad
\Pr((\mathbf1_{g_i>0})_{i=0}^3=1010)=\frac3{38}.             \tag{23}
$$

The difference is $1/76$. The supplied solver enumerates every composition,
constructs the rate-one generator, solves the normalized stationary system
over the rationals, and checks every equation of $\pi Q=0$, normalization,
and nonnegativity. The finite-chain uniqueness proved in Section 7 identifies
that vector with $\pi_{4,3}$. Thus (23) is an exactly reproducible finite
counterexample to uniformity among occupied subsets of the same cardinality.
It says nothing by itself about asymptotic independence or the limit in (19).

## Literature context

For the backchip model family, see Justin Whitehouse, André Costa,
Richard A. Blythe, and Martin R. Evans, *Maintenance of order in a moving
strong condensate* (2014), [arXiv:1407.1668](https://arxiv.org/abs/1407.1668).
That paper studies mass transport sending all but one particle from a
multiply occupied site, with an occupation-dependent rate. The present note
specifies its own unit-rate rule, including singleton behavior, in (1).
Its proofs do not import a mean-field factorization or numerical phase
diagram from that work. This reference is context, not an exhaustive
literature or originality review.
