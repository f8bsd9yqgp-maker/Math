"""Exact audit of the NEW Fourier formula; no old solver is rerun.

The rational T_N values below are archived regression fixtures, not new data.
Every original Poisson equation is checked on a function reconstructed from
the new boundary solution. No full-state linear system is solved.
"""

import json
import platform
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path

from exact_boundary import exact_solution


ARCHIVED = {
    2: F(1), 3: F(11, 6), 4: F(14, 5), 5: F(75, 19),
    6: F(37, 7), 7: F(409, 60), 8: F(6943, 813),
    9: F(296561, 28365), 10: F(212937, 16951),
    11: F(64288181, 4326262), 12: F(50671493, 2920671),
}


def states(n):
    for x in range(n + 1):
        for y in range(n - x + 1):
            yield (x, y, n - x - y)


def moves(g):
    for j in range(3):
        if g[j]:
            h = list(g)
            h[j] -= 1
            h[(j + 1) % 3] += 1
            yield tuple(h)


def boundary_index(g):
    assert min(g) == 0 and sum(v == 0 for v in g) == 1
    for j in range(3):
        h = g[j:] + g[:j]
        if h[2] == 0:
            return h[0]
    raise AssertionError


def audit_exit_multiplicities(n):
    checks = 0
    for sites in combinations(range(n), 3):
        actual = [0] * (n - 2)
        for j, v in enumerate(sites):
            if (v - 1) % n not in sites:
                continue
            # Moving the particle at v left closes its preceding gap.
            gaps = tuple((sites[(k + 1) % 3] - sites[k]) % n
                         for k in range(3))
            g = list(gaps)
            g[(j - 1) % 3] -= 1
            g[j] += 1
            c = boundary_index(tuple(g)) - 1
            assert 1 <= c <= n - 2
            actual[c - 1] += 1
        predicted = []
        for c in range(1, n - 1):
            predicted.append(sum(
                tuple(sorted((u % n, (c + u) % n, (n - 1 + u) % n)))
                == sites for u in range(n)))
        assert actual == predicted, (n, sites, actual, predicted)
        checks += n - 2
    return checks


def audit(n):
    result = exact_solution(n)
    t = result["boundary"]
    assert result["T"] == ARCHIVED[n]
    harmonic = {}
    if n >= 3:
        spectral = result["spectral"]
        for g in states(n):
            if min(g) > 0:
                harmonic[g] = spectral.harmonic(g)
                assert all(p >= 0 for p in harmonic[g])
                assert sum(harmonic[g]) == 1
        assert result["kernel"] == [harmonic[(a, n - a - 1, 1)]
                                    for a in range(1, n - 1)]

    # Direct killed-generator action on every harmonic-measure column.
    harmonic_checks, polynomial_checks = 0, 0
    for g, probs in harmonic.items():
        targets = list(moves(g))
        for c, p in enumerate(probs, start=1):
            value = 3 * p
            exits = 0
            for h in targets:
                if min(h) > 0:
                    value -= harmonic[h][c - 1]
                else:
                    exits += boundary_index(h) == c + 1
            assert value == exits, (n, g, c, value, exits)
            harmonic_checks += 1
        v = F(g[0] * g[1] * g[2], n)
        qv = sum(F(h[0] * h[1] * h[2], n) - v for h in targets)
        assert qv == -1
        polynomial_checks += 1

    # Reconstruct the full candidate without solving its Poisson system.
    values = {}
    for g in states(n):
        if max(g) == n:
            values[g] = F(0)
        elif min(g) == 0:
            values[g] = t[boundary_index(g)]
        else:
            values[g] = F(g[0] * g[1] * g[2], n) + sum(
                p * t[c + 1] for c, p in enumerate(harmonic[g], start=1))
    poisson_checks = 0
    for g, v in values.items():
        assert v >= 0
        if max(g) != n:
            qv = sum(values[h] - v for h in moves(g))
            assert qv == -1, (n, g, qv)
            poisson_checks += 1
        assert v == values[g[1:] + g[:1]]
    if n >= 3:
        assert 2 * t[n - 1] - t[n - 2] - t[1] == 1
        collision_checks = audit_exit_multiplicities(n)
    else:
        collision_checks = 0
    return {
        "N": n, "T_N": str(result["T"]), "boundary_unknowns": max(0, n - 2),
        "boundary_values": list(map(str, t[1:])),
        "harmonic_equations": harmonic_checks,
        "interior_polynomial_equations": polynomial_checks,
        "original_poisson_equations": poisson_checks,
        "collision_multiplicity_checks": collision_checks,
        "status": "passed_exactly",
    }


def main():
    rows = []
    for n in ARCHIVED:
        row = audit(n)
        rows.append(row)
        print(f"N={n}: T_N={row['T_N']}; exact audit passed", flush=True)
    result = {
        "scope": "New spectral/boundary representation, N=2,...,12",
        "arithmetic": "fractions.Fraction and exact cyclotomic polynomials",
        "old_solvers_rerun": False,
        "results": rows,
        "totals": {key: sum(r[key] for r in rows) for key in (
            "harmonic_equations", "interior_polynomial_equations",
            "original_poisson_equations", "collision_multiplicity_checks")},
        "status": "all_passed_exactly",
    }
    destination = Path(__file__).parent / "results"
    destination.mkdir(exist_ok=True)
    (destination / "exact_audit.json").write_text(json.dumps(result, indent=2) + "\n")
    environment = {"python": platform.python_version(),
                   "platform": platform.platform(), "third_party_required": False}
    (destination / "exact_environment.json").write_text(
        json.dumps(environment, indent=2) + "\n")
    print(json.dumps(result["totals"], sort_keys=True))


if __name__ == "__main__":
    main()
