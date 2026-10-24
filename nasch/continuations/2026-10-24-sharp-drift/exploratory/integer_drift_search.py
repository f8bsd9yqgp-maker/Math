from itertools import product
from pathlib import Path
import json,sys
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import lil_matrix
D=int(sys.argv[1]); K=3;q=4
words=list(product(range(5),repeat=4))
A=lil_matrix((len(words),80),dtype=float);rhs=np.zeros(len(words))
P=lambda a,b:min(a,3)*4+min(b,3)
W=lambda a,b,c:16+(min(a,3)*4+min(b,3))*4+min(c,3)
for row,(a,b,c,e) in enumerate(words):
 r=int(c>=2);d=c-r
 for idx,s in [(P(a,b+d),1),(P(a,b),-1),(P(b+d,r),1),(P(b,c),-1),
               (P(r,e),1),(P(c,e),-1),(W(a,b,c),1),(W(b,c,e),-1)]:A[row,idx]-=s
 rhs[row]=D*c-(17*D//5)*r
res=milp(np.ones(80),integrality=np.ones(80),bounds=Bounds(0,200),
         constraints=LinearConstraint(A.tocsr(),-np.inf,rhs),
         options={'time_limit':10.0,'mip_rel_gap':0.0})
out={'D':D,'message':res.message,'success':res.success}
if res.x is not None:
 x=np.rint(res.x).astype(int)
 assert np.all(A@x<=rhs)
 out.update(P=x[:16].reshape(4,4).tolist(),W=x[16:].reshape(4,4,4).tolist(),
            objective=int(np.sum(x)))
Path(__file__).with_name('integer_drift_D%d.json'%D).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('P','W')},indent=2))
