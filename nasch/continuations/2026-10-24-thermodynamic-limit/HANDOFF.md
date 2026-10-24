# Canonical pile-probability limit: new proof completed

24 October 2026. Read README.md and AUDIT.md in this directory first.
The main scalar fixed-density convergence problem now has a complete
analytic proof in this continuation, subject to independent review.
Do not repeat the preceding investigations or present their results as new.

## The theorem

For every finite R,

  sup_(0<=eta<=R) |q_(N,floor(eta*N))-Q(eta)|
       = O_R((log(4N)/N)^(1/4)).

Hence every sequence N_j->infinity, H_j/N_j->eta<infinity gives
q_(N_j,H_j)->Q(eta). This answers the requested limit question on (0,2).
The theorem applies to the reduced unit-rate process, not to full NaSch
at a fixed positive nontrivial braking parameter.

## The missing estimate, now proved

For balanced initial heights and theta=H/N<=R, let
R_(N,H)(t)=E(max_i U_i(t)-min_i U_i(t)). If
t>=max(1,log(2N)) and ceil(4t)<=N, then with c=3log(3)-2,

  R_(N,H)(t) <= 22R [t^3 log(2N)]^(1/4)+2R+6
                  +2N(2Rt+1) exp(-ct).

This replaces the unproved assumption in the previous height-comparison
continuation. The proof does not require any stationary mass-tail control.

## Mechanism

1. On an m-site auxiliary ring of mass h, average ell<=m consecutive
   lifted heights in A. Then 0<=LA<=K=h/ell.
2. For v_u=P_u A, monotonicity gives predictive jumps a_i>=0, and
   sum_i a_i=L P_u A=P_u LA<=K. Therefore the time-dependent Doob
   martingale has the two-sided exponential bound

   E exp[+/-lambda(A_t-E A_t)] <= exp[t(e^(lambda K)-1-lambda K)].

3. Spatial height monotonicity bounds a one-site increment by averages
   to its left and right, with deterministic error <=phi*ell+1.
   Floor-profile rotation gives mean differences at most one.
4. Localize every target site to an auxiliary ring of m=ceil(4t) sites,
   mass floor(theta*m). Share its clocks with the corresponding target
   segment. Auxiliaries may overlap; their independence is not used.
5. Outside first-winding events, initial-height differences are in
   {0,1,2}. On failure use the full Poisson path-count bound, retaining
   the +1 phase correction and its expectation.
6. Log-sum-exp bounds the range of N auxiliary terminal heights.
   Choose ell=ceil((t^3 log(2N))^(1/4)) to balance averaging bias against
   martingale fluctuations. This proves the displayed oscillation bound.
7. Apply the already proved cross-size comparison at t=n/8, n<=m<=2n.
   The error is O_R((log(n)/n)^(1/4)). Sum over doublings and the final
   comparable-size step. This proves all-size convergence uniformly in eta.

The README supplies an explicit comparison E_R(n) and a convergent series
Omega_R(n)=sum_(j>=0) E_R(2^j n) bounding the final error.

## Exact new verification

The standard-library verifier checks integer-scaled finite semigroups with
the additive height coordinate correctly retained. All passed:
54 chains; 432 observables; 7,724,727 predictive jumps; 1,194,264 commutation
checks; 2,187 phase means; 132,696 spatial averages; 1,131,601 rounding cases.
No new simulation or old-verifier rerun was used to establish the theorem.

## Scope still open

Q is not given in elementary closed form. Full local canonical-measure
convergence, stationary mass UI, condensate behavior, positive lower
occupancy, the original first-passage T_N, interchange of limits, and
the unrestricted fixed-braking NaSch flow remain unresolved.

The rare-braking-first coefficient at vehicle density rho>1/3 now has a
unique thermodynamic limit rho*(eta-Q(eta)), eta=(1-rho)/rho. This does not
interchange the limits or prove a general stationary traffic formula.

This is internally audited AI-assisted research. It is not peer reviewed
or formally verified; no literature-priority claim is made. The proof
should be checked independently before its status is externally asserted.
