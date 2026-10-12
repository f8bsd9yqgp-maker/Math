# A sharp lower bound for the binary length-nine Lyndon superstring problem

**Computationally verified research note — October 12, 2026**

**Theorem.** The shortest binary word containing all 56 binary Lyndon words of length nine as contiguous factors has **exactly 185 bits**.

*This note describes an AI-assisted mathematical proof and a reproducible certificate. It has not yet undergone independent specialist review, and publication priority has not been established. Length nine is a natural generalization of the listed length-eight problem, not necessarily a separately registered open problem.*

## 1. Definitions

A binary Lyndon word of length nine is a binary word strictly smaller in lexicographic order than each of its eight nontrivial cyclic rotations. There are 56 such words: by the necklace formula, \((2^9-2^3)/9=56\).

The order-eight binary de Bruijn digraph has vertices \(0,\ldots,255\), each interpreted as an eight-bit binary word. Its directed edges are the 512 nine-bit words, represented by
\[
 u\to ((2u+b)\bmod 256),\qquad b\in\{0,1\}.
\]

Any binary word \(S\) of length \(L\geq 9\) determines a directed walk of \(L-8\) edges, one for each consecutive nine-bit factor.

## 2. Potential function

For vertices \(a,v\), write \(d(a,v)\) for the shortest directed distance from \(a\) to \(v\). The explicit formula uses eight-bit representations:
\[
 d(a,v)=\min\{ k\in\{0,\ldots,8\}:\; \operatorname{suffix}_{8-k}(a)=\operatorname{prefix}_{8-k}(v)\}.
\]

Let
\[
 Z=\{75,77,79,83,103,107,109,117,123,125,171,175,183,187,191,223,239,255\}.
\]

Define the integer-valued potential
\[
 p(v)=\min\left(8,\;5+d(35,v),\;\min_{z\in Z}d(z,v)\right).
\]

**Lemma.** \(0\leq p(v)\leq8\) for every vertex, and \(p(v)-p(u)\leq1\) for every directed edge \(u\to v\).

**Proof.** Clearly \(0\leq p\leq8\). For any source \(a\) and any edge \(u\to v\), appending that edge to a shortest path from \(a\) to \(u\) gives \(d(a,v)\leq d(a,u)+1\). Each term of the pointwise minimum satisfies the same inequality, including the constant 8, so the minimum does too. \(\square\)

## 3. Potential drop of the compulsory factors

Let \(W\) be the set of 56 Lyndon words and \(\Delta(v)\) the outgoing degree minus incoming degree of vertex \(v\) within the 56 mandatory edges. Exhaustive generation of \(W\) gives precisely 20 vertices with \(\Delta=+1\), 20 with \(\Delta=-1\), and 216 with \(\Delta=0\).

The potential values on vertices with nonzero imbalance are:

| Imbalance | Vertices | Potential |
| --- | --- | --- |
| +1 | 0, 2, 4, 6, 8, 10, 12, 14, 18, 20, 22, 26, 28, 30, 38, 42 | 8 |
| +1 | 46, 54, 62 | 2 |
| +1 | 58 | 3 |
| -1 | 35 | 5 |
| -1 | 57 | 3 |
| -1 | All 18 vertices of \(Z\) | 0 |

Thus the sum of the decreases over every compulsory edge is
\[
 D=\sum_{w\in W}\bigl(p(\operatorname{tail}w)-p(\operatorname{head}w)\bigr)
 =\sum_v \Delta(v)p(v)
 =16\cdot8+3\cdot2+3-5-3=\boxed{129}.
\]

This small table is the numerical core of the certificate. All entries are regenerated from first principles by the accompanying standard-library Python verifier.

## 4. Universal lower bound

Suppose a binary word \(S\) of length \(L\) contains every word in \(W\). Select one occurrence of each of the 56 distinct required length-nine factors. Along the de Bruijn walk, those selected factors contribute exactly \(-129\) to the total change in \(p\). The remaining \((L-8)-56=L-64\) edges can each increase \(p\) by at most 1, so
\[
 p(\operatorname{end})-p(\operatorname{start})\leq -129+(L-64)=L-193.
\]

Since the potential always lies between 0 and 8, the left side is at least \(-8\). Therefore \(-8\leq L-193\), implying
\[
 \boxed{L\geq185}.
\]

This reasoning applies to **every** binary string containing all the Lyndon words; it makes no block-preservation, overlap-ordering, or solver assumptions.

## 5. Matching witness

The following 185-bit word contains each of the 56 length-nine binary Lyndon words:

```text
00101010110001001011101100010100110000111011110000011011111000000001111111100000100111110100011110110000110011101010001110010011011010001011011100001000110101100001010111100000010111111
```

Its SHA-256 digest when encoded as ASCII is

```text
bfa8fe8782250d86f25a02d47265be0fc9769a3e128fdb4eccb636d4b1d0b274
```

The independent verifier generates all 56 required words directly from the definition, checks every containment, checks every potential inequality on the 512 graph edges, and confirms the total compulsory-edge drop of 129. It also verifies that the 121 edges not selected as target occurrences each increase the potential by exactly 1, while the witness starts at potential 8 and ends at potential 0. Thus both inequalities above are tight.

**Conclusion.** Combining \(L\geq185\) with the exhibited word of length 185 proves that the minimum is \(\boxed{185}\). \(\square\)

## 6. Reproducibility and research status

Run `python3 lyndon9_verify.py` with any recent Python 3 interpreter. The program uses only Python's standard library and requires no optimization software. The values and inequalities can be verified without trusting a linear-programming optimizer.

Related background: TheoremDB P2600 asks the analogous length-eight question, and Marcin Mucha's paper *Lyndon Words and Short Superstrings* (SODA 2013; DOI 10.1137/1.9781611973105.69) explains the wider shortest-superstring context. This note does not claim Mucha's paper asserts this exact value or technique.

The construction and certificate were developed with OpenAI's ChatGPT. Independent verification, comparison against unpublished work, and scholarly review are still needed before claiming originality or community acceptance.