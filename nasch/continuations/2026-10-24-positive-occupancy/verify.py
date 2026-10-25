#!/usr/bin/env python3
"""Exact audits of NEW weighted empty-block / exponential-height bounds.

Standard library only. No simulations or reruns of the previous verifiers.
Finite checks supplement, and do not replace, the analytic proof in README.md.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import platform
import random
import time

HERE = Path(__file__).resolve().parent


def compositions(h, n):
    if n == 1:
        yield (h,)
    else:
        for a in range(h + 1):
            for rest in compositions(h-a, n-1):
                yield (a,) + rest


def move(g, i):
    out = list(g)
    sent = g[i] - int(g[i] >= 2)
    out[i] -= sent
    out[(i-1) % len(g)] += sent
    return tuple(out), sent


def empty(g, i, k):
    return int(all(g[(i+j) % len(g)] == 0 for j in range(k)))


def potential(g, ell):
    n = len(g)
    return [F(4, ell*(ell+1))*sum((ell-k)*empty(g, i, k)
                                  for k in range(1, ell))
            for i in range(n)]


def local_empty_audit():
    count = 0
    # A spare site keeps the incoming boundary distinct from the block.
    for k in range(1, 7):
        n = k+2
        for local in product(range(3), repeat=k+1):
            g = local + (0,)
            drift = sum(empty(move(g, i)[0], 0, k)-empty(g, 0, k)
                        for i in range(n))
            expected = (int(g[0] == 1)*empty(g, 1, k-1)
                        - empty(g, 0, k)*int(g[k] > 0))
            assert drift == expected
            count += 1
    return count


def weighted_audit(g, ell, u):
    n, h = len(g), sum(g)
    heights = [0]
    for a in g[:-1]:
        heights.append(heights[-1]+a)
    # lambda = n*log(u), theta = h/n. All weights are rational.
    v = [u**(n*heights[i]-h*i) for i in range(n)]
    z, delta = u**n, 1-u**(-h)
    beta = z+1/z-2
    a, b = F(ell-3, ell+1), F(4, ell*(ell+1))
    cap = F(2*(ell-1), ell+1)
    shift_cap = F(2*(ell-1)*(ell-2), ell*(ell+1))
    phi = potential(g, ell)
    assert all(0 <= x <= cap for x in phi)
    V, G = sum(v), sum(x*y for x, y in zip(v, g))
    P = sum(v[i] for i in range(n) if g[i] == 1)
    W0 = sum(v[i] for i in range(n) if g[i] == 0)
    Phi = sum(x*y for x, y in zip(v, phi))
    LV = LPhi = frozen = cross = F(0)
    for i in range(n):
        nxt, sent = move(g, i)
        pnext = potential(nxt, ell)
        dv = v[i]*(z**sent-1)
        LV += dv
        frozen += sum(v[j]*(pnext[j]-phi[j]) for j in range(n))
        cross += dv*pnext[i]
        LPhi += sum(v[j]*pnext[j] for j in range(n))+dv*pnext[i]-Phi
    assert LPhi == frozen+cross and cross >= 0
    assert LV == (u**(h-n)-1)*V+(1-1/z)*W0+(z-1)*P
    assert LV <= (u**(h-n)-1/z)*V+beta*P
    assert sum(v[i]*z**g[i] for i in range(n)) == u**h*V
    variation = sum(max(F(0), v[i]-v[(i-1) % n]) for i in range(n))
    assert variation <= delta*V
    # This is the essential NEW weighted certificate before any log bound.
    assert P <= a*G+(b+shift_cap*delta)*V+frozen
    assert P <= a*G+(b+shift_cap*delta)*V+LPhi
    Y, LY = V-beta*Phi, LV-beta*LPhi
    assert LY <= (u**(h-n)-1/z+beta*(b+shift_cap*delta))*V+beta*a*G
    assert (1-cap*beta)*V <= Y <= V
    if h:
        x = u-1
        log_lower = n*(x-x*x/2)
        assert log_lower > 0
        assert log_lower*G <= (u**h-1)*V
        C = (u**(h-n)-1/z
             +beta*(a*(u**h-1)/log_lower+b+shift_cap*delta))
        assert LY <= C*V
        if cap*beta < 1:
            assert LY <= C*Y/(1-cap*beta)
    return 1


def exp_interval(x, terms=24):
    """Rigorous rational enclosure, used only for 0 <= x <= 1/10."""
    if x < 0:
        lo, hi = exp_interval(-x, terms)
        return 1/hi, 1/lo
    assert x <= F(1, 10)
    term = total = F(1)
    for k in range(1, terms+1):
        term *= x/k
        total += term
    nxt = term*x/(terms+1)
    return total, total+nxt/(1-x/(terms+2))


def rate_certificate(theta):
    ell = max(3, -(-2*theta.denominator // theta.numerator))
    lam = theta/96
    a, b = F(ell-3, ell+1), F(4, ell*(ell+1))
    cap = F(2*(ell-1), ell+1)
    K = F(2*(ell-1)*(ell-2), ell*(ell+1))
    ep = exp_interval(lam)
    em = exp_interval(-lam)
    et = exp_interval(lam*theta)
    ent = exp_interval(-lam*theta)
    eat = exp_interval(lam*(theta-1))
    beta_upper = ep[1]+em[1]-2
    B_upper = a*(et[1]-1)/lam+b+K*(1-ent[0])
    C_upper = eat[1]-em[0]+beta_upper*B_upper
    upper_speed = C_upper/(lam*(1-cap*beta_upper))
    lower_q = theta-upper_speed
    assert lower_q >= theta**3/1152
    return {'theta': str(theta), 'ell': ell, 'lambda': str(lam),
            'certified_q_lower_rational': str(lower_q),
            'certified_q_lower_display': float(lower_q),
            'simple_lower': str(theta**3/1152)}


def density_one_certificate():
    z = F(21, 20)
    beta = z+1/z-2
    B = F(1, 3)+F(1, 3)*(1-1/z)
    ratio = (1-1/z+beta*B)/(1-beta)
    x = z-1
    log_lower = x-x*x/2+x**3/3-x**4/4
    lower = 1-ratio/log_lower
    assert beta == F(1, 420) and B == F(22, 63)
    assert ratio == F(1282, 26397)
    assert log_lower == F(93677, 1920000)
    assert lower == F(3783923, 824263923) and lower > F(1, 218)
    return {'q_at_density_one_lower': str(lower),
            'q_at_density_one_lower_display': float(lower),
            'simple_lower': '1/218',
            'explicit_uniform_integrability_interval': '0 < eta <= 1/217'}


def main():
    started = time.monotonic()
    local_count = local_empty_audit()
    weighted_count = 0
    for n in range(3, 7):
        for h in range(0, 6):
            for g in compositions(h, n):
                for ell in range(3, n+1):
                    weighted_count += weighted_audit(g, ell, F(101, 100))
    rng = random.Random(2026102416)
    for _ in range(60):
        n = rng.randrange(3, 10)
        g = tuple(rng.randrange(0, 25) for _ in range(n))
        ell = rng.randrange(3, n+1)
        weighted_count += weighted_audit(g, ell, F(1001, 1000))
    alpha_count = 0
    for n in range(3, 201):
        for h in range(2, n+1):
            theta = F(h, n)
            ell = max(3, -(-2*n//h))
            assert ell <= n
            c = F(ell-3, ell+1)*theta+F(4, ell*(ell+1))
            alpha = theta*(theta-2)/2+c
            assert 0 <= c <= theta
            assert alpha <= -theta**2/6
            alpha_count += 1
    rates = [rate_certificate(t) for t in
             [F(1,100), F(1,20), F(1,10), F(1,4), F(1,2),
              F(2,3), F(3,4), F(1)]]
    result = {'status': 'all passed', 'local_empty_block_checks': local_count,
              'weighted_generator_certificates': weighted_count,
              'exact_alpha_checks': alpha_count, 'rigorous_rate_enclosures': rates,
              'seed_for_finite_test_states_only': 2026102416,
              'seconds': time.monotonic()-started,
              'scope': 'Finite exact audits, not a proof by extrapolation.'}
    result['density_one_and_critical_density_certificate'] = density_one_certificate()
    (HERE/'results').mkdir(exist_ok=True)
    (HERE/'results/verified.json').write_text(json.dumps(result, indent=2)+'\n')
    (HERE/'results/environment.json').write_text(json.dumps(
        {'python': platform.python_version(), 'dependencies': 'standard library only'},
        indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items()
                      if k != 'rigorous_rate_enclosures'}, indent=2))
    print('Rigorous q lower bounds:', [(x['theta'], x['certified_q_lower_display'])
                                     for x in rates])


if __name__ == '__main__':
    main()
