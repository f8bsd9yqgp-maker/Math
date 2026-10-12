#!/usr/bin/env python3
"""Solver-free finite proof certificate: L_14 = 5564.

Run from any directory: python3 /path/to/lyndon14_verify.py
Uses only the standard Python library and the two companion data files:
 lyndon14_seeds.txt and lyndon14_witness.txt.

The potential is reconstructed by a multi-source shortest-path calculation,
not by reading the optimization solver's dual variables.
"""
from collections import Counter
from hashlib import sha256
from pathlib import Path
from heapq import heappush, heappop

N = 14
B = N-1
V = 1 << B
ALL = 1 << N
HERE = Path(__file__).resolve().parent

seeds_raw = (HERE / 'lyndon14_seeds.txt').read_text().strip().splitlines()
seeds = []
for line in seeds_raw:
    z,h = map(int,line.split())
    assert 0 <= z < V and 0 <= h < B
    seeds.append((z,h))
assert len(seeds) == 358
assert len(seeds) == len(set(z for z,h in seeds))
assert sha256((HERE/'lyndon14_seeds.txt').read_bytes()).hexdigest() == (
    '611a9cf5eb8fa9deff0d00ae6be8e74da8ee8588ec368999144825293fe86283')

# Compute p(v) = min(B, min_{(z,h) in seeds} [h + d(z,v)]).
P = [B]*V
heap=[]
for z,h in seeds:
    assert h <= P[z]
    P[z]=h
    heappush(heap,(h,z))
while heap:
    d,u=heappop(heap)
    if d != P[u]:
        continue
    for bit in (0,1):
        v=((u<<1)|bit)&(V-1)
        if d+1 < P[v]:
            P[v]=d+1
            heappush(heap,(d+1,v))
assert min(P)==0 and max(P)==B
assert len(P)==8192

# The proof only requires one-sided graph Lipschitz, checked exhaustively.
for u in range(V):
    for bit in (0,1):
        v=((u<<1)|bit)&(V-1)
        assert P[v] <= P[u]+1,(u,v,P[u],P[v])

# An independent target-set generation by comparing actual bitstrings.
def is_lyndon(s):
    return all(s < s[k:] + s[:k] for k in range(1,N))
W = [format(i,f'0{N}b') for i in range(ALL)
     if is_lyndon(format(i,f'0{N}b'))]
assert len(W)==1161 and len(set(W))==1161

# Compute total mandatory potential drop in two independent forms.
D = sum(P[int(w[:-1],2)] - P[int(w[1:],2)] for w in W)
delta=Counter()
for w in W:
    delta[int(w[:-1],2)]+=1
    delta[int(w[1:],2)]-=1
assert sum(delta.values())==0
assert all(abs(t)<=1 for t in delta.values())
assert sum(x==1 for x in delta.values())==479
assert sum(x==-1 for x in delta.values())==479
assert D==sum(delta[v]*P[v] for v in range(V))==4403

# Universal argument for any string length L:
# -B <= p(end)-p(start) <= -D +(L-B-|W|),
# so L >= |W| + D (since p has range at most B).
LOWER_BOUND = len(W) + D
assert LOWER_BOUND==5564

S=(HERE/'lyndon14_witness.txt').read_text().strip()
assert len(S)==LOWER_BOUND
assert set(S)<={'0','1'}
assert sha256(S.encode('ascii')).hexdigest()==(
    '31bb9576482c795a61811a5d678193218b5a67da2d48dce17659d7bce020f277')
positions={w:S.find(w) for w in W}
assert all(v>=0 for v in positions.values())
assert len(set(positions.values()))==1161
assert int(S[:B],2)==40
assert int(S[-B:],2)==5631
assert P[40]==13 and P[5631]==0

# Extra strong equality certificate: every extra edge gains +1.
chosen=set(positions.values())
extra=0
required_gain=0
for i in range(len(S)-B):
    u=int(S[i:i+B],2)
    v=int(S[i+1:i+N],2)
    diff=P[v]-P[u]
    if i in chosen:
        required_gain+=diff
    else:
        extra+=1
        assert diff==1,(i,u,v,diff)
assert required_gain==-4403
assert extra==4390

print('PASS: 1161 required length-14 binary Lyndon words regenerated')
print('PASS: 8192 vertices, all 16384 potential inequalities checked')
print('PASS: 358 weighted seeds independently reconstruct potential 0..13')
print('PASS: mandatory-edge potential drop = 4403')
print('PASS: universal lower bound = 5564 bits')
print('PASS: 5564-bit witness contains all required words')
print('PASS: all 4390 additional edges gain exactly +1')
print('PASS: witness begins with potential 13 and ends with potential 0')
print('SHA256:',sha256(S.encode('ascii')).hexdigest())
print('CERTIFIED EXACT MINIMUM:',LOWER_BOUND)