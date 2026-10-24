from fractions import Fraction as F
from pathlib import Path
import sys, json
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'code'))
from exact_support import stationary

out=[]
for n,h in [(3,5),(3,8),(4,4),(4,6),(4,8),(5,4),(5,6),(6,4)]:
    ss,pp=stationary(n,h)
    row={'N':n,'H':h,'covariances':[]}
    for threshold in range(1,min(h,5)+1):
        p=sum(w for g,w in zip(ss,pp) if g[0]>=threshold)
        for offset in range(1,n//2+1):
            joint=sum(w for g,w in zip(ss,pp)
                      if g[0]>=threshold and g[offset]>=threshold)
            cov=joint-p*p
            row['covariances'].append({'threshold':threshold,'distance':offset,
                                       'covariance':str(cov),'float':float(cov)})
    out.append(row)
    print(json.dumps({'N':n,'H':h,'positive': [x for x in row['covariances'] if x['float']>0]}),flush=True)
Path(__file__).with_name('covariance_probe.json').write_text(json.dumps(out,indent=2)+'\n')
