# BioResolve: conditional fault-tolerant count reconciliation

**Research note — 22 October 2026.** AI-assisted, internally tested mathematical exposition. **Not peer reviewed; not claimed as a new theorem.** The result combines established exact Poisson and binomial confidence intervals, a union bound, and an interval sweep. It does **not** prove that arbitrary biological measurements can be reconciled without valid calibration.

## Theorem 1 — exact set from partially trustworthy closed intervals

Given $n\ge 1$ observed nonempty closed intervals $I_1,\ldots,I_n$ (allowing infinite endpoints) and an integer $0\le f<n$, define

$$
\mathcal C_f=\{t\in[0,\infty):\sum_{i=1}^n {\bf 1}\{t\in I_i\}\ge n-f\}.
$$

Then $\mathcal C_f$ is **exactly the union of intersections over all choices of $n-f$ intervals**:

$$
\boxed{\mathcal C_f=\bigcup_{\substack{S\subseteq\{1,\dots,n\}\\|S|=n-f}}\ \bigcap_{i\in S} I_i\ \cap [0,\infty).}
$$

In particular, it contains precisely the values supported by at least $n-f$ reported intervals. It may be empty, a point, one interval, or a disconnected union of intervals. It can be computed exactly in $O(n\log n)$ time and $O(n)$ space without enumerating the subsets.

**Proof.** Membership in the union means that *some* subset of size $n-f$ consists entirely of intervals containing $t$. This is equivalent to at least $n-f$ intervals containing $t$, which is precisely membership in the defining set. For the algorithm, sort the at most $2n$ distinct finite and infinite endpoints. Sweep in ascending order, adding interval starts before testing the endpoint and removing interval ends afterward. An endpoint is included exactly when its coverage count is at least $n-f$. Each open segment between consecutive endpoints is included exactly when its constant coverage count is at least $n-f$. Merge neighboring included pieces. This handles coincident endpoints and isolated points. Sorting takes $O(n\log n)$ time and the sweep $O(n)$. QED.

**Interpretation caveat.** The theorem is an exact identity concerning *reported intervals*. It does not make their probabilistic assumptions true, identify which instruments failed, or establish that values outside the intervals were physically impossible.

## Theorem 2 — finite-sample fault-tolerant coverage for calibrated counts

Let $\theta\ge0$ be a fixed quantity. Instrument $i$ reports nonnegative integer count $K_i$, known exposure $D_i>0$, and an **externally justified** multiplicative gain bound $0<L_i\le G_i\le U_i<\infty$.

Assume at least $n-f$ **fixed** instruments are honest, and that for each honest instrument

$$K_i\sim\operatorname{Poisson}(D_iG_i\theta).$$

The other $f$ instruments may report arbitrary data. No independence **between** instruments is assumed. Choose overall miscoverage budget $\delta\in(0,1)$ and individual budget $\alpha=\delta/n$.

Let $[\ell_i,u_i]$ be the ordinary equal-tailed Garwood $(1-\alpha)$ confidence interval for the Poisson mean, obtained from the observed $K_i=k$:

$$
\ell_i =
\begin{cases}
0&k=0,\\[2pt]
\tfrac12\chi^2_{2k,\alpha/2}&k>0,
\end{cases}\qquad
u_i=\tfrac12\chi^2_{2(k+1),\,1-\alpha/2}.
$$

Define the interval for $\theta$ by

$$ I_i=\left[\frac{\ell_i}{D_iU_i},\frac{u_i}{D_iL_i}\right]$$

and compute $\mathcal C_f$ as in Theorem 1. Then

$$\boxed{\Pr_\theta(\theta\in\mathcal C_f)\ge 1-\delta.}$$

**Proof.** For an honest instrument, exact Poisson interval coverage yields $\Pr(D_iG_i\theta\in[\ell_i,u_i])\ge1-\delta/n$. Because $G_i\in[L_i,U_i]$, that event implies $\theta\in I_i$. By Boole's inequality, the probability that *any* of the at least $n-f$ fixed honest instruments has $\theta\notin I_i$ is at most $(n-f)\delta/n\le\delta$. On the complementary event, all honest intervals contain $\theta$, so the total number containing $\theta$ is at least $n-f$. Consequently $\theta\in\mathcal C_f$. QED.

The guarantee is **conditional on** the Poisson model, known exposures, fixed honest set, and correct gain bounds. It is conservative, not an experimentally verified calibration claim. An empty calculated set can indicate contradictory observations or invalid model/calibration assumptions.

## Theorem 3 — confidence sets for an A/B concentration ratio

Let $r=c_A/c_B>0$ and suppose for each honest instrument $i$:

$$X_i\sim\operatorname{Poisson}(D_{Ai}e_{Ai}c_A),\qquad
Y_i\sim\operatorname{Poisson}(D_{Bi}e_{Bi}c_B),$$

where **within each instrument** $X_i$ and $Y_i$ are independent, $D_{Ai},D_{Bi}>0$ are known, and the independently certified efficiency ratio satisfies

$$0<L_i\le e_{Bi}/e_{Ai}\le U_i<\infty.$$

Conditional on $N_i=X_i+Y_i$, $X_i$ has the binomial law

$$X_i\mid N_i \sim\operatorname{Binomial}(N_i,p_i),\qquad
\frac{p_i}{1-p_i}=\frac{D_{Ai}}{D_{Bi}}\frac{e_{Ai}}{e_{Bi}}r.$$

Construct an equal-tailed Clopper–Pearson confidence interval $[p_i^-,p_i^+]$ for $p_i$ at individual error level $\delta/n$ and set

$$
I_i=\left[
\frac{p_i^-}{1-p_i^-}\frac{D_{Bi}}{D_{Ai}}L_i,\quad
\frac{p_i^+}{1-p_i^+}\frac{D_{Bi}}{D_{Ai}}U_i
\right]
$$

with the usual limiting conventions $0/(1-0)=0$ and $1/(1-1)=+\infty$. If $N_i=0$, use $I_i=[0,\infty]$; **never** impute an informative ratio from two zero counts.

For at most $f$ faulty instruments, define $\mathcal C_f$ from these intervals using Theorem 1. Then

$$\boxed{\Pr_r(r\in\mathcal C_f)\ge 1-\delta.}$$

**Proof.** Conditional binomial coverage gives $\Pr(p_i\in[p_i^-,p_i^+]\mid N_i)\ge1-\delta/n$ for each honest instrument, hence the same unconditional guarantee. The odds map $p\mapsto p/(1-p)$ is increasing; the externally certified efficiency bound therefore implies that the true $r$ is in $I_i$ whenever $p_i$ is covered. Apply the union-bound argument from Theorem 2. The instruments need not be independent of each other. QED.

## Theorem 4 — unconditional biological identification is impossible without calibration

Suppose the expected count for an endogenous gene in sample $s$ is

$$\lambda_s=D_s e_s c_s,$$

where $D_s$ is observed, while concentration $c_s$ and sample-specific gene efficiency $e_s$ are both unknown positive values and the efficiency may vary freely across samples.

For any choice $h_s>0$, set $c_s'=h_sc_s$ and $e_s'=e_s/h_s$. Then

$$D_se_s'c_s'=D_se_sc_s=\lambda_s.$$

The entire distribution of observed Poisson counts is unchanged, yet the concentration ratio $c_A'/c_B'=(h_A/h_B)(c_A/c_B)$ can be made different. Known spike-in values do not resolve this ambiguity when they impose no constraints on the **endogenous gene's** efficiencies. Therefore this unrestricted model does **not** uniquely identify its A/B concentration ratio. QED.

## Scope, provenance, and prior methods

This is a solved **conditional mathematical inference problem**, not a universal biological solution and not an assertion of originality or publication priority. The statistical ingredients are classical (Garwood Poisson intervals, Clopper–Pearson binomial intervals, Bonferroni/union bound, closed-interval event sweeps). Numerical tests verify an implementation; they are not a proof of real-world instrument calibration.

For biological context: BioResolve v1.9 additionally reports exploratory SEQC GSE47774 ERCC-ratio prediction on held-out sequencing sites, but the empirical improvement is **not** part of the proofs above. No inference about true endogenous-gene concentrations follows from an ERCC prediction score alone.

*Reproducibility source:* BioResolve v1.9 internal research package, 22 Oct 2026. Requires independent specialist review and experimental confirmation of any claimed calibration bounds.
