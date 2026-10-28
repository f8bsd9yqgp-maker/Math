# Continue here — integrated-current anchors, run 23

27 October 2026. Parent commit:
`ae78d6f3897ef3560518ac38690d8346ede37273`.

The user's target is the general fixed-density stationary flow. It is
still not closed. This run makes a new step from local gap distributions
to actual integrated-current distributions, without epsilon N restrictions.
Do not re-prove the old scalar Q limit, pushing bound, or dynamic Hamming
coupling, and do not turn distributional convergence into a mean formula.

## New proved mechanism

I_i(n) is actual displacement over n full updates. K_i(t) is the reduced
integrated transfer at i. Full traffic starts stationary and cyclically
averaged. Z(0)=G_0 is its full-braking projected gap vector. Use the
previous Poisson coupling with lambda=-log(1-epsilon).

If initial qualification c_j=0 and no own nonbraking coin occurs through
step n-1, car j never moves. A Poisson-empty site j is also frozen for
the reduced current. For any i<j,

    I_i(n)-I_j(n)=sum_(a=i)^(j-1) [g_a(0)-g_a(n)],

and the same identity holds for K and Z. Matching endpoint gaps and
one common frozen anchor therefore imply exact current equality.

Select the first site j in 1,...,L with no Poisson event through n lambda,
L<N. Candidate selection is independent of the initial state. Its
probability of being initially qualified is at most C, not L*C.

With the preceding coupling error

    Delta_n=8 epsilon(C+2B/p+epsilon)
               [n+lambda n(n-1)/2],

the new exact bound is

    P(I_0(n)!=K_0(n lambda))
      <= (1-exp(-n lambda))^L + C + L(4C+Delta_n).

For fixed t, n=floor(t/epsilon), take L->infinity slowly with L<N.
This proves local finite-dimensional convergence of actual integrated
currents jointly with the gaps, along every stationary local-limit
subsequence N->infinity, H/N->eta in (0,2), epsilon->0. There is no
epsilon N restriction. At fixed bounded times the finite-ring comparison
has error O(epsilon^alpha log(1/epsilon))+exp(-c_T N), with alpha=1/3
generally and alpha=1 below eta=1. No rate of initial-law convergence is
claimed.

## New mean consequences, with exact scope

For the limiting reduced-stationary law mu, put
m=E_mu g_0<=eta, q=mu(g_0>=2), F_mu=m-q. Then

    liminf U/epsilon >= F_mu,
    liminf J/epsilon >= F_mu/(1+eta),
    liminf C/epsilon >= E_mu (g_0-2)^+.

The proof is nonnegative truncation after the current-distribution
limit. It does not show m=eta or q=Q(eta).

Along this subsequence, for any one fixed t>0,

    U/epsilon -> F_mu

is equivalent to uniform integrability of the actual displacements
I_0(floor(t/epsilon)). Both directions are proved in README.
This is not uniform integrability of instantaneous v/epsilon; the latter
normally fails when the normalized mean stays positive while v becomes
rarely nonzero.

## What remains

The fixed-density formula still requires a tail estimate for these
integrated currents and identification F_mu=eta-Q(eta) for all selected
subsequences. The old epsilon N->0 theorem is unchanged.

Potential rare starts in long moving blocks can contribute to the mean
despite probability O(epsilon). The previous pushing bound controls a
first moment but not uniform integrability; its initial dominating
height offset can grow with N. No stationary counterexample or missing
tail proof was obtained. No general fixed-positive-epsilon flow formula
or thermodynamic uniqueness theorem was found.

Literature on strong-overbraking vehicle-jam condensation was checked,
including Miedema/de Wijn/Schall (2014) and the author's thesis. Its
scaling analysis is not the missing stationary tail theorem, and
near-transition-density limits must not be confused with arbitrary
fixed eta. See ATTEMPTS for the precise distinction.

verify.py passed 300,608 full histories, 196,472 full-anchor checks,
27,922 reduced words, 27,200 reduced-anchor checks, and 1,548 exact
probability identities. All analytic claims are internally audited,
not independently peer-reviewed or formally certified. User-facing
prose should remain in a copybox. Preserve proved work on GitHub under
the user's standing authorization.
