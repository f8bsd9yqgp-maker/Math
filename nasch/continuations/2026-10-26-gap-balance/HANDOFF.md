# Continuation 21 handoff: resume without repeating old runs

Read README.md and LOCAL_STATIONARY_REDUCTION.md first. Parent repository
commit is `3d8fe96af4cbd9644e3f565a376509d82bf00ada`. The new contribution
is a uniform zero-noise theorem, followed by an unrestricted local
stationary reduction. It is not a full general-flow solution.

## Completed

Let epsilon=1-p, C=average P(v_i>0,g_i>=2), B=average P(c_i=1,c_(i+1)=0),
eta=H/N. The block-work inequality extends to every finite H:

```text
B + epsilon C <= epsilon eta.
```

For S_j=average P(c_i=c_(i+1)=1,g_i=j), S_1=0, stationary threshold
births and losses prove

```text
S_j <= S_(j-1)+(2B+epsilon)/(1-epsilon).
P_av(c_i=1,g_i=j) <= B+(j-1)(2B+epsilon)/(1-epsilon).
```

Sum over j<=M and bound the remaining gap tail by eta/(M+1). This gives
the complete finite-M formula and

```text
U <= (3+6R)epsilon^(1/3),  H/N<=R, epsilon<=1/2, N>=2.
```

This also holds for translation-invariant infinite-volume stationary laws
with finite mean gap. It excludes the moving component of every bounded-
density positive-noise local limit. The old classification at p=1 is
still mathematically valid; its moving component cannot be selected here.

For H<2N, the resting-gap projection has Hamming Lipschitz constant 2
in (g,v). Changing one coin therefore changes at most four projected
gaps. Remove all coins in components of `{c=1 or xi=1}` touching c=1.
The actual and rest-started projected updates then coincide, so their
Hamming distance is at most eight times the number of removed coins.
This count has conditional mean at most `epsilon m+2epsilon b/p`.

For f on r consecutive gaps with norm M, N>2r+2:

```text
|mu Lf| <= [16r+8(r+1)^2] M C + 32r M B/p
           +8r(r+1) M epsilon.
```

Here mu is the cyclically averaged original stationary gap law and L is
the reduced backchip generator. Therefore every local limit with eta<2
is reduced-stationary, without any restriction on epsilon N.

All new scripts passed. Read results/ and AUDIT.md for exact counts. Do
not repeat the old full-state stationary or Poisson solvers.

## Remaining obstruction

Local stationarity alone does not select the canonical density phase or
preserve its mean. A uniformly translated single pile has generator
residual O(1/N), fixed finite-ring density eta, and local vacuum limit.
This example is not stationary full traffic; it invalidates only an
inference from the new local bound alone.

Likewise the new Hamming estimate does not control mass transported or
lifted-height displacement. The known normalized current formula still
requires epsilon N->0. Unrestricted first-order interchange, fixed-
epsilon thermodynamic current uniqueness, the exact general flow, and
remaining reduced phase/condensate alternatives are not solved.

If U/epsilon diverges, then conditional on a uniformly sampled qualified
car both its gap and its qualified-block length tend to infinity in
probability. Uniform tightness of these conditional gap laws would give
a size-uniform U=O(epsilon) bound; that tightness is unproved and would
not alone identify the coefficient. This is a concrete next research
target, not an authorization to assume it.

All results are AI-assisted and internally audited, without independent
specialist peer review. Do not label the unrestricted problem closed.
