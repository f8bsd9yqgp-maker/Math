# Closure attempts and the exact remaining obstruction

26 October 2026, research run 18. Started after commit
`83a55738ad2d542acc333d8407e81ec95b95f655` and continued at interruptions.
Earlier proofs and old stationary solvers were not restarted.

## Fixed-density stationary laws: no closure claimed

The scalar `pi_(N,H)(g_0>=2)` already has a unique limit `Q(eta)` along every
sequence with `N->infinity` and `H/N->eta`. The remaining work concerns an
explicit `Q`, full canonical phase selection, possible finite critical
density, and the original finite-braking traffic model.

The new small pure-phase lower barriers from run 17 are useful but do not
close the condensate problem. A positive density on every macroscopic arc
is compatible with a moving large pile above a positive background. It does
not give a microscopic environment law under conditioning on such a pile.

The particle-weighted environment seen from a large moving head remains a
different object from an unconditioned stationary background. Formal head
balance identities relate successive mean masses and pile probabilities,
but using them to produce an erosion contradiction requires controlled
first moments and a far-field identification under this biased law. Neither
was obtained. No formal balance calculation is promoted to a new theorem.

Nor does first-moment retention alone eliminate an affine phase interval.
The identities `E R=eta` and `E Q(R)=Q(eta)` are consistent with mixtures
supported in an affine interval. Spatial ergodicity at each finite time
does not survive a local weak limit automatically. The converse from
existence of a pure phase to canonical selection remains unjustified.

A literature shortcut was explicitly checked and rejected. Rafferty,
Chleboun and Grosskinsky, *Monotonicity and Condensation in Homogeneous
Stochastic Particle Systems*, [arXiv:1505.02049v2](https://arxiv.org/html/1505.02049v2),
Theorem 2.4 assumes stationary **product measures**. Its conclusion cannot
be applied to our nonproduct backchip model. Their Section 5.3 explicitly
addresses nonproduct monotone examples separately. This is not a proof
either for or against condensation in our model.

## The successful finite-first-passage route

The old triangular Poisson problem has a free three-particle interior.
Killing at its first zero spacing makes that interior an exterior power of
a circulant one-particle generator. Translation projection selects total
momentum zero. Integrating its explicit semigroup gives every boundary exit
probability, leaving a linear-size boundary problem.

The potentially dangerous steps were treated explicitly: orientation,
odd-particle circle signs, repeated translation orbits, corner-source
normalization, and invertibility after pinning the known excursion value.
Theorem 1 in README.md proves the kernel. Theorems 2 and 3 give the mean and
the complete first-passage transform. Exact verification reconstructs the
original functions and checks their equations rather than rerunning the
old full-state solver.

Further inspection found that the first and last rows of `K` coincide
(their interior starting triples are rotations), as do the first and last
columns (the corresponding exit intensities coincide). This is compatible
with the explicit formula but did not yield an elementary scalar recurrence
or a complete diagonalization of the boundary interaction. No additional
theorem is claimed from these matrix patterns.

## Why the new representation does not close the unrestricted problem

1. The Fourier diagonalization applies before the first collision. The
   nontrivial repeated boundary interaction is still present in the explicit
   `M` or `A(alpha)` matrix. It has not been discarded.
2. As `N` grows, the smallest real parts of the free eigenvalues approach
   zero and the boundary inverse also changes. A formal termwise limit does
   not establish a limit of `T_N/N^2`. No such limit is proved here.
3. The original target has exactly three vacancies before taking the
   thermodynamic limit. This does not become fixed positive vacancy density
   by increasing `N` in the same formula.
4. The general backchip generator moves a whole mass minus one, so it is
   not the free unit-chip generator used in this killed interior. A direct
   extension of this Fourier basis would require a new identity.
5. Velocity memory and burst overlap in full discrete-time NaSch still
   require uniform control before interchanging the rare-braking and
   thermodynamic limits.

The full traffic problem remains open. The verified advance is an exact,
explicit, smaller first-passage representation with a faster numerical
algorithm and a complete proof, rather than another stationary data table.
