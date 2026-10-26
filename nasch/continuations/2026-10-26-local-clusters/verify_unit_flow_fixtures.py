"""Certify the exact finite one-speed comparison for archived traffic flows."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json,sys

sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'2026-10-26-rare-braking-error'))
from verify_flow_bounds import FIXTURES,add,mul,scale,bernstein

def main():
    rows=[]
    for n,h,a,b,factor,flow in FIXTURES:
        top=min(n,h); z=[F(0)]*(top+1); zk=[F(0)]*(top+1)
        for k in range(1,top+1):
            value=F(comb(n,k)*comb(h-1,k-1))
            z[top-k]=value; zk[top-k]=k*value
        difference=add(scale(mul(a,z),n),scale(mul(b,zk),-factor))
        coefficients=bernstein(difference)
        assert all(x>=0 for x in coefficients)
        assert all(x>=0 for x in b) and b[0]>0
        assert z[0]>0 and all(x>=0 for x in z)
        rows.append({'N':n,'H':h,'p_interval':['0','1'],
                     'bernstein_coefficients':list(map(str,coefficients)),
                     'status':'certified_exactly'})
    out={'status':'all_passed_exactly','old_stationary_solves_rerun':False,
         'exact_polynomial_certificates':len(rows),'records':rows}
    (Path(__file__).parent/'results'/'unit_flow_fixtures.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'certificates':len(rows),'p_interval':['0','1']}))
if __name__=='__main__':main()
