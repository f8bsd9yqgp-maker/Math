"""Exploratory search for a pointwise stationary-current certificate.

Seek sum_i (g_i-kappa*r(g_i)) + L sum_i phi(g_i,g_(i+1)) >= 0.
A telescoping triple potential certifies each individual four-site term.
phi and the triple potential use masses truncated at K.
"""
from itertools import product
from pathlib import Path
import json, sys
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix

K=int(sys.argv[1]) if len(sys.argv)>1 else 3
q=K+1
npair=q*q
ntriple=q*q*q
nvar=npair+ntriple+1
quads=list(product(range(K+2),repeat=4))
mat=lil_matrix((len(quads),nvar),dtype=float)
rhs=np.zeros(len(quads))
P=lambda a,b: min(a,K)*q+min(b,K)
T=lambda a,b,c:npair+(min(a,K)*q+min(b,K))*q+min(c,K)
for row,(a,b,c,e) in enumerate(quads):
    r=int(c>=2); d=c-r
    # -[c-kappa*r+L(phi sum)+telescoping triple difference] <= 0
    for idx,sgn in [(P(a,b+d),1),(P(a,b),-1),
                    (P(b+d,r),1),(P(b,c),-1),
                    (P(r,e),1),(P(c,e),-1),
                    (T(a,b,c),1),(T(b,c,e),-1)]:
        mat[row,idx]-=sgn
    mat[row,-1]=r
    rhs[row]=c
obj=np.zeros(nvar);obj[-1]=-1
res=linprog(obj,A_ub=mat.tocsr(),b_ub=rhs,
            bounds=[(None,None)]*(nvar-1)+[(0,None)],method='highs')
report={'K':K,'success':res.success,'status':res.message}
if res.success:
    report.update(kappa=float(res.x[-1]),minimum_slack=float(np.min(rhs-mat@res.x)),
                  phi=res.x[:npair].reshape(q,q).tolist(),
                  triple=res.x[npair:npair+ntriple].reshape(q,q,q).tolist())
print(json.dumps({k:v for k,v in report.items() if k not in ('phi','triple')},indent=2))
Path(__file__).with_name('drift_lp_K%d.json'%K).write_text(json.dumps(report,indent=2)+'\n')
