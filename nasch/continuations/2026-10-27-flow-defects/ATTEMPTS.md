# What the new identities resolve, and the attempted closure

27 October 2026. This continuation starts after the current-anchor proof;
it does not repeat that argument or the earlier stationary solvers.

## Successful new step

The previous result left a uniform-integrability condition on an
integrated displacement over order 1/epsilon updates. The present work
revisited the exact one-site activity-weighted gap drift. Keeping the
clipping term at gap two, rather than bounding it, produces a remainder
with a fixed nonnegative sign. This yields an exact formula for U/epsilon.

A separate time mass-transport argument identifies U/epsilon as the mean
distance of a single eligible forced-start experiment, with zero reward
for ineligible states. Its entire episode is coupled to one backchip
transfer using only the car's and its leader's coins. The coupling is
uniform in road size and requires no bound on episode duration on the
failure event.

Combining the two proofs identifies mean amplification of an episode
with S/epsilon up to a vanishing, explicitly bounded remainder, where
S=P(c_0=c_1=1). This is a new quantitative interpretation of the missing
tail contribution.

## Attempt to close the adjacent-pair term

The remaining estimate is S=o(epsilon), not merely S->0. The known
C=O(epsilon) bound below eta=1 gives S=O(epsilon), leaving exactly the
scale capable of a nonzero defect. Above eta=1 the inherited arrest
bound is weaker still. None of these bounds supplies the required
little-o estimate.

Conditioning on one car's independent starting coin does not make the
two adjacent movement episodes independent. A long episode of the leader
can keep supplying vacancies to its follower and prolong the follower's
episode. Treating their overlap as a product of one-car probabilities
would remove the very correlation represented by S and is not justified.

The exact local drift is therefore retained as a correlation identity.
It is not called a closed stationary flow formula.

## A successful localization of the pair obstruction

The pair's birth rate is at most epsilon^2(2eta+1). A first attempt
protected all cars in a short qualified run by requiring every coin in
a space-time rectangle to brake. That gives a valid but needlessly weak
probability cost. The final argument freezes only the first unqualified
car ahead. Conservation caps the movement of its followers by the
initial vacancies between them and this fixed car, regardless of all
other coins.

This proves P(c_0=c_1=1,M_1<=L)<=L epsilon^2(2eta+1)p^(-L), where
M_1 is the vacancy mass in the qualified run starting at the leader.
Hence pairs supported on run masses o(1/epsilon) cannot carry a nonzero
first-order defect. Any surviving contribution needs order 1/epsilon
run mass or more. The same argument bounds normalized current whenever
epsilon H remains bounded, but does not identify its coefficient.

What remains missing is a stationary tail estimate at or above this
scale. The estimate does not rule out the rare moving-run alternative
and does not replace it with an unproved no-condensation assumption.

## Attempt to close the mass contribution

For a chosen limiting law of mean m, all escaped mean is eta-m.
The new proof shows that the part carried by qualified cars can be
subtracted exactly from that missing mass in the current formula. The
remaining contribution is the tail of Y=(1-c_0)g_0, the gap mass at
unqualified cars. This distinguishes two mechanisms previously hidden
inside the integrated-current tail condition.

The full gap mean bound supplies tightness, but still does not bound this
tail in expectation. Conversely, even preservation of the full gap mean
would leave S=o(epsilon) to prove. The two mechanisms cannot simply be
identified or assumed to cancel: their contributions to the new defect
formula are both nonnegative.

No stationary full-model counterexample with either positive defect was
found. The theorem classifies potential subsequential defects; it does
not establish that the alternatives occur.

## Remaining scope

An unrestricted mean passage to the selected local reduced flux now has
three equivalent tests: episode-reward UI, integrated-current UI, or the
combination of unqualified-gap UI and S=o(epsilon). None is proved
unconditionally. Flux selection F_mu=eta-Q(eta) is a separate remaining
condition for the proposed canonical coefficient. The original full
stationary formula at fixed positive nonbraking probability remains open
in this project as well.

This run uses no new literature theorem or publication-priority claim.
All new mathematical statements are derived from the model's update
rule and the explicitly linked inherited results.
