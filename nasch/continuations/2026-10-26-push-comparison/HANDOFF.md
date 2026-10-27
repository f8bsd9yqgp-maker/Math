# Continue from here — run 22

Completed 27 October 2026. Do not restart old stationary solves.
Parent: `146dab8e50d54298b2a2fe019871e7290905dc06`.
User wants chat prose in a copybox and genuine proved results preserved
on GitHub. All model-specific research remains internally audited,
AI-assisted, not independently peer-reviewed. The complete problem is
not closed.

## Strongest new result

For full stationary NaSch, N>=2, 1<=H<N, 0<epsilon=1-p<1,

    U <= epsilon sum_(k=1)^H p^(k-1)(H)_k/(N)_k
      <= epsilon eta/(1-p eta),   eta=H/N.

Also U<=epsilon H/(N-H+1). Together with the inherited lower bound,

    epsilon H/(N+H-1) <= U <= epsilon eta/(1-p eta).

Consequently J/(epsilon delta)->1 whenever eta->0, uniformly over
epsilon in (0,1), with no restriction on epsilon N. Here
delta=H/(N+H), J=U/(1+eta), and the explicit relative error is at most
eta/(1-eta). This is the vanishing-vacancy regime, not fixed eta>0.

Proof mechanism: original height update <= a monotone memoryless upper
map A. Take binary auxiliary gaps b and use the same Bernoulli mask.
In each run of ones move the prefix ending at the rightmost marked site.
Then y'>=A(y), with y' still having binary gaps. Uniform binary words
are stationary: use zero-to-zero one-run lengths L; the hole movement
kernel is p^L for K=0 and epsilon p^(L-K) for 1<=K<=L. It factors
as v(K)w(L-K), v(0)=1, v(k>0)=epsilon, w(r)=p^r, whose convolution
is identically one. A uniform anchor supplies the unrooted binary law.
Expected movement is the displayed falling-factorial sum. Start from
an independent stationary auxiliary word with a finite dominating height
translation, then take long-time mean speeds. Read README for details.

The initial Poisson pushing proof is preserved in POISSON_PUSH.md.
Its logarithmic factor is now superseded. Do not state it as the best bound.

## Dynamic reduction, including the sharper polynomial time error

Let X_n be stationary full traffic, G_n its exact full-braking projection,
and Z a reduced backchip chain with Z(0)=G_0. Take epsilon<=1/2,
lambda=-log(1-epsilon), C=P(v_0>0,g_0>=2),
B=P(c_0=1,c_1=0), and D=number of unequal gaps. Then

    E D(G_n,Z(n lambda))/N
      <= 8 epsilon(C+2B/p+epsilon)
           [n+lambda n(n-1)/2].

For r observed labels add the projection error 2rC and multiply the
displayed fraction by r. The same coupling covers any finite number
of observation times. One step uses Poisson events over length lambda,
with a coin meaning at least one event. Mixed old activity costs
8 epsilon(C+2B/p) per site. Bad donors (repeated or adjacent marks)
cost at most 8epsilon^2 per site.

The crucial improvement over an exponential error: a discrepancy can
propagate only left. One seed's influence interval extends at rate one,
so E D_t<=(1+t)D_0. Telescope inserted errors and propagate each through
the independent future only once; do not iterate the linear bound
multiplicatively.

Existing C=O_R(epsilon^(1/3)), B<=epsilon R give unrestricted local
finite-dimensional reduction for every eta in (0,2). For eta<=R<1 the
new upper comparison gives C<=epsilon R/(1-R), improving the error
to O(epsilon). On the same finite ring, tracking at a fixed number of
growing observation times is valid up to o(epsilon^(-1/6)) generally
and o(epsilon^(-1/2)) below eta=1. These statements are not uniform path
convergence and do not identify unbounded currents.

## New obstruction and the remaining proof gap

For ell>=1, N=5ell+3, take g_i=3,v_i=1 for i=1,...,ell,
g_(ell+1)=ell+2 with zero velocity, and zero elsewhere. One nonbraking
coin at ell+1 changes the eventual projected lift by ell+1 at every
site 1,...,ell+1. Total projected travel is (ell+1)^2, whereas the
rest-started experiment gives only ell+1. Extra travel is ell(ell+1),
but the two projected gap words differ at only two sites. This is a
pointwise obstruction, not a stationary counterexample.

Do not conclude current uniform integrability from either the Hamming
coupling or the O(epsilon) mean bound. Do not infer pure phase selection
from local stationary/process convergence or from time-averaging a
mass-thinned state. No valid capacity-two extension of the pushing
comparison has been constructed.

The earlier unrestricted reduced scalar limit Q(eta), strict positivity,
critical-density alternative, and affine-gap selection results remain
in place. The restricted full-current theorem still requires epsilon N->0.
The new work does not decide eta_c finite versus infinite, pure selection
inside any actual affine gap, or the unrestricted fixed-positive-density
coefficient (eta-Q(eta))/(1+eta).

Next substantive target: a stationary, size-uniform weighted-transport
or tail estimate that closes the gap between local dynamic convergence
and normalized current, or a stronger comparison that actually matches
the reduced flux. Avoid another unbounded-current limit justified only
by bounded local convergence.

## Audits

Four new standard-library scripts passed. README and AUDIT list exact
counts. The final synchronous-law proof was checked coefficientwise for
all epsilon, not with numerical samples; the propagation proof has
362,529 exact event-word checks. No old stationary or Poisson equation
was solved again. Primary literature is credited in AUDIT; no priority
or independent-review claim is made.
