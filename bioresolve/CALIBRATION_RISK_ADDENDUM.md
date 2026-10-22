# BioResolve — calibration uncertainty addendum

**22 October 2026. Status:** mathematically valid conditional clarification of the [original proof](PROOF.md); not peer reviewed, not a new theorem, and **not** proof of an endogenous-RNA assay's physical validity.

## The issue

The previous conditional Poisson and standard-addition results assume that limits on spike-in dose, instrument exposure, assay response, and sample/blank background contain the true physical values.

If those limits are **estimated from other measurements**, their own failure probabilities matter. An interval with 95% coverage cannot be treated as a deterministic bound just because a user calls it "calibrated."

## Joint finite-sample coverage theorem

Let \(\theta\) be the biological quantity being measured, let \(E_1,\ldots,E_m\) denote the events that all relevant count/rate intervals and calibration bounds contain their true quantities, and suppose a scientifically justified procedure guarantees

\[
\Pr(E_j^c)\le \alpha_j
\]

for each event. An event can cover an entire vector of calibration parameters jointly; when so, count its error allowance **once**. Let \(C\) be the complete inverse-image set of concentrations compatible with *all* the measured confidence limits and the declared physical forward model.

Provided the forward model is correct, whenever all \(E_j\) occur, the true \(\theta\) belongs to \(C\). Thus

\[
\boxed{\Pr(\theta\in C)\ \ge\ 1-\sum_{j=1}^{m}\alpha_j.}
\]

**Proof.** On \(\bigcap_j E_j\), the true parameters satisfy every declared inequality, hence the true concentration is among the feasible inverse-image concentrations. Therefore \(\Pr(\theta\in C)\ge \Pr(\bigcap_j E_j)\ge 1-\sum_j\Pr(E_j^c)\ge1-\sum_j\alpha_j\), by the union bound. No independence between the coverage events is needed. QED.

For a **95%** claim the complete sum of *all stochastic* error budgets must be no more than 0.05. Example: 0.03 for the joint rate uncertainty and 0.04 for the native-versus-spike response calibration give only a **93%** lower bound, not 95%.

This theorem is still **conditional on the forward physical model**. It does not cure incorrect native/spike response equivalence, RT nonlinearity, shared systematic batch biases, overdispersed count models, wrong dilution units, or laboratory selection. Those assumptions require direct biological validation and cannot be rescued by merely assigning them an arbitrary error allowance.

## Study-sizing clarification

The earlier BioResolve acceptance screen requires a **one-sided 95% exact binomial lower bound** on independent batch success of at least 0.95.

- With 60 genuinely independent batches it demands **60/60 successes**.
- If the real probability of meeting that batch gate is 0.98, a 60-batch experiment has only \(0.98^{60}\approx29.8\%\) chance to pass.
- With 234 independent exchangeable batch outcomes the exact design chance is about **80.9%** when true success is 98%.

These are **study-power calculations, not assay-validation results**. Independence across preparations, lots and laboratories must be justified; 234 wells from three correlated laboratory runs do *not* qualify as 234 independent batches. Nor does the 234 result establish power for a randomly sampled unseen laboratory.

## Biological caveat

NIST's ERBB2 SRM 2373 concerns *genomic DNA copy number*, not independently certified endogenous ERBB2 *RNA concentration*. It must not be substituted for RNA calibration truth. Published MIQE 2.0 guidance explicitly warns that reverse-transcription yield and synthetic versus endogenous RNA response may differ.

**Current status:** BioResolve's conditional mathematics is preserved. Actual human ERBB2 RNA response bounds, rate-model validity and blinded orthogonal laboratory coverage remain unverified.

## Code and detailed reports

The independent audit bundle named *BioResolve v2.6 — Joint Calibration Risk and Power Audit* includes executable risk-budget checks and exact binomial study-power code. As before, passing software tests does **not** constitute physical certification.
