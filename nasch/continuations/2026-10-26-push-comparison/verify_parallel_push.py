"""Exact audits of the sharper synchronous pushing comparison.

Uniform stationarity is checked coefficient by coefficient in the
Bernstein basis epsilon^k(1-epsilon)^(H-k), not at sampled probabilities.
"""
from itertools import product,combinations
from math import comb
from fractions import Fraction as F
from pathlib import Path
from random import Random
import json
from verify_push import compositions,heights,gaps,majorant,advance


def parallel_push(y,H,xi):
    b=gaps(y,H)
    n=len(b)
    assert set(b)<={0,1} and H<n
    s=[0]*n
    zero=b.index(0)
    for k in range(1,n+1):
        i=(zero-k)%n
        s[i]=int(bool(b[i] and (xi[i] or s[(i+1)%n])))
    out=tuple(y[i]+s[i] for i in range(n))
    assert set(gaps(out,H))<={0,1}
    return out,sum(s)


def main():
    counts={'domination_masks':0,'random_domination_masks':0,
            'uniform_states':0,'transition_masks':0,
            'bernstein_coefficients':0,'reward_identities':0}
    for n in range(2,6):
        masks=list(product((0,1),repeat=n))
        for H in range(1,n):
            for g in compositions(H,n):
                h=heights(g)
                y=majorant(h,H)
                for xi in masks:
                    upper,_=parallel_push(y,H,xi)
                    for v in masks:
                        actual=advance(h,v,xi,H)
                        assert all(a<=b for a,b in zip(actual,upper)),(g,v,xi)
                        counts['domination_masks']+=1
    rng=Random(20261027)
    for n in range(2,80):
        for trial in range(100):
            H=rng.randrange(1,n)
            g=[0]*n
            for _ in range(H):g[rng.randrange(n)]+=1
            h=heights(g)
            y=majorant(h,H)
            xi=[rng.randrange(2) for _ in range(n)]
            v=[rng.randrange(3) for _ in range(n)]
            upper,_=parallel_push(y,H,xi)
            actual=advance(h,v,xi,H)
            assert all(a<=b for a,b in zip(actual,upper))
            counts['random_domination_masks']+=1
    for n in range(2,11):
        for H in range(1,n):
            configs=[]
            for sites in combinations(range(n),H):
                ss=set(sites)
                configs.append(tuple(int(i in ss) for i in range(n)))
            incoming={g:[0]*(H+1) for g in configs}
            rewards=[0]*(H+1)
            for g in configs:
                sites=[i for i in range(n) if g[i]]
                for bits in product((0,1),repeat=H):
                    xi=[0]*n
                    for i,v in zip(sites,bits):xi[i]=v
                    y,cost=parallel_push(heights(g),H,xi)
                    k=sum(bits)
                    incoming[gaps(y,H)][k]+=1
                    rewards[k]+=cost
                    counts['transition_masks']+=1
            for arr in incoming.values():
                for k,val in enumerate(arr):
                    assert val==comb(H,k),(n,H,k,val)
                    counts['bernstein_coefficients']+=1
            counts['uniform_states']+=len(configs)
            for eps in (F(1,7),F(1,3),F(1,2),F(1)):
                p=1-eps
                measured=sum(F(rewards[k])*eps**k*p**(H-k) for k in range(H+1))/(n*len(configs))
                ratio=F(1)
                predicted=F(0)
                for k in range(1,H+1):
                    ratio*=F(H-k+1,n-k+1)
                    predicted+=eps*p**(k-1)*ratio
                assert measured==predicted
                eta=F(H,n)
                assert predicted<=eps*eta/(1-p*eta)
                counts['reward_identities']+=1
    out={'status':'all_passed_exactly','counts':counts,'seed':20261027,
         'scope':'All-probability invariant-law coefficients; exact original-rule domination and reward checks.'}
    (Path(__file__).parent/'results/parallel_push.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))


if __name__=='__main__':main()
