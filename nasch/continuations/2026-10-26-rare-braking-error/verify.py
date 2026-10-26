"""Exact audit of new NaSch relaxation, serialization and error-bound lemmas.

No stationary distribution or previous Poisson system is solved. Counts refer
to new identities, not to an independent verification of the full theorem.
Python standard library only.
"""

import json
import platform
from fractions import Fraction as F
from itertools import product
from pathlib import Path


def compositions(h, n):
    if n == 1:
        yield (h,)
    else:
        for x in range(h + 1):
            for y in compositions(h - x, n - 1):
                yield (x,) + y


def d(m):
    return m - int(m >= 2)


def update(g, a, coins):
    """Exact v_max=2 gap/activity quotient; retain actual new velocities."""
    n = len(g)
    velocities = tuple(int(a[i] > 0 and g[i] >= 2)
                       + int(coins[i] and g[i] >= 1) for i in range(n))
    gaps = tuple(g[i] + velocities[(i + 1) % n] - velocities[i]
                 for i in range(n))
    assert min(gaps) >= 0
    return gaps, velocities


def original_update(g, v, coins):
    """Independent implementation of acceleration, gap cap, braking, motion."""
    n = len(g)
    new_v = []
    for i in range(n):
        attempted = min(v[i] + 1, 2, g[i])
        new_v.append(max(attempted - (1 - coins[i]), 0))
    gaps = tuple(g[i] + new_v[(i + 1) % n] - new_v[i] for i in range(n))
    return gaps, tuple(new_v)


def remaining(g, a):
    """Explicit future displacement under full braking."""
    n = len(g)
    qualified = [a[i] > 0 and g[i] >= 2 for i in range(n)]
    assert not all(qualified)
    result = []
    for i in range(n):
        value, j = 0, i
        while qualified[j]:
            value += g[j] - 1
            j = (j + 1) % n
        result.append(value)
    return tuple(result)


def rest_time(g, a):
    return 1 + max(remaining(g, a)) if any(a) else 0


def serialized_word(g, coins):
    """Singleton triggers first; then big triggers with upstream first."""
    n = len(g)
    singles = [i for i in range(n) if coins[i] and g[i] == 1]
    big = {i for i in range(n) if coins[i] and g[i] >= 2}
    assert len(big) < n
    word = singles[:]
    while big:
        eligible = [i for i in big if (i + 1) % n not in big]
        assert eligible
        for i in sorted(eligible):
            word.append(i)
            big.remove(i)
    return word


def run_word(g, word):
    gaps = list(g)
    displacement = [0] * len(g)
    for i in word:
        amount = d(gaps[i])
        gaps[i] -= amount
        gaps[(i - 1) % len(g)] += amount
        displacement[i] += amount
    return tuple(gaps), tuple(displacement)


def audit_local_rule():
    count = 0
    for gap, v, coin in product(range(21), range(3), range(2)):
        direct = max(min(v + 1, 2, gap) - (1 - coin), 0)
        binary = int(v > 0 and gap >= 2) + coin * int(gap >= 1)
        assert direct == binary
        count += 1
    return count


def audit_pair(n, h):
    counts = {key: 0 for key in (
        "initial_activity_states", "explicit_relaxation_steps",
        "rest_time_descent", "projected_invariance", "arbitrary_coin_updates",
        "projection_shift_bounds", "active_workload_perturbation_bounds",
        "rest_serializations", "rest_workload_bounds")}
    zeros = (0,) * n
    masks = list(product(range(2), repeat=n))
    for g in compositions(h, n):
        # New simultaneous-trigger serialization, from rest.
        for coins in masks:
            next_g, v = original_update(g, zeros, coins)
            rem = remaining(next_g, v)
            actual_displacement = tuple(v[i] + rem[i] for i in range(n))
            actual_g = tuple(g[i] + actual_displacement[(i + 1) % n]
                             - actual_displacement[i] for i in range(n))
            predicted_g, predicted_displacement = run_word(
                g, serialized_word(g, coins))
            assert actual_displacement == predicted_displacement
            assert actual_g == predicted_g
            counts["rest_serializations"] += 1
            r = rest_time(next_g, v)
            assert r <= sum(coins[i] * d(g[i]) for i in range(n))
            counts["rest_workload_bounds"] += 1

        for a in masks:
            rem = remaining(g, a)
            r = rest_time(g, a)
            assert 0 <= r <= h
            assert max(rem) <= h - 1
            counts["initial_activity_states"] += 1
            cumulative = [0] * n
            gg, vv = g, a
            for t in range(1, r + 1):
                gg, vv = original_update(gg, vv, zeros)
                cumulative = [cumulative[i] + vv[i] for i in range(n)]
                assert cumulative == [min(t, rem[i]) for i in range(n)]
                counts["explicit_relaxation_steps"] += 1
            assert not any(vv)
            base_g, base_v = update(g, a, zeros)
            assert rest_time(base_g, base_v) == max(r - 1, 0)
            counts["rest_time_descent"] += 1
            base_rem = remaining(base_g, base_v)
            assert all(base_v[i] + base_rem[i] == rem[i] for i in range(n))
            counts["projected_invariance"] += 1

            for coins in masks:
                next_g, next_v = update(g, a, coins)
                assert (next_g, next_v) == original_update(g, a, coins)
                next_rem = remaining(next_g, next_v)
                shift = [next_v[i] + next_rem[i] - rem[i] for i in range(n)]
                assert min(shift) >= -(h - 1) and max(shift) <= h + 1
                counts["arbitrary_coin_updates"] += 1
                counts["projection_shift_bounds"] += 1
                if r:
                    assert rest_time(next_g, next_v) - r <= (
                        -1 + h * int(any(coins)))
                    counts["active_workload_perturbation_bounds"] += 1
    return {"N": n, "H": h, "counts": counts, "status": "passed_exactly"}


def audit_probability_bounds():
    count = 0
    for n in range(2, 31):
        for eps in (F(1, 10000), F(1, 100), F(1, 10), F(1, 2), F(1)):
            a = (1 - eps) ** (n - 1)
            low = eps * a
            high = eps * a + n * eps * (1 - a)
            assert eps - low <= (n - 1) ** 2 * eps ** 2
            assert high - eps <= (n - 1) ** 2 * eps ** 2
            for h in range(1, 2 * n):
                eps_small = F(1, 2 * h * (n - 1))
                probability_bound = eps_small * h / (
                    1 - eps_small * h * (n - 1))
                assert probability_bound == 2 * eps_small * h
                density = F(h, n)
                # Use F_current <= density and denominator >= 1/2.
                error_over_eps = 2 * h * (n * (h + 1) + density)
                error_over_eps += (n - 1) ** 2 * density
                assert error_over_eps <= (4 * density ** 2 + 3 * density) * n ** 3
                count += 1
    return count


def audit_acceleration_counterexample():
    rows = []
    for n in range(6, 107):
        m = n - 3
        g = (1, 2, m) + (0,) * (n - 3)
        v = (0, 1, 1) + (0,) * (n - 3)
        preparation = (0, 2, m + 1) + (0,) * (n - 3)
        prep_coins = (0, 1, 1) + (0,) * (n - 3)
        assert original_update(preparation, (0,) * n, prep_coins) == (g, v)
        base = remaining(g, v)
        extra = (0, 1, 0) + (0,) * (n - 3)
        next_g, next_v = original_update(g, v, extra)
        tail = remaining(next_g, next_v)
        changed = tuple(next_v[i] + tail[i] for i in range(n))
        difference = tuple(changed[i] - base[i] for i in range(n))
        assert difference[1] == -(n - 5)
        assert all(difference[i] == 0 for i in range(n) if i != 1)
        rows.append({"N": n, "H": n, "travel_loss": n - 5})
    return rows


def main():
    records = []
    for n in range(2, 6):
        for h in range(1, min(2 * n, 7)):
            row = audit_pair(n, h)
            records.append(row)
            print(f"N={n}, H={h}: new structural identities passed", flush=True)
    totals = {key: sum(row["counts"][key] for row in records)
              for key in records[0]["counts"]}
    totals["local_velocity_rules"] = audit_local_rule()
    totals["rational_probability_and_constant_checks"] = audit_probability_bounds()
    counterexamples = audit_acceleration_counterexample()
    totals["acceleration_counterexamples"] = len(counterexamples)
    report = {"status": "all_passed_exactly", "arithmetic": "integers and Fraction",
              "old_stationary_or_poisson_solvers_rerun": False,
              "pairs": records, "totals": totals,
              "acceleration_counterexamples": counterexamples}
    destination = Path(__file__).parent / "results"
    destination.mkdir(exist_ok=True)
    (destination / "verified.json").write_text(json.dumps(report, indent=2) + "\n")
    (destination / "environment.json").write_text(json.dumps({
        "python": platform.python_version(), "platform": platform.platform(),
        "third_party_dependencies": []}, indent=2) + "\n")
    print(json.dumps(totals, sort_keys=True))


if __name__ == "__main__":
    main()
