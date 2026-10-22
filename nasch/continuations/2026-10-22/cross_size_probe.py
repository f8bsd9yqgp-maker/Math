"""Exploratory stationary computations; floats are not proof certificates.

The chain is quotiented by rotations. Exact arithmetic is available for any
putative counterexample. All clocks, including null moves, have rate one.
"""
import argparse
import json
import math
import sys
from pathlib import Path

import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'code'))
from exact_support import compositions, ring_move, solve_fraction


def canonical(g):
    return min(g[i:] + g[:i] for i in range(len(g)))


def generator(n, h):
    states = sorted({canonical(g) for g in compositions(h, n)})
    index = {g: i for i, g in enumerate(states)}
    rows, cols, vals = [], [], []
    for j, g in enumerate(states):
        for i in range(n):
            k = index[canonical(ring_move(g, i))]
            if k != j:
                rows.extend([k, j])
                cols.extend([j, j])
                vals.extend([1, -1])
    return states, coo_matrix((vals, (rows, cols)), shape=(len(states),)*2).tocsc()


def stationary_q(n, h, exact=False):
    states, qt = generator(n, h)
    if exact:
        a = qt.toarray().tolist()
        a[-1] = [1] * len(states)
        p = solve_fraction(a, [0]*(len(states)-1) + [1])
        assert all(x >= 0 for x in p) and sum(p) == 1
        raw = qt.toarray().tolist()
        assert all(sum(a*b for a, b in zip(row, p)) == 0 for row in raw)
        return sum(x * sum(k >= 2 for k in g) / n for g, x in zip(states, p))
    a = qt.tolil()
    a[-1, :] = np.ones(len(states))
    b = np.zeros(len(states))
    b[-1] = 1
    p = spsolve(a.tocsc(), b)
    residual = max(abs(qt @ p))
    assert p.min() > -1e-10 and residual < 1e-9 and abs(p.sum()-1) < 1e-9
    q = sum(x * sum(k >= 2 for k in g) / n for g, x in zip(states, p))
    return float(q), len(states), float(residual)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-n', type=int, default=10)
    parser.add_argument('--max-h', type=int, default=20)
    parser.add_argument('--max-compositions', type=int, default=100000)
    parser.add_argument('--output', default=str(Path(__file__).resolve().parent / 'results' / 'cross_size_probe.json'))
    args = parser.parse_args()
    data = {}
    for n in range(2, args.max_n + 1):
        for h in range(1, args.max_h + 1):
            if math.comb(n+h-1, n-1) <= args.max_compositions:
                q, size, residual = stationary_q(n, h)
                data[n, h] = q
                print(n, h, q, size, residual, flush=True)
    failures = {name: [] for name in ['join_n_plus_m', 'join_n_plus_m_minus_1', 'ratio_order']}
    counts = dict.fromkeys(failures, 0)
    for (n, h), q in data.items():
        for (m, k), r in data.items():
            for shift, name in [(0, 'join_n_plus_m'), (-1, 'join_n_plus_m_minus_1')]:
                if (n+m+shift, h+k-1) in data:
                    counts[name] += 1
                    joined = data[n+m+shift, h+k-1]
                    if joined > max(q, r) + 1e-10:
                        failures[name].append([n,h,m,k,joined,max(q,r)])
            if n >= m and (h-1)*(m-1) <= (k-1)*(n-1):
                counts['ratio_order'] += 1
                if q > r + 1e-10:
                    failures['ratio_order'].append([n,h,m,k,q,r])
    result = {'status': 'exploratory floating-point, not a proof',
              'parameters': vars(args), 'chains': len(data), 'tested': counts,
              'failures': failures, 'q': {f'{n},{h}': q for (n,h),q in data.items()}}
    Path(args.output).write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'chains': len(data), 'tested':counts,
                      'failure_counts':{k:len(v) for k,v in failures.items()}}))


if __name__ == '__main__':
    main()
