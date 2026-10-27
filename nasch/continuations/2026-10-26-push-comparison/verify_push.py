"""Exact finite checks for the new NaSch upper comparison with drop-push.

No earlier stationary solver is used. The pushing invariant law is checked
by incoming transition counts, and its reward is counted exactly.
"""
from itertools import product,permutations,combinations
from fractions import Fraction as F
from random import Random
from pathlib import Path
import json

def compositions(h,n):
    if n==1:yield (h,);return
    for k in range(h+1):
        for tail in compositions(h-k,n-1):yield (k,)+tail

def heights(g):
    out=[0]
    for v in g[:-1]:out.append(out[-1]+v)
    return tuple(out)

def gaps(h,H):return tuple(h[i+1]-h[i] for i in range(len(h)-1))+(h[0]+H-h[-1],)

def majorant(h,H):
    n=len(h)
    return tuple(max(h[(i+k)%n]+H*((i+k)//n)-k for k in range(n)) for i in range(n))

def advance(h,v,xi,H):
    g=gaps(h,H)
    w=tuple(max(0,min(2,v[i]+1,g[i])-(1-xi[i])) for i in range(len(h)))
    return tuple(x+y for x,y in zip(h,w))

def push(h,H,i):
    n=len(h);g=list(gaps(h,H));out=list(h);travel=0
    assert set(g)<=set((0,1))
    if g[i]==0:return h,0
    j=i
    while True:
        out[j]+=1;travel+=1;g[j]-=1;g[(j-1)%n]+=1
        j=(j-1)%n
        if g[j]<=1:break
        assert travel<=n
    assert sum(g)==H and set(g)<=set((0,1))
    return tuple(out),travel

def inspect(g,v,xi,orders,counts):
    n=len(g);H=sum(g);h=heights(g);s=majorant(h,H)
    assert all(s[i]>=h[i] for i in range(n)) and set(gaps(s,H))<=set((0,1))
    actual=advance(h,v,xi,H)
    for order in orders:
        y=s
        for i in order:y,_=push(y,H,i)
        assert all(actual[i]<=y[i] for i in range(n)),(g,v,xi,order,actual,y)
        counts['pathwise_mask_order_checks']+=1

def main():
    counts={'pathwise_mask_order_checks':0,'random_order_checks':0,
            'uniform_stationary_states':0,'uniform_transition_counts':0,
            'exact_current_identities':0,'positive_amplification_families':0}
    rng=Random(20261027)
    for n in range(2,6):
        masks=list(product((0,1),repeat=n))
        for H in range(1,n):
            for g in compositions(H,n):
                for v in masks:
                    for xi in masks:
                        marked=[i for i in range(n) if xi[i]]
                        orders=list(permutations(marked)) if n<=4 else [tuple(marked),tuple(reversed(marked))]
                        inspect(g,v,xi,orders,counts)
    for n in range(2,36):
        for trial in range(160):
            H=rng.randrange(1,n);g=[0]*n
            for k in range(H):g[rng.randrange(n)]+=1
            v=[rng.randrange(3) for k in range(n)];word=[rng.randrange(n) for k in range(rng.randrange(3*n))]
            xi=[int(i in word) for i in range(n)]
            inspect(tuple(g),v,xi,[word],counts)
            counts['random_order_checks']+=1
    for n in range(2,13):
        for H in range(1,n):
            configs=[]
            for indices in combinations(range(n),H):
                s=set(indices);configs.append(tuple(int(i in s) for i in range(n)))
            incoming=dict.fromkeys(configs,0);travel=0
            for g in configs:
                h=heights(g)
                for i in range(n):
                    nh,cost=push(h,H,i);incoming[gaps(nh,H)]+=1;travel+=cost
                    counts['uniform_transition_counts']+=1
            assert all(k==n for k in incoming.values())
            assert F(travel,n*len(configs))==F(H,n-H+1)
            counts['uniform_stationary_states']+=len(configs)
            counts['exact_current_identities']+=1
    # Exact analytic obstruction to a mass-only projected-current charge.
    # Direct full-braking displacement, with original four-step updates.
    def coast(g,v):
        n=len(g);H=sum(g);h=heights(g);start=h
        for t in range(H+1):
            if not any(v):return tuple(h[i]-start[i] for i in range(n))
            nh=advance(h,v,[0]*n,H);v=tuple(nh[i]-h[i] for i in range(n));h=nh
        raise AssertionError('coasting failed')
    for ell in range(1,51):
        n=5*ell+3;g=[0]*n;v=[0]*n
        for i in range(1,ell+1):g[i]=3;v[i]=1
        g[ell+1]=ell+2;H=sum(g);h=heights(g)
        old=coast(tuple(g),tuple(v));P=tuple(h[i]+old[i] for i in range(n))
        xi=[int(i==ell+1) for i in range(n)]
        nh=advance(h,v,xi,H);nv=tuple(nh[i]-h[i] for i in range(n));ng=gaps(nh,H)
        extra=coast(ng,nv)
        delta=tuple(nh[i]+extra[i]-P[i] for i in range(n))
        assert delta==tuple(ell+1 if 1<=i<=ell+1 else 0 for i in range(n))
        assert sum(delta)==(ell+1)**2 and H==4*ell+2<n
        counts['positive_amplification_families']+=1
    out={'status':'all_passed_exactly','counts':counts,'seed':20261027,
         'scope':'Finite exact structural audits, not a proof by numerical extrapolation.'}
    (Path(__file__).parent/'results/push.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))
if __name__=='__main__':main()
