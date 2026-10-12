#!/usr/bin/env python3
"""Independent pure-Python verification of length-10 binary Lyndon superstring optimum 359.
Checks the exact 99 targets, an explicit edge potential bound 260, and the
359-bit upper witness. No linear or integer programming is required.
"""
from collections import Counter, deque
from hashlib import sha256

N = 10
V = 1 << (N - 1)
ZERO_SINKS = (101, 105, 115, 121, 147, 149, 151, 155, 157, 159, 167,
              179, 181, 205, 207, 213, 215, 221, 235, 237, 245, 247,
              251, 253, 343, 347, 351, 367, 375, 379, 383, 439, 447,
              479, 511)
WITNESS = (
    "00001111011100010010011101101000001010111110000100101111011000001100111101010001011101110000111001100110101010001111101100011010010000101101111000110010110101000111010110000101001110000001101111110000000101111111000001110111110000001001111110100000000011111111100001100010011011101000101010111000011010111000110110111000100010110011000001000111100100101011011"
)

def dist(a, b):
    """Shortest directed distance between 9-bit de Bruijn vertices."""
    aa = format(a, '09b')
    bb = format(b, '09b')
    for k in range(10):
        if aa[k:] == bb[:9-k]:
            return k
    raise AssertionError('distance undefined')

def bfs_distances(source):
    distlist = [-1] * V
    distlist[source] = 0
    queue = deque([source])
    while queue:
        u = queue.popleft()
        for bit in (0, 1):
            v = ((u << 1) | bit) & (V-1)
            if distlist[v] == -1:
                distlist[v] = distlist[u] + 1
                queue.append(v)
    assert max(distlist) <= 9
    return distlist

# Independently cross-check the overlap distance formula using BFS.
for source in (*ZERO_SINKS, 49, 69, 71):
    dd = bfs_distances(source)
    assert all(dd[v] == dist(source,v) for v in range(V))

def lyndon(s):
    return all(s < s[k:] + s[:k] for k in range(1, len(s)))

TARGETS = [format(x, '010b') for x in range(1024)
           if lyndon(format(x, '010b'))]
assert len(TARGETS) == 99

# Distinct distance offsets are checked directly from the stated formula.
def potential(v):
    return min(9, 4 + dist(49, v), 6 + dist(69, v),
               6 + dist(71, v),
               *(dist(z, v) for z in ZERO_SINKS))

P = [potential(v) for v in range(V)]
assert min(P) == 0 and max(P) == 9
for u in range(V):
    for bit in (0, 1):
        v = ((u << 1) | bit) & (V-1)
        assert P[v] - P[u] <= 1, (u, v, P[u], P[v])

DELTA = [0] * V
for w in TARGETS:
    u = int(w[:9], 2)
    v = int(w[1:], 2)
    DELTA[u] += 1
    DELTA[v] -= 1

POSITIVES = [v for v in range(V) if DELTA[v] == 1]
NEGATIVES = [v for v in range(V) if DELTA[v] == -1]
assert len(POSITIVES) == len(NEGATIVES) == 38
assert all(d in (-1, 0, 1) for d in DELTA)
assert Counter(P[v] for v in POSITIVES) == {9:27, 2:6, 3:2, 4:1, 5:1, 6:1}
assert Counter(P[v] for v in NEGATIVES) == {0:35, 4:1, 6:2}
assert sorted(v for v in NEGATIVES if P[v]==0) == sorted(ZERO_SINKS)
assert [v for v in NEGATIVES if P[v] == 4] == [49]
assert [v for v in NEGATIVES if P[v] == 6] == [69, 71]
D = sum(DELTA[v] * P[v] for v in range(V))
assert D == 260
assert sum(P[int(w[:9], 2)] - P[int(w[1:], 2)] for w in TARGETS) == D
LOWER_BOUND = (N-1) + len(TARGETS) + D - (max(P) - min(P))
assert LOWER_BOUND == 359

assert len(WITNESS) == 359
POSITIONS = {w:WITNESS.find(w) for w in TARGETS}
assert all(v >= 0 for v in POSITIONS.values())
assert len(set(POSITIONS.values())) == 99  # one distinct selected occurrence per target
assert P[int(WITNESS[:9], 2)] == 9
assert P[int(WITNESS[-9:], 2)] == 0

G = []
for i in range(len(WITNESS) - 9):
    tail = int(WITNESS[i:i+9],2)
    head = int(WITNESS[i+1:i+10],2)
    G.append(P[head]-P[tail])
selected = set(POSITIONS.values())
assert sum(G[i] for i in selected) == -260
assert len(G) - len(selected) == 251
assert all(G[i] == 1 for i in range(len(G)) if i not in selected)
assert sum(G) == -9

print('PASS: 99 binary Lyndon words of length 10')
print('PASS: BFS independently validates all 38 directed distance profiles')
print('PASS: 1,024 de Bruijn edges obey potential increase <= 1')
print('PASS: 38 source and 38 sink imbalances; mandatory potential drop 260')
print('PASS: universal lower bound = 359')
print('PASS: 359-bit witness contains all 99 required words')
print('PASS: 251 nonmandatory transitions each increase the potential by 1')
print('PASS: witness potential starts at 9 and finishes at 0')
print('WITNESS_SHA256:',sha256(WITNESS.encode()).hexdigest())
print('CONCLUSION: exact minimum =', LOWER_BOUND)