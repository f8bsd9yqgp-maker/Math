"""Exact finite influence exploration; no asymptotic conclusion."""
from fractions import Fraction as Q
from pathlib import Path
import importlib.util
import json

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    'published_corrector', HERE.parent/'2026-10-22-corrector-audit'/'corrector_probe.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def main():
    results = []
    for n,h in [(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(4,2),(4,6),(5,8)]:
        F,psi = module.orbit_corrector(n,h)
        worst = (Q(0),None)
        for g in psi:
            for i,mass in enumerate(g):
                if mass == 0:
                    continue
                y = list(g)
                y[i] -= 1
                y[(i-1)%n] += 1
                p = Q(1,n)+psi[tuple(y)]-psi[g]
                assert 0 <= p <= 1
                if p > worst[0]:
                    worst = p,[list(g),i]
        row = {'N':n,'H':h,'F':str(F),'max_increment':str(worst[0]),
               'N_times_max_increment':str(n*worst[0]),'witness':worst[1]}
        results.append(row)
        print(json.dumps(row),flush=True)
    (HERE/'results'/'influence_probe.json').write_text(json.dumps(
        {'status':'Exact finite exploration; not an asymptotic theorem',
         'results':results},indent=2)+'\n')


if __name__ == '__main__':
    main()
