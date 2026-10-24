"""Exact small-time covariance search. No stationary-law conclusion."""
import sys,json,math
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[3]/'code'))
from exact_support import compositions,ring_move
results=[]
for n,h in [(3,5),(4,7),(5,8),(6,8)]:
 states=list(compositions(h,n));index={g:j for j,g in enumerate(states)}
 trans=[[index[ring_move(g,i)] for i in range(n)] for g in states]
 def L(f):return [sum(f[j]-f[k] for j in row) for k,row in enumerate(trans)]
 witness=None
 for j in range(1,n):
  a=[[int(g[0]>=2) for g in states]]
  b=[[int(g[j]>=2) for g in states]]
  ab=[[x*y for x,y in zip(a[0],b[0])]]
  alive=set(range(len(states)))
  for order in range(1,9):
   a.append(L(a[-1]));b.append(L(b[-1]));ab.append(L(ab[-1]))
   for k in list(alive):
    value=ab[order][k]-sum(math.comb(order,l)*a[l][k]*b[order-l][k] for l in range(order+1))
    if value:
     alive.remove(k)
     if value>0:
      witness={'N':n,'H':h,'state':states[k],'pair':[0,j],'first_nonzero_order':order,'derivative':value}
      break
   if witness:break
  if witness:break
 results.append({'N':n,'H':h,'witness':witness})
 print(results[-1],flush=True)
Path(__file__).with_name('transient_dependence_probe.json').write_text(json.dumps(results,indent=2)+'\n')
