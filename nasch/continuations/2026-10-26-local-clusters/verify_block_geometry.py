"""Exact finite audit of the new full-model qualified-block drift lemma."""
from itertools import product
from fractions import Fraction as F
from pathlib import Path
import json,sys

sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'2026-10-26-rare-braking-error'))
from verify import compositions,original_update

def kval(g,v):
    return tuple(int(v[i]>0 and g[i]>=2) for i in range(len(g)))
def work(g,v):
    c=kval(g,v)
    return sum(c[i]*(g[i]-1) for i in range(len(g)))
def main():
    checks=0; cases=[]; rational_checks=0
    for n in range(2,6):
        masks=list(product((0,1),repeat=n));zero=(0,)*n
        for h in range(1,min(2*n,7)):
            count=0
            for g in compositions(h,n):
                for a in masks:
                    c=kval(g,a); m=sum(c)
                    blocks=sum(c[i] and not c[(i+1)%n] for i in range(n))
                    assert not all(c)
                    gg,vv=original_update(g,a,zero);base=work(gg,vv)
                    assert base-work(g,a)==-blocks
                    weight=sum(g[i] for i in range(n) if not c[i])+m
                    assert weight<=h-m
                    for xi in masks:
                        gx,vx=original_update(g,a,xi)
                        coin_bound=sum(xi[(i+1)%n] for i in range(n) if c[i])
                        coin_bound+=sum(xi[i]*g[i] for i in range(n) if not c[i])
                        assert work(gx,vx)-base<=coin_bound
                        count+=1;checks+=1
                    for eps in (F(1,7),F(1,2),F(6,7)):
                        expected=F(0)
                        for xi in masks:
                            gx,vx=original_update(g,a,xi)
                            probability=eps**sum(xi)*(1-eps)**(n-sum(xi))
                            expected+=probability*(work(gx,vx)-work(g,a))
                        assert expected<=-blocks+eps*(h-m)
                        rational_checks+=1
            cases.append({'N':n,'H':h,'masks_checked':count})
    out={'status':'all_passed_exactly','mask_drift_checks':checks,
         'exact_conditional_drift_checks':rational_checks,'cases':cases,
         'scope':'New qualified-block drift identity; no stationary-system solve.'}
    (Path(__file__).parent/'results'/'block_geometry.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ('status','mask_drift_checks','exact_conditional_drift_checks')}))
if __name__=='__main__':main()
