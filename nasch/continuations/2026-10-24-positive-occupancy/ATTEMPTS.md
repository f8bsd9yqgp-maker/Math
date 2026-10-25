# Continuation record and rejected shortcuts

24 October 2026. This run began after commit
914102c5840511b8f97da0640ec30ade81c069e0 had already proved the scalar
fixed-density limit. That result was not rederived or counted as new.

## Work leading to the new proof

The initial target was stronger stationary-law control or an explicit Q.
Several lines of reasoning were considered before the successful weighted
height certificate:

* One-site threshold balances, spacing duality and tandem-queue formulas
  still leave multi-site temporal correlations. The previous exact
  counterexamples to scalar closure remain valid.
* Knowing E Q(R)=Q(eta) and E R<=eta does not in general select a phase.
  The eventual successful supporting-line argument adds a sign to both
  defects and uses the largest contact point. It is applied only where its
  hypotheses really hold.
* A return to the three-vacancy T_N problem identified the critical tandem
  queue near a corner as a possible route to a potential kernel. No kernel
  formula, asymptotic constant proof, or improved T_N recurrence was obtained.
  No new numerical table was produced or represented as progress on that target.
* A naive attempt to transfer the height argument to full NaSch fails:
  its velocity memory does not obey the monotone two-coordinate height update
  used here. No finite-braking result is inferred.
* Exponential heights initially gave an insufficient bound if singleton
  occupancies were estimated pointwise by one. Empty-block generator
  identities supply a density-dependent singleton bound with a bounded
  potential. Retaining the moving-weight error and the jump-product term
  makes that bound usable in an exponential height estimate.

## Proven outcomes

The README supplies the uniform positive pile-density theorem and a
finite-parameter current bound. PHASE_SELECTION supplies the phase-current
identity, upper supporting-line selection, the critical-density alternative,
and the explicit interval 0<eta<=1/217 with preserved mass and no order-N
pile. These are analytic proofs with exact finite audits, not extrapolations.

## Specific remaining gaps

1. Determine the function Q, or enough of its shape to identify every
   below-critical canonical phase.
2. Decide whether Q reaches its supremum at finite density. Equivalently,
   decide whether the critical endpoint eta_c defined here is finite.
   If it is infinite, the new theorem already gives mass uniform
   integrability at every finite density; that premise is not yet proved.
3. Even when first moments are preserved, exclude or characterize mixtures
   of finite-density stationary phases at arbitrary densities below eta_c.
4. Solve the original T_N closed-form/recurrence question and the unrestricted
   finite-braking NaSch stationary traffic flow.

## Literature scope

Primary-source searches found no theorem imported to close these gaps.
The backchip model antecedent remains Whitehouse, Costa, Blythe and Evans,
https://arxiv.org/abs/1407.1668 . General non-product attractive-system
hydrodynamics is relevant context, for example Bahadoran, Guiol, Ravishankar
and Saada, https://arxiv.org/abs/math/0609605 and
https://doi.org/10.1214/EJP.v15-728 . Those results are not used as a substitute
for checking unbounded-mass assumptions or existence of every density phase.
No assertion of first discovery relative to the literature is made.
