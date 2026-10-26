"""Optional NumPy cross-check of the new FFT implementation.

Compares with the new exact cyclotomic representation, then exercises four
larger sizes. Residuals are not forward-error bounds or asymptotic proofs.
"""

import json
import platform
from pathlib import Path

import numpy as np

from exact_boundary import SpectralBoundary
from fft_boundary import fft_kernel, compute
from verify import ARCHIVED


def main():
    checks = []
    for n in range(3, 13):
        exact = np.array([[float(x) for x in row]
                          for row in SpectralBoundary(n).kernel()])
        numerical = fft_kernel(n)
        error = float(np.max(np.abs(numerical - exact)))
        mean_error = abs(compute(n)["T_N_approx"] - float(ARCHIVED[n]))
        assert error < 1e-12 and mean_error < 1e-10
        checks.append({"N": n, "max_exact_kernel_difference": error,
                       "T_N_archived_difference": mean_error})
    benchmarks = [compute(n) for n in (40, 80, 160, 320)]
    report = {
        "scope": "Numerical implementation audit, not an asymptotic proof",
        "checks": checks, "benchmarks": benchmarks,
        "numpy": np.__version__, "python": platform.python_version(),
    }
    path = Path(__file__).parent / "results" / "fft_audit.json"
    path.write_text(json.dumps(report, indent=2) + "\n")
    print(f"All {len(checks)} exact-kernel/FFT checks passed.")
    for row in benchmarks:
        print(json.dumps(row, sort_keys=True))


if __name__ == "__main__":
    main()
