#!/usr/bin/env python3
"""Standalone certificate: binary Lyndon superstrings of length 11 need 715 bits.

No third-party packages or network. Independent of the linear optimizer or
network-flow routine that discovered the certificate.
"""
from collections import Counter
from hashlib import sha256
from heapq import heappush, heappop
from pathlib import Path

N = 11
B = N - 1
V = 1 << B
ZERO_ANCHORS = (
    203, 217, 233, 243, 249, 295, 299, 301, 303, 307, 309, 311,
    315, 317, 319, 331, 333, 335, 339, 359, 371, 373, 411, 413,
    415, 423, 427, 429, 431, 437, 445, 463, 469, 471, 475, 477,
    491, 493, 501, 503, 507, 509, 683, 687, 695, 699, 703, 727,
    731, 735, 751, 759, 763, 767, 879, 887, 895, 959, 991, 1023
)
WEIGHTED_ANCHORS = (
    (67, 6), (113, 4), (137, 7), (139, 7), (141, 7),
    (143, 7), (163, 5), (199, 6), (201, 3), (229, 2), (293, 2)
)
ANCHORS = tuple((a, 0) for a in ZERO_ANCHORS) + WEIGHTED_ANCHORS
assert len(ZERO_ANCHORS) == 60 and len(ANCHORS) == 71
assert len({a for a, _ in ANCHORS}) == 71

# Shortest directed distance in the length-10 binary de Bruijn graph.
def overlap_distance(a, b):
    for k in range(B + 1):
        overlap_length = B - k
        if (a & ((1 << overlap_length) - 1)) == (b >> k):
            return k
    raise AssertionError('Impossible: zero-length overlap always matches')

# This definition is a completely explicit finite certificate.
p = [min([B] + [weight + overlap_distance(a, v)
                 for a, weight in ANCHORS]) for v in range(V)]
assert min(p) == 0 and max(p) == 10

# Independent second computation of the SAME potential via multi-source Dijkstra.
p2 = [B] * V
queue = []
for a, weight in ANCHORS:
    if weight < p2[a]:
        p2[a] = weight
        heappush(queue, (weight, a))
while queue:
    cost, u = heappop(queue)
    if cost != p2[u]:
        continue
    for bit in (0, 1):
        v = (2*u + bit) % V
        if cost + 1 < p2[v]:
            p2[v] = cost + 1
            heappush(queue, (p2[v], v))
assert p == p2, 'Independent distance calculations disagree'

for u in range(V):
    for bit in (0, 1):
        v = (2*u + bit) % V
        assert p[v] <= p[u] + 1, (u, v)

# Generate required Lyndon factors directly, without stored target list.
def is_lyndon(bits):
    return all(bits < bits[k:] + bits[:k] for k in range(1, len(bits)))

W = [format(w, f'0{N}b') for w in range(1 << N)
     if is_lyndon(format(w, f'0{N}b'))]
assert len(W) == 186 and len(set(W)) == 186

imbalance = [0] * V
for w in W:
    imbalance[int(w[:B], 2)] += 1
    imbalance[int(w[1:], 2)] -= 1
assert Counter(imbalance) == {0: 882, 1: 71, -1: 71}

# Two mathematically equivalent independently calculated potential-drop sums.
drop1 = sum(imbalance[v] * p[v] for v in range(V))
drop2 = sum(p[int(w[:B], 2)] - p[int(w[1:], 2)] for w in W)
assert drop1 == drop2 == 529
assert Counter(p[v] for v in range(V) if imbalance[v] == 1) == \
       {10: 52, 7: 4, 4: 2, 3: 3, 2: 10}
assert Counter(p[v] for v in range(V) if imbalance[v] == -1) == \
       {0: 60, 2: 2, 3: 1, 4: 1, 5: 1, 6: 2, 7: 4}

# Every containing string has m=L-10 length-11 factors.
# Of these, 186 distinct factors are mandatory and decrease p by 529 total.
# All other edges increase p by at most one.
# Because p(final)-p(initial) >= -10:
# -10 <= -529 + ((L-10)-186)  =>  L >= 715.
LOWER_BOUND = B + len(W) + drop1 - B
assert LOWER_BOUND == 715

# The witness is stored separately so it can also be inspected byte-for-byte.
witness_path = Path(__file__).with_name('lyndon11_witness.txt')
S = witness_path.read_text(encoding='ascii').strip()
assert set(S) <= {'0', '1'}
assert len(S) == 715
positions = {w: S.find(w) for w in W}
assert all(pos >= 0 for pos in positions.values())
assert len(set(positions.values())) == len(W)

# Extra sharpness check: each remaining edge raises p exactly one.
chosen = set(positions.values())
gains = []
for i in range(len(S) - B):
    u = int(S[i:i+B], 2)
    v = int(S[i+1:i+B+1], 2)
    assert v == (2*u + int(S[i+B])) % V
    gains.append(p[v] - p[u])
assert sum(gains[i] for i in chosen) == -529
extra = [gains[i] for i in range(len(gains)) if i not in chosen]
assert len(extra) == 519 and all(d == 1 for d in extra)
assert p[int(S[:B], 2)] == 10 and p[int(S[-B:], 2)] == 0

print('PASS: 186 distinct length-11 binary Lyndon words')
print('PASS: explicit potential, independent BFS distances, 2048 inequalities')
print('PASS: total required-edge potential drop 529')
print('PASS: universal lower bound 715 bits')
print('PASS: witness has length 715 and covers all 186 words')
print('PASS: all 519 non-required edges gain +1; endpoints 10 and 0')
print('SHA256(ASCII witness):', sha256(S.encode('ascii')).hexdigest())
print('EXACT MINIMUM:', LOWER_BOUND)