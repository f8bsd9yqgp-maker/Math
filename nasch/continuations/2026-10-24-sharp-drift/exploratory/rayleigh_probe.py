"""Finite exact search only; no conclusion of stationary real stability."""
from fractions import Fraction as F
from itertools import product, chain
from pathlib import Path
import json
import random
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / 'code'))
from exact_support import stationary

rng = random.Random(724)
results = []
for n, h in [(4, 6), (4, 8), (5, 6), (6, 6)]:
    states, pi = stationary(n, h)
    weights = {}
    for g, p in zip(states, pi):
        bits = tuple(int(x >= 2) for x in g)
        weights[bits] = weights.get(bits, F(0)) + p
    witness = None
    fields = chain(product([-2, -1, 0, 1, 2], repeat=n-2),
                   (tuple(rng.randint(-100, 100) for _ in range(n-2))
                    for _ in range(500)))
    for z in fields:
        for j in range(1, n):
            others = [k for k in range(n) if k not in [0, j]]
            c = [F(0)]*4
            for bits, p in weights.items():
                v = p
                for k, x in zip(others, z):
                    if bits[k]:
                        v *= x
                c[bits[0]+2*bits[j]] += v
            d = c[1]*c[2]-c[0]*c[3]
            if d < 0:
                witness = {'pair': [0, j], 'z': z,
                           'coeffs': list(map(str, c)), 'rayleigh': str(d)}
                break
        if witness:
            break
    results.append({'N': n, 'H': h, 'witness': witness})
    print(results[-1], flush=True)
(HERE/'rayleigh_exploration.json').write_text(json.dumps(results, indent=2)+'\n')
