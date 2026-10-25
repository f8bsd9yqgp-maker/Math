#!/usr/bin/env python3
"""New exact audits only; no stationary solve or previous verifier is rerun.

The finite contact audit checks the algebraic selection step. The arc audit
checks the deterministic implication used before the two ordered limits.
Neither is a numerical proof of the infinite-volume theorem.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement, product
from pathlib import Path
import json
import platform
import sys


def compositions(total, length):
    if length == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in compositions(total - first, length - 1):
            yield (first,) + rest


def contact_audit():
    # Density nodes are 0,1,2,3,4. Q values and slopes have denominator 8.
    # This is an audit of the finite moment argument, not a model fit.
    denominator = 8
    by_mean = {c: [] for c in range(5)}
    for weights in compositions(denominator, 5):
        mean_numerator = sum(i * w for i, w in enumerate(weights))
        if mean_numerator % denominator == 0:
            by_mean[mean_numerator // denominator].append(weights)
    candidates = 0
    exact_contacts = 0
    interior_contacts = 0
    for q in combinations_with_replacement(range(5), 5):
        for slope in range(-2, 7):
            f = tuple(q[i] - slope * i for i in range(5))
            for extreme in (min(f), max(f)):
                c = max(i for i, value in enumerate(f) if value == extreme)
                for weights in by_mean[c]:
                    candidates += 1
                    eq = sum(w * value for w, value in zip(weights, q))
                    ef = sum(w * value for w, value in zip(weights, f))
                    assert ef - denominator * f[c] == eq - denominator * q[c]
                    if eq == denominator * q[c]:
                        exact_contacts += 1
                        interior_contacts += int(0 < c < 4)
                        assert weights[c] == denominator
                        assert sum(weights[i] for i in range(5) if i != c) == 0
    return {
        "candidate_moment_checks": candidates,
        "exact_extremal_contacts": exact_contacts,
        "interior_extremal_contacts": interior_contacts,
        "largest_extremizer_selection": "PASS",
    }


def arc_audit():
    # alpha = 1/2 or 1. Work entirely with integers after clearing denominators.
    checks = 0
    nonvacuous = 0
    for alphabet, sizes in ((range(2), range(4, 11)), (range(3), range(4, 8))):
        for n in sizes:
            for x in product(alphabet, repeat=n):
                doubled = x + x
                prefix = [0]
                for value in doubled:
                    prefix.append(prefix[-1] + value)
                for length in range(1, n // 4 + 1):
                    for alpha_denominator in (1, 2):
                        # alpha = 1 / alpha_denominator.
                        bad = [
                            2 * alpha_denominator *
                            (prefix[i + length] - prefix[i]) < length
                            for i in range(n)
                        ]
                        for start in range(n):
                            for mass_length in range(4 * length, n + 1):
                                checks += 1
                                arc_mass = prefix[start + mass_length] - prefix[start]
                                if 4 * alpha_denominator * arc_mass < mass_length:
                                    nonvacuous += 1
                                    internal_bad = sum(
                                        bad[(start + j) % n]
                                        for j in range(mass_length - length + 1)
                                    )
                                    assert 4 * internal_bad >= mass_length
                                    assert 4 * sum(bad) >= mass_length
    return {
        "cyclic_arc_checks": checks,
        "low_density_arcs_checked": nonvacuous,
        "macroscopic_window_implication": "PASS",
    }


def constants_audit():
    a_max = F(1, 2**20)
    assert a_max < F(1, 218)
    assert a_max / 2 < F(1, 217)
    assert 218 * a_max < F(1, 1152)
    assert 1152 * a_max < F(1, 4)
    assert a_max / 4 == F(1, 2**22)
    assert F(1152, 2**20) == F(9, 8192)
    return {
        "maximum_lower_contact_slope": str(a_max),
        "component_floor_coefficient": str(a_max / 4),
        "large_density_exclusion_margin": str(F(1, 1152) - 218 * a_max),
        "small_density_squared_bound": str(1152 * a_max),
        "constant_checks": "PASS",
    }


def obstruction_audit():
    # Without equality of means, a strict minimum does not select the phase.
    nodes = (F(0), F(1), F(2))
    q = (F(0), F(1, 8), F(3, 8))
    slope = F(3, 16)
    f = tuple(value - slope * r for r, value in zip(nodes, q))
    assert f[1] < f[0] and f[1] < f[2]
    weights = (F(2, 3), F(0), F(1, 3))
    mean = sum(w * r for w, r in zip(weights, nodes))
    pile_mean = sum(w * v for w, v in zip(weights, q))
    assert mean == F(2, 3) < 1
    assert pile_mean == q[1]

    # In an affine interval, even the complete one-site marginal can agree
    # while two-site laws disagree. These are illustrative probability laws,
    # explicitly NOT invariant laws of the backchip process.
    def marginal(rho):
        return (1 - 4 * rho / 5, 3 * rho / 5, rho / 5)

    left, right, middle = F(1, 2), F(1), F(3, 4)
    p_left, p_right, p_middle = map(marginal, (left, right, middle))
    mixture = tuple((x + y) / 2 for x, y in zip(p_left, p_right))
    assert mixture == p_middle
    for rho, p in ((left, p_left), (right, p_right), (middle, p_middle)):
        assert sum(p) == 1 and min(p) >= 0
        assert sum(i * p[i] for i in range(3)) == rho
        assert p[2] == rho / 5
    pure_pair = p_middle[2]**2
    mixed_pair = (p_left[2]**2 + p_right[2]**2) / 2
    assert mixed_pair - pure_pair == F(1, 400)
    # Monotone coupling: both P(X>=1)=4rho/5 and P(X>=2)=rho/5 increase.
    assert sum(p_left[1:]) < sum(p_middle[1:]) < sum(p_right[1:])
    assert p_left[2] < p_middle[2] < p_right[2]

    # Choosing a non-largest contact is not sufficient when a whole segment
    # is extremal: the endpoint mixture has interior mean and is not pure.
    assert (left + right) / 2 == middle
    assert (left / 5 + right / 5) / 2 == middle / 5
    return {
        "mean_loss_counterexample": {
            "chosen_contact": "1",
            "actual_mean": str(mean),
            "matched_Q": str(pile_mean),
        },
        "affine_mixture_obstruction": {
            "matched_one_site_law": list(map(str, p_middle)),
            "pure_two_site_pile_probability": str(pure_pair),
            "mixed_two_site_pile_probability": str(mixed_pair),
            "difference": str(mixed_pair - pure_pair),
            "scope": "Abstract probability laws, not backchip stationary measures.",
        },
        "obstruction_checks": "PASS",
    }


def main():
    results = {
        "scope": "New exact audits only; no finite-ring stationary solver or prior verifier.",
        "constants": constants_audit(),
        "contacts": contact_audit(),
        "arcs": arc_audit(),
        "obstructions": obstruction_audit(),
        "status": "PASS",
    }
    root = Path(__file__).resolve().parent
    (root / "results").mkdir(exist_ok=True)
    (root / "results" / "verified.json").write_text(json.dumps(results, indent=2) + "\n")
    (root / "results" / "environment.json").write_text(json.dumps({
        "python": sys.version,
        "platform": platform.platform(),
        "dependencies": "Python standard library only",
        "randomness": "None",
    }, indent=2) + "\n")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
