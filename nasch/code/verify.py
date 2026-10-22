#!/usr/bin/env python3
"""Exact finite audits accompanying density_phases_proof.md.

No simulation and no inference of an infinite-volume theorem from finite data.
The measure-theoretic arguments are in the report, not certified by this script.
Python standard library only.
"""
from fractions import Fraction
from itertools import product
from pathlib import Path
import argparse
import json
from exact_support import compositions, stationary


def r(n):
    return int(n >= 2)


def d(n):
    return n - r(n)


def move(g, i):
    h = list(g)
    amount = d(h[i])
    h[i] -= amount
    h[(i - 1) % len(h)] += amount
    return tuple(h)



def capped_discrepancy():
    """Audit the bounded identity (6) and subadditivity used before Fatou."""
    split_count = subadditivity_count = 0
    for lower, upper in product(range(18), repeat=2):
        delta = upper - lower
        residual = r(upper) - r(lower)
        sent = d(upper) - d(lower)
        assert delta == residual + sent
        assert residual * sent >= 0 and abs(residual) <= 1
        for cap in range(1, 19):
            f = lambda value: min(abs(value), cap)
            expected = int(abs(residual) == 1 and abs(sent) >= cap)
            assert f(residual) + f(sent) - f(delta) == expected
            split_count += 1
    for x, y in product(range(-18, 19), repeat=2):
        for cap in range(1, 19):
            f = lambda value: min(abs(value), cap)
            assert f(x) + f(y) - f(x + y) >= 0
            subadditivity_count += 1
    return {
        'donor_split_identities': split_count,
        'subadditivity_cases': subadditivity_count,
    }

def local_loss():
    count = 0
    for a, b, c, e in product(range(10), repeat=4):
        x, y = b - a, e - c
        rr, dd = r(b) - r(a), d(b) - d(a)
        incoming = d(e) - d(c)
        loss = abs(x) + abs(incoming) - abs(x + incoming)
        assert abs(x) == abs(rr) + abs(dd)
        assert loss == 2 * min(abs(x), abs(incoming)) * (x * incoming < 0)
        # Receiving + donor increments, with the translation-canceling term.
        generator = abs(rr) - abs(x) + abs(x + incoming) - abs(x)
        assert generator == abs(incoming) - abs(dd) - loss
        count += 1
    return count


def ring_loss_and_gather():
    count = gather_count = 0
    # Different total masses included; no stationarity assumption in identity.
    for n, bound in [(2, 5), (3, 4), (4, 3)]:
        states = [g for h in range(bound + 1) for g in compositions(h, n)]
        for g, h in product(states, repeat=2):
            delta = tuple(y - x for x, y in zip(g, h))
            incoming = tuple(d(y) - d(x) for x, y in zip(g, h))
            old = sum(map(abs, delta))
            for i in range(n):
                gg, hh = move(g, i), move(h, i)
                new = sum(abs(y - x) for x, y in zip(gg, hh))
                z, w = delta[(i - 1) % n], incoming[i]
                assert new - old == -2 * min(abs(z), abs(w)) * (z * w < 0)
                count += 1
            gg, hh = g, h
            for i in range(n - 1, 0, -1):
                gg, hh = move(move(gg, i), i), move(move(hh, i), i)
            assert gg == (sum(g),) + (0,) * (n - 1)
            assert hh == (sum(h),) + (0,) * (n - 1)
            assert sum(abs(y - x) for x, y in zip(gg, hh)) == abs(sum(h) - sum(g))
            gather_count += 1
    return count, gather_count


def boundary_conservation():
    count = 0
    for n in range(2, 8):
        for total in range(6):
            for g in compositions(total, n):
                for length in range(1, n):
                    block = set(range(length))
                    for i in range(n):
                        h = move(g, i)
                        change = sum(h[j] - g[j] for j in block)
                        expected = d(g[i]) * (int((i - 1) % n in block) - int(i in block))
                        assert change == expected
                        count += 1
    return count


def fifo_lifetime():
    count = 0
    # Arrival event sizes 0,1,2,3 and service event S. Queue order is oldest first.
    for initial in range(5):
        for length in range(1, 7):
            for word in product(range(5), repeat=length):
                queue = list(range(initial))
                next_label = initial
                services_seen = {label: 0 for label in queue}
                for event in word:
                    if event < 4:
                        arrivals = list(range(next_label, next_label + event))
                        next_label += event
                        queue.extend(arrivals)
                        services_seen.update({label: 0 for label in arrivals})
                    else:
                        for label in queue:
                            services_seen[label] += 1
                        retained = queue[-1:] if len(queue) >= 2 else []
                        departed = queue[:-1] if len(queue) >= 2 else queue[:]
                        assert all(services_seen[label] <= 2 for label in departed)
                        queue = retained
                        assert all(services_seen[label] <= 1 for label in queue)
                count += 1
    # Real particles leave quickly, but one-unit memory can perpetually change label.
    low, high = 0, 1
    for _ in range(100):
        low, high = r(low + 1), r(high + 1)
        assert (low, high) == (0, 1)
    return count


def occupation_projection_probe():
    results = []
    for total in range(2, 9):
        states, probabilities = stationary(4, total)
        adjacent = sum((p for g, p in zip(states, probabilities)
                        if tuple(int(x > 0) for x in g) == (1, 1, 0, 0)), Fraction())
        separated = sum((p for g, p in zip(states, probabilities)
                         if tuple(int(x > 0) for x in g) == (1, 0, 1, 0)), Fraction())
        results.append({'N': 4, 'H': total,
                        'P_1100': str(adjacent), 'P_1010': str(separated),
                        'difference': str(adjacent - separated)})
    assert results[1]['P_1100'] == '7/76'
    assert results[1]['P_1010'] == '3/38'
    assert results[1]['difference'] == '1/76'
    return results


if __name__ == '__main__':
    if not __debug__:
        raise SystemExit('Run without -O: this verifier uses assertions.')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='Optional JSON output path')
    args = parser.parse_args()
    transitions, gatherings = ring_loss_and_gather()
    result = {
        'status': 'PASS',
        'capped_discrepancy': capped_discrepancy(),
        'local_discrepancy_quadruples': local_loss(),
        'ring_discrepancy_transitions': transitions,
        'two_copy_gatherings': gatherings,
        'boundary_current_identities': boundary_conservation(),
        'fifo_initial_states_and_event_words': fifo_lifetime(),
        'finite_occupation_projection': occupation_projection_probe(),
        'limits': 'Finite identities only. No numerical certification of measure-theoretic or thermodynamic claims.'
    }
    rendered = json.dumps(result, indent=2) + '\n'
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding='utf-8')
    print(rendered, end='')

