# Internal audit of the new closure argument

24 October 2026. This is an internal mathematical audit by the same research
assistant, not an independent referee report. The all-parameter proof is in
README.md; the finite audit is supplementary.

## Claim being audited

For the unit-rate reduced backchip chain, the canonical pile probability
converges uniformly on compact density intervals, with bound
O_R((log(N)/N)^(1/4)). In particular all sequences N->infinity,
H/N->eta<infinity give the same pile-probability limit.

## Critical steps

1. **The observable is a spatial average, not one height.** Its instantaneous
   drift is at most total_mass/block_length. This bound is pointwise even
   for a single macroscopic pile; it does not presume a tail bound.
2. **Predictive jumps are nonnegative.** The height update is inflationary,
   its common-clock semigroup preserves coordinatewise height order, and
   the averaged height has positive coefficients. These facts apply to
   two profiles of the same mass on the same ring, exactly the setting
   used for each predictive jump.
3. **Their sum, not merely each jump, is bounded.** The identity
   L P_u A=P_u LA gives sum_i a_i<=H/ell. No factor equal to the number of
   clocks appears in the exponential compensator. The exact audit tests
   this identity, its positivity, and the squared-jump consequence.
4. **Unbounded heights cause no generator-domain gap.** The function
   LA is a bounded function on the finite gap state space. The identity
   P_u A=A+integral_0^u P_s LA ds reduces commutation to a finite-state
   backward equation. Actual height growth has finite exponential moments
   for each fixed ring, since jumps are bounded and the clock count is
   Poisson. Thus the Doob and exponential martingale arguments are valid.
5. **The centering is the terminal expectation.** The martingale is
   P_(t-s) A(h(s)); at time zero it equals E A(h(t)), and at time t it
   equals A(h(t)). It is not incorrectly centered by A(h(0)) or Ft.
6. **Left averages use lifted indices.** Consecutive blocks of length at
   most the ring size use distinct physical clocks. Helical offsets add
   deterministic constants to the average and do not affect its drift,
   jumps, or centered moment-generating function.
7. **Spatial monotonicity is applied to h, not to increments U.** The
   floor-profile bias is kept explicitly. Initial spatial rotation followed
   by vertical recentering differs from the original floor profile by only
   zero or one, so the expected increments at all phases differ by at most
   one. No spatial independence or symmetry of the stationary law is used.
8. **Auxiliary rings have mass floor(theta*m).** They need not have exactly
   the target density. Before the first winding, the difference of their
   initial heights from the phase-shifted target heights is in {0,1,2}.
   The rounding audit checks this new step exactly.
9. **Overlapping auxiliary rings need not be independent.** Each auxiliary
   marginal has m distinct independent target Poisson clocks. The maximum
   bound uses individual moment-generating functions and log-sum-exp, which
   requires no independence between copies.
10. **Localization failures are controlled in expectation.** On a winding
    event the actual height change can be large. The proof retains it,
    bounds it by the Poisson path count, and uses
    E[Z 1{Z>=m}]=t P(Z>=m-1). The extra +1 for a nonzero floor phase is
    retained. No bad event is discarded solely because it is unlikely.
11. **The averaging length fits in the auxiliary ring.** For
    ell=ceil((t^3 log(2N))^(1/4)) and t>=log(2N), ell<=ceil(t)<=ceil(4t).
12. **The time is linear in the smaller road size.** With t=n/8 and
    n<=m<=2n, n>=64, both target rings satisfy all localization hypotheses.
    The original comparison's winding probability is also exponentially
    small. The resulting error is O_R((log(n)/n)^(1/4)), not just o(1).
13. **The error is summable over doublings.** The logarithmic factor grows
    polynomially in the doubling index, while its coefficient decays
    geometrically. The last step from a power-of-two multiple to an
    arbitrary larger size uses the same comparable-size estimate.
14. **The total density is not inferred from a weak limit.** The argument
    uses finite canonical currents and deterministic balanced initial data.
    It never assumes that local weak limits retain mean mass or are pure
    density phases. Thus the old escaped-mass obstacle is bypassed for this
    observable, rather than silently assumed away.

## Exact new audit

`verify_new_step.py` uses integer-scaled embedded semigroups. For k future
clock events, it represents ell*N^k*P^k A exactly, including the change of
the height-zero reference after a clock at zero. This avoids both rounding
and a possible incorrect treatment of the additive height coordinate.
All compositions are included, including transient states.

All assertions passed for 54 chains and 432 averaged-height observables:

* 7,724,727 predictive-jump checks;
* 1,194,264 exact commutation and drift-bound checks;
* 2,187 phase-mean checks;
* 132,696 deterministic left/right average checks;
* 1,131,601 auxiliary-density and phase-rounding checks.

Only the new steps were checked here. The already completed finite-clock
path, current-bracket, and cross-size coupling audits were not rerun.

## Scope verdict

No unproved probabilistic estimate remains in the argument for convergence
of q_(N,H). A complete analytic proof is supplied, supported by the exact
new finite audits. The bound is not claimed sharp. Independent expert review
is still needed before treating this as an externally validated result.

This does not establish full canonical-measure convergence, absence of
condensation, an explicit formula for Q, the T_N formula, interchange of
limits, or the unrestricted fixed-braking NaSch flow formula.
