"""Exact audits of frozen anchors and integrated-current reconstruction.

Original traffic updates and reduced firings are coded directly.
No stationary distribution or earlier Poisson equation is solved.
"""
from itertools import product
from fractions import Fraction as F
from pathlib import Path
import json


def compositions(h,n):
    if n==1:
        yield (h,)
        return
    for m in range(h+1):
        for rest in compositions(h-m,n-1):yield (m,)+rest


def full_step(g,v,xi):
    n=len(g)
    w=tuple(max(0,min(2,v[i]+1,g[i])-(1-xi[i])) for i in range(n))
    gg=tuple(g[i]+w[(i+1)%n]-w[i] for i in range(n))
    assert min(gg)>=0 and sum(gg)==sum(g)
    return gg,w


def reduced_step(g,i):
    a=list(g)
    amount=a[i]-int(a[i]>=2)
    a[i]-=amount
    a[(i-1)%len(a)]+=amount
    return tuple(a),amount


def main():
    count={'full_histories':0,'full_frozen_anchor_checks':0,
           'reduced_words':0,'reduced_anchor_checks':0,
           'anchor_probability_identities':0}
    for n in range(2,5):
        masks=list(product((0,1),repeat=n))
        for H in range(1,min(2*n,5)):
            for g in compositions(H,n):
                for v in masks:
                    c=tuple(int(v[i]>0 and g[i]>=2) for i in range(n))
                    for x1 in masks:
                        g1,v1=full_step(g,v,x1)
                        for x2 in masks:
                            g2,v2=full_step(g1,v1,x2)
                            I=tuple(v1[i]+v2[i] for i in range(n))
                            assert all(g2[i]-g[i]==I[(i+1)%n]-I[i] for i in range(n))
                            for j in range(1,n):
                                if c[j]==0 and x1[j]==x2[j]==0:
                                    assert I[j]==0
                                    assert I[0]==sum(g[i]-g2[i] for i in range(j))
                                    count['full_frozen_anchor_checks']+=1
                            count['full_histories']+=1
        words=[word for k in range(5) for word in product(range(n),repeat=k)]
        for H in range(1,min(2*n,5)):
            for g in compositions(H,n):
                for word in words:
                    z=g
                    I=[0]*n
                    for i in word:
                        z,d=reduced_step(z,i)
                        I[i]+=d
                    assert all(z[i]-g[i]==I[(i+1)%n]-I[i] for i in range(n))
                    for j in range(1,n):
                        if j not in word:
                            assert I[j]==0
                            assert I[0]==sum(g[i]-z[i] for i in range(j))
                            count['reduced_anchor_checks']+=1
                    count['reduced_words']+=1
    # The candidate anchor is selected by future clocks, independently of
    # the initial qualification word. Average each deterministic word over
    # rotations and enumerate every possible no-clock mask in the window.
    for n in range(2,7):
        for c in product((0,1),repeat=n):
            C=F(sum(c),n)
            for L in range(1,n):
                for q in (F(1,3),F(1,2),F(2,3)):
                    noanchor=F(0)
                    qualified=F(0)
                    for absence in product((0,1),repeat=L):
                        weight=q**sum(absence)*(1-q)**(L-sum(absence))
                        if not any(absence):
                            noanchor+=weight
                            continue
                        j=absence.index(1)+1
                        qualified+=weight*sum(c[(j+s)%n] for s in range(n))/n
                    assert noanchor==(1-q)**L
                    assert qualified==C*(1-(1-q)**L)
                    assert qualified<=C
                    count['anchor_probability_identities']+=1
    out={'status':'all_passed_exactly','counts':count,
         'scope':'Deterministic anchor identities and exact rational probabilities, not a stationary-current closure.'}
    folder=Path(__file__).parent/'results'
    folder.mkdir(exist_ok=True)
    (folder/'verified.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))


if __name__=='__main__':main()
