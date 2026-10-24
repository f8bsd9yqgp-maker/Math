#!/usr/bin/env python3
"""Exact audit of transfer capping and the subdivided-transition protocol.

Standard-library only. Run from any working directory. This audits finite
identities and examples; the dimension-uniform theorem has an analytic proof.
"""
from collections import defaultdict
from fractions import Fraction as Q
from pathlib import Path
import json
import sys

if not __debug__:
    raise RuntimeError('Run without -O: this verifier requires assertions.')

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / 'code'))
from exact_support import compositions, d, solve_fraction, stationary


def move(g, i, amount):
    v = list(g)
    assert 0 <= amount <= v[i]
    v[i] -= amount
    v[(i - 1) % len(g)] += amount
    return tuple(v)


def extra(amount, cap):
    return max(0, (amount + cap - 1) // cap - 1)


def solve_caps(n, h, caps):
    states = list(compositions(h, n))
    idx = {g: j for j, g in enumerate(states)}
    size = len(states)
    qt = [[0] * size for _ in states]
    for j, g in enumerate(states):
        for i in range(n):
            amount = min(d(g[i]), caps[i]) if i in caps else d(g[i])
            qt[idx[move(g, i, amount)]][j] += 1
            qt[j][j] -= 1
    a = [row[:] for row in qt]
    a[-1] = [1] * size
    rhs = [0] * size
    rhs[-1] = 1
    pi = solve_fraction(a, rhs)
    assert all(p >= 0 for p in pi) and sum(pi) == 1
    assert all(sum(x * p for x, p in zip(row, pi)) == 0 for row in qt)
    currents = [sum(p * (min(d(g[i]), caps[i]) if i in caps else d(g[i]))
                    for g, p in zip(states, pi)) for i in range(n)]
    assert len(set(currents)) == 1
    return states, pi, currents[0]


def subdivided_certificate(n, h, caps, states, pi):
    """Explicit invariant weights, checked against every extended balance.

    Active state: (g,-1,0). Intermediate state: (original_g,donor,chunks).
    Distinct labels retain the pre-event state even when physical states merge.
    At an intermediate state only the designated donor clock acts.
    """
    raw = { (g, -1, 0): p for g, p in zip(states, pi) }
    R = sum(p * extra(d(g[i]), cap) for g, p in zip(states, pi)
            for i, cap in caps.items())
    Z = 1 + R
    for g, p in zip(states, pi):
        for i, cap in caps.items():
            for ell in range(1, extra(d(g[i]), cap) + 1):
                raw[g, i, ell] = p
    assert sum(raw.values()) == Z
    law = {s: p / Z for s, p in raw.items()}
    balance = defaultdict(Q)
    currents = [Q(0)] * n
    legal_chunks = 0
    for s, p in law.items():
        g, donor, ell = s
        if donor == -1:
            events = []
            for i in range(n):
                cap = caps.get(i, h)
                amount = min(d(g[i]), cap)
                if d(g[i]) > cap:
                    target = (g, i, 1)
                else:
                    target = (move(g, i, amount), -1, 0)
                events.append((target, i, amount))
        else:
            cap = caps[donor]
            already = ell * cap
            physical = move(g, donor, already)
            remaining = d(g[donor]) - already
            amount = min(cap, remaining)
            assert 0 < amount <= min(cap, d(physical[donor]))
            if amount == remaining:
                target = (move(g, donor, d(g[donor])), -1, 0)
            else:
                target = (g, donor, ell + 1)
            events = [(target, donor, amount)]
            legal_chunks += 1
        for target, i, amount in events:
            assert target in law
            balance[target] += p
            balance[s] -= p
            currents[i] += p * amount
    assert all(balance[s] == 0 for s in law)
    F = sum(p * d(g[0]) for g, p in zip(states, pi))
    assert currents == [F / Z] * n
    return {
        'n': n, 'h': h, 'caps': caps, 'R': str(R),
        'normalizer': str(Z), 'current': str(F / Z),
        'states': [{'source': list(s[0]), 'donor': s[1], 'chunks': s[2],
                    'probability': str(p)} for s, p in law.items()],
    }, len(law), legal_chunks


def local_checks():
    count = 0
    def B(a, b):
        return min(b, max(a + 1, b - 1))
    for cap in range(1, 9):
        for mass in range(25):
            amount = d(mass)
            assert extra(amount, cap) == sum(amount > k * cap
                                            for k in range(1, 26))
            assert Q(extra(amount, cap)) <= Q(amount, cap)
            left, remaining = mass, amount
            chunks = 0
            while remaining:
                chunk = min(cap, remaining)
                assert chunk <= min(cap, d(left))
                left -= chunk
                remaining -= chunk
                chunks += 1
            assert left == mass - d(mass)
            assert max(0, chunks - 1) == extra(amount, cap)
            count += 1
        for a in range(-3, 4):
            for gap in range(12):
                b = a + gap
                v = min(a + cap, B(a, b))
                assert a <= v <= b
                for da in range(4):
                    for db in range(4):
                        aa, bb = a + da, b + db
                        if aa <= bb:
                            vv = min(aa + cap, B(aa, bb))
                            assert v <= vv
                            # Every legal partial move at the lower state
                            # lies below a full capped move at the upper state.
                            for chunk in range(v - a + 1):
                                assert a + chunk <= vv
                            count += 1
    return count


def main():
    cases = []
    balance_count = 0
    protocol_count = 0
    chunk_count = 0
    protocol_example = None
    # Full labelled chains, including transient compositions.
    for n in range(2, 5):
        for h in range(1, 6):
            states, pi = stationary(n, h)
            F = sum(p * d(g[0]) for g, p in zip(states, pi))
            candidates = [{0: 1}, {0: 2}, {0: 3},
                          {0: 1, 1: 2}, {i: 2 for i in range(n)}]
            if n >= 3:
                candidates.append({0: 2, n - 1: 3})
            for caps in candidates:
                ss, pp, FC = solve_caps(n, h, caps)
                assert ss == states
                R = sum(p * extra(d(g[i]), cap)
                        for g, p in zip(states, pi) for i, cap in caps.items())
                tail_R = sum(p for g, p in zip(states, pi)
                             for i, cap in caps.items()
                             for k in range(1, h + 1) if g[i] >= k * cap + 2)
                assert R == tail_R
                assert 0 < F / (1 + R) <= FC <= F
                cap_sum = sum(Q(1, cap) for cap in caps.values())
                assert R <= F * cap_sum
                assert 0 <= 1 / FC - 1 / F <= R / F <= cap_sum
                eta = Q(h, n)
                original_q = eta - F
                capped_q = sum(p * sum(m >= 2 for m in g) / n
                               for g, p in zip(ss, pp))
                overflow = sum(p * max(0, d(g[i]) - cap) / n
                               for g, p in zip(ss, pp) for i, cap in caps.items())
                D = max(1, h - 1)
                BH = sum(max(Q(0), Q(D, cap) - 1) for cap in caps.values())
                assert FC == eta - capped_q - overflow
                assert 0 <= overflow <= FC * BH / n
                assert -FC * BH / n <= capped_q - original_q
                assert capped_q - original_q <= F * F * cap_sum / (1 + F * cap_sum)
                assert abs(capped_q - original_q) <= eta * eta * cap_sum
                cap_mass = sum(p * g[i] / n for g, p in zip(ss, pp) for i in caps)
                mass_bound = Q(len(caps), n) + FC / n * sum(
                    max(Q(1), Q(D, cap)) for cap in caps.values())
                assert cap_mass <= mass_bound
                cert, cnt, chunks = subdivided_certificate(n, h, caps, states, pi)
                protocol_count += cnt
                chunk_count += chunks
                balance_count += len(states)
                if (n, h, caps) == (3, 5, {0: 2, 2: 3}):
                    protocol_example = cert
                cases.append({'n': n, 'h': h, 'caps': caps,
                              'F': str(F), 'F_cap': str(FC), 'R': str(R),
                              'q_original': str(original_q),
                              'q_cap_average': str(capped_q),
                              'overflow': str(overflow),
                              'protocol_current': str(F / (1 + R)),
                              'states': [list(g) for g in states],
                              'original_pi': [str(p) for p in pi],
                              'capped_pi': [str(p) for p in pp]})
    report = {'status': 'all exact assertions passed',
              'cases': len(cases), 'capped_balance_equations': balance_count,
              'protocol_balance_equations': protocol_count,
              'intermediate_chunk_checks': chunk_count,
              'local_map_checks': local_checks(),
              'scope': 'Finite audits support, but do not replace, the analytic theorem. '
                       'No thermodynamic convergence assertion is tested or proved here.'}
    out = HERE / 'results'
    out.mkdir(exist_ok=True)
    for name, value in [('verified.json', report), ('certificates.json', cases),
                        ('protocol_certificate.json', protocol_example)]:
        (out / name).write_text(json.dumps(value, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
