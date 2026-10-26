"""Exact discounted Poisson audit of the full first-passage transform."""

import json
from fractions import Fraction as F
from pathlib import Path

from exact_boundary import exact_laplace
from verify import states, moves, boundary_index


def main():
    rows = []
    for n in range(2, 11):
        for discount in (F(0), F(1, 2), F(1), F(2)):
            result = exact_laplace(n, discount)
            values = {}
            for g in states(n):
                if max(g) == n:
                    value = F(1)
                elif min(g) == 0:
                    value = result["boundary"][boundary_index(g)]
                else:
                    harmonic = result["spectral"].harmonic(g)
                    value = sum(p * result["boundary"][c + 1]
                                for c, p in enumerate(harmonic, start=1))
                values[g] = value
                assert 0 <= value <= 1
                if discount == 0:
                    assert value == 1
            count = 0
            for g, value in values.items():
                if max(g) == n:
                    continue
                generator = sum(values[h] - value for h in moves(g))
                assert generator == discount * value
                count += 1
            rows.append({"N": n, "discount": str(discount),
                         "laplace_B": str(result["laplace"]),
                         "discounted_poisson_equations": count,
                         "status": "passed_exactly"})
        print(f"N={n}: all four discounted audits passed", flush=True)
    report = {"results": rows, "total_discounted_poisson_equations": sum(
        r["discounted_poisson_equations"] for r in rows),
        "status": "all_passed_exactly", "old_solvers_rerun": False}
    path = Path(__file__).parent / "results" / "laplace_audit.json"
    path.write_text(json.dumps(report, indent=2) + "\n")
    print(report["total_discounted_poisson_equations"])


if __name__ == "__main__":
    main()
