"""Exact tests of new full-model adjacent-pair and gap-threshold balance."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,sys

sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'2026-10-26-rare-braking-error'))
from verify import compositions, original_update

def qual(g,v):
    return tuple(int(v[i]>0 and g[i]>=2) for i in range(len(g)))

def main():
    counts={'gap_threshold_tests':0,'mask_state_tests':0,'rational_final_constants':0}
    pairs=[]
    for n in range(2,6):
        masks=list(product((0,1),repeat=n))
        for h in range(1,min(2*n,7)):
            before=counts['gap_threshold_tests']
            for g in compositions(h,n):
                for a in masks:
                    c=qual(g,a)
                    for xi in masks:
                        ng,nv=original_update(g,a,xi); nc=qual(ng,nv)
                        for i in range(n):
                            ip=(i+1)%n
                            for j in range(2,h+2):
                                old=bool(c[i] and c[ip] and g[i]>=j)
                                new=bool(nc[i] and nc[ip] and ng[i]>=j)
                                birth=int(new and not old)
                                loss=int(old and not new)
                                possible_birth=(int(not c[i] and c[ip])*xi[i]
                                  +int(c[i] and not c[ip])*xi[ip]
                                  +int(not c[i] and not c[ip])*xi[i]*xi[ip]
                                  +int(c[i] and c[ip] and g[i]==j-1)
                                    *xi[ip]*(1-xi[i]))
                                forced_loss=int(c[i] and c[ip] and g[i]==j)*xi[i]*(1-xi[ip])
                                assert birth<=possible_birth,(n,h,g,a,xi,i,j)
                                assert loss>=forced_loss,(n,h,g,a,xi,i,j)
                                counts['gap_threshold_tests']+=1
                        counts['mask_state_tests']+=1
            pairs.append({'N':n,'H':h,'threshold_tests':counts['gap_threshold_tests']-before})
    for n in range(2,71):
        for h in range(1,2*n):
            eta=F(h,n)
            for eps in (F(1,2),F(1,5),F(1,16),F(1,125)):
                p=1-eps
                # Choose a rational x >= cube root epsilon and M >= 1/x.
                # Check the displayed elementary reduction whenever x^3>=eps.
                for x in (F(1,2),F(1,3),F(1,4),F(1,5),F(1)):
                    if x**3<eps:continue
                    M=(x.denominator+x.numerator-1)//x.numerator
                    M=max(M,2)
                    bound=(eps+eps*eta*(M-1)
                           +eps*(1+2*eta)*M*(M-1)/(2*p)+eta/(M+1))
                    assert bound <= (3+6*eta)*x,(n,h,eps,x,M,bound)
                    counts['rational_final_constants']+=1
    out={'status':'all_passed_exactly','counts':counts,'pairs':pairs,
         'scope':'One-step deterministic pair balance and rational constants; no stationary solves.'}
    (Path(__file__).parent/'results'/'verified.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out['counts']))
if __name__=='__main__':main()
