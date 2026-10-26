# Proof audit and provenance

## Latest result: local clusters and a uniform one-sided bound, 26 October 2026

The [local-cluster continuation](continuations/2026-10-26-local-clusters/README.md)
proves a full-model error of order `(1-p)N` at bounded vacancy density and
therefore the joint current limit when `(1-p)N->0`. It uses the inherited
projection and corrector, a new disagreement-cluster comparison, and a
pair-minimum workload. A separate
[one-speed comparison](continuations/2026-10-26-local-clusters/UNIFORM_LOWER_BOUND.md)
gives an explicit full-model lower bound valid uniformly in N.
The separate [block drift](continuations/2026-10-26-local-clusters/ACTIVE_BLOCK_GEOMETRY.md)
proves `E b+epsilon E m<=epsilon H` for qualified moving blocks.

New exact audits include 529,232 mixed-cluster mask comparisons, 503,992
two-firing words, 25,240 full-ring cases, 6,840 independent direct
relaxations, 470,240 one-speed order checks, 12,348 exact one-speed
transition weights, 9,996 rational constant checks, and twelve additional
Bernstein certificates. These support, but do not replace, the analytic
proofs. The block drift has 529,232 mask and 55,716 rational expectation
checks. No old stationary or Poisson solver was rerun. General stationary
flow, the phase/condensate alternatives, and unrestricted interchange
remain open; independent peer review remains outstanding.

## Latest result: polynomial full-model rare-braking error, 26 October 2026

The [new proof](continuations/2026-10-26-rare-braking-error/README.md)
constructs the exact full-braking projection and rest time R<=H for H<2N.
It serializes all simultaneous nonbraking triggers from rest as a word of
backchip moves and proves a stationary global nonrest-probability bound.
Composing the inherited reduced current corrector with the projection gives
an explicit full-model current error. The
[sharper continuation](continuations/2026-10-26-rare-braking-error/SHARP_WORKLOAD_BOUND.md)
uses individual and excess workloads to improve that error to
O((1-p)*N+(1-p)^2*N^3) after division by 1-p at bounded vacancy density.
This proves a joint limit when (1-p)*N^(3/2)->0, not unrestricted
interchange of limits.

New exact audits passed 529,232 original-rule update comparisons and
projected-height shift bounds, 18,572 trigger serializations, 510,660
workload perturbation bounds, 38,146 relaxation-step checks, 4,495 rational
bounds, and 101 reachable counterexamples to pathwise acceleration.
Eight Bernstein-polynomial certificates check the new error against four
archived full-model current functions over complete epsilon intervals.
The sharper argument adds a 529,232-mask workload audit, 495,976 dominating
word checks, 88,528 single-coin comparisons, 14,510 commutation checks,
5,394 rational constant checks, and eight further exact interval
certificates. The old stationary and Poisson solvers were not rerun.

The [detailed audit](continuations/2026-10-26-rare-braking-error/AUDIT.md)
separates the new proofs from the inherited current-corrector and reduced
scalar-limit theorems. Full stationary flow, remaining phase/condensate
alternatives, and thermodynamic-first interchange are not claimed solved.
Independent specialist peer review remains outstanding.

## Latest result: explicit first-passage boundary formula, 26 October 2026

The [new proof](continuations/2026-10-26-first-passage-fourier/README.md)
represents the killed three-site unit-chip interior by three walkers on a
circle. An exterior Fourier basis and a translation projection give its
boundary exit kernel explicitly. Pinning the inherited value S_N leaves
N-2 unknowns for T_N; the full Laplace transform requires N-1 unknowns.
The dense numerical arithmetic count is O(N^3), with O(N^2) memory.
No rational bit-complexity bound or numerical-conditioning claim is made.

Exact audits passed 1,705 harmonic-measure equations, 220 interior-duration
identities, 418 original mean Poisson equations, 5,863 exit-multiplicity
checks, and 1,020 discounted Poisson equations. The 11 archived T_N values
are regression fixtures for the new formula. The original full-state
solvers were not rerun. Fourier/FFT coefficients were also compared against
exact coefficients; numerical residuals are not forward-error certificates.

The [detailed audit](continuations/2026-10-26-first-passage-fourier/AUDIT.md)
records the circle signs, the N=3 multiplicities, zero-mode treatment,
matrix invertibility and scholarly status. This is an internally audited
proof and explicit representation, not independent peer review or a solution
of the unrestricted NaSch stationary flow. The thermodynamic scalar
convergence theorem below remains an inherited result.

## Latest result: affine phase gaps and macroscopic backgrounds, 25 October 2026

The [new continuation](continuations/2026-10-25-affine-phase-selection/README.md)
uses the already proved uniform integrability below eta_c to justify lower
supporting-line contacts. It constructs selected positive phases approaching
zero and gives every canonical local limit an explicit positive floor on its
component densities. Thus vacuum mixture components are excluded at every
positive density. A deterministic sliding-window argument proves positive
mass and pile densities on every macroscopic arc, without a uniform mixing
assumption and without excluding a condensate above that background.

The canonically selected pure-phase set is closed. A gap must be an affine
interval of Q, because an interior largest maximum or minimum of Q minus
its endpoint chord would select a new pure phase. This proves selection
wherever Q is not locally affine. It does not prove affine intervals absent,
equate phase existence with canonical selection, or choose a mixture inside
an affine interval.

New exact checks passed: 6,206 contact moment cases, including 2,268 exact
extremal equalities; 467,568 arc cases, including 17,147 low-density premises;
the rational constants; and two obstruction examples. The
[detailed audit](continuations/2026-10-25-affine-phase-selection/AUDIT.md)
records all assumptions and boundaries. These are internally audited
AI-assisted proofs, not independently peer-reviewed mathematics. No old
stationary solver or verifier was rerun.

## Latest result: positivity and critical mass retention, 24 October 2026

The [new continuation](continuations/2026-10-24-positive-occupancy/README.md)
proves q_(N,H)>=min(H/N,1)^3/1152 for N>=3,H>=2. Its new weighted empty-block
certificate is absorbed into a positive exponential-height function. This
excludes vacuum local limits and complete condensation at every positive
density. It is not a claim that every large pile is excluded at every density.

The [phase-selection argument](continuations/2026-10-24-positive-occupancy/PHASE_SELECTION.md)
identifies phase currents with the same Q, proves canonical selection at
largest upper supporting-line contact points, and propagates mass uniform
integrability by stochastic domination. It defines eta_c>1/217: mass is
preserved at all finite eta<=eta_c, and Q is strictly increasing there.
If eta_c is finite, the canonical local law above it is the critical phase
and escaped mean is exactly eta-eta_c. Its finiteness remains open.

The new exact audit passed 3,276 empty-block checks, 2,972 weighted rational
generator certificates, 19,899 parameter checks, eight rigorous exponential
enclosures, and an exact logarithm certificate giving Q(1)>1/218.
[The audit note](continuations/2026-10-24-positive-occupancy/AUDIT.md) details
all sign, boundary, first-moment, and phase-selection issues. No previous
verifier or stationary solve was rerun. Independent peer review remains
outstanding; full below-critical phase selection and the unrestricted
NaSch stationary flow are not claimed.

## Latest result: canonical pile-probability convergence, 24 October 2026

The [new continuation](continuations/2026-10-24-thermodynamic-limit/README.md)
supplies a complete analytic proof of the scalar fixed-density limit, with
uniform-on-compact error O_R((log(N)/N)^(1/4)). It proves the oscillation
estimate that was left open in the immediately preceding height comparison.
The mechanism is an averaged-height Doob martingale, a deterministic spatial
sandwich, and localization to auxiliary rings with total mass O(t).

The [new internal audit](continuations/2026-10-24-thermodynamic-limit/AUDIT.md)
checks semigroup commutation on affine heights, the sum of predictive jump
sizes, helical blocks, phase rounding, dependent auxiliary copies, winding
errors, and summation over all road sizes. The new exact verifier passed
7,724,727 predictive-jump checks, 1,194,264 commutation checks, 2,187 phase-mean
checks, 132,696 spatial-sandwich checks, and 1,131,601 rounding checks.
No old verifier or simulation was rerun to establish the result.

This is internally audited working mathematics, not an independent referee
report or formal proof certification. The entire stationary-measure limit,
condensate characterization, an explicit Q formula, the T_N formula, limit
interchange, and the unrestricted NaSch stationary flow remain unresolved.
The older audit entries below retain their historical scope and dates.

## 24 October continuation: sharp drift and recurrent support

The new continuation supplies an all-mass reduction to 320 exact integer
inequalities, proving `q <= 5H/(17N)` for `N >= 3`. The N=3,H=3 exact
stationary law establishes sharpness over that finite-system class. The
N=2 exception is explicit. The bounded potential has range [0,15N], full
jump bound 14, and full-minus-partial jump bound 14. Those constants are
independently audited; the associated finite-time and modified-bond bounds
are proved in the note. They do not compare arbitrary stationary sizes.

The short-time covariance counterexample checks all 341 words of length
at most four and has a direct analytic proof. It refutes preservation of
negative dependence, not stationary negative dependence. The support proof
uses explicit reverse legal edges, each checked by the original forward
map: 31,733 paths and 552,001 edges pass, as do 45 independent forward
reachability graphs. Its consequence for trace matrices uses nilpotence
proved by a Vandermonde argument, allowing signed and complex matrices.
The low-density dimension bound applies to the stated local cancellation
ansatz; it is not a universal lower bound for all conceivable representations.

The rank-one-zero obstruction is certified by the full 462-state rational
stationary law at N=H=6, with all balances checked. Discovery LP outputs,
uncertified longer-block coefficients, and unsuccessful finite searches are
kept separate. The main fixed-density limit, mass retention, and phase
selection remain open. No external peer review or priority determination
has occurred.

The earlier audit record follows unchanged.

Audit date: 22 October 2026. This is an internal audit by the AI research
assistant, not an independent human referee report, formal proof-assistant
verification, or priority review.

## Result of the audit

The arguments in `density_phases_proof.md` support the stated structural
theorems under their explicit assumptions. The main canonical convergence
problem remains open. No numerical convergence claim is used as a proof.

The publication makes the finite-first-moment assumption explicit everywhere
deterministic density is used. It supplies full proofs of the ordering and
strict-pile-detection prerequisites, and does not require the reader to
accept any theorem from an inaccessible earlier archive.

| Step | Reason it is valid | Boundary of the conclusion |
| --- | --- | --- |
| Infinite-line graphical construction | A dependency crossing k adjacent sites in time t requires an ordered clock chain; its probability is at most a constant times t^k/k! | This controls fixed times, not the interchange of infinite time and road size |
| Moment-free stationary order | Bounded capped discrepancy identity, nonnegative Fatou limit, and a positive-probability finite gathering word | Every coordinate must be finite; the conclusion is about stationary common-clock couplings |
| Stationary coupling from time averages | Fixed marginal distributions give tightness; Feller continuity passes invariance | No density moment is passed across varying canonical sizes |
| Direction of the order | Conditioning on a spatially invariant order event preserves deterministic spatial densities; integrability gives the corresponding conditional means | An expected density alone is insufficient |
| L1 synchronization | Discrepancy expectation decreases; time-average limits are ordered; fixed integrable marginals provide uniform integrability | No uniform synchronization rate over densities or system sizes is obtained |
| Representation by past clocks | Conditional terminal replicas are independent stationary seeds under common clocks; vanishing conditional variance and martingale convergence remove seed randomness | This does not exclude additional global randomness in limits of finite rings |
| Density disintegration | Boundary-current conservation preserves spatial density in L1; conditional laws are stationary and have their specified densities | Existence of positive-density phases at all densities is not proved |
| Phase diagnostic | Conditional ergodicity gives the block-variance limit; strict pile detection makes q injective | Uniform canonical block-variance decay is not proved |

The note keeps three different statements separate:

1. A stationary law at a deterministic finite density, **if it exists**, is
   unique and mixing.
2. Every existing finite-mean stationary law has a unique density-phase
   decomposition.
3. Finite rings at a prescribed density select the same limiting pile
   probability along every increasing sequence of sizes.

The first two are proved here. The third is not.

## Exact computational audit

Executed successfully with:

```sh
python3 nasch/code/verify.py --output nasch/results/verification.json
```

| Check | Cases | Outcome |
| --- | ---: | --- |
| Capped donor-split identities | 5,832 | PASS |
| Capped absolute-value subadditivity | 24,642 | PASS |
| Local discrepancy quadruples | 10,000 | PASS |
| Coupled ring discrepancy transitions | 9,457 | PASS |
| Two-copy gathering words | 2,891 | PASS |
| Block boundary-current identities | 54,054 | PASS |
| FIFO initial states and finite event words | 97,650 | PASS |
| Exact stationary chains, N=4 and H=2,…,8 | 7 chains | PASS |

All arithmetic used for finite stationary probabilities is rational. Each
computed vector is checked against every equation of the original generator,
not merely the square system used to solve for it. It is also checked for
normalization and nonnegativity. The finite-state uniqueness proof is in
Section 7 of the note.

All outputs already present in the run-8 audit reproduced unchanged. The
publication adds checks of the bounded capped identity, an explicit optional
output path, and a guard against Python's `-O` option disabling assertions.
The simulation used during the earlier exploration is not included as proof
evidence. No mixing time, confidence interval, or thermodynamic extrapolation
is claimed.

## Provenance and reproducibility

The order and strict-detection argument originates in this project's run 6;
the synchronization, clock representation, and density decomposition were
developed in run 8. The GitHub note reorganizes those arguments into a
self-contained proof. It clarifies assumptions and includes a direct proof
of finite-ring uniqueness and stationarity of canonical local limits.
These are claims within this research record; originality relative to all
published mathematics has not been established.

The earlier full research archive is preserved separately under the filename
`NaSch_Density_Phases_Research_Package_2026-10-21.zip`, with SHA-256:

```text
a52a34a1c78f4a96959e15307ccf6cc7b0549fb2b38a82690359c806521bd6cc
```

Source files consulted for this publication:

| Earlier filename | SHA-256 |
| --- | --- |
| `NaSch_Moment_Free_Order_And_Upper_Process_2026-10-20.md` | `db7a10d36ecc56be7c9b6fcf503fc8939df7bdda52ff9e920d3002395062f58f` |
| `NaSch_Density_Phases_And_Synchronization_2026-10-21.md` | `a8a3364d145567ac57f54be82fabb2f9113c060630aac909cace710a1a01fb93` |
| `synchronization_audit.py` | `ea5beac238efa719905b916f14330f15c585a343fd3c0b616c37b0699f7c86f6` |
| `exact_support.py` | `2b8a6f04c9419bc6039ab65c51de66211cea09966537fab4de02c6dc1ab2d843` |

`MANIFEST.json` records byte lengths and SHA-256 hashes of the files actually
published in this directory, excluding the manifest itself. It identifies
the submitted content, not the correctness of the proofs.

No claim is made that the original first-passage problem, the entire NaSch
stationary current, condensation exclusion, or the required canonical
selection estimate has been solved. A counterexample to a finite ansatz is
not a counterexample to the thermodynamic limit.

## Continuation of 23 October 2026

The [buffer-coupling continuation](continuations/2026-10-23-buffer-coupling/README.md)
adds complete finite-network proofs, an explicit two-block stationary loss
bound, and exact counterexamples to two proposed comparison shortcuts. Its
own manifest records the associated proof, verifier, certificates, and
separately labelled exploratory programs and outputs.

The exact audit passed: 2,548 labelled balance equations and 340 quotient
equations for eight clock-correlation chains; 32 additional labelled balance
equations for the weighted-loss counterexample; 3,900 synchronized-cover
event identities; 9,860 physical buffer-event checks; 3,480 corrector-loss
identities; 1,740 quadratic-generator identities; and 892 positive-loss
support checks. These checks verify the finite algebra and certificates.
They do not establish the missing sublinear-reserve estimate or the
thermodynamic limit. The proofs remain internally audited working mathematics,
not independently peer-reviewed results.

## Continuation of 23–24 October 2026

The [capped-transfer note](continuations/2026-10-23-capped-bonds/README.md)
proves a stationary current comparison by explicitly subdividing selected
generator edges into legal physical moves. Its auxiliary stationary law is
written down and checked analytically. The resulting reciprocal-current
error is at most the sum of reciprocal caps; the site-averaged pile
probability has a corresponding uniform bound. The proposed capped-chain
convergence and capped-block gluing steps remain unproved.

The standard-library rational audit passed for 85 capped chains: 1,180
stationary balance equations, 1,348 auxiliary-protocol balance equations,
168 legal intermediate chunks, and 10,392 local checks. It also verifies
normalization, nonnegativity, equality of bond currents, the sharpened
current comparison, the overflow identity, and the averaged pile bounds.
The continuation includes a complete analytic proof of the flat negative
branch of the pile-occupation pressure. It does not claim that differentiating
that limiting branch gives the thermodynamic pile probability.

The eight-ring threshold-covariance probe is labelled exploratory. Neither
negative association, uniform mass integrability, nor the main fixed-density
limit is established by these calculations. A separate manifest preserves
the proof, handoff, exact certificates, and exploratory output.

## Finite-time height comparison, 24 October 2026

The [height comparison](continuations/2026-10-24-height-comparison/README.md)
proves an exact Poisson backward-path identity, a finite-time bracket for
stationary current, and an explicit current comparison across ring sizes.
It proves a conditional canonical convergence theorem: a specified uniform
sublinear bound on balanced-start expected height oscillation implies
all-size convergence, with a quantitative rate. **The hypothesis is not
proved.** No absence of condensates or mass uniform integrability is assumed.

The note also proves the exact Strahler-rank conjugacy and a family of
linear-size counterexamples to a maximum-envelope comparison. The
counterexamples are pathwise; they do not invalidate an expected oscillation
bound or canonical convergence.

The standard-library audit passed 651 local cases; 4,995 original-generator
states and 27,018 transitions; 26,212 clock words with 131,060 initial-state
and word pairs; 78,255 coupled-ring word cases; 54 exact rational current
brackets; and 303 explicit envelope counterexamples. The all-parameter
arguments are given separately in the proof. Finite tests are not an
asymptotic argument.

A separate fixed-seed C++ experiment samples exact finite times from balanced
initial data, with no burn-in. Its observed decay of range/time is labelled
exploratory and is not used to justify the conditional theorem's hypothesis.
Proofs, code, exact results, the CSV, and the handoff have a separate manifest.
