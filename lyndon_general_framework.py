#!/usr/bin/env python3
"""A general finite theorem/conditional construction for binary Lyndon superstrings.

Usage: python lyndon_general_framework.py 10
Requires NumPy and SciPy for the matching step; the mathematical statements
are proven in the companion research note. This is NOT a proof of an all-n
closed formula or of all-n relaxation tightness.
"""
import argparse
from collections import defaultdict, deque
from math import gcd
import numpy as np
from scipy.optimize import linear_sum_assignment


def lyndon_words(n):
    full = (1 << n) - 1
    return [w for w in range(1 << n)
            if all(w < (((w << k) | (w >> (n - k))) & full)
                   for k in range(1, n))]


def bridge_distance(a, b, bits):
    for k in range(bits + 1):
        if (a & ((1 << (bits - k)) - 1)) == (b >> k):
            return k
    raise AssertionError("de Bruijn graph must be strongly connected")


def run(n, save_witness=None):
    if not 2 <= n <= 18:
        raise ValueError('Use n=2..18; large matching matrices become expensive')
    B = n - 1
    V = 1 << B
    required = lyndon_words(n)
    q = len(required)
    assert all((w >> (n-1)) == 0 and (w & 1) == 1 for w in required)

    out_required = {w >> 1: w & (V - 1) for w in required}
    assert len(out_required) == q
    assert len(set(out_required.values())) == q
    starts = sorted(set(out_required) - set(out_required.values()))
    ends = sorted(set(out_required.values()) - set(out_required))
    assert len(starts) == len(ends)
    r = len(starts)
    if not r: raise AssertionError('Expected at least one required path')

    mat = np.zeros((r + 1, r + 1), dtype=np.int32)
    for i, a in enumerate(ends):
        for j, b in enumerate(starts):
            mat[i, j] = bridge_distance(a, b, B)
    mat[r, r] = 10**7  # Disallow unused artificial start/end
    rows, cols = linear_sum_assignment(mat)
    M = int(mat[rows, cols].sum())
    assert (r, r) not in zip(rows, cols)
    actual_start = starts[int(cols[rows == r][0])]
    actual_end = ends[int(rows[cols == r][0])]

    adj = defaultdict(list)
    degrees_in = defaultdict(int)
    degrees_out = defaultdict(int)
    undirected = defaultdict(list)
    total_arcs = 0

    def add_arc(a, b):
        nonlocal total_arcs
        assert b == (2 * a) % V or b == ((2 * a + 1) % V)
        adj[a].append(b)
        degrees_in[b] += 1
        degrees_out[a] += 1
        undirected[a].append(b)
        undirected[b].append(a)
        total_arcs += 1

    for w in required:
        add_arc(w >> 1, w & (V - 1))

    for i, j in zip(rows, cols):
        if i == r or j == r:
            continue
        a, b = ends[int(i)], starts[int(j)]
        k = int(mat[i, j])
        for t in range(k):
            x = (b >> (k - t - 1)) & 1
            nxt = ((2 * a) | x) & (V - 1)
            add_arc(a, nxt)
            a = nxt
        assert a == b

    assert total_arcs == q + M
    nodes = set(degrees_in) | set(degrees_out)
    assert all(degrees_out[v] - degrees_in[v] == (v == actual_start) - (v == actual_end)
               for v in nodes)
    seen = {actual_start}
    todo = [actual_start]
    while todo:
        for v in undirected[todo.pop()]:
            if v not in seen:
                seen.add(v)
                todo.append(v)
    connected = (seen == nodes)
    L_bound = B + q + M
    result = {'n': n, 'lyndon_words': q, 'mandatory_paths': r,
              'matching_cost': M, 'rigorous_lower_bound': L_bound,
              'matching_connected': connected, 'nodes_in_support': len(nodes)}

    if connected:
        # Hierholzer's Euler-trail algorithm. The adjacency multiset uses every
        # compulsory edge and every chosen shortest connector precisely once.
        stack = [actual_start]
        rev = []
        while stack:
            v = stack[-1]
            if adj[v]:
                stack.append(adj[v].pop())
            else:
                rev.append(stack.pop())
        route = rev[::-1]
        assert len(route) == total_arcs + 1
        assert route[0] == actual_start and route[-1] == actual_end
        bits = format(actual_start, f'0{B}b') + ''.join(str(v & 1) for v in route[1:])
        assert len(bits) == L_bound
        factors = {int(bits[i:i+n], 2) for i in range(len(bits)-n+1)}
        assert all(w in factors for w in required)
        result['exact_optimum'] = L_bound
        if save_witness:
            with open(save_witness, 'w') as file:
                file.write(bits + '\n')
            result['witness_file'] = save_witness
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('n', type=int)
    parser.add_argument('--witness', default=None)
    args = parser.parse_args()
    for key, val in run(args.n, args.witness).items():
        print(f'{key}: {val}')