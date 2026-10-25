# Internal audit of the 25 October phase-selection continuation

This is the assistant's own proof audit, not an independent referee report
or formal verification. The inherited results are linked in README Section 1;
their numerical audits were not rerun and are not counted as new work.

## Analytic checks

1. **Correct model.** The generator is the unit-rate continuous-time backchip
   process. No statement about fixed nonzero braking in NaSch is inferred.
2. **Definition of selection.** C requires convergence along every sequence
   H_N/N->eta to a deterministic-density phase. Existence of an infinite-line
   phase alone is not substituted for this stronger condition.
3. **Component densities are initially only mean-bounded.** A pointwise bound
   R<=b is obtained only after stochastic domination by a selected pure phase
   of density b. Ordered spatial averages establish the bound.
4. **Means in the minimum argument.** Uniform integrability is already proved
   below eta_c, including every c<=b_* used here. It gives E R=c. Without this
   equality, the lower-contact argument is invalid; see the exact example below.
5. **Largest contact matters.** After extremality restricts R to a contact set,
   choosing its largest point bounds R above by its own mean. An arbitrary
   interior member of a flat contact set would not suffice.
6. **Both signs of curvature.** A non-affine curve can lie below its chord.
   The gap proof therefore uses a minimum in that case, not only a maximum.
7. **A selected upper barrier exists.** The ratio maximum b_* is a previously
   selected upper supporting-line contact. It is finite, with
   1/217<b_*<218. Its existence is not assumed at a prescribed density.
8. **Rounded constants are not used.** The bounds 218/2^20<1/1152 and
   1152/2^20<1/4 are exact rational comparisons. The chosen contact lies
   strictly below one before the cubic small-density lower bound is used.
9. **Target density need not retain its mean.** Domination at the small
   selected density works at every larger target eta. Thus the no-vacuum
   component result and macroscopic-arc result also apply above a finite
   critical endpoint. Uniform integrability is used at the auxiliary small
   density, not silently assumed at the target.
10. **Macroscopic arcs use all window starts.** Checking a single partition
    into L-blocks would introduce an uncontrolled factor L. The proof counts
    all internal sliding windows and obtains the factor 4/epsilon, independent
    of L. Boundary arcs, including arcs wrapping around the ring, are covered.
11. **Order of limits.** At each fixed L, finite canonical order and local
    selection bound the bad-window probability. Only afterwards does L tend
    to infinity by ergodicity of one fixed phase. No uniform mixing rate or
    exchange of limits is asserted.
12. **Closedness is stronger than weak convergence of mixing laws.** The
    ordered phases have coordinate L1 distance equal to their density
    difference. This gives a uniform error for separated cylinder correlations
    and proves that their limit is mixing. Mere weak convergence would not.
13. **All-size selection at a limit density.** The finite estimate (16) compares
    arbitrary H_N/N->c with floor(c_j N) in the same ring. It proves the full
    canonical statement, not only one chosen subsequence or only floors.
14. **Gap endpoints.** Closedness and the cofinal upper contacts give finite
    selected endpoints on both sides of any gap. The finite critical endpoint
    is already selected. No gap can extend to infinity without a barrier.
15. **Affine is necessary, not sufficient.** The proof confines failures of
    pure selection to affine intervals. It neither creates such a failure nor
    proves nonconvergence anywhere. It does not specify a two-phase mixture
    in an affine interval when other phases might exist there.
16. **Condensate scope.** Positive mass and pile densities on every macroscopic
    arc rule out a macroscopic depleted background as specified in (5). A
    large pile coexisting with a positive background is still possible outside
    the previously proved uniform-integrability regime.

## New exact computations

Run `python3 verify.py` from this directory, or invoke it by absolute path.
Only the Python standard library is required; there is no random sampling.

* 6,206 finite rational moment checks, containing 2,268 exact extremal-contact
  cases, of which 208 have an interior selected contact.
* 467,568 cyclic-arc checks, including 17,147 arcs satisfying the low-density
  premise of the deterministic counting lemma.
* Exact rational checks of all numerical constants in the small-phase proof.
* Two exact obstruction examples below.

All passed. The output is in results/verified.json. These finite checks audit
the algebra and the counting implication; the arbitrary-density and
infinite-volume assertions follow from the analytic proofs.

## Exact example: a lost mean invalidates minimum selection

At density nodes 0,1,2, set Q=(0,1/8,3/8) and s=3/16. The function Q(r)-sr
has its unique minimum at r=1 among these nodes. Yet the distribution with
weights (2/3,0,1/3) has E R=2/3<1 and E Q(R)=1/8=Q(1). It is not concentrated
at the minimizing density. Thus the equality of means in (8) is indispensable.
This is an algebraic example, not a proposed backchip current.

## Exact example: affine current data do not select a local law

For rho in [1/2,1], let nu_rho be the iid law on site masses 0,1,2 with
probabilities (1-4rho/5,3rho/5,rho/5). These laws are mixing, are ordered in
rho, have mean rho, and have pile probability rho/5.

At eta=3/4, compare nu_(3/4) with
(nu_(1/2)+nu_1)/2. They have the same mean, pile probability, and even the
same complete one-site law (2/5,9/20,3/20). Their two-site pile probabilities
are 9/400 and 1/40, respectively, differing by 1/400.

Both the pure family and the endpoint-mixture family are stochastically
increasing in the parameter. This shows why order, the two scalar identities,
and one-site marginals do not alone close an affine interval. These iid and
mixed laws are **not claimed invariant for the backchip generator**. The
example is not a counterexample to canonical convergence in the actual model.
