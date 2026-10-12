"""Independent optimization cross-check (requires NumPy/SciPy, not needed for proof)."""
import numpy as np
from scipy.optimize import linear_sum_assignment
from time import perf_counter
N=14;B=13;V=1<<B;mask=(1<<N)-1
W=[w for w in range(1<<N) if all(w<((w<<k | w>>(N-k))&mask) for k in range(1,N))]
delta=np.zeros(V,dtype=int)
for w in W:delta[w>>1]+=1;delta[w&(V-1)]-=1
starts=np.where(delta==1)[0];ends=np.where(delta==-1)[0]
assert len(starts)==len(ends)==479

def dist(a,b):
 for k in range(B+1):
  if (a&((1<<(B-k))-1)) == b>>k: return k
 raise AssertionError
M=np.zeros((480,480),dtype=np.int16)
for i,a in enumerate(ends):
 for j,b in enumerate(starts):
  M[i,j]=dist(int(a),int(b))
M[-1,-1]=32767
t=perf_counter();rows,cols=linear_sum_assignment(M)
score=M[rows,cols].sum();start=starts[cols[rows==479]][0];end=ends[rows[cols==479]][0]
print('independent Hungarian edges',score,'total length',score+len(W)+B,'time',round(perf_counter()-t,3),'start',start,'end',end)
assert score==4390
