"""O(N^3) floating-point evaluation of the Fourier boundary formula.

Requires NumPy. The returned diagnostics are residuals, NOT rigorous error
bounds. Use exact_boundary.py for exact small-N reference values.
"""

import argparse
import itertools
import json
import time

import numpy as np


def permutation_sign(p):
    return (-1) ** sum(p[i] > p[j] for i in range(3)
                      for j in range(i + 1, 3))


def fft_kernel(n, discount=0.0):
    if n < 3 or discount < 0:
        raise ValueError("Need N>=3 and nonnegative discount.")
    modes = np.arange(n)
    z = np.exp(-2j * np.pi * modes / n)
    eigenvalues = 3 + discount - z[:, None] - z[None, :] - 1 / (
        z[:, None] * z[None, :])
    # The constant mode is annihilated by both alternants even when alpha>0.
    eigenvalues[0, 0] = 1
    reciprocal = 1 / eigenvalues
    reciprocal[0, 0] = 0
    green = np.fft.ifft2(reciprocal)
    sites = (np.zeros(n - 2, dtype=int), np.arange(1, n - 1),
             -np.ones(n - 2, dtype=int))
    terms = [(sites[p[0]] - sites[p[2]], sites[p[1]] - sites[p[2]],
              permutation_sign(p)) for p in itertools.permutations(range(3))]
    kernel = np.zeros((n - 2, n - 2), dtype=complex)
    for u, v, sign in terms:
        for up, vp, signp in terms:
            kernel += sign * signp * green[(u[:, None] - up[None, :]) % n,
                                           (v[:, None] - vp[None, :]) % n]
    return kernel / 6


def compute(n):
    if n < 2:
        raise ValueError("Need N>=2.")
    if n == 2:
        return {"N": 2, "T_N_approx": 1.0, "status": "exact_trivial_case"}
    started = time.monotonic()
    kernel = fft_kernel(n)
    matrix = 2 * np.eye(n - 2) - np.eye(n - 2, k=-1)
    matrix[:, 1:] -= kernel.real[:, :-1]
    a = np.arange(1, n - 1)
    known = (n - 1) * (n + 4) / 6
    rhs = 1 + a * (n - a - 1) / n + kernel.real[:, -1] * known
    values = np.linalg.solve(matrix, rhs)
    return {
        "N": n, "T_N_approx": float(values[0]),
        "seconds": time.monotonic() - started,
        "max_imaginary_kernel": float(np.max(np.abs(kernel.imag))),
        "max_kernel_row_sum_error": float(np.max(np.abs(kernel.sum(axis=1) - 1))),
        "minimum_real_kernel_entry": float(np.min(kernel.real)),
        "max_boundary_residual": float(np.max(np.abs(matrix @ values - rhs))),
        "omitted_boundary_equation_residual": float(abs(
            2 * known - values[-1] - values[0] - 1)),
        "status": "floating_point_not_certified",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("N", nargs="+", type=int)
    args = parser.parse_args()
    for n in args.N:
        print(json.dumps(compute(n), sort_keys=True), flush=True)
