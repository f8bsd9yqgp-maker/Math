"""Exact structural audit of the size-uniform local stationary reduction.

The update below implements the four original NaSch steps. Projection is
computed by repeated full braking, independently of the analytic formula.
No stationary or Poisson equations are solved.
"""
from itertools import product
from pathlib import Path
from random import Random
from fractions import Fraction as F
import json

def compositions(h,n):
    if n==1:
        yield (h,); return
    for k in range(h+1):
        for tail in compositions(h-k,n-1): yield (k,)+tail

def advance(g,v,coins):
    n=len(g)
    w=tuple(max(0,min(2,v[i]+1,g[i])-(1-coins[i])) for i in range(n))
    return tuple(g[i]+w[(i+1)%n]-w[i] for i in range(n)),w

def project(g,v):
    for _ in range(sum(g)+1):
        if not any(v): return g
        g,v=advance(g,v,[0]*len(g))
    raise AssertionError('failed to reach rest')

def mixed(c,xi):
    n=len(c); unseen={i for i in range(n) if c[i] or xi[i]}; marked=set()
    while unseen:
        stack=[unseen.pop()]; component=[]
        while stack:
            i=stack.pop(); component.append(i)
            for j in ((i-1)%n,(i+1)%n):
                if j in unseen: unseen.remove(j);stack.append(j)
        if any(c[i] for i in component):
            marked.update(i for i in component if xi[i])
    return marked

def hd(g,h): return sum(x!=y for x,y in zip(g,h))

def inspect(g,v,xi,counts):
    n=len(g); G=project(g,v)
    c=tuple(int(v[i]>0 and g[i]>=2) for i in range(n))
    S=mixed(c,xi); reduced=tuple(int(xi[i] and i not in S) for i in range(n))
    actual=project(*advance(g,v,xi)); aux=project(*advance(G,[0]*n,xi))
    clean_a=project(*advance(g,v,reduced)); clean_b=project(*advance(G,[0]*n,reduced))
    assert clean_a==clean_b,(g,v,xi,S)
    assert hd(actual,aux)<=8*len(S)
    assert all(G[i]==g[i] or c[i] or c[(i+1)%n] for i in range(n))
    counts['mask_comparisons']+=1
    for i in range(n):
        flipped=list(xi);flipped[i]=1-flipped[i]
        other=project(*advance(g,v,flipped))
        assert hd(actual,other)<=4,(g,v,xi,i,actual,other)
        counts['single_coin_hamming_checks']+=1

def main():
    counts={'mask_comparisons':0,'single_coin_hamming_checks':0,
            'random_projection_lipschitz':0,'conditional_mixed_expectations':0,
            'independent_threshold_checks':0,'high_density_drift_checks':0}
    for n in range(2,5):
        masks=list(product((0,1),repeat=n))
        for h in range(1,min(2*n,6)):
            for g in compositions(h,n):
                for v in masks:
                    for xi in masks: inspect(g,v,xi,counts)
    rng=Random(20261027)
    for n in range(2,23):
        for _ in range(160):
            h=rng.randrange(1,2*n); g=[0]*n
            for k in range(h):g[rng.randrange(n)]+=1
            v=[rng.randrange(3) for k in range(n)]
            xi=[rng.randrange(2) for k in range(n)]
            inspect(tuple(g),v,xi,counts)
            gg=list(g);vv=list(v)
            for k in range(rng.randrange(1,n+1)):
                i,j=rng.randrange(n),rng.randrange(n)
                if gg[i]:gg[i]-=1;gg[j]+=1
                vv[j]=rng.randrange(3)
            D=sum(gg[i]!=g[i] or vv[i]!=v[i] for i in range(n))
            assert hd(project(tuple(g),v),project(tuple(gg),vv))<=2*D
            counts['random_projection_lipschitz']+=1
    # Conditional expectation bound uses arbitrary binary c words; no gap law.
    for n in range(2,8):
        masks=list(product((0,1),repeat=n))
        for c in masks:
            m=sum(c); b=sum(c[i]*(1-c[(i+1)%n]) for i in range(n))
            for eps in (F(1,9),F(1,2),F(3,4)):
                value=sum(len(mixed(c,xi))*eps**sum(xi)*(1-eps)**(n-sum(xi)) for xi in masks)
                assert value<=eps*m+2*eps*b/(1-eps),(n,c,eps,value)
                counts['conditional_mixed_expectations']+=1
    # New independent four-step checks also cover H>=2N, where no rest
    # projection is used and the vanishing-velocity theorem still applies.
    for n in range(2,24):
        for _ in range(240):
            h=rng.randrange(0,8*n+1);g=[0]*n
            for k in range(h):g[rng.randrange(n)]+=1
            v=[rng.randrange(3) for k in range(n)];xi=[rng.randrange(2) for k in range(n)]
            c=[int(v[i]>0 and g[i]>=2) for i in range(n)]
            ng,nv=advance(g,v,xi);nc=[int(nv[i]>0 and ng[i]>=2) for i in range(n)]
            bg,bv=advance(g,v,[0]*n);bc=[int(bv[i]>0 and bg[i]>=2) for i in range(n)]
            W=lambda gap,act:sum(act[i]*(gap[i]-1) for i in range(n))
            b=sum(c[i]*(1-c[(i+1)%n]) for i in range(n))
            assert W(bg,bc)-W(g,c)==-b
            assert W(ng,nc)-W(bg,bc)<=sum(c[i]*xi[(i+1)%n]+(1-c[i])*xi[i]*g[i] for i in range(n))
            counts['high_density_drift_checks']+=1
            for i in range(n):
                k=(i+1)%n
                for j in range(2,max(g[i],ng[i])+2):
                    old=bool(c[i] and c[k] and g[i]>=j)
                    new=bool(nc[i] and nc[k] and ng[i]>=j)
                    births=(int(not c[i] and c[k])*xi[i]+int(c[i] and not c[k])*xi[k]
                       +int(not c[i] and not c[k])*xi[i]*xi[k]
                       +int(c[i] and c[k] and g[i]==j-1)*(1-xi[i])*xi[k])
                    deaths=int(c[i] and c[k] and g[i]==j)*xi[i]*(1-xi[k])
                    assert int(new and not old)<=births
                    assert int(old and not new)>=deaths
                    counts['independent_threshold_checks']+=1
    out={'status':'all_passed_exactly','seed':20261027,'counts':counts,
         'scope':'Exhaustive small structural checks and seeded larger checks, not statistical inference.'}
    (Path(__file__).parent/'results'/'local_reduction.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))

if __name__=='__main__':main()
