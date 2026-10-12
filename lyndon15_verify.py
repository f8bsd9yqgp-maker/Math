#!/usr/bin/env python3
"""Solver-free proof certificate for the 15-bit binary Lyndon superstring.

Run: python3 lyndon15_verify.py
Requires only Python >= 3.8 and the same-directory files
  lyndon15_seeds.txt and lyndon15_witness.txt.

The verifier independently regenerates all Lyndon words, reconstructs
an integer potential from weighted seeds via Dijkstra, checks all 32768
one-step inequalities, and verifies an exact 11037-bit construction.
"""
from collections import Counter
from hashlib import sha256
from heapq import heappush, heappop
from pathlib import Path

N, B, V = 15, 14, 1 << 14
HERE = Path(__file__).resolve().parent

seed_data = (HERE / 'lyndon15_seeds.txt').read_bytes()
assert sha256(seed_data).hexdigest() == '10ec744ed2003d420855cb4b6343f5c3a3586e5395d6a6f520141f6c62907572'
seeds = [tuple(map(int, row.split())) for row in seed_data.decode('ascii').splitlines()]
assert len(seeds) == 657 and len({z for z, h in seeds}) == 657
assert all(0 <= z < V and 0 <= h < B for z, h in seeds)

# Each vertex is a 14-bit string; edges shift left and append 0 or 1.
# P(v) = min(B, min_(z,h) (h + directed_distance(z,v))).
# Independent multi-source Dijkstra reconstruction (no optimizer).
P = [B] * V
heap = []
for z, h in seeds:
    P[z] = h
    heappush(heap, (h, z))
while heap:
    d, u = heappop(heap)
    if d != P[u]:
        continue
    for v in ((u << 1) & (V - 1), ((u << 1) | 1) & (V - 1)):
        if d + 1 < P[v]:
            P[v] = d + 1
            heappush(heap, (d + 1, v))

assert len(P) == V and min(P) == 0 and max(P) == B
assert set(P) == set(range(B + 1))
for u in range(V):
    for v in ((u << 1) & (V - 1), ((u << 1) | 1) & (V - 1)):
        assert P[v] - P[u] <= 1, (u, v, P[u], P[v])

# First target enumeration: direct lexicographic string rotation test.
def is_lyndon(word):
    return all(word < word[k:] + word[:k] for k in range(1, N))

W = [format(i, '015b') for i in range(1 << N)
     if is_lyndon(format(i, '015b'))]
assert len(W) == 2182 and len(W) == len(set(W))

# Second target enumeration: 15-bit arithmetic rotations, independent
# of the string implementation. This verifies the target set identity.
M = (1 << N) - 1
W2 = {format(w, '015b') for w in range(1 << N)
      if all(w < (((w << k) | (w >> (N - k))) & M)
             for k in range(1, N))}
assert set(W) == W2

D_edges = sum(P[int(w[:-1], 2)] - P[int(w[1:], 2)] for w in W)
imbalance = Counter()
for w in W:
    imbalance[int(w[:-1], 2)] += 1
    imbalance[int(w[1:], 2)] -= 1
assert all(abs(v) <= 1 for v in imbalance.values())
assert sum(v == 1 for v in imbalance.values()) == 905
assert sum(v == -1 for v in imbalance.values()) == 905
D_divergence = sum(P[v] * imbalance[v] for v in range(V))
assert D_edges == D_divergence == 8855

# Every string S of length L containing W corresponds to a walk
# with L-B edges, of which 2182 are distinguished required edges.
# The distinguished ones have total potential gain -8855, and all
# other edges gain <=1. Net gain is >=-B, therefore:
#       -B <= -D + (L-B-|W|) => L >= |W| + D = 11037.
LOWER_BOUND = len(W) + D_edges
assert LOWER_BOUND == 11037

S = (HERE / 'lyndon15_witness.txt').read_text().strip()
assert len(S) == LOWER_BOUND and set(S) == {'0', '1'}
assert sha256(S.encode('ascii')).hexdigest() == '64f05492c9b978dbd5ac2bb1f92bcdc9b08310a42a4789d26138c7a7325938e0'
positions = {w: S.find(w) for w in W}
assert len(positions) == 2182 and all(position >= 0 for position in positions.values())
assert len(set(positions.values())) == 2182
assert int(S[:B], 2) == 92
assert int(S[-B:], 2) == 11743
assert P[92] == B and P[11743] == 0

selected = set(positions.values())
extras = 0
chosen_potential_change = 0
for i in range(len(S) - B):
    a = int(S[i:i+B], 2)
    b = int(S[i+1:i+N], 2)
    change = P[b] - P[a]
    if i in selected:
        chosen_potential_change += change
    else:
        extras += 1
        assert change == 1, (i, change)
assert extras == 8841 and chosen_potential_change == -8855

print('PASS: independently generated exactly 2182 Lyndon words (two methods)')
print('PASS: 657 seed certificate, 16384 potential values in 0..14')
print('PASS: all 32768 potential inequalities')
print('PASS: 905 positive and 905 negative required-edge imbalances')
print('PASS: mandatory-edge potential decrease = 8855 (two methods)')
print('PASS: universal lower bound L >= 11037')
print('PASS: 11037-bit witness containing all 2182 targets')
print('PASS: 8841 non-required transitions each increase potential by 1')
print('PASS: endpoints at potentials 14 and 0')
print('SHA256:', sha256(S.encode('ascii')).hexdigest())
print('CERTIFIED EXACT MINIMUM:', LOWER_BOUND)