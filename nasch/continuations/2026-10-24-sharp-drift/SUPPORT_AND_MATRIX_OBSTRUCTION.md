# Exact recurrent support and a finite-matrix obstruction

24 October 2026. AI-assisted working proofs, internally audited but not
independently peer-reviewed. These theorems concern the continuous-time
backchip process defined in the main note. They do not prove a thermodynamic
limit or exclude infinite-dimensional stationary representations.

The earlier infinite-line work ruled out fixed finite-dimensional cylinder
representations of a non-vacuum stationary law using factorial pile-run
bounds. The present result is different: it determines finite-ring support
constructively and gives an obstruction directly for canonical trace
representations, including a quantitative dimension bound for a specified
local cancellation ansatz. The earlier infinite-line result is not claimed
as new here.

## 1. Complete recurrent support

**Theorem A.** For $N\ge2$ and $H\ge0$, the unique closed recurrent class is

$$\mathcal C_{N,H}=\{g\in\mathbb N_0^N:\ \sum_i g_i=H,
                                      \ \min_i g_i\le1\}. \tag{1}$$

The stationary law is strictly positive at every state in this set and zero
elsewhere. In particular the entire composition chain is irreducible when
$H<2N$. Its recurrent-state count is

$$\binom{H+N-1}{N-1}-\mathbf1_{\{H\ge2N\}}
                              \binom{H-N-1}{N-1}.         \tag{2}$$

**Proof.** Every nontrivial forward update leaves its donor at zero or one.
Thus no transition enters the complement of (1), and every state in that
complement leaves it at its first clock event. The set (1) is closed.
The zero-mass case is immediate. Descending double forward firings gather
all positive mass at a specified site, so every state reaches a single pile.
It remains to prove that every state of (1) is reachable from a single pile.

We construct a path backwards in the directed transition graph. Write
$(a,b)$ for masses at adjacent sites $(j-1,j)$. The following moves are
valid reverse edges:

$$
(a,0)\longmapsto(a-1,1)\quad(a\ge1),\qquad
(a,1)\longmapsto(a-k,1+k)\quad(1\le k\le a).             \tag{3}
$$

In each case, applying the original clock $j$ to the new pair returns
the old pair. In particular an adjacent positive mass can be swapped
clockwise into a zero:

$$ (m,0)\longmapsto(0,m),                                \tag{4}$$

using one reverse edge if $m=1$, and two if $m\ge2$ (first take one unit,
then take the remaining $m-1$ units). A singleton can absorb its entire
left neighbor in one reverse edge:

$$ (m,1)\longmapsto(0,m+1).                              \tag{5}$$

If the initial state has no zero, it has a singleton by (1); (5) creates
a zero. Designate any positive mass as the head, of mass $A$.
We maintain at least one zero and repeatedly increase the head mass by one
until it contains all $H$ units.

If another positive mass exists, move the head clockwise through any zeros
using (4), until its next neighbor has mass $B>0$. If $B=1$, use (5) to
merge it into the head, now located one site clockwise and of mass $A+1$.

Suppose $B\ge2$. We can place a zero immediately to the right of this
adjacent pair without changing either member of the pair: choose any zero
in their complementary cyclic arc and move that zero counterclockwise by
successive swaps (4). Stop at the site just to the right of $B$. Swapping
two zeros simply means choosing the other zero as the tracked one; it
requires no event. The path never crosses the adjacent head and neighbor.
This gives three distinct adjacent sites $(A,B,0)$; if $N=2$, the situation
of two positive masses and a zero cannot arise.

Use (3) at the third site, first taking one unit and then, if $B>2$,
taking $B-2$ further units. The triple becomes $(A,1,B-1)$. Now apply
(5) to the first two sites, obtaining

$$ (A,B,0)\longmapsto(0,A+1,B-1).                        \tag{6}$$

The new head and remaining neighbor are still adjacent; a zero remains.
Thus every iteration increases the designated head mass exactly by one.
After finitely many iterations all mass is at one site. This constructs
a reverse path from the desired configuration to a single pile; reversing
its edges is a legal forward path from that pile to the configuration.

All single-pile positions communicate: two forward firings of its donor
move the whole pile one site counterclockwise. Combined with ordinary
forward gathering, the preceding reverse construction proves that (1) is
one communicating closed class. Finite irreducibility on that class gives
strict positivity of its stationary weights. Finally, counting all weak
compositions and subtracting those with every coordinate at least two
gives (2). $\square$

This closes the finite reduced-chain irreducibility subproblem in the
original rare-braking handoff. It does not supply the other conditions for
an interchange of rare-braking and road-size limits.

## 2. An algebraic lemma

**Lemma.** If a complex $D\times D$ matrix $A$ satisfies
$\operatorname{tr}(A^k)=0$ for all integers $k\ge2$, then $A$ is nilpotent
and $A^D=0$.

**Proof.** Suppose its distinct nonzero eigenvalues are
$\lambda_1,\ldots,\lambda_s$, with algebraic multiplicities $m_j\ge1$.
The trace identities for $k=2,\ldots,s+1$ say

$$\sum_{j=1}^s(m_j\lambda_j^2)\lambda_j^{k-2}=0.$$

The Vandermonde matrix is invertible, so every $m_j\lambda_j^2=0$, a
contradiction. All eigenvalues vanish. Cayley--Hamilton gives $A^D=0$.
$\square$

## 3. No common finite-dimensional trace formula for all canonical systems

**Theorem B.** There is no finite $D$ and single collection of complex
$D\times D$ matrices $(A_m)_{m\ge0}$ giving all canonical stationary laws,
for every $N\ge2,H\ge0$, by

$$\pi_{N,H}(g)=Z_{N,H}^{-1}
              \operatorname{tr}(A_{g_0}\cdots A_{g_{N-1}}), \tag{7}$$

with nonzero normalizers $Z_{N,H}$. This assertion permits signed or complex
matrix entries; it is not restricted to nonnegative matrices.

**Proof.** At $H=2N$, the all-two configuration is outside the recurrent
support. Therefore $\operatorname{tr}(A_2^N)=0$ for every $N\ge2$.
The lemma implies $A_2^D=0$. But at $N=D+1,H=2D$, the configuration
with $D$ consecutive twos and one zero is in the recurrent class, so
Theorem A makes its stationary probability strictly positive. Formula
(7) would assign it $Z_{D+1,2D}^{-1}\operatorname{tr}(A_2^D A_0)=0$,
a contradiction. $\square$

The universality over all $H$ is part of the hypothesis. This proof alone
does not exclude an arbitrary trace formula designed only for $H<2N$,
or matrices changing with $N,H$. The next result treats a standard
local-cancellation construction even in that restricted density range.

## 4. Linear dimension requirement for the local cancellation ansatz

For clarity, we specify the ansatz rather than claiming to exclude every
matrix-product method. A sufficient local stationary cancellation relation
for (7) is

$$
K_{a,b}=A_a\widehat A_b-\widehat A_a A_b,                 \tag{8}
$$

where the local incoming-minus-outgoing expression is

$$
K_{a,b}=
\mathbf1_{\{b=0,a\ge1\}}A_{a-1}A_1
+\mathbf1_{\{b=1\}}\sum_{k=1}^a A_{a-k}A_{k+1}
-\mathbf1_{\{b\ge1\}}A_a A_b.                           \tag{9}
$$

Indeed a clock's outgoing rate is one for a positive donor. Its resulting
donor is either zero (coming from one unit) or one (coming from $k+1\ge2$
units), giving exactly the two incoming terms. In a cyclic trace the
terms in (8) cancel after summing over bonds, proving stationarity if
normalization and nonnegative weights are also established.

**Theorem C.** Fix $N,H$ with $4\le H<2N$. Suppose complex $D\times D$
matrices represent the canonical stationary weights by (7) and satisfy
(8)--(9), at least for the pair $(a,b)=(2,2)$. Then

$$\boxed{D\ge\lfloor H/2\rfloor+1.}                    \tag{10}$$

The matrices and auxiliary matrices may depend on $N,H$ in this theorem.

**Proof.** The $(2,2)$ equation is

$$-A_2^2=A_2\widehat A_2-\widehat A_2 A_2.$$

Multiply by $A_2^k$ and take the trace. Cyclicity gives
$\operatorname{tr}(A_2^{k+2})=0$ for every $k\ge0$.
The lemma again gives $A_2^D=0$.
Put $R=\lfloor H/2\rfloor$. Since $H<2N$, $R\le N-1$.
There is a recurrent configuration consisting of $R$ consecutive twos,
then one unit if $H$ is odd, and zeros in the remaining positions.
(For odd $H=2N-1$, its only non-two coordinate is that one.)
It has strictly positive stationary probability by Theorem A. If $D\le R$,
its matrix product contains $A_2^R=0$, so (7) assigns probability zero.
This contradiction proves (10). $\square$

At fixed $0<\eta<2$, the usual local cancellation construction thus needs
dimension growing at least linearly in $N$ for $H=\lfloor\eta N\rfloor$.
This does not rule out an infinite-dimensional algebra, a nonstandard
cancellation identity, non-trace constructions, or a different recurrence.
It is an obstruction to a specified exact-formula route, not an obstruction
to existence of the thermodynamic limit.

## 5. A rank-one empty-site matrix also fails

**Theorem D.** Even at the single system $(N,H)=(6,6)$, there is no
stationary trace representation (7) with $A_0$ of rank one. This also
excludes infinite-dimensional rank-one constructions for which the
displayed products and traces are well defined and obey the usual
rank-one trace identities.

**Proof.** If $A_0=u v$, where $u$ is a column and $v$ a row, then

$$\operatorname{tr}(A_2 A_0 A_1 A_0 A_3 A_0)
=(vA_2u)(vA_1u)(vA_3u)
=\operatorname{tr}(A_2 A_0 A_3 A_0 A_1 A_0).              \tag{11}$$

It would follow that the stationary probabilities of $a=(2,0,1,0,3,0)$
and $b=(2,0,3,0,1,0)$ are equal. Exact balance for the full 462-state chain
instead gives, with $D_0=49823178685960907060573907009905368591$,

$$
\pi(a)=\frac{67144873485729264308973386199592099}{D_0},
\qquad
\pi(b)=\frac{59114762006505684538188885516224093}{D_0}.
$$

Their difference is $8030111479223579770784500683368006/D_0>0$.
The [full rational certificate](results/zero_matrix_certificate.json)
lists every composition and stationary weight. The verifier regenerates
the generator, solves it with rational arithmetic, and checks all 462
balance equations, normalization, and nonnegativity. Theorem A gives
uniqueness, so these exact weights prove the contradiction. $\square$

More generally this disproves a stationary weight that factors into
independent scalar weights of the positive blocks separated by zeros:
the two configurations have the same three blocks in a different order.
Neither a higher-rank empty-site matrix nor every infinite-dimensional
construction is excluded.

## 6. Exact audit

```sh
python3 nasch/continuations/2026-10-24-sharp-drift/support_verify.py
```

The standard-library script constructs 31,733 reverse-gathering paths,
checks all 552,001 reverse edges using the original forward update, and
then reverses each complete word to recover the target state. Independently,
forward breadth-first searches of 45 finite chains, covering 4,995 full
compositions, recover exactly the claimed support. These checks audit the
constructive algorithm. The all-size proof and the matrix obstructions
are the analytic arguments above.
The same script checks all 462 rational balances for Theorem D and
writes its complete stationary certificate.

- [Audit code](support_verify.py)
- [Recorded result](results/support_verified.json)
- [Main drift theorem](README.md)
