#!/usr/bin/env python3
"""Independent verifier of the length-94 Lyndon superstring theorem.

Uses breadth-first search on the binary order-seven de Bruijn digraph,
rather than the overlap-distance formula in the mathematical argument.
Requires only Python 3.9+ and the standard library.
"""
from collections import deque
from hashlib import sha256

TARGETS = [format(x, "08b") for x in range(256)
           if all(format(x, "08b") <
                  format(x, "08b")[k:] + format(x, "08b")[:k]
                  for k in range(1, 8))]
assert len(TARGETS) == len(set(TARGETS)) == 30

ADJ = {v: [((v * 2) & 127), ((v * 2 + 1) & 127)]
       for v in range(128)}

def bfs(source):
    dist = [-1] * 128
    dist[source] = 0
    queue = deque([source])
    while queue:
        v = queue.popleft()
        for u in ADJ[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + 1
                queue.append(u)
    assert min(dist) == 0 and max(dist) <= 7
    return dist

SINKS = [37, 39, 53, 59, 61, 87, 91, 95, 111, 127]
DS = [bfs(z) for z in SINKS]
D25 = bfs(25)
p = [min([7, 3 + D25[v]] + [d[v] for d in DS])
     for v in range(128)]

assert 0 <= min(p) <= max(p) <= 7
for a in range(128):
    for b in ADJ[a]:
        assert p[b] - p[a] <= 1, (a, b, p[a], p[b])

imb = [0] * 128
for s in TARGETS:
    a, b = int(s[:7], 2), int(s[1:], 2)
    imb[a] += 1
    imb[b] -= 1

assert sum(imb) == 0
positive = {v: (imb[v], p[v]) for v in range(128) if imb[v] > 0}
negative = {v: (-imb[v], p[v]) for v in range(128) if imb[v] < 0}
assert positive == ({v: (1, 7) for v in
                     [0, 2, 4, 6, 10, 12, 14, 18, 26]} |
                    {22: (1, 2), 30: (1, 2)})
assert negative == ({25: (1, 3)} |
                    {v: (1, 0) for v in SINKS})

drop_by_divergence = sum(imb[v] * p[v] for v in range(128))
drop_by_edges = sum(p[int(s[:7], 2)] - p[int(s[1:], 2)]
                    for s in TARGETS)
assert drop_by_divergence == drop_by_edges == 64

WITNESS = ("00000001111111000001011111000010011110100001101111"
           "00010101110001100100101101100011101100110101")
assert len(WITNESS) == 94
positions = {s: WITNESS.find(s) + 1 for s in TARGETS}
assert all(i > 0 for i in positions.values())

# Any superstring of length L gives m=L-7 edges.
# The selected 30 required edges contribute -64 potential change.
# Other edges increase potential by at most one; total change >= -7.
minimum_proved = 7 + len(TARGETS) + (drop_by_divergence - 7)
assert minimum_proved == len(WITNESS) == 94

selected = {i - 1 for i in positions.values()}
edge_gains = []
for i in range(len(WITNESS) - 7):
    a = int(WITNESS[i:i + 7], 2)
    b = int(WITNESS[i + 1:i + 8], 2)
    edge_gains.append(p[b] - p[a])
assert len(selected) == 30
assert p[int(WITNESS[:7], 2)] == 7
assert p[int(WITNESS[-7:], 2)] == 0
assert sum(edge_gains[i] for i in selected) == -64
assert [edge_gains[i] for i in range(len(edge_gains))
        if i not in selected] == [1] * 57

print("BFS-derived potential: VERIFIED on all 128 nodes")
print("All 256 edge inequalities: PASS")
print("30 Lyndon words and degree imbalances: PASS")
print("Required-edge potential drop: 64")
print("Witness length and containment checks: PASS")
print("Witness SHA256:", sha256(WITNESS.encode()).hexdigest())
print("All 57 extra edges gain exactly +1 potential: PASS")
print("Certified exact minimum:", minimum_proved)
print("One-indexed witness positions:")
for s in TARGETS:
    print(s + ":", positions[s])
