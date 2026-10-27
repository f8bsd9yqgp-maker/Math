"""New audits of the reduced-time Poisson coupling, not stationary solves."""
from pathlib import Path
from itertools import product
from random import Random
from fractions import Fraction as F
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'2026-10-26-gap-balance'))
from verify_local_reduction import compositions,project,advance,hd,mixed

def fire(g,i):
    n=len(g);gg=list(g);d=gg[i]-int(gg[i]>=2)
    gg[i]-=d;gg[(i-1)%n]+=d;return tuple(gg)

def badset(n,word):
    k=[word.count(i) for i in range(n)]
    return {i for i in range(n) if k[i]>=2 or (k[i] and (k[(i-1)%n] or k[(i+1)%n]))}

def main():
    counts={'poisson_word_comparisons':0,'coupled_hamming_drift':0,
            'random_full_projection_to_word':0,'rational_constants':0}
    for n in range(2,5):
        words=[w for k in range(5) for w in product(range(n),repeat=k)]
        for H in range(1,min(2*n,5)):
            for g in compositions(H,n):
                for word in words:
                    xi=[int(i in word) for i in range(n)];Q=project(*advance(g,[0]*n,xi))
                    z=g
                    for i in word:z=fire(z,i)
                    assert hd(Q,z)<=2*len(badset(n,word)),(g,word,Q,z)
                    counts['poisson_word_comparisons']+=1
    for n in range(2,5):
        for H in range(0,7):
            configs=list(compositions(H,n))
            for g in configs:
                for h in configs:
                    D=hd(g,h)
                    for i in range(n):
                        assert hd(fire(g,i),fire(h,i))-D<=int(g[i]!=h[i])
                        counts['coupled_hamming_drift']+=1
    rng=Random(20261027)
    for n in range(2,24):
        for trial in range(240):
            H=rng.randrange(1,2*n);g=[0]*n
            for k in range(H):g[rng.randrange(n)]+=1
            g=tuple(g);v=[rng.randrange(3) for i in range(n)];G=project(g,v)
            word=[rng.randrange(n) for k in range(rng.randrange(3*n))]
            xi=[int(i in word) for i in range(n)]
            c=[int(v[i]>0 and g[i]>=2) for i in range(n)]
            actual=project(*advance(g,v,xi));z=G
            for i in word:z=fire(z,i)
            assert hd(actual,z)<=8*len(mixed(c,xi))+2*len(badset(n,word))
            counts['random_full_projection_to_word']+=1
    for denom in range(2,100):
        for num in range(1,denom//2+1):
            eps=F(num,denom);p=1-eps
            # lambda<=epsilon/p<=2epsilon, obtained by integrating 1/(1-x).
            assert eps/p<=2*eps
            assert 2*eps**2+(eps/p)**2/2<=4*eps**2
            # lambda-epsilon<=epsilon^2/(2p): bound every series coefficient 1/k by 1/2.
            tail=sum(eps**k/F(k) for k in range(2,25))
            assert tail<=eps**2/(2*p)
            counts['rational_constants']+=1
    out={'status':'all_passed_exactly','counts':counts,'seed':20261027,
         'scope':'New deterministic coupling checks and exact rational bounds; no old solvers.'}
    (Path(__file__).parent/'results/dynamic.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))
if __name__=='__main__':main()
