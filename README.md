# The shortest superstring of the binary Lyndon words of length eight

Also in this repository: [NaSch/backchip canonical pile-probability
convergence and structural proofs](nasch/README.md) (updated 24 October 2026).
The fixed-density pile probability has a convergence proof with rate
O((log(N)/N)^(1/4)), a uniform positive lower bound, and a critical-density
mass-retention theorem. These are AI-assisted, internally audited results,
not independently peer-reviewed. The unrestricted NaSch flow formula remains open.

**Theorem.** The minimum length of a binary word containing each binary Lyndon word of length eight as a contiguous substring is **94**.

*Research note — 12 October 2026. This is a self-contained, AI-assisted proof with a reproducible finite certificate. Independent specialist review and publication-priority verification are pending. Its presence on GitHub does not imply formal peer review or institutional endorsement.*

## Statement and definitions

A binary **Lyndon word** of length eight is an eight-bit word that is lexicographically strictly smaller than each of its seven nontrivial cyclic rotations. Let `W` be the set of all such words. Direct enumeration gives `|W| = 30`.

We prove that any binary string containing every element of `W` has length at least 94, and exhibit one attaining 94.

## Proof

### 1. Model length-eight factors as directed edges

Consider the binary de Bruijn digraph of order seven. Its 128 vertices are the seven-bit strings; its 256 directed edges are the eight-bit strings. An edge `b1...b8` goes from `b1...b7` to `b2...b8`.

Equivalently, identify seven-bit strings with integers `0,...,127`. The outgoing neighbors of `v` are `2v mod 128` and `(2v+1) mod 128`.

A string of length `L` generates a directed walk of `m = L - 7` edges, one for each consecutive eight-bit factor.

### 2. Construct a one-sided Lipschitz potential

Let `d(a,b)` be the shortest directed-path length from vertex `a` to vertex `b`. Since the graph has order seven, `0 <= d(a,b) <= 7`. It can be computed by the explicit overlap formula

```
d(a,b) = min { k in {0,...,7} :
               suffix_(7-k)(a) = prefix_(7-k)(b) }.
```

Set

```
Z = {37,39,53,59,61,87,91,95,111,127}

p(v) = min( 7, 3 + d(25,v), min_{z in Z} d(z,v) ).
```

Every potential value belongs to `{0,...,7}`.

**Lemma.** For every directed edge `u -> v`, we have `p(v) - p(u) <= 1`.

**Proof of lemma.** Appending `u -> v` to a shortest directed path from any source `a` to `u` gives `d(a,v) <= d(a,u) + 1`. This holds for every distance function in the minimum defining `p`; it also holds for the constant function 7. Taking their pointwise minimum preserves the inequality. QED.

### 3. The 30 mandatory edges have potential drop 64

For vertex `v`, let `Delta(v)` be its outgoing-minus-incoming degree in the directed edge collection `W`. Enumerating the 30 Lyndon edges gives the complete list of nonzero values:

| Vertices | Delta | p |
| --- | ---: | ---: |
| 0, 2, 4, 6, 10, 12, 14, 18, 26 | +1 each | 7 |
| 22, 30 | +1 each | 2 |
| 25 | -1 | 3 |
| 37, 39, 53, 59, 61, 87, 91, 95, 111, 127 | -1 each | 0 |

All other vertices have `Delta(v) = 0`. The table follows from finite enumeration and the explicit definition of `p` (and is independently checked by the accompanying Python verifier).

The total decrease in potential across the 30 required edges is therefore

```
D = sum_(w in W) [p(tail(w)) - p(head(w))]
  = sum_(v=0)^127 Delta(v) p(v)
  = 9*7 + 2*2 - 3 - 10*0
  = 64.
```

### 4. Lower bound for every possible superstring

Let `S` contain every word in `W`, and let `m = |S| - 7` be the number of length-eight factors. Select one occurrence of each of the 30 distinct required factors. Those selected edges contribute total potential change `-64`, irrespective of their order.

There are `m-30` remaining edges. By the lemma, each adds **at most** `+1` to the potential. Consequently,

```
p(end) - p(start) <= -64 + (m - 30).
```

Since `0 <= p <= 7`, the change on the left is at least `-7`. Thus

```
-7 <= -64 + (m - 30)
m >= 87
|S| = m + 7 >= 94.
```

This is a **global** lower bound: it does not assume any fixed ordering or merging of blocks.

### 5. Matching upper-bound witness

The following previously recorded string has length exactly 94:

```text
0000000111111100000101111100001001111010000110111100010101110001100100101101100011101100110101
```

It contains all 30 eight-bit binary Lyndon words as contiguous factors. The verifier regenerates the target set and checks each occurrence.

Therefore the minimum possible length is both at least 94 and at most 94:

**QED: the exact minimum is 94.**

## Reproduce the certificate

Run `python3 lyndon8_independent_check.py`. The program uses only the Python standard library. It independently builds all graph distances by breadth-first search, tests all 256 potential inequalities, regenerates the 30 Lyndon words, verifies the imbalance table and the potential drop 64, and checks all occurrences in the 94-bit witness.

A useful extra check: in the witness all 57 edges beyond the selected 30 required ones increase the potential by exactly 1, and the walk goes from potential 7 to potential 0. Both lower-bound inequalities are therefore tight.

## Source and scholarly status

- [TheoremDB P2600 — Shortest superstring of the binary Lyndon words of length eight](https://theoremdb.org/statements/P2600/) recorded bounds of 49–94 and the 94-character witness. On 12 October 2026 the entry was marked *Solution submitted*, but the displayed submitted result covered only the 49–94 interval. The site did not provide an externally reviewed proof of the equality 94 in the record inspected.
- The upper-bound witness is credited to the existing TheoremDB work, **not** claimed as new here.
- This note's claimed contribution is the matching general lower-bound certificate. It was developed with ChatGPT/OpenAI assistance. The result should be independently checked before claims about priority, acceptance by the mathematical community, or publication.
- The algorithmic field is *combinatorics on words*, with an equivalent proof in graph theory using a de Bruijn digraph.


## Companion result: length nine

**Theorem (computationally checkable).** The minimum length of a binary superstring containing all 56 binary Lyndon words of length nine is **185**.

- [Full length-nine proof](lyndon9_exact_185_proof.md)
- [Independent length-nine verifier (Python standard library)](lyndon9_verify.py)

This is an AI-assisted research note with an explicit 185-bit construction and a matching global potential-function lower bound. The proof certificate passes exhaustive finite checks; independent specialist review and priority verification are still pending.


## Companion result: length ten

**Theorem (computationally checkable).** The shortest binary superstring containing all 99 binary Lyndon words of length ten has length **359**.

- [Full length-ten proof](lyndon10_exact_359_proof.md)
- [Independent length-ten Python verifier](lyndon10_verify.py)
- [Explicit 359-bit witness](lyndon10_witness.txt)

The proof provides a graph-potential lower bound of 359 and an explicit matching construction. This is AI-assisted research, with exhaustive computational checking but without independent specialist peer review or confirmed publication priority.

## Companion result: length eleven

**Theorem (computationally checkable).** The shortest binary superstring containing all **186** binary Lyndon words of length eleven has length **715**.

- [Complete length-eleven mathematical proof](lyndon11_exact_715_proof.md)
- [Independent length-eleven verification script](lyndon11_verify.py)
- [Explicit 715-bit witness](lyndon11_witness.txt)

The certificate supplies a matching general lower bound and an explicit construction. Run `python3 lyndon11_verify.py` to verify all 2,048 graph-edge potential inequalities and all 186 required substrings. This is AI-assisted research with computational verification, not independent specialist peer review; publication priority is still unconfirmed.

## Companion result: length twelve

**Theorem (computationally checkable).** The shortest binary superstring containing all **335** binary Lyndon words of length twelve has length **1,415**.

- [Complete length-twelve proof](lyndon12_exact_1415_proof.md)
- [Independent length-twelve Python verifier](lyndon12_verify.py)
- [Explicit 1,415-bit witness](lyndon12_witness.txt)

The argument gives a matching global graph-potential lower bound and an explicit construction. Run `python3 lyndon12_verify.py` to check all 4,096 graph transitions and every required word without external packages. This is AI-assisted research with computational validation, but not independent specialist peer review; scholarly priority remains unconfirmed.

## Companion result: length thirteen

**Theorem (computationally checkable).** The shortest binary superstring containing all **630** binary Lyndon words of length thirteen has length **2,804**.

- [Complete length-thirteen mathematical proof](lyndon13_exact_2804_proof.md)
- [Independent length-thirteen verifier (Python standard library)](lyndon13_verify.py)
- [Explicit 2,804-bit witness](lyndon13_witness.txt)

The graph-potential certificate proves a global lower bound of 2,804, and the witness attains it. Run `python3 lyndon13_verify.py` to regenerate the potential, verify all 8,192 edge inequalities and 630 required words, and confirm the construction. The research is AI-assisted. The finite checks are reproducible; independent specialist review and publication-priority verification are still pending.

## Companion result: length fourteen

**Theorem (finite, independently checkable certificate).** The minimum binary superstring containing all **1,161** binary Lyndon words of length fourteen has length **5,564**.

- [Complete length-fourteen mathematical proof](lyndon14_exact_5564_proof.md)
- [Solver-free Python verifier](lyndon14_verify.py)
- [Weighted-seed potential certificate (358 entries)](lyndon14_seeds.txt)
- [Explicit 5,564-bit witness](lyndon14_witness.txt)
- [Independent NumPy/SciPy assignment cross-check (optional)](lyndon14_assignment_crosscheck.py)

Download the five files into the same folder and run `python3 lyndon14_verify.py` to regenerate the 1,161 required words, reconstruct the potential, test all **16,384** directed-edge inequalities, and check the exact 5,564-bit witness. The pure-Python verifier does not require an optimizer or third-party libraries. The auxiliary assignment cross-check needs NumPy and SciPy.

This is **AI-assisted mathematical research**, reproducible through finite certificate checks. Independent specialist peer review and publication-priority verification remain outstanding.

## Companion result: length fifteen

**Theorem (computationally checkable).** The shortest binary superstring containing all **2,182** binary Lyndon words of length fifteen has length **11,037**.

- [Complete length-fifteen proof](lyndon15_exact_11037_proof.md)
- [Independent standard-library Python verifier](lyndon15_verify.py)
- [657-entry weighted-seed potential certificate](lyndon15_seeds.txt)
- [Explicit 11,037-bit witness](lyndon15_witness.txt)

Download these four files together and run `python3 lyndon15_verify.py`. The verifier regenerates the 2,182 Lyndon words by two independent methods, reconstructs the lower-bound potential, checks all 32,768 graph inequalities, and verifies the matching witness. The uploaded seed and witness SHA-256 hashes were checked against the verifier's declared values. This is AI-assisted, computationally certified research; independent specialist review and originality verification are still pending.

## General exact matching theorem (proof candidate, October 2026)

**Claim, with a complete proof candidate supplied:** Let `W` be any finite set of *distinct Lyndon words of the same length* `n` over a totally ordered alphabet. Let `H(W)` be the maximum sum of proper suffix-prefix overlaps across a bipartite matching on the words. Then

`ShortestSuperstring(W) = n * |W| - H(W)`.

The crucial observation is that **every positive suffix-prefix overlap `u -> v` between two distinct same-length Lyndon words implies `u < v` in lexicographic order**. Consequently positive-overlap arcs are acyclic; selecting a maximum-weight matching gives disjoint paths whose concatenation attains the universal matching lower bound.

For the special case of *all binary Lyndon words of length n*, this also yields `L_n = (n-1) + q_n + M_n`, resolving the cycle-connectivity obstruction identified in the earlier general-framework notes. Here `M_n` is the minimum de Bruijn path-endpoint connector matching cost.

- [Complete all-length exact matching theorem and proof candidate](lyndon_all_lengths_exact_matching_theorem_2026-10-12.md)
- [Independent maximum-overlap solver and witness generator (NumPy/SciPy)](lyndon_all_lengths_matching_solver.py)
- [Earlier general framework and conjecture — historical note, **superseded**](lyndon_general_theorem_and_conjecture.md)
- [Earlier graph matching implementation](lyndon_general_framework.py)

Run `python3 lyndon_all_lengths_matching_solver.py 12` to reproduce the length-12 result; the current full-overlap-matrix implementation is limited to `n <= 17` because of memory requirements, **not** because the theorem is restricted to those lengths. Earlier single-length proof certificates remain available separately.

**Research status:** This work is AI-assisted. The proof candidate is public and testable; it has *not* been independently peer-reviewed, accepted, or established as previously unpublished. The former wording that the all-length connected-matching claim was still an open conjecture is superseded by this proof candidate; expert review of the new argument is still pending.

### Companion result: length sixteen (21,902 bits)

An exact finite certificate checks a matching cost of 17,807 for the 4,080 length-16 Lyndon words, with a 21,902-bit matching witness.

- [One-command solver-free verification](lyndon16_run_all.py)
- [Independent assignment-dual and witness verifier](lyndon16_verify.py)
- [Restore the SHA-256-checked assignment dual data](lyndon16_restore_dual.py)
- [Restore the SHA-256-checked witness](lyndon16_restore_witness.py)

Download the four length-16 Python files into the same folder and run `python3 lyndon16_run_all.py`. Both compressed data files are restored locally and checked against their SHA-256 hashes before the verifier checks all 2,979,076 dual inequalities and containment of all 4,080 required words.

These are **AI-assisted mathematical research notes**, not externally peer-reviewed publications. The all-length connected-matching conjecture now has a proposed proof in the matching theorem linked above; independent review, originality, and priority checks remain outstanding.

