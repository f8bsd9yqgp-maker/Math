# What the current-anchor argument closes, and what it does not

27 October 2026.

## Completed step

The previous dynamic reduction controlled gap observations. Algebraically,
gap changes determine current differences, not a common height translation.
The new argument uses a model-specific fact to fix that translation:
an initially unqualified car with no subsequent nonbraking coin does not
move. With probability tending to one, such an anchor exists within a
finite, slowly growing neighborhood. The same Poisson construction freezes
the corresponding reduced current. Endpoint gap agreement then identifies
the integrated current exactly.

This proves joint finite-dimensional current and gap convergence without
an epsilon N restriction. It is a strict extension of the previous
bounded-gap theorem, not another simulation or restatement of stationarity.

## Why that is not yet the fixed-density mean formula

The proof gives a small **probability** of a discrepancy. It does not
bound the displacement on the exceptional event. The rare-event scale
contains order 1/epsilon physical steps, and the elementary speed bound
of two allows an order 1/epsilon displacement. Multiplying a small event
probability by that bound need not produce a vanishing expectation.

The upper comparison from continuation 22 bounds the mean U/epsilon
uniformly for eta<1. A bounded first moment does not imply uniform
integrability. For example X_a=1/a with probability a and zero otherwise
has mean one and converges in probability to zero. This is a logical
counterexample to an inference, not a proposed stationary traffic law.

The new theorem does identify the exact needed tail condition for any
selected local stationary law mu:

    lim_(M->infinity) sup_k
      E[I_k(t) 1{I_k(t)>M}] = 0,

where I_k(t) is actual car displacement over floor(t/epsilon_k) updates.
It is equivalent to mean-current convergence to E_mu d(g_0), once the
proved distributional convergence is used. This condition has not been
proved for the full-model stationary sequence.

It would be a mistake to impose the same condition on the instantaneous
velocity divided by epsilon. Instantaneous nonzero velocity becomes rare,
so that variable converges to zero in probability while its expectation
can stay positive. The right observable is integrated displacement on
the rare-event time scale.

## Attempts to bound the exceptional contribution

An anchor can fail to be initially unqualified. Its probability is at
most C, but a car already moving may have a long remaining coast. The
bound C=O(epsilon) below eta=1 does not exclude a nonvanishing contribution
to rescaled mean current from these rare starts. A conditional moving-car
workload estimate is still missing.

Likewise, an upper pushing trajectory starts above the original profile
by a finite vertical offset, at most H with the normalization used in
continuation 22. That offset disappears in a long-time stationary speed
comparison. It can grow with N and cannot be discarded uniformly on a
fixed rescaled observation interval. Thus the existing comparison does
not give a uniform tail bound for the integrated current.

The earlier positive-amplification family remains relevant: one coin
changes total projected travel quadratically in a block length while
only two final projected gaps differ. It prevents charging an unbounded
transport discrepancy merely to the number of changed coordinates or
to a fixed multiple of the triggering gap mass. It does not disprove
the desired stationary formula.

No new finite-size stationary system was solved to evade these issues.
The new finite computations test the anchor identities directly.

## Stationary law selection is a second issue

The local full-model limit is a reduced-stationary law mu, whose mean
m may be less than the nominal eta. Its pile probability q is a bounded
observable. The new mean lower bound is

    liminf U/epsilon >= m-q.

It is not automatically eta-Q(eta): the theorem has not selected the
canonical reduced law at the nominal density. Even proving the current
tail condition leaves the separate identification of m-q to address.
The project already has the desired identification under epsilon N->0;
that restricted result has not been upgraded here.

## Literature check on possible condensation shortcuts

A primary article relevant to strong-overbraking phase separation is
Miedema, de Wijn and Schall, [*Criterion for condensation in kinetically
constrained one-dimensional transport models*](https://doi.org/10.1103/PhysRevE.89.062812)
(2014; [preprint](https://arxiv.org/abs/1402.6220)). Its condensation
criterion is not an exact general stationary current formula.

The related [author's thesis](https://pure.uva.nl/ws/files/2518584/164085_DEFINITIEF_BIBLIO_bw_Miedema_LR_complete.pdf),
Sections 5.3.2–5.3.3, analyzes strong-overbraking jam formation through
scaling estimates and simulation-supported creation rates. Figure 5.2
uses densities near the transition density; this must not be silently
identified with our arbitrary fixed eta regime. These arguments do not
supply the stationary integrated-current uniform-integrability estimate
needed above. Nor are vehicle-jam condensation and condensation of vacancy
mass at a gap identical assertions. No theorem excluding either relevant
alternative is imported from that work.

## Status

The unrestricted local current-distribution reduction is proved here.
The general fixed-density stationary flow is not proved, and no
stationary counterexample to the proposed limit is established. A claim
that the full problem is closed would still require an unproved passage
to expectation and an unproved stationary-flux selection step.
