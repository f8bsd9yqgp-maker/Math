# Pure-phase selection, affine gaps, and a positive background on every macroscopic arc

25 October 2026. Continuation of commit
`34b46770173e30ada33e50ac76cb16710ae19287`.

These are new, self-contained deductions from the project's preceding
proved results. They are internally audited AI-assisted mathematics, not
independent peer review or proof-assistant certification. No priority claim
is made. The process here is the **continuous-time unit-rate backchip
reduction**, not unrestricted finite-braking Nagel–Schreckenberg dynamics.

The scalar canonical limit was proved in an earlier continuation; it is not
reproved or counted as new here. This note addresses stronger local-law and
spatial-background questions.

## 1. Model and precise inputs

On an N-site ring, each site has a rate-one clock. A clock at i performs

\[
(g_{i-1},g_i)\longmapsto(g_{i-1}+d(g_i),r(g_i)),\qquad
r(m)=\mathbf1_{\{m\ge2\}},\quad d(m)=m-r(m).
\]

Let pi_(N,H) be its unique stationary law with total mass H. Write

\[
q_{N,H}=\pi_{N,H}(g_0\ge2),\qquad
Q(\eta)=\lim_{N\to\infty}q_{N,\lfloor\eta N\rfloor}.
\]

All limiting statements below allow arbitrary N_j tending to infinity and
arbitrary integers H_j with H_j/N_j tending to the stated density.

We use these established project results, with their exact scope:

1. [Scalar convergence](../2026-10-24-thermodynamic-limit/README.md): Q is
   continuous and nondecreasing, bounded by one, and the same Q applies to
   every such canonical sequence.
2. [Positivity](../2026-10-24-positive-occupancy/README.md) and the earlier
   [unit-service comparison](../2026-10-22/README.md) give

   \[
   \frac{\min(\eta,1)^3}{1152}\le Q(\eta)
       \le\frac{\eta^2}{1+\eta},\qquad Q(1)>\frac1{218}.       \tag{1}
   \]

3. [Density-phase classification](../../density_phases_proof.md): every
   finite-mean, translation-invariant stationary law decomposes into unique
   deterministic-density phases nu_r. Each existing such phase is spatially
   mixing. Existing phases are stochastically ordered by density. No
   existence at every density is assumed.
4. [Phase-current identification and the critical endpoint](../2026-10-24-positive-occupancy/PHASE_SELECTION.md):
   every existing nu_r has pile probability Q(r). A canonical local limit at
   density eta has a random component density R satisfying

   \[
   \mathbb E R\le\eta,\qquad \mathbb E Q(R)=Q(\eta).           \tag{2}
   \]

   Let r_+(a) be the largest maximizer of Q(r)-ar on r>=0, for a>0, and
   eta_c=lim_(a down to 0) r_+(a). Every positive r_+(a) has a pure canonical
   limit nu_(r_+(a)). Canonical one-site masses are uniformly integrable at
   every finite eta<=eta_c. Q is strictly increasing there. If eta_c is
   finite, eta_c itself is selected, and every canonical sequence at
   eta>=eta_c converges locally to nu_(eta_c). The endpoint may be infinite.
5. Coordinatewise common-clock attractiveness orders finite canonical laws
   by H. Their one-site means are exactly H/N. Local canonical limits exist
   subsequentially and are stationary and translation invariant.

In particular, when eta<=eta_c, (2) improves to E R=eta. The equality is
essential in the new lower-contact argument.

## 2. New conclusions

Call a density eta<=eta_c **selected** if every canonical sequence at that
density converges locally to its deterministic-density phase nu_eta. This
definition includes existence of the phase and selection by arbitrary
canonical sequences. Write C for the set of selected densities, including 0.

**Theorem A: small selected phases and a positive background.** There are
positive selected densities arbitrarily close to zero. More quantitatively,
for every eta>0 there is a selected density c_eta satisfying

\[
\kappa(\eta):=2^{-22}\min(\eta^2,1)
       \le c_\eta<\eta/2.                                  \tag{3}
\]

Every canonical local limit mu at density eta stochastically dominates
nu_(c_eta). Consequently every component density R of mu satisfies

\[
R\ge c_\eta\ge\kappa(\eta)\quad\hbox{almost surely}.          \tag{4}
\]

Thus there is **no vacuum component** in any canonical local limit at any
positive density. This strengthens the previous exclusion of the vacuum law
itself: a mixture with a positive vacuum weight is excluded too.

Set xi(eta)=kappa(eta)^3/1152. For every fixed epsilon in (0,1], under a
canonical sequence at density eta,

\[
\Pr\left(\exists\hbox{ cyclic arc }I,\ |I|\ge\varepsilon N:
   \frac1{|I|}\sum_{i\in I}g_i<\frac{\kappa(\eta)}4
   \ \hbox{or}\ 
   \frac1{|I|}\sum_{i\in I}r(g_i)<\frac{\xi(\eta)}4\right)
       \longrightarrow0.                                  \tag{5}
\]

In particular the longest arc containing no pile, divided by N, tends to
zero in probability. The constants in (3)-(5) are deliberately conservative.
No rate of convergence in (5) is asserted.

**Theorem B: affine gaps are the only remaining obstruction to pure
canonical selection.** The set C is closed relative to [0,eta_c], with the
usual interpretation when eta_c is infinite, and is cofinal below eta_c.
Each component (a,b) of its complement has finite endpoints in C, and

\[
Q(r)=Q(a)+\frac{Q(b)-Q(a)}{b-a}(r-a),\qquad a\le r\le b.   \tag{6}
\]

For eta in such a gap, every canonical local limit has its component
densities in [a,b], with mean eta. Hence every density at which Q is **not
locally affine** is selected. The possible gaps form at most a countable
collection of disjoint open intervals; none starts at zero.

This is a necessary obstruction, not a claim that every affine interval
causes nonconvergence or a mixed limit. If Q has no nonempty affine interval
below eta_c, then pure canonical convergence holds at every density up to
eta_c, and the earlier supercritical theorem supplies the rest. Absence of
such affine intervals has not been proved.

## 3. A contact lemma that uses preserved mass

**Lemma 1.** Suppose b>0 is selected. Let s be real, and let c be the
largest maximizer or the largest minimizer of

\[
f(r)=Q(r)-sr\quad\hbox{on }[0,b].                          \tag{7}
\]

Then c is selected.

**Proof.** The endpoint c=0 is immediate. At any c<=b, the preceding
uniform-integrability theorem applies, because a selected finite-density
phase in use here lies at or below eta_c. Take any local canonical limit mu
at c. Finite mass order and selection at b imply mu<=_st nu_b. Therefore its
random component density R is at most b almost surely; it is nonnegative.
To justify this implication, take an ordered coupling and pass to the
almost-sure spatial averages of its two coordinates. The upper marginal
has deterministic density b. No bound on each component was assumed before
this coupling argument.

By (2) and uniform integrability, E R=c and E Q(R)=Q(c). Thus

\[
\mathbb E f(R)=f(c).                                      \tag{8}
\]

Since f(c) is the extremal value over the entire possible range of R, equality
forces R to belong to the corresponding extremizer set. By the choice of its
largest member, R<=c. Together with E R=c this forces R=c almost surely.
The stationary density classification identifies mu with the unique nu_c,
and establishes its existence. Every subsequential limit is the same, so
the whole canonical sequence converges. The reasoning applies to every
sequence of masses with ratio tending to c. Square.

The proof works for minima as well as maxima because the mean is preserved.
Replacing E R=c by E R<=c would invalidate (8) for the lower-contact use.

## 4. Quantitative construction of small pure phases

Let

\[
M=\max_{r>0}\frac{Q(r)}r,
\qquad b_*=\max\operatorname*{argmax}_{r>0}\frac{Q(r)}r.     \tag{9}
\]

These extrema exist: Q(r)/r tends to zero at zero by (1), tends to zero at
infinity by boundedness, and is positive somewhere. At slope M, b_* is
exactly r_+(M), since Q(r)-Mr<=0 with equality at zero and at the ratio
maximizers. Thus b_* is selected by the preceding upper-contact theorem.
Moreover (1) gives

\[
M\ge Q(1)>1/218,\qquad 1/217<b_*<218.                     \tag{10}
\]

For the lower bound use M<=b_*/(1+b_*); for the upper bound use
M b_*=Q(b_*)<=1.

For fixed eta>0 set

\[
a_\eta=2^{-20}\min(\eta^2,1),\qquad
c_\eta=\max\operatorname*{argmin}_{0\le r\le b_*}
                    \{Q(r)-a_\eta r\}.                   \tag{11}
\]

Write a=a_eta and f(r)=Q(r)-ar. We have a/2<b_* by (10), and

\[
f(a/2)\le(a/2)^2-a(a/2)=-a^2/4<0.                        \tag{12}
\]

On the other hand f(0)=0 and f(b_*)=b_*(M-a)>0. Hence c_eta is an interior
point and is selected by Lemma 1. Since Q>=0,

\[
-ac_\eta\le f(c_\eta)\le-a^2/4,
\quad\hbox{so}\quad c_\eta\ge a/4=\kappa(\eta).            \tag{13}
\]

If c_eta>=1, (1) and (10) would give

\[
f(c_\eta)\ge1/1152-a b_*>1/1152-218/2^{20}>0,
\]

contradicting (12). Thus c_eta<1. Positivity in (1), together with
f(c_eta)<0, now gives

\[
c_\eta^2<1152a
   \le\frac{1152}{2^{20}}\eta^2<\eta^2/4.                 \tag{14}
\]

Equations (13)-(14) prove (3). In particular selected positive phases approach
zero. This construction is implicit through the function Q; it is not an
explicit formula for Q or for the stationary distribution.

## 5. Domination, component bounds, and macroscopic arcs

Fix eta>0 and c=c_eta. For every sequence H_N/N->eta, eventually
H_N>=floor(cN), since c<eta/2. Finite canonical attractiveness gives

\[
\pi_{N,\lfloor cN\rfloor}\le_{\rm st}\pi_{N,H_N}.
\]

The lower law converges locally to nu_c. Taking ordered local couplings
along any subsequence proves nu_c<=_st mu for every limit mu of the upper
law. Both marginal spatial averages exist, because both have finite mean.
Pointwise order then implies R>=c almost surely, proving (4).

For clarity, the passage to a density bound uses the random spatial average
of mu, not just its expectation. The argument does not require uniform
integrability at the target density eta; that density may exceed eta_c.

We prove (5) by a deterministic counting lemma. Consider a nonnegative
periodic array x_0,...,x_(N-1), a fixed alpha>0, and an integer L. Call a
length-L window bad when its average is less than alpha/2. If a cyclic arc
I of length m>=4L has average less than alpha/4, the sum of the masses of
its m-L+1 internal windows is at most L times the mass of I. Thus fewer
than m/2 internal windows can have mass at least alpha L/2. At least m/4
of the internal windows are bad. In particular, if also m>=epsilon N,
the fraction of bad window starts in the whole ring is at least epsilon/4.

Translation invariance and Markov's inequality consequently give, whenever
epsilon N>=4L,

\[
\Pr(\exists I:\ |I|\ge\varepsilon N,
                   |I|^{-1}\sum_I x_i<\alpha/4)
\le\frac4\varepsilon
 \Pr\left(L^{-1}\sum_{i=0}^{L-1}x_i<\alpha/2\right).       \tag{15}
\]

Apply this first to x_i=g_i and alpha=kappa(eta), and then to x_i=r(g_i)
and alpha=xi(eta). Each bad-window event is a bounded, decreasing cylinder
event in the gaps. The finite ordered comparison bounds its probability
by the corresponding probability under pi_(N,floor(cN)). At fixed L,
selection at c passes this probability to nu_c. The spatial ergodic theorem
then makes it tend to zero as L tends to infinity: the limiting averages
are c>=kappa and Q(c)>=c^3/1152>=xi, respectively. Take N to infinity first,
then L to infinity in (15), and use a union bound for the two arrays. This
proves (5), with no uniform mixing rate and no unproved exchange of limits.

## 6. Closedness of the selected-density set

We first record a useful finite-volume continuity estimate. If f is a
bounded cylinder observable depending on k distinct sites, finite canonical
order and integer-valued discrepancies imply

\[
|\pi_{N,H'}f-\pi_{N,H}f|
\le k\operatorname{osc}(f)\,|H'-H|/N.                     \tag{16}
\]

Indeed, choose an ordered coupling for H<=H'. Every coordinate difference
has mean (H'-H)/N. The probability that any of the k observed coordinates
differs is at most the sum of these means. No independence is used.

Suppose c_j in C tends monotonically to a finite c<=eta_c. The phases
nu_(c_j) are ordered by density and admit a countable monotone coupling.
If c_j increases, monotone convergence gives a finite coordinatewise limit
of mean c. If it decreases, domination by the first finite-mean marginal
gives the same conclusion. Call the limiting law nu. It is stationary and
translation invariant by the Feller property and cylinder limits. In the
ordered coupling,

\[
\mathbb E|G_0^{(j)}-G_0|=|c_j-c|.                         \tag{17}
\]

This law is mixing, not merely a weak limit of mixing laws. To check it,
approximate any bounded cylinder observable by its value in nu_(c_j).
If it observes k sites, the probability of a discrepancy is at most
k|c_j-c|. For a product of two cylinder observables, the resulting error is
uniform in their spatial separation. First use mixing in the fixed phase
nu_(c_j), then let j tend to infinity. Cylinder approximation gives mixing
of nu. Thus it is the deterministic-density phase nu_c.

For any canonical sequence H_N/N->c, compare it using (16) with
pi_(N,floor(c_j N)). Take N to infinity at fixed j and then j to infinity.
For every bounded cylinder f the limiting difference vanishes, so the
canonical law converges to nu_c. Hence c belongs to C.

Every sequence of real numbers converging to c contains either a constant
subsequence equal to c or a monotone subsequence. The preceding argument
therefore proves that C is closed. Its cofinality follows from the selected
upper-contact densities r_+(a) tending to eta_c. If eta_c is finite, its
selection was already proved; zero is selected by its zero mean.

## 7. The affine-gap argument

Let (a,b) be a component of [0,eta_c] minus C. Closedness, cofinality, and
selection of the endpoints zero and a finite eta_c imply that a,b are finite
members of C. For any eta in (a,b), finite mass order, followed by selection
at the endpoints, gives for every canonical local limit mu

\[
\nu_a\le_{\rm st}\mu\le_{\rm st}\nu_b.                   \tag{18}
\]

Spatial averages in ordered couplings show a<=R<=b almost surely. Uniform
integrability at eta<=b<=eta_c gives E R=eta, and (2) gives E Q(R)=Q(eta).

Let s=(Q(b)-Q(a))/(b-a) and f(r)=Q(r)-sr on [a,b]. The endpoint values
f(a) and f(b) are equal. If Q is not affine there, either f has a maximum
strictly above this endpoint value or a minimum strictly below it. Choose
the largest extremizer c for such an extremum. It lies strictly in (a,b).

Apply (18) and the moment identities at density c. They give E f(R)=f(c),
so R is supported on the extremizer set. Every point of that set is at most
c. Since E R=c, it follows that R=c almost surely. The stationary density
classification then identifies every canonical limit with nu_c. This makes
c selected, contradicting the gap. Therefore Q is affine on [a,b], proving
(6). Its slope is positive by the preceding strict-increase theorem.

Every open subset of the real line is a countable disjoint union of open
intervals. There is no gap (0,b), either by the explicit small-phase
construction or because an affine Q on [0,b] would have positive slope at
zero, contradicting Q(r)/r tending to zero. The remaining assertions of
Theorem B follow.

## 8. What has and has not been closed

The new unconditional conclusions are small-density pure phases, exclusion
of every vacuum mixture component, the explicit positive component-density
floor (4), and positive mass and pile densities on every macroscopic arc
in the sense of (5). These hold at every fixed positive target density,
including if that target lies above a finite critical endpoint.

The new selection theorem confines any remaining failure of pure canonical
selection to affine intervals of Q. It does **not** show that such intervals
exist or that they are absent. A density with an existing pure stationary
phase has not automatically been shown to belong to C; that converse must
not be inserted into the proof. Nor does affine behavior force a specific
two-phase mixture. The exact counterexamples in the audit explain why the
two scalar moment identities alone cannot supply those inferences.

Finiteness of eta_c, an exact Q, all-density canonical local-law selection,
the original first-passage T_N formula, interchange with the rare-braking
limit, and unrestricted finite-braking NaSch stationary flow remain open.
The new macroscopic-background statement does not exclude a condensate
coexisting with that background.

See [AUDIT.md](AUDIT.md), [ATTEMPTS.md](ATTEMPTS.md), [HANDOFF.md](HANDOFF.md),
and the new exact arithmetic [verifier](verify.py). Finite audits support
the displayed algebra and the counting lemma; the infinite-volume proofs
are the analytic arguments above.
