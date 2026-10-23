# Continue from this checkpoint

The canonical fixed-density limit is still OPEN. Do not infer it from the
finite identities or describe the uniform buffer loss estimate as proved.

Read README.md in this directory. It supplies complete proofs of:

1. A synchronized k-sheet cover with total mass k(H-1)+1 and stationary
   pile probability ((k-1) q_(N,H-1)+q_(N,H))/k. The invariant law is
   obtained from an ordered one-extra-particle coupling and a uniform sheet.
   Uniqueness of all synchronized invariant laws is not asserted or needed.
2. Failure of monotonicity in clock correlations. At fixed eight-site,
   five-particle mass, q(1/2)<q(0)<q(9/10). These are rationally certified
   stationary values, not numerical trend extrapolations. Clock-rate
   monotonicity from run 9 is unaffected.
3. A finite core-and-buffer protocol dominated by the ordinary backchip
   process in height order. For any invariant protocol law,

   J = F_(N,H) - E loss,
   q_(kN,kH) <= q_(N,H) + B/(kN) + E loss.

   Core mass is H per block. Total buffer mass is B. Partial boundary
   transfers are essential. Relabelling a buffer particle as a core
   particle does not physically move it.
4. An unconditional two-block loss bound, valid for every invariant law:

   E loss <= F^2 / [B - 2(H-1-q)] if B > 2(H-1-q).

   Normalize chi=Phi-h_0 to [0,A], A=H(N-1)/N. Define signed corrected
   buffers w_r=b_r+chi_(r+1)-chi_r. A block-r event transfers its corrected
   increment a from w_r to w_(r-1). On positive loss, w_r<=H-1-q.
   Stationarity of w_0^2+w_1^2 proves the bound. At fixed density the
   threshold is of order N, so the bound DOES NOT close the problem.

   The exact identity is B E loss = E V/2 + sum_r E[w_r loss_r],
   V=sum over all event types of a^2 <= 2F^2. The final weighted term is
   NOT always nonpositive: N=2,H=3,B=1 gives 54163/211093 > 0.
   An exact full-state certificate is included. A uniform upper bound
   on this term would suffice for the two-block estimate, but is unproved.

   For any k, the elementary capacity bound J<=B/k also holds.
5. A fully conditional convergence implication: an O(1/B) stationary loss
   bound at B=ceil(sqrt(N)), for k=2,3, would prove the desired all-size
   thermodynamic limit. Any summable geometric error O(N^-alpha), alpha>0,
   suffices in the earlier two-prime comparison argument.

The most concrete remaining target is the loss estimate in item 5. The
protocol core marginal is NOT known to be the ordinary canonical law. It
is invalid to apply canonical pile tail estimates to it without proof.
The bounded-jump current corrector does NOT remove the order-N boundary
current bias. At B=0 there is a fully blocked absorbing state with loss F.

The correlation derivative identity is also exact:

q'(c) = - E_pi_c sum_i (T_i-I)(T_(i+N)-I) psi_c.

The mixed difference has no universal averaged sign, as the exact examples
show. A more subtle bound could still prove the original dilation inequality;
the counterexample does not refute that inequality or canonical convergence.

Verification uses standard-library Fraction arithmetic, verifies the
quotient equations, then independently expands to all labelled states and
checks their balance equations. Results: 8 chains; 2,548 full equations;
340 quotient equations; 3,900 cover event identities; 9,860 physical buffer
event checks; 3,480 corrector-loss identities; 1,740 quadratic generator
identities; 892 positive-loss support bounds. The weighted-loss counterexample
adds 32 labelled balance equations. All passed.

Exploratory simulations at H=N, N=32,128,512,2048, suggest that the
small-buffer protocol may retain most current when B>=2. They do not certify
mixing or stationary error, and prove no large-N bound. All code and output
are retained in exploratory/. Floating-point covariance probes similarly
do not establish a uniform estimate. Do not promote either to a theorem.

No new proof of condensate exclusion, positive limiting occupancy,
phase purity, uniform integrability, the original T_N formula, or the
unrestricted NaSch stationary flow formula was obtained in this run.
