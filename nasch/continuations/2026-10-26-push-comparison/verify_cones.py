"""Exact event-word audit of one-sided discrepancy propagation.

No stationary distribution or old Poisson equation is solved. The
Poisson expectation and independence assertions are analytic in the proof.
"""
from itertools import product
from fractions import Fraction
from pathlib import Path
import json


def fire(g, i):
    a=list(g)
    amount=a[i]-(a[i]>=2)
    a[i]-=amount
    a[(i-1)%len(a)]+=amount
    return tuple(a)


def check(g,h,word,seed):
    n=len(g)
    reached={seed}
    boundary=seed
    for i in word:
        if i==boundary and len(reached)<n:
            boundary=(boundary-1)%n
            reached.add(boundary)
        g=fire(g,i)
        h=fire(h,i)
        assert all(g[j]==h[j] or j in reached for j in range(n))


def main():
    count=0
    for n in range(2,5):
        words=[w for k in range(5) for w in product(range(n),repeat=k)]
        for g in product(range(3),repeat=n):
            for seed in range(n):
                for mass in range(4):
                    if mass==g[seed]:continue
                    h=list(g)
                    h[seed]=mass
                    for word in words:
                        check(g,tuple(h),word,seed)
                        count+=1
    telescopes=0
    for n in range(101):
        for lam in (Fraction(1,100),Fraction(1,3),Fraction(3,2)):
            exact=sum(1+j*lam for j in range(n))
            assert exact==n+lam*n*(n-1)/2
            T=n*lam
            assert lam*exact<=T+T*T/2
            telescopes+=1
    result={'status':'all_passed_exactly',
            'single_seed_event_words':count,
            'rational_telescoping_identities':telescopes,
            'scope':'Deterministic containment and exact constants; analytic Poisson-front proof is in DYNAMIC_REDUCTION.md.'}
    (Path(__file__).parent/'results/cones.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))


if __name__=='__main__':main()
