"""Audit only the new sharp-workload lemmas; no stationary solves.

Imports the previously audited deterministic update and projection as fixtures.
All new assertions use integer or Fraction arithmetic.
"""

import json
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path

from verify import (compositions, d, original_update, remaining, run_word,
                    serialized_word)


def upstream_word(selected, n):
    selected = set(selected)
    assert len(selected) < n
    word = []
    while selected:
        eligible = [i for i in selected if (i + 1) % n not in selected]
        assert eligible
        for i in sorted(eligible):
            word.append(i)
            selected.remove(i)
    return word


def excess(r):
    return sum(r) - max(r)


def audit_pair(n, h):
    counts = dict.fromkeys([
        "mask_projection_upper", "remaining_workload_perturbation",
        "excess_workload_perturbation", "negative_coin_necessity",
        "dominating_word", "single_coin_structure", "rest_excess_bound",
        "isolated_word_commutations"], 0)
    masks = list(product((0, 1), repeat=n))
    for g in compositions(h, n):
        for a in masks:
            ell = remaining(g, a)
            c = tuple(int(a[i] and g[i] >= 2) for i in range(n))
            projected = tuple(g[i] + ell[(i + 1) % n] - ell[i]
                              for i in range(n))
            assert min(projected) >= 0 and sum(projected) == h
            r = tuple(a[i] + ell[i] for i in range(n))
            k = sum(a)
            assert sum(ell) - sum(r) == -k
            assert excess(ell) - excess(r) == -max(k - 1, 0)
            for coins in masks:
                gg, vv = original_update(g, a, coins)
                ee = remaining(gg, vv)
                delta = tuple(vv[i] + ee[i] - ell[i] for i in range(n))
                rr = tuple(int(vv[i] > 0) + ee[i] for i in range(n))
                kk = sum(coins)
                budget = sum(coins[i] * d(projected[i]) for i in range(n))
                assert max(delta) <= budget
                counts["mask_projection_upper"] += 1
                positive = sum(max(rr[i] - ell[i], 0) for i in range(n))
                assert positive <= (k + kk) * budget
                counts["remaining_workload_perturbation"] += 1
                assert excess(rr) - excess(ell) <= positive
                counts["excess_workload_perturbation"] += 1
                candidates = [i for i in range(n)
                              if c[i] and c[(i + 1) % n] and g[i] == 2]
                assert len(candidates) <= max(k - 1, 0)
                if min(delta) < 0:
                    assert any(coins[i] for i in candidates)
                counts["negative_coin_necessity"] += 1
                selected = [i for i in range(n) if c[i] or coins[i]]
                if len(selected) < n:
                    word = upstream_word(selected, n)
                    _, disp = run_word(projected, word)
                    assert all(disp[i] >= delta[i] for i in range(n))
                    assert len(word) <= k + kk
                    counts["dominating_word"] += 1
                else:
                    assert k + kk >= n and max(delta) <= h
                if kk == 1:
                    j = coins.index(1)
                    if not c[j]:
                        if g[j] == 0:
                            assert not any(delta)
                        else:
                            amount = delta[j]
                            assert 1 <= amount <= d(projected[j])
                            support = {j}
                            i = (j - 1) % n
                            while c[i]:
                                support.add(i)
                                i = (i - 1) % n
                            assert delta == tuple(amount * int(i in support)
                                                  for i in range(n))
                            if len(support) < n:
                                word = [j]
                                i = (j - 1) % n
                                while c[i]:
                                    word.append(i)
                                    i = (i - 1) % n
                                _, disp = run_word(projected, word)
                                assert all(disp[i] >= delta[i] for i in range(n))
                    elif g[j] == 2 and not c[(j + 1) % n]:
                        support = {j}
                        i = (j - 1) % n
                        while c[i]:
                            support.add(i)
                            i = (i - 1) % n
                        assert delta == tuple(int(i in support) for i in range(n))
                    else:
                        assert max(delta) <= 0
                    counts["single_coin_structure"] += 1
                if k == 0:
                    assert excess(rr) <= max(kk - 1, 0) * budget
                    counts["rest_excess_bound"] += 1
                    if n <= 4:
                        marked = [i for i in range(n) if coins[i]]
                        bad = {i for i in marked
                               if coins[(i - 1) % n] or coins[(i + 1) % n]}
                        isolated = [i for i in marked if i not in bad]
                        serial = serialized_word(g, coins)
                        assert run_word(g, serial) == run_word(
                            g, isolated + [i for i in serial if i in bad])
                        for order in permutations(marked):
                            assert run_word(g, order) == run_word(
                                g, isolated + [i for i in order if i in bad])
                            counts["isolated_word_commutations"] += 1
    return {"N": n, "H": h, "counts": counts, "status": "passed_exactly"}


def constants():
    count = 0
    for n in range(2, 31):
        for h in range(1, 2 * n):
            density = F(h, n)
            for fraction in (F(1, 9), F(1, 2), F(1)):
                eps = fraction / (2 * max(n, h))
                bound_m = eps * h * (1 + (n - 1) * eps) / (1 - eps * h)
                assert bound_m <= 3 * eps * h
                for flow in (density / 2, density):
                    upper = F(5 * n - 1, 2) * eps * flow + 4 * flow * bound_m
                    upper += 3 * eps * flow * n * (n - 1) * bound_m
                    lower = flow * (bound_m + (n - 1) * eps)
                    lower += (h - 1) * (2 * eps * h * bound_m
                                        + eps ** 2 * h * (n - 1))
                    coarse = ((12 * density ** 2 + 3 * density) * eps * n
                              + (6 * density ** 3 + 10 * density ** 2)
                              * eps ** 2 * n ** 3)
                    assert upper <= coarse and lower <= coarse
                    count += 1
    return count


def main():
    pairs = [audit_pair(n, h) for n in range(2, 6)
             for h in range(1, min(2 * n, 7))]
    totals = {key: sum(p["counts"][key] for p in pairs)
              for key in pairs[0]["counts"]}
    result = {"status": "all_passed_exactly", "pairs": pairs,
              "totals": totals, "rational_constant_checks": constants(),
              "scope": "New sharp-workload inequalities only; no stationary solves."}
    out = Path(__file__).resolve().parent / "results" / "sharp_workloads.json"
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "totals": totals,
                      "rational_constant_checks": result["rational_constant_checks"]}))


if __name__ == "__main__":
    main()
