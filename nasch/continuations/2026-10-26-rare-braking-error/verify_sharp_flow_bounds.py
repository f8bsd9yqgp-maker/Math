"""Exact interval certificates for the new asymmetric workload error bounds.

Archived rational currents are reused as fixtures; no stationary solve is run.
"""

import json
from fractions import Fraction as F
from pathlib import Path

from verify_flow_bounds import FIXTURES, add, bernstein, mul, scale, substitute_p


def main():
    records = []
    for n, h, num, den, factor, current in FIXTURES:
        denominator = 2 * max(n, h)
        eps = [F(0), F(1, denominator)]
        eps2 = mul(eps, eps)
        d = add([F(1)], scale(eps, -h))
        m_num = scale(mul(eps, add([F(1)], scale(eps, n - 1))), h)
        upper_num = scale(mul(eps, d), F(5 * n - 1, 2) * current)
        upper_num = add(upper_num, scale(m_num, 4 * current))
        upper_num = add(upper_num, scale(mul(eps, m_num),
                                         3 * current * n * (n - 1)))
        lower_num = add(scale(m_num, current),
                        scale(mul(eps, d), current * (n - 1)))
        lower_num = add(lower_num, scale(add(
            scale(mul(eps, m_num), 2 * h),
            scale(mul(eps2, d), h * (n - 1))), h - 1))
        a = substitute_p(num, denominator)
        b = scale(substitute_p(den, denominator), F(factor))
        assert all(c >= 0 for c in den) and den[0] > 0
        diff = mul(d, add(a, scale(b, -current)))
        polynomials = {
            "upper_error_minus_U_over_epsilon_plus_F":
                add(mul(upper_num, b), scale(diff, -1)),
            "lower_error_plus_U_over_epsilon_minus_F":
                add(mul(lower_num, b), diff),
        }
        certificates = {}
        for label, poly in polynomials.items():
            coefficients = bernstein(poly)
            assert all(v >= 0 for v in coefficients)
            assert coefficients[0] == 0
            certificates[label] = list(map(str, coefficients))
        records.append({"N": n, "H": h, "reduced_current": str(current),
                        "epsilon_interval": ["0", str(F(1, denominator))],
                        "bernstein_certificates": certificates,
                        "status": "certified_exactly"})
    report = {"status": "all_passed_exactly", "polynomial_certificates": 8,
              "records": records, "old_stationary_solvers_rerun": False}
    path = Path(__file__).parent / "results" / "sharp_flow_certificates.json"
    path.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": report["status"], "certificates": 8,
                      "interval_endpoints": [r["epsilon_interval"][1]
                                             for r in records]}))


if __name__ == "__main__":
    main()
