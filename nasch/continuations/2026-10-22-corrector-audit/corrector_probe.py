"""Exact corrector and folded-potential probe; no convergence claim."""
from fractions import Fraction as Q
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'code'))
from exact_support import compositions, stationary, ring_move, solve_fraction


def height(g):
    a = [0]
    for z in g[:-1]:
        a.append(a[-1] + z)
    return a


def corrector(n, h):
    states, pi = stationary(n, h)
    ix = {g:i for i,g in enumerate(states)}
    L = [[Q(0)] * len(states) for _ in states]
    f = [Q(sum(z-int(z>=2) for z in g), n) for g in states]
    F = sum(p*j for p,j in zip(pi,f))
    for i,g in enumerate(states):
        for j in range(n):
            L[i][ix[ring_move(g,j)]] += 1
            L[i][i] -= 1
    a = [row[:] for row in L]
    b = [F-x for x in f]
    pivot = next(i for i,p in enumerate(pi) if p > 0)
    a[pivot] = list(pi)
    b[pivot] = Q(0)
    values = solve_fraction(a,b)
    assert all(sum(v*c for v,c in zip(values,row)) == F-j for row,j in zip(L,f))
    assert sum(p*c for p,c in zip(pi,values)) == 0
    return F, dict(zip(states,values))


def orbit_corrector(n, h):
    canon = lambda g: min(g[j:]+g[:j] for j in range(n))
    all_states = list(compositions(h,n))
    states = sorted({canon(g) for g in all_states})
    ix = {g:i for i,g in enumerate(states)}
    L = [[Q(0)]*len(states) for _ in states]
    for i,g in enumerate(states):
        for j in range(n):
            L[i][ix[canon(ring_move(g,j))]] += 1
            L[i][i] -= 1
    a = [list(row) for row in zip(*L)]
    a[-1] = [Q(1)]*len(states)
    pi = solve_fraction(a,[Q(0)]*(len(states)-1)+[Q(1)])
    assert sum(pi)==1 and all(p>=0 for p in pi)
    assert all(sum(pi[i]*L[i][j] for i in range(len(states)))==0
               for j in range(len(states)))
    f = [Q(sum(z-int(z>=2) for z in g),n) for g in states]
    F = sum(p*j for p,j in zip(pi,f))
    a = [row[:] for row in L]
    b = [F-j for j in f]
    pivot = next(i for i,p in enumerate(pi) if p > 0)
    a[pivot], b[pivot] = list(pi), Q(0)
    v = solve_fraction(a,b)
    assert all(sum(c*z for c,z in zip(row,v)) == F-j for row,j in zip(L,f))
    assert sum(p*c for p,c in zip(pi,v))==0
    return F,{g:v[ix[canon(g)]] for g in all_states}


def fold(a, n, h, k, shift=0):
    cols = [sorted(a[j+r*n]-r*(h-shift) for r in range(k)) for j in range(n)]
    return [[cols[j][r] for j in range(n)] for r in range(k)]


def gaps(a, h):
    return tuple(a[(j+1)%len(a)] + (h if j+1==len(a) else 0) - a[j]
                 for j in range(len(a)))


def potential(a, n, h, k, psi, shift=0):
    return sum((Q(sum(b),n) + psi[gaps(b,h)] for b in fold(a,n,h,k,shift)), Q(0))/k


def drift(a, n, h, k, psi, shift=0):
    before = potential(a,n,h,k,psi,shift)
    out = Q(0)
    for j in range(k*n):
        b = a[:]
        upper = a[(j+1)%(k*n)] + (k*h-(k-1)*shift if j+1==k*n else 0)
        b[j] = upper-int(upper-a[j]>=2)
        out += potential(b,n,h,k,psi,shift)-before
    return out


if __name__ == '__main__':
    shift = int(sys.argv[1]) if len(sys.argv)>1 else 0
    for n,h,k in [(2,1,2),(2,2,2),(3,2,2),(3,3,2),(4,3,2),(4,4,2),(5,3,2)]:
        F, psi = corrector(n,h)
        worst = None
        total = 0
        for g in compositions(k*h-(k-1)*shift,k*n):
            d = drift(height(g),n,h,k,psi,shift)
            if worst is None or d < worst[0]:
                worst = (d,g)
            total += 1
        print({'n':n,'h':h,'k':k,'shift':shift,'states':total,'F':str(F),'min_drift':str(worst[0]),
               'required_C':str(max(Q(0),n*(F-worst[0])-Q((k-1)*shift,k))),'witness':worst[1]}, flush=True)
