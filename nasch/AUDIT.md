# Proof audit and provenance

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
