# An exact flow identity and movement-episode reduction

27 October 2026. Continuation 24, following commit
`a4c2e15e77bf4770ca9a0a939a95a782794fe72e`.

The general fixed-density stationary flow is **not solved**. This note
identifies the remaining mean-current defect more precisely. It proves an
exact finite-noise identity, reduces an entire movement episode to one
backchip transfer in total variation, and characterizes mean-current
convergence by two static conditions. Neither of those conditions is
asserted to hold in the unrestricted limit.

These are AI-assisted analytic arguments with exact structural checks,
not independent peer review or a claim of publication priority.

## 1. Notation and the exact identity

There are N>=2 cars, H vacancies, and epsilon=1-p in (0,1). The full
parallel-update model has stationary gaps g and velocities v. Average the
law over cyclic car-label shifts. Set

\[
a_i=\mathbf1_{\{v_i>0\}},\quad o_i=\mathbf1_{\{g_i\ge1\}},
\quad c_i=a_i\mathbf1_{\{g_i\ge2\}}.
\]

Independent fresh nonbraking coins xi_i have parameter epsilon. The exact
update and its stationary mean speed are

\[
w_i=c_i+\xi_i o_i,\quad g_i'=g_i+w_{i+1}-w_i,\quad v_i'=w_i,
\qquad U=C+\epsilon\mathbb E o_0,                 \tag{1}
\]

where

\[
\eta=H/N,\quad C=\mathbb E c_0,\quad
S=\mathbb E(c_0c_1),\quad B=C-S,\quad
q=\mathbb P(g_0\ge2),\quad W=\mathbb E[c_0(g_0-1)].
\]

Here q is a probability in the **full-model** stationary law. It is not
the reduced canonical probability q_(N,H). Define the nonnegative local
remainder

\[
\begin{split}
\mathcal R=\mathbb E[\,&t_0(1-pc_1-\epsilon o_1)+c_0o_1+u_0c_1
                    +\epsilon s_0c_1+\epsilon u_0o_1\,],\tag{2}\\
t_0&=c_0\mathbf1_{\{g_0=2\}},\quad
u_0=(1-a_0)\mathbf1_{\{g_0\ge2\}},\quad
s_0=\mathbf1_{\{g_0=1\}}.
\end{split}
\]

The factor 1-pc_1-epsilon o_1 is precisely the conditional probability
that the leader does not move, so every summand in (2) is nonnegative.

**Theorem 1.** Every such stationary law satisfies

\[
\boxed{\frac U\epsilon=\eta-q-W+\frac S\epsilon+\mathcal R.} \tag{3}
\]

Writing Y=(1-c_0)g_0 gives the equivalent formula

\[
\boxed{\frac U\epsilon=\mathbb E Y-q+\frac S\epsilon+C+\mathcal R,}
\qquad
0\le\mathcal R\le C+2B+\epsilon.                 \tag{4}
\]

These identities also hold for a translation-invariant infinite-line
stationary law of finite mean gap. They require only a first moment.

**Proof.** Apply the one-step transition to the integrable single-site
potential V=c_0(g_0-1). Direct conditional calculation gives

\[
\mathbb E[V'-V\mid g,v]
=-c_0(1-c_1)+\epsilon\{(g_0-2)^+-c_0(g_0-1)+r(g,v)\}, \tag{5}
\]

where r is the integrand in (2). The following table verifies all cases;
write h=o_1 and z=c_1, with z<=h.

| Initial state at car 0 | r(g,v) | Conditional drift of V |
| --- | --- | --- |
| g_0=0 | 0 | 0 |
| g_0=1 | epsilon z | epsilon^2 z |
| g_0>=2, a_0=0 | z+epsilon h | epsilon(g_0-2+z+epsilon h) |
| g_0=2, a_0=1 | 1+p(h-z) | -(1-z)+epsilon p(h-z) |
| g_0>=3, a_0=1 | h | -(1-z)+epsilon(h-1) |

For example, in the fourth case the clipping at zero contributes when
the car moves two and its leader does not move. Keeping this term is
essential. The update depends on the two fresh coins only, and the
table follows from their four possibilities. It also verifies (5)
pointwise, without a stationary-distribution approximation.

Stationarity in (5) yields

\[
\frac B\epsilon=\mathbb E(g_0-2)^+-W+\mathcal R
                  =\eta-\mathbb E o_0-q-W+\mathcal R.
\]

Use C=B+S and (1) to obtain (3). Since
E Y=eta-W-C, equation (4) follows.

To bound the remainder, its first summand is at most c_0(1-c_1), and
c_0o_1<=c_0. Also u_0+epsilon s_0<=1-c_0, so the third and fourth
summands together are at most (1-c_0)c_1. The final summand is at most
epsilon. Cyclic or translation invariance makes the expectations of
c_0(1-c_1) and (1-c_0)c_1 equal to B. This proves the bound. Square.

The inherited block-work inequality B+epsilon C<=epsilon eta therefore
gives the explicit estimate

\[
0\le \frac U\epsilon-
       \left(\mathbb E Y-q+\frac S\epsilon\right)
\le 2C+(2\eta+1)\epsilon.                          \tag{6}
\]

In bounded-density zero-noise limits, the inherited uniform arrest
theorem gives C=O(epsilon^(1/3)); below eta<=R<1 the pushing comparison
improves this to O_R(epsilon). Thus the error in (6) vanishes uniformly
in road size. Equation (3) is an exact correlation identity, **not a
closed flow formula**, because its stationary terms remain unknown.

## 2. An entire episode from a forced start

For the remainder of the note, assume 1<=H<2N. Sample an ordinary full
stationary state. If v_0>0 or g_0=0, set A=0. Otherwise force the first
coin at car zero to be nonbraking; leave all other coins, including its
later coins, independent with their original probabilities. Let A be the
total distance car zero travels in the consecutive sequence of positive
movements beginning at this forced start, ending just before its first
zero movement.

This sampling includes a zero outcome when no start is eligible. It is
not the normalized conditional law given an actual episode start.

Episodes are finite almost surely. Indeed, H consecutive all-braking
updates take every state to rest when H<2N. Such a word has positive
probability p^(NH) in every disjoint block of H steps. The same fact and
stationarity exclude a movement episode extending indefinitely into the
past.

Put d(m)=m-1{m>=2}, including d(0)=0.

**Theorem 2.** The variable A satisfies

\[
\boxed{\mathbb E A=\frac U\epsilon.}              \tag{7}
\]

It can be coupled to d(g_0), using the same sampled state, so that

\[
\boxed{\mathbb P\{A\ne d(g_0)\}
\le 2C+2\epsilon(\eta+1).}                       \tag{8}
\]

Consequently their total-variation distance is bounded by the right side.
No epsilon N restriction is used. This controls the distribution of the
distance in an **entire** episode, not its expectation.

**Proof of (7).** An actual episode starts at time k exactly when
v_0(k)=0, g_0(k)>=1 and xi_0(k)=1. Charge each positive movement to its
unique episode start. By stationarity and Tonelli's theorem, the expected
movement at time zero equals the expected sum of all movements charged
to a start at zero. The independent first coin contributes epsilon;
the remaining conditional experiment is exactly the definition of A.
Hence U=epsilon E A. This proof does not assume independent episodes or
an ergodic stationary law. It also proves integrability of A. Square.

**Proof of (8).** On an eligible state with g_0=m, suppose c_1=0. If the
leader's coins are braking at times 0,...,d(m), it stays fixed, regardless
of all cars farther ahead. If car zero's coins at times 1,...,d(m) are
also braking, its forced first movement is followed by deterministic
coasting to gap one (gap zero for m=1), then a stop. Thus A=d(m).

These are 2d(m)+1 distinct coin decisions, whose failure probability is
at most epsilon(2d(m)+1). The ineligible case with d(g_0)>0 requires
v_0>0. Writing D=P(v_0>0), the coupling error is therefore at most

\[
D+C+\epsilon\mathbb E[\mathbf1_{\{v_0=0,g_0\ge1\}}
                                      (2d(g_0)+1)]
\le D+C+\epsilon(2\eta+1).
\]

From (1) and stationarity of the velocity flag,
D=pC+epsilon E o_0<=C+epsilon. This proves (8). Square.

There is also a pointwise lower bound in every eligible experiment:

\[
A\ge d(g_0).                                    \tag{9}
\]

To see this, let L be the number of positive-movement steps in the
episode. The stored velocity at time L is positive, but the next
movement is zero, so g_0(L)<=1. Conservation during the episode gives
A=g_0(0)+I_1(L)-g_0(L)>=g_0(0)-1. For g_0(0)=1 the forced first
movement already gives A>=1=d(1). This proves (9).

## 3. The mean amplification is an adjacent-pair probability

Let e=1{v_0=0,g_0>=1}, and define the nonnegative expected gain over the
isolated backchip episode by

\[
G=\mathbb E[A-e\,d(g_0)].
\]

Equations (3) and (7) imply the further exact identity

\[
\boxed{G=\frac S\epsilon+\mathcal R+
                   \mathbb P(v_0>0,g_0=1).}       \tag{10}
\]

Indeed E[a_0d(g_0)]=W+P(v_0>0,g_0=1), so subtracting E[e d(g_0)]
from (3) gives (10). Stationarity of the velocity flag also gives

\[
\mathbb P(v_0>0,g_0\le1)=D-C
                  =\epsilon(\mathbb E o_0-C)\le\epsilon.
\]

Together with the remainder bound and B<=epsilon eta, this yields

\[
\boxed{0\le G-S/\epsilon\le C+2\epsilon(\eta+1).} \tag{11}
\]

Thus, in any bounded-density zero-noise sequence, vanishing expected
amplification is equivalent to S=o(epsilon). A small probability of
interference in (8) does not establish this: the distance gained on the
exceptional event is still unbounded uniformly in N and epsilon.

## 4. Complete decomposition of a subsequential mean-flow defect

Let N_k->infinity, H_k/N_k->eta in (0,2), and epsilon_k->0. Take a
subsequence whose full stationary gaps converge locally to mu. The
previous unrestricted local reduction proves that mu is stationary for
the backchip process. Write

\[
m=\mathbb E_\mu g_0\le\eta,\quad
q_*=\mu(g_0\ge2),\quad F_\mu=m-q_*,\quad\delta=\eta-m.
\]

Uniform arrest implies C_k->0. Hence Y_k=(1-c_0)g_0 converges in
distribution to g_0 under mu, and q_k->q_*.

Pass to any further subsequence with W_k->w and
S_k/epsilon_k->kappa in [0,infinity]. Such a subsequence exists with
w finite, because W_k<=eta_k. Then

\[
0\le w\le\delta,\qquad
\boxed{\lim_k U_k/\epsilon_k=F_\mu+(\delta-w)+\kappa.} \tag{12}
\]

The limit is infinity if kappa=infinity. The corresponding road-flow
limit is (12) divided by 1+eta.

**Proof.** For each fixed integer M,

\[
c_0(g_0-1)\le M c_0+(g_0-M)^+.
\]

Taking expectations, then limits along the chosen subsequence, gives
w<=eta-E_mu min(g_0,M). Let M->infinity to obtain w<=delta.
Now use (3), q_k->q_*, and R_k->0. Square.

Both defects in (12) are nonnegative. More explicitly,

\[
\delta-w=\lim_{M\to\infty}\lim_k
                 \mathbb E[(1-c_0)(g_0-M)^+].      \tag{13}
\]

For fixed M this follows by writing the expectation as
E Y_k-E[(1-c_0)min(g_0,M)] and using
E Y_k=eta_k-W_k-C_k. Thus delta-w is precisely the escaped gap mass
at **unqualified** cars. The other defect kappa is an adjacent qualified
pair probability on the scale epsilon, or equivalently the limiting
mean episode amplification in (11).

Below eta<1 the inherited pushing bound makes U_k/epsilon_k bounded,
so kappa is finite. This does not force either defect to vanish.

## 5. Four equivalent forms of the remaining mean-current condition

Along the local-limit subsequence above, the following are equivalent:

1. U_k/epsilon_k -> F_mu.
2. The episode distances A_k in Section 2 are uniformly integrable.
3. The variables Y_k=(1-c_0)g_0 are uniformly integrable **and**
   P(c_0=c_1=1)=o(epsilon_k).
4. For any one fixed t>0, the actual integrated displacements
   I_0(floor(t/epsilon_k)) are uniformly integrable.

**Proof.** Equation (8), local gap convergence, and C_k->0 imply
A_k converges in distribution to d(g_0) under mu. That limit has mean
F_mu. Equation (7) and the elementary equivalence between convergence of
means and uniform integrability for convergent nonnegative variables
prove 1 iff 2.

From (4),

\[
U_k/\epsilon_k+q_k
  =\mathbb E Y_k+S_k/\epsilon_k+C_k+\mathcal R_k.    \tag{14}
\]

All terms on the right are nonnegative, and Fatou's lemma gives
liminf E Y_k>=m. If item 1 holds, the left side tends to m. Hence
E Y_k->m and S_k/epsilon_k->0. Since Y_k converges in distribution to
an integrable variable of mean m, equality of means is equivalent to
uniform integrability. Conversely, item 3 and (14) imply item 1 because
C_k+R_k->0. This proves 1 iff 3.

The preceding [current-anchor theorem](../2026-10-27-current-anchors/README.md)
proves convergence in distribution of the integrated currents to the
stationary reduced current, of mean t F_mu. Their expectations are
floor(t/epsilon_k) U_k. The same first-moment argument proves 1 iff 4.
Square.

In particular, if the **full gaps** are uniformly integrable, then
m=eta and Y_k is automatically uniformly integrable. In that case the
entire remaining passage from local dynamics to its mean current is
equivalent to the concrete two-site estimate S_k=o(epsilon_k).
Full-gap uniform integrability alone does not supply that estimate.

These equivalences do not establish their conditions. Even their
verification would identify the flux of mu; obtaining the proposed
(eta-Q(eta))/(1+eta) additionally requires F_mu=eta-Q(eta) for every
selected subsequence. The general fixed-positive-noise stationary flow,
that selection, and the vanishing of both defects remain unproved.

## 6. A nonzero pair defect requires a large qualified run

The pair contribution can be localized more sharply. For any state with
H<2N, let ell_i be the distance car i would still travel if every future
coin were braking. It is zero when c_i=0, and otherwise equals the sum
of g_j-1 along the consecutive qualified run starting at i. This is the
previously proved full-braking projection. Let M_1 be the sum of the
gaps in the qualified run starting at car 1, or zero if c_1=0. Each gap
in that run is at least two, so ell_1<=M_1<=2ell_1. Also M_1<=H.

**Theorem 3.** For every integer L>=1,

\[
\boxed{\mathbb P(c_0=c_1=1,\ M_1\le L)
\le L\epsilon^2(2\eta+1)\,p^{-L}.}               \tag{15}
\]

In particular, for every bounded-density joint sequence and a>0,

\[
\boxed{\limsup_k\frac1{\epsilon_k}
 \mathbb P(c_0=c_1=1,\ \epsilon_k M_1\le a)
\le a(2R+1)e^a,}\qquad \eta_k\le R.             \tag{16}
\]

The right side tends to zero as a decreases to zero. Thus a nonzero
subsequential S/epsilon defect requires a positive part of that scaled
pair weight to lie on qualified runs containing at least a/epsilon
vacancies, for some a>0. Equivalently, their remaining coast is at least
a/(2epsilon). This is a necessary geometry, not proof that such runs
have appreciable stationary weight. It need not mean an order-N pile.

**Proof.** Put Z(k)=c_0(k)c_1(k). Since an old unqualified car can become
qualified only if its own fresh coin is one, its stationary birth rate
beta=P(Z(0)=0,Z(1)=1) satisfies

\[
\beta\le 2\epsilon B+\epsilon^2
          \le\epsilon^2(2\eta+1).               \tag{17}
\]

The two one-qualified patterns have probability B each; the pattern
with neither qualified requires both independent coins. No independence
of the old state is asserted.

Stationarity of the binary Z makes its one-step loss rate equal to beta.
A union bound over L steps therefore gives

\[
\mathbb P(\text{at least one transition }Z=1\text{ to }Z=0
                     \text{ by time }L)\le L\beta. \tag{18}
\]

On the event Z(0)=1 and M_1<=L, choose the first initially unqualified
leader j ahead of the qualified run starting at car 1. It exists because
H<2N. Require only this car's L coins to be braking. Conditional on the
initial state, that event has probability p^L even though j was selected
from the state. The car stays fixed, regardless of every other coin.

Conservation between car 1 and the fixed car j gives

\[
I_1(L)=M_1-\sum_{i=1}^{j-1}g_i(L)\le M_1\le L.
\]

If Z had remained one through time L, car 1 would have moved at least
one at each of the L steps, and its final gap would still be at least
two. The same equation would then give I_1(L)<=M_1-2<=L-2, a
contradiction. Hence a loss of Z occurs by time L. It is irrelevant
whether Z later returns to one: (18) counts the occurrence of a loss,
not only an endpoint disagreement. Combining (17)-(18) with p^L proves
(15).

For (16), choose L=floor(a/epsilon_k). Then epsilon_k L<=a and
p_k^(-L)->e^a. Apply (15) and take the limsup. Square.

Taking L=H also proves the unconditional finite-system estimate

\[
\boxed{S\le H\epsilon^2(2\eta+1)p^{-H},\qquad
U/\epsilon\le\eta+1+\epsilon H(2\eta+1)p^{-H}.}   \tag{19}
\]

Thus normalized mean speeds remain bounded at bounded density whenever
epsilon H stays bounded, including a nonzero finite critical scaling.
For epsilon<=1/2 and epsilon H<=A, one may replace p^(-H) by e^(2A).
This does not identify the coefficient or control epsilon H->infinity.

There is a related duration statement. Consecutive runs of Z=1 have
finite lengths, by the same all-braking reset argument. If S>0, then
beta>0 and their mean length, sampled at an actual pair birth, is
S/beta. Thus S/epsilon->kappa>0 would require a mean pair-episode
duration at least (kappa+o(1))/((2R+1)epsilon). These episodes need not
be independent. This is ordinary stationary reward accounting, not a
bound excluding long episodes.

See [AUDIT.md](AUDIT.md), [ATTEMPTS.md](ATTEMPTS.md), and
[HANDOFF.md](HANDOFF.md). The exact code is [verify.py](verify.py).
