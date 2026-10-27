"""New exact cylinder-observable and escaped-mass obstruction audits."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
from verify_local_reduction import project,advance,compositions

def fire(g,i):
    gg=list(g);d=g[i]-int(g[i]>=2);gg[i]-=d;gg[(i-1)%len(g)]+=d
    return tuple(gg)

def total(g,r,f):
    return sum(f(tuple(g[(i+j)%len(g)] for j in range(r))) for i in range(len(g)))

def main():
    rows=[];count=0;obstructions=0
    functions=[(1,'pile',lambda x:int(x[0]>=2)),
               (1,'signed_parity',lambda x:2*(x[0]%2)-1),
               (2,'pile_empty',lambda x:int(x[0]>=2 and x[1]==0)),
               (2,'ordered',lambda x:int(x[0]<x[1]))]
    for n in (5,6,7):
        masks=list(product((0,1),repeat=n))
        for h in range(1,4):
            for g in compositions(h,n):
                for r,name,f in functions:
                    if n<=2*r+2:continue
                    before=total(g,r,f)
                    delta=[total(fire(g,i),r,f)-before for i in range(n)]
                    assert all(abs(a)<=2*(r+1) for a in delta)
                    for xi in masks:
                        after=project(*advance(g,[0]*n,xi))
                        err=total(after,r,f)-before-sum(xi[i]*delta[i] for i in range(n))
                        pairs=sum(xi[i]*xi[(i+d)%n] for i in range(n)
                                  for d in range(-r,r+1) if d)
                        assert abs(err)<=4*(r+1)*pairs,(n,h,g,r,xi,err,pairs)
                        count+=1
            rows.append({'N':n,'H':h})
    for n in range(5,121):
        for h in (1,n//2,n,2*n-1):
            g=(h,)+(0,)*(n-1)
            for r,name,f in functions:
                if n<=2*r+2:continue
                F=total(g,r,f)
                # Only the pile clock can change this state.
                residual=Q(sum(total(fire(g,i),r,f)-F for i in range(n)),n)
                assert abs(residual)<=Q(4*r,n)
                zero=f((0,)*r)
                assert abs(Q(F,n)-zero)<=Q(2*r,n)
                obstructions+=1
    out={'status':'all_passed_exactly','resting_cylinder_mask_checks':count,
         'escaped_mass_obstruction_checks':obstructions,'pairs':rows,
         'scope':'Exact finite structural tests; the one-pile examples are not stationary full-model laws.'}
    (Path(__file__).parent/'results'/'cylinders.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))
if __name__=='__main__':main()
