# The shortest superstring of all binary Lyndon words of length twelve

**Research note · 12 October 2026**  
**Status:** finite computational proof certificate reproduced with independent standard-library Python; mathematical priority and external peer review not established. AI-assisted investigation and proof development.

## Theorem

The minimum length of a binary string containing all binary Lyndon words of length 12 as contiguous substrings is

\[
\boxed{L_{12}=1415}.
\]

There are 335 required Lyndon words. A **Lyndon word** here is a string lexicographically strictly smaller than every one of its 11 nontrivial rotations. The number of length-twelve binary Lyndon words is
\[
\frac{2^{12}-2^6-2^4+2^2}{12}=\frac{4020}{12}=335.
\]

## 1. Directed overlap graph

Let \(G\) be the binary de Bruijn graph of order 11. Its vertex set is \(\{0,\dots,2047\}\), representing 11-bit binary strings, with two edges leaving each vertex:

\[
u\longrightarrow ((2u+b)\bmod2048), \quad b\in\{0,1\}.
\]

The 4096 edges correspond bijectively to 12-bit strings: the edge spells the 11-bit tail plus one appended bit. A superstring \(S\) of length \(L\) spells a walk of \(L-11\) edges. Each required Lyndon word labels a distinct compulsory edge, so 335 distinct edges must occur in the walk.

## 2. A compact dual potential

Write \(d(a,v)\) for the shortest directed-path distance from vertex \(a\) to vertex \(v\) in \(G\). Directed de Bruijn distances never exceed 11; they can also be computed from the longest suffix–prefix overlap between the two 11-bit strings.

Let the **zero-source set** be

```
Z = {
  357, 405, 407, 421, 425, 441, 461, 467, 473, 485, 487, 489, 499, 505,
  613, 661, 663, 667, 669, 671, 679, 691, 717, 719, 723, 725, 743, 747,
  755, 757, 847, 853, 855, 859, 861, 863, 871, 875, 877, 885, 893, 925,
  927, 939, 941, 943, 949, 951, 955, 957, 981, 983, 987, 989, 1003, 1005,
  1007, 1013, 1015, 1019, 1021, 1367, 1371, 1375, 1387, 1391, 1399,
  1403, 1407, 1455, 1463, 1467, 1471, 1499, 1503, 1519, 1527, 1531,
  1535, 1759, 1775, 1783, 1791, 1919, 1983, 2047
}
```

and let the **weighted-source list** \(T\) consist of pairs \((a,c)\):

```
T = {
  (823,1), (459,1), (97,5), (133,7), (135,7), (403,4),
  (409,3), (291,5), (827,1), (831,1), (197,6), (329,3),
  (457,3), (209,4), (227,5), (355,5), (619,3), (241,4)
}
```

Define for every vertex \(v\)

\[
p(v)=\min\Big\{11,\ \min_{z\in Z}d(z,v),\ \min_{(a,c)\in T}\bigl(c+d(a,v)\bigr)\Big\}.
\]

**Lemma 1.** The potential satisfies \(0\le p(v)\le11\) and, for every directed edge \(u\to v\),

\[
p(v)-p(u)\le1.
\]

**Proof.** For each source \(a\), appending \(u\to v\) to a shortest directed path from \(a\) to \(u\) shows \(d(a,v)\le d(a,u)+1\). Each term of the displayed minimum is one-sided 1-Lipschitz along every directed edge; their minimum retains that property. The constant 11 also satisfies the property. Nonnegativity and the upper bound are immediate. \(\square\)

**Lemma 2 (finite enumeration).** Let \(W\) be the 335 mandatory 12-bit Lyndon edges, and let \(\Delta(v)\) denote required outdegree minus required indegree. Then

\[
D:=\sum_{w\in W}\bigl[p(\operatorname{tail}(w))-p(\operatorname{head}(w))\bigr]
=\sum_{v=0}^{2047}\Delta(v)p(v)=1080.
\]

This is a finite calculation. The imbalance of every vertex is -1, 0 or +1; there are 134 vertices of each nonzero sign. The complete numerical summary is:

| \(p(v)\) | \(\Delta=+1\) vertices | \(\Delta=-1\) vertices | Contribution \(p\times(\# + - \# -)\) |
|---:|---:|---:|---:|
| 0 | 0 | 86 | 0 |
| 1 | 0 | 4 | -4 |
| 2 | 0 | 12 | -24 |
| 3 | 0 | 5 | -15 |
| 4 | 15 | 6 | 36 |
| 5 | 4 | 5 | -5 |
| 6 | 6 | 5 | 6 |
| 7 | 2 | 4 | -14 |
| 8 | 7 | 7 | 0 |
| 9 | 0 | 0 | 0 |
| 10 | 0 | 0 | 0 |
| 11 | 100 | 0 | 1100 |
| **Total** | **134** | **134** | **1080** |

The accompanying `lyndon12_verify.py` regenerates the set \(W\) from the definition, computes \(p\) from the source lists using a separate shortest-path algorithm, checks every one of the 4096 inequalities, and independently computes the two expressions for \(D\). No optimizer is required to check the proof.

## 3. Universal lower bound

Take any binary string \(S\) containing every member of \(W\) and write \(L=|S|\). It has \(L-11\) length-12 substrings, thus a walk of that many directed edges. Pick one occurrence of each of the 335 mandatory Lyndon edges. The total potential change on those selected edges is exactly \(-D=-1080\), regardless of their order. The remaining \(L-11-335\) edges each increase the potential by at most 1, by Lemma 1. Consequently

\[
p(\operatorname{end})-p(\operatorname{start})\le-1080+(L-11-335).
\]

But the potential lies between 0 and 11, so the left side is at least \(-11\). Therefore

\[
-11\le -1080+L-346=L-1426,
\qquad\boxed{L\ge1415}.
\]

This proves the lower bound for **every** possible binary superstring. No assumption about a particular order or about the connectivity of a relaxed flow solution enters this argument.

## 4. Matching construction

The file [`lyndon12_witness.txt`](lyndon12_witness.txt) gives an explicit 1415-bit witness. The standalone standard-library verification script [`lyndon12_verify.py`](lyndon12_verify.py) embeds that same bit string and checks all 335 target occurrences directly.

Its ASCII SHA-256 digest is:

```
a60713e2e8cacda5f13a69721afac2e5c9236ba84b10d9d5edd2ce0cc50bc95f
```

There are 1404 length-12 factors in the witness. Selecting one occurrence of each of the 335 mandatory factors, the remaining **1069** edges each increase the constructed potential by exactly 1. The walk begins at vertex 60 with potential 11 and ends at vertex 1783 with potential 0, and the selected mandatory edges have total potential change -1080. This saturates the lower-bound inequality:

\[
-11=-1080+1069.
\]

Thus a length-1415 superstring exists, and none of length 1414 or less exists:

\[
\boxed{L_{12}=1415}.\quad\square
\]

## 5. Reproduction and scholarly status

Run `python3 lyndon12_verify.py` (Python standard library only). The script needs no external data files and checks all 4096 directed edge inequalities, the potential summary, and the explicit construction. The companion `lyndon12_witness.txt` file permits direct inspection of the construction; the verifier reconstructs all potential values.

The finite certificate was found computationally using a graph-flow relaxation, but **its proof does not depend on that solver's correctness**: all required statements can be replayed using only the published source lists, witness, and basic algorithms.

**Priority warning.** This is a new analysis within this research session, **not** a verified claim of first discovery or a peer-reviewed result. The precise length-twelve instance may have appeared in earlier literature or unpublished work. Related context: Marcin Mucha, *Lyndon Words and Short Superstrings* (SODA 2013, doi:10.1137/1.9781611973105.69), concerns the general shortest-superstring problem and use of Lyndon words; it does not establish the exact value here on the basis of the material checked. The earlier length-eight instance is recorded as P2600 at TheoremDB: https://theoremdb.org/statements/P2600/ . AI assistance should be disclosed in any eventual submission.