"""New velocity upper bound against archived full-model rational fixtures.

Positive rational Bernstein coefficients certify entire epsilon intervals.
The earlier stationary solvers are not rerun.
"""
from fractions import Fraction as F
from pathlib import Path
import json,sys
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'2026-10-26-rare-braking-error'))
from verify_flow_bounds import FIXTURES,add,scale,mul,substitute_p,bernstein

def main():
    records=[]
    for n,h,num,den,factor,_ in FIXTURES:
        eps=[F(0),F(1,2)];p=[F(1),F(-1,2)];eta=F(h,n)
        a=substitute_p(num,2);b=scale(substitute_p(den,2),F(factor))
        assert all(c>=0 for c in den) and den[0]>0
        for M in (2,3,4,5,8):
            # p*(upper - U)*b; U=epsilon*a/b, p>=1/2.
            upperp=add(mul(p,add(scale(eps,1+(M-1)*eta),[eta/(M+1)])),
                       scale(eps,(1+2*eta)*M*(M-1)/2))
            poly=add(mul(upperp,b),scale(mul(mul(p,eps),a),-1))
            coefficients=bernstein(poly)
            assert all(c>=0 for c in coefficients),(n,h,M,coefficients)
            records.append({'N':n,'H':h,'M':M,'epsilon_interval':['0','1/2'],
                            'bernstein_coefficients':list(map(str,coefficients))})
    out={'status':'all_passed_exactly','polynomial_certificates':len(records),
         'old_stationary_solvers_rerun':False,'records':records}
    (Path(__file__).parent/'results'/'flow_fixtures.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'certificates':len(records)}))
if __name__=='__main__':main()
