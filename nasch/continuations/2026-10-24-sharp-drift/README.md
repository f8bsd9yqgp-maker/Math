# A sharp uniform drift bound for the backchip process

24 October 2026. AI-assisted working mathematics, internally audited with
exact integer and rational arithmetic; not independently peer-reviewed.
No claim of literature priority is made.

**The fixed-density canonical thermodynamic limit remains open.** The new
result is a sharp inequality valid for every finite ring with at least three
sites, together with bounds on finite-time averages and on modified bonds.
It does not establish convergence, phase selection, or absence of condensates.

## 1. Model and main theorem

For a ring of $N\ge3$ sites, let $g_i\in\mathbb N_0$ and
$\sum_i g_i=H$. Independent rate-one clocks apply

$$
(g_{i-1},g_i)\mapsto(g_{i-1}+d(g_i),r(g_i)),\qquad
r(m)=\mathbf1_{\{m\ge2\}},\quad d(m)=m-r(m).
$$

Write $L=\sum_i(T_i-I)$ for the generator, $Q(g)=\sum_i r(g_i)$,
$\pi_{N,H}$ for its unique stationary distribution, and

$$q_{N,H}=\pi_{N,H}(g_0\ge2),\qquad F_{N,H}=H/N-q_{N,H}.$$

For completeness, two consecutive firings empty any donor. Descending double
firings gather every state at a specified site. Every closed recurrent class
therefore contains that single-pile state. The finite chain has exactly one
closed class and a unique stationary law; uniqueness makes it cyclically
translation invariant. Full irreducibility is not required.

**Theorem 1.** For every $N\ge3$ and $H\ge0$,

$$
\boxed{q_{N,H}\le\frac{5H}{17N},\qquad
F_{N,H}\ge\frac{12H}{17N}.}                              \tag{1}
$$

The coefficient $5/17$ is optimal over this entire finite-system class:
equality holds at $(N,H)=(3,3)$. This is not a claim of asymptotic sharpness
as $N\to\infty$. The hypothesis $N\ge3$ matters: $q_{2,2}=1/3>5/17$.

A stronger tail-sensitive statement is

$$
17q_{N,H}+\mathbb E_{\pi_{N,H}}(5g_0-18)_+
\le 5H/N.                                               \tag{2}
$$

Equivalently, $17q_{N,H}\le\mathbb E\min(5g_0,18)$.
All these assertions concern the reduced continuous-time process. They do
not solve the unrestricted discrete-time Nagel--Schreckenberg model.

## 2. An explicit bounded potential

All arguments of the tables below are clipped to $3$. Thus, for example,
$P(7,2)=P(3,2)$. Define

$$
P=\begin{pmatrix}
15&15&14&11\\
15&11&11&11\\
2&0&1&2\\
1&0&0&0
\end{pmatrix},\qquad
\Phi(g)=\sum_i P(g_i,g_{i+1}).                            \tag{3}
$$

In particular $0\le\Phi\le15N$. A telescoping auxiliary table $W(a,b,c)$
has the following four slices, indexed by $a$; rows are $b$ and columns $c$:

$$
W_0=\begin{pmatrix}3&2&2&3\\6&11&10&6\\4&3&2&0\\3&0&0&0\end{pmatrix},\quad
W_1=\begin{pmatrix}3&6&6&6\\6&10&9&2\\4&0&0&0\\3&0&0&0\end{pmatrix},
$$

$$
W_2=\begin{pmatrix}3&4&4&3\\6&9&8&0\\4&0&0&0\\3&0&0&0\end{pmatrix},\quad
W_3=\begin{pmatrix}3&3&3&3\\6&10&9&2\\4&0&0&0\\3&0&0&0\end{pmatrix}. \tag{4}
$$

Put $a=g_{i-2},b=g_{i-1},c=g_i,e=g_{i+1}$, $r=r(c)$, and $d=c-r$.
For any partial transfer $0\le v\le d$, define

$$
\Delta_v(a,b,c,e)=P(a,b+v)-P(a,b)
+P(b+v,c-v)-P(b,c)+P(c-v,e)-P(c,e).                       \tag{5}
$$

This is the actual change of $\Phi$ at that transfer. For $N=3$, $a=e$;
the three affected bonds are still distinct, so (5) remains valid. For
$N=2$ they are not distinct, which is why that case is excluded.

The certificate is the pointwise inequality

$$
Z(a,b,c,e):=5c-17r(c)+\Delta_d(a,b,c,e)
 +W(a,b,c)-W(b,c,e)\ \ge\ (5c-18)_+\ \ge0.               \tag{6}
$$

Here is a finite, fully specified arithmetic proof of (6). Clipping the
non-donor coordinates $a,b,e$ at $3$ leaves the expression unchanged.
For $c\ge4$, all table arguments are constant as $c$ increases: $r=1$,
$d\ge3$, and the receiving mass $b+d$ clips to $3$. Consequently

$$Z(a,b,c,e)=Z(a,b,4,e)+5(c-4),\qquad c\ge4.              \tag{7}$$

It therefore suffices to check $4^3\cdot5=320$ integer inequalities.
The following matrices give $\min_{0\le a\le3}Z(a,b,c,e)$, with rows
$b=0,1,2,3$ and columns $e=0,1,2,3$, for $c=0,1,2,3,4$ respectively:

$$
M_0=\begin{pmatrix}0&1&1&0\\3&0&0&0\\1&0&0&1\\0&0&0&0\end{pmatrix},\quad
M_1=\begin{pmatrix}1&0&0&1\\0&0&0&4\\0&1&1&6\\0&0&0&4\end{pmatrix},
$$

$$
M_2=\begin{pmatrix}1&0&0&1\\0&2&1&0\\0&2&1&0\\2&4&3&2\end{pmatrix},\quad
M_3=\begin{pmatrix}0&0&0&0\\0&0&0&0\\4&4&4&4\\9&9&9&9\end{pmatrix},
$$

$$M_4=\begin{pmatrix}2&2&2&2\\5&5&5&5\\9&9&9&9\\14&14&14&14\end{pmatrix}. \tag{8}$$

Every entry is nonnegative, and every entry in $M_4$ is at least $2$.
Equations (7)--(8) prove (6) for every nonnegative integer quadruple.
These small tables can be checked directly from (3)--(5); the independent
standard-library verifier recomputes every entry with integers.

Sum (6) over all donor sites. The $W$ terms cancel by cyclic reindexing.
The $\Delta_d$ terms sum to $L\Phi$. Thus, pointwise on every ring,

$$
L\Phi=17Q-5H+\sum_i Z(g_{i-2},g_{i-1},g_i,g_{i+1})
\ge17Q-5H+\sum_i(5g_i-18)_+.                            \tag{9}
$$

Stationarity of the bounded function $\Phi$ gives $\mathbb E L\Phi=0$.
Using cyclic invariance and dividing by $N$ proves (1)--(2).

To verify sharpness, at $(N,H)=(3,3)$ the ten labelled states and their
stationary weights, in the displayed order, are

$$
\begin{array}{c|rrrrrrrrrr}
g&003&012&021&030&102&111&120&201&210&300\\\hline
17\pi(g)&2&1&2&2&2&2&1&1&2&2.
\end{array}
$$

Direct substitution verifies all ten balance equations. The only state
without a pile is $111$, so $\mathbb E Q=15/17$ and $q=5/17$.
For $(N,H)=(2,2)$ the three states $02,11,20$ have equal weights,
giving the stated exception. This completes the proof of Theorem 1.

The earlier bound $q_{N,H}\le H(H-1)/[N(H+N-1)]$ is stronger at some
small masses. Taking the minimum of the two bounds is valid. For $H>0$,
the new linear bound is strictly smaller exactly when $12(H-1)>5N$.
No comparison with that earlier theorem is needed in the proof above.

## 3. Uniform bounds before equilibrium

**Theorem 2.** Start from any state, or any initial distribution of fixed
total mass $H$, on $N\ge3$ sites. For all $t>0$,

$$
\mathbb E\left[\frac1{Nt}\int_0^t Q(g_s)\,ds\right]
\le\frac{5H}{17N}+\frac{15}{17t}.                        \tag{10}
$$

Furthermore, for $\epsilon>0$, with
$h(u)=(1+u)\log(1+u)-u$,

$$
\Pr\left\{\frac1{Nt}\int_0^t Q(g_s)\,ds
 \ge\frac{5H}{17N}+\frac{15}{17t}+\epsilon\right\}
\le \exp\{-Nt\,h(17\epsilon/14)\}.                      \tag{11}
$$

These are bounds above a universal envelope. They are not concentration
about the unknown stationary value $q_{N,H}$, and contain no assertion of
mixing or equilibration.

**Proof.** Dynkin's formula, (9), and $0\le\Phi\le15N$ give (10).
Define the martingale

$$M_t=\Phi(g_t)-\Phi(g_0)-\int_0^t L\Phi(g_s)\,ds.$$

Equation (9) yields the pathwise upper bound

$$\frac1{Nt}\int_0^t Q(g_s)\,ds
\le\frac{5H}{17N}+\frac{15}{17t}-\frac{M_t}{17Nt}.        \tag{12}$$

Every clock changes $\Phi$ by at most $14$ in absolute value. This follows
by checking (5) for $a,b,e\in\{0,1,2,3\}$ and $c\in\{0,1,2,3,4\}$;
larger masses reduce by the same clipping argument. The verifier checks all
320 increments, and the maximum is exactly $14$.

For $\theta>0$ and $|x|\le14$,

$$e^{-\theta x}-1+\theta x\le e^{14\theta}-1-14\theta.$$

There are $N$ rate-one potential clocks, including null events. The jump
exponential formula therefore shows that

$$\exp\{-\theta M_t-Nt(e^{14\theta}-1-14\theta)\}$$

is a nonnegative supermartingale, initially one. Alternatively, its
nonpositive conditional drift follows directly by expanding at each clock
event; bounded jumps and finite rate justify localization and expectation.
Chernoff's inequality now gives

$$\Pr(-M_t\ge17Nt\epsilon)
\le\inf_{\theta>0}\exp\{Nt(e^{14\theta}-1-14\theta-17\theta\epsilon)\}.$$

Choose $14\theta=\log(1+17\epsilon/14)$ and use (12) to obtain (11).
The argument bounds the integrated pile count; it is not a bound for the
mass-current martingale, whose jumps can be large. $\square$

## 4. Robustness to finitely many partial-transfer bonds

**Theorem 3.** Modify the rules at a set $S$ of $k$ sites, keeping their
rate-one potential clocks. At a modified event allow any transfer
$v\in\{0,\ldots,d(g_i)\}$, chosen as part of a finite Markov extension if
desired. Leave all other sites unchanged and conserve total mass $H$.
For every stationary law of this modified system,

$$\bar q:=\frac1N\mathbb E Q\le\frac{5H}{17N}+rac{14k}{17N}. \tag{13}$$

Translation invariance and uniqueness of the modified stationary law are
not required. Capped transfers are one example of the allowed modifications.

**Proof.** Direct integer checking of (5) gives

$$\Delta_d(a,b,c,e)-\Delta_v(a,b,c,e)\le14,
\qquad 0\le v\le d(c).                                  \tag{14}$$

Here the finite reduction is slightly different. Clip $a,b,e$ at $3$.
For $c\le3$, check all allowed $v$. For $c\ge4$, the full-transfer terms
are constant; the partial-transfer terms depend only on
$\min(v,3)$ and $\min(c-v,3)$. The residual $c-v$ is at least one.
Every such pair of clipped values has a representative with $4\le c'\le6$:
choose the clipped values themselves, raising a value clipped at three if
needed to make their sum at least four. The sole pair whose clipped sum
is below four is $(0,3)$, represented by $(v',c'-v')=(0,4)$.
Their largest minimal sum is six. The verifier uses the slightly redundant
range $0\le c\le7$, containing 1,920 integer inequalities, whose maximum
left side is exactly $14$.

Let $L'$ be the modified generator. Equations (9) and (14) imply
$L'\Phi\ge17Q-5H-14k$. Extra transitions of an auxiliary state do not alter
$\Phi$. Stationarity and division by $17N$ prove (13). $\square$

This is a shared absolute upper bound. It does **not** say that changing
$k$ bonds changes the stationary pile probability by $O(k/N)$; no such
difference estimate follows from (13). For capped systems the current also
contains the cap-overflow term, so it must not be replaced by $H/N-\bar q$.

## 5. Infinite-volume consequence and its limitation

For any translation-invariant stationary infinite-line law $\mu$ with
finite mean $\rho$, the same certificate gives

$$17q(\mu)+\mathbb E_\mu(5g_0-18)_+\le5\rho.             \tag{15}$$

To justify this without summing an infinite potential, apply stationarity
to the bounded cylinder $P(g_0,g_1)$. Translation invariance makes its
expected generator equal to the expectation of the three terms in
$\Delta_d(g_{-2},g_{-1},g_0,g_1)$. Translation invariance also cancels the
two $W$ expectations. Taking expectations in (6) proves (15).
All generator terms here are bounded. Indeed the equivalent bound

$$17q(\mu)\le\mathbb E_\mu\min(5g_0,18)$$

does not require a first moment: subtract $(5c-18)_+$ from (6) before
taking expectations.

If $\rho>0$, the linear bound is strict: $17q(\mu)<5\rho$.
Here is a proof of strictness, rather than an extrapolation from finite
examples. A translation-invariant law cannot put positive probability on
a nonzero configuration with finite total mass. Conditional on total mass
at most $K$ and at least one, translation invariance would give
$L\Pr(g_0>0)\le K$ for every block length $L$, a contradiction as
$L\to\infty$. Thus positive probability of nonzero mass implies positive
probability that some fixed finite interval contains at least four units.
Freeze its outside input and output clocks and perform descending double
firings inside it. This positive-probability finite clock word gathers at
least four units at a fixed endpoint; hold it there until a deterministic
time. Stationarity implies $\mu(g_0\ge4)>0$ after a spatial shift.
By (6)--(8), $Z\ge2$ on this event. Hence
$5\rho-17q(\mu)=\mathbb E Z>0$. No quantitative strictness uniform in
$\mu$ follows from this argument.

For the canonical target with $H_N/N\to\eta$ this establishes only

$$0\le\liminf_N q_{N,H_N}\le\limsup_N q_{N,H_N}\le5\eta/17.$$

The earlier phase theorem identifies a canonical local subsequential limit
as $\int\nu_\rho\,\kappa(d\rho)$ with
$\int\rho\,\kappa(d\rho)\le\eta$. The present result restricts the
admissible phases but does not identify $\kappa$, prove equality of its mean
with $\eta$, or show that $\int q(\nu_\rho)\,\kappa(d\rho)$ is independent
of the subsequence. Large moving piles remain an unresolved mechanism for
loss of mean. None of the three new theorems rules it out.

## 6. Negative dependence is not preserved

The previous finite stationary calculations had found no positive pile
covariances. A possible route to phase selection was therefore to prove
preservation of negative dependence and pass it to stationarity. The
following exact counterexample rules out that general preservation claim.

**Theorem 4.** Start the four-site chain of mass seven from
$g=(0,0,0,7)$. Put $I_i(t)=\mathbf1_{\{g_i(t)\ge2\}}$. Then

$$\operatorname{Cov}(I_0(t),I_1(t))=t^4/24+O(t^5)>0$$

for all sufficiently small positive $t$. In fact it is positive for
$0<t\le1/4096$. Thus the semigroup does not preserve negative association
of the pile indicators, even from deterministic full mass configurations
at a fixed density in $(0,2)$.

**Proof.** Include all potential events, so their total count $K_t$ is
Poisson with mean $4t$. Conditional on $K_t=k$, the $k$ clock labels are
independent and uniform on $\{0,1,2,3\}$.
Pile creation at site 1 requires at least two events; at site 0 it requires
at least three. There is no clock word of length at most three producing
both piles. At length four the unique word producing both is

$$
(0,0,0,7)\xrightarrow{3}(0,0,6,1)
\xrightarrow{2}(0,5,1,1)\xrightarrow{1}(4,1,1,1)
\xrightarrow{2}(4,2,0,1).                                \tag{16}
$$

For uniqueness, reaching site 0 in three events requires the ordered
word $3,2,1$. If the fourth event is before the last firing of site 1,
that last firing leaves site 1 with at most one unit. Thus it must be
after this word; only clock 2 then creates the second pile.
Consequently $\mathbb E[I_0 I_1]=e^{-4t}t^4/24+O(t^5)$, while
$\mathbb E I_0=O(t^3)$ and $\mathbb E I_1=O(t^2)$. This proves the
expansion. For the explicit interval, factorial moments of $K_t$ give

$$
\operatorname{Cov}(I_0,I_1)
\ge e^{-4t}t^4/24-\Pr(K_t\ge3)\Pr(K_t\ge2)
\ge t^4\left[\frac{1-4t}{24}-\frac{4^5t}{12}\right]>0
$$

when $0<t\le1/4096$. Deterministic fields are negatively associated, so
the conclusion follows. All 341 words of length at most four are also
checked by the verifier. $\square$

This does **not** refute negative association of the canonical stationary
law itself. The displayed law at positive time is transient. In particular,
this is not a stationary nonconvergence counterexample. It blocks one
natural method for proving a stationary correlation bound, not every such
method.

## 7. Reproduction and provenance

Run, from the repository root, with Python 3.9 or later:

```sh
python3 nasch/continuations/2026-10-24-sharp-drift/verify.py
```

The verifier requires only the Python standard library. It checks all
essential integer inequalities and the clipping reductions on additional
inputs. It also independently computes actual before/after potentials on
4,950 full ring configurations and 26,928 clock events, and solves 12 finite
chains, checking 275 stationary balance equations in rational arithmetic.
It separately checks the 341 short words for Theorem 4 and the exact
capped-current concavity counterexample recorded in the closure log.
The stationary examples corroborate the theorem; the analytic reduction
(7) and the finite certificate, not extrapolation, prove its all-size scope.

The potential was discovered using SciPy linear and integer programming.
A coboundary gauge $u(a)-u(b)$, $u=(11,0,0,0)$, reduced the potential's
range without changing any cyclic sum or transfer increment. Optimizer
statuses and floating-point slacks are not used in the proof.
The separately labelled exploratory directory preserves those searches.

- [Exact tables](certificate.json)
- [Verifier](verify.py)
- [Recorded audit](results/verified.json)
- [Exact stationary examples](results/stationary_certificates.json)
- [Complete recurrent support and matrix obstructions](SUPPORT_AND_MATRIX_OBSTRUCTION.md)
- [Support and matrix audit](support_verify.py)
- [Unfinished closure attempts](CLOSURE_ATTEMPTS.md)
- [Next-run handoff](HANDOFF.md)
- [File manifest](MANIFEST.json)
