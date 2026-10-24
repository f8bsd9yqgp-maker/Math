#!/usr/bin/env python3
"""Exact audits; Python standard library only. Not a thermodynamic proof."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path
import json
import sys

if not __debug__:
    raise RuntimeError("Run without -O")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "code"))
from exact_support import compositions, ring_move, stationary


def B(a, b):
    assert a <= b
    return min(b, max(a+1, b-1))


def S(a, b):
    return max(a, b) + int(a == b)


def heights_to_gaps(h, total):
    return tuple(h[i+1]-h[i] if i+1 < len(h) else h[0]+total-h[i]
                 for i in range(len(h)))


def apply_height(h, total, i):
    h = list(h)
    b = h[i+1] if i+1 < len(h) else h[0]+total
    h[i] = B(h[i], b)
    return tuple(h)


def balanced(n, total):
    return tuple(i*total//n for i in range(n))


def trajectory(n, total, word):
    h = balanced(n, total)
    retains = []
    for i in word:
        if i >= n:
            retains.append(None)
            continue
        g = heights_to_gaps(h, total)
        retains.append(int(g[i] >= 2))
        h = apply_height(h, total, i)
    count = penalty = 0
    for i, r in reversed(tuple(zip(word, retains))):
        if i == count % n:
            assert r is not None
            count += 1
            penalty += r
    assert h[0] == total*count//n - penalty
    assert 0 <= h[0] <= total*count//n
    return h, count


def main():
    out = {"status": "all assertions passed", "exact_arithmetic": True,
           "thermodynamic_limit_proved": False}
    local = 0
    for a in range(-10, 11):
        for b in range(a, a+31):
            assert B(a,b) == b-int(b-a >= 2)
            assert B(a,b) == S(a,b-1)
            assert S(a,b) == max(a,b,min(a,b)+1)
            # Exact power-of-two floor-log identity, avoiding floating point.
            lower = min(a,b)
            integer_sum = (1 << (a-lower))+(1 << (b-lower))
            assert S(a,b) == lower+integer_sum.bit_length()-1
            local += 1
    out["local_identities"] = local

    states = edges = 0
    for n in range(2,7):
        for total in range(9):
            for g in compositions(total,n):
                h = [0]
                for z in g[:-1]:
                    h.append(h[-1]+z)
                for i in range(n):
                    updated = apply_height(tuple(h),total,i)
                    assert heights_to_gaps(updated,total) == ring_move(g,i)
                    x = [h[j]-j for j in range(n)]
                    right = x[i+1] if i+1<n else x[0]+total-n
                    assert updated[i]-i == S(x[i],right)
                    edges += 1
                states += 1
    out["ring_generator_states"] = states
    out["ring_generator_edges"] = edges

    words = spine_states = 0
    for n in range(2,6):
        for length in range(7):
            counts = Counter()
            for word in product(range(n), repeat=length):
                count = 0
                for i in reversed(word):
                    if i == count % n:
                        count += 1
                counts[count] += 1
                for total in sorted({0,n-1,n,3*n//2,2*n+1}):
                    _, count2 = trajectory(n,total,word)
                    assert count2 == count
                    spine_states += 1
                words += 1
            for z in range(length+1):
                assert counts[z] == comb(length,z)*(n-1)**(length-z)
    out["spine_clock_words"] = words
    out["spine_initial_state_word_pairs"] = spine_states

    coupled = 0
    for n,m in [(2,3),(3,4),(3,5)]:
        for length in range(7):
            for word in product(range(m),repeat=length):
                for total_n,total_m in [(n,m),(n-1,m-1),(n,2*m-1)]:
                    hn,zn = trajectory(n,total_n,word)
                    hm,zm = trajectory(m,total_m,word)
                    assert (zn >= n) == (zm >= n)
                    if zn < n:
                        assert zn == zm
                        if F(total_n,n) == F(total_m,m):
                            assert hn[0] == hm[0]
                        else:
                            delta = abs(F(total_n,n)-F(total_m,m))
                            assert abs(hn[0]-hm[0]) <= delta*zn+1
                    coupled += 1
    out["coupled_ring_word_cases"] = coupled

    brackets = []
    for n,total in [(2,1),(2,2),(2,3),(3,2),(3,3),(3,5),
                    (4,2),(4,4),(5,3)]:
        ss,pp = stationary(n,total)
        q = sum(p*sum(x>=2 for x in g)/n for g,p in zip(ss,pp))
        flux = F(total,n)-q
        initial = balanced(n,total)
        for length in range(1,7):
            low = high = 0
            for word in product(range(n),repeat=length):
                h,_ = trajectory(n,total,word)
                increments = [a-b for a,b in zip(h,initial)]
                low += min(increments)
                high += max(increments)
            lower = F(low,n**length)
            upper = F(high,n**length)
            target = F(length,n)*flux
            assert lower <= target <= upper
            brackets.append({"N":n,"H":total,"events":length,
                             "lower":str(lower),"target":str(target),
                             "upper":str(upper),"F":str(flux)})
    out["exact_current_brackets"] = len(brackets)

    envelopes = 0
    max_defect = 0
    for n in list(range(1,25))+[31,63,101]:
        ks = range(n) if n<=24 else [(n-1)//2]
        for k in ks:
            size=2*n+2
            a=tuple(-max(0,n-k-abs(i-n)) for i in range(size))
            b=tuple(-max(0,k+1-min(i,size-i)) for i in range(size))
            assert all(max(x,y)==0 for x,y in zip(a,b))
            histories = []
            word=tuple(i for level in range(n) for i in range(n-level))
            for profile in [a,b,(0,)*size]:
                h=tuple(i+profile[i] for i in range(size))
                g=heights_to_gaps(h,size)
                assert sum(g)==size and min(g)>=0 and max(g)<=2
                for i in word:
                    h=apply_height(h,size,i)
                    g2=ring_move(g,i)
                    assert heights_to_gaps(h,size)==g2
                    g=g2
                histories.append(h[0])
            assert histories == [k,n-k-1,n]
            defect=n-max(k,n-k-1)
            assert defect==min(k+1,n-k)
            max_defect=max(max_defect,defect)
            envelopes += 1
    out["max_envelope_counterexamples"] = envelopes
    out["largest_verified_envelope_defect"] = max_defect

    (HERE/"results").mkdir(exist_ok=True)
    (HERE/"results"/"verification.json").write_text(json.dumps(out,indent=2)+"\n")
    (HERE/"results"/"current_brackets.json").write_text(json.dumps(brackets,indent=2)+"\n")
    print(json.dumps(out,indent=2))


if __name__ == "__main__":
    main()
