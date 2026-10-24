# What the present run closes, and what it does not

24 October 2026. This is an auditable research record, not a thermodynamic
convergence claim. The proved main result is in README.md.

## A. Sharp upper drift certificate: completed

The search sought a pair potential and a telescoping triple term satisfying

    5 c - 17 1{c>=2} + Delta P + W(a,b,c)-W(b,c,e) >= 0.

The selected integer tables prove the inequality for all masses by a finite
clipping reduction. They yield q <= 5 eta/17 for N>=3, a tail-sensitive
version, a finite-time expectation bound and exponential upper-deviation
bound, and a bound for finitely many partially transferring bonds.

The exact N=3,H=3 stationary law attains equality. Larger coefficients from
other floating block searches were not converted to exact certificates and
are not theorems. The sharpness is over all N>=3,H, not at fixed positive
density as N tends to infinity.

## B. Why bounded local drift searches cannot supply the missing lower bound

The following elementary obstruction explains a limit of this approach.
Fix N>R and let

    Psi_N(g) = sum_i f_N(g_i,...,g_(i+R-1)),

where each summand has oscillation at most B_N. The table may depend on N
and H. At a configuration with all H>=2 units at one site, Q=1 and only
one clock makes a nontrivial update. It changes two adjacent coordinates.
At most R+1 summands change, so

    |L Psi_N(single pile)| <= (R+1) B_N.

Therefore a pointwise lower certificate

    Q(g) + L Psi_N(g) >= N ell_N

on the entire canonical state space necessarily satisfies

    ell_N <= [1+(R+1)B_N]/N.

If (R+1)B_N=o(N), this method cannot prove a strictly positive limiting
lower bound for q. The same single-pile test obstructs a two-sided uniform
local Poisson approximation to a positive limiting pile probability.

This is a complete deterministic argument; it does not say the true limit
is zero. Unbounded potentials, growing interaction ranges, estimates in
stationary expectation, or a comparison using more than local drift are
not ruled out. The older nearly stationary single-pile constructions are
consistent with this obstruction and must not be mistaken for stationary
canonical laws.

## C. Negative-dependence preservation: disproved

The main note proves the exact small-time counterexample

    g(0)=(0,0,0,7),
    Cov(1{g_0(t)>=2},1{g_1(t)>=2}) = t^4/24 + O(t^5) > 0.

The sole four-event joint-pile word is (3,2,1,2). This starts from a
deterministic configuration with density 7/4, so even that especially
simple initial class does not preserve negative dependence of piles.

Negative association of stationary canonical laws is still undecided.
Exact exploratory tests of several stationary generating polynomials did
not find a negative Rayleigh difference. A finite search without a failure
is not a stability theorem. Moreover, a stationary pile-correlation bound
would address phase mixing but would not by itself control escaped mass.

## D. Concavity of capped current in total mass: disproved in general

Cap site 0 at two units on a two-site ring. For H=1,2,3 the cap never changes
a legal move, since the largest transfer is at most two. Exact stationary
currents are

    J(1)=1/2,   J(2)=2/3,   J(3)=1.

Thus J(3)-2 J(2)+J(1)=1/6>0. The assertion of general concavity in H,
sometimes suggested as a route to canonical interpolation, is false.
This does not decide an asymptotic concavity claim or the target limit.

## E. Capped bonds, buffers, and the remaining scale issue

The preceding capped-bond theorem is preserved, not re-proved here:
one cap of size C increases reciprocal current by at most 1/C. It reduces
the original limit to convergence with a fixed capped bond for arbitrarily
large C. That convergence is still unproved.

The new defect estimate

    qbar_modified <= 5 eta/17 + 14 k/(17N)

does not compare qbar_modified with q_original. Both may lie well below the
same upper envelope. Treating this bound as an O(k/N) comparison would be
a logical error. Likewise, a cap does not reduce the already-established
order-N worst-case current-corrector oscillation to its cap size.

The earlier core-buffer argument still needs a loss estimate tending to
zero with sublinear total reserves. The proved order-N reserve threshold
has not been removed. No new estimate here supplies that missing premise.

## F. Other structures examined but not completed

The FIFO departure recurrence remains a useful min/max recursion, but a
proof of the spatial scaling limit or the needed subadditivity was not
obtained. Mean preservation through every finite tandem stage does not
guarantee preservation in the limit; aggregation can violate uniform
integrability. Two-service residence for a FIFO-labelled particle is not
a two-service reset of arbitrary upstream memory.

A formal matrix-product stationarity algebra was examined more closely.
The resulting [support and matrix note](SUPPORT_AND_MATRIX_OBSTRUCTION.md)
proves the exact recurrent support by constructive reverse gathering.
It then excludes a common fixed finite-dimensional trace formula for all
N,H and proves that the usual local cancellation ansatz requires dimension
at least floor(H/2)+1 when 4<=H<2N. These statements allow complex matrices.
An exact 462-state example also rules out a rank-one empty-site matrix,
or scalar factorization of positive blocks separated by zeros.

These are new finite-canonical obstructions, distinct from the older
infinite-line cylinder-matrix obstruction. No positive infinite-dimensional
representation or partition-function asymptotics was constructed. The
ranked-reservoir representation remains exact but has no proved fixed-density
scaling limit for its exiting rank.

## G. Literature check and scope of external results

The new proofs above do not depend on an imported model-specific theorem.
The following primary sources were revisited as possible alternative routes:

* Gobron and Saada, [arXiv:0903.0316](https://arxiv.org/abs/0903.0316),
  gives attraction and discrepancy couplings for conservative multi-particle
  jumps, with hydrodynamic applications to specified models. Its abstract
  was checked; no applicable all-size canonical convergence theorem for
  this backchip rule was established in this run.
* Armstrong, Tran and Yu,
  [arXiv:1410.7053](https://arxiv.org/abs/1410.7053), proves stochastic
  homogenization for a class of one-dimensional nonconvex Hamilton--Jacobi
  equations. Its abstract was checked. A monotone height update alone does
  not verify its PDE hypotheses or identify our finite-ring limit, so no
  transfer of that result is claimed.
* Whitehouse, Costa, Blythe and Evans,
  [arXiv:1407.1668v3](https://arxiv.org/html/1407.1668v3), studies moving
  condensates for the rate family 1+b/n^alpha. The article labels relevant
  evidence numerical and its analytical condensate treatment approximate.
  It is context for this constant-rate problem, not a rigorous resolution
  of the canonical convergence question.

These checks are not a comprehensive priority review. No claim is made that
the wider literature cannot contain a useful theorem not yet applied here.

## H. Exact remaining objective

For H_N=floor(eta N), 0<eta<2, prove that every local subsequential
canonical limit has the same value of q. Existing structure gives a
mixture of unique finite-density stationary phases, with mean at most eta.
It does not select the mixture or retain the mean.

An adequate next step must genuinely address this issue: a valid comparison
between arbitrary sizes, control of canonical collision/mass tails together
with phase selection, or an exact stationary construction with asymptotics.
The new sharp upper bound and transient counterexample do not supply it.
