# Remaining closure attempts and precise missing estimates

26 October 2026. Run 19 starts from published commit
`d940b3834c3b6c85f33dfcdc36a862fe6b1d797d`. The user's requested targets are
the general stationary flow, the remaining phase/condensate alternatives,
and interchange of thermodynamic and rare-braking limits. This run advances
the third target, with a restricted joint-limit theorem. It does not close
all three.

The continuation within this run subsequently improved the explicit error
to `O_R(epsilon N+epsilon^2 N^3)` and its sufficient joint-limit condition
to `epsilon N^(3/2)->0`; see [the completed sharper proof](SHARP_WORKLOAD_BOUND.md).
The all-parameter analytic argument and new exact audits passed. The
initial cubic condition is no longer the strongest result.

## 1. Why an explicit full-braking map was useful

The original fast dynamics does not need a mixing estimate: every active
car continues at speed one until its forward active block has used its
available gaps. That gives the exact sums in (7) of README.md. Composing
the reduced current corrector with the resulting resting-height projection
removes every all-braking step from its drift.

The initial crude estimate would charge every rare event a worst-case
H-step burst and give an unnecessarily large size error. The exact
serialization from rest improves the expected workload injection to
epsilon*H. The corrector further makes the one-event current drift equal
to epsilon*F at every resting configuration, avoiding a comparison of
stationary distributions or an inverse spectral gap.

## 2. The obstruction to unrestricted interchange

The initial proof treated the whole road as one resting/nonresting object.
The sharper continuation replaces its crude activity estimate with bounds
on the number of moving cars and the excess beyond one. The resulting
error is epsilon*N+epsilon^2*N^3 at bounded vacancy density. For fixed
epsilon and increasing N, these estimates still deteriorate. No uniform
local substitute was proved.

A sufficient improvement would be a modulus omega(epsilon)->0 such that

```text
sup over N,H with H/N in a fixed compact subset of (0,2)
    |J_(N,H)(1-epsilon)/epsilon - N*F_(N,H)/(N+H)|
        <= omega(epsilon).
```

Together with the existing reduced scalar limit, this would control all
joint sequences and any thermodynamic-first current limits. It would not,
by itself, prove uniqueness of full-model thermodynamic current at each
fixed epsilon if that inner limit has not otherwise been established.

The explicit acceleration counterexample rules out one proposed route:
the relaxed trajectory is not monotone in the nonbraking coins, and its
single-event displacement defect can grow linearly in N at density one.
This does not rule out an averaged uniform estimate. It does prevent
silently using the reduced model's height order for the full dynamics.

## 3. Stationary phase selection

The existing phase theorem identifies canonically selected densities
outside possible affine intervals of Q. On an affine interval, preserved
mean and the identity E Q(R)=Q(eta) still permit mixtures with E R=eta.
No strict-curvature theorem or independent local concentration estimate
was obtained here.

Constructing a multicolour stationary family does not automatically remove
this gap. Under a common-clock threshold construction, a site with ordered
particle marks retains its second-smallest mark, so every threshold obeys
the backchip rule. Finite first moments can be retained under an upper
stationary phase. But local limits of these marked fields can still lose
spatial ergodicity through phase separation. Deterministic initial colour
densities and finite-time ergodicity alone do not establish an ergodic
stationary threshold law or canonical selection. No new theorem is claimed
from this construction.

The finite time-memory reset of a single bulk-service queue likewise does
not give spatial contraction of the infinite tandem at fixed mass
intensity. Input marks have temporal correlations. No Burke property or
independent-input closure was assumed.

## 4. The critical-density/condensate alternative

The positive macroscopic background theorem for reduced canonical laws is
not a microscopic statement under conditioning on a large moving pile.
The particle-weighted head environment is biased. Its exact local balance
conditions allow stationary infinite-head laws, as already established in
run 5. No contradiction from those local conditions was found here.

A velocity argument based on a head moving at rate one and an ordinary
background particle moving more slowly also fails to close the proof:
mass left behind the head can return, and the environment sampled by the
head is not the unconditioned background. Identifying its far-field flux
requires a new theorem, not just the ordinary stationary mean current.

For context, Whitehouse, Costa, Blythe and Evans study the backchip rule
with mass-dependent rates in *Maintenance of order in a moving strong
condensate*, [arXiv:1407.1668v3](https://arxiv.org/html/1407.1668v3).
Their constant-rate discussion reports simulation evidence and explains
why their rate-separation mechanism does not apply there. It is not a
rigorous proof excluding every partial condensate in our constant-rate
canonical model. No such exclusion is imported from it.

## 5. The stationary formula itself

The reduced coefficient `(eta-Q(eta))/(1+eta)` is known to exist, and the
new theorem identifies it with a genuine full-model joint limit. Its
function Q remains implicit. A generic finite Markov-chain determinant
formula or a telescoping series of finite-size values would not by itself
resolve the requested general thermodynamic stationary formula, so neither
is presented as closure.

The supplementary [zero-noise classification](ZERO_NOISE_LIMITS.md) is an
additional completed argument. Any unrestricted joint local limit of the
full stationary laws is a mixture of all-rest configurations and all-moving
configurations with every gap at least two. A spatially ergodic such limit
at mean gap below two must be resting, but spatial ergodicity of these
limits has not been established. Even proving that unscaled current tends
to zero would not determine its coefficient after division by epsilon.

The remaining concrete tasks are therefore unchanged in their essential
content: obtain an exact stationary construction or a new closure for Q;
settle pure selection inside possible affine intervals and finiteness of
the critical density; and replace the global rare-event error by local
control uniform in the road size. The verified progress here is the first
explicit polynomial full-model error and its stated joint-limit regime
within this project, not a solution of those outstanding tasks.
