# Closure attempts and an obstruction to a pressure argument

24 October 2026. This records the mathematical limits of the continuation.
The fixed-density canonical limit has not been proved or disproved.

## A. What the capping theorem removes

The main theorem permits transfer caps at finitely many chosen interfaces
with an error uniform in ring size. For one cap at $C$,

$$0\le F_{N,H}-J_{N,H}^{(C)}\le (H/N)^2/C.$$

It also controls the site-averaged pile probability of that modified chain.
Consequently either of the following would suffice:

1. Prove all-size convergence of the current, or averaged pile probability,
   with one fixed capped bond, for an unbounded sequence of caps $C$.
2. Prove a sufficiently accurate gluing comparison after capping the finitely
   many block boundaries. For example, errors bounded by constants times
   $C/N+1/C$ would give a summable $O(N^{-1/2})$ error by $C\asymp\sqrt N$.

These are conditional targets, not conclusions. The first keeps a finite
batch size at an interface; the second keeps finite-size comparison as the
objective. Neither currently supplies an explicit stationary law.

In particular, this calculation did **not** establish the speculative bound

$$J_{kN,kH}^{(C,\,k\text{ boundaries})}
 \ge J_{N,H}^{(C,\,1\text{ boundary})}-K_{\rho_0,k}C/N,
 \qquad k=2,3,\ H/N\le\rho_0.$$

If it held with the stated uniformity, the capping comparison, mass-response
bound, and the previously proved two-prime criterion would close the target.
The cap changes outgoing batch sizes; it does not bound all site masses,
remove long temporal correlations, or produce independent boundary inputs.

## B. Why the previous buffer proof is still incomplete

The previous continuation uses independent core rings, conserved buffer
particles, and a current corrector. Its loss bound depends on a corrector
oscillation of order $H$. Imposing a cap at the core boundary does not by
itself turn that oscillation into $O(C)$. The capped current can be
approximated, but this is different from controlling the stationary coupling
of two cores through a sublinear buffer.

Trying to run the chunk-clearing protocols in parallel also needs care.
The proved auxiliary chain suppresses every other update while it completes
one oversized transfer. This is why its stationary weights can be computed
by subdividing generator edges. Parallel clearing changes the active-state
trace and can introduce arrivals into a partially cleared donor. The proof
does not justify dropping the sum over capped interfaces from the error.

For a fixed cap at every site, the available bound is proportional to $N/C$.
That does not give a uniform approximation of the original system by a
bounded-transfer process throughout the road.

## C. A proved flat negative branch of the pile-occupation pressure

A different route would try to recover the pile probability by differentiating
a limiting dynamical pressure. There is an exact obstruction to using only
its negative-bias branch.

Write $Q(g)=\sum_{i=0}^{N-1}\mathbf1_{\{g_i\ge2\}}$. For $H\ge2$ define

$$\Lambda_{N,H}(s)=\lim_{t\to\infty}\frac1t\log
 \mathbb E_{\pi_{N,H}}\exp\left(s\int_0^tQ(g(u))\,du\right).$$

The limit exists: on the unique finite irreducible recurrent class it is the
principal eigenvalue of the Feynman–Kac matrix $L+s\operatorname{diag}(Q)$.
This follows directly by exponentiating that finite matrix and applying
Perron–Frobenius to its positive semigroup. The stationary law has positive
weight on every state in the recurrent class.

**Proposition.** For every $N\ge2$, $H\ge2$, and $s\le0$,

$$s-1\le\Lambda_{N,H}(s)\le0.                            \tag{C.1}$$

In particular, for every sequence $H_N\ge2$,

$$\lim_{N\to\infty}\frac1N\Lambda_{N,H_N}(s)=0
\quad\text{for each fixed }s\le0.                       \tag{C.2}$$

**Proof.** For $s\le0$ the integrand in the expectation is at most one,
which proves the upper bound. A configuration with all $H$ particles at
one site is in the recurrent class: all states can reach that configuration,
and the finite chain has a closed class. Its stationary probability $p_*$
is therefore positive. Starting there, suppress the occupied site's clock
up to time $t$. This event has probability $e^{-t}$; every other clock is a
null update. On the event the configuration stays fixed and $Q=1$. Hence

$$\mathbb E_\pi\exp\left(s\int_0^t Q(g(u))\,du\right)
       \ge p_*e^{(s-1)t}.$$

Take $t^{-1}\log$ and then $t\to\infty$ to obtain the lower bound.
Dividing (C.1) by $N$ gives (C.2). $\square$

At every fixed $N,H$, differentiating the simple principal eigenvalue at
zero gives

$$\frac1N\Lambda'_{N,H}(0)=q_{N,H}.$$

Nevertheless (C.2) is the same function for all densities. Exchanging the
thermodynamic limit and this derivative is an additional statement that has
not been proved. This note does not assert a proven failure of derivative
convergence: a positive limiting $q$ is itself not yet established. The
proposition establishes the flat branch and identifies why pressure
convergence on the negative half-line alone does not justify that exchange.
The single-pile trajectories used in the lower bound are rare trajectories,
not a construction of a typical canonical condensate.

## D. Stationary covariance exploration

The archived exploratory script checks exact stationary covariances of
threshold indicators in eight small rings. It found no positive covariance
in the tested cases. Earlier work had already tested off-diagonal mass
moments in several small systems. These observations are not a proof of
negative association or even a general pairwise covariance inequality.

If a uniform negative covariance bound for the pile indicators were proved,
it would help exclude mixtures of different local pile probabilities. It
would not by itself give uniform integrability of the unbounded masses or
identify the surviving density after possible mass loss. Neither inference
was used in the capping proof.

Other attempts considered the exact FIFO departure recurrence, monotone
height games, queue-output fixed points, and ordinary pair-moment balance.
No new closed stationary recursion or valid general homogenization theorem
was obtained from those attempts. In particular, a queue's independent
potential service clock does not make its incoming batch marks independent.

## E. Literature scope

The direct predecessor for the backchip family remains Whitehouse, Costa,
Blythe and Evans, *Maintenance of order in a moving strong condensate*,
[arXiv:1407.1668v3](https://arxiv.org/html/1407.1668v3). Its numerical and
approximate discussion of subcritical finite-size condensation does not
supply the fixed-density theorem sought here. No theorem from that paper
is used in the new capping proof. A further search did not identify an
applicable exact stationary formula or a theorem whose hypotheses close
the present limit. This is not an exhaustive literature-priority search.
