#!/usr/bin/env python3
"""Self-contained independently replayable proof certificate for L_12=1415.
Uses only the standard library, no optimizer or external data files.
"""
from hashlib import sha256
from heapq import heappop, heappush

N = 12
V = 1 << (N-1)
# Unweighted zero-source vertices for the directed distance potential.
ZERO_SOURCES = (
    357, 405, 407, 421, 425, 441, 461, 467, 473, 485, 487, 489, 499, 505,
    613, 661, 663, 667, 669, 671, 679, 691, 717, 719, 723, 725, 743, 747,
    755, 757, 847, 853, 855, 859, 861, 863, 871, 875, 877, 885, 893, 925,
    927, 939, 941, 943, 949, 951, 955, 957, 981, 983, 987, 989, 1003, 1005,
    1007, 1013, 1015, 1019, 1021, 1367, 1371, 1375, 1387, 1391, 1399, 1403, 1407, 1455,
    1463, 1467, 1471, 1499, 1503, 1519, 1527, 1531, 1535, 1759, 1775, 1783, 1791, 1919,
    1983, 2047,
 )
# Extra weighted sources (vertex, starting potential).
WEIGHTED_SOURCES = (
    (823, 1), (459, 1), (97, 5), (133, 7),
    (135, 7), (403, 4), (409, 3), (291, 5),
    (827, 1), (831, 1), (197, 6), (329, 3),
    (457, 3), (209, 4), (227, 5), (355, 5),
    (619, 3), (241, 4),
 )
# Exact upper-bound witness; the length and every occurrence are checked below.
WITNESS = (
    '00000111100111000001010001110011010001110101011000011111001100000011110111111000001111101111000111110101'
    '10000000000011111111111000010111101111000110101001000000011001111110101000001011101111100000100100111110'
    '11010000000001011111111100001110100110001101110010000101100011110110110000110011011101010000010001011110'
    '01100000011010111110001010110011000000110001111110010000001000011111101110000000100011111110110001011111'
    '01110000001011011111100010011110111010001000111011001001001101101101000000001101111111100001011100111000'
    '00101100111100000000100111111110100000110010111000000011101111111000011101101110000100101011110110000101'
    '01101111000011011001110001011001010000010101011111000101001101100011101110110000100110011110101010000111'
    '10001011101011000000100101111110110001011011011100001001000111101001000011100101101010100001100100111010'
    '11010000100011011010110001100101011010110001100110011010101010000000101011111110000100010011100111010000'
    '00111001111100010100100110010100000100110111110100000110100111100011110010100101010000111101011100010010'
    '01011101101100001100010110100110000100001010010111101010001101001011001101000100101101110110000100111011'
    '11010000011011011111000001110101111000010110101111000011011101111000110101101100001101010111000100010101'
    '01011100010011010111010001000110011101101010000011100011100100101010110110000110100010010100111010000011'
    '000010101001110000001010011111000101011101110001100011011110111'
)

assert len(ZERO_SOURCES)==86 and len(set(ZERO_SOURCES))==86
assert len(WEIGHTED_SOURCES)==18
assert len(WITNESS)==1415 and set(WITNESS)=={"0","1"}
assert sha256(WITNESS.encode()).hexdigest() == (
    'a60713e2e8cacda5f13a69721afac2e5c9236ba84b10d9d5edd2ce0cc50bc95f')

# Compute p(v) = min(11, min_Z d(z,v), min_(a,c) (c+d(a,v))).
# This is a weighted multi-source shortest-path computation, with an
# initial cap of 11. Every directed edge has unit length.
P = [11] * V
heap=[]
for a,c in [(z,0) for z in ZERO_SOURCES] + list(WEIGHTED_SOURCES):
    if c < P[a]:
        P[a]=c
        heappush(heap,(c,a))
while heap:
    val,u=heappop(heap)
    if val != P[u]:
        continue
    for v in ((2*u)&(V-1),((2*u)+1)&(V-1)):
        if val+1 < P[v]:
            P[v]=val+1
            heappush(heap,(val+1,v))
assert min(P)==0 and max(P)==11
assert sha256(''.join(format(x,'x') for x in P).encode()).hexdigest()==(
    'd187c8de940e9eb793a8906bc94e629f1628dd1c25dadd0c48193193e68db24b')

# All 4096 possible transitions satisfy p(v)-p(u) <= 1.
for u in range(V):
    for bit in (0,1):
        v=((u<<1)|bit)&(V-1)
        assert P[v]-P[u]<=1

# Independently enumerate Lyndon words, with STRICT comparison to rotations.
W=[]
for i in range(1<<N):
    w=format(i,'012b')
    if all(w < w[k:]+w[:k] for k in range(1,N)):
        W.append(w)
assert len(W)==len(set(W))==335

# Both edge-by-edge and vertex-degree computations agree on D=1080.
DELTA=[0]*V
D=0
for w in W:
    u=int(w[:11],2)
    v=int(w[1:],2)
    DELTA[u]+=1;DELTA[v]-=1
    D+=P[u]-P[v]
assert D==sum(DELTA[u]*P[u] for u in range(V))==1080

# Any superstring of length L has L-11 edges. After selecting one of
# each 335 mandatory edges (net gain -D), all others gain at most 1;
# moreover the entire walk's gain is at least -11. Hence
# L >= 11 + 335 + D - 11 = 1415.
LOWER=(N-1)+len(W)+D-(max(P)-min(P))
assert LOWER==1415

# The upper bound needs no shortest-path or integer-programming solver.
positions={w: WITNESS.find(w) for w in W}
assert all(i>=0 for i in positions.values())
assert all(WITNESS[i:i+N]==w for w,i in positions.items())
assert len(WITNESS)==LOWER

# Tightness of the dual certificate along the construction.
used=set(positions.values())
assert len(used)==335
changes=[]
for i in range(len(WITNESS)-N+1):
    u=int(WITNESS[i:i+11],2)
    v=int(WITNESS[i+1:i+12],2)
    changes.append(P[v]-P[u])
assert sum(changes[i] for i in used)==-D
extras=[v for i,v in enumerate(changes) if i not in used]
assert len(extras)==1069 and all(v==1 for v in extras)
assert P[int(WITNESS[:11],2)]==11
assert P[int(WITNESS[-11:],2)]==0
assert sum(changes)==-11
print('PASS: 335 Lyndon words generated and found in 1415-bit witness')
print('PASS: 2048 graph vertices and all 4096 directed inequalities')
print('PASS: potential drop 1080 and range 11')
print('PASS: all 1069 extra transitions have unit potential gain')
print('THEOREM: exact minimum length =',LOWER)