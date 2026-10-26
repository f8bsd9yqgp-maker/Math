"""Certify the NEW error bound against archived exact full-model formulas.

No old stationary solver is rerun. These four rational current functions are
regression fixtures from the 15 October research record. Nonnegative exact
Bernstein coefficients certify both error inequalities on a whole interval
of epsilon, rather than checking finitely many epsilon values.
"""

import json
from fractions import Fraction as F
from math import comb
from pathlib import Path


def add(a, b):
    c = [F(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        c[i] += x
    for i, x in enumerate(b):
        c[i] += x
    return c


def scale(a, c):
    return [c * x for x in a]


def mul(a, b):
    c = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c


def substitute_p(coefficients, denominator):
    """p=1-x/denominator; coefficient lists are in ascending powers."""
    out = [F(0)] * len(coefficients)
    for i, c in enumerate(coefficients):
        for j in range(i + 1):
            out[j] += F(c * comb(i, j) * (-1) ** j, denominator ** j)
    return out


def bernstein(poly):
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    degree = len(poly) - 1
    return [sum(poly[j] * F(comb(k, j), comb(degree, j))
                for j in range(k + 1)) for k in range(degree + 1)]


# U/epsilon = numerator(p)/(factor*denominator(p)). These are OLD formulas.
FIXTURES = [
    (3, 3, [4, 2, 5, 1], [4, 4, 6, 3], 1, F(12, 17)),
    (4, 3, [6, 15, 12, 8, 1], [2, 6, 6, 4, 1], 4, F(21, 38)),
    (5, 3, [18, 43, 57, 56, 29, 11, 1], [6, 17, 24, 25, 15, 6, 1],
     5, F(43, 94)),
    (3, 4, [4, 16, 11, 22, 2, 4, -1], [1, 5, 4, 7, 2, 1],
     3, F(29, 30)),
]


def main():
    records = []
    for n, h, num, den, factor, current in FIXTURES:
        assert F(sum(num), factor * sum(den)) == current
        assert all(c >= 0 for c in den) and den[0] > 0
        epsilon_den = 2 * h * (n - 1)
        a = substitute_p(num, epsilon_den)
        b = scale(substitute_p(den, epsilon_den), F(factor))
        # epsilon=x/epsilon_den and D=1-x/2.
        epsilon, d = [F(0), F(1, epsilon_den)], [F(1), F(-1, 2)]
        beta = (n - 1) ** 2
        c = h * (n * (h + 1) + current)
        rhs_numerator = mul(mul(epsilon, add([c], scale(d, beta * current))), b)
        difference_numerator = mul(d, add(a, scale(b, -current)))
        certificates = []
        for sign in (-1, 1):
            polynomial = add(rhs_numerator, scale(difference_numerator, F(sign)))
            coefficients = bernstein(polynomial)
            assert all(value >= 0 for value in coefficients)
            assert coefficients[0] == 0
            certificates.append({"sign": sign,
                                 "bernstein_coefficients": list(map(str, coefficients))})
        records.append({"N": n, "H": h, "reduced_current": str(current),
                        "epsilon_interval": ["0", str(F(1, epsilon_den))],
                        "certificates": certificates, "status": "certified_exactly"})
        print(f"N={n}, H={h}: both bounds certified for 0<=epsilon<=1/{epsilon_den}")
    report = {"status": "all_passed_exactly", "archived_formula_count": len(records),
              "polynomial_certificates": 2 * len(records), "records": records,
              "old_stationary_solvers_rerun": False,
              "fixture_source": "nasch_three_holes_research.md, 15 October 2026"}
    path = Path(__file__).parent / "results" / "flow_bound_certificates.json"
    path.write_text(json.dumps(report, indent=2) + "\n")


if __name__ == "__main__":
    main()
