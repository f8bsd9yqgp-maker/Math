# Continue here without restarting

Date: 24 October 2026. The main fixed-density limit is **still open**.
Do not mistake a sharp finite-class bound for thermodynamic convergence.

## Newly completed

1. For all N>=3,H>=0, q_(N,H)<=5H/(17N), F_(N,H)>=12H/(17N).
   Equality at N=H=3 proves the coefficient optimal for this class.
   N=2 is excluded, with the exact counterexample q_(2,2)=1/3.
2. A bounded pair potential Phi, 0<=Phi<=15N, and an explicit triple
   telescoping table prove L Phi >=17 Q-5 H pointwise. There are only
   320 essential integer inequalities; clipping reduces all larger masses.
   The stronger residual is at least (5c-18)_+.
3. For every initial state, E integral_0^t Q/(Nt)
   <=5H/(17N)+15/(17t). With h(u)=(1+u)log(1+u)-u, the probability of
   exceeding this envelope by epsilon is <=exp[-Nt h(17 epsilon/14)].
   This is NOT concentration about the unknown stationary q.
4. At k modified rate-one bonds, any legal partial transfer gives
   qbar_modified<=5H/(17N)+14k/(17N). This is NOT a difference bound
   between modified and original q. For caps, retain the overflow term
   in the current formula.
5. For an infinite-line TI stationary law of finite positive mean rho,
   q<5rho/17. Strictness follows by finite gathering of four units.
   Without any moment assumption, 17q<=E min(5g_0,18) still holds.
6. Negative association of piles is NOT preserved even from deterministic
   data: N=4,H=7,g(0)=(0,0,0,7) gives
   Cov(1{g_0(t)>=2},1{g_1(t)>=2})=t^4/24+O(t^5)>0.
   The unique four-event word is (3,2,1,2). This does NOT disprove
   stationary negative association.
7. Any additive local potential with range R and summand oscillation B_N
   can certify a pointwise lower bound q>=ell_N only with
   ell_N<=[1+(R+1)B_N]/N. Test the single-pile configuration. Fixed-range
   uniformly bounded drift tables cannot prove a positive limiting lower q.
8. Exact recurrent class: all configurations with min_i g_i<=1. A reverse
   gathering algorithm proves reachability. Thus the entire composition
   chain is irreducible for H<2N. This closes that old finite subproblem.
9. No single finite-dimensional complex trace-matrix representation can
   give all canonical laws for every N,H. All-two states are transient, so
   tr(A_2^k)=0 for every k>=2; hence A_2 is nilpotent. The recurrent state
   of D consecutive twos and one zero contradicts dimension D.
10. A specified local cancellation ansatz even with N,H-dependent matrices
    requires dimension D>=floor(H/2)+1 for 4<=H<2N. Its (2,2) equation
    forces [A_2,hat A_2]=-A_2^2, hence nilpotence.
11. A rank-one A_0, including well-defined infinite-dimensional versions,
    fails already at N=H=6: states (2,0,1,0,3,0) and (2,0,3,0,1,0) have
    different exact stationary weights, but rank-one zero factorization
    would force equality. Full 462-state rational certificate is provided.

## Exact audit

Run `python3 nasch/continuations/2026-10-24-sharp-drift/verify.py` from
the repo root. It uses only the standard library. All 320 main inequalities,
1,920 partial-defect inequalities, 4,950 global ring states/26,928 events,
12 stationary chains/275 balance equations, and 341 short clock words pass.
The analytic finite-reduction proof is supplied in README.md.
Run `support_verify.py` alongside it: 31,733 reverse paths, 552,001 reverse
edges, 45 independent reachability graphs, and all 462 rational balances
for the rank-one-zero counterexample pass. See SUPPORT_AND_MATRIX_OBSTRUCTION.md.

## Discovery provenance

`certificate.json` is authoritative for the proved tables. The discovery
MILP used D=5, pile coefficient17; the gauge u=(11,0,0,0) gives the
displayed P with range [0,15]. No floating optimizer output is a proof.
Exploratory larger-block coefficients have no exact certificate here.

## Do not repeat these unsupported steps

* Common upper envelopes are not stationary difference estimates.
* Transient positive correlation is not a stationary counterexample.
* Stationary negative pile correlations, even if proved, do not alone
  establish uniform integrability of mass.
* Capped current is not generally concave in H: N=2,cap2 gives currents
  1/2,2/3,1 at H=1,2,3 and positive second difference 1/6.
* A one-bond cap does not automatically remove order-N corrector range.
* Existing uniqueness is conditional on deterministic finite density;
  canonical limits can still mix phases and lose mean.

The most concrete unresolved routes remain the corrected two-prime dilation
comparison, sublinear-reserve core-buffer loss, fixed-cap convergence, or
the marked exiting-rank scaling law. None was proved in this continuation.
The original T_N and the unrestricted stationary traffic formula remain open.
