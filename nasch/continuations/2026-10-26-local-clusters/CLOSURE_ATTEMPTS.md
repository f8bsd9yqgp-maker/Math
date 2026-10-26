# Remaining closure attempts and obstructions

The local-cluster argument improves the joint full-traffic approximation
from `(1-p)N^(3/2)->0` to `(1-p)N->0`. It also gives a one-sided current
bound valid uniformly in road size. The user's general stationary formula,
phase/condensate alternatives, and thermodynamic-first interchange remain
open.

## Why the cluster comparison is still not uniform

The corrector is monotone and the sum of its reduced single-clock
increments is F. However, the full-to-auxiliary disagreement set depends
on the current traffic state. Its sites can correlate with large corrector
increments. Translation invariance of the stationary distribution does not
by itself make the conditional influence of such a site equal to the
unconditional mean F/N.

This failure is exact even at fixed positive density. Take `H=floor(eta N)`
and put all mass at one site of the reduced ring, then choose that site's
location uniformly. This is a translation-invariant gap distribution. All
backchip updates except the one at the pile are identities, so the sum
identity for corrector increments forces the pile increment to be F and
all others to be zero. If a state-dependent selected set consists of that
single pile site, its density is 1/N but its total corrector influence is F,
not F/N. This example need not be a stationary full-model distribution,
and its selected set is not asserted to be the particular mixed cluster
set in the new proof. It demonstrates only that translation invariance and
the corrector sum identity, without a further structural argument, cannot
justify the desired factorization.

The proof charges two reduced updates per disagreement site, each by F,
and therefore needs bounds on the *global* active-car moments. The proved
moment estimate requires `epsilon H<1/2`. This is why the final bound
still grows with N. No uniform-in-N local-influence or active-cluster
estimate was established.

The one-speed comparison avoids this obstruction for a lower bound: it has
a monotone update even though the full model does not. It does not furnish
an upper comparison of comparable sharpness. In particular, a simple
single-speed process cannot represent persistent movement created by an
earlier nonbraking event.

## Condensate and phase alternatives

The [qualified-block drift theorem](ACTIVE_BLOCK_GEOMETRY.md) proves a
size-uniform geometric restriction: `E b+epsilon E m<=epsilon H`. If the
unscaled current remains positive as epsilon tends to zero, a positive
fraction of cars must sit in qualified blocks whose lengths diverge at
least on the `1/epsilon` scale. This does not bound those lengths above or
show that the blocks are macroscopic compared to the ring. It concerns car
activity and is not an exclusion of vacancy-mass condensation.

The reduced scalar limit Q and its positive-background/critical-endpoint
theorems are inherited. The new full-model bounds do not transfer the
reduced canonical phase classification to fixed positive epsilon. A
moving-pile Palm environment can differ from an unconditioned spatial
environment; no argument here excludes a condensate coexisting with the
positive background. Possible affine selection intervals and finite
versus infinite critical density remain unresolved.

## Honest next target

A sufficient statement would bound
`|J_(N,H)(1-epsilon)/epsilon - N*F_(N,H)/(N+H)|` by a function tending
to zero with epsilon uniformly over all N at fixed density range. This
would control unrestricted joint sequences and any thermodynamic-first
limits that already exist. It would not, without another argument, prove
existence and uniqueness of the full-model thermodynamic current for each
fixed positive epsilon. Neither this estimate nor that existence theorem
is claimed here.
