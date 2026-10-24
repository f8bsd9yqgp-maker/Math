# A uniform comparison for capped transfers

23–24 October 2026. AI-assisted working mathematics, internally audited and not
independently peer-reviewed. No claim of publication priority is made.

**The fixed-density thermodynamic-limit problem remains open.** This note
proves a comparison uniform in the ring size. It permits finitely many
interfaces to have bounded transfers at an arbitrarily small cost in
stationary current. The proof does not require a mass-tail estimate, absence
of condensates, or mixing uniform in the ring size.

## 1. Statement

Let $N\ge2$, $H\ge1$, and

$$d(m)=m-\mathbf1_{\{m\ge2\}}.$$

In the original ring, independent rate-one clocks at sites $i$ send $d(g_i)$
units to $i-1$ modulo $N$. Its unique invariant law is $\pi_{N,H}$ and its
current across each bond is

$$F=F_{N,H}=H/N-q_{N,H}>0,\qquad
q_{N,H}=\pi_{N,H}(g_0\ge2).$$

Choose a set $S$ of sites and integers $C_i\ge1$ for $i\in S$. The **capped
ring** replaces the transfer at such a site by $\min\{d(g_i),C_i\}$.
All clocks retain rate one. Let its unique invariant law be $\pi^{\rm cap}$
and its common stationary bond current be $J$.

For an integer $x\ge0$, put

$$e_C(x)=\left(\left\lceil x/C\right\rceil-1\right)^+,
\quad
R=\sum_{i\in S}\mathbb E_{\pi_{N,H}}e_{C_i}(d(g_i)),
\quad A=\sum_{i\in S}C_i^{-1}.$$

**Theorem 1 (capping comparison).**

$$\boxed{\frac{F}{1+R}\le J\le F,\qquad
0\le\frac1J-\frac1F\le\frac RF\le A.}                 \tag{1.1}$$

Consequently,

$$0\le F-J\le\frac{F^2 A}{1+FA}.                        \tag{1.2}$$

The sharper quantity in (1.1) is a sampled tail sum under the **original**
stationary law:

$$R=\sum_{i\in S}\sum_{k\ge1}
      \pi_{N,H}(g_i\ge k C_i+2).                        \tag{1.3}$$

For one capped bond, the reciprocal current increases by at most $1/C$.
For $k$ capped bonds with a common cap $C$ and $H/N\le\rho_0$,

$$0\le F-J\le\frac{k\rho_0^2}{C+k\rho_0}
                  \le\frac{k\rho_0^2}{C}.              \tag{1.4}$$

Neither $N$ nor a stationary second moment occurs in this bound.

## 2. Uniqueness and height order

Every occupied donor sends at least one particle at a firing in either
chain. Suppress all clocks except $N-1$, and fire it $H$ times; then do the
same at $N-2$, down through site $1$. This finite clock word gathers every
initial configuration at site zero. Every word has positive probability.
Thus each finite chain has exactly one closed communicating class and a
unique invariant law; full irreducibility is unnecessary.

Stationary mass balance equates neighboring bond currents. Their common
value is positive: every nonempty configuration has at least one positive
transfer, so the sum of its mean instantaneous bond currents is at least one.

Lift a configuration to integer heights

$$h_{i+1}-h_i=g_i,\qquad h_{i+N}=h_i+H.$$

A full firing at $i$ replaces $h_i$ by

$$B(h_i,h_{i+1}),\qquad
B(a,b)=\min\{b,\max(a+1,b-1)\}.$$

The capped firing instead uses

$$B_C(a,b)=\min\{a+C,B(a,b)\}.                            \tag{2.1}$$

Both maps are nondecreasing in both arguments and are translation
homogeneous. If a slower protocol, at a clock ring, raises its height
coordinate by an amount between zero and its full capped increment, it is
dominated by the ordinary capped chain started from the same physical
configuration and driven by the same clocks. Induction over clock rings
proves this: at the updated coordinate its new height is at most its own
full capped image, which is at most the full capped image of the larger
heights. All other coordinates retain their order.

Applying the same argument to full and capped maps proves $J\le F$.
Height growth is integrated bond transfer; finite-state ergodic averaging
identifies its asymptotic speed with the stationary current. Initial height
offsets are bounded and do not change this speed.

## 3. Subdivide an oversized transfer

We construct a finite auxiliary protocol using the same physical rate-one
clocks as the capped ring. Its states have an active or a paused label.

At an active state $g$, a clock at an uncapped site performs the usual full
transfer. At a capped site $i$, write $x=d(g_i)$.

* If $x\le C_i$, perform the full transfer and stay active.
* If $x>C_i$, perform the first chunk $C_i$. Pause all updates except the
  clock at $i$. At its subsequent rings send further chunks of size $C_i$,
  followed by the remaining smaller chunk if necessary. After all $x$
  particles have been sent, return to active mode.

In a paused state remember the original active state $g$, the donor $i$,
and the number $\ell$ of chunks already sent. This makes different
intermediate paths distinct even when their physical configurations agree.
There are only finitely many such labels.

All chunks are legal partial capped moves. Indeed an oversized transfer
starts with $g_i\ge3$ and has $x=g_i-1$. After $s<x$ particles have been
sent, its physical donor contains $1+(x-s)$ particles. Its full available
transfer is exactly $x-s$. Thus the next prescribed chunk is
$\min\{C_i,x-s\}$. No other update occurs during the pause, so no arrival
can invalidate this calculation. At completion the physical configuration
is exactly the destination of the single original transfer.

The auxiliary protocol therefore satisfies the domination in Section 2.
The number of added waiting stages at an original event is exactly
$e_{C_i}(x)$.

## 4. An explicit stationary distribution for the auxiliary protocol

Let $p(g)=\pi_{N,H}(g)$ and $Z=1+R$. Assign weight

$$\lambda(g,\mathrm{active})=p(g)/Z.                     \tag{4.1}$$

For each capped oversized transition starting at $g$ and donor $i$, assign
every one of its $e_{C_i}(d(g_i))$ intermediate labels the same weight
$p(g)/Z$. These weights are nonnegative and sum to

$$Z^{-1}\left[\sum_g p(g)+
 \sum_g p(g)\sum_{i\in S}e_{C_i}(d(g_i))\right]=1.$$

Here is a direct check of all balance equations, including transient states
of zero stationary weight. At every intermediate label, one rate-one edge
enters and one rate-one edge leaves; both carry probability flow $p(g)/Z$.
At an active state, an original rate-one transition has either been left
unchanged or replaced by a finite directed path with exactly the same flow
at its first and last edges. Consequently its balance equation is the
original stationary balance equation divided by $Z$. Null clock events
cancel on both sides. Thus (4.1) is an invariant law, without appealing to
an informal deletion of random time intervals.

Consider a physical bond $i$. The chunks replacing any original transition
at that bond sum to its original amount $d(g_i)$, and every edge of their
path has stationary flow $p(g)/Z$. Therefore the auxiliary stationary
current at every bond is exactly

$$J_{\rm aux}=Z^{-1}\sum_g p(g)d(g_i)=F/(1+R).           \tag{4.2}$$

For completeness the auxiliary chain also has one closed class: subdivision
of directed edges does not alter reachability between active states, and
every intermediate state reaches its destination active state. The unique
closed class of the original chain therefore yields the unique closed class
of the auxiliary chain. Its long-run current is (4.2).

The height coupling gives $J\ge J_{\rm aux}$. Finally

$$e_C(x)\le x/C,\qquad
\mathbb E_{\pi_{N,H}}d(g_i)=F,$$

so $R\le FA$. This proves (1.1) and (1.2). The identity
$e_C(x)=\sum_{k\ge1}\mathbf1_{\{x>kC\}}$ gives (1.3), since
$d(g_i)>kC$ is equivalent to $g_i\ge kC+2$ for $kC\ge1$.
The function $f\mapsto f^2A/(1+fA)$ is increasing for $f\ge0$;
using $F\le\rho_0$ gives (1.4). $\square$

## 5. The averaged pile probability is also approximated uniformly

The capped stationary law is generally not rotation invariant. Define its
**site-averaged** pile probability and overflow by

$$\bar q^{\rm cap}=\frac1N\sum_{i=0}^{N-1}
       \pi^{\rm cap}(g_i\ge2),\qquad
O=\frac1N\sum_{i\in S}\mathbb E_{\pi^{\rm cap}}
                   (d(g_i)-C_i)^+.$$

Current conservation gives the exact identity

$$J=H/N-\bar q^{\rm cap}-O.                             \tag{5.1}$$

The overflow term must not be omitted: in the capped chain the current is
not in general $H/N-\bar q^{\rm cap}$.

**Theorem 2.** Put $D_H=\max(1,H-1)$ and
$B_H=\sum_{i\in S}(D_H/C_i-1)^+$. Then

$$-\frac{J B_H}{N}\le\bar q^{\rm cap}-q_{N,H}
       \le\frac{F^2A}{1+FA},                            \tag{5.2}$$

and in particular, with $\eta=H/N$,

$$\boxed{|\bar q^{\rm cap}-q_{N,H}|\le\eta^2 A.}        \tag{5.3}$$

**Proof.** For $0\le x\le D_H$,

$$(x-C)^+\le (D_H/C-1)^+\min\{x,C\}.$$

At a capped bond, the stationary expectation of the minimum is $J$.
Hence $0\le O\le J B_H/N$. Subtracting the original identity
$F=\eta-q_{N,H}$ from (5.1) gives

$$\bar q^{\rm cap}-q_{N,H}=F-J-O.$$

Use $0\le F-J\le F^2A/(1+FA)$ for (5.2). Its positive endpoint is at
most $\eta^2 A$. Its negative endpoint has magnitude at most
$JD_H A/N\le\eta^2 A$, since $D_H\le H$ and $J\le F\le\eta$.
This proves (5.3). $\square$

A related estimate controls how much mass can reside at the capped sites:

$$\frac1N\sum_{i\in S}\mathbb E_{\pi^{\rm cap}}g_i
 \le \frac{|S|}{N}+rac JN
              \sum_{i\in S}\max\{1,D_H/C_i\}.           \tag{5.4}$$

To check it, use $g\le1+d(g)$ and
$x\le\max\{1,D_H/C\}\min\{x,C\}$, then sum. In particular if
$H/N$ is bounded, $|S|/N\to0$, and $A\to0$, their expected total mass
divided by $N$ vanishes. At fixed positive density this is also a vanishing
fraction of total mass. This says nothing comparable
about uncapped sites and does not exclude moving condensates elsewhere.

## 6. What would close the problem after this reduction

The theorem gives a precise alternative sufficient target. On each
$N$-site ring, cap **one fixed bond** at an integer $C$ and let $J_N^{(C)}$
be its stationary current at $H=\lfloor\eta N\rfloor$.

**Corollary 3 (fixed-cap reduction).** If, for every positive integer $C$
in any unbounded sequence, $J_N^{(C)}$ converges as $N\to\infty$, then the
original $q_{N,\lfloor\eta N\rfloor}$ converges. It suffices instead to
prove convergence of $\bar q_N^{(C)}$ for those caps.

**Proof.** Uniformly in $N$,

$$|F_{N,\lfloor\eta N\rfloor}-J_N^{(C)}|\le\eta^2/C,
\qquad
|q_{N,\lfloor\eta N\rfloor}-\bar q_N^{(C)}|\le\eta^2/C.$$

If the capped sequence converges, the limsup minus liminf of the original
sequence is at most $2\eta^2/C$. Send $C\to\infty$ along the stated
sequence. Finally $q_{N,H}=H/N-F_{N,H}$ and $H/N\to\eta$.
$\square$

**The premise of Corollary 3 has not been proved.** Bounded outgoing batches
at one bond do not by themselves supply spatial mixing, a product law,
or a stationary block-gluing comparison. The theorem also allows caps
$C=N^\alpha$ at a fixed number of interfaces, with a summable
$O(N^{-\alpha})$ error along geometric size sequences. The missing joining
estimate is still missing after imposing those caps.

The estimate scales with the number of capped bonds. Capping all $N$ bonds
with a fixed $C$ gives $A=N/C$, which does not control the thermodynamic
limit. Replacing this sum by a maximum has not been justified. The paused
protocol deliberately suppresses all other clocks during a split transfer;
parallel clearing would require a different proof.

## 7. Exact audit and scope

Run, using Python's standard library:

```sh
python3 nasch/continuations/2026-10-23-capped-bonds/verify.py
```

The verifier computes 85 full labelled capped chains with rational arithmetic,
checks all 1,180 capped stationary balance equations, and checks 1,348
stationary balance equations for the explicitly subdivided protocols.
It also checks 168 intermediate chunks and 10,392 local map/tail identities.
The full stationary weights are retained in `results/certificates.json`;
one extended protocol is recorded in `results/protocol_certificate.json`.
Finite checks are an independent audit of the algebra and construction,
not an extrapolation proving an infinite-system claim.

The statements are for the reduced continuous-time backchip process.
No formula for the original first-passage quantity $T_N$, no interchange of
rare-braking and thermodynamic limits, and no unrestricted NaSch stationary
traffic formula is established here. The older spacing inequality, ordering
theorems, and corrector identities are not being claimed as new results.
