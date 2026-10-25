# A uniform positive pile-density theorem

24 October 2026. AI-assisted mathematical research. The proofs and exact
computations below are internally audited, not independently peer reviewed
or formally certified. No literature-priority claim is made.

## 1. Result and scope

Consider the continuous-time backchip process on an N-site ring. At rate
one, site i of mass g_i retains r(g_i)=1{g_i>=2} and transfers
 d(g_i)=g_i-r(g_i) to site i-1. Write H=sum g_i, theta=H/N and
q_(N,H)=pi_(N,H)(g_0>=2), where pi is the unique finite stationary law.
The uniqueness follows by gathering all mass with descending double firings.

**Theorem 1 (uniform positive pile density).** For every N>=3 and H>=2,

\[
\boxed{\quad q_{N,H}\ \ge\ \frac{\min\{H/N,1\}^{3}}{1152}.\quad}       \tag{1}
\]

Consequently, for the limiting function established in the
[preceding continuation](../2026-10-24-thermodynamic-limit/README.md),

\[
\boxed{\quad Q(\eta)\ge\frac{\min\{\eta,1\}^{3}}{1152}>0
                 \qquad(\eta>0).\quad}                              \tag{2}
\]

The constants are deliberately conservative. A stronger explicit
one-parameter bound is given in (17), without a small-parameter expansion.
The H>=2 qualification is necessary: at H=1, q_(N,1)=0.

This is new relative to the preceding project record, which proved scalar
canonical convergence but left even positivity open. The proof does not
assume stationary mass uniform integrability, stationary negative
correlations, an independent-site approximation, or absence of condensates.
It uses a positive function of the evolving height profile and exact
empty-block generator identities.

This does **not** give an elementary formula for Q, the whole stationary
law, or the full discrete-time NaSch traffic flow at fixed braking
probability. It does not exclude partial condensation or all escaped mean
mass. Those remain unresolved.

## 2. Heights, weights, and bounded local potentials

Use integer lifted heights

\[
g_i=h_{i+1}-h_i,\qquad h_{i+N}=h_i+H.
\]

A clock at i increases h_i by d(g_i). Fix lambda>0 and set

\[
v_i=\exp[\lambda(h_i-\theta i)],\quad
V=\sum_{i=0}^{N-1}v_i,\quad
G=\sum_i v_i g_i,\quad
P=\sum_i v_i\mathbf1_{\{g_i=1\}},\quad
R=\sum_i v_i r(g_i).                                      \tag{3}
\]

The v_i are genuinely N-periodic, since theta*N=H. Denote the generator
by \(\mathcal L\); the block length below is the integer ell, not the
generator. Two elementary bounds are

\[
\sum_i v_i e^{\lambda g_i}=e^{\lambda\theta}V,
\qquad
G\le \frac{e^{\lambda\theta}-1}{\lambda}V.                 \tag{4}
\]

The first identity follows from v_i e^(lambda*g_i)=e^(lambda*theta)v_(i+1).
The second follows from exp(x)-1>=x for x>=0.

Put delta=1-exp(-lambda*theta). Since v_(i+1)>=exp(-lambda*theta)v_i,

\[
\sum_i(v_i-v_{i-1})_+
 =\sum_i(v_{i-1}-v_i)_+\le\delta V.                        \tag{5}
\]

Thus for arbitrary numbers 0<=z_i<=1,
\(\sum_i(v_i-v_{i-1})z_i\le\delta V\). This remains valid for profiles
with arbitrarily large piles; no upper bound on an individual gap is used.

Let
\[
e_{i,k}=\mathbf1_{\{g_i=\cdots=g_{i+k-1}=0\}},\qquad e_{i,0}=1,
\quad E_k=\sum_i v_i e_{i,k},
\quad A=\sum_i v_i\mathbf1_{\{g_i>0\}}=P+R.
\]

For 1<=k<N the exact local generator identity is

\[
\mathcal L e_{i,k}
 =e_{i+1,k-1}-2e_{i,k}+e_{i,k+1}
       -r(g_i)e_{i+1,k-1}.                                \tag{6}
\]

Indeed, an empty block is created only when its leftmost site contains a
singleton and fires, with all remaining block sites empty. It is destroyed
only when a positive incoming donor immediately to its right fires.
These gains and losses give
\(\mathbf1_{\{g_i=1\}}e_{i+1,k-1}-e_{i,k}\mathbf1_{\{g_{i+k}>0\}}\),
which is (6). An internal move cannot empty the entire block because it
keeps positive mass inside. The incoming boundary is distinct when k<N.

## 3. A weighted empty-block certificate

Fix an integer 3<=ell<=N, and define

\[
a_\ell=\frac{\ell-3}{\ell+1},\qquad
b_\ell=\frac4{\ell(\ell+1)},\qquad
m_\ell=\frac{2(\ell-1)}{\ell+1}<2,\qquad
K_\ell=\frac{2(\ell-1)(\ell-2)}{\ell(\ell+1)}<2,
\]
\[
\phi_i=\frac4{\ell(\ell+1)}
             \sum_{k=1}^{\ell-1}(\ell-k)e_{i,k},\qquad
\Phi=\sum_i v_i\phi_i.                                    \tag{7}
\]

In particular 0<=phi_i<=m_ell.

**Lemma 2 (pointwise weighted certificate).** Every mass and height
configuration satisfies

\[
\boxed{\quad P\le a_\ell G+(b_\ell+K_\ell\delta)V
                         +\mathcal L\Phi.\quad}           \tag{8}
\]

**Proof.** Multiply (6) by v_i and sum, holding the weights fixed when
applying the generator to e. Write
\(R_{k-1}=\sum_i v_i r(g_i)e_{i+1,k-1}\le R\). Then

\[
E_{k+1}-2E_k+E_{k-1}
 =\sum_i v_i\mathcal L e_{i,k}+R_{k-1}+S_{k-1},
\quad S_{k-1}=\sum_i(v_i-v_{i-1})e_{i,k-1}.
\]

Here S_0=0, and (5) gives S_(k-1)<=delta*V for k>=2. Since E_0=V and
E_1=V-A, telescoping the second differences gives

\[
E_\ell=V-\ell A+\sum_{k=1}^{\ell-1}(\ell-k)
                (E_{k+1}-2E_k+E_{k-1}).
\]

Use E_ell>=0, R_(k-1)<=R and the preceding bounds on S. Consequently,

\[
\ell P\le V+\frac{\ell(\ell-3)}2R
 +\sum_{k=1}^{\ell-1}(\ell-k)\sum_i v_i\mathcal L e_{i,k}
 +\frac{(\ell-1)(\ell-2)}2\delta V.
\]

Pointwise g_i>=1{g_i=1}+2r(g_i), so R<=(G-P)/2. Its coefficient in the
last display is nonnegative because ell>=3. Substitution and division by
ell*(ell+1)/4 yield

\[
P\le a_\ell G+(b_\ell+K_\ell\delta)V+\sum_i v_i\mathcal L\phi_i.
                                                                  \tag{9}
\]

It remains to treat the moving weights correctly. At clock j only v_j
changes, by the nonnegative increment v_j(exp(lambda*d(g_j))-1). The
product rule for a jump generator gives exactly

\[
\mathcal L\Phi
 =\sum_i v_i\mathcal L\phi_i
  +\sum_i v_i(e^{\lambda d(g_i)}-1)\phi_i(T_i g)
 \ \ge\ \sum_i v_i\mathcal L\phi_i.                      \tag{10}
\]

The sign in (10) uses the **post-update** potential and its nonnegativity.
It is not a claim that phi_i itself increases. Combining (9) and (10)
proves (8). \(\square\)

For orientation, setting all weights to one before taking stationary
expectations recovers the useful finite bound
\(\Pr(g_0=1)\le a_\ell\theta+b_\ell\), including the universal
singleton bound 1/3 at ell=3. The crucial new step for (1) is the weighted,
nonstationary version (8).

## 4. Exponential height bound for the stationary current

Set

\[
\beta=e^\lambda+e^{-\lambda}-2,
\quad A_\theta=e^{\lambda(\theta-1)}-e^{-\lambda},
\quad
B_\ell=a_\ell\frac{e^{\lambda\theta}-1}{\lambda}
                   +b_\ell+K_\ell(1-e^{-\lambda\theta}).             \tag{11}
\]

A direct calculation gives

\[
\mathcal L V=(e^{\lambda(\theta-1)}-1)V
 +(1-e^{-\lambda})\sum_i v_i\mathbf1_{\{g_i=0\}}
 +(e^\lambda-1)P
 \ \le\ A_\theta V+\beta P.                              \tag{12}
\]

Use (4) and Lemma 2 in (12). If m_ell*beta<1, the function

\[
Y=V-\beta\Phi
\]

is positive and obeys

\[
(1-m_\ell\beta)V\le Y\le V,
\qquad
\mathcal L Y\le (A_\theta+\beta B_\ell)V
 \le \frac{A_\theta+\beta B_\ell}{1-m_\ell\beta}Y.          \tag{13}
\]

The coefficient is positive when theta>0. Dynkin's formula and Gronwall's
inequality imply

\[
\mathbb E Y(t)\le Y(0)
 \exp\left[t\frac{A_\theta+\beta B_\ell}{1-m_\ell\beta}\right].       \tag{14}
\]

There is no integrability gap in (14): N,H are fixed here, every gap is
at most H, and the total number of clocks on a bounded interval is Poisson.
The exponential moments of the lifted heights are therefore finite. One
may also stop at a fixed number of events and then pass to the limit.

Choose any deterministic lifted initial profile with h_0(0)=0. Since
exp(lambda*h_0(t))<=V(t)<=Y(t)/(1-m_ell*beta), Jensen's inequality gives

\[
\limsup_{t\to\infty}\frac{\mathbb E h_0(t)}t
 \le\frac{A_\theta+\beta B_\ell}{\lambda(1-m_\ell\beta)}.             \tag{15}
\]

Finite-chain stationarity and the Poisson compensator identify the left
side as

\[
F_{N,H}=\mathbb E_\pi d(g_0)=\theta-q_{N,H}.                         \tag{16}
\]

We have proved the following exact, explicitly evaluable bound:

\[
\boxed{\quad
q_{N,H}\ge \theta-
 \frac{A_\theta+\beta B_\ell}{\lambda(1-m_\ell\beta)},
\quad 3\le\ell\le N,\quad \lambda>0,\quad m_\ell\beta<1.
\quad}                                                           \tag{17}
\]

A negative right side is merely uninformative; the next section supplies
parameters giving a uniformly positive value.

## 5. Uniform choice of parameters and all constants

First suppose 0<theta<=1, N>=3 and H>=2. Choose

\[
\ell=\max\{3,\lceil2/\theta\rceil\},\qquad \lambda=\theta/96.
                                                                    \tag{18}
\]

Because 2/theta=2N/H<=N, this ell is at most N. Put
\(c_\ell=a_\ell\theta+b_\ell\). Then 0<=c_ell<=theta and

\[
\alpha=\frac{\theta(\theta-2)}2+c_\ell
 \le-\frac{\theta^2}6.                                    \tag{19}
\]

For ell=3 we have 2/3<=theta<=1, c_ell=1/3, and
\(\alpha+\theta^2/6=(2\theta-1)(\theta-1)/3\le0\).
For ell>=4, write x=ell*theta. Then
\(2\le x<2\ell/(\ell-1)\), and

\[
\frac{\alpha}{\theta^2}
 =\frac12-\frac{4\ell}{\ell+1}\frac{x-1}{x^2}
 \le\frac12-\frac{\ell-1}{\ell}
 \le-\frac14.
\]

The first inequality uses that (x-1)/x^2 decreases for x>=2. This proves
(19), including the rounding in (18).

For completeness, all small-lambda estimates needed below hold on
0<lambda<=1/10, 0<theta<=1:

\[
\begin{split}
A_\theta/\lambda
 &=\int_{1-\theta}^1 e^{-\lambda u}\,du
 \le \theta-\lambda\theta(2-\theta)/2+\theta\lambda^2/2,\\
\beta&\le\lambda^2(1+\lambda^2),\\
(e^{\lambda\theta}-1)/\lambda&\le\theta+\lambda\theta^2,\\
1-e^{-\lambda\theta}&\le\lambda\theta,\\
B_\ell&\le c_\ell+3\lambda\theta,\\
(1-m_\ell\beta)^{-1}&\le1+3\lambda^2.
\end{split}                                                       \tag{20}
\]

The first uses exp(-u)<=1-u+u^2/2 and u^2<=1 on the integration range.
The second follows from the even exponential series; the terms after
lambda^2 sum to at most lambda^4 for lambda<=1. The third follows from
exp(x)<=1+x+x^2 for 0<=x<=1. The fourth is elementary. The fifth uses
0<=a_ell<=1 and K_ell<2. For the last, m_ell<2 and
2(1+lambda^2)/(1-2lambda^2(1+lambda^2))<=3 when lambda<=1/10.
These inequalities also verify m_ell*beta<1.

Using c_ell<=theta in (20) gives

\[
\frac{A_\theta+\beta B_\ell}{\lambda}
 \le\theta+\alpha\lambda+4\theta\lambda^2.
\]

For example, the coefficient of theta*lambda^2 before rounding to 4 is
at most 7/2+lambda+3lambda^2<=4. Since alpha<0, multiplication by the
last bound in (20) yields

\[
\frac{A_\theta+\beta B_\ell}{\lambda(1-m_\ell\beta)}
 \le\theta+\alpha\lambda+8\theta\lambda^2
 \le\theta-\theta^2\lambda/6+8\theta\lambda^2.
\]

At lambda=theta/96, the right side is exactly at most
\(\theta-\theta^3/1152\). Equation (17) proves (1) for theta<=1.

For H>=N, use monotonicity in total mass. Both r and d are nondecreasing,
so the same clocks preserve coordinatewise order of gap configurations.
Time averaging an ordered finite coupling gives ordered stationary
marginals. Thus q_(N,H)>=q_(N,N)>=1/1152. This completes Theorem 1.
Passing to the already proved canonical limit proves (2). \(\square\)

## 6. What this says about condensates

Let H_N/N->eta>0. Every subsequential local canonical limit mu satisfies

\[
\mu(g_0\ge2)=Q(\eta)>0,\qquad
\mathbb E_\mu g_0\ge2Q(\eta)
 \ge\min\{\eta,1\}^3/576.                                \tag{21}
\]

The first equality uses only convergence of a bounded cylinder event.
The second is pointwise g_0>=2*1{g_0>=2}. In particular the local limit
cannot be the all-empty law, and the occupied fraction has a positive
uniform lower bound.

There is also a direct bound on the largest pile M_N=max_i g_i. Pointwise,
if K_N is the number of sites of mass at least two, then

\[
H_N-M_N\ge2(K_N-1).
\]

Taking expectations and using cyclic invariance,

\[
\limsup_N\mathbb E\frac{M_N}{H_N}
 \le1-\frac{2Q(\eta)}\eta
 \le1-\frac{\min\{\eta,1\}^3}{576\eta}<1.                \tag{22}
\]

Thus M_N/H_N cannot tend to one in probability: bounded convergence would
force its expectation to tend to one. This excludes **complete** stationary
condensation in that precise sense. It does not prove M_N/N->0, does not
bound every tail first moment, and does not exclude a mixture having a
vacuum component or a partially condensed component.

The earlier saturation envelope a_K=sup_H q_(K+1,H), whose decreasing
limit a_* was established in the marked-reservoir work, now satisfies
\(a_*\ge1/1152\). Hence its previously unresolved zero alternative is
excluded. This uses the earlier envelope theorem only for that corollary;
it is not needed for (1) or (2).

## 7. Further stationary-measure consequences

The companion [phase-selection proof](PHASE_SELECTION.md) uses (2), the
previous scalar limit, and the earlier stationary coupling classification
to establish a stronger critical-density alternative. There is an intrinsic
endpoint eta_c>1/217, possibly infinite. Canonical masses are uniformly
integrable at every finite eta<=eta_c, and no order-N pile occurs there.
Q is strictly increasing up to eta_c. If eta_c is finite, Q is permanently
constant above it and the whole local canonical law at and above eta_c
converges to the unique critical phase, with escaped mean eta-eta_c.

In particular, absence of an order-N pile is now unconditional on the
explicit interval 0<eta<=1/217. The proof does not decide whether eta_c is
finite, or select every below-critical local canonical law.

## 8. Audit and remaining problem

Run the new audit from the repository root:

```sh
python3 nasch/continuations/2026-10-24-positive-occupancy/verify.py
```

The audit independently implements the moves and local empty-block
observable. It checks (6), the weighted telescoping estimate, the exact
jump-product rule (10), the exponential-height drift, and the resulting
Lyapunov inequality using rational weights. It separately checks the
rounded parameter choice in (19) and evaluates (17) with rigorous rational
exponential enclosures at selected densities. These are deterministic
finite audits; no Monte Carlo evidence is used in the proof.

The structural reason the method succeeds is that the exponential weights
have small total downward variation, even when a gap is very large.
The local occupancy certificate therefore survives weighting, with a
controlled error. Its generator term is absorbed into a positive height
function. This supplies a stationary-current bound without first bounding
stationary mass tails.

Still open: an explicit general formula for Q, full local canonical measure
convergence, preservation of the entire first moment, exclusion of partial
condensation, the original T_N closed form, and interchange with the
finite-braking thermodynamic limit. The unrestricted NaSch problem has not
been solved by this theorem.
