# Attempts and limits of the 23 October continuation

This is an audit trail, not an additional list of theorems. It records the
arguments actually investigated so the next run does not repeat them.

## Core rings and buffers

The physical embedding and the exact loss identity succeeded; see the proof.
A tempting next step was to use the bounded-jump corrector martingale as a
uniform buffer estimate. That step did not succeed. If
chi_r=Phi_r-h_(r,0), the corrected buffer

    w_r = b_r + chi_(r+1) - chi_r

has total B and bounded transfers equal to core-corrector increments.
However, w_r need not be nonnegative: the range of chi_r has width
H(N-1)/N. Applying a nonnegative-queue estimate to these signed variables
would omit an order-N term. A quadratic stationary balance did give the
proved bound F^2/[B-2(H-1-q)] when its denominator is positive. This is
uniform over invariant laws but has an order-N reserve threshold.

Trying to discard the loss-weighted term in that quadratic balance fails:
for N=2,H=3,B=1 its stationary value is exactly 54163/211093 > 0.
This additional counterexample was promoted from a floating-point probe
to a full exact stationary certificate. A bounded positive value would
still be adequate, but no uniform upper bound has been proved.

The retained simulations suggest that B of order sqrt(N), and perhaps
even a fixed sufficiently large B, permits good throughput. These are
finite uncalibrated Monte Carlo runs, not a mixing-time or stationary-error
certificate. They should guide a proof attempt, not substitute for one.

At a boundary, a partial transfer v changes chi by a_partial-v. At internal
events, chi increases by the corresponding nonnegative corrector increment.
Thus internal positive increments have total instantaneous rate at most F,
but this alone does not control the stationary starvation loss.

The version that refuses an entire boundary batch when the buffer is too
small can deadlock: if every core is piled at site zero and B<H-1, all
buffers are too small for that batch. This is why the proved protocol uses
partial transfers. This deadlock argument does not apply to that partial
protocol with positive reserve.

## Synchronized clocks and decorrelation

The ordered-prefix representation suggested embedding k identical lower
cores plus one additional particle in a k-sheet ring. This gives an exact
stationary synchronized law, including its explicit pile probability.
No identification with an integrable stationary product law was obtained.

The proposed next step, monotonicity under replacing synchronized clocks
by independent clocks, is false. The report contains exact certificates
in both directions and a nonmonotone example at fixed size and mass.
The original corrected-mass dilation inequality remains unrefuted.

## Corrector influence

Another contemplated estimate was a uniform bound of order 1/N for every
single-coordinate height increment of Phi at bounded density. Exact small
systems do not support assuming such a bound. The exploratory influence
probe at H=N found maxima of N times this increment approximately

    N=2: 1.3333, N=3: 1.2353, N=4: 1.5727,
    N=5: 1.9784, N=6: 2.3229, N=7: 2.6359.

For N=5,6,7, a maximizing state has masses (H-2,2) at two adjacent sites
and zero elsewhere, with the coordinate increment at the two-particle site.
These finite results do NOT prove that the bound is false asymptotically.
The exact probe and its output are retained separately from the theorem
verifier. No asymptotic claim relies on them.

## Other paths considered but not completed

* A hydrodynamic argument might identify averaged current even if canonical
  local limits mix phases or lose mass. No theorem applicable to the
  unbounded batch transfers, with these possible singular masses, was
  verified. A bounded-occupation or stationary-product theorem is not enough.
* Spatially mixing clock representations of existing finite-density phases
  remain qualitative. They do not yield a uniform finite coding radius or
  justify periodizing an infinite stationary process on every large ring.
* One-sided tandem queues have bounded mean mass at a fixed input rate, but
  bounded first moments do not imply uniform integrability along tandem
  depth. Pure aggregation already shows why this inference would fail in
  a related process. No backchip-specific tail argument was supplied.
* No proof of negative association, no stationary product formula, and no
  universal stochastic ordering in road size at fixed density was obtained.
* A moving-condensate erosion argument was reconsidered. In a finite-mean
  stationary background the current is density minus pile probability,
  while a large pile moves at asymptotic rate one. Turning this velocity
  observation into a rigorous erosion estimate requires controlling the
  biased environment seen by the pile. Replacing that environment by the
  ordinary stationary background is not justified.

Literature context was rechecked, without a claim of exhaustive coverage:
Whitehouse et al., *Maintenance of order in a moving strong condensate*,
[author preprint](https://arxiv.org/abs/1407.1668), studies the relevant
backchip family; its approximate treatment does not provide the missing
estimate used here. Kuniba et al., *Multispecies totally asymmetric zero
range process: I. Multiline process and combinatorial R*,
[primary preprint](https://arxiv.org/abs/1511.09168), concerns a different
priority jump rule. No equivalence with the second-smallest-retention rule
was established, so none of its stationary formulas is imported.

Rajesh and Krishnamurthy, *Effect of spatial bias on the nonequilibrium
phase transition in a system of coagulating and fragmenting particles*,
[primary preprint](https://arxiv.org/abs/cond-mat/0206100), supplies a
related condensate-frame argument for a different diffusion-and-chipping
process. Its analysis starts with a single aggregate and finite-density
background and uses far-separated correlation factorization. This is not
the canonical phase-selection and uniform-integrability theorem needed
here. No unconditional result for our backchip chain was inferred from it.

The negative findings in this file concern proposed proof routes. They do
not constitute a stationary counterexample to the user's target limit.
