# The remaining first-order and phase-selection obstruction

The new arguments close two gaps: all bounded-density zero-noise limits
are resting, and in the range eta<2 their gap laws are stationary for the
backchip reduction. They do not close the complete problem.

## 1. What anomalously large normalized current would require

The adjacent-pair proof gives the stronger information

\[
\mathbb P_{\rm av}(c_0=1,2\le g_0\le M)
 \le\epsilon A_M(\eta,p),\qquad
A_M=(M-1)\eta+{(1+2\eta)M(M-1)\over2p}.            \tag{1}
\]

The block drift also gives

\[
\mathbb P_{\rm av}(c_0=1,L_0\le s)\le s\epsilon\eta,\tag{2}
\]

where L_0 is the length of the qualified block containing the sampled
car. For H<2N, every qualified block has a boundary, so (2) follows by
counting at most s cars per boundary. These statements require only
cyclic averaging, not a chosen ergodic stationary law.

Suppose along a bounded-density sequence epsilon->0 and U/epsilon->infinity.
Since `U=C+epsilon E o_0`, this implies C/epsilon->infinity. For every
fixed M and s, division of (1)-(2) by C shows

\[
\mathbb P(g_0\le M\mid c_0=1)\to0,
\qquad\mathbb P(L_0\le s\mid c_0=1)\to0.           \tag{3}
\]

Thus a diverging normalized current would require *both* diverging gaps
and diverging block lengths as viewed from a uniformly sampled qualified
car. This is a necessary condition, not a construction of such a regime.
The unconditional gap laws remain tight; the conditional laws in (3)
condition on an event whose probability tends to zero.

A useful exact sufficient condition now follows. If these conditional
gap laws are uniformly tight, choose a fixed M with
`P(g_0>M | c_0=1)<=1/2` for every relevant law with C>0. Then

\[
C\le2\epsilon A_M(\eta,p),\qquad
U/\epsilon\le1+2 A_M(\eta,p).                      \tag{4}
\]

For bounded eta and p>=1/2, this is a size-uniform first-order upper bound.
**The conditional tightness hypothesis is not proved.** Even (4), if
established, would bound the coefficient rather than identify its value.

## 2. Local generator convergence does not select the density

There is a simple rigorous obstruction to claiming more from the new
local estimate alone. Set `H=floor(eta N)>0`, put all H gap units at one
site of an N-ring, and randomize that site's location uniformly. Call the
resulting gap law lambda_N. For every cylinder f supported on r sites,

\[
|\lambda_N Lf|\le {4r\|f\|_\infty\over N}.         \tag{5}
\]

Indeed only the pile clock can change the configuration. One backchip
move changes at most two gap coordinates, hence at most 2r terms in
the cyclic sum of f, each by at most `2||f||`. Divide by N.
Nevertheless lambda_N converges locally to the empty gap configuration,
whose mean is zero, although every finite-ring mean tends to eta.

The instantaneous spatially averaged reduced current in lambda_N is
`H/N-1/N` for H>=2, tending to eta; the limiting empty law's current is
zero. This shows exactly why an unbounded mass/current observable cannot
be passed through local convergence using only (5). These lambda_N are
**not** claimed to be stationary full-traffic laws or canonical reduced
laws. They are counterexamples to an inference from local generator
residual and conserved finite-ring mean alone.

The previously proved positive-background theorem concerns canonical
stationary reduced laws. The new full-model local stationarity theorem
does not identify its limits as those canonical laws, so importing that
positive-background conclusion here would be circular.

## 3. Why the new Hamming comparison does not control current

The resting projection is Lipschitz in the number of coordinates changed
by a perturbation. A bounded cylinder observable can charge an error to
those coordinates without caring about their mass or separation.

A current observable cannot do that. One altered projected gap may
contain a macroscopically large mass, and the other altered gap may be
far away. Equivalently, lifted-height differences can persist over a
long qualified run even if only its endpoint gaps differ. The new
comparison therefore proves a uniform local stationary reduction but
does not upgrade the older current-corrector estimate to a size-uniform
first-order error.

The existing theorem identifying J/epsilon when epsilon N->0 is preserved.
For unrestricted sequences, the equality

\[
\lim {J_{N,H}(1-\epsilon)\over\epsilon}
 ={\eta-Q(\eta)\over1+\eta}
\]

has neither been proved nor disproved here. The vanishing bound
`U=O(epsilon^(1/3))` does not supply it.

## 4. Relation to the physics literature

The primary paper by de Wijn, Miedema, Nienhuis and Schall,
[*Criticality in Dynamic Arrest: Correspondence between Glasses and Traffic*,
Phys. Rev. Lett. 109, 228001 (2012)](https://doi.org/10.1103/PhysRevLett.109.228001),
studies dynamic arrest and phase coexistence near p=1. Its near-critical
scaling includes road vehicle densities of order epsilon. Such a regime
has unbounded vacancy-to-car ratio and is not covered by a fixed-R bound.

Miedema, de Wijn and Schall,
[*Criterion for condensation in kinetically constrained one-dimensional
transport models*, Phys. Rev. E 89, 062812 (2014)](https://doi.org/10.1103/PhysRevE.89.062812),
analyze jam growth and creation using a cluster criterion and scaling
arguments. The [primary preprint](https://arxiv.org/abs/1402.6220) makes
the scaling assumptions and simulation input visible. That analysis is
relevant context, not a substitute for the uniform stationary current
and canonical phase-selection estimates required here.

These papers concern traffic-jam clusters; a vacancy-mass condensate in
car-gap coordinates is a distinct object. Neither our resting-limit
theorem nor its literature comparison rules out all condensation.

## 5. Honest remaining target

The complete problem still requires a general stationary-flow formula,
selection of the relevant reduced phase/mixture and treatment of escaped
mass, and control of first-order current along unrestricted joint limits.
Existence and uniqueness of the fixed-positive-epsilon thermodynamic
current are also not proved by these zero-noise arguments.

The new strongest route is to establish control of the environment seen
from qualified moving cars, then convert it into a weighted transport
estimate. Equations (1)-(4) isolate one concrete prerequisite; no proof
of that prerequisite or assertion that it alone closes the problem is made.
