# Exploratory calculations, not asymptotic proofs

`buffer_sim.cpp` runs the two-block partial-transfer protocol at H=N. It uses
Mersenne Twister seed 41731871, 2000*N burn-in events and 20000*N measured
events per parameter pair. Boundary transfer totals are converted to current
by multiplying by N/(number of measured events), since there are 2N total
rate-one clocks and two boundaries. Observations are in `buffer_sim.txt`.
No mixing-time bound, effective sample-size calculation, confidence interval,
or assertion of equilibrium sampling is provided. These observations cannot
prove stationary convergence or a uniform loss estimate.

To reproduce from this directory:

```sh
c++ -O2 -std=c++17 buffer_sim.cpp -o /tmp/nasch_buffer_sim
/tmp/nasch_buffer_sim
python3 buffer_covariance.py
```

The covariance probe requires NumPy and SciPy. It solves small full generators
in floating point and checks normalization, nonnegativity within tolerance,
and balance residuals. `weighted` in its output is **one half** the sum of
expected corrected-buffer times loss, whereas equation (4.9) in the report
uses the full sum. Its positive N=2,H=3,B=1 example was separately certified
using exact fractions in the main verifier. The other floating-point entries
are exploratory only. Some probe densities exceed the research target eta<2;
those entries concern the finite protocol, which is defined at all masses.

The stronger candidate E loss <= F^2/B held in these small calculations.
No general theorem, claim of exhaustive testing, or implication for k=3 is
made from this finite observation.
