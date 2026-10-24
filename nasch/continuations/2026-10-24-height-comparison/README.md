# A finite-time comparison for the canonical currents

24 October 2026. Continuation of the already published sharp-drift and support
results. **The fixed-density thermodynamic limit is still not proved.**

The main unconditional result here bounds the difference between stationary
currents on different rings by height oscillations at a finite time, starting
from balanced deterministic configurations. A quantitative sublinear bound on
these oscillations would settle convergence along arbitrary road sizes. That
bound remains unproved. It does not assume absence of stationary condensates.

We also give an exact conjugacy to a Horton–Strahler rank update and a family
of counterexamples to a bounded-error maximum-envelope formula. All proofs
below are internally audited working mathematics, not independently peer
reviewed. No literature-priority claim is made. The numerical experiment at
the end is explicitly exploratory.

## 1. Model and finite-time observable

At independent rate-one clocks, a site of mass $m$ retains
$r(m)=\mathbf1_{\{m\ge2\}}$ and sends $d(m)=m-r(m)$ to its left neighbor.
For an $N$-site ring of total mass $H$, write

$$\theta=H/N,\qquad q_{N,H}=\pi_{N,H}(g_0\ge2),\qquad
F_{N,H}=\theta-q_{N,H}.$$

These are quantities for the reduced continuous-time process. Nothing here
interchanges the rare-braking and thermodynamic limits of the original
parallel-update NaSch model.

Lift gaps to integer heights:

$$g_i=h_{i+1}-h_i,\qquad h_{i+N}=h_i+H.$$

The clock at $i$ updates all corresponding lifts by

$$h_i\longleftarrow B(h_i,h_{i+1}),\qquad
B(a,b)=\min\{b,\max\{a+1,b-1\}\}
       =b-\mathbf1_{\{b-a\ge2\}},\quad a\le b. \tag{1}$$

This height map, its monotonicity, and vertical translation homogeneity were
proved in the [corrector continuation](../2026-10-22-corrector-audit/README.md).
They are not new claims here. They also follow immediately from (1).

Start this process at the balanced profile

$$\ell_i=\lfloor \theta i\rfloor,\qquad i\in\mathbb Z.$$

It satisfies the helical boundary condition because $\theta N=H$. Put

$$U_i(t)=h_i(t)-\ell_i,\qquad
f_{N,H}(t)=\mathbb E U_0(t),$$
$$\mathcal R_{N,H}(t)=
\mathbb E\left[\max_{0\le i<N} U_i(t)-\min_{0\le i<N} U_i(t)\right]. \tag{2}$$

The expectation in (2) concerns a deterministic initial condition and a
specified finite time. It is not a stationary roughness or mixing-time
assumption. Each $U_i(t)$ is nonnegative.

## 2. A Poisson backward path and an exact identity

**Lemma 1 (backward path).** Starting at space-time point $(0,t)$, find the
last clock at the current site before the current time, move one site to the
right at that clock, and repeat backward until reaching time zero. Let
$Z(t)$ be the number of these steps, with the spatial index lifted to
$0,1,\ldots,Z(t)$. Then

$$Z(t)\sim\operatorname{Poisson}(t), \tag{3}$$

also on a finite ring, regardless of its size. If the selected events have
pre-event donor masses $m_1,\ldots,m_{Z(t)}$, then

$$h_0(t)=\lfloor\theta Z(t)\rfloor
          -\sum_{j=1}^{Z(t)}r(m_j),\qquad
0\le h_0(t)\le\theta Z(t). \tag{4}$$

Moreover, the whole dependency diagram for $h_0(t)$ is contained in the
lifted sites $0,\ldots,Z(t)$.

**Proof.** At a selected clock, (1) expresses the post-event height as the
right neighbor's pre-event height minus $r(m)$. Iteration gives (4), ending
at the initial height at site $Z(t)$. Monotonicity in time supplies the lower
bound zero.

For a direct proof of (3), condition on the total number $M$ of ring clocks
in $(0,t]$. The clock identities in chronological order, and hence in reverse
order, are iid uniform on the $N$ sites. Scan them backward with a counter
$z$, initially zero. An event is selected exactly when its identity is
$z\bmod N$; a selection increments $z$. Conditional on every previously
scanned identity, its probability of being selected is $1/N$. Thus the
selection indicators are independent Bernoulli variables and
$Z\mid M\sim\operatorname{Binomial}(M,1/N)$. Since
$M\sim\operatorname{Poisson}(Nt)$, thinning proves (3). This argument permits
arbitrarily many windings around the ring.

To check the dependency assertion, a dependency edge either goes backward
at the same site or goes to the right at an earlier clock. The displayed
path takes the latest possible clock for each right step. Induction on the
number of right steps shows that any other dependency path reaches a given
lifted site no later than this path. Taking an extra same-site backward edge
cannot expose a further site. Consequently no dependency reaches beyond
$Z(t)$. This also constructs the infinite-line evolution from any increasing
initial height profile, since the relevant diagram is almost surely finite.
$\square$

The retention indicators on the path are generally dependent. Equation (4)
does **not** turn them into independent Bernoulli variables and is not a
closed formula for the current.

## 3. Stationary speed from finite-time extrema

**Lemma 2 (current bracket).** For every $N\ge2,H\ge0,t>0$,

$$\frac{\mathbb E\min_i U_i(t)}t\le F_{N,H}
\le\frac{\mathbb E\max_i U_i(t)}t,$$
$$\left|F_{N,H}-\frac{f_{N,H}(t)}t\right|
\le\frac{\mathcal R_{N,H}(t)}t. \tag{5}$$

**Proof.** Let $m=\min_i U_i(t)$ and $M=\max_i U_i(t)$. Pathwise,
$\ell+m\le h(t)\le\ell+M$. Apply the future update maps, using monotonicity
and commutation with integer vertical translations. With an independent
future clock block of length $t$, the minimum increment after two blocks is
at least the sum of the two balanced-start minimum increments. The maximum
increment is at most the analogous sum of maxima. Iterating gives

$$k\,\mathbb E\min_i U_i(t)\le\mathbb E U_0(kt)
\le k\,\mathbb E\max_i U_i(t).$$

The finite gap chain has a unique stationary law. Its bounded mean
instantaneous increment at coordinate zero tends, in time average, to
$\mathbb E_\pi d(g_0)=F_{N,H}$. Divide the last display by $kt$ and let
$k\to\infty$. Finally $\min_i U_i\le U_0\le\max_i U_i$, so the interval in
the first display has width $\mathcal R(t)/t$, proving (5). $\square$

The uniqueness used here is an earlier finite-system result; its full
recurrent support is given in the
[support theorem](../2026-10-24-sharp-drift/SUPPORT_AND_MATRIX_OBSTRUCTION.md).
There is no claim that the balanced process is near stationarity at time $t$.

## 4. An explicit comparison across ring sizes

**Theorem 3 (finite-time ring comparison).** Let $N,M\ge2$,
$\theta=H/N$, $\varphi=K/M$, $L=\min(N,M)$, and
$Z_t\sim\operatorname{Poisson}(t)$. For any $t>0$,

$$\begin{split}
|q_{N,H}-q_{M,K}|\ \le\;&2|\theta-\varphi|
+\frac{\mathcal R_{N,H}(t)+\mathcal R_{M,K}(t)+1}{t}\\
&+(\theta+\varphi)\Pr(Z_t\ge L-1).
\end{split} \tag{6}$$

If the two densities are exactly equal, the $1/t$ term can be omitted,
as can the density-difference term. The same bound for $|F_{N,H}-F_{M,K}|$
has coefficient one, rather than two, on $|\theta-\varphi|$.

**Proof.** Give the rings the same Poisson clocks at sites
$0,\ldots,L-1$; all other clocks are independent, with each ring's helical
extension. Their backward paths agree until they reach lifted site $L$.
Call this event $D$. The first $L$ right steps use the common clocks, hence

$$D=\{Z_N(t)\ge L\}=\{Z_M(t)\ge L\}$$

in this coupling. Each count separately has law (3).

On $D^c$ the entire dependency diagram is shared. Its initial leaves have
indices $j\in[0,Z_N(t)]$. Their height differences satisfy

$$|\lfloor\theta j\rfloor-\lfloor\varphi j\rfloor|
\le |\theta-\varphi|Z_N(t)+1.$$

Monotonicity and vertical homogeneity of the finite compositions of $B$
transfer this bound to the two output heights. One can use the integer
maximum of the leaf differences, so no extension to noninteger heights is
needed. If $\theta=\varphi$, the shared initial data and the output heights
are identical on $D^c$.

On $D$, (4) bounds the absolute output difference by
$\theta Z_N(t)+\varphi Z_M(t)$. The Poisson identity

$$\mathbb E[Z_t\mathbf1_{\{Z_t\ge L\}}]
=t\Pr(Z_t\ge L-1)$$

therefore gives

$$|f_{N,H}(t)-f_{M,K}(t)|
\le |\theta-\varphi|t+1
 +(\theta+\varphi)t\Pr(Z_t\ge L-1). \tag{7}$$

For equal densities the first two terms vanish. Combine (7) with (5).
Finally use $q=\theta-F$, which adds another $|\theta-\varphi|$ for (6).
$\square$

For $t\ll L$, the Poisson error is extremely small. The obstruction has been
isolated in the two expected height ranges. The deterministic estimate
$\mathcal R\le H$ is too large when $t\ll N$; choosing $t\gg N$ instead
makes the Poisson term large. Thus (6) is a comparison theorem, **not by
itself a convergence theorem**.

## 5. A concrete sufficient estimate for the full thermodynamic limit

**Theorem 4 (conditional flat-start criterion).** Fix $\eta>0$ and put
$H_n=\lfloor\eta n\rfloor$. Suppose there exist $C<\infty$ and
$0<\delta\le1$ such that, for every sufficiently large $n$,

$$\boxed{\quad
\mathcal R_{n,H_n}(t)\le C t^{1-\delta}
\quad\hbox{for all }\sqrt{n/2}\le t\le\sqrt n.
\quad} \tag{8}$$

Then $q_{n,H_n}$ converges along all increasing road sizes. In fact, for a
constant $C'$ depending on $C,\delta,\eta$ and the starting threshold,

$$|q_{n,H_n}-q(\eta)|\le C'n^{-\delta/2}$$

for every sufficiently large $n$.

**Proof.** First let $n\le m\le2n$ and use $t=\sqrt n$ in (6).
This time belongs to the interval in (8) for both rings. Moreover

$$|H_n/n-H_m/m|\le1/n+1/m\le2/n.$$

Both densities are at most $\eta$. Therefore (6) gives

$$|q_{n,H_n}-q_{m,H_m}|
\le\frac4n+2C n^{-\delta/2}+n^{-1/2}
     +2\eta\Pr(\operatorname{Poisson}(\sqrt n)\ge n-1). \tag{9}$$

The last probability is smaller than every inverse power of $n$. For
example, for large $n$ the elementary Poisson Chernoff estimate bounds it by
$[e\sqrt n/(n-1)]^{n-1}$. Since $\delta\le1$, the right side of (9) is at
most $A n^{-\delta/2}$ for all sufficiently large $n$.

For arbitrary $m\ge n$, compare consecutive sizes
$n,2n,4n,\ldots,2^j n$ until $2^j n\le m<2^{j+1}n$, and then compare
$2^j n$ with $m$. Summing (9) gives

$$|q_{n,H_n}-q_{m,H_m}|
\le\frac{A}{1-2^{-\delta/2}}n^{-\delta/2}.$$

This proves the Cauchy property for the entire integer sequence and the
claimed convergence rate. $\square$

**Exact remaining gap in this route:** estimate (8) has not been proved,
for any interval of positive densities. The theorem assumes a uniform power
saving, not just a decreasing ratio in several simulations. It requires
only finite-time data from balanced initial mass, and does not assume
stationary mass uniform integrability, canonical phase purity, a stationary
condensate bound, or a separate infinite-line shape theorem.

## 6. Exact Strahler-rank form of the height dynamics

**Proposition 5.** With $x_i=h_i-i$, an update becomes

$$x_i\longleftarrow S(x_i,x_{i+1}),\qquad
S(a,b)=\max(a,b)+\mathbf1_{\{a=b\}}. \tag{10}$$

The admissibility and boundary conditions are
$x_i\le x_{i+1}+1$ and $x_{i+N}=x_i+H-N$. For arbitrary integers $a,b$,

$$S(a,b)=\max\{a,b,1+\min(a,b)\}
=\left\lfloor\log_2(2^a+2^b)\right\rfloor. \tag{11}$$

**Proof.** Write $a=x_i,b=x_{i+1}$, so the gap is $b-a+1$.
If $a=b+1$, the gap is zero and the site does not move. If $a=b$, the gap
is one and $a$ increases by one. If $a<b$, the gap is at least two and
the updated value is $b$. These are (10). For (11), equality of $a,b$
doubles a power of two. If they are unequal, their sum lies between the
larger power and the next power of two. The max-min expression follows from
the same two cases. $\square$

For any finite clock word, introduce a binary node each time a coordinate
is updated, with its previous value and its right neighbor's previous value
as children. Reusing an existing child gives a directed acyclic dependency
diagram; unfolding it gives a finite binary tree. Evaluating (10) from the
initial leaf values gives the exact final height. At $H=N$ with balanced
initial data, all $x_i(0)=0$, and this is precisely the binary
Horton–Strahler rank, with leaf rank zero. The tree can have repeated leaves
and strongly dependent subtrees. It is **not** a Galton–Watson tree.

The Horton–Strahler/register function itself is established mathematics;
see, for example, Robin Khanfir,
[arXiv:2401.13771](https://arxiv.org/abs/2401.13771).
That paper does not prove a traffic or random-clock circuit limit applicable
here. The present algebraic identification does not license importing its
random-tree distributional results.

## 7. A linear-size obstruction to maximum envelopes

Let $\mathcal T_w$ denote the height evolution for a finite legal clock word
$w$. Monotonicity always gives

$$\mathcal T_w(h\vee z)\ge\mathcal T_w(h)\vee\mathcal T_w(z).$$

The reverse inequality cannot be repaired by a universal additive constant,
or even an error $o(N)$ uniformly over clock words, including at $H=N$ with
initial gaps bounded by two.

**Theorem 6 (explicit maximum-envelope counterexample).** For each $r\ge1$
there is an $N=4r$ site ring with $H=N$, two admissible initial profiles
$h^A,h^B$ whose gaps all belong to $\{0,1,2\}$, and a finite clock word $w$
such that

$$\left[\mathcal T_w(h^A\vee h^B)
 -(\mathcal T_w(h^A)\vee\mathcal T_w(h^B))\right]_0
=r=N/4. \tag{12}$$

**Proof, with a more general formula.** Let $n\ge1$, $0\le k<n$, and
$N=2n+2$. For $0\le i<N$, define periodic $x$-profiles

$$A_i=-\max\{0,n-k-|i-n|\},$$
$$B_i=-\max\{0,k+1-\min(i,N-i)\}.$$

Their negative supports are disjoint on the integer ring: $A_i<0$ requires
$k<i<2n-k$, whereas $B_i<0$ requires $i<k+1$ or $i>N-k-1$.
Consequently $A\vee B=0$. Neighbor differences in each profile belong to
$\{-1,0,1\}$. Thus $h_i^A=i+A_i$ and $h_i^B=i+B_i$, extended helically with
mass $N$, have gaps in $\{0,1,2\}$, and $h^A\vee h^B$ is the balanced
profile $h_i=i$.

Use the word of successively shorter left-to-right sweeps

$$w=(0,1,\ldots,n-1;\ 0,1,\ldots,n-2;\ \ldots;\ 0).$$

It has $n(n+1)/2$ events. In each sweep the right neighbor has not yet been
updated in that sweep. Thus the value at zero after these sweeps is exactly
the value after $n$ parallel evaluations of $S$ on the dependency triangle
with initial indices $0,\ldots,n$.

On that interval, $A_i=\min(0,k-i)$. Its value after $s$ triangle layers is
$\min(s,k-i)$, because

$$S(\min(s,u),\min(s,u-1))=\min(s+1,u).$$

Also $B_i=\min(0,i-k-1)$. Each neighboring pair has equal values or rises by
one; applying $S$ therefore increases every value in the remaining triangle
by one. Its value after $s$ layers is $s+\min(0,i-k-1)$. The all-zero
profile has value $s$ after $s$ layers. At the final vertex these three
values are, respectively,

$$k,\qquad n-k-1,\qquad n.$$

Hence the maximum-envelope defect is
$n-\max(k,n-k-1)=\min(k+1,n-k)$. Taking $n=2r-1$, $k=r-1$ gives $N=4r$
and (12). All steps are valid original mass-process updates by (1).
$\square$

Any specified finite clock word has positive probability under the Poisson
clocks. Its probability here can be very small. This is a **pathwise**
obstruction to an envelope proof, not a stationary counterexample, not a
lower bound on expected oscillation, and not a disproof of (8).

## 8. Exact audit and finite-time experiment

Run, from the repository root:

```sh
python3 nasch/continuations/2026-10-24-height-comparison/verify.py
```

The standard-library verifier independently checks the height/mass generator
correspondence, exact backward-path identities, the binomial clock-word
counts underlying (3), coupled rings before the first winding, rational
current brackets for finite chains, and the explicit envelope counterexamples.
Results and all rational bracket values are under `results/`. These finite
checks complement the all-parameter proofs; they do not prove (8).

The optional C++ experiment in `exploratory/flat_oscillation.cpp` samples the
balanced-start process at the exact fixed time $t=\sqrt N$. It first samples
a Poisson number of events of mean $Nt$, then iid uniform clock identities.
There is no burn-in or stationarity approximation. Its fixed seed is
202610240701. `se_range` in the CSV is the usual sample standard error of
the empirical mean across repetitions, not a rigorous confidence bound.

Observed mean $\mathcal R(t)/t$ in this finite experiment:

| N | eta=0.5 | eta=1 | eta=1.5 |
|---:|---:|---:|---:|
| 64 | 0.51484 | 0.89375 | 1.45703 |
| 256 | 0.40508 | 0.75664 | 1.25000 |
| 1024 | 0.29922 | 0.59063 | 1.00254 |
| 4096 | 0.21250 | 0.43477 | 0.75205 |
| 16384 | 0.14665 | 0.30729 | 0.55241 |

The first four sizes use 160 repetitions per density; the last uses 48.
These observations support investigating (8), but establish neither a
uniform exponent nor the bound at other times or densities. They are not
used in any theorem.

## 9. Status for the next continuation

Proved here: (3)–(7), the conditional implication (8)–(9), the exact rank
conjugacy (10)–(11), and the counterexample family (12).

Not proved: (8), canonical convergence on any positive-density interval,
absence of large moving condensates, a general stationary formula, the
original first-passage formula for $T_N$, or any interchange of NaSch limits.

The most specific next target in this route is a rigorous finite-time
oscillation estimate from balanced initial configurations. A proof must
control the dependent retention marks in (4); treating them as iid, assuming
that the unfolded rank tree has independent branches, or using a bounded-error
maximum envelope would be invalid. The preceding fixed-cap, buffer, dilation,
and marked-exit-rank routes remain available and unresolved.
