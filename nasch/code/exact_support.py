"""Exact finite-ring stationary solver used throughout the research project.

Rate-one clock i sends d(g_i) to i-1 modulo N. All arithmetic is rational.
The full compositions are included, including any transient states.
"""
from fractions import Fraction as F


def compositions(total, sites):
    if sites == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for rest in compositions(total - first, sites - 1):
                yield (first,) + rest


def d(n):
    return n - int(n >= 2)


def ring_move(g, j):
    y = list(g)
    amount = d(y[j])
    y[j] -= amount
    y[(j - 1) % len(y)] += amount
    return tuple(y)


def solve_fraction(a, b):
    n = len(b)
    rows = [[F(x) for x in row] + [F(rhs)] for row, rhs in zip(a, b)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if rows[i][j])
        rows[j], rows[pivot] = rows[pivot], rows[j]
        for i in range(j + 1, n):
            if not rows[i][j]:
                continue
            ratio = rows[i][j] / rows[j][j]
            rows[i][j] = F(0)
            for k in range(j + 1, n + 1):
                rows[i][k] -= ratio * rows[j][k]
    ans = [F(0)] * n
    for j in range(n - 1, -1, -1):
        ans[j] = (rows[j][-1] - sum(rows[j][k] * ans[k]
                                  for k in range(j + 1, n))) / rows[j][j]
    return ans


def stationary(n, h):
    states = list(compositions(h, n))
    index = {g: i for i, g in enumerate(states)}
    size = len(states)
    qt = [[0] * size for _ in states]
    for col, g in enumerate(states):
        for j in range(n):
            row = index[ring_move(g, j)]
            qt[row][col] += 1
            qt[col][col] -= 1
    a = [row[:] for row in qt]
    a[-1] = [1] * size
    rhs = [0] * size
    rhs[-1] = 1
    pi = solve_fraction(a, rhs)
    assert sum(pi) == 1 and all(p >= 0 for p in pi)
    assert all(sum(F(x) * p for x, p in zip(row, pi)) == 0 for row in qt)
    return states, pi

