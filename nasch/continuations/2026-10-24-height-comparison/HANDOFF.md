# Continue from the finite-time comparison

24 October 2026. **The fixed-density limit remains open.**
This follows the sharp-drift/support publication at commit
`4319ebfcaa7a8d04250e79ae4c6dbe76335d7456`. Do not reclassify its results as
new in the next run. The current new proof is in this directory's README.

## Main advance, with the missing hypothesis separated

For balanced initial heights ell_i=floor((H/N)i), let U_i(t)=h_i(t)-ell_i and
R_(N,H)(t)=E[max_i U_i(t)-min_i U_i(t)]. This is a finite-time expectation
from deterministic initial data, not a stationary expectation.

1. The backward right-going clock path from (0,t) has exactly Poisson(t)
   steps Z, including on finite rings after winding. The exact identity is
   h_0(t)=floor((H/N)Z)-sum of retention indicators along that path.
   In particular 0<=h_0(t)<=(H/N)Z. The entire dependency diagram lies in
   lifted sites 0,...,Z. The retention marks are NOT independent.
2. |F_(N,H)-E U_0(t)/t|<=R_(N,H)(t)/t, proved by repeating finite clock
   blocks and applying height monotonicity and vertical homogeneity.
   No assumption that the finite-time law is near stationarity is used.
3. For theta=H/N, phi=K/M, L=min(N,M), and Z_t~Poisson(t):

   |q_(N,H)-q_(M,K)| <= 2|theta-phi|
       +[R_(N,H)(t)+R_(M,K)(t)+1]/t
       +(theta+phi) P(Z_t>=L-1).

   At equal densities, omit both the density term and 1/t. In current
   variables the density-difference coefficient is one instead of two.
4. **Conditional theorem, not a proved estimate:** If for fixed eta there
   are C<infinity, delta in (0,1] with

   R_(n,floor(eta*n))(t)<=C*t^(1-delta)
   for every large n and sqrt(n/2)<=t<=sqrt(n),

   then the canonical q converges along every integer sequence, with error
   O(n^(-delta/2)). Compare n<=m<=2n at t=sqrt(n), then sum over doublings.
   The finite-time oscillation bound is the exact missing lemma in this route.
   Neither stationary mass UI nor absence of moving condensates is assumed.

## Additional exact structure and obstruction

x_i=h_i-i conjugates the height update to
S(a,b)=max(a,b)+1{a=b}=max(a,b,1+min(a,b)).
This is a weighted Horton–Strahler/register-rank operation. At H=N and flat
initial x=0, a finite clock word unfolds to a binary tree with zero leaves.
Its branches share clocks and ancestors; it is not an independent branching
model and standard Galton–Watson rank limit theorems cannot be imported.

There is an explicit family, at N=H=4r and initial gaps all in {0,1,2}, where
T_w(hA vee hB)_0 - max(T_w(hA)_0,T_w(hB)_0)=r.
Thus no universal bounded-error maximum-envelope identity, or o(N) pathwise
replacement uniform over words, is possible. The construction uses
n=2r-1,k=r-1,N=2n+2 and periodic profiles

 A_i=-max(0,n-k-|i-n|),
 B_i=-max(0,k+1-min(i,N-i)).

Their maximum is zero. Apply the triangular clock word
(0,...,n-1; 0,...,n-2; ...; 0). The final x_0 values are k, n-k-1, n.
This does not disprove an expectation bound: the chosen word can be rare.

## Verification and experiment

`verify.py` uses only the Python standard library and the repo's existing
exact_support.py. All checks passed: 651 local cases; 4,995 generator states
and 27,018 events; 26,212 clock words and 131,060 initial-state/word pairs;
78,255 coupled-ring cases; 54 exact rational current brackets; 303 envelope
counterexamples, including a verified defect of 51. Results are saved.

The C++ experiment samples finite times exactly via a Poisson(Nt) event count.
At t=sqrt(N), N=64,...,16384, and eta=0.5,1,1.5, the empirical mean R/t
decreased. The CSV records sample counts, standard errors and seed
202610240701. This is not a proof of a uniform exponent, not a certified
confidence interval, and not a stationary simulation. It tests only one time
per size, whereas the conditional theorem requires a time interval.

## Other attacks considered in this continuation

* A logarithmic loss bound for joining two rank trees is false. A complete
  binary tree of depth 2r-1, split into leaves with at most r-1 right turns
  and the complementary leaves, has rank 2r-1 but each pruned color tree
  has rank r-1. The actual admissible-ring construction above strengthens
  this observation and is the result to retain.
* The rank operation is a max-min operation. General max-plus growth,
  independent-tree, ballistic-deposition, or stochastic homogenization
  theorems have not been shown to apply. No shape theorem was imported.
* A naive bounded-difference argument in individual clock events fails:
  one extra event can copy a large upstream height, producing an unbounded
  height change. Any concentration proof needs more than this argument.
* Existing stationary order/uniqueness results still do not identify the
  canonical subsequential density mixture or prevent escaped mean mass.

Next target: prove the finite-time oscillation estimate, or a summable
variant sufficient for the same dyadic argument. A single simulation or a
fixed-time local limit does not supply the required uniform estimate.
The cap, buffer, corrected-dilation and exiting-rank routes are still open.
