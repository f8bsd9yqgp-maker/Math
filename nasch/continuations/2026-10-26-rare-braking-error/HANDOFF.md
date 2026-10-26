# Continue from the quantitative full-model rare-braking bound

26 October 2026. Research run 19. Parent before publication:
`d940b3834c3b6c85f33dfcdc36a862fe6b1d797d`.

Read SHARP_WORKLOAD_BOUND.md first, then README.md, AUDIT.md and
CLOSURE_ATTEMPTS.md. Do not restart the previous
scalar convergence, phase-selection, or first-passage Fourier work. The
user requests chat prose in a text copybox and has authorized publishing
proved results to the existing GitHub repository.

## Strongest result: sufficient exponent improved from 3 to 3/2

The later part of the same run proves, if H/N<=R and
epsilon*max(N,H)<=1/2,

```text
|J(1-epsilon)/epsilon-N*F/(N+H)|
 <= (12*R^2+3*R)*epsilon*N
    +(6*R^3+10*R^2)*epsilon^2*N^3.
```

Hence the full-model joint limit holds whenever epsilon*N^(3/2)->0.
This supersedes the initial sufficient condition epsilon*N^3->0 below.
The exponent is not claimed optimal; thermodynamic-first interchange is
still open.

New ingredients: for projected gaps G and any coin mask, the projected
coordinate increase is at most B=sum xi_i*d(G_i). The individual remaining
lifetimes r_i=a_i+ell_i give stationary bounds

```text
M=E[number active] <= epsilon*H*(1+(N-1)*epsilon)/(1-epsilon*H),
E(number active-1)_+ <= 2*epsilon*H*M+epsilon^2*H*(N-1).
```

A negative projected increment requires a coin at an old qualified site
with gap 2 and a qualified leader. Rest-state serialization compared with
a uniformly random order of marked sites gives a linear, not quadratic,
size error: (5*N-1)*epsilon^2*F/2. Exact single-coin and arbitrary-mask
word comparisons complete the sharper current bounds. See the complete
analytic proof; do not replace these comparisons by unproved full-model
monotonicity.

The new integer audit checks 529,232 masks for each main projection and
workload inequality, 495,976 dominating words, 88,528 single-coin cases,
14,510 isolated-word commutations, and 5,394 rational constants. Eight
additional Bernstein certificates check the sharpened current inequalities
against the four archived rational currents over entire epsilon intervals.
Both new audit scripts passed. No old stationary solver was rerun.

ZERO_NOISE_LIMITS.md also proves that every TI stationary p=1 law is a
mixture of all-rest and all-speed-one (all gaps>=2) laws. A local joint
stationary limit with H/N->eta has moving-class weight alpha<=eta/2 and
unscaled U->alpha. If eta<2 and that limit is spatially ergodic, alpha=0.
Spatial ergodicity of unrestricted limits is NOT established, and even
alpha=0 would not identify U/epsilon. This is not a noncommutation example.

## New theorem for full parallel-update NaSch

Let epsilon=1-p, N>=2, 1<=H<2N, and let F_(N,H) be the reduced backchip
current. For any full-model stationary law, with U its mean velocity per
car, if D=1-epsilon*H*(N-1)>0,

```text
|U/epsilon-F| <= epsilon * [
    H*(N*(H+1)+F)/D + (N-1)^2*F
].
```

For H/N<=R and epsilon*H*(N-1)<=1/2,

```text
|J_(N,H)(1-epsilon)/epsilon - N*F/(N+H)|
    <= (4*R^2+3*R)*epsilon*N^3.
```

Hence for every sequence N->infinity, H/N->eta in (0,2),
epsilon>0 and epsilon*N^3->0,

```text
J_(N,H)(1-epsilon)/epsilon -> (eta-Q(eta))/(1+eta).
```

This is a restricted simultaneous limit, not thermodynamic-first
interchange. The general fixed-p stationary flow remains open.

## Mechanism and definitions that must be kept straight

The exact velocity rule is

```text
w_i = 1[v_i>0 and g_i>=2] + xi_i*1[g_i>=1],
g_i' = g_i+w_(i+1)-w_i,
```

where xi_i=1 means no random braking. Under all future xi=0, put
c_i=1[v_i>0,g_i>=2]. Along the consecutive run of c=1 starting at i,
ell_i=sum(g_j-1). Car i's displacement by time t is min(t,ell_i).
The exact rest time R is zero at rest and otherwise 1+max ell_i<=H.
The full-braking projection of lifted heights is P(h,v)=h+ell.

From rest, any simultaneous trigger mask followed by full relaxation is
exactly a word of backchip moves: original singleton triggers first, then
triggered large-gap blocks upstream first. Its post-first-step rest time
is bounded by sum_i xi_i*d(g_i).

The stationary probability A that SOME car is moving obeys
A<=epsilon*H/[1-epsilon*H*(N-1)]. This is a global probability.

Use the inherited monotone current corrector Phi with
sum_i [Phi(T_i h)-Phi(h)]=F and every increment in [0,F]. Set
Psi(h,v)=Phi(P(h,v)). Full-braking steps have zero Psi increment.
Stationary E Delta Psi=U because Psi-average(h) is a finite-state function.
At rest the drift differs from epsilon*F by at most
(N-1)^2*epsilon^2*F. At nonrest its absolute drift is bounded by
epsilon*N*(H+1). These facts prove the displayed error.

## New obstruction to a stronger shortcut

For every N>=6, H=N, M=N-3, take gaps (1,2,M,0,...) and velocities
(0,1,1,0,...). This is reached from resting gaps (0,2,M+1,0,...) by
nonbraking at sites 1 and 2 (zero-based indices).

Full braking then gives displacements M at site 1 and M-1 at site 2.
One extra nonbraking decision at site 1 gives displacement only 2 there,
leaving every other eventual displacement unchanged. The loss is N-5.
Thus extra nonbraking is not a monotone perturbation of the relaxed
trajectory, even up to a constant independent of N.

This is not a counterexample to stationary current monotonicity or limit
interchange. It rules out that specific pathwise comparison.

## New audit only

verify.py uses integers/Fraction, without third-party libraries or old
stationary/Poisson solvers. All checks passed: 18,572 activity states,
38,146 relaxation steps, 18,572 serializations, 529,232 arbitrary-coin
updates and projection bounds, 510,660 workload perturbation bounds,
4,495 rational bounds, and 101 reachable acceleration counterexamples.
Machine-readable outputs are under results/.

verify_flow_bounds.py supplies eight exact Bernstein-polynomial certificates
against four archived rational full-model current formulas. They verify the
new error on entire epsilon intervals, without rerunning the old solves.

These are internally audited AI-assisted proofs, not independent peer
review. The corrector and reduced scalar limit are inherited assumptions
with complete earlier project proofs; they were not reverified here.

## Remaining work

No explicit general Q, affine-interval selection theorem, critical-density
decision, fixed-p thermodynamic flow formula, or unrestricted limit
interchange was obtained. The sharpened bound cannot be used with fixed epsilon
and N->infinity.

The strongest next target is a local replacement for the global rest-state
decomposition, giving an error tending to zero with epsilon uniformly in N.
Positive-background and phase-selection results for reduced canonical laws
do not automatically describe stationary full-model laws or the biased
environment seen from a large pile. Preserve those distinctions.
