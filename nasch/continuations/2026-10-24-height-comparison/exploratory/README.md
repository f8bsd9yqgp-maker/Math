# Finite-time diagnostic, not a theorem

`flat_oscillation.cpp` samples independent clock realizations, always from
balanced deterministic initial gaps. It observes the process at exactly
t=sqrt(N), using a Poisson(Nt) total event count and uniform site labels.
No stationarity or mixing assumption enters this experiment.

Reproduce with a C++17 compiler, from the repository root:

```sh
g++ -std=c++17 -O3 nasch/continuations/2026-10-24-height-comparison/exploratory/flat_oscillation.cpp -o /tmp/nasch_flat_oscillation
/tmp/nasch_flat_oscillation > /tmp/nasch_flat_oscillation.csv
```

The saved CSV uses seed 202610240701. C++ distribution implementations may
produce different exact streams across standard-library implementations.
`se_range` is the sample standard error, not a rigorous confidence bound.
The other empirical means do not have separate standard errors recorded.
The main proof uses none of these numerical estimates.

Observed decay of R/t at these finitely many sizes and densities does not
establish the conditional theorem's all-size, all-required-times power bound.
In particular, no asymptotic exponent has been asserted or fitted here.
