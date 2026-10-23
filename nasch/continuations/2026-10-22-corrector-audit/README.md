# Monotone current correctors and an obstruction to folding rings

Continuation of the 22 October 2026 research run.

**The fixed-density limit remains unresolved.** This note proves an exact
finite-volume current characterization with an order bound, an exact extension
to real heights, a uniform martingale fluctuation bound, and a counterexample
family to a proposed proof mechanism.
The counterexamples concern a current certificate, **not** the stationary
dilation inequality or the thermodynamic limit. No general stationary traffic
formula or new solution of the first-passage problem is claimed.

These are AI-assisted, internally audited proofs, not independently peer-reviewed
results. Finite-chain Poisson equations and their minimax interpretation are
standard mathematics. The model-specific monotonicity, rounding identity, and
folding calculation are proved below; no claim of literature priority is made.

## 1. The exact comparison still needed

Use the reduced backchip process, not the unrestricted discrete-time NaSch
process. At rate one, site i retains

$$r(g_i)=\mathbf1_{\{g_i\ge2\}}$$

and sends $d(g_i)=g_i-r(g_i)$ to i-1. The ring has N sites and total mass H.
Let

$$q_{N,H}=\pi_{N,H}(g_0\ge2),\qquad F_{N,H}=H/N-q_{N,H}.$$

The preceding [continuation](../2026-10-22/README.md), Sections 4–6, proves
site-removal monotonicity of current and

$$0\le q_{N,H+a}-q_{N,H}\le\frac{2a}{3N}.$$

It also proves that a uniform bound

$$q_{kN,k(H-1)+1}\le q_{N,H}+C_R/N,\qquad k=2,3,\ H/N\le R \tag{1.1}$$

would imply convergence along **all** increasing road sizes, at every fixed
density. Its hypothesis remains unproved.

**Lemma 1 (remove the population correction at the cost of a constant).**
The existence of constants in (1.1) is equivalent to the existence of constants
in

$$q_{kN,kH}\le q_{N,H}+C'_R/N,\qquad k=2,3,\ H/N\le R.\tag{1.2}$$

**Proof.** Mass monotonicity makes (1.2) imply (1.1) with the same constant.
Conversely, the two target populations differ by k-1. The displayed Lipschitz
bound gives

$$0\le q_{kN,kH}-q_{kN,k(H-1)+1}
\le\frac{2(k-1)}{3kN}\le\frac{4}{9N}.$$

Thus (1.1) implies (1.2) with $C'_R=C_R+4/9$. ∎

In current variables (1.2) is simply

$$F_{kN,kH}\ge F_{N,H}-C'_R/N.$$

Exact zero-error versions are not equivalent. The one-particle example in the
previous report rules out the ordinary zero-error inequality.

## 2. A monotone corrector for every finite ring

Lift a mass configuration to ordered integer heights with

$$h_{i+1}-h_i=g_i,\qquad h_{i+N}=h_i+H.$$

A clock at i changes only coordinate i, using

$$B(a,b)=\min\{b,\max\{a+1,b-1\}\}.
\tag{2.1}$$

For integer $a\le b$, this is $b-\mathbf1_{\{b-a\ge2\}}$.
Write $T_i$ for this height update and

$$\mathcal L\Phi(h)=\sum_{i=0}^{N-1}[\Phi(T_i h)-\Phi(h)].$$

**Theorem 2 (monotone current corrector).** For every N≥2 and integer H≥1,
there exists a function $\Phi_{N,H}$ on the lifted integer heights such that

$$\mathcal L\Phi_{N,H}(h)=F_{N,H}\quad\hbox{for every }h,\tag{2.2}$$

$$h\le z\ \Longrightarrow\ \Phi_{N,H}(h)\le\Phi_{N,H}(z),\qquad
\Phi_{N,H}(h+c\mathbf1)=\Phi_{N,H}(h)+c.\tag{2.3}$$

In particular, for any two lifted states of the same mass,

$$\min_i(h_i-z_i)\le\Phi_{N,H}(h)-\Phi_{N,H}(z)
\le\max_i(h_i-z_i).\tag{2.4}$$

The constant in this order bound is one, independent of N and H.

**Proof.** The map B is coordinatewise monotone and commutes with common
vertical translations. Both properties therefore hold pathwise for every
composition of clock updates.

The word consisting of two firings at N-1, then two at N-2, and so on down
to two at 1 gathers all the mass at site zero. It does not change height
coordinate zero during the word. It sends any lifted state to

$$(h_0,h_0+H,\ldots,h_0+H).$$

The embedded clock identities are iid uniform on N sites. Disjoint blocks of
length $2(N-1)$ have a fixed positive probability of realizing this word.
Consequently two systems with the same mass, driven by the same clocks,
eventually have exactly the same gaps and thereafter differ by a constant
vertical shift. This also proves uniqueness of the finite canonical invariant
law: every state reaches the same corner. Full irreducibility is unnecessary.

Let a reference gap process start with law $\pi_{N,H}$ and reference height
$h^*_0(0)=0$. Its mean height increment is

$$E h^*_0(t)=tE_{\pi_{N,H}}d(g_0)=tF_{N,H}.$$

Couple an arbitrary initial height h to this reference using the same clocks.
The height difference is bounded between its initial coordinatewise minimum
and maximum. After the gathering word it is a constant C, which remains
unchanged. Thus bounded convergence gives

$$\Phi_{N,H}(h):=\lim_{t\to\infty}
       [E_h h_0(t)-tF_{N,H}]=EC.\tag{2.5}$$

The limit inherits monotonicity and vertical homogeneity. Sandwiching h between
$z+\min_i(h_i-z_i)\mathbf1$ and
$z+\max_i(h_i-z_i)\mathbf1$ proves (2.4).

The same clock word gives a uniform geometric tail for coupling, so the limit
in (2.5) is uniform over the finite gap state space. The Markov property yields

$$E_h\Phi_{N,H}(h(t))=\Phi_{N,H}(h)+tF_{N,H}.$$

Differentiating at t=0 gives (2.2). All update increments are bounded for fixed
H, so this differentiation is valid. ∎

For an explicit estimate, put $\ell=2(N-1)$ and $p_N=e^{-N}/\ell!$.
During a unit time interval, the probability of exactly the required sequence
of $\ell$ clock events and no others is $p_N$. For $h_0=0$, the coupling above
therefore proves

$$\left|E_hh_0(t)-tF_{N,H}-\Phi_{N,H}(h)\right|
\le2H(1-p_N)^{\lfloor t\rfloor}.\tag{2.6}$$

This estimate is finite-volume. Its dependence on N is much too poor to prove
the requested limit.

### Poisson equation and transport bound

Let $\bar h=N^{-1}\sum_i h_i$ and
$f(g)=N^{-1}\sum_i d(g_i)$. Since $\mathcal L\bar h=f(g)$, the function

$$\psi(g)=\Phi_{N,H}(h)-\bar h$$

is well-defined on gap configurations and satisfies

$$L\psi(g)=F_{N,H}-f(g).\tag{2.7}$$

It can be centered to have stationary mean zero. Rotation invariance follows
by uniqueness of this centered Poisson solution, since f and the generator are
rotation invariant. For completeness, uniqueness follows because a harmonic
function on a finite chain with a unique closed communicating class is
constant: it is constant on that class and equals its value there by hitting
the class from any transient state.

If $\delta_i=h'_i-h_i$, (2.4) gives the more useful transport estimate

$$\min_i\delta_i-\bar\delta
\le\psi(g')-\psi(g)
\le\max_i\delta_i-\bar\delta.\tag{2.8}$$

For example, if the lift changes by one on a proper cyclic interval of length
l and by zero elsewhere—one unit of mass is relocated between its endpoints—
the change in $\psi$ lies in $[-l/N,1-l/N]$.

When solving (2.7) numerically, replace an equation whose stationary weight is
**positive** by the centering equation. Replacing a transient-state equation
can make the system singular. The supplied solver explicitly enforces this
condition and checks every original equation afterward.

### Exact finite current certificates

Let $\mathcal M$ be the functions on lifted integer states satisfying (2.3).
For any such function U, the difference $U(h)-\bar h$ is a function on the
finite gap state space. Stationarity gives

$$E_{\pi_{N,H}}\mathcal LU=F_{N,H}.$$

Consequently

$$\inf_h\mathcal LU(h)\le F_{N,H}\le\sup_h\mathcal LU(h),\tag{2.9}$$

and Theorem 2 attains both sides:

$$F_{N,H}
=\sup_{U\in\mathcal M}\inf_h\mathcal LU(h)
=\inf_{U\in\mathcal M}\sup_h\mathcal LU(h).\tag{2.10}$$

This is an exact variational characterization, not a closed-form solution.
Its value here is that a proposed comparison can be tested through a generator
inequality without assuming a stationary distribution for the larger ring.

### A size-independent bound for corrected current fluctuations

There is a useful consequence beyond the variational formulation. Put

$$a_i(h)=\Phi(T_i h)-\Phi(h).$$

Each height update increases its updated coordinate. Monotonicity and (2.2)
therefore give, pointwise,

$$a_i\ge0,\qquad \sum_i a_i=F_{N,H},\qquad
\sum_i a_i^2\le F_{N,H}^2.\tag{2.11}$$

In particular, **every corrected jump is at most F**, even though an actual
mass transfer can be as large as H. The bound is independent of N at fixed
mass density because $F_{N,H}\le H/N$.

**Corollary 2.1 (Poisson bound for corrected current).** Write $F=F_{N,H}>0$.
For any initial state, the process

$$M_t=\Phi(h(t))-\Phi(h(0))-Ft$$

is a square-integrable martingale and satisfies

$$E M_t^2\le F^2t,\qquad
E\exp(\lambda M_t/F)\le
\exp\{t(e^\lambda-1-\lambda)\},\quad\lambda\in\mathbb R.\tag{2.12}$$

Let $J_0(t)=h_0(t)-h_0(0)$ be the actual transported mass across bond zero.
Put $A=H(N-1)/N$. Then pathwise

$$|J_0(t)-Ft-M_t|\le A.\tag{2.13}$$

This is the exact oscillation of the state correction $\Phi(h)-h_0$;
its worst-case linear growth in N cannot be removed from this corrector.

Consequently, for $t>0$ and $x\ge0$,

$$\Pr(J_0(t)-Ft\ge A+Fx)
\le \exp[-t\,\mathfrak h(x/t)],\qquad
\mathfrak h(u)=(1+u)\log(1+u)-u,\tag{2.14}$$

and for $0\le x\le t$,

$$\Pr(J_0(t)-Ft\le-A-Fx)
\le \exp[-t\,\mathfrak h(-x/t)],\tag{2.15}$$

with $\mathfrak h(-1)=1$. The lower event is impossible for $x>t$.

**Proof.** The compensated-jump martingale has predictable quadratic
variation $\int_0^t\sum_i a_i(h(s))^2ds\le F^2t$, proving the first claim.
For any real $\lambda$, the convex function
$v\mapsto e^{\lambda v}-1-\lambda v$ vanishes at zero, so on $[0,1]$ it is
at most $v(e^\lambda-1-\lambda)$. Apply this with $v=a_i/F$ and sum,
using $\sum_i a_i/F=1$. The exponential compensator, or its elementary
generator inequality followed by Gronwall's inequality, proves the moment
bound in (2.12). All jumps are bounded and the total clock rate is finite,
so the exponentials are integrable on every bounded time interval.

The function $\chi(g)=\Phi(h)-h_0$ is independent of the vertical lift.
Every lift normalized by $h_0=0$ lies between $(0,\ldots,0)$ and
$(0,H,\ldots,H)$ coordinatewise. These two extremal lifts have gap states
which are rotations of the same one-pile configuration. Rotation invariance
of $\psi=\Phi-\bar h$ therefore makes the difference of their $\Phi$ values
exactly $H(N-1)/N$. Monotonicity gives $\operatorname{osc}\chi=A$.
Subtracting the martingale identity from the identity defining $J_0$ gives
(2.13). Chernoff's inequality
with $\lambda=\log(1+x/t)$ gives (2.14); with
$\lambda=\log(1-x/t)$ it gives (2.15), including the endpoint by a limit.
Finally $\Phi(h(t))-\Phi(h(0))\ge0$, so $M_t/F\ge-t$. This and (2.13)
exclude the lower event for $x>t$. ∎

The fluctuation estimate concerns the corrected current. The sharp deterministic
offset A in (2.13) is still of order N at fixed density. Thus this result does
**not** validate exchanging the long-time and large-road limits. It separates
the controlled clock noise from the still-uncontrolled finite-size bias.

## 3. Exact rounding and real-height interpolation

Extend B to real $a\le b$ by (2.1), with integer total mass H still imposed on
the height period. This real-height extension is an auxiliary mathematical
process, not a modification of the physical mass model.

**Lemma 3 (common-threshold rounding).** For every real u,

$$\lfloor B(a,b)+u\rfloor
=B(\lfloor a+u\rfloor,\lfloor b+u\rfloor).\tag{3.1}$$

Thus componentwise rounding by the same u commutes with every clock update.

**Proof.** The floor function preserves minimum and maximum, and commutes with
addition of an integer. Apply these three facts to (2.1). Since H is integer,
the lifted boundary relation is also preserved. ∎

It follows that the monotone corrector has the extension

$$\widetilde\Phi(h)
=\int_0^1\Phi_{N,H}(\lfloor h+u\mathbf1\rfloor)\,du,\tag{3.2}$$

and this extension satisfies $\mathcal L\widetilde\Phi=F_{N,H}$ exactly.
Indeed, commute each update through the rounding and integrate (2.2).
It is monotone and homogeneous under arbitrary real vertical translations:
for the latter, the integrand minus u is periodic with period one.
Also $\int_0^1\lfloor x+u\rfloor du=x$, so the extension agrees with the
long-time expectation construction using the real-height dynamics.

For half-integer heights, (3.2) requires just two evaluations of the integer
corrector, each with weight 1/2. This made it possible to test fractional
offsets in the folding construction exactly, without floating-point arithmetic.

## 4. Folding can change retention by an extensive amount

First consider a $2N$-site ring with total mass $2H$. Fold its lifted heights
into two columns at each small-ring site:

$$x_{0,j}=h_j,\qquad x_{1,j}=h_{N+j}-H,\qquad 0\le j<N.$$

Sort these two numbers at each j, obtaining ordered rows $y^-_j\le y^+_j$.
Both rows are valid lifted N-site profiles of mass H. Internal monotonicity
survives sorting. At the seam, the original inequalities have the two rows
interchanged, and sorting again preserves the inequalities with increment H.

For every even N≥2, take H=N and set

$$h_j=j+\mathbf1_{\{j\text{ odd}\}},\qquad
h_{N+j}=N+j+\mathbf1_{\{j\text{ even}\}}.\tag{4.1}$$

The two seam gaps are one; the internal gaps alternate between zero and two.
There are exactly N-1 original piles of mass at least two. But sorting gives

$$y^-_j=j,\qquad y^+_j=j+1,$$

so every gap in either sorted row is one and their total pile count is zero.
The retention discrepancy is N-1, and the difference in average retention
approaches 1/2. It is not a boundary error of order $1/N$.

The sign is not universal: for N=H=2, the four-site state $(0,0,0,4)$ has one
pile, while its two sorted rows both have gaps $(0,2)$ and hence have two piles
in total.

These are deterministic configuration comparisons. Neither configuration
calculation compares stationary probabilities.

## 5. Even the exact harmonic correction does not rescue this fold

The more serious test uses the corrected population $2H-1$, as in (1.1).
Define

$$x_{0,j}=h_j,\qquad x_{1,j}=h_{N+j}-(H-1),$$

and sort to $y^-,y^+$. Both rows are again valid N-site profiles of mass H:
at the seam the two original upper bounds use increments H-1 and H, and
replacing the smaller increment by H makes the sorted inequalities valid.
Now use the **exact** small-ring current corrector and set

$$U(h)=\tfrac12[\Phi_{N,H}(y^-)+\Phi_{N,H}(y^+)].\tag{5.1}$$

This is a monotone, vertically homogeneous function on the larger ring, so
(2.9) applies to it.

**Theorem 4 (failure of the folded harmonic certificate).** For every odd
N≥3, put H=N. There is a state of the $2N$-site, $2N-1$-mass chain at which

$$\mathcal L_{2N,2N-1}U=\tfrac12 F_{N,N}.\tag{5.2}$$

Consequently no constant C independent of N can make this candidate satisfy

$$\mathcal L_{2N,2N-1}U(h)
\ge F_{N,N}-\frac1{2N}-\frac C N\quad\text{for every }h.\tag{5.3}$$

**Proof.** Index the large-ring gaps by $0,\ldots,2N-1$ and take

$$g_j=\begin{cases}
1,&j=N-1,\\
2,&j\text{ even and }j\ne N-1,\\
0,&j\text{ odd}.
\end{cases}\tag{5.4}$$

Their sum is $2N-1$. Set $h_0=0$ and recover the other heights by summation.
For $0\le j<N$ the folded columns are

$$x_{0,j}=j+\mathbf1_{\{j\text{ odd}\}},\qquad
x_{1,j}=j+\mathbf1_{\{j\text{ even}\}}.$$

Hence $y^-=(0,1,\ldots,N-1)$ and $y^+=y^-+\mathbf1$.
Only the N even-indexed large-ring clocks act nontrivially. Each moves one
unit, including the singleton at N-1. In its folded column it raises the
smaller entry by exactly one, to equality with the larger entry. As these
N clocks range over the even indices, they raise each coordinate of $y^-$
once and leave $y^+$ unchanged.

Every small-ring clock at the all-one-gap profile $y^-$ also raises its own
height coordinate by one. Therefore

$$\mathcal L_{2N,2N-1}U(h)
=\tfrac12\sum_{j=0}^{N-1}
  [\Phi_{N,N}(y^-+e_j)-\Phi_{N,N}(y^-)]
=\tfrac12F_{N,N},$$

which proves (5.2). If (5.3) held, this state would require

$$C\ge\frac N2F_{N,N}-\frac12.
\tag{5.5}$$

The earlier current bound gives $F_{N,N}\ge N/(2N-1)>1/2$, so the right side
is greater than $N/4-1/2$ and is unbounded. ∎

This obstruction applies to the specified **pointwise lower-drift certificate**.
It does not rule out averaging its defect under the unknown large-ring
stationary law, another choice of potential, or a different coupling. In
particular, it does not disprove (1.1).

## 6. What was tested beyond the theorem

The scripts also test half-integer folding offsets using (3.2), and cyclic
minimum, maximum, and average envelopes of the folded potential. These are
attempts to improve the certificate, not proposed stationary laws.

No tested variant supplied a proved error bound uniform in N. For example,
at small-ring N=H=5, the minimum drift of the cyclic-mean candidate over all
48,620 large-ring states is $280597085/621456291$, whereas
$F_{5,5}=1086961580/1450064679$. This candidate needs at least
$C=8616857413/8700388074$ in (5.3) at that size. A single finite value neither
proves nor disproves that some larger uniform C exists for this variant.

The direct current route therefore remains an unfinished proof attempt.
Constructing a different potential with the necessary uniform generator
bound, or controlling the stationary average of its defect, would be a
substantive advance. The existing phase-ordering results alone do not supply
that estimate; mass escape and phase mixtures remain unexcluded.

## 7. Audit and reproducibility

From the repository root, with Python 3 and the standard library:

```sh
python3 nasch/continuations/2026-10-22-corrector-audit/verify.py
python3 nasch/continuations/2026-10-22-corrector-audit/corrector_probe.py 1
python3 nasch/continuations/2026-10-22-corrector-audit/stagger_probe.py
python3 nasch/continuations/2026-10-22-corrector-audit/envelope_probe.py
```

The verifier checks the full and rotation-quotient Poisson solvers against
one another, every generator equation in the selected finite systems, the
order bound for every pair of their states, rounding, real-height gathering,
real-height current equations, and the two counterexample families. See
`results/verified.json` for exact counts and rational values.

The proofs establish finite-volume statements and failure of one proposed
method. **They do not establish the target thermodynamic limit.**
