# Continue from the exact mean-flow defect identity

27 October 2026. Research continuation 24. Parent before publication:
`a4c2e15e77bf4770ca9a0a939a95a782794fe72e`.

Read README.md and AUDIT.md here first. The user requests copyboxes for
chat prose and has authorized publishing proved work in the existing
GitHub repository. Do not restart the completed current-anchor or
canonical reduced-limit work.

## Newly proved

For any cyclically averaged full stationary law, N>=2, epsilon=1-p,
write a=1{v>0}, c=a*1{g>=2}, C=E c, S=E c_0 c_1, B=C-S,
q=P_full(g>=2), W=E[c(g-1)], and Y=(1-c)g. Then exactly

```text
U/epsilon = eta-q-W+S/epsilon+R
          = E Y-q+S/epsilon+C+R,
0 <= R <= C+2B+epsilon.
```

R is an explicit sum of five nonnegative local terms in README equation
(2). The proof is an exact drift of c(g-1), retaining the gap-two
clipping correction. Combining B<=epsilon eta with the old arrest bound
gives C+R->0 uniformly in size. This is a correlation identity, not a
closed flow formula.

For H<2N, sample the ordinary stationary state. If car zero is resting
and has a nonempty gap, force its first coin to be nonbraking, then run
the original process until that car's first zero movement. Let A be
the distance in that episode; set A=0 for an ineligible initial state.
Then exactly

```text
E A = U/epsilon,
P(A != d(g_0)) <= 2C+2epsilon(eta+1),
d(g)=g-1{g>=2}.
```

This is an entire-episode total-variation comparison, using a frozen
leader and only 2d(g)+1 coin decisions. It does not control the reward
on the failure event. The unnormalized eligible experiment, with its
zero outcomes, is essential to E A=U/epsilon.

With e=1{v_0=0,g_0>=1}, the mean gain G=E[A-e d(g_0)] is nonnegative
and obeys

```text
G = S/epsilon+R+P(v_0>0,g_0=1),
0 <= G-S/epsilon <= C+2epsilon(eta+1).
```

## Exact alternatives for every local limiting law

Along N->infinity, H/N->eta in (0,2), epsilon->0, let mu be a local
stationary full-gap limit. It is reduced-stationary by earlier work.
Put m=E_mu g, q*=mu(g>=2), delta=eta-m. Along further subsequences
with W->w and S/epsilon->kappa in [0,infinity],

```text
0 <= w <= delta,
U/epsilon -> (m-q*)+(delta-w)+kappa.
```

The two defects are nonnegative. Delta-w is exactly the escaped
unqualified gap mass. Kappa is the adjacent-qualified-pair contribution,
equivalently the limiting mean episode amplification. It is finite
below eta<1 by the previous pushing bound, but need not be zero by
anything proved here.

The following are equivalent along the chosen local-limit sequence:

1. U/epsilon -> m-q*.
2. The variables A are uniformly integrable.
3. The variables Y=(1-c)g are uniformly integrable and S=o(epsilon).
4. Actual displacement over floor(t/epsilon) updates is uniformly
   integrable, for one fixed t>0.

If full gap means are retained, then condition 3 reduces to the single
estimate S=o(epsilon). Gap mean retention itself remains unproved for
unrestricted full-model limits.

## New localization of the pair defect

Let M_1 be the vacancy mass of the qualified run starting at car 1.
For every L>=1,

```text
P(c_0=c_1=1,M_1<=L) <= L epsilon^2(2eta+1) p^(-L).
```

The pair birth rate is at most epsilon^2(2eta+1). Freeze just the first
initially unqualified leader for L steps, at probability p^L. Its finite
vacancy supply forces at least one pair loss if M_1<=L, whatever all
other coins do. Stationary loss rate equals birth rate. Do not replace
"at least one loss" by an endpoint condition: the pair may reform.

For bounded density,

```text
limsup (1/epsilon) P(c_0=c_1=1, epsilon M_1<=a)
 <= a(2R+1) exp(a).
```

Thus nonzero first-order pair defects require run vacancy mass of order
1/epsilon or more. Since ell_1<=M_1<=2ell_1, their remaining coast is
of this order as well. This does not necessarily mean a macroscopic
road-size pile. Pair episodes would also have mean duration at least
of order 1/epsilon.

Taking L=H proves S<=H epsilon^2(2eta+1)p^(-H) and
U/epsilon<=eta+1+epsilon H(2eta+1)p^(-H). Normalized current is therefore
bounded if epsilon H stays bounded, including a nonzero finite scaling;
its coefficient is not identified by this bound.

## Audit and remaining work

The new standard-library verifier passed 2,601 coefficientwise local
drift identities valid for all epsilon, 10,404 direct local masks,
5,202 remainder certificates, 603 mass/reward identities, 38,496 episode
histories, 4,459 isolated-episode reductions, and 28,500 combinatorial
time-reward words. A further 5,832 exhaustive reachable-state transitions
check the single-frozen-boundary extinction for 236 initial states.
No old stationary or first-passage solver was rerun.
These proofs are not independently peer reviewed.

Next targets are genuinely specific: prove or refute unqualified-gap UI
and S=o(epsilon) for stationary full-model sequences; identify the selected
local flux with eta-Q(eta); determine the unrestricted fixed-positive-noise
thermodynamic flow. Do not infer pair independence from independent coins,
or infer mean convergence from the new episode total-variation estimate.
No complete flow formula or stationary counterexample is established.
