"""Exact finite audits for the October 22 height-comparison note.

Standard library only. These checks supplement the proofs; they do not prove
the conjectured comparison between different ring sizes.
"""
from fractions import Fraction as Q
from itertools import product, combinations_with_replacement
from bisect import bisect_right
from math import comb
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'code'))
from exact_support import compositions, stationary, ring_move, solve_fraction

if not __debug__:
    raise RuntimeError('Run without -O: assertions are part of this audit.')


def height(g):
    a = [0]
    for n in g[:-1]:
        a.append(a[-1] + n)
    return a


def update(a, h, i, rule):
    b = a[i+1] if i+1 < len(a) else a[0]+h
    if rule == 'backchip':
        a[i] = b - int(b-a[i] >= 2)
    else:
        a[i] = min(a[i]+1, b)


def canonical(g):
    return min(g[i:] + g[:i] for i in range(len(g)))


def orbit_q(n, h):
    states = sorted({canonical(g) for g in compositions(h, n)})
    ix = {g:i for i,g in enumerate(states)}
    a = [[0]*len(states) for _ in states]
    for j,g in enumerate(states):
        for i in range(n):
            a[ix[canonical(ring_move(g,i))]][j] += 1
            a[j][j] -= 1
    raw = [r[:] for r in a]
    a[-1] = [1]*len(states)
    p = solve_fraction(a, [0]*(len(states)-1)+[1])
    assert sum(p)==1 and all(x >= 0 for x in p)
    assert all(sum(x*y for x,y in zip(row,p))==0 for row in raw)
    return sum(x*Q(sum(k>=2 for k in g),n) for g,x in zip(states,p))


def audit():
    checks = {}
    count = 0
    for a,b,c,d in product(range(-3,9), repeat=4):
        if a<=b and c<=d and a<=c and b<=d:
            f = lambda x,y: y-int(y-x>=2)
            assert f(a,b) <= f(c,d)
            assert f(a,b) == min(b,max(a+1,b-1))
            assert min(a+1,b) <= f(a,b)
            count += 1
    checks['ordered_local_height_pairs'] = count

    count = 0
    for n in range(2,6):
        for h in range(3,7):
            states = list(compositions(h,n))
            gather = [i for i in range(n-1,0,-1) for _ in range(h)]
            word = gather+[0]+gather
            for g in states:
                for z in states:
                    a,b = height(g),height(z)
                    shift = -min(x-y for x,y in zip(a,b))
                    a = [x+shift for x in a]
                    for i in word:
                        before = min(x-y for x,y in zip(a,b))
                        update(a,h,i,'backchip')
                        update(b,h,i,'unit')
                        assert min(x-y for x,y in zip(a,b)) >= before
                    assert len(set(x-y for x,y in zip(a,b))) == 1
                    assert min(x-y for x,y in zip(a,b)) >= h-2
                    count += 1
    checks['strict_word_initial_pairs'] = count

    count = 0
    for m in range(1,7):
        for arrivals in combinations_with_replacement(range(0,10,2),m):
            for bits in product([0,1], repeat=5):
                services = [2*i+1 for i,b in enumerate(bits) if b]+[11,13]
                queue, departures = [], [None]*m
                next_arrival = 0
                for s in services:
                    while next_arrival<m and arrivals[next_arrival]<s:
                        queue.append(next_arrival)
                        next_arrival += 1
                    remove = len(queue)-int(len(queue)>=2)
                    for customer in queue[:remove]:
                        departures[customer] = s
                    queue = queue[remove:]
                recurrence = []
                previous = float('-inf')
                for j,a in enumerate(arrivals):
                    following = arrivals[j+1] if j+1<m else float('inf')
                    threshold = min(following,max(a,previous))
                    previous = services[bisect_right(services,threshold)]
                    recurrence.append(previous)
                assert departures == recurrence
                count += 1
    checks['FIFO_arrival_and_service_patterns'] = count

    cache = {}
    for n in range(2,9):
        for h in range(1,11):
            if comb(n+h-1,n-1) > 300:
                continue
            q = orbit_q(n,h)
            cache[n,h] = q
            bound = Q(h*(h-1),n*(h+n-1))
            assert q <= bound
            if h<=2:
                assert q==bound
            else:
                ell = 2*h*(n-1)+1
                assert q <= bound-Q(h-2,ell*n**(ell-1))
            if (n-1,h) in cache:
                assert Q(h,n)-q <= Q(h,n-1)-cache[n-1,h]
    checks['exact_stationary_chains'] = len(cache)

    quotient_checks = 0
    for n,h in [(2,5),(3,4),(4,3),(5,3)]:
        gs, ps = stationary(n,h)
        q = sum(p for g,p in zip(gs,ps) if g[0]>=2)
        assert q == cache[n,h]
        quotient_checks += 1
    checks['rotation_quotient_independent_checks'] = quotient_checks

    conjecture_checks = {'join_n_plus_m':0,'join_n_plus_m_minus_1':0,
                        'dilation_2':0,'dilation_3':0,'ratio_order':0}
    for (n,h), q in cache.items():
        for (m,k), r in cache.items():
            for shift,name in [(0,'join_n_plus_m'),(-1,'join_n_plus_m_minus_1')]:
                target = (n+m+shift,h+k-1)
                if target in cache:
                    assert cache[target] <= max(q,r)
                    conjecture_checks[name] += 1
            if n>=m and (h-1)*(m-1) <= (k-1)*(n-1):
                assert q<=r
                conjecture_checks['ratio_order'] += 1
        for k in [2,3]:
            target = (k*n,k*(h-1)+1)
            if target in cache:
                assert cache[target] <= q
                conjecture_checks[f'dilation_{k}'] += 1
    return {'status':'PASS', 'proved_statement_audits':checks,
            'finite_checks_of_UNPROVED_conjectures':conjecture_checks,
            'q_values':{f'{n},{h}':str(q) for (n,h),q in cache.items()}}


if __name__ == '__main__':
    result = audit()
    out = Path(__file__).resolve().parent / 'results' / 'verified.json'
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='q_values'},indent=2))
