"""Rational audits of the monotone corrector and folding obstruction.

Standard library only. The general results are proved in README.md; this
program checks finite instances and does not certify thermodynamic convergence.
"""
from fractions import Fraction as Q
from itertools import product
from math import floor
from pathlib import Path
import json
from corrector_probe import (corrector, orbit_corrector, height, gaps, fold,
                             drift, compositions, ring_move)
from stagger_probe import phi

if not __debug__:
    raise RuntimeError('Assertions are required; do not use -O.')


def B(a,b):
    return min(b,max(a+1,b-1))


def update(a,h,j):
    a[j]=B(a[j],a[(j+1)%len(a)]+(h if j+1==len(a) else 0))


def run():
    counts={}
    chains=[]
    pairs=0
    equation_checks=0
    jump_bounds=0
    bias_bounds=0
    for n in range(2,6):
        for h in range(1,6):
            F,psi=corrector(n,h)
            FF,pp=orbit_corrector(n,h)
            assert F==FF and psi==pp
            profiles={g:height(g) for g in psi}
            values={g:Q(sum(a),n)+psi[g] for g,a in profiles.items()}
            for g,a in profiles.items():
                value=values[g]
                rate=Q(0)
                quadratic_rate=Q(0)
                for j in range(n):
                    b=a[:];update(b,h,j)
                    gp=gaps(b,h)
                    jump=Q(sum(b),n)+psi[gp]-value
                    assert 0<=jump<=F
                    rate+=jump
                    quadratic_rate+=jump*jump
                assert rate==F
                assert quadratic_rate<=F*F
                jump_bounds+=1
                equation_checks+=1
                for z,b in profiles.items():
                    delta=[x-y for x,y in zip(a,b)]
                    assert min(delta)<=value-values[z]<=max(delta)
                    pairs+=1
            assert max(values.values())-min(values.values())==Q(h*(n-1),n)
            bias_bounds+=1
            chains.append({'n':n,'h':h,'states':len(psi),'current':str(F)})
    counts['full_and_quotient_correctors']=len(chains)
    counts['generator_equations']=equation_checks
    counts['corrector_oscillation_pairs']=pairs
    counts['martingale_jump_and_quadratic_bounds']=jump_bounds
    counts['bond_current_bias_oscillation_bounds']=bias_bounds

    rounding=0
    for ai,bi,ui in product(range(-8,17),range(-8,17),range(4)):
        a,b,u=Q(ai,4),Q(bi,4),Q(ui,4)
        if a>b:continue
        assert floor(B(a,b)+u)==B(floor(a+u),floor(b+u))
        rounding+=1
    counts['rounding_commutations']=rounding

    resets=0
    interpolated=0
    for n in range(2,5):
        for h in range(1,5):
            F,psi=orbit_corrector(n,h)
            for z in compositions(2*h,n):
                a=[Q(x,2) for x in height(z)]
                original=a[:]
                for j in range(n-1,0,-1):
                    update(a,h,j);update(a,h,j)
                assert a==[original[0]]+[original[0]+h]*(n-1)
                resets+=1
                value=phi(original,h,psi)
                rate=Q(0)
                for j in range(n):
                    b=original[:];update(b,h,j)
                    rate+=phi(b,h,psi)-value
                assert rate==F
                interpolated+=1
    counts['half_integer_gather_resets']=resets
    counts['interpolated_generator_equations']=interpolated

    raw=0
    for n in range(2,102,2):
        a=[j+int(j%2==1) for j in range(n)]
        b=[n+j+int(j%2==0) for j in range(n)]
        original=gaps(a+b,2*n)
        rows=fold(a+b,n,n,2)
        assert sum(x>=2 for x in original)==n-1
        assert all(gaps(row,n)==(1,)*n for row in rows)
        raw+=1
    counts['raw_sorting_family_instances']=raw

    obstruction=[]
    for n in (3,5,7):
        F,psi=orbit_corrector(n,n)
        g=[2 if j%2==0 else 0 for j in range(2*n)]
        g[n-1]=1
        assert sum(g)==2*n-1
        a=height(g)
        rows=fold(a,n,n,2,1)
        assert rows==[list(range(n)),list(range(1,n+1))]
        assert drift(a,n,n,2,psi,1)==F/2
        obstruction.append({'n':n,'small_current':str(F),
                            'folded_drift':str(F/2),
                            'necessary_error_constant':str(n*F/2-Q(1,2))})
    counts['harmonic_folding_family_instances']=len(obstruction)
    return {'status':'PASS','scope':'Finite audits; fixed-density convergence remains OPEN',
            'checks':counts,'chains':chains,'harmonic_obstruction':obstruction}


if __name__=='__main__':
    result=run()
    target=Path(__file__).resolve().parent/'results'/'verified.json'
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='chains'},indent=2))
