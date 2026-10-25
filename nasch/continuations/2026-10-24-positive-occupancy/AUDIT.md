# Internal audit

24 October 2026. This is the assistant's internal mathematical audit, not
an independent expert report, formal proof-assistant certificate, or priority
review. Both proof files must be read with their stated scope.

## Positive pile-density proof

1. **Correct model.** This is the rate-one continuous-time backchip process,
   not the parallel-update NaSch chain at a fixed braking probability.
2. **Periodic weights.** Although lifted heights are not periodic, the
   weights exp(lambda*(h_i-theta*i)) are: theta*N=H exactly.
3. **Large gaps are allowed.** The bound on total downward weight variation
   uses only nonnegative gaps and periodicity. It does not bound a ratio
   v_(i+1)/v_i from above.
4. **Block boundary.** The generator formula is used only at lengths k<N.
   Choosing ell<=N uses k<=ell-1<N, including when ell=N.
5. **Weight transport is retained.** Summing a shifted empty-block indicator
   changes its weight. The error is S_(k-1), bounded by delta*V; S_0 is zero.
6. **Eliminating R.** Its coefficient is nonnegative only for ell>=3.
   That restriction is maintained before substituting R<=(G-P)/2.
7. **Jump product rule.** The extra term is
   v_i(exp(lambda*d_i)-1)*phi_i(T_i g), with the post-update potential.
   It is nonnegative because phi is nonnegative. It is not dropped with
   an unjustified assumption about the sign of L phi.
8. **Positive corrected function.** Y=V-beta*Phi is bounded below by
   (1-m*beta)V>0. The sign of the coefficient multiplying V is positive,
   allowing conversion to a bound multiplying Y.
9. **Unbounded heights at fixed N.** Gap increments are bounded by H and the
   event count has all exponential moments. Dynkin/Gronwall and Jensen
   therefore apply without a hidden stationary exponential-moment assumption.
10. **Finite time to stationary speed.** The finite gap chain has one closed
    recurrent class. The expected integrated donor current divided by time
    tends to the stationary current. No mixing bound uniform in N is used.
11. **Rounding and constants.** ell=max(3,ceil(2/theta)) is admissible because
    H>=2. The proof treats ell=3 and ell>=4 separately. The bound on alpha
    is analytic, not inferred from the rational grid audit.
12. **Scope of condensation claim.** The positive lower bound excludes local
    vacuum and M_N/H_N->1 in probability. It alone does not exclude partial
    condensation or a vacuum component in a mixture.

## Phase-current and critical-density proof

13. **Stationary phase current is identified, not assumed.** The flat line
    speed is obtained from the proved ring oscillation bound with N~8t.
    Random initial partial-sum errors are o(t) in L1 by the ergodic theorem
    and uniform integrability of averages of one fixed integrable marginal.
    Future clock counts are independent of the initial configuration.
14. **No density bound on each mixture component is assumed.** Initially
    only E R<=eta is available. At a supporting-line contact point, the
    two nonnegative terms in equation (8) force equality of means and
    support on the contact set. Choosing its *largest* point then forces
    a single density. This is the step that establishes existence of a phase.
15. **Uniform integrability is earned.** At contact points it follows from
    weak convergence plus convergence of means; below them, from stochastic
    domination. At a finite endpoint it follows from the explicit
    1-Lipschitz tail comparison, with the remaining mass difference sent to zero.
16. **Critical limiting phase.** First moments pass through a coordinatewise
    monotone coupling of the contact phases. Mixing is proved by bounded
    cylinder approximation with L1 error eta_c-r_j, not by asserting that
    mixing is closed under arbitrary weak convergence.
17. **Saturation is conditional on finite eta_c.** Maximizer inequalities
    prove a permanent plateau in that case. Stochastic order and the earlier
    strict pile-detection theorem identify all supercritical local limits.
    Neither a finite critical density nor an infinite one has been selected.
18. **Below-critical phase selection remains separate.** Uniform integrability
    at all eta<=eta_c does not prove ergodicity or unique local canonical
    limits at every such eta. The report does not make that inference.
19. **Explicit small-density interval.** The rational logarithm certificate
    gives Q(1)>1/218. Combining it with Q(r)/r<=r/(1+r) at a maximizer
    gives eta_c>1/217. This proves a specific interval without an order-N
    pile, not an assertion that eta_c lies below or above 2.

## New computation completed

`verify.py` passed 3,276 local empty-block generator checks, 2,972 weighted
rational generator certificates, and 19,899 rounded-parameter checks.
Eight rate bounds use rational exponential enclosures. The density-one
logarithm certificate is exact rational arithmetic. Its addition was checked
separately without rerunning the earlier passed checks; the complete script
contains all checks for future reproduction.

No simulation, floating-point extrapolation, old stationary-chain solve,
or old verifier was used to establish the new conclusions. Floats in the
results are display values of rigorously enclosed rational bounds.
