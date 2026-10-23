"""Test cyclic max/min/mean envelopes of the folded corrector."""
from fractions import Fraction as Q
from pathlib import Path
import json
from corrector_probe import orbit_corrector, height, potential, compositions, ring_move


def probe(n,h):
    F,psi=orbit_corrector(n,h)
    states=list(compositions(2*h-1,2*n))
    raw={g:potential(height(g),n,h,2,psi,1)-Q(sum(height(g)),2*n) for g in states}
    envelopes={m:{} for m in ('max','min','mean')}
    for g in states:
        vals=[raw[g[j:]+g[:j]] for j in range(2*n)]
        envelopes['max'][g]=max(vals)
        envelopes['min'][g]=min(vals)
        envelopes['mean'][g]=sum(vals)/(2*n)
    worst={m:None for m in envelopes}
    for g in states:
        f=Q(sum(z-int(z>=2) for z in g),2*n)
        for m,v in envelopes.items():
            d=f+sum(v[ring_move(g,j)]-v[g] for j in range(2*n))
            if worst[m] is None or d<worst[m][0]:worst[m]=(d,g)
    return {'n':n,'h':h,'states':len(states),'F':str(F),'worst':{m:{'drift':str(w[0]),'required_C':str(max(Q(0),n*(F-w[0])-Q(1,2))),'witness':w[1]} for m,w in worst.items()}}


if __name__=='__main__':
    records=[]
    for n,h in [(2,2),(3,2),(3,3),(4,3),(4,4),(5,3),(5,5)]:
        result=probe(n,h)
        records.append(result)
        print(json.dumps(result),flush=True)
    (Path(__file__).resolve().parent/'results'/'envelope_probe.json').write_text(
        json.dumps({'status':'Exact finite certificate probes; no uniform bound proved',
                    'results':records},indent=2)+'\n')
