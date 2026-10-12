#!/usr/bin/env python3
"""Standalone exact n=16 Lyndon superstring certificate verifier.
Requires only Python's standard library (no SciPy/NumPy/solver).

Input files, same folder:
  lyndon16_matching_dual.json -- optimal assignment and its dual inequalities
  lyndon16_witness_experiment.txt -- construction matching the lower bound

Each of the 1726^2 assignment inequalities is checked from scratch.
"""
import json
from pathlib import Path
from hashlib import sha256

HERE=Path(__file__).resolve().parent
n=16; B=n-1;V=1<<B;FULL=(1<<n)-1
words=[w for w in range(1<<n) if all(w < ((w<<k)|(w>>(n-k)))&FULL for k in range(1,n))]
assert len(words)==4080
out={w>>1:w&(V-1) for w in words}
assert len(out)==len(words)==len(set(out.values()))
starts=sorted(set(out)-set(out.values()))
ends=sorted(set(out.values())-set(out))
r=len(starts)
assert r==1725

def dist(a,b):
    for k in range(B+1):
        if (a&((1<<(B-k))-1)) == b>>k:
            return k
    raise AssertionError

cert=json.loads((HERE/'lyndon16_matching_dual.json').read_text())
C=cert['assignment_col_for_row']; u=cert['dual_row'];v=cert['dual_col']
assert len(C)==len(u)==len(v)==r+1
assert sorted(C)==list(range(r+1))

def cost(i,j):
    if i==j==r: return 10000000
    if i==r or j==r: return 0
    return dist(ends[i], starts[j])

matching_cost=0
for i in range(r+1):
    matching_cost+=cost(i,C[i])
    assert u[i]+v[C[i]]==cost(i,C[i]),('not tight',i)
assert matching_cost==17807
assert sum(u)+sum(v)==matching_cost
for i in range(r+1):
    for j in range(r+1):
        if u[i]+v[j]>cost(i,j):
            raise AssertionError(('dual infeasible',i,j,u[i],v[j],cost(i,j)))
print('PASS: all 1726^2 matching dual inequalities, total cost', matching_cost)

s=(HERE/'lyndon16_witness_experiment.txt').read_text().strip()
assert len(s)==21902
assert all(ch in '01' for ch in s)
seen={int(s[i:i+n],2) for i in range(len(s)-n+1)}
assert all(w in seen for w in words)
assert len(s)==B+len(words)+matching_cost
print('PASS: all 4080 Lyndon words in the 21902-bit witness')
print('WITNESS SHA256:',sha256(s.encode()).hexdigest())
print('CERTIFIED EXACT MINIMUM: 21902')
