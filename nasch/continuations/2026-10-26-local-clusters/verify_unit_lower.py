"""Exact tests of a new full-traffic lower comparison, not a stationary solve."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

def compositions(h,n):
    if n==1:
        yield (h,)
    else:
        for x in range(h+1):
            for rest in compositions(h-x,n-1):yield (x,)+rest

def prefix(g):
    h=[0]
    for x in g[:-1]:h.append(h[-1]+x)
    return h

def exact_product_invariance():
    checks=0;probabilities=(F(1,4),F(1,2),F(3,4))
    for n in range(2,5):
        for h in range(1,7):
            states=list(compositions(h,n)); masks=list(product((0,1),repeat=n))
            for eps in probabilities:
                p=1-eps
                weights={g:p**(-sum(x>0 for x in g)) for g in states}
                arriving=defaultdict(F)
                for g in states:
                    for mask in masks:
                        chips=[int(mask[i] and g[i]>0) for i in range(n)]
                        target=tuple(g[i]-chips[i]+chips[(i+1)%n] for i in range(n))
                        prob=eps**sum(mask)*p**(n-sum(mask))
                        arriving[target]+=weights[g]*prob
                        checks+=1
                assert dict(arriving)==weights
                z=sum(weights.values())
                mean=sum(sum(x>0 for x in g)*w for g,w in weights.items())/z
                assert mean/n>=F(h,h+n-1)
    return checks

def pathwise_comparison():
    checks=0
    for n in range(2,5):
        for h in range(1,5):
            states=list(compositions(h,n));masks=list(product((0,1),repeat=n))
            for g in states:
                base=prefix(g)
                for z_g in states:
                    z=prefix(z_g)
                    offset=max([0]+[z[i]-base[i] for i in range(n)])
                    heights=[base[i]+offset for i in range(n)]
                    assert all(heights[i]>=z[i] for i in range(n))
                    for a in masks:
                        for coin in masks:
                            w=[int(a[i] and g[i]>=2)+coin[i]*int(g[i]>=1)
                               for i in range(n)]
                            after=[heights[i]+w[i] for i in range(n)]
                            other=[z[i]+coin[i]*int(z_g[i]>=1) for i in range(n)]
                            assert all(after[i]>=other[i] for i in range(n))
                            checks+=1
    return checks

def main():
    out={'status':'all_passed_exactly','product_invariance_transitions':exact_product_invariance(),
         'ordered_one_step_checks':pathwise_comparison(),
         'scope':'Direct transition identity and height comparison; no stationary-system solves.'}
    (Path(__file__).parent/'results'/'unit_lower.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))
if __name__=='__main__':main()
