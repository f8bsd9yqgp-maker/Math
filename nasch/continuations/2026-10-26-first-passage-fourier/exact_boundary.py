"""Exact Fourier boundary formula for the original three-hole T_N.

Python standard library only. Arithmetic takes place in Q[z]/Phi_N(z).
This is a small-N reference implementation, not the fast FFT implementation.
It never solves the original two-dimensional hitting-time system.
"""

from fractions import Fraction as F
from itertools import combinations, permutations


def trim(a):
    a = list(a)
    while a and not a[-1]:
        a.pop()
    return a


def padd(a, b, sign=1):
    c = [F(0)] * max(len(a), len(b))
    for i, v in enumerate(a):
        c[i] += v
    for i, v in enumerate(b):
        c[i] += sign * v
    return trim(c)


def pmul(a, b):
    if not a or not b:
        return []
    c = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                c[i + j] += x * y
    return trim(c)


def pdiv(a, b):
    a, b = trim(a), trim(b)
    if not b:
        raise ZeroDivisionError
    q = [F(0)] * max(0, len(a) - len(b) + 1)
    while len(a) >= len(b):
        k, v = len(a) - len(b), a[-1] / b[-1]
        q[k] = v
        for j, w in enumerate(b):
            a[k + j] -= v * w
        a = trim(a)
    return trim(q), a


def cyclotomic(n):
    polys = {}
    for d in range(1, n + 1):
        if n % d:
            continue
        p = [F(-1)] + [F(0)] * (d - 1) + [F(1)]
        for e in polys:
            if d % e == 0:
                p, rem = pdiv(p, polys[e])
                assert not rem
        polys[d] = p
    return polys[n]


class Field:
    def __init__(self, n):
        self.n, self.mod = n, cyclotomic(n)
        self.degree = len(self.mod) - 1
        self.zero = (F(0),) * self.degree
        self.one = self.element([F(1)])
        self.powers = [self.element([F(0)] * k + [F(1)])
                       for k in range(n)]

    def element(self, a):
        _, r = pdiv([F(x) for x in a], self.mod)
        return tuple(r + [F(0)] * (self.degree - len(r)))

    def add(self, a, b):
        return tuple(x + y for x, y in zip(a, b))

    def scale(self, a, b):
        return tuple(x * b for x in a)

    def sub(self, a, b):
        return tuple(x - y for x, y in zip(a, b))

    def mul(self, a, b):
        return self.element(pmul(a, b))

    def inv(self, a):
        old_r, r, old_t, t = self.mod, trim(a), [], [F(1)]
        while r:
            q, new_r = pdiv(old_r, r)
            old_r, r = r, new_r
            old_t, t = t, padd(old_t, pmul(q, t), -1)
        assert len(old_r) == 1 and old_r[0]
        ans = self.element([x / old_r[0] for x in old_t])
        assert self.mul(a, ans) == self.one
        return ans

    def conj(self, a):
        ans = self.zero
        for i, c in enumerate(a):
            ans = self.add(ans, self.scale(self.powers[-i % self.n], c))
        return ans

    def rational(self, a):
        assert not any(a[1:]), (self.n, a)
        return a[0]


PERMS = list(permutations(range(3)))


def parity(p):
    return (-1) ** sum(p[i] > p[j] for i in range(3)
                      for j in range(i + 1, 3))


def determinant(field, sites, modes):
    ans = field.zero
    for p in PERMS:
        exponent = sum(sites[i] * modes[p[i]] for i in range(3))
        ans = field.add(ans, field.scale(field.powers[exponent % field.n],
                                         parity(p)))
    return ans


class SpectralBoundary:
    def __init__(self, n, discount=F(0)):
        if n < 3:
            raise ValueError("The interior is empty for N=2.")
        self.n, self.field = n, Field(n)
        self.discount = F(discount)
        if self.discount < 0:
            raise ValueError("Discount must be nonnegative.")
        f = self.field
        self.modes = [k for k in combinations(range(n), 3)
                      if sum(k) % n == 0]
        self.inverse = []
        for k in self.modes:
            lam = f.scale(f.one, 3 + self.discount)
            for v in k:
                lam = f.sub(lam, f.powers[-v % n])
            self.inverse.append(f.inv(lam))
        self.boundary_dets = [self.dets((0, c, n - 1))
                              for c in range(1, n - 1)]
        self.weighted_conjugates = [
            [f.mul(f.conj(d), inv) for d, inv in zip(ds, self.inverse)]
            for ds in self.boundary_dets]

    def dets(self, sites):
        return [determinant(self.field, sites, k) for k in self.modes]

    def harmonic(self, gaps):
        """Discounted exit probabilities into boundary orbits b_(c+1)."""
        x, y, z = gaps
        assert min(gaps) > 0 and x + y + z == self.n
        f = self.field
        ds = self.dets((0, x, x + y))
        answer = []
        for wc in self.weighted_conjugates:
            v = f.zero
            for d, w in zip(ds, wc):
                v = f.add(v, f.mul(d, w))
            answer.append(f.rational(f.scale(v, F(1, self.n ** 2))))
        return answer

    def kernel(self):
        return [self.harmonic((a, self.n - a - 1, 1))
                for a in range(1, self.n - 1)]


def solve_rational(matrix, rhs):
    """Ordinary Gaussian elimination, restricted to the boundary matrix."""
    n = len(rhs)
    a = [list(map(F, row)) + [F(b)] for row, b in zip(matrix, rhs)]
    for j in range(n):
        k = next(i for i in range(j, n) if a[i][j])
        a[j], a[k] = a[k], a[j]
        pivot = a[j][j]
        for r in range(j, n + 1):
            a[j][r] /= pivot
        for i in range(j + 1, n):
            v = a[i][j]
            if v:
                for r in range(j, n + 1):
                    a[i][r] -= v * a[j][r]
    answer = [F(0)] * n
    for i in range(n - 1, -1, -1):
        answer[i] = a[i][n] - sum(a[i][j] * answer[j]
                                  for j in range(i + 1, n))
    assert all(sum(v * x for v, x in zip(row, answer)) == b
               for row, b in zip(matrix, rhs))
    return answer


def boundary_system(n, kernel):
    size = n - 2
    known = F((n - 1) * (n + 4), 6)
    matrix, rhs = [], []
    for a in range(1, size + 1):
        matrix.append([F(2 * (a == b) - (b == a - 1))
                       - (kernel[a - 1][b - 2] if b >= 2 else 0)
                       for b in range(1, size + 1)])
        rhs.append(1 + F(a * (n - a - 1), n)
                   + kernel[a - 1][-1] * known)
    return matrix, rhs, known


def exact_solution(n):
    if n == 2:
        return {"T": F(1), "boundary": [F(0), F(1)]}
    spectral = SpectralBoundary(n)
    kernel = spectral.kernel()
    matrix, rhs, known = boundary_system(n, kernel)
    unknown = solve_rational(matrix, rhs)
    return {"T": unknown[0], "boundary": [F(0)] + unknown + [known],
            "kernel": kernel, "spectral": spectral}


def exact_laplace(n, discount):
    """Return E_B exp(-discount*tau), and all boundary values."""
    discount = F(discount)
    if n == 2:
        value = 1 / (1 + discount)
        return {"laplace": value, "boundary": [F(1), value]}
    spectral = SpectralBoundary(n, discount)
    kernel = spectral.kernel()
    size = n - 1
    matrix = [[F(0)] * size for _ in range(size)]
    rhs = [F(0)] * size
    for a in range(1, size):
        matrix[a - 1][a - 1] += 2 + discount
        if a == 1:
            rhs[0] = F(1)
        else:
            matrix[a - 1][a - 2] -= 1
        for c in range(1, size):
            matrix[a - 1][c] -= kernel[a - 1][c - 1]
    matrix[-1][-1] += 2 + discount
    matrix[-1][-2] -= 1
    matrix[-1][0] -= 1
    values = solve_rational(matrix, rhs)
    return {"laplace": values[0], "boundary": [F(1)] + values,
            "kernel": kernel, "spectral": spectral}


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("N", type=int)
    args = parser.parse_args()
    print(exact_solution(args.N)["T"])
