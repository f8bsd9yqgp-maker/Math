#!/usr/bin/env python3
"""Exact audit of the complete recurrent support and reverse gathering.

Each constructed reverse edge is checked by the original forward map.
An independent forward reachability search checks the support on small rings.
"""
from collections import deque
from pathlib import Path
import json
import sys

if not __debug__:
    raise RuntimeError('Run without -O.')

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / 'code'))
from exact_support import compositions, ring_move, stationary


def reverse_gather(initial):
    n, total = len(initial), sum(initial)
    assert n >= 2 and min(initial) <= 1
    g = list(initial)
    events = []

    def reverse(j, amount):
        old = tuple(g)
        left = (j-1) % n
        assert amount >= 1 and amount <= g[left]
        assert (g[j] == 0 and amount == 1) or g[j] == 1
        g[left] -= amount
        g[j] += amount
        assert ring_move(tuple(g), j) == old
        events.append(j)

    def swap_into_zero(j):
        assert g[j] == 0
        mass = g[(j-1) % n]
        if mass:
            reverse(j, 1)
            if mass > 1:
                reverse(j, mass-1)

    if total == 0:
        return tuple(g), events
    if 0 not in g:
        singleton = next(i for i, x in enumerate(g) if x == 1)
        reverse(singleton, g[(singleton-1) % n])
        head = singleton
    else:
        head = next(i for i, x in enumerate(g) if x)

    while g[head] < total:
        old_head_mass = g[head]
        # Move the head clockwise through zeros to its next positive neighbor.
        while g[(head+1) % n] == 0:
            swap_into_zero((head+1) % n)
            head = (head+1) % n
        b = (head+1) % n
        if g[b] == 1:
            reverse(b, g[head])
            head = b
        else:
            # There is a zero outside the adjacent positive head and neighbor.
            assert n >= 3
            c = (b+1) % n
            zero = next(i for i, x in enumerate(g) if x == 0)
            steps = 0
            while zero != c:
                assert zero not in (head, b)
                assert (zero-1) % n not in (head, b)
                swap_into_zero(zero)
                zero = (zero-1) % n
                steps += 1
                assert steps <= n-3
            neighbor = g[b]
            reverse(c, 1)
            if neighbor > 2:
                reverse(c, neighbor-2)
            assert g[b] == 1
            reverse(b, g[head])
            head = b
        assert g[head] == old_head_mass+1
        assert sum(g) == total and 0 in g
    assert sum(x > 0 for x in g) == 1 and max(g) == total
    # Reverse the entire path with the original transition, independently.
    back = tuple(g)
    for clock in reversed(events):
        back = ring_move(back, clock)
    assert back == initial
    return tuple(g), events


def main():
    paths = edges = longest = 0
    for n in range(2, 8):
        for h in range(11):
            for g in compositions(h, n):
                if min(g) <= 1:
                    final, events = reverse_gather(g)
                    paths += 1
                    edges += len(events)
                    longest = max(longest, len(events))

    graphs = graph_states = 0
    for n in range(2, 7):
        for h in range(9):
            start = (h,)+(0,)*(n-1)
            seen = {start}
            todo = deque([start])
            while todo:
                g = todo.popleft()
                for i in range(n):
                    y = ring_move(g, i)
                    if y not in seen:
                        seen.add(y)
                        todo.append(y)
            expected = {g for g in compositions(h, n) if min(g) <= 1}
            assert seen == expected
            # Every state with all coordinates >=2 exits that set at every clock.
            for g in compositions(h, n):
                if min(g) >= 2:
                    assert all(min(ring_move(g, i)) <= 1 for i in range(n))
            graphs += 1
            graph_states += len(list(compositions(h, n)))

    output = {
        'status': 'all exact assertions passed',
        'reverse_gathering_paths': paths, 'verified_reverse_edges': edges,
        'longest_constructed_path': longest,
        'independent_forward_graphs': graphs,
        'full_compositions_in_graph_checks': graph_states,
        'scope': 'Exact recurrent support plus constructive finite-word proof. '
                 'Matrix obstructions follow algebraically; no thermodynamic limit.'
    }
    # A rank-one zero matrix would make the following two weights equal.
    states, weights = stationary(6, 6)
    law = dict(zip(states, weights))
    a, b = (2, 0, 1, 0, 3, 0), (2, 0, 3, 0, 1, 0)
    assert law[a] > law[b] > 0
    assert str(law[a]-law[b]) == (
        '8030111479223579770784500683368006/'
        '49823178685960907060573907009905368591')
    zero_certificate = {
        'N': 6, 'H': 6, 'a': list(a), 'b': list(b),
        'pi_a': str(law[a]), 'pi_b': str(law[b]),
        'difference': str(law[a]-law[b]),
        'states': [list(g) for g in states],
        'pi': [str(p) for p in weights]
    }
    (HERE/'results'/'zero_matrix_certificate.json').write_text(
        json.dumps(zero_certificate, indent=2)+'\n')
    output['rank_one_zero_counterexample_balance_equations'] = len(states)
    output['rank_one_zero_counterexample_difference'] = zero_certificate['difference']
    (HERE/'results'/'support_verified.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
