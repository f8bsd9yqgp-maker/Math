"""Independent direct relaxation audit of the mixed-cluster lemma.

No imported update, relaxation, projected-gap, or serialization routines.
Original four NaSch steps are simulated until every stored speed is zero.
Random trials use a fixed seed and are examples, not a proof.
"""
from pathlib import Path
from random import Random
from collections import deque
import json,platform

def advance(g,v,coins):
    n=len(g); w=[]
    for i in range(n):
        acceleration=min(2,v[i]+1)
        collision=min(acceleration,g[i])
        w.append(max(0,collision-(1-coins[i])))
    return tuple(g[i]+w[(i+1)%n]-w[i] for i in range(n)),tuple(w)

def coast(g,v):
    n=len(g); limit=sum(g); travel=[0]*n
    for t in range(limit+1):
        if not any(v): return tuple(travel)
        g,v=advance(g,v,[0]*n)
        for i in range(n):travel[i]+=v[i]
    raise AssertionError(('did not reach rest',g,v,limit))

def affected(c,xi):
    n=len(c); on=[bool(c[i] or xi[i]) for i in range(n)]
    unseen={i for i in range(n) if on[i]}; result=set()
    while unseen:
        q=deque([unseen.pop()]); comp=[]
        while q:
            i=q.popleft();comp.append(i)
            for j in ((i-1)%n,(i+1)%n):
                if j in unseen: unseen.remove(j);q.append(j)
        if any(c[i] for i in comp) and any(xi[i] for i in comp):
            result.update(comp)
    return result

def pairpot(r):
    return sum(min(r[i],r[j]) for i in range(len(r)) for j in range(i+1,len(r)))

def inspect(g,v,xi):
    n=len(g);h=sum(g);assert n>=2 and 1<=h<2*n
    ell=coast(g,v); c=[int(v[i]>0 and g[i]>=2) for i in range(n)]
    G=tuple(g[i]+ell[(i+1)%n]-ell[i] for i in range(n))
    assert min(G)>=0 and sum(G)==h
    ng,nv=advance(g,v,xi); ne=coast(ng,nv)
    actual=tuple(nv[i]+ne[i]-ell[i] for i in range(n))
    rg,rv=advance(G,[0]*n,xi); re=coast(rg,rv)
    rest=tuple(rv[i]+re[i] for i in range(n))
    S=affected(c,xi)
    assert all(actual[i]==rest[i] for i in range(n) if i not in S)
    assert all(-(h-1)<=x<=h for x in actual)
    assert all(0<=x<=h for x in rest)
    r=[int(v[i]>0)+ell[i] for i in range(n)]
    rr=[int(nv[i]>0)+ne[i] for i in range(n)]
    k=sum(1 for vi in v if vi>0);K=sum(xi)
    assert pairpot(ell)-pairpot(r)==-k*(k-1)//2
    positive=sum(max(rr[i]-ell[i],0) for i in range(n))
    B=sum(xi[i]*(G[i]-int(G[i]>=2)) for i in range(n))
    assert positive<=(k+K)*B
    assert pairpot(rr)-pairpot(ell)<=max(k+K-1,0)*positive
    return len(S)==n,any(actual[i]<0 for i in range(n))

def main():
    rng=Random(20261026); totals={'trials':0,'full_ring':0,'negative_projection':0}
    for n in range(2,21):
        for z in range(220):
            h=rng.randrange(1,2*n); g=[0]*n
            for _ in range(h):g[rng.randrange(n)]+=1
            v=[rng.randrange(3) for _ in range(n)]
            xi=[rng.randrange(2) for _ in range(n)]
            full,negative=inspect(g,v,xi)
            totals['trials']+=1;totals['full_ring']+=full;totals['negative_projection']+=negative
        # Construct long qualified blocks in which every local gap is 2.
        for k in range(1,n):
            g=[2 if i<k else 0 for i in range(n)]
            v=[1 if i<k else 0 for i in range(n)]
            for j in range(n):
                xi=[int(i==j) for i in range(n)]
                full,negative=inspect(g,v,xi)
                totals['trials']+=1;totals['full_ring']+=full;totals['negative_projection']+=negative
    out={'status':'all_passed_exactly','seed':20261026,'python':platform.python_version(),
         'scope':'Independent original four-step simulation and repeated full braking; no stationary solver.',
         'totals':totals}
    (Path(__file__).parent/'results'/'independent.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))
if __name__=='__main__':main()
