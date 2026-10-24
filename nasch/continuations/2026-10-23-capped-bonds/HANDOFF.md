# Continue here: capped-bond comparison, 24 October 2026

## Status

The requested all-size fixed-density limit remains OPEN:

    lim_N pi_(N,floor(eta N))(g_0 >= 2), 0 < eta < 2.

Do not claim a full solution, a condensation theorem, or an unrestricted
NaSch flow formula. The user repeatedly requests closure and asks for all
chat prose in a copybox. They authorized adding genuinely proved results
to GitHub. Preserve the previous proofs rather than restarting.

Repository: f8bsd9yqgp-maker/Math, under nasch/.
This continuation builds on commit
75ce673c6fb9c22e16c09f1a5d4c5781e892274b, which published the buffer protocol
and exact clock-correlation counterexamples. Read current main before any
further GitHub mutation; the repository also contains unrelated work.

## New theorem proved in this continuation

For the ordinary N-site mass-H unit-rate backchip chain, let F be its current.
Cap transfers at sites i in S at positive integers C_i; let J be the capped
chain's common stationary current. Put

    e_C(x) = max(ceil(x/C)-1, 0),
    R = sum_(i in S) E_pi e_(C_i)(d(g_i)),
    A = sum_(i in S) 1/C_i.

Then, for every finite N >= 2 and H >= 1,

    F/(1+R) <= J <= F,
    0 <= 1/J - 1/F <= R/F <= A,
    0 <= F-J <= F^2 A/(1+FA).

R is exactly the original-law sampled tail sum
sum_i sum_(k>=1) pi(g_i >= k C_i + 2).
The proof is analytic, not inferred from finite computations.

Key construction: split an oversized transfer into legal chunks at the
same donor clock, suppressing all other updates until clearing completes.
Keep distinct intermediate labels (original state, donor, chunk count).
The auxiliary chain is exactly a subdivision of selected generator edges.
Its active state g has invariant weight pi(g)/(1+R), and each intermediate
label on an edge starting from g has the same weight. All balance equations
hold explicitly. Its current is F/(1+R). Monotone heights sandwich it below
the capped chain, which is itself below the original chain.

This avoids the earlier informal random-time-deletion justification. Do
not silently let other sites evolve while a transfer is partially cleared.

## New observable bound

Capped chains need not be rotation invariant. For their site-averaged pile
probability qbar, eta=H/N, and overflow

    O = (1/N) sum_(i in S) E_cap (d(g_i)-C_i)^+,

the exact identity is J=eta-qbar-O. Let

    D_H=max(1,H-1), B_H=sum_i max(D_H/C_i-1,0).

Then

    -J B_H/N <= qbar-q_original <= F^2 A/(1+FA),
    |qbar-q_original| <= eta^2 A.

Also expected mass at capped sites divided by N is at most

    |S|/N + (J/N) sum_i max(1,D_H/C_i).

Thus finitely many increasing caps approximate both current and averaged
pile probability uniformly in road size. No bound on masses at other sites
or on spatial mixing follows.

## Exact remaining target

If for every fixed C in any unbounded sequence the current of the ring
with ONE capped bond converges at H=floor(eta N), the original limit follows
by the uniform O(1/C) approximation. The same is true for its averaged pile
probability. This fixed-cap convergence is NOT proved.

Alternatively a capped-block gluing loss O(C/N), together with the capping
loss O(1/C), would close the previously proved two-prime criterion after
C~sqrt(N). No such gluing estimate has been proved. A cap at a core boundary
does not automatically reduce the order-H corrector oscillation to O(C).

Capping all sites costs sum_i 1/C_i=N/C in the available argument. A
dimension-independent replacement for that sum has not been established.

## Additional proved observation

For Q=sum_i 1{g_i>=2}, H>=2, and s<=0, the finite stationary Feynman–Kac
pressure satisfies s-1 <= Lambda_(N,H)(s) <= 0. Thus Lambda/N -> 0 at every
fixed negative bias and arbitrary mass sequence. Proof: start at the
single-pile recurrent state and suppress its lone active clock, at cost
exp(-t). The full proof and derivative caveat are in CLOSURE_ATTEMPTS.md.
This is not a canonical condensation proof and does not justify exchanging
the thermodynamic limit with a derivative at zero.

## Checks and files

verify.py, standard library, exact rational arithmetic:

* 85 full labelled capped stationary chains;
* 1,180 capped-chain stationary equations;
* 1,348 subdivided-protocol stationary equations;
* 168 intermediate legal chunks;
* 10,392 local monotonicity, chunking, and tail-identity checks;
* current inequalities, overflow identities, q bounds, cap-mass bounds.

All passed. Full stationary weights and one extended protocol certificate
are retained. These checks do not mechanically verify an asymptotic theorem.

The eight-ring covariance probe is exploratory and must not be promoted to
negative association. It found no positive threshold covariance in those
eight cases. The old mass-moment exploration already suggested related
finite inequalities; this is not a fresh general theorem.

All new proofs are internally audited working mathematics, not independently
peer-reviewed and not claimed to be first in the literature. Original T_N,
mass uniform integrability, canonical phase selection, the earlier spacing
bound's missing occupancy lower bound, and limit interchange all remain open.
