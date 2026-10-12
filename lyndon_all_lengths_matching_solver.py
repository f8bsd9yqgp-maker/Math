#!/usr/bin/env python3
"""Exact shortest superstring for all length-n binary Lyndon words.

Mathematical principle: positive proper suffix-prefix overlap u -> v between
Lyndon words implies u < v. Therefore the positive-overlap graph is acyclic.
A maximum-weight bipartite matching gives disjoint directed paths, which can
be concatenated into an optimal superstring.

Uses NumPy and SciPy for maximum-weight matching; there is NO extrapolation
from earlier n. For n>=18, the explicit q-by-q matrix can use considerable RAM.

Usage: python lyndon_all_lengths_matching_solver.py 12
       python lyndon_all_lengths_matching_solver.py 17 --witness /mnt/data/lyndon17_new_witness.txt
"""
from argparse import ArgumentParser
from time import perf_counter
import numpy as np
from scipy.optimize import linear_sum_assignment


def lyndon_words(n):
    mask=(1<<n)-1
    return [w for w in range(1<<n)
            if all(w < (((w << k)|(w>>(n-k)))&mask) for k in range(1,n))]


def solve(n, witness_file=None):
    assert 1 <= n <= 17, 'For n>17 prefer path-compressed matching (less RAM)'
    t0=perf_counter()
    ints=lyndon_words(n)
    q=len(ints)
    W=np.asarray(ints,dtype=np.int64)
    O=np.zeros((q,q),dtype=np.int16)
    # Largest proper overlap. Notice that every selected positive arc points
    # lexicographically forward; this can be verified using the next assert.
    for k in range(1,n):
        O[(W[:,None]&((1<<k)-1))==(W[None,:]>>(n-k))]=k
    I,J=np.where(O>0)
    assert np.all(W[I]<W[J]), 'Lyndon overlap-order lemma violated'
    rows,cols=linear_sum_assignment(O,maximize=True)
    weight=int(O[rows,cols].sum())
    succ={int(i):int(j) for i,j in zip(rows,cols) if O[i,j]>0}
    targets=set(succ.values())
    heads=[i for i in range(q) if i not in targets]
    seen=set()
    path_strings=[]
    for head in heads:
        i=head
        s=format(ints[i],f'0{n}b')
        while True:
            assert i not in seen
            seen.add(i)
            if i not in succ:break
            j=succ[i]
            k=int(O[i,j])
            s+=format(ints[j],f'0{n}b')[k:]
            i=j
        path_strings.append(s)
    assert len(seen)==q
    result=''.join(path_strings)
    optimum=n*q-weight
    assert len(result)==optimum
    # Explicit, separate factor-coverage check.
    have={int(result[i:i+n],2) for i in range(len(result)-n+1)}
    assert set(ints)<=have
    print('length n:',n)
    print('required Lyndon words:',q)
    print('maximum total overlap:',weight)
    print('selected positive-overlap paths:',len(heads))
    print('THEOREM: shortest length =',optimum)
    print('Witness contains all required Lyndon words: YES')
    print('elapsed:',round(perf_counter()-t0,3),'seconds')
    if witness_file:
        with open(witness_file,'w') as f:f.write(result+'\n')
        print('witness:',witness_file)
    return optimum


if __name__=='__main__':
    p=ArgumentParser()
    p.add_argument('n',type=int)
    p.add_argument('--witness')
    args=p.parse_args()
    solve(args.n,args.witness)