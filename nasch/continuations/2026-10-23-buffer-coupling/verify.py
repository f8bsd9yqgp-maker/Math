"""Exact audits for the 23 October continuation; no asymptotic inference.

Run from any working directory. Python standard library only. All finite
stationary certificates are checked again on labelled, unquotiented states.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import argparse
import importlib.util
import json
import sys

if not __debug__:
    raise SystemExit('Run without -O: this audit requires Python assertions.')

HERE = Path(__file__).resolve().parent
NASCH = HERE.parents[1]
sys.path.insert(0, str(NASCH / 'code'))
from exact_support import compositions, d, ring_move, solve_fraction

spec = importlib.util.spec_from_file_location(
    'published_corrector', HERE.parent / '2026-10-22-corrector-audit' / 'corrector_probe.py')
corrector_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(corrector_module)


def canonical(g):
    return min(g[j:] + g[:j] for j in range(len(g)))


def clock_moves(g, n, c):
    for j in range(2*n):
        yield ring_move(g, j), 1-c
    for j in range(n):
        yield ring_move(ring_move(g, j), j+n), c


def correlation_certificate(n, h, c):
    full = list(compositions(2*h-1, 2*n))
    states = sorted({canonical(g) for g in full})
    ix = {g:i for i,g in enumerate(states)}
    size = len(states)
    L = [[Q(0)]*size for _ in states]
    for i,g in enumerate(states):
        for y,rate in clock_moves(g,n,c):
            L[i][ix[canonical(y)]] += rate
            L[i][i] -= rate
    a = [list(row) for row in zip(*L)]
    a[-1] = [Q(1)]*size
    p = solve_fraction(a, [Q(0)]*(size-1)+[Q(1)])
    assert all(x >= 0 for x in p) and sum(p) == 1
    assert all(sum(p[i]*L[i][j] for i in range(size)) == 0
               for j in range(size))

    # Independent expansion: every labelled configuration and every event.
    orbit_sizes = {g:0 for g in states}
    for g in full:
        orbit_sizes[canonical(g)] += 1
    full_p = {g:p[ix[canonical(g)]]/orbit_sizes[canonical(g)] for g in full}
    assert sum(full_p.values()) == 1 and min(full_p.values()) >= 0
    balance = {g:Q(0) for g in full}
    for g in full:
        for y,rate in clock_moves(g,n,c):
            balance[y] += full_p[g]*rate
            balance[g] -= full_p[g]*rate
    assert all(x == 0 for x in balance.values())
    q = sum(full_p[g]*Q(sum(z >= 2 for z in g),2*n) for g in full)
    assert q == sum(p[i]*Q(sum(z >= 2 for z in g),2*n)
                    for i,g in enumerate(states))
    return {'n':n, 'h':h, 'c':str(c), 'full_states':len(full),
            'rotation_classes':size, 'q':str(q),
            'class_weights':[{'g':list(g), 'p':str(v)} for g,v in zip(states,p)]}


def audit_symbolic_vector():
    count = 0
    for i in range(21):
        c = Q(i,20)
        D = c*c-14*c+19
        p = [5*(1-c)/D, (1-c)*(2-c)/D, 5*(1-c)/D,
             (3+c)/D, (4-2*c)/D]
        L = [[-1,0,1,0,0], [0,-2,1,1,0], [1,0,-2,0,1],
             [0,0,1-c,c-2,1], [0,1-c,0,1+c,-2]]
        assert all(v >= 0 for v in p) and sum(p) == 1
        assert all(sum(p[j]*L[j][i] for j in range(5)) == 0 for i in range(5))
        assert sum(p[:4])/4 == (c*c-12*c+15)/(4*D)
        assert -(c*c-4*c+9)/(2*D*D) < 0
        count += 1
    return count


def embed_cover(g, x, sheet, k):
    y = list(g)*k
    y[sheet*len(g)+x] += 1
    return tuple(y)


def audit_cover():
    count = 0
    parameters = []
    for n,h,k in product(range(2,5), range(1,5), (2,3)):
        parameters.append([n,h,k])
        for g in compositions(h-1,n):
            for x,sheet in product(range(n),range(k)):
                big = embed_cover(g,x,sheet,k)
                upper = list(g); upper[x] += 1
                assert sum(z>=2 for z in big) == (
                    (k-1)*sum(z>=2 for z in g)+sum(z>=2 for z in upper))
                for i in range(n):
                    moved = big
                    for r in range(k):
                        moved = ring_move(moved,i+r*n)
                    after = ring_move(g,i)
                    xp,sp = x,sheet
                    if x == i and g[i] != 1:
                        xp = (x-1)%n
                        if x == 0:
                            sp = (sheet-1)%k
                    assert moved == embed_cover(after,xp,sp,k)
                    assert sum(moved) == k*(h-1)+1
                    count += 1
    return {'parameters':parameters,'event_identities':count}


def physical(cores,buffers):
    out = []
    for g,b in zip(cores,buffers):
        block = list(g)
        block[-1] += b
        out.extend(block)
    return tuple(out)


def partial_core(g,v):
    out = list(g)
    out[0] -= v
    out[-1] += v
    return tuple(out)


def protocol_move(cores,buffers,r,j):
    gs,bs = list(cores),list(buffers)
    if j:
        amount = d(gs[r][j])
        gs[r] = ring_move(gs[r],j)
    else:
        amount = min(d(gs[r][0]),bs[r])
        gs[r] = partial_core(gs[r],amount)
        bs[r] -= amount
        bs[(r-1)%len(bs)] += amount
    return tuple(gs),tuple(bs),amount


def audit_buffers():
    count = 0
    states_checked = 0
    losses_checked = 0
    energy_checked = 0
    support_checked = 0
    parameters = []
    for n,h in product((2,3),range(1,4)):
        F,psi = corrector_module.corrector(n,h)
        core_states = list(compositions(h,n))
        chi = {g:psi[g]+Q(sum((n-1-i)*g[i] for i in range(n)),n)
               for g in core_states}
        chi_min = min(chi.values())
        chi = {g:x-chi_min for g,x in chi.items()}
        A = Q(h*(n-1),n)
        assert min(chi.values()) == 0 and max(chi.values()) == A
        q = Q(h,n)-F
        K = h-1-q
        assert K == A+F-1 and K >= 0
        for k,B in product((2,),range(4)):
            parameters.append([n,h,k,B])
            for cores in product(core_states,repeat=k):
                for buffers in compositions(B,k):
                    states_checked += 1
                    before = physical(cores,buffers)
                    assert sum(before) == k*h+B
                    w = tuple(buffers[r]+chi[cores[(r+1)%k]]-chi[cores[r]]
                              for r in range(k))
                    assert sum(w) == B
                    losses = []
                    for r,g in enumerate(cores):
                        v = min(d(g[0]),buffers[r])
                        a_full = Q(d(g[0]),n)+psi[ring_move(g,0)]-psi[g]
                        a_part = Q(v,n)+psi[partial_core(g,v)]-psi[g]
                        loss = a_full-a_part
                        losses.append(loss)
                        assert 0 <= a_part <= a_full <= F
                        if loss > 0:
                            assert buffers[r] <= d(g[0])-1
                            assert w[r] <= K
                            support_checked += 1
                        drift = a_part
                        for j in range(1,n):
                            drift += Q(d(g[j]),n)+psi[ring_move(g,j)]-psi[g]
                        assert drift == F-loss
                        losses_checked += 1
                    energy_drift = Q(0)
                    V = Q(0)
                    per_block_square_sum = [Q(0)]*k
                    for r,j in product(range(k),range(n)):
                        gs,bs,v = protocol_move(cores,buffers,r,j)
                        assert all(sum(g) == h and min(g) >= 0 for g in gs)
                        assert sum(bs) == B and min(bs) >= 0
                        after = list(before)
                        pos = r*n+j
                        after[pos] -= v
                        after[(pos-1)%(k*n)] += v
                        assert tuple(after) == physical(gs,bs)
                        assert 0 <= v <= d(before[pos])
                        a = Q(v,n)+psi[gs[r]]-psi[cores[r]]
                        wp = tuple(bs[s]+chi[gs[(s+1)%k]]-chi[gs[s]]
                                   for s in range(k))
                        assert wp[r] == w[r]-a
                        assert wp[(r-1)%k] == w[(r-1)%k]+a
                        increment = sum(x*x for x in wp)-sum(x*x for x in w)
                        assert increment == 2*a*(w[(r-1)%k]-w[r])+2*a*a
                        energy_drift += increment
                        V += a*a
                        per_block_square_sum[r] += a*a
                        count += 1
                    assert all(x <= F*F for x in per_block_square_sum)
                    assert energy_drift == -2*sum(
                        (w[(r-1)%k]-w[r])*losses[r] for r in range(k))+2*V
                    energy_checked += 1
        # Exact absorbing state at zero reserve, and its entire lost drift.
        g = (h,)+(0,)*(n-1)
        assert Q(d(g[0]),n)+psi[ring_move(g,0)]-psi[g] == F
    return {'parameters':parameters,'states':states_checked,
            'physical_event_checks':count,'corrector_loss_checks':losses_checked,
            'quadratic_generator_checks':energy_checked,
            'positive_loss_support_checks':support_checked,
            'zero_buffer_absorbing_examples':6}


def stationary_buffer_certificate(n,h,B):
    """Full labelled exact certificate; no assumed block exchangeability."""
    F,psi = corrector_module.corrector(n,h)
    gs = list(compositions(h,n))
    states = list(product(gs,gs,range(B+1)))
    ix = {s:i for i,s in enumerate(states)}
    m = len(states)
    L = [[Q(0)]*m for _ in states]
    chi = {g:psi[g]+Q(sum((n-1-i)*g[i] for i in range(n)),n) for g in gs}
    losses = []
    weighted = []
    square_rates = []
    for i,(g0,g1,b) in enumerate(states):
        cores,buffers = (g0,g1),(b,B-b)
        ls = []
        for r in range(2):
            g = cores[r]
            v = min(d(g[0]),buffers[r])
            ls.append(Q(d(g[0])-v,n)+psi[ring_move(g,0)]-psi[partial_core(g,v)])
        w = [buffers[r]+chi[cores[1-r]]-chi[cores[r]] for r in range(2)]
        losses.append(sum(ls)/2)
        weighted.append(sum(wr*lr for wr,lr in zip(w,ls)))
        V = Q(0)
        for r,j in product(range(2),range(n)):
            after,bs,v = protocol_move(cores,buffers,r,j)
            z = ix[(after[0],after[1],bs[0])]
            L[i][z] += 1
            L[i][i] -= 1
            a = Q(v,n)+psi[after[r]]-psi[cores[r]]
            V += a*a
        square_rates.append(V)
    a = [list(row) for row in zip(*L)]
    a[-1] = [Q(1)]*m
    p = solve_fraction(a,[Q(0)]*(m-1)+[Q(1)])
    assert sum(p) == 1 and min(p) >= 0
    assert all(sum(p[i]*L[i][j] for i in range(m)) == 0 for j in range(m))
    loss = sum(x*y for x,y in zip(p,losses))
    W = sum(x*y for x,y in zip(p,weighted))
    V = sum(x*y for x,y in zip(p,square_rates))
    assert B*loss == V/2+W
    assert W > 0  # Refutes a proposed nonpositivity shortcut, not the loss bound.
    return {'n':n,'h':h,'B':B,'states':m,'F':str(F),
            'mean_loss':str(loss),'sum_expected_corrected_buffer_times_loss':str(W),
            'expected_square_rate':str(V),
            'stationary_weights':[{'g0':list(s[0]),'g1':list(s[1]),
                                   'b0':s[2],'p':str(x)} for s,x in zip(states,p)]}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output',default=str(HERE/'results'/'verified.json'))
    parser.add_argument('--certificates',default=str(HERE/'results'/'certificates.json'))
    parser.add_argument('--buffer-certificate',
                        default=str(HERE/'results'/'buffer_certificate.json'))
    args = parser.parse_args()
    cases = [(2,2,Q(0)),(2,2,Q(1,2)),(2,2,Q(1)),
             (2,3,Q(0)),(2,3,Q(1,2)),
             (4,3,Q(0)),(4,3,Q(1,2)),(4,3,Q(9,10))]
    certificates = [correlation_certificate(n,h,c) for n,h,c in cases]
    get = lambda n,h,c: Q(next(x['q'] for x in certificates
                              if (x['n'],x['h'],x['c']) == (n,h,str(c))))
    assert get(2,2,Q(0)) > get(2,2,Q(1,2)) > get(2,2,Q(1))
    assert get(2,3,Q(0)) < get(2,3,Q(1,2))
    assert get(4,3,Q(1,2)) < get(4,3,Q(0)) < get(4,3,Q(9,10))
    buffer_certificate = stationary_buffer_certificate(2,3,1)
    summary = {'status':'PASS; exact finite audits only; thermodynamic limit unresolved',
               'stationary_chains':len(certificates),
               'full_stationary_balance_equations':sum(x['full_states'] for x in certificates),
               'quotient_stationary_balance_equations':sum(x['rotation_classes'] for x in certificates),
               'symbolic_vector_parameter_checks':audit_symbolic_vector(),
               'cover':audit_cover(),'buffers':audit_buffers(),
               'buffer_weighted_loss_counterexample':{
                   k:v for k,v in buffer_certificate.items() if k != 'stationary_weights'},
               'counterexamples':[{k:v for k,v in x.items() if k != 'class_weights'}
                                  for x in certificates]}
    Path(args.certificates).parent.mkdir(parents=True,exist_ok=True)
    Path(args.certificates).write_text(json.dumps(certificates,indent=2)+'\n')
    Path(args.buffer_certificate).parent.mkdir(parents=True,exist_ok=True)
    Path(args.buffer_certificate).write_text(json.dumps(buffer_certificate,indent=2)+'\n')
    Path(args.output).parent.mkdir(parents=True,exist_ok=True)
    Path(args.output).write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))


if __name__ == '__main__':
    main()
