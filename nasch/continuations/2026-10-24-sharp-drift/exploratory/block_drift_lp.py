"""Explore bounded block potentials; no floating result is a proof."""
from itertools import product
from pathlib import Path
import json,sys
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix

K=int(sys.argv[1]); length=int(sys.argv[2]); q=K+1
words=list(product(range(K+2),repeat=length+1))
size=q**length
mat=lil_matrix((len(words),2*size+1),dtype=float)
rhs=np.zeros(len(words))
def code(x):
 out=0
 for a in x:out=out*q+min(a,K)
 return out
def d(m):return m-int(m>=2)
for row,x in enumerate(words):
 base=x[:-1]; idx=code(base)
 # Observable is phi at the first length sites; clocks 0..length affect it.
 for j in range(length+1):
  y=list(base)
  if j<length:y[j]-=d(x[j])
  if j>0:y[j-1]+=d(x[j])
  mat[row,code(y)]-=1
  mat[row,idx]+=1
 mat[row,size+code(x[:-1])]-=1
 mat[row,size+code(x[1:])]+=1
 mat[row,-1]=int(x[0]>=2)
 rhs[row]=x[0]
obj=np.zeros(2*size+1);obj[-1]=-1
res=linprog(obj,A_ub=mat.tocsr(),b_ub=rhs,
            bounds=[(None,None)]*(2*size)+[(0,None)],method='highs')
out={'K':K,'length':length,'success':res.success,'status':res.message}
if res.success:
 out.update(kappa=float(res.x[-1]),min_slack=float(np.min(rhs-mat@res.x)),
            phi=res.x[:size].tolist(),coboundary=res.x[size:2*size].tolist())
Path(__file__).with_name('block_drift_K%d_L%d.json'%(K,length)).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('phi','coboundary')},indent=2))
