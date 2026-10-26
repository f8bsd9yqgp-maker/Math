# Continue after the local-cluster theorem

26 October 2026. This is the next continuation after GitHub commit
`9e7323bf9c323a581f4a304964cffb26614ba92d`. Read README.md,
UNIFORM_LOWER_BOUND.md, AUDIT.md, and CLOSURE_ATTEMPTS.md in this folder.
The user requests that chat prose be placed in a copybox and has authorized
publishing complete audited results in the existing GitHub repository.

## New stronger joint-limit bound

For 0<epsilon*max(N,H)<=1/4, 1<=H<2N, H/N<=R, and any stationary full
NaSch law,

```text
|J(1-epsilon)/epsilon - N*F_(N,H)/(N+H)|
  <= (5*R/2 + 65*R^2 + 20*R^3)*epsilon*N.
```

Therefore the full-model coefficient converges to `(eta-Q(eta))/(1+eta)`
along every joint sequence with epsilon*N->0. The previous sufficient
condition was epsilon*N^(3/2)->0. Neither condition covers a fixed
epsilon as N grows.

The new idea: compare the actual full-braking projection after one mask
to a rest-started projection from the current projected profile P under
the same mask. The outputs differ only on connected components of
`{qualified cars} union {marked cars}` containing both types. A two-firing
word bounds the corrector difference by 4F times the size of this set,
including a separate full-ring case. Fresh coins give conditional expected
size <=epsilon*(k^2+6k), where k counts all stored-moving cars. The new
pair-minimum workload potential bounds E[k(k-1)]. The analytic proof and
new exact audit are in this folder.

## New unconditional lower bound on the full-model flow

For every N>=2, H>=1, 0<epsilon<1, and any stationary full-model law,

```text
J/epsilon >= N*H / ((N+H)*(N+H-1)).
```

The proof couples ordered full heights below by a one-speed parallel
exclusion process with the same coins and proves that process's explicit
gap product law. This is an all-size result with no epsilon*N restriction.
There is a sharper explicit lower liminf at fixed epsilon in the note.
It does not provide a matching upper bound or identify the full current.

## What is still missing

The comparison error above controls the **global** number of active cars
and diverges with N for fixed epsilon. A thermodynamic-first theorem needs
a genuinely local, size-uniform estimate, or another characterization of
the stationary full model. A useful target is a bound on the corrected
influence of mixed clusters in terms of their density and local geometry,
instead of total size; the corrector's influence weights can correlate
with cluster location, so translation invariance alone does not justify
replacing them by their mean. Such a bound has not been proved here.

The reduced scalar Q exists by the inherited result. Explicit Q,
selection inside possible affine intervals, finiteness of its critical
density, and moving-condensate behavior remain unresolved. Full-model
coupling with one-speed exclusion gives only a lower bound. Do not describe
either new result as a solution of general fixed-p flow or unrestricted
interchange.

## Exact audit

The new audits include 529,232 mask comparisons, 503,992 explicit
two-firing words, 25,240 full-ring cases, 6,840 independent direct
relaxations, 470,240 one-speed ordered comparisons, 12,348 rational
product-invariance transitions, 9,996 rational constants, and eight
Bernstein interval certificates, plus four certificates for the finite
one-speed comparison on the whole p range. Raw counts and inputs are in results/.
No old stationary or Poisson solver was rerun. The proofs have not been
independently peer-reviewed.

## Size-uniform geometry of qualified moving blocks

ACTIVE_BLOCK_GEOMETRY.md proves, with c_i=1[v_i>0,g_i>=2],
m=sum c_i and b=sum c_i*(1-c_(i+1)), that every stationary law with
H<2N satisfies

```text
E[b] + epsilon*E[m] <= epsilon*H.
```

For shift-invariant laws, the chance a qualified site belongs to a block
of length at most s is at most s*epsilon*(H/N-E[m]/N). Hence if U has a
positive lower limit as epsilon->0, a positive fraction of car labels
must lie in qualified blocks whose length is at least order 1/epsilon.
This need not be macroscopic relative to N and does not rule out or
prove vacancy-mass condensation. The drift audit passed 529,232 new
mask checks and 55,716 exact conditional expectation checks.
