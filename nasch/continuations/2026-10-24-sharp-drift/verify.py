#!/usr/bin/env python3
"""Exact, standard-library audit of the sharp local drift certificate.

All inequalities use integers. Stationary examples use rational arithmetic.
No optimizer, simulation, tolerance, or numerical extrapolation is used.
The analytic reduction from all masses to the finite certificate is in README.
"""
from fractions import Fraction
from itertools import product
from pathlib import Path
import json
import sys

if not __debug__:
    raise RuntimeError('Run without -O: assertions are part of this audit.')

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / 'code'))
from exact_support import compositions, ring_move, stationary

CERT = json.loads((HERE / 'certificate.json').read_text())
P, W = CERT['P'], CERT['W']


def p(a, b):
    return P[min(a, 3)][min(b, 3)]


def w(a, b, c):
    return W[min(a, 3)][min(b, 3)][min(c, 3)]


def delta(a, b, c, e, v):
    return (p(a, b + v) - p(a, b) + p(b + v, c - v) - p(b, c)
            + p(c - v, e) - p(c, e))


def residual(a, b, c, e):
    r = int(c >= 2)
    return (5*c - 17*r + delta(a, b, c, e, c-r)
            + w(a, b, c) - w(b, c, e))


def phi(g):
    return sum(p(g[i], g[(i+1) % len(g)]) for i in range(len(g)))


def main():
    assert CERT['coefficient_mass'] == 5
    assert CERT['coefficient_pile'] == 17
    assert len(P) == 4 and all(len(row) == 4 for row in P)
    assert len(W) == 4 and all(len(sl) == 4 for sl in W)
    assert all(len(row) == 4 for sl in W for row in sl)
    assert all(type(x) is int for row in P for x in row)
    assert all(type(x) is int for sl in W for row in sl for x in row)
    assert min(x for row in P for x in row) == 0
    assert max(x for row in P for x in row) == 15

    vals, jumps = [], []
    for a, b, e in product(range(4), repeat=3):
        for c in range(5):
            z = residual(a, b, c, e)
            assert z >= 0
            assert z >= max(0, 5*c-18)
            vals.append(z)
            jumps.append(delta(a, b, c, e, c-int(c >= 2)))
    minima = [[[min(residual(a, b, c, e) for a in range(4))
                for e in range(4)] for b in range(4)] for c in range(5)]
    assert minima == CERT['minimum_tables']
    assert max(map(abs, jumps)) == CERT['jump_bound'] == 14

    # Supplementary check of the analytic clipping reduction, not its proof.
    reduction_checks = 0
    for a, b, c, e in product(range(10), repeat=4):
        cc = min(c, 4)
        assert residual(a, b, c, e) == (
            residual(min(a, 3), min(b, 3), cc, min(e, 3)) + 5*(c-cc))
        reduction_checks += 1

    defects = []
    for a, b, e in product(range(4), repeat=3):
        for c in range(8):
            full = delta(a, b, c, e, c-int(c >= 2))
            for v in range(c-int(c >= 2)+1):
                defects.append(full-delta(a, b, c, e, v))
    assert max(defects) == CERT['partial_defect_bound'] == 14
    # For c>=4, every partial-transfer category has a representative c'<=6.
    representatives = {}
    for c in range(4, 8):
        for v in range(c):
            representatives[(min(v, 3), min(c-v, 3))] = (c, v)
    partial_reduction_checks = 0
    for c in range(4, 100):
        for v in range(c):
            cc, vv = representatives[(min(v, 3), min(c-v, 3))]
            for a, b, e in [(0, 0, 0), (3, 3, 3), (1, 2, 3), (2, 1, 0)]:
                assert delta(a, b, c, e, v) == delta(a, b, cc, e, vv)
                assert delta(a, b, c, e, c-1) == delta(a, b, cc, e, cc-1)
                partial_reduction_checks += 1

    # Independent global updates: compute actual Phi before and after moves.
    # Includes N=3, where a=e but the three affected bonds are distinct.
    states_checked = event_checks = 0
    for n in range(3, 7):
        for h in range(9):
            for g in compositions(h, n):
                pg = phi(g)
                generator = 0
                for i in range(n):
                    actual = phi(ring_move(g, i)) - pg
                    local = delta(g[(i-2) % n], g[(i-1) % n], g[i],
                                  g[(i+1) % n], g[i]-int(g[i] >= 2))
                    assert actual == local and abs(actual) <= 14
                    generator += actual
                    event_checks += 1
                qcount = sum(m >= 2 for m in g)
                rz = sum(residual(g[(i-2) % n], g[(i-1) % n], g[i],
                                  g[(i+1) % n]) for i in range(n))
                assert generator == 17*qcount - 5*h + rz
                assert generator >= 17*qcount - 5*h
                assert rz >= sum(max(0, 5*m-18) for m in g)
                states_checked += 1

    examples = []
    balance_checks = 0
    for n, h in [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5),
                 (4, 3), (4, 4), (5, 3), (5, 4), (6, 3), (2, 2)]:
        states, weights = stationary(n, h)
        balance_checks += len(states)
        q = sum(v*int(g[0] >= 2) for g, v in zip(states, weights))
        slack = Fraction(5*h, n)-17*q
        if n >= 3:
            assert slack >= 0
            assert sum(v*sum(residual(g[(i-2) % n], g[(i-1) % n], g[i],
                                     g[(i+1) % n]) for i in range(n))
                       for g, v in zip(states, weights)) == n*slack
        if (n, h) == (3, 3):
            assert q == Fraction(5, 17) and slack == 0
        if (n, h) == (2, 2):
            assert q == Fraction(1, 3) > Fraction(5*h, 17*n)
        examples.append({'N': n, 'H': h, 'q': str(q),
                         'slack_per_site': str(slack),
                         'states': [list(g) for g in states],
                         'pi': [str(v) for v in weights]})

    # Negative dependence is not preserved, even from a deterministic state.
    # Count all short clock words; rates remain four including null events.
    initial = (0, 0, 0, 7)
    word_counts = []
    joint_words = []
    for length in range(5):
        counts = [0, 0, 0]
        for word in product(range(4), repeat=length):
            g = initial
            for i in word:
                g = ring_move(g, i)
            f, h = int(g[0] >= 2), int(g[1] >= 2)
            counts[0] += f
            counts[1] += h
            counts[2] += f*h
            if f*h:
                joint_words.append({'word': list(word), 'terminal': list(g)})
        word_counts.append(counts)
    assert word_counts == [[0, 0, 0], [0, 0, 0], [0, 1, 0],
                           [1, 9, 0], [12, 55, 1]]
    assert joint_words == [{'word': [3, 2, 1, 2], 'terminal': [4, 2, 0, 1]}]
    # An explicit positive covariance lower bound for 0<t<=1/4096:
    assert (1-4*Fraction(1, 4096))/24 - Fraction(4**5, 12*4096) > 0

    # One bond capped at two is unchanged for N=2, H<=3.
    # The stationary current is not concave in H.
    capped_currents = [Fraction(1, 2), Fraction(2, 3), Fraction(1)]
    for mass, expected in enumerate(capped_currents, 1):
        ss, pp = stationary(2, mass)
        for g in ss:
            assert g[0]-int(g[0] >= 2) <= 2
        actual = sum(p*(g[0]-int(g[0] >= 2)) for g, p in zip(ss, pp))
        assert actual == expected
    assert capped_currents[2]-2*capped_currents[1]+capped_currents[0] == Fraction(1, 6)

    report = {
        'status': 'all exact assertions passed',
        'essential_integer_inequalities': len(vals),
        'minimum_residual': min(vals), 'maximum_finite_residual': max(vals),
        'zero_residuals': vals.count(0), 'minimum_tables': minima,
        'potential_range': [0, 15], 'maximum_absolute_jump': 14,
        'partial_defect_inequalities': len(defects), 'maximum_partial_defect': 14,
        'supplementary_clipping_checks': reduction_checks,
        'supplementary_partial_clipping_checks': partial_reduction_checks,
        'global_ring_states': states_checked, 'global_clock_events': event_checks,
        'stationary_chains': len(examples), 'stationary_balance_equations': balance_checks,
        'negative_dependence_short_words': sum(4**k for k in range(5)),
        'negative_dependence_word_counts': word_counts,
        'negative_dependence_joint_word': joint_words[0],
        'capped_current_concavity_counterexample': {
            'N': 2, 'cap_at_site_zero': 2, 'H': [1, 2, 3],
            'currents': list(map(str, capped_currents)), 'second_difference': '1/6'},
        'scope': 'Sharp universal finite-system bound, finite-time upper envelope, '
                 'and finite-defect corollaries. No thermodynamic convergence claim.'
    }
    out = HERE / 'results'
    out.mkdir(exist_ok=True)
    (out / 'verified.json').write_text(json.dumps(report, indent=2)+'\n')
    (out / 'stationary_certificates.json').write_text(json.dumps(examples, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
