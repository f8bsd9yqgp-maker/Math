# The shortest binary superstring containing every Lyndon word of length thirteen

**Research note — 12 October 2026**  
**Result:** a finite, reproducible proof certificate for the exact minimum of **2,804 bits**.  
**Scholarly status:** AI-assisted computation; independently reproducible mathematical certificate, but not yet independently peer-reviewed or checked exhaustively for prior publication.

## Theorem

Let \(\mathcal L_{13}\) be the set of all binary Lyndon words of length thirteen. Then the least length of a binary word containing every member of \(\mathcal L_{13}\) as a contiguous substring is

\[
\boxed{L_{13}=2804}.
\]

The assertion is accompanied by (1) a finite, precisely specified potential function proving the global lower bound, (2) a 2,804-bit witness, and (3) a standard-library Python verifier. **No trust in an optimization solver is required to verify the proof.**

## 1. The graph model

Put \(b=12\), \(V=2^b=4096\). Regard each integer \(v\in\{0,\ldots,4095\}\) as a length-twelve binary word. The directed binary de Bruijn graph has edges

\[
  u \longrightarrow (2u+a)\bmod4096,\qquad a\in\{0,1\}.
\]

The 8,192 edges correspond bijectively to the 13-bit words. The source of the edge labeled by \(w\in[0,8191]\) is \(\lfloor w/2\rfloor\), and its target is \(w\bmod4096\).

A word \(S\) of length \(L\ge13\) determines a directed walk of exactly \(L-12\) edges, one per consecutive thirteen-bit factor.

Recall that a **Lyndon word** is strictly lexicographically smaller than each nontrivial cyclic rotation. Because 13 is prime, the number of binary Lyndon words of length 13 is

\[
  |\mathcal L_{13}|=\frac{2^{13}-2}{13}=\boxed{630}.
\]

The verifier also constructs this set directly, testing all \(8,192\) possible 13-bit words against their 12 nontrivial rotations.

## 2. A finite potential certificate

Write \(d(a,v)\) for the shortest **directed** distance from vertex \(a\) to vertex \(v\) in the de Bruijn graph. Its value is at most 12: append the twelve bits of \(v\) to reach it from any \(a\).

Take the weighted seed sets \(A_h\) in **Table 1** below, and define

\[
 p(v)=\min\left\{12,\ \min_{0\le h\le8}\ \min_{a\in A_h}\bigl(h+d(a,v)\bigr)\right\}.
\]

There are **188** weighted seed vertices total. The table, formula, and direct shortest-path calculations completely specify every one of the 4,096 values of \(p\).

### Table 1: Seeds grouped by initial potential height

| Height \(h\) | \(|A_h|\) | Vertices \(a\in A_h\) |
|---:|---:|---|
| 0 | 153 | 741, 811, 813, 815, 825, 843, 857, 869, 873, 889, 921, 923, 933, 937, 947, 953, 971, 973, 979, 985, 997, 999, 1001, 1011, 1017, 1227, 1253, 1267, 1323, 1325, 1327, 1331, 1333, 1335, 1339, 1341, 1343, 1355, 1357, 1359, 1363, 1383, 1395, 1435, 1437, 1439, 1447, 1451, 1459, 1461, 1485, 1487, 1491, 1493, 1511, 1515, 1523, 1525, 1691, 1693, 1695, 1703, 1707, 1709, 1711, 1717, 1719, 1723, 1725, 1727, 1743, 1749, 1751, 1757, 1767, 1771, 1773, 1781, 1789, 1851, 1853, 1855, 1871, 1877, 1879, 1883, 1885, 1887, 1899, 1901, 1903, 1909, 1915, 1917, 1951, 1963, 1965, 1967, 1973, 1975, 1979, 1981, 2005, 2007, 2011, 2013, 2027, 2029, 2031, 2037, 2039, 2043, 2045, 2731, 2735, 2743, 2747, 2751, 2775, 2779, 2783, 2795, 2799, 2807, 2811, 2815, 2907, 2911, 2927, 2935, 2939, 2943, 2991, 2999, 3003, 3007, 3035, 3039, 3055, 3063, 3067, 3071, 3511, 3519, 3551, 3567, 3575, 3583, 3823, 3839, 3967, 4031, 4095 |
| 1 | 8 | 919, 1431, 1639, 1643, 1647, 1655, 1659, 1663 |
| 2 | 1 | 1255 |
| 3 | 4 | 713, 809, 841, 969 |
| 4 | 5 | 401, 433, 465, 497, 659 |
| 5 | 5 | 225, 483, 611, 675, 739 |
| 6 | 4 | 323, 453, 581, 583 |
| 7 | 4 | 131, 391, 393, 395 |
| 8 | 4 | 265, 267, 269, 271 |

**Lemma 1 (unit-increase bound).** For every directed graph edge \(u\to v\),

\[
0\le p\le12,\qquad p(v)-p(u)\le1.
\]

**Proof.** A shortest directed path from any vertex \(a\) to \(u\), followed by the edge \(u\to v\), shows \(d(a,v)\le d(a,u)+1\). Thus every function \(v\mapsto h+d(a,v)\) satisfies the same unit-increase inequality; so does the constant function 12. Their pointwise minimum also satisfies it. The definition gives \(0\le p\le12\). \(\square\)

The machine-readable verifier independently computes all 188 shortest-path functions using breadth-first search. It confirms every inequality on **all 8,192 edges** and confirms that the potential attains both 0 and 12.

## 3. Potential drop across the 630 mandatory words

Define the incoming/outgoing imbalance of each vertex among the 630 compulsory Lyndon edges by

\[
 \Delta(v)=\#\{w\in\mathcal L_{13}:\operatorname{tail}(w)=v\}
              -\#\{w\in\mathcal L_{13}:\operatorname{head}(w)=v\}.
\]

For these words there are precisely **252 vertices with \(\Delta=+1\)**, **252 with \(\Delta=-1\)**, and all others have zero imbalance. (Each claim is checked by generating the target set from its definition.)

The sum of potential decreases over the required edges, computed exactly from Table 1, is

\[
 D=\sum_{w\in\mathcal L_{13}}\bigl(p(\operatorname{tail}w)-p(\operatorname{head}w)\bigr)
  =\sum_{v=0}^{4095}\Delta(v)p(v)
  =\boxed{2174}.
\]

The equality \(D=2174\) is checked in two equivalent ways by the companion verifier: summing decreases across the 630 required edges and summing the divergence-weighted vertex potentials. The Lipschitz inequalities and potential range are checked separately.

## 4. Global lower bound

Let \(S\) be **any** superstring containing all 630 Lyndon words. Select one occurrence of each required thirteen-bit factor along its de Bruijn walk. Those 630 selected transitions cause an aggregate potential change \(-D=-2174\). Their positions, order and overlap do not matter because each contribution is associated with its directed edge.

There are \((L-12)-630\) other transitions. Lemma 1 says every such transition increases the potential by at most 1, so

\[
 p(\mathrm{end})-p(\mathrm{start})\le-2174+(L-12-630).
\]

The range \(0\le p\le12\) forces the left side to be at least \(-12\). Hence

\[
 -12\le-2174+(L-642),
 \quad L\ge\boxed{2804}.
\]

This is universal: there is no assumption about the order of the Lyndon words, block-preserving merges, disjoint substring copies, or any optimization algorithm.

## 5. A matching upper bound

The file [`lyndon13_witness.txt`](lyndon13_witness.txt) contains an explicit binary word of **2,804 bits**. The verifier independently checks that it contains **all 630** Lyndon factors, one by one. Its ASCII SHA-256 checksum is

```
ddbb6eb0f9b5a726778028a172715d9a93597a7a9745eb8b8fb991076788fd81
```

A stronger tightness check also passes: the word begins at graph vertex 200 with potential 12 and finishes at vertex 1979 with potential 0. Choosing the first occurrence of every Lyndon word, all 2,162 remaining transitions increase potential by **exactly one unit**. Consequently our lower-bound inequalities are equalities for the witness.

The 2,804-bit witness is therefore optimal. \(\square\)

## 6. How to reproduce the certificate

Put `lyndon13_verify.py` and `lyndon13_witness.txt` in the same directory and run

```bash
python3 lyndon13_verify.py
```

This needs **only Python 3's standard library**, not NumPy, SciPy, or an LP optimizer. It constructs the potential from the 188 weighted seeds using independent breadth-first searches and regenerates the Lyndon set directly from the definition. The independent assignment calculation (SciPy's Hungarian algorithm) also found that 2,162 supplementary transitions are necessary. This matching lower bound corroborates the potential proof but is not required for checking it.

## 7. Context, scope and priority

TheoremDB problem [P2600](https://theoremdb.org/statements/P2600/) concerns the analogous length-eight question. The length-thirteen result is a natural extension of that exact combinatorics-on-words problem; the present note does **not** establish that it was already registered as an open problem or that this value has never appeared elsewhere. For background see Marcin Mucha, *Lyndon Words and Short Superstrings* (SODA 2013; arXiv:1205.6787), and Harold Fredricksen and James Maiorana, *Necklaces of beads in k colors and k-ary de Bruijn sequences* (Discrete Mathematics, 1978). Neither reference is claimed to establish this particular exact value.

This result and its computational certificate were developed with assistance from OpenAI's ChatGPT. Reproduction of the finite checks, independent human mathematical review, and a thorough literature/priority check are recommended before making claims of an original published discovery. GitHub publication is not peer review.