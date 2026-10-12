#!/usr/bin/env python3
"""Self-contained standard-library certificate for length-13 binary Lyndon superstrings.
Run beside lyndon13_witness.txt. No optimizer or scientific libraries required.
"""
from collections import deque
from hashlib import sha256
from pathlib import Path

N = 13
B = N - 1
V = 1 << B
SEEDS = {
    0: (741, 811, 813, 815, 825, 843, 857, 869, 873, 889, 921, 923, 933, 937, 947, 953,
        971, 973, 979, 985, 997, 999, 1001, 1011, 1017, 1227, 1253, 1267, 1323, 1325,
        1327, 1331, 1333, 1335, 1339, 1341, 1343, 1355, 1357, 1359, 1363, 1383, 1395,
        1435, 1437, 1439, 1447, 1451, 1459, 1461, 1485, 1487, 1491, 1493, 1511, 1515,
        1523, 1525, 1691, 1693, 1695, 1703, 1707, 1709, 1711, 1717, 1719, 1723, 1725,
        1727, 1743, 1749, 1751, 1757, 1767, 1771, 1773, 1781, 1789, 1851, 1853, 1855,
        1871, 1877, 1879, 1883, 1885, 1887, 1899, 1901, 1903, 1909, 1915, 1917, 1951,
        1963, 1965, 1967, 1973, 1975, 1979, 1981, 2005, 2007, 2011, 2013, 2027, 2029,
        2031, 2037, 2039, 2043, 2045, 2731, 2735, 2743, 2747, 2751, 2775, 2779, 2783,
        2795, 2799, 2807, 2811, 2815, 2907, 2911, 2927, 2935, 2939, 2943, 2991, 2999,
        3003, 3007, 3035, 3039, 3055, 3063, 3067, 3071, 3511, 3519, 3551, 3567, 3575,
        3583, 3823, 3839, 3967, 4031, 4095,),
    1: (919, 1431, 1639, 1643, 1647, 1655, 1659, 1663,),
    2: (1255,),
    3: (713, 809, 841, 969,),
    4: (401, 433, 465, 497, 659,),
    5: (225, 483, 611, 675, 739,),
    6: (323, 453, 581, 583,),
    7: (131, 391, 393, 395,),
    8: (265, 267, 269, 271,),
}

# A graph potential is specified by weighted source distances,
# p(v) = min(B, min_{(source,height)} [height + distance(source,v)]).
# BFS, not linear programming, reconstructs the entire certificate.

def directed_distances(source):
    dist = [-1] * V
    dist[source] = 0
    q = deque([source])
    while q:
        u = q.popleft()
        for bit in (0, 1):
            v = (u * 2 + bit) % V
            if dist[v] < 0:
                dist[v] = dist[u] + 1
                q.append(v)
    assert min(dist) == 0 and max(dist) <= B
    return dist

P = [B] * V
for height, sources in SEEDS.items():
    for source in sources:
        d = directed_distances(source)
        for v in range(V):
            P[v] = min(P[v], height + d[v])
assert (min(P), max(P)) == (0, B)
assert sum(len(s) for s in SEEDS.values()) == 188

# Independently confirm all 8192 directed edge inequalities.
for u in range(V):
    for bit in (0, 1):
        v = (2 * u + bit) % V
        assert P[v] - P[u] <= 1, (u, v, P[u], P[v])

# Generate the entire required set directly from the Lyndon definition.
def rotate(w, k):
    return ((w << k) | (w >> (N - k))) & ((1 << N) - 1)

WORDS = [w for w in range(1 << N)
         if all(w < rotate(w, k) for k in range(1, N))]
assert len(WORDS) == len(set(WORDS)) == 630

# Check the mandatory-edge potential drop without the optimization solver.
D = sum(P[w >> 1] - P[w & (V - 1)] for w in WORDS)
imbalance = [0] * V
for w in WORDS:
    imbalance[w >> 1] += 1
    imbalance[w & (V - 1)] -= 1
assert sum(x == 1 for x in imbalance) == 252
assert sum(x == -1 for x in imbalance) == 252
assert all(abs(x) <= 1 for x in imbalance)
assert D == sum(imbalance[v] * P[v] for v in range(V)) == 2174, D

# The lower bound follows from D, N, number of required words and range B:
# p(end)-p(start) <= -D + (L-B-len(WORDS)); left hand >= -B.
LOWER_BOUND = B + len(WORDS) + D - B
assert LOWER_BOUND == 2804

witness = (Path(__file__).resolve().parent / 'lyndon13_witness.txt').read_text().strip()
assert len(witness) == LOWER_BOUND
assert set(witness) <= {'0', '1'}
assert sha256(witness.encode('ascii')).hexdigest() == ('ddbb6eb0f9b5a726778028a172715d9'
                                                       'a93597a7a9745eb8b8fb991076788fd81')
positions = {}
for w in WORDS:
    target = format(w, '013b')
    pos = witness.find(target)
    assert pos >= 0, target
    positions[target] = pos

assert len(set(positions.values())) == 630
assert int(witness[:B], 2) == 200
assert int(witness[-B:], 2) == 1979
assert P[200] == B and P[1979] == 0

# Stronger check: the witness saturates the dual bound on every extra edge.
selected = set(positions.values())
extra = []
required_drop = 0
for i in range(len(witness) - B):
    u = int(witness[i:i + B], 2)
    v = int(witness[i + 1:i + N], 2)
    change = P[v] - P[u]
    if i in selected:
        required_drop += change
    else:
        extra.append(change)
assert required_drop == -D
assert len(extra) == 2162 and all(change == 1 for change in extra)

print('PASS: 630 length-thirteen binary Lyndon words generated and covered')
print('PASS: 4096 vertices and all 8192 potential inequalities')
print('PASS: 188-source independently reconstructed potential; range 0..12')
print('PASS: required potential decrease exactly 2174')
print('PASS: 2162 additional edges each have potential gain +1')
print('PASS: witness begins at potential 12 and ends at 0')
print('SHA256:', sha256(witness.encode('ascii')).hexdigest())
print('THEOREM: exact shortest length =', LOWER_BOUND)