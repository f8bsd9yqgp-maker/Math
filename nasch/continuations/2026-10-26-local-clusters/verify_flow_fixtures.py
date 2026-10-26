"""Exact Bernstein certificates for the new bound and archived currents.

Uses recorded rational current formulas as fixtures; performs no stationary
state computation. The verified inequality is the unsimplified bound from
the new proof, over the entire stated epsilon interval.
"""
from fractions import Fraction as F
from pathlib import Path
import json,sys

sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'2026-10-26-rare-braking-error'))
from verify_flow_bounds import FIXTURES,add,scale,mul,substitute_p,bernstein

def main():
    rows=[]
    for n,h,num,den,factor,flow in FIXTURES:
        end_den=4*max(n,h); eps=[F(0),F(1,end_den)]; R=F(h,n)
        upper=scale(add(scale(eps,F(5,2)*n+56*h),
                        scale(mul(eps,eps),80*h*h+36*h*n)),R)
        a=substitute_p(num,end_den); b=scale(substitute_p(den,end_den),F(factor))
        assert all(v>=0 for v in den) and den[0]>0
        diff=add(a,scale(b,-flow))
        cert=[]
        for sign in (-1,1):
            coefficients=bernstein(add(mul(upper,b),scale(diff,sign)))
            assert all(v>=0 for v in coefficients) and coefficients[0]==0
            cert.append({'sign':sign,'bernstein_coefficients':list(map(str,coefficients))})
        rows.append({'N':n,'H':h,'epsilon_interval':['0',str(F(1,end_den))],
                     'reduced_current':str(flow),'certificates':cert,
                     'status':'certified_exactly'})
    out={'status':'all_passed_exactly','old_stationary_solves_rerun':False,
         'polynomial_certificates':2*len(rows),'records':rows}
    (Path(__file__).parent/'results'/'flow_fixtures.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'certificates':out['polynomial_certificates']}))
if __name__=='__main__':main()
