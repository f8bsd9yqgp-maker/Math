# Synchronized covers, a buffer comparison, and a clock-correlation counterexample

23 October 2026. AI-assisted working mathematics, internally checked and not
independently peer-reviewed. No claim of publication priority is made.

**The fixed-density canonical limit remains open.** This continuation proves
two finite-network constructions and a quantitative two-block loss bound,
gives an exact counterexample to a proposed monotonicity mechanism, and reduces
one possible proof of convergence to a stronger stationary loss estimate.
That stronger estimate is a conjectural input, not a conclusion. Neither this
note nor its computations exclude condensates.

## 1. Definitions and inherited results

On a ring of $N\ge2$ sites with total mass $H$, clock $i$ sends
$d(g_i)=g_i-\mathbf1_{\{g_i\ge2\}}$ units to $i-1$. Write $T_i$ for this
map, $\pi_{N,H}$ for its unique invariant law, and

$$q_{N,H}=\pi_{N,H}(g_0\ge2),\qquad F_{N,H}=H/N-q_{N,H}.$$

The zero-mass law is the point mass at zero. The full state space includes
transient configurations. Uniqueness follows from the double-firing gathering
word; full irreducibility is not needed.

We use two already-proved results, with proofs in the linked notes:

* [The previous finite comparison note](../2026-10-22/README.md) proves
  mass monotonicity, the bound
  $0\le q_{N,H+a}-q_{N,H}\le2a/(3N)$, and
  $q_{M,H}\le q_{K,H}+H(1/M-1/K)$ for $2\le M\le K$.
* [The corrector note](../2026-10-22-corrector-audit/README.md) constructs
  a monotone, translation-homogeneous height function
  $\Phi_{N,H}(h)=\bar h+\psi_{N,H}(g)$ with
  $L\Phi_{N,H}=F_{N,H}$. Here $h_{i+1}-h_i=g_i$ and
  $h_{i+N}=h_i+H$. Its individual clock increments $a_i(h)$ satisfy
  $a_i\ge0$ and $\sum_i a_i=F_{N,H}$ pointwise.

These are statements about the reduced continuous-time backchip process.
The unrestricted discrete-time NaSch model and the interchange of rare-braking
and thermodynamic limits are outside the conclusions.

## 2. An exact synchronized cover at the corrected mass

**Theorem 1.** Fix $N\ge2$, $H\ge1$, and $k\ge2$. On the $kN$-site ring,
give each residue class $i\bmod N$ one rate-one clock. Its event applies all
$k$ maps $T_{i+rN}$ simultaneously. These maps commute, since their donors
and destinations are disjoint. There is a rotation-invariant stationary law
of mass $k(H-1)+1$ for this process whose pile probability is exactly

$$q^{\rm sync}_{kN,k(H-1)+1}
 =\frac{k-1}{k}q_{N,H-1}+\frac1k q_{N,H}.                 \tag{2.1}$$

Each physical site's clock has marginal rate one. The clocks at different
sheets of a residue class are perfectly correlated. Equation (2.1) does
not assert uniqueness of every synchronized invariant law.

**Proof.** Take a stationary ordered common-clock coupling $(G,U)$ of the
$N$-site mass-$H-1$ and mass-$H$ chains. It exists by time averaging a finite
ordered coupling. Since its total discrepancy is one, write
$U=G+e_X$. The lower and upper marginals are respectively $\pi_{N,H-1}$
and $\pi_{N,H}$. When clock $i$ rings, the extra unit moves from $i$ to $i-1$
exactly when $X=i$ and $G_i\ne1$. Indeed,

$$d(m+1)-d(m)=\mathbf1_{\{m\ne1\}}.$$

Introduce a sheet $S\in\mathbb Z/k\mathbb Z$, independent and uniform.
If the extra unit crosses the bond $0\to N-1$, replace $S$ by $S-1$;
otherwise leave $S$ fixed. Uniformity of $S$, independent of $(G,X)$,
is preserved: conditional on each transition of the base pair, its update
is a bijective translation of the sheet. Thus the enlarged law is stationary.

Put a copy of $G$ on each of the $k$ consecutive blocks and add one unit
at physical site $SN+X$. At a synchronized event, all ordinary copies
undergo $T_i$. If the extra unit moves, it goes to the preceding site, with
exactly the sheet change just specified at a block boundary. Hence this
embedding intertwines the two generators.

In every embedded configuration, the total number of piles is
$(k-1)\sum_i r(G_i)+\sum_i r(U_i)$, where $r(m)=\mathbf1_{\{m\ge2\}}$.
Taking stationary expectations and dividing by $kN$ proves (2.1).
If necessary average the embedded law over all $kN$ spatial rotations.
The generator is rotation invariant, and the pile average is unchanged.
$\square$

This explains the corrected mass $k(H-1)+1$ by an exact construction. It
also identifies a stationary endpoint for a possible noise-correlation
comparison. A comparison with independent clocks still requires a proof.

## 3. Clock decorrelation is not monotone

For $k=2$ interpolate between independent and paired clocks by

$$L_c=(1-c)\sum_{j=0}^{2N-1}(T_j-I)
       +c\sum_{i=0}^{N-1}(T_iT_{i+N}-I),\qquad 0\le c\le1. \tag{3.1}$$

Operators act on observables by composition with the indicated state maps.
Every site still has marginal clock rate one. For $c<1$, the independent
single-clock events supply a gathering word, so there is a unique invariant
law. Let $q(c)$ be its site-averaged pile probability. At $c=0$ it is the
ordinary canonical value on $2N$ sites.

**Theorem 2.** There is no general monotonicity of $q(c)$ in either direction.
There is even a fixed system for which $q(c)$ is nonmonotone on $[0,1)$.

**An analytic four-site example.** For $N=2,H=2$, so total mass is three,

$$q(c)=\frac{c^2-12c+15}{4(c^2-14c+19)},\qquad
q'(c)=-\frac{(c-2)^2+5}{2(c^2-14c+19)^2}<0.               \tag{3.2}$$

Here is a full calculation. The five rotation classes, in order, are

$$0003,\quad0012,\quad0021,\quad0102,\quad0111.$$

With rows indexed by starting state, their generator is

$$\begin{pmatrix}
-1&0&1&0&0\\
0&-2&1&1&0\\
1&0&-2&0&1\\
0&0&1-c&c-2&1\\
0&1-c&0&1+c&-2
\end{pmatrix}.$$

Writing $D=c^2-14c+19$, its stationary row vector is

$$D^{-1}\big(5(1-c),(1-c)(2-c),5(1-c),3+c,4-2c\big).$$

All entries are nonnegative on $[0,1]$, sum to one, and direct multiplication
by the displayed generator gives zero. Every class except $0111$ has one
pile, giving (3.2). In particular, $q(0)=15/76$ and $q(1)=1/6$.

**The opposite direction.** For $N=2,H=3$ (four sites, five particles),
exact stationary balance gives

$$q(0)=148061/476832
 <q(1/2)=841177/2551180.$$

**A nonmonotone fixed system.** For $N=4,H=3$ (eight sites, five particles),
the exact answers satisfy

$$q(1/2)<q(0)<q(9/10).                                    \tag{3.3}$$

For readability their decimal values are

| $c$ | $q(c)$, decimal display only |
|---|---:|
| $0$ | $0.1449920850416556$ |
| $1/2$ | $0.1446324764398561$ |
| $9/10$ | $0.1455144829339839$ |

The proof of these last finite claims is an exhaustive rational certificate,
not an inference from these decimals. The [certificate](results/certificates.json)
lists all rotation classes and their rational stationary weights. The
[verifier](verify.py) independently expands those weights to the full
composition space, checks positivity and normalization, and verifies every
full-state balance equation. It then compares the rational numbers by exact
arithmetic. There are 99 rotation classes and 792 labelled configurations in
the eight-site example. Unique stationarity for these three values of $c$
was proved above using the single-clock gathering word. This completes the
finite computer-assisted proof of (3.3). $\square$

This counterexample concerns **changing correlations**, while preserving
individual rates. It does not contradict the earlier theorem about increasing
individual clock rates. It does not disprove the proposed dilation inequality:
the synchronized value in (2.1) is below $q_{N,H}$, and the target comparison
allows that difference. Nor does (3.3) exhibit nonconvergence with road size.

### An exact derivative identifying the missing sign

Let $f(g)=(2N)^{-1}\sum_jd(g_j)$, and let $\psi_c$ solve
$L_c\psi_c=F(c)-f$, where $F(c)=(2H-1)/(2N)-q(c)$.
For every $0<c<1$,

$$q'(c)=-\mathbb E_{\pi_c}\sum_{i=0}^{N-1}
 (T_i-I)(T_{i+N}-I)\psi_c.                               \tag{3.4}$$

The same formula gives the right derivative at zero. To prove it, differentiate
$\pi_cL_c=0$ and $\pi_c1=1$. Finite-state uniqueness on $c<1$ implies analytic
dependence by the nonsingular normalized stationary linear system. Then

$$-F'(c)=\pi_c'(L_c\psi_c)=-\pi_c(L_c'\psi_c).$$

For nonadjacent paired maps,
$L_c'=\sum_i(T_i-I)(T_{i+N}-I)$, which gives (3.4).
The examples prove that the averaged mixed difference in this identity
does not have a universal sign.

## 4. A rigorous comparison using core rings and buffers

The following construction uses **independent physical clocks** and does not
require monotonicity in the parameter $c$.

Fix $N\ge2,H\ge1,k\ge2,B\ge0$. There are $k$ blocks. Block $r$ has a core
configuration $G^r$ of mass exactly $H$ on $N$ sites. It also has a buffer
$b_r\ge0$, with $\sum_rb_r=B$. Store this buffer physically at site $N-1$
of block $r$, in addition to the core mass there. Give every physical site
an independent rate-one clock.

* At internal site $j\in\{1,\ldots,N-1\}$, move $d(G^r_j)$ core units to
  core site $j-1$. Do not move buffer units.
* At site zero of block $r$, put $v_r=\min\{d(G^r_0),b_r\}$. Move $v_r$
  physical units from that site to the last site of block $r-1$, labelling
  them buffer there. At the same time relabel $v_r$ of the buffer units at
  the last site of block $r$ as core units.

Thus the core undergoes the partial cyclic move $0\to N-1$ by $v_r$, and
the buffers undergo $b_r\mapsto b_r-v_r$, $b_{r-1}\mapsto b_{r-1}+v_r$.
Every core keeps mass $H$ and total buffer mass stays $B$. Relabelling does
not move physical mass. This is a finite-state continuous-time chain and
therefore has at least one invariant law. No uniqueness is assumed.

Let $a_0(G^r)$ be the full boundary-clock increment of the inherited
corrector $\Phi_{N,H}$. Let $a_0^{(v_r)}(G^r)$ be its increment when that
height coordinate is raised by only $v_r$. Define the nonnegative loss

$$\ell_r=a_0(G^r)-a_0^{(v_r)}(G^r).                       \tag{4.1}$$

Both increments are independent of the additive choice of height lift.
Monotonicity of $\Phi$ and $0\le v_r\le d(G^r_0)$ imply

$$0\le a_0^{(v_r)}\le a_0\le F_{N,H},\qquad
0\le\ell_r\le F_{N,H}.                                  \tag{4.2}$$

**Theorem 3 (buffer comparison).** For any invariant law $\lambda$ of this
finite protocol, every physical bond has the same mean current $J$, and
for every block $r$,

$$J=F_{N,H}-\mathbb E_\lambda\ell_r.                      \tag{4.3}$$

The ordinary independent-clock backchip ring satisfies

$$\boxed{\quad
q_{kN,kH}\le q_{kN,kH+B}
 \le q_{N,H}+\frac{B}{kN}+\mathbb E_\lambda\ell_r.
\quad}                                                  \tag{4.4}$$

**Proof.** Stationary physical mass balance makes the currents of all
neighboring bonds equal. Alternatively, stationary core balance equates
the $N$ currents within each block, and stationary buffer balance equates
the boundary currents between blocks.

On one lifted core, replacing the full boundary move by the partial move
changes its corrector drift from $F_{N,H}$ to $F_{N,H}-\ell_r$. The
corrector is $\bar h+\psi(G^r)$. Since $\psi$ is a bounded function on the
finite core state space, its mean drift is zero under $\lambda$. The mean
drift of $\bar h$ is the average of the $N$ core bond currents, namely $J$.
This proves (4.3), without treating an unbounded height as a stationary
observable.

At every event the protocol's actual transfer is at most $d$ of the physical
donor mass. At internal sites this follows from monotonicity of $d$; at a
boundary it follows from the definition of $v_r$. Consequently the ordinary
ring can be coupled above the protocol in height order, using the same clocks
and initially identical physical masses. In detail, its height update is

$$B(a,b)=\min\{b,\max(a+1,b-1)\},$$

which is nondecreasing in both inputs. The protocol raises that coordinate
by an amount no larger than $B(a,b)-a$. Induction over events therefore
preserves height order. The two systems have the same total physical mass
$kH+B$. Their long-time expected one-bond growth rates give
$F_{kN,kH+B}\ge J$; the initial finite lift contributes no asymptotic error.
Insert (4.3), subtract current from density, and use mass monotonicity for
the first inequality of (4.4). $\square$

### A proved quantitative loss bound for two blocks

The corrector note also proves the exact oscillation
$\operatorname{osc}(\Phi_{N,H}(h)-h_0)=H(N-1)/N$. Normalize its additive
constant so that the gap function

$$\chi(g)=\Phi_{N,H}(h)-h_0\quad\hbox{satisfies}\quad
0\le\chi(g)\le A:=H(N-1)/N.$$

Write $F=F_{N,H}$, $q=q_{N,H}$, and $K=H-1-q=A+F-1$.
Here $K\ge0$: it is zero for $H=1$, while for $H\ge2$ this follows
from $q\le1$.

**Theorem 4.** For $k=2$, every invariant law of the buffer protocol obeys

$$\boxed{\quad
\mathbb E_\lambda\ell_r\le
\frac{F^2}{B-2(H-1-q)}\qquad\text{if }B>2(H-1-q).
\quad}                                                   \tag{4.5}$$

This statement requires no irreducibility or symmetry of the invariant law.

**Proof.** Define signed corrected buffers

$$w_r=b_r+\chi(G^{r+1})-\chi(G^r),\qquad w_0+w_1=B.$$

Consider a protocol event in block $r$, and let $a$ be its actual core
corrector increment. It transfers exactly $a$ from $w_r$ to $w_{r-1}$.
For an internal event the anchor height $h_0$ does not change, so
$\Delta\chi(G^r)=a$. For a boundary event with physical transfer $v$,
the anchor increases by $v$, so $\Delta\chi(G^r)=a-v$; together with the
buffer transfer $v$ this gives the same corrected transfer $a$.
Thus in both cases the asserted update follows by direct substitution.
For each block, summing over its rate-one event types gives

$$\sum_j a_{r,j}=F-\ell_r,\qquad
0\le a_{r,j}\le F,\qquad\sum_j a_{r,j}^2\le F^2.          \tag{4.6}$$

On the support of $\ell_r>0$, the boundary transfer is truncated, so
$b_r<d(G^r_0)$ and, since these are integers, $b_r\le d(G^r_0)-1$.
The full boundary increment satisfies

$$a_0=d(G^r_0)+\chi(T_0G^r)-\chi(G^r)\le F.$$

As $\chi(T_0G^r)\ge0$, this implies
$\chi(G^r)\ge d(G^r_0)-F$. Consequently

$$\ell_r>0\quad\Longrightarrow\quad
w_r\le d(G^r_0)-1+A-d(G^r_0)+F=K.                      \tag{4.7}$$

Apply stationarity to the bounded finite-state observable
$S=w_0^2+w_1^2$. A transfer $a$ from $w_r$ to $w_{r-1}$ changes it by
$2a(w_{r-1}-w_r)+2a^2$. The terms with the common drift $F$ cancel
between blocks. Hence, writing $V=\sum_{r,j}a_{r,j}^2$,

$$\sum_{r=0}^1\mathbb E_\lambda
 [(w_{r-1}-w_r)\ell_r]=\mathbb E_\lambda V\le2F^2.       \tag{4.8}$$

On the support of each loss, $w_{r-1}-w_r=B-2w_r\ge B-2K$.
Theorem 3 gives the same mean loss $\bar\ell=F-J$ for both blocks.
Thus $2(B-2K)\bar\ell\le2F^2$, proving (4.5). $\square$

For fixed $N,H$, this proves $J\to F$ as $B\to\infty$, uniformly over
all invariant protocol laws. At fixed positive $H/N$, however, its threshold
is of order $N$. The reserve term $B/(2N)$ in (4.4) then remains of order
one. Therefore (4.5) does **not** prove thermodynamic convergence.

The same energy calculation gives the exact identity

$$B\bar\ell=\tfrac12\mathbb E_\lambda V+
 \sum_{r=0}^1\mathbb E_\lambda[w_r\ell_r].                \tag{4.9}$$

A uniform upper bound on the last, loss-weighted term would remove the
order-$N$ threshold for two blocks. Such a bound has not been proved.
Nonpositivity is false: at $N=2,H=3,B=1$, an exact stationary certificate gives

$$F=1,\qquad \bar\ell=\frac{108599}{211093},\qquad
\mathbb E V=\frac{108872}{211093},\qquad
\sum_r\mathbb E[w_r\ell_r]=\frac{54163}{211093}>0.$$

All 32 labelled balance equations, positivity, normalization, and (4.9)
are checked by the verifier. The full rational stationary weights are in
[buffer_certificate.json](results/buffer_certificate.json). This counterexample
refutes the nonpositivity shortcut, not a uniform upper bound or convergence.

There is also a necessary capacity restriction for every $k$: the boundary
transfer satisfies $v_r\le b_r$, so stationarity and $\sum_rb_r=B$ give
$kJ=\sum_r\mathbb E v_r\le B$. In particular,
$\bar\ell\ge\max\{0,F-B/k\}$. A reserve of one unit can cause a fixed
positive loss; positive reserve alone is not a closure argument.

## 5. A weaker sufficient estimate than the earlier order-$1/N$ comparison

Here is the precise missing bound for the new construction. It is **not
proved**:

> For $k=2,3$, $H/N\le R$, and $B=\lceil\sqrt N\rceil$, there is an invariant
> protocol law $\lambda$ such that
> $\mathbb E_\lambda\ell_r\le C_R/B$, with $C_R$ independent of $N,H$.

A bound for all $B$ would be stronger than necessary. The assertion only
needs some invariant law for each parameter set; (4.3) makes its loss the
same in expectation for every block.

**Conditional corollary.** If that estimate holds, the requested canonical
limit exists for every fixed positive density in its stated range.

**Proof of the implication.** Equation (4.4), mass monotonicity, and
$B=\lceil\sqrt N\rceil$ give

$$q_{kN,k(H-1)+1}\le q_{N,H}+D_RN^{-1/2},\qquad k=2,3,   \tag{5.1}$$

for a constant $D_R$. The earlier proof with an order-$1/N$ error works
with any error $D_RN^{-\alpha}$, $\alpha>0$: along successive doublings
and triplings its accumulated error is at most
$D_R n^{-\alpha}/(1-2^{-\alpha})$.

For completeness, fix $\eta>0$ and start at
$h=\lfloor\eta n\rfloor+2$. The iterated sizes and masses are
$K=sn,L=s(h-1)+1$ for $s=2^a3^b$. Their densities stay bounded, and their
pile probabilities are at most $q_{n,h}+O(n^{-1/2})$, uniformly in $a,b$.
For every sufficiently large target size $M$, one can choose such an $s$
with $K\ge M$ and $K/M\to1$. To see this, the nonnegative multiples of
$\log3$ are dense modulo $\log2$; a finite set of them approximates every
residue to any specified accuracy. For large $\log(M/n)$ the required
remaining multiple of $\log2$ is nonnegative. Letting that accuracy tend
to zero gives the stated choice of $K$.

Since $(h-1)/n>\eta$, the target mass $\lfloor\eta M\rfloor$ is at most $L$.
Mass monotonicity followed by the inherited site-removal inequality gives

$$q_{M,\lfloor\eta M\rfloor}
 \le q_{K,L}+L(1/M-1/K).
$$

For fixed $n$, the last term tends to zero. Also
$q_{n,h}\le q_{n,\lfloor\eta n\rfloor}+4/(3n)$. Thus the limsup over $M$
is at most $q_{n,\lfloor\eta n\rfloor}+O(n^{-1/2})+4/(3n)$.
Let $n$ follow a subsequence attaining the liminf. Limsup and liminf agree.
$\square$

### Why the missing estimate cannot be inferred from the construction

If $B=0$, the state with every core's entire mass at its first site is
absorbing. It has $J=0$ and $\ell_r=F_{N,H}$. Positive reserve mass matters.
For positive $B$, a requested boundary transfer can still be of order $H$.
The stationary core marginal need not be $\pi_{N,H}$, since its boundary
service is restricted. A canonical tail estimate therefore cannot simply
be applied to that marginal.

The inherited corrected-current martingale has bounded jumps, but the
correction between it and actual boundary current has oscillation
$H(N-1)/N$. That is of order $N$ at fixed density. Using that worst-case
correction alone does not justify an order-$1/B$ loss bound for
$B=\lceil\sqrt N\rceil$. An additional argument is required.

## 6. Audit and unresolved claims

Run `python3 nasch/continuations/2026-10-23-buffer-coupling/verify.py` from
the repository root. The program uses only the Python standard library and
the already-published exact solver and corrector. Its checks include:

* every full-state balance equation behind the correlation counterexamples;
* the symbolic five-class stationary vector at exact rational parameters;
* the synchronized embedding and its sheet changes, on enumerated states;
* physical embedding, conservation, transfer domination, and the exact
  corrector-loss identity for the buffer protocol, on enumerated states;
* corrected-buffer transfers, the support bound (4.7), and the pointwise
  quadratic-generator calculation underlying (4.8).

The finite checks support the algebra and the explicitly finite
counterexamples. They do not establish the uniform stationary loss estimate.

The [exploratory calculations](exploratory/README.md) retain the buffer
simulator, floating-point stationary covariance probes, their outputs, and
reproduction instructions. They are separate from the exact proof audit.

The principal target, phase selection in canonical local limits, control of
escaped mean mass, exclusion of moving condensates, the original first-passage
formula $T_N$, and a general stationary NaSch flow formula remain unresolved.
The synchronized cover and the buffer comparison are proved constructions;
clock-correlation monotonicity is refuted; the loss estimate in Section 5 is
an unproved sufficient condition.
