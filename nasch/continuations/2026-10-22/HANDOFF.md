# Continue at this point

Status: fixed-density canonical convergence is still unresolved. Do not
restart the earlier structural proofs. Do not describe the new sufficient
condition as a verified property of the model.

Read README.md in this directory, then ../../density_phases_proof.md only
as needed for the existing infinite-volume theory.

## New proved results

* Height map B(a,b) = min(b,max(a+1,b-1)). It is monotone and dominates the
  unit-service map U(a,b) = min(a+1,b).
* F_(N,H) >= H/(N+H-1), hence
  q_(N,H) <= H(H-1)/[N(H+N-1)]. Equality holds for H <= 2;
  a finite gathering word proves strictness for H >= 3 with an explicit
  positive bound. This is an upper bound on piles and does not rule out
  condensation.
* Increasing any clock rate cannot decrease current. Sending one rate to
  infinity removes that site. Thus F_(N,H) <= F_(N-1,H), at fixed H.
* The main target would follow if, for k = 2 and 3,
  q_(kN,k(H-1)+1) <= q_(N,H)+C_R/N for H/N <= R, with C_R independent of
  N,H. The implication is proved. The hypothesis is not.
* An exact single-queue FIFO recurrence is included. It is not a closed
  recurrence for the original T_N.

## Most concrete unresolved attack

Prove or falsify the preceding two dilation inequalities, allowing the
O(1/N) error. Exact versions and stronger joining/ratio inequalities have
survived the listed finite checks. They have no coupling proof yet.

If the exact dilation inequalities hold, the limit has the conditional
formula inf q_(n,h) over (h-1)/n > eta. The difference between proving this
formula conditionally and actually establishing its hypothesis is the
remaining logical gap.

The number-theoretic part of the reduction uses the asymptotic multiplicative
density of 2^a 3^b; only doubling alone would not justify the same step.
Site removal controls the small remaining mismatch in ring sizes.

## Audits and calculations already done

verify.py: standard-library rational arithmetic. It checks the strict
comparison word for all 79,594 listed initial pairs, the FIFO recurrence,
48 exact stationary chains, the new finite inequalities, and selected
conjectured comparisons. It independently checks four rotation quotients
against full-state solves. See results/verified.json for exact counts.

cross_size_probe.py: SciPy; 174 chains at N <= 12, H <= 24 and at most
50,000 unquotiented compositions. No floating-point violations of the
two joining variants or the stronger ratio ordering were found. The
output is exploratory, not a proof certificate.

pile_covariance_probe.cpp and its output preserve simulations at H=N,
N=32,128,512. The observed negative pile covariances have no certified
stationary error. There is no proof of negative association.

Earlier exact conditional-pair covariance probes also found no positive
values at (N,H)=(4,4),(4,5),(4,6),(4,7),(5,4),(5,5),(6,4), but no general
claim follows. They are a possible direction, not an input to this note.

## Shortcuts rejected

* The height map does not commute with minima or maxima: the pairs (0,3)
  and (2,2) both map to 2, but their minimum maps to 1 and maximum to 3.
* The finite-time height certificate has error H/t. Taking t small relative
  to N to avoid wrap-around does not make that error vanish at fixed density.
* Finite-occupation hydrodynamic theorems and stationary-product condensation
  theorems checked in this run do not directly apply to this model.
* The FIFO two-service fact is not a two-service bound for a second-class
  discrepancy in the monotone mass coupling. New background arrivals can
  block that discrepancy repeatedly.

The original T_N, a general stationary traffic formula, canonical mass
uniform integrability, and fixed-density condensate exclusion are all still
open here. No example of stationary nonconvergence has been constructed.
