# The shortest superstring containing all binary Lyndon words of length fifteen

**Research note · October 12, 2026**  
**Result:** An exact finite proof certificate for **11,037 bits**, with a solver-free, standard-library Python verifier.  
**Research status:** AI-assisted mathematical computation. The finite certificate has passed local independent checks, but it has **not** undergone independent specialist peer review or an exhaustive literature/prior-publication audit.

## Theorem

Let \(\mathcal L_{15}\) be the set of binary Lyndon words of length fifteen: the binary words of length fifteen that are strictly lexicographically smaller than all of their nontrivial cyclic rotations. The minimum length of a binary string containing every member of \(\mathcal L_{15}\) as a contiguous substring is

\[
\boxed{L_{15}=11037}.
\]

The proof consists of two finite, independently inspectable certificates: a potential-function lower bound, reconstructed from 657 weighted seeds, and an explicit matching binary string of length 11,037. The proof relies **only** on checking these certificates, not on trusting an optimization algorithm.

## 1. Binary de Bruijn graph representation

Let \(b=14\) and \(V=2^{14}=16384\). The directed de Bruijn graph has vertices identified with fourteen-bit binary strings (equivalently integers in \(0,\ldots,V-1\)). For each vertex \(u\), the two outgoing edges terminate at

\[
(u\cdot2)\bmod V,\qquad (u\cdot 2+1)\bmod V.
\]

Equivalently, each binary fifteen-bit word \(w\), regarded as an integer, specifies the directed edge

\[
\left\lfloor w/2\right\rfloor \longrightarrow w\bmod V.
\]

The graph therefore has 16,384 vertices and 32,768 directed edges. A binary string of length \(L\) spells a directed walk of exactly \(L-14\) edges, corresponding to consecutive length-fifteen substrings.

The number of length-fifteen binary Lyndon words is

\[
|\mathcal L_{15}| = \frac{1}{15}(2^{15}-2^5-2^3+2)=\boxed{2182}.
\]

This follows from Möbius inversion, and is also reproduced by two distinct enumerations in the verifier.

## 2. A finite potential-function certificate

For vertices \(a,v\), write \(d(a,v)\) for the shortest directed path length from \(a\) to \(v\). The companion file [lyndon15_seeds.txt](lyndon15_seeds.txt) lists exactly 657 ordered pairs \((a,h)\), each consisting of a vertex \(a\in\{0,\ldots,16383\}\) and a nonnegative integer height \(h\leq 13\). The file's SHA-256 hash is:

```text
10ec744ed2003d420855cb4b6343f5c3a3586e5395d6a6f520141f6c62907572
```

Define the integer-valued potential by

\[
\boxed{p(v)=\min\left(14,\ \min_{(a,h)\text{ listed in seeds}}\bigl(h+d(a,v)\bigr)\right).}
\]

The verifier reconstructs all 16,384 values using multi-source shortest paths, without consulting the optimization solver that originally produced the certificate. This gives \(\min p=0\) and \(\max p=14\).

**Lemma (one-sided Lipschitz bound).** For every graph edge \(u\to v\),

\[
p(v)-p(u)\leq1.
\]

**Proof.** Appending \(u\to v\) to a shortest directed path from \(a\) to \(u\) establishes \(d(a,v)\le d(a,u)+1\). For every seed \((a,h)\), the function \(h+d(a,\cdot)\) therefore satisfies the claimed bound. The constant function 14 does too. The pointwise minimum preserves this one-sided Lipschitz bound. \(\square\)

The verifier also explicitly checks the inequality for all **32,768** edges.

The 657 seed heights are distributed as follows:

| Height | Count |
|---:|---:|
| 0 | 523 |
| 1 | 26 |
| 2 | 7 |
| 3 | 8 |
| 4 | 13 |
| 5 | 18 |
| 6 | 15 |
| 7 | 12 |
| 8 | 16 |
| 9 | 12 |
| 10 | 7 |
| **Total** | **657** |

## 3. Mandatory-edge potential drop

For every Lyndon word \(w\in\mathcal L_{15}\), let \(t(w)\) and \(h(w)\) denote its tail and head in the directed graph. The reconstructed potential gives the exact integer sum

\[
D:=\sum_{w\in\mathcal L_{15}}\bigl(p(t(w))-p(h(w))\bigr)=\boxed{8855}.
\]

This is the numerical core of the proof certificate. As an independent check, write \(\Delta(v)\) for the number of required edges leaving \(v\) minus the number entering \(v\). Direct enumeration produces exactly **905** vertices with \(\Delta=+1\), **905** with \(\Delta=-1\), and zero at all remaining vertices. Then the verifier separately establishes

\[
D=\sum_{v=0}^{V-1}\Delta(v)p(v)=8855.
\]

There is no numerical approximation: all values and operations in the certificate are integers.

## 4. Universal lower bound

Consider *any* binary superstring \(S\) of length \(L\) containing every element of \(\mathcal L_{15}\). It spells a graph walk of \(L-14\) transitions. Select one occurrence of each of the 2,182 mandatory words. Their combined potential change is \(-D=-8855\), regardless of their ordering or the locations of the chosen occurrences.

All other transitions can increase the potential by **at most 1**, by the lemma. Their number is

\[
(L-14)-2182=L-2196.
\]

Therefore

\[
p(\mathrm{end})-p(\mathrm{start})\le-8855+(L-2196).
\]

Since the potential lies between 0 and 14, the change on the left is at least \(-14\). Consequently,

\[
-14\le -8855+(L-2196)\quad\Longrightarrow\quad\boxed{L\ge11037}.
\]

This is a universal lower bound. It does not assume any particular construction, order of the Lyndon words, or restriction on overlap-merging algorithms.

## 5. Explicit matching upper bound

The companion file [lyndon15_witness.txt](lyndon15_witness.txt) contains an explicit binary word \(S\) of length **11,037**. Its SHA-256 digest, computed on the ASCII bits without the trailing file newline, is

```text
64f05492c9b978dbd5ac2bb1f92bcdc9b08310a42a4789d26138c7a7325938e0
```

A standard-library-only program regenerates the 2,182 required words by two independent methods and verifies that each appears in \(S\) as a contiguous factor.

Further equality checks show that the first fourteen bits give vertex **92**, where \(p=14\), and the final fourteen bits give vertex **11743**, where \(p=0\). If one occurrence of each required word is selected, every one of the other **8,841** edge transitions increases the potential by exactly **1**. Hence the witness *saturates* the inequalities from the lower-bound argument.

This proves an upper bound \(L\le11037\) that matches the universal lower bound. Thus

\[
\boxed{L_{15}=11037}.\qquad\square
\]

## 6. How to reproduce the proof

Place these files together:

- [lyndon15_verify.py](lyndon15_verify.py) — independent Python standard-library verifier;
- [lyndon15_seeds.txt](lyndon15_seeds.txt) — 657 weighted seeds defining the lower-bound potential;
- [lyndon15_witness.txt](lyndon15_witness.txt) — explicit 11,037-bit construction.

Run:

```sh
python3 lyndon15_verify.py
```

The script recomputes the target set by string rotation and bitwise rotation, reconstructs the potential via multi-source shortest paths, tests every one of the 32,768 graph inequalities, verifies the mandatory drop both edgewise and by vertex imbalance, checks the witness and both SHA-256 hashes, and confirms every equality condition.

It requires no SciPy, NumPy, solver, web connection, or privileged computational resource. It should finish rapidly on an ordinary computer. The optimization originally used to *discover* the certificate is not logically needed to *verify* the theorem.

## 7. Scope, sources, and novelty

This result concerns an **exact finite instance** of a shortest-superstring problem, rather than a solution of the general NP-hard shortest-superstring problem. The general reduction to de Bruijn graph edge-covering, as well as shortest-path potentials and linear-programming duality, are well-established methods in discrete optimization. The candidate contribution is the explicit matching certificate for this Lyndon-word instance and the developing family of related certificates for lengths 8–15.

Background references:

1. [TheoremDB P2600](https://theoremdb.org/statements/P2600/) gives a separately recorded, then-open *length-eight* instance and previous bounds, not a result about length fifteen.
2. Marcin Mucha, [*Lyndon Words and Short Superstrings*](https://doi.org/10.1137/1.9781611973105.69), SODA 2013, explains connections between Lyndon-word structure and shortest-superstring approximation algorithms; that work is **not claimed** to establish or refute this exact length-fifteen result.
3. Harold Fredricksen and James Maiorana, *Necklaces of beads in k colors and k-ary de Bruijn sequences*, *Discrete Mathematics* 23(3) (1978), 207–210, for classical de Bruijn/Lyndon construction context.

**Originality caveat:** A reproducible result is not automatically a previously unknown discovery. Independent specialists should scrutinize the certificate and earlier literature before a novelty or priority claim. This note and its computations were produced with OpenAI ChatGPT assistance.