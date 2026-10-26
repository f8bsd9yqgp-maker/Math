"""New local-support and pair-workload tests; no stationary-system solves."""
from itertools import product
from collections import Counter
from pathlib import Path
import sys,json
from fractions import Fraction as F

SOURCE = Path(__file__).resolve().parent.parent / '2026-10-26-rare-braking-error'
sys.path.insert(0, str(SOURCE))
from verify import compositions, remaining, original_update, run_word, serialized_word, d

def affected(c,xi):
    n=len(c); on=[bool(c[i] or xi[i]) for i in range(n)]; seen=set(); result=set()
    for i in range(n):
        if not on[i] or i in seen: continue
        stack=[i]; seen.add(i); component=[]
        while stack:
            j=stack.pop();component.append(j)
            for z in ((j-1)%n,(j+1)%n):
                if on[z] and z not in seen:
                    seen.add(z);stack.append(z)
        if any(c[j] for j in component) and any(xi[j] for j in component):
            result.update(component)
    return result

def upword(selected,n):
    left=set(selected);out=[]
    while left:
        eligible=[i for i in left if (i+1)%n not in left]
        assert eligible,(selected,left)
        for i in sorted(eligible):out.append(i);left.remove(i)
    return out

def pairpotential(r):
    return sum(min(r[i],r[j]) for i in range(len(r)) for j in range(i+1,len(r)))

def test_pair(n,h):
    counts=Counter()
    masks=list(product(range(2),repeat=n))
    for g in compositions(h,n):
        for a in masks:
            c=tuple(int(a[i] and g[i]>=2) for i in range(n)); ell=remaining(g,a)
            G=tuple(g[i]+ell[(i+1)%n]-ell[i] for i in range(n))
            assert min(G)>=0 and sum(G)==h
            k=sum(a); r=tuple(a[i]+ell[i] for i in range(n)); V0=pairpotential(ell)
            assert V0-pairpotential(r)==-k*(k-1)//2
            for xi in masks:
                gg,v=original_update(g,a,xi); ee=remaining(gg,v)
                delta=tuple(v[i]+ee[i]-ell[i] for i in range(n))
                _,dr=run_word(G,serialized_word(G,xi))
                S=affected(c,xi)
                assert all(delta[i]==dr[i] for i in range(n) if i not in S),(n,h,g,a,xi,delta,dr,S,G)
                counts['support_comparisons']+=1
                rr=tuple(int(v[i]>0)+ee[i] for i in range(n)); K=sum(xi)
                budget=sum(xi[i]*d(G[i]) for i in range(n))
                positive=sum(max(rr[i]-ell[i],0) for i in range(n))
                assert pairpotential(rr)-V0 <= max(k+K-1,0)*positive
                assert positive<= (k+K)*budget
                counts['pair_workload_inequalities']+=1
                if len(S)<n:
                    P=[0]*n
                    for i in range(1,n):P[i]=P[i-1]+G[i-1]
                    low=[P[i]+min(delta[i],dr[i]) for i in range(n)]
                    high=[P[i]+max(delta[i],dr[i]) for i in range(n)]
                    gaps=tuple((low[(i+1)%n]+(h if i==n-1 else 0))-low[i] for i in range(n))
                    assert min(gaps)>=0 and sum(gaps)==h
                    word=[j for i in upword(S,n) for j in (i,i)]
                    _,dw=run_word(gaps,word)
                    assert all(low[i]+dw[i]>=high[i] for i in range(n)),(n,h,g,a,xi,low,high,word,dw)
                    counts['two_firing_domination']+=1
                else:
                    assert max(abs(delta[i]-dr[i]) for i in range(n))<=2*h
                    counts['full_ring_fallback']+=1
    return {'N':n,'H':h,**counts}

def exact_cluster_expectations():
    checks=0
    for n in range(2,9):
        masks=list(product((0,1),repeat=n))
        for c in masks:
            if all(c): continue
            k=sum(c)
            counts=Counter()
            for xi in masks:
                counts[sum(xi)] += len(affected(c,xi))
            for eps in (F(1,2),F(1,5),F(1,17)):
                expectation=sum(value*eps**m*(1-eps)**(n-m)
                                for m,value in counts.items())
                upper=eps*(k*k+2*k+F(2*k,1-eps))
                assert expectation<=upper,(n,c,eps,expectation,upper)
                assert upper<=eps*(k*k+6*k)
                checks+=1
    return checks

def exact_moment_constants():
    checks=0
    for n in range(2,51):
        for h in range(1,2*n):
            for frac in (F(1),F(1,2),F(1,5),F(1,100)):
                eps=frac/(4*max(h,n));B0=1+(n-1)*eps
                m=eps*h*B0/(1-eps*h)
                f=(4*eps*h*B0*m+4*eps**2*h*(n-1)
                   +2*eps**3*h*(n-1)*(n-2))/(1-2*eps*h)
                assert m<=2*eps*h
                assert f<=20*eps**2*h**2+9*eps**2*h*n
                C=F(5*n-1,2)
                exact=C*eps+4*(7*m+f)
                coarse=(F(5,2)*n+56*h)*eps+80*eps**2*h**2+36*eps**2*h*n
                assert exact<=coarse
                R=F(h,n)
                assert R*coarse<=(F(5,2)*R+65*R**2+20*R**3)*eps*n
                checks+=1
    return checks

def main():
    rows=[test_pair(n,h) for n in range(2,6) for h in range(1,min(2*n,7))]
    out={'status':'all_passed_exactly', 'rows':rows,
         'totals':{x:sum(row.get(x,0) for row in rows) for x in
                   ['support_comparisons','pair_workload_inequalities','two_firing_domination','full_ring_fallback']},
         'exact_cluster_expectation_checks':exact_cluster_expectations(),
         'exact_moment_constant_checks':exact_moment_constants()}
    (Path(__file__).parent/'results'/'verified.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'totals':out['totals'],
                      'exact_cluster_expectation_checks':out['exact_cluster_expectation_checks'],
                      'exact_moment_constant_checks':out['exact_moment_constant_checks']}))
if __name__=='__main__': main()
