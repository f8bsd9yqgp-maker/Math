#!/usr/bin/env python3
"""Self-contained proof certificate for length-nine binary Lyndon superstrings.
No third-party libraries; verifies bound 185 and an explicit matching witness.
"""
from collections import Counter
from hashlib import sha256

N = 9
B = N-1
ZERO_SINKS = (75, 77, 79, 83, 103, 107, 109, 117, 123,
              125, 171, 175, 183, 187, 191, 223, 239, 255)
SPECIAL_SOURCE = (35, 5)
WITNESS = ("00101010110001001011101100010100110000111011110000011011111000000001111111100000100111110100011110110000110011101010001110010011011010001011011100001000110101100001010111100000010111111")

def directed_distance(a, b):
    """Shortest directed path from a to b in the 8-bit de Bruijn graph."""
    aa = format(a, '08b')
    bb = format(b, '08b')
    return next(k for k in range(9) if aa[k:] == bb[:8-k])

def p(v):
    return min(8, 5 + directed_distance(35, v),
               *(directed_distance(z, v) for z in ZERO_SINKS))

P = [p(v) for v in range(256)]
assert min(P) == 0 and max(P) == 8
for u in range(256):
    for bit in (0, 1):
        v = (2*u + bit) % 256
        assert P[v] - P[u] <= 1, (u, v)

WORDS = sorted(format(x, '09b') for x in range(512)
               if all(format(x, '09b') < format(x, '09b')[k:] + format(x, '09b')[:k]
                      for k in range(1, 9)))
assert len(WORDS) == 56
assert len(set(WORDS)) == 56
DELTA = [0] * 256
for w in WORDS:
    u, v = int(w[:8], 2), int(w[1:], 2)
    DELTA[u] += 1
    DELTA[v] -= 1
assert Counter(DELTA) == {0: 216, 1: 20, -1: 20}
assert {v for v in range(256) if DELTA[v] == -1} == set(ZERO_SINKS) | {35, 57}
D = sum(DELTA[v] * P[v] for v in range(256))
assert D == 129, D
LOWER_BOUND = 8 + 56 + (D - 8)
assert LOWER_BOUND == 185
assert len(WITNESS) == 185
assert set(WITNESS) == {'0', '1'}
positions = {w: WITNESS.find(w) for w in WORDS}
assert all(q >= 0 for q in positions.values())
assert len(set(positions.values())) == 56
assert P[int(WITNESS[:8], 2)] == 8
assert P[int(WITNESS[-8:], 2)] == 0
selected = set(positions.values())
assert len(WITNESS) - 8 - len(selected) == 121
extra_gains = [P[int(WITNESS[i+1:i+9], 2)] - P[int(WITNESS[i:i+8], 2)]
               for i in range(len(WITNESS)-8) if i not in selected]
assert all(d == 1 for d in extra_gains)
print('PASS: 56 distinct length-nine Lyndon words')
print('PASS: 256 vertices and all 512 edge inequalities')
print('PASS: required edges give total potential drop D=129')
print('PASS: potential range R=8')
print('PASS: universal lower bound L>=185')
print('PASS: witness length 185, covers all 56 words')
print('PASS: all 121 additional factors increase potential exactly 1')
print('PASS: witness starts at potential 8 and ends at 0')
print('WITNESS:', WITNESS)
print('SHA256:', sha256(WITNESS.encode()).hexdigest())
print('MINIMUM:', LOWER_BOUND)
print('Positive imbalances and p-values:', [(i,P[i]) for i,x in enumerate(DELTA) if x==1])
print('Negative imbalances and p-values:', [(i,P[i]) for i,x in enumerate(DELTA) if x==-1])
print('All target-word positions (1-based):')
for w,pos in positions.items():print(w,pos+1)