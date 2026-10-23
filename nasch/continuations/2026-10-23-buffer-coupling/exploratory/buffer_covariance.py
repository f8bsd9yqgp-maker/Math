import importlib.util,sys
from pathlib import Path
from itertools import product
import numpy as np
from scipy.sparse import coo_matrix, eye
from scipy.sparse.linalg import spsolve
p=Path(__file__).resolve().parents[1]/'verify.py'
spec=importlib.util.spec_from_file_location('v',p);v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
for n,h in [(2,h) for h in range(1,9)]+[(3,h) for h in range(1,5)]+[(4,h) for h in range(1,4)]:
 F,psi=v.corrector_module.corrector(n,h);F=float(F)
 gs=list(v.compositions(h,n))
 chi={g:float(psi[g])+sum((n-1-i)*g[i] for i in range(n))/n for g in gs}
 for B in [1,2,3,6]:
  states=list(product(gs,gs,range(B+1)));ix={s:i for i,s in enumerate(states)};m=len(states)
  rr=[];cc=[];dd=[];loss=[];cross=[];weighted=[]
  for si,(g0,g1,b) in enumerate(states):
   cores=(g0,g1);buf=(b,B-b);ls=[]
   for r in range(2):
    g=cores[r];a=v.d(g[0]);z=min(a,buf[r]);l=float(v.Q(a-z,n)+psi[v.ring_move(g,0)]-psi[v.partial_core(g,z)]);ls.append(l)
   loss.append(sum(ls)/2)
   weighted.append(((b+chi[g1]-chi[g0])*ls[0]+(B-b+chi[g0]-chi[g1])*ls[1])/2)
   cross.append(((chi[g1]-chi[g0])*ls[0]+(chi[g0]-chi[g1])*ls[1])/2)
   for r,j in product(range(2),range(n)):
    gp,bp,amount=v.protocol_move(cores,buf,r,j);sj=ix[(gp[0],gp[1],bp[0])]
    rr.extend([si,si]);cc.extend([sj,si]);dd.extend([1.,-1.])
  L=coo_matrix((dd,(rr,cc)),shape=(m,m)).tocsr()
  A=L.T.tolil();A[-1,:]=np.ones(m);bb=np.zeros(m);bb[-1]=1
  pp=spsolve(A.tocsr(),bb)
  assert np.max(np.abs(pp@L))<1e-9 and min(pp)>-1e-9
  el=np.dot(pp,loss);cr=np.dot(pp,cross)
  print(n,h,B,'loss',el,'cross',cr,'weighted',np.dot(pp,weighted),'boundratio',el*B/(F*F),flush=True)
