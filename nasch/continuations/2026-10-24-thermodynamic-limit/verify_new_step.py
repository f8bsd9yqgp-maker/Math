#!/usr/bin/env python3
"""Exact audits of the NEW averaging and localization argument.

No Monte Carlo and no rerun of the preceding continuation's verifier.
Uses integer-scaled finite semigroups; standard library only.
"""
from pathlib import Path
import json
import sys

if not __debug__:
    raise RuntimeError("Run without -O")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]/"code"))
from exact_support import compositions, ring_move


def canonical_heights(g):
    h=[0]
    for mass in g[:-1]:
        h.append(h[-1]+mass)
    return h


def lifted(h,total,j):
    q,r=divmod(j,len(h))
    return h[r]+q*total


def main():
    counts={"chains":0,"semigroup_observables":0,"predictive_jump_checks":0,
            "commutation_checks":0,"phase_mean_checks":0,
            "spatial_sandwich_checks":0,"localization_rounding_checks":0}
    largest_jump_ratio_num=0
    for n in range(2,8):
        for total in range(9):
            states=list(compositions(total,n)); ids={g:i for i,g in enumerate(states)}
            targets=[[ids[ring_move(g,j)] for j in range(n)] for g in states]
            shifts=[[g[0]-int(g[0]>=2)]+[0]*(n-1) for g in states]
            heights=[canonical_heights(g) for g in states]
            balanced=tuple((j+1)*total//n-j*total//n for j in range(n))
            counts["chains"]+=1
            for ell in range(1,n+1):
                for start in sorted({0,1-ell}):
                    block=list(range(start,start+ell))
                    # W_k = ell*n^k * (P^k A)(canonical(g)).
                    w=[sum(lifted(h,total,j) for j in block) for h in heights]
                    # y_k = n^k P^k(sum_{j in block} d(g_j)).
                    y=[sum(g[j%n]-int(g[j%n]>=2) for j in block) for g in states]
                    scale=1
                    counts["semigroup_observables"]+=1
                    for future_steps in range(9):
                        for idx,g in enumerate(states):
                            jumps=[w[dest]+ell*scale*shift-w[idx]
                                   for dest,shift in zip(targets[idx],shifts[idx])]
                            assert min(jumps)>=0,(n,total,ell,start,future_steps,g,jumps)
                            assert sum(jumps)==y[idx]
                            assert 0<=sum(jumps)<=total*scale
                            assert sum(x*x for x in jumps)<=total*total*scale*scale
                            counts["predictive_jump_checks"]+=n
                            counts["commutation_checks"]+=1
                        if ell==1 and start==0:
                            base=w[ids[balanced]]
                            for shift in range(n):
                                rotated=balanced[shift:]+balanced[:shift]
                                assert 0<=w[ids[rotated]]-base<=scale
                                counts["phase_mean_checks"]+=1
                        if future_steps<8:
                            next_w=[];next_y=[]
                            for idx in range(len(states)):
                                next_w.append(sum(w[j]+ell*scale*s
                                                  for j,s in zip(targets[idx],shifts[idx])))
                                next_y.append(sum(y[j] for j in targets[idx]))
                            w,y=next_w,next_y
                            scale*=n
                    # Deterministic left/right inequalities, with rational
                    # quantities multiplied by n*ell.
                    for h in heights:
                        inc=[lifted(h,total,j)-(total*j//n) for j in block]
                        target=h[0]
                        if start==0:
                            assert n*ell*target <= n*sum(inc)+total*ell*(ell-1)//2 + n*ell
                        else:
                            assert n*ell*target >= n*sum(inc)-total*ell*(ell-1)//2 - n*ell
                        counts["spatial_sandwich_checks"]+=1

    # Phase and density rounding in the small auxiliary ring, without redoing
    # the previously audited Poisson-path coupling.
    for n in range(2,35):
        for total in range(2*n+1):
            for m in sorted({2,max(2,n//2),n}):
                aux=total*m//n
                for i in range(n):
                    initial0=total*i//n
                    for j in range(m):
                        diff=total*(i+j)//n-initial0-aux*j//m
                        assert diff in (0,1,2),(n,total,m,i,j,diff)
                        counts["localization_rounding_checks"]+=1

    out={"status":"all exact assertions passed",
         "scope":"new martingale jump, commutation, averaging, and rounding steps only",
         "counts":counts,
         "proof_note":"Finite audits support but do not replace the analytic all-size argument."}
    (HERE/"results").mkdir(exist_ok=True)
    (HERE/"results"/"new_step_verification.json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2))


if __name__=="__main__":
    main()
