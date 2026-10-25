# Continue from here: small phases and affine gaps

25 October 2026. Parent before this continuation:
34b46770173e30ada33e50ac76cb16710ae19287.

Read README.md and AUDIT.md in this directory. These are internally audited
AI-assisted proofs, not independent peer review. Do not restart or rerun
the previous scalar convergence, positive-occupancy, or critical-density work.

## Newly proved

1. If b is a canonically selected pure-phase density, the largest minimum
   or maximum of Q(r)-s*r on [0,b] is also selected. For minima the already
   proved preservation of the mean below eta_c is essential.
2. Let b_* be the largest maximizer of Q(r)/r. It is selected and
   1/217<b_*<218. For every eta>0 choose

       a = 2^(-20) min(eta^2,1),
       c_eta = largest argmin_[0,b_*] (Q(r)-a*r).

   Then c_eta is selected and

       kappa(eta)=2^(-22) min(eta^2,1) <= c_eta < eta/2.

3. Every canonical local limit at eta dominates nu_(c_eta), so its random
   component density R is at least kappa(eta) almost surely. This excludes
   a vacuum mixture component, not just the vacuum law itself.
4. Put xi=kappa^3/1152. For every fixed epsilon>0, with probability tending
   to one, every cyclic arc of at least epsilon*N sites has mean mass at
   least kappa/4 and pile density at least xi/4. In particular the longest
   pile-free arc is o(N) in probability. This holds at every positive target
   density, including above a possible finite critical endpoint.
5. The set C of canonically selected pure-phase densities is closed and
   cofinal below eta_c. Every gap (a,b) of C is an affine interval of Q,
   with selected endpoints. Canonical limits inside the gap have component
   densities in [a,b] and mean equal to the target density.
6. Therefore every density where Q is not locally affine is selected. The
   remaining possible gaps are a countable collection of disjoint open
   affine intervals; no gap begins at zero.

## Crucial distinctions

The set of existing stationary pure phases has not been proved equal to C.
Do not infer canonical selection merely from existence of a pure phase.
Do not infer a specific endpoint mixture on an affine interval. The exact
toy law in AUDIT.md shows the missing information, but is not an actual
stationary backchip counterexample.

The new positive-background theorem does not exclude a condensate above a
positive background. Whether eta_c is finite remains open. The exact Q,
affine-interval exclusion or selection within such intervals, original T_N,
rare-braking interchange, and unrestricted finite-braking NaSch flow are
not solved.

## New audit only

verify.py uses exact integers and fractions, with no random sampling:
6,206 contact moment checks (2,268 extremal equalities; 208 interior contacts),
467,568 arc checks (17,147 low-density premises), constants, and two obstruction
examples. All passed. No previous verifier or stationary solver was rerun.

## Next substantive targets

* Exclude open affine intervals of Q by a model-specific strict-curvature or
  fluctuation theorem, or prove canonical selection inside them directly.
* Determine whether the positive-background condensate alternative really
  occurs, equivalently whether the critical endpoint is finite.
* Use the new small pure phases as genuine stochastic lower barriers in
  a condensate-environment argument; ordinary unconditioned background
  averages must still not replace the environment seen by a moving pile.
