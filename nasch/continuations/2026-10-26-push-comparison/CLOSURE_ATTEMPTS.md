# Attempts to close the remaining problem, and a transport obstruction

27 October 2026. This record separates completed new deductions from
routes that did not close. It is not a stationary counterexample or a
claim that the full problem has been solved.

## 1. What the exact pushing law does and does not identify

The synchronous upper comparison has an exactly uniform binary stationary
law and an exact finite-polynomial speed. Its factorization is proved in
README.md. This solves the auxiliary system, and gives a rigorous bound
on the original process. It does not give the original process's law.
The comparison deliberately replaces the qualification condition
`v_i>0,g_i>=2` by `g_i>=2`; equality of the two stationary speeds has
not been established and is not asserted.

For eta<=R<1, it improves the full-model bound from order epsilon^(1/3)
to order epsilon. Together with the lower comparison, it gives an exact
law as eta->0, uniformly in epsilon. At fixed eta>0 the upper and lower
coefficients remain separated. For eta>=1 the binary majorant has no
vacant site to stop a pushing run, or cannot have the required mass at
all. Replacing it by capacity-two sites does not repair the proof:
the memoryless upper map already moves an unmarked site with gap two.
No valid first-order upper comparison over 1<=eta<2 was obtained.

## 2. A new exact positive-amplification family

Let ell>=1, N=5ell+3, H=4ell+2, and take

* `g_i=3, v_i=1` for i=1,...,ell;
* `g_(ell+1)=ell+2, v_(ell+1)=0`;
* all other gaps and velocities zero.

Indices are cyclic, with the displayed block away from the wrap. This
is a valid traffic state with H<N and H/N->4/5. Only the coin at
j=ell+1 is nonbraking in the next update; every other coin brakes.

Let h be the initial lift, and P its full-braking projected lift. The
initial coasting distances are

\[
P_i-h_i=2(\ell-i+1)\quad(1\le i\le\ell),
\qquad P_i-h_i=0\quad\hbox{otherwise}.
\]

Under the chosen mask, all cars i=1,...,ell+1 move one cell. The first
ell gaps remain three, and the last becomes ell+1. They are all now
qualified. Their remaining coasting distances are

\[
\ell_i'=2(\ell-i+1)+\ell\quad(1\le i\le\ell),
\qquad \ell_{\ell+1}'=\ell.
\]

Thus the new projected lift P' satisfies, exactly,

\[
P_i'-P_i=
\begin{cases}
\ell+1,&1\le i\le\ell+1,\\
0,&\text{otherwise}.
\end{cases}
\]

Its total projected-height increment is `(ell+1)^2`. By contrast,
start from rest at the old projection and use the same single coin.
The projected gap at j is still ell+2. Its isolated backchip move
changes only height j, by ell+1. The difference between the actual
and rest-started total projected travel is therefore

\[
\boxed{\ell(\ell+1).}
\]

The triggering gap contains only ell+2 units. Hence no universal
constant times that mass bounds the extra projected travel from one
coin in an arbitrary state. The two final projected gap configurations
disagree at only two coordinates, despite this quadratic height effect.
This is precisely why a Hamming estimate is not a mass/transport estimate.

The proof covers every ell. Independent original-rule simulation of
complete full-braking relaxation checks ell=1,...,50 in verify_push.py.
The family is not claimed to occur with significant stationary probability,
nor to lie in a specified recurrent class. It disproves a pointwise
shortcut, not the desired stationary current formula. It is consistent
with the new size-uniform stationary current bound.

## 3. Why polynomial-time local tracking still falls short

The dynamic proof now gives

`E D(G_n,Z(n lambda))/N <=
 8 epsilon(C+2B/p+epsilon)[n+lambda n(n-1)/2]`.

This controls bounded local observations, and permits growing observation
times: o(epsilon^(-1/6)) generally, or o(epsilon^(-1/2)) below eta=1.
It does not establish that the reduced chain has mixed to its canonical
finite-ring law by those times, uniformly over arbitrarily large N.
Neither uniform spatial mixing nor mean retention follows just by
letting the observation time grow.

Likewise, boundedness of U/epsilon is an L1 bound. It is not uniform
integrability of displacement on the rescaled time interval. As a purely
logical example, a variable equal to 1/a with probability a and zero
otherwise converges to zero in probability as a->0 while keeping mean
one. This is not asserted to be a traffic distribution; it identifies
the missing implication. The family in Section 2 shows why unbounded
transport corrections cannot be bounded solely by the number of affected
coordinates in the actual dynamics.

The upper comparison also starts with a vertical height offset that
can depend on N. Its disappearance as time tends to infinity proves
a stationary mean-speed inequality. It does not give a size-uniform
bound on the tails of a finite-time current increment.

## 4. Phase and condensate alternatives examined

The existing canonical reduced results are retained, not claimed again:
the scalar pile probability converges along every size sequence; positive
background and a critical-density alternative are proved in prior notes.
The critical endpoint may still be finite or infinite. Below it, affine
gaps of the limiting pile function are the remaining obstruction to the
available pure-selection argument.

Time-averaging a mass-thinned state between ordered stationary phases
preserves its expected density when an integrable upper law dominates
it. This does not preserve spatial ergodicity through the subsequent
limit: the result can be a mixture of endpoint phases with the correct
mean. Thus this construction does not fill a putative phase gap.
Common-clock synchronization of already existing pure phases does not
by itself construct every intermediate phase.

A moving-pile drift calculation would need the conditional environment
seen by that pile. Substituting an unconditional bulk density, a
compound-Poisson arrival law, or independent neighboring masses is not
justified. These are the same unresolved correlation issues identified
by the earlier queue work, and no such approximation is used here.

The primary backchip paper, Whitehouse, Costa, Blythe and Evans,
[*Maintenance of order in a moving strong condensate*](https://arxiv.org/html/1407.1668v3),
discusses apparent finite-size condensation and a logarithmically growing
critical density in the weak-condensate regime. Its numerical and
approximate arguments do not supply the required theorem for the
constant-rate process. No proof that eta_c=infinity is imported from it.

## 5. Exact status at the end of this run

Completed here: a new synchronous upper comparison; its exact auxiliary
stationary law and speed; a uniform dense-traffic asymptotic; a local
dynamic rare-event reduction with polynomial time error; and the
positive-amplification obstruction above.

Still unresolved:

1. An exact general stationary current for full NaSch and uniqueness of
   its fixed-positive-noise thermodynamic current along arbitrary sizes.
2. Identification, at each fixed positive eta, of the unrestricted
   joint limit of J/epsilon with `(eta-Q(eta))/(1+eta)`.
3. Selection of the full-model zero-noise gap law, including possible
   escaped mean and density mixtures.
4. Finiteness or infiniteness of the reduced critical density, and pure
   canonical selection inside any affine intervals that actually exist.

No contradiction to the desired general formula, and no complete proof
of it, has been produced. The new results restrict the possibilities;
they do not justify declaring these remaining items solved.
