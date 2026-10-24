# Canonical pile-probability convergence for the unit-rate backchip process

24 October 2026. **This continuation supplies a complete argument for the
fixed-density convergence of the canonical pile probability.** It proves
the finite-time estimate left open in the preceding continuation. The proof
and new exact audits are provided for independent review; this is not a
peer-reviewed publication or a formal proof-assistant certification. No
literature-priority claim is made.

The conclusion concerns the reduced continuous-time process. It does not
give an explicit formula for its limiting pile probability, prove convergence
of the entire canonical measure, exclude condensates, or solve the stationary
flow of the unrestricted discrete-time NaSch model.

## 1. Main theorem

At each independent rate-one site clock on an $N$-site ring, a mass $m$
retains $r(m)=\mathbf1_{\{m\ge2\}}$ and transfers $d(m)=m-r(m)$ to the
left neighbor. The total mass is $H$. Let $\pi_{N,H}$ be its unique invariant
law, and define

$$q_{N,H}=\pi_{N,H}(g_0\ge2),\qquad
F_{N,H}=H/N-q_{N,H}.$$

Finite uniqueness was established in the preceding work. For completeness,
the fixed word that double-fires donors $N-1,N-2,\ldots,1$ gathers every
state into the same single-pile state, so there is only one closed class.
Rotation invariance then identifies $F$ as the stationary current at each
bond.

**Theorem A.** There is a function $Q:[0,\infty)\to[0,1]$ such that, for
every finite $R>0$,

$$\sup_{0\le\eta\le R}
\left|q_{N,\lfloor\eta N\rfloor}-Q(\eta)\right|
=O_R\!\left(\left(\frac{\log(4N)}N\right)^{1/4}\right). \tag{1}$$

In particular, if $N_j\to\infty$ and $H_j/N_j\to\eta<\infty$, then

$$q_{N_j,H_j}\longrightarrow Q(\eta),\qquad
F_{N_j,H_j}\longrightarrow\eta-Q(\eta). \tag{2}$$

The same $Q(\eta)$ applies to every increasing road-size sequence. Thus the
question posed in the second-run handoff is answered affirmatively for every
$0<\eta<2$, and the reduced-process convergence statement holds at every
finite nonnegative density.

The central new ingredient is a finite-time spatial-oscillation bound. No
stationary moment-tail, phase-purity, or condensate-exclusion hypothesis is
used.

## 2. Notation and the previously proved comparison

Use increasing integer lifts

$$g_i=h_{i+1}-h_i,\qquad h_{i+N}=h_i+H.$$

At a clock $i$ the height update is

$$h_i\leftarrow B(h_i,h_{i+1}),\qquad
B(a,b)=\min\{b,\max\{a+1,b-1\}\},\quad a\le b. \tag{3}$$

Each update increases its updated height, preserves height order, and
commutes with common vertical translations. Let $\mathcal L$ and $P_t$
denote the height generator and semigroup for a fixed ring and fixed mass.

For $\theta=H/N$, start at $\ell_i=\lfloor\theta i\rfloor$ and set

$$U_i(t)=h_i(t)-\ell_i,\qquad
\mathcal R_{N,H}(t)=\mathbb E[\max_{0\le i<N}U_i(t)-\min_{0\le i<N}U_i(t)].$$

We use the following established results from the
[preceding height comparison](../2026-10-24-height-comparison/README.md).
They are inputs to this continuation, not new claims here:

* The backward right-going clock path has $Z(t)\sim\operatorname{Poisson}(t)$
  steps, even on a ring after winding. The full dependency diagram lies in
  its lifted interval. At an arbitrary starting site $i$,
  $0\le U_i(t)\le\theta Z(t)+1$; at $i=0$ the extra one can be omitted.
* Finite-time extrema bracket stationary speed:
  $|F_{N,H}-\mathbb E U_0(t)/t|\le\mathcal R_{N,H}(t)/t$.
* For $N,M\ge2$, $\theta=H/N$, $\varphi=K/M$, and $L=\min(N,M)$,

$$\begin{split}
|q_{N,H}-q_{M,K}|\le{}&2|\theta-\varphi|
+\frac{\mathcal R_{N,H}(t)+\mathcal R_{M,K}(t)+1}{t}\\
&+(\theta+\varphi)\Pr(\operatorname{Poisson}(t)\ge L-1).
\end{split} \tag{4}$$

The new proof supplies a bound for the two oscillations in (4).

## 3. Concentration of a local spatial average

**Lemma 1 (averaged-height martingale).** On an $m$-site ring of mass $h$,
let $A$ average any $\ell\le m$ consecutive lifted height coordinates.
Start from any deterministic admissible height profile and put $K=h/\ell$.
For every $t\ge0$ and $\lambda\ge0$,

$$\mathbb E\exp\!\left(\pm\lambda
[A(h(t))-\mathbb E A(h(t))]\right)
\le\exp\{t(e^{\lambda K}-1-\lambda K)\}. \tag{5}$$

When $K=0$ the centered variable is zero.

**Proof.** If the block is $J$, each physical clock appears at most once
in it, including for a block crossing the helical boundary. Hence

$$b(g):=\mathcal L A(h)=\frac1\ell\sum_{j\in J}d(g_j),
\qquad 0\le b(g)\le K. \tag{6}$$

Write $v_u=P_u A$. Monotonicity of the height semigroup implies
$v_u(T_i h)-v_u(h)\ge0$. The generator also satisfies

$$\mathcal L v_u=P_u b. \tag{7}$$

There is no unbounded-observable domain assumption hidden in (7): $b$ is a
bounded function on the finite gap state space, and Dynkin's formula gives
$P_u A=A+\int_0^u P_s b\,ds$. Apply $\mathcal L$ to this expression and
use the finite-state backward equation for $b$ to obtain (7).

Thus, pointwise in the current state and in $u$,

$$a_i(u,h):=v_u(T_i h)-v_u(h)\ge0,\qquad
\sum_i a_i(u,h)=P_u b(g)\le K. \tag{8}$$

In particular every $a_i\le K$. For a fixed terminal time $t$, the Doob
martingale $M_s=v_{t-s}(h(s))$, $0\le s\le t$, has these clock jumps.
It starts at $\mathbb E A(h(t))$ and ends at $A(h(t))$. Between jumps its
drift is $-\sum_i a_i$, by the backward equation. All rates and jumps are
bounded for this fixed ring.

For either sign of a real $\lambda$, convexity on $[0,K]$ yields

$$\sum_i(e^{\lambda a_i}-1-\lambda a_i)
\le\frac{\sum_i a_i}{K}(e^{\lambda K}-1-\lambda K)
\le e^{\lambda K}-1-\lambda K. \tag{9}$$

The compensated exponential-jump martingale and (9) bound
$\mathbb E e^{\lambda(M_t-M_0)}$ by the corresponding exponential on the
right of (5). For the negative sign, also use
$e^{-z}-1+z\le e^z-1-z$ for $z\ge0$. This proves (5). $\square$

The key point in (8) is a bound on the **sum** of predictive jump sizes.
It avoids paying an additional factor equal to the number of clocks.

## 4. From averages to one height

Consider the $m$-site ring in Lemma 1 at density $\phi=h/m$, now started
at $\ell_j=\lfloor\phi j\rfloor$. Put $V_j=h_j(t)-\ell_j$ and
$f=\mathbb E V_0$.

**Lemma 2 (phase means and spatial sandwich).** For every lifted index $j$,

$$0\le\mathbb E V_j-f\le1. \tag{10}$$

Let $A^+$ and $A^-$ average the increments $V_j$ over
$j=0,\ldots,\ell-1$ and $j=-\ell+1,\ldots,0$, respectively. There are
centered variables

$$X^+=A^+-\mathbb E A^+,\qquad
X^-=\mathbb E A^- -A^-$$

which each obey the positive-sign exponential bound in (5), and, with
$b=\phi\ell+1$,

$$V_0-f\le b+X^+,\qquad f-V_0\le b+X^-. \tag{11}$$

**Proof.** The rotated, vertically recentered initial profile
$\ell_{i+j}-\ell_j$ differs from $\ell_i$ by either zero or one at each
coordinate. Both profiles have the same helical mass. Coupling by rotated
clocks and using height monotonicity keeps that difference between zero and
one. At coordinate zero, the two laws are those of $V_j$ and $V_0$.
This proves (10), for negative indices as well as positive ones.

At all times the lifted heights are nondecreasing in space. Consequently

$$V_0\le A^++\frac1\ell\sum_{j=0}^{\ell-1}\ell_j,
\qquad
V_0\ge A^-+\frac1\ell\sum_{j=-\ell+1}^{0}\ell_j.$$

The deterministic initial averages are at most
$\phi(\ell-1)/2$ and at least $-\phi(\ell-1)/2-1$, respectively.
Combining these facts with (10) proves (11) using the stated, deliberately
loose constant $b$. Subtracting a deterministic initial average does not
change a centered random variable, so Lemma 1 applies to both $X^+$ and
$X^-$, using its two signs. $\square$

**Lemma 3 (many copies, without independence).** Suppose
$V^{(1)},\ldots,V^{(n)}$ each have the law of $V_0$ above; their joint
dependence is arbitrary. If $t\ge\log(2n)$, then

$$\mathbb E[\max_i V^{(i)}-\min_i V^{(i)}]
\le 2b+4K\sqrt{t\log(2n)},\qquad K=h/\ell. \tag{12}$$

**Proof.** Realize the left and right averages for each copy on its own
underlying ring; this allows any dependencies already present. Equation
(11) gives

$$\max_i|V^{(i)}-f|\le b+\max_{i,\sigma\in\{+,-\}}X_i^\sigma.$$

For $a=\log(2n)$ and $K>0$, the log-sum-exponential inequality and (5) give

$$\mathbb E\max_{i,\sigma}X_i^\sigma
\le\frac{a+t(e^{\lambda K}-1-\lambda K)}\lambda.$$

Choose $\lambda=K^{-1}\sqrt{a/t}$. Then $0\le\lambda K\le1$, and
$e^z-1-z\le z^2$ on this interval. The last bound is at most
$2K\sqrt{ta}$. The range is at most twice the maximum absolute deviation
from $f$, proving (12). The case $K=0$ is immediate. $\square$

## 5. Localization to rings of size proportional to time

**Theorem B (unconditional oscillation bound).** Let $H/N\le R$, and suppose

$$t\ge\max\{1,\log(2N)\},\qquad \lceil4t\rceil\le N.$$

With $c=3\log3-2>0$,

$$\boxed{\quad
\mathcal R_{N,H}(t)
\le22R\,[t^3\log(2N)]^{1/4}+2R+6
 +2N(2Rt+1)e^{-ct}.
\quad} \tag{13}$$

**Proof.** Put $\theta=H/N$, $m=\lceil4t\rceil$,
$h=\lfloor\theta m\rfloor$, and $\phi=h/m\le\theta$.
For every target site $i$, construct an auxiliary $m$-site ring with balanced
initial density $\phi$, using the target clocks at
$i,i+1,\ldots,i+m-1\pmod N$. These are distinct physical clocks because
$m\le N$. Each auxiliary ring separately has independent rate-one clocks.
Different auxiliary rings are allowed to share clocks.

Let $V_i$ be the auxiliary height increment at its site zero. All $V_i$ have
the same marginal law. Compare the target height at $i$, recentered by its
initial height, to that auxiliary height. Before the common backward path
reaches lifted site $m$, its initial leaves have indices $0\le j<m$.
Writing $\alpha_i=\theta i-\lfloor\theta i\rfloor\in[0,1)$, the two initial
leaf heights differ by

$$\lfloor\theta j+\alpha_i\rfloor-\lfloor\phi j\rfloor\in\{0,1,2\}. \tag{14}$$

Indeed $0\le\theta-\phi<1/m$ and $j<m$. Monotonicity and vertical
homogeneity propagate this integer difference through their shared
dependency diagram. Therefore $|U_i-V_i|\le2$ outside the event $D_i$ that
the common path reaches $m$.

For the target and auxiliary path counts, respectively, we have exactly

$$D_i=\{Z_i\ge m\}=\{\widetilde Z_i\ge m\},$$

and both counts have marginal law $\operatorname{Poisson}(t)$. No
independence between these counts, the heights, or different $i$ is used.
The pathwise growth bounds give, also on $D_i$,

$$0\le U_i\le\theta Z_i+1,\qquad
0\le V_i\le\phi\widetilde Z_i.$$

Put $p=\Pr(\operatorname{Poisson}(t)\ge m-1)$. The Poisson identity
$\mathbb E[Z\mathbf1_{\{Z\ge m\}}]=t\Pr(Z\ge m-1)$ implies

$$\begin{split}
\mathbb E\max_i|U_i-V_i|
&\le 2+\sum_i\mathbb E[(U_i+V_i)\mathbf1_{D_i}]\\
&\le2+N[(\theta+\phi)t+1]p. \tag{15}
\end{split}$$

The range of the target variables is at most the range of the auxiliary
variables plus twice their maximum coordinatewise difference. Applying
(12), for any integer $1\le\ell\le m$, therefore gives

$$\mathcal R_{N,H}(t)
\le2R\ell+6+\frac{4Rm}{\ell}\sqrt{t\log(2N)}
       +2N(2Rt+1)p. \tag{16}$$

Choose $\ell=\lceil[t^3\log(2N)]^{1/4}\rceil$. The assumption
$\log(2N)\le t$ ensures $\ell\le\lceil t\rceil\le m$.
Since $t\ge1$, we also have $m\le5t$ and $m-1\ge3t$.
The elementary Poisson exponential bound gives

$$p\le\exp[-t(3\log3-3+1)]=e^{-ct}.$$

Finally, the first two nonconstant terms in (16) are bounded by
$22R[t^3\log(2N)]^{1/4}+2R$. This proves (13). $\square$

The localization is essential: the total mass in each auxiliary ring is
$O_R(t)$, so the martingale constant is $K=O_R(t/\ell)$, rather than
$O_R(N/\ell)$. Applying Lemma 1 directly on the large ring would give an
insufficient bound.

## 6. Proof of the canonical limit

Fix $R>0$ and $0\le\eta\le R$, and abbreviate
$q_n(\eta)=q_{n,\lfloor\eta n\rfloor}$. Let $n\le m\le2n$, $n\ge64$,
and choose $t=n/8$. For both target rings, the conditions of Theorem B hold:
$\lceil4t\rceil=\lceil n/2\rceil\le n$, and
$t\ge\log(4n)\ge\log(2m)$. Their densities differ by at most $2/n$.

Applying (4) and (13), and using
$n-1\ge7t$, yields the explicit comparison

$$|q_n(\eta)-q_m(\eta)|\le E_R(n), \tag{17}$$

where, with $c_3=3\log3-2$ and $c_7=7\log7-6$,

$$\begin{split}
E_R(n)={}&44R\left(\frac{8\log(4n)}n\right)^{1/4}
+\frac{32R+108}{n}\\
&+(12Rn+48)e^{-c_3n/8}+2R e^{-c_7n/8}.
\end{split} \tag{18}$$

Every constant in (18) is explicit. For example, the $1/n$ contribution
combines the two constant terms of (13), the rounding term in (4), and the
density difference. The exponential term from (13) uses $n+m\le3n$.

Define the convergent, explicit series

$$\Omega_R(n)=\sum_{j=0}^{\infty}E_R(2^j n). \tag{19}$$

For arbitrary $m\ge n\ge64$, compare $n,2n,4n,\ldots$ until the last
doubling below $m$, then compare that size with $m$. All comparisons have
size ratio between one and two. Equation (17) gives

$$\sup_{0\le\eta\le R}|q_n(\eta)-q_m(\eta)|\le\Omega_R(n). \tag{20}$$

To see that $\Omega_R(n)\to0$ with the claimed order, its main series is
bounded by a constant times

$$n^{-1/4}\sum_{j\ge0}2^{-j/4}
       [\log(4n)+j\log2]^{1/4}
\le C n^{-1/4}[\log(4n)]^{1/4},$$

because $\sum_j2^{-j/4}(1+j)^{1/4}<\infty$. The $1/n$ terms form a
geometric series. The two exponential series are smaller than this order
as $n\to\infty$. Thus (20) proves the uniform Cauchy property and (1),
with the explicit bound

$$\sup_{0\le\eta\le R}|q_n(\eta)-Q(\eta)|\le\Omega_R(n). \tag{21}$$

There is no unproved hypothesis remaining in this argument.

For the joint limit (2), compare on the **same** ring the masses $H_n$ and
$\lfloor\eta n\rfloor$. Use (4) at $t=n/8$ and (13), with a common fixed
upper bound $R$ on their densities. The oscillation and Poisson terms tend
to zero, while the density term is at most

$$2|H_n/n-\lfloor\eta n\rfloor/n|\longrightarrow0.$$

Consequently the corresponding pile probabilities differ by $o(1)$, which
proves (2). This argument applies to any subsequence of road sizes as well.
$\square$

The same comparison shows directly that $Q$ is 2-Lipschitz. The sharper
previously proved finite mass-response inequality implies that $Q$ is in
fact nondecreasing and $2/3$-Lipschitz. That sharper constant is inherited
from the earlier work and is not needed for Theorem A.

## 7. What this resolves, and what it does not

The target observable has a unique thermodynamic limit, including in the
presence of any possible stationary large-pile behavior. The proof does not
need to decide whether such piles occur. Therefore they cannot cause
subsequence-dependent values of this observable.

For the previously established **fixed-system, rare-braking-first** NaSch
reduction, put $\rho=1/(1+\eta)>1/3$. Its thermodynamic coefficient now
exists and is

$$C(\rho)=\rho\,[\eta-Q(\eta)]
=1-\rho-\rho\,Q((1-\rho)/\rho). \tag{22}$$

Equation (22) identifies the coefficient through the proved limiting
function, not through an elementary closed form. The order of limits remains
rare braking first at each finite system, followed by road size.

Still unresolved here:

* an explicit formula for $Q(\eta)$ or the general canonical stationary law;
* uniqueness of the entire subsequential local canonical measure, stationary
  mass uniform integrability, and exclusion or characterization of condensates;
* a strict positive lower bound for limiting occupancy or pile probability;
* the original three-hole first-passage formula $T_N$;
* interchange of the rare-braking and thermodynamic limits, and the general
  stationary traffic-flow formula at fixed braking probability.

These distinctions limit the theorem's scope; they are not missing steps in
the pile-probability convergence proof.

## 8. Verification and provenance

The new standard-library audit can be run from the repository root:

```sh
python3 nasch/continuations/2026-10-24-thermodynamic-limit/verify_new_step.py
```

It uses integer-scaled embedded semigroups, including transient states, to
test the genuinely new predictive-jump and generator-commutation claims.
The old continuation's checks and simulations were not rerun.

All new checks passed: 54 finite chains, 432 averaged-height observables,
7,724,727 predictive-jump checks, 1,194,264 exact commutation checks,
2,187 phase-mean checks, 132,696 spatial-sandwich checks, and 1,131,601
localization-rounding checks. The recorded output is in `results/`.

The infinite-size conclusion is obtained from the analytic proof, not from
extrapolating these checks. The exponential martingale argument, log-sum
bound, and convergent dyadic series are proved in the text. The separate
audit note identifies their delicate points. No new simulation is used.

The process has a literature antecedent in Whitehouse, Costa, Blythe and
Evans, [arXiv:1407.1668](https://arxiv.org/abs/1407.1668), at constant rate.
General concentration methods for growing surfaces also have a substantial
literature; see, for context, Chatterjee,
[arXiv:2103.09199](https://arxiv.org/abs/2103.09199). No theorem from that paper
is imported into the argument. The model-specific proof above is supplied
in full, without an assertion that the result is first in the literature.
