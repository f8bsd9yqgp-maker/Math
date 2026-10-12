# The shortest binary superstring containing every Lyndon word of length fourteen

**Research note — October 12, 2026**  
**Result:** A finite, independently replayable proof certificate for the exact minimum **5,564 bits**.  
**Research status:** AI-assisted computational mathematics. The finite certificate can be checked without an optimization solver. Independent specialist review and verification of publication priority have not yet been completed.

## Theorem

Let \(\mathcal L_{14}\) be the set of all binary Lyndon words of length fourteen. The shortest binary word that contains every member of \(\mathcal L_{14}\) as a contiguous factor has exactly

\[
\boxed{L_{14}=5564}
\]

characters (bits).

The proof has two independent, inspectable components: a **universal lower-bound potential certificate** specified by 358 weighted seed vertices, and a **5,564-bit construction** that contains every required word. Both components are checked by the accompanying Python standard-library program. The proof does *not* require trusting the original optimization output.

## 1. The directed de Bruijn graph

Set \(b=13\), \(V=2^{13}=8192\). Represent each vertex by a binary word of length thirteen, or equivalently an integer \(v\in\{0,\ldots,V-1\}\). Each length-fourteen binary word \(w\) determines an edge from its first thirteen bits to its last thirteen bits:

\[
\left\lfloor w/2\right\rfloor\;\longrightarrow\; w\bmod V.
\]

Equivalently, edges leaving vertex \(u\) terminate at \((2u+a)\bmod V\) for \(a\in\{0,1\}\). Thus there are **16,384 possible edges**.

A binary string of length \(L\geq14\) generates a directed graph walk with exactly \(L-13\) edges, one for every consecutive length-fourteen substring.

A Lyndon word is strictly lexicographically smaller than each nontrivial cyclic rotation. By direct generation, or the necklace formula,

\[
|\mathcal L_{14}| = \frac{2^{14}-2^7-2^2+2}{14}=\boxed{1161}.
\]

Each required word corresponds to a distinct mandatory edge.

## 2. Explicit potential-function certificate

For vertices \(u,v\), write \(d(u,v)\) for shortest directed path length in the graph. Every vertex can reach every other in at most thirteen steps, by appending the bits of the destination.

The file [`lyndon14_seeds.txt`](lyndon14_seeds.txt) lists exactly **358** vertex-height pairs \((a,h)\), one pair per line. Heights are integers between 0 and 9, inclusive. The file is part of the certificate and is identified by SHA-256:

```text
611a9cf5eb8fa9deff0d00ae6be8e74da8ee8588ec368999144825293fe86283
```

The number of seeds at each height is:

| Height | Number of seeds |
|:--:|--:|
| 0 | 284 |
| 1 | 16 |
| 2 | 5 |
| 3 | 4 |
| 4 | 7 |
| 5 | 10 |
| 6 | 10 |
| 7 | 6 |
| 8 | 8 |
| 9 | 8 |
| **Total** | **358** |

Define \(p:\{0,\ldots,8191\}\to \{0,\ldots,13\}\) by

\[
\boxed{p(v)=\min\left\{13,\;\min_{(a,h)\text{ in seeds}}\bigl(h+d(a,v)\bigr)\right\}.}
\]

This formula completely specifies every one of the 8,192 potential values. A multi-source shortest-path search with initial distances equal to the seed heights reconstructs \(p\), without a numerical optimization package. The verifier independently confirms \(\min p=0\) and \(\max p=13\).

**Lemma (one-sided unit change).** For every edge \(u\to v\),

\[
0\leq p\leq13,\qquad p(v)-p(u)\leq1.
\]

**Proof.** For every source \(a\), a shortest path from \(a\) to \(u\), followed by the edge \(u\to v\), yields \(d(a,v)\leq d(a,u)+1\). Adding a fixed height preserves this inequality, and the constant function 13 also satisfies it. The pointwise minimum of functions satisfying this one-sided Lipschitz inequality again satisfies the inequality. The bounds on \(p\) are immediate. \(\square\)

The verifier also directly checks all **16,384** edge inequalities.

## 3. Potential decrease across mandatory Lyndon edges

The certificate proves the following exact numerical identity:

\[
D:=\sum_{w\in\mathcal L_{14}}\left(p\left(\left\lfloor\frac{w}{2}\right\rfloor\right)-p(w\bmod8192)\right)=\boxed{4403}.
\]

To check it independently, generate all Lyndon words by lexicographically comparing with rotations, reconstruct \(p\) from the 358 weighted seeds, and sum the integer differences. The verifier also computes the same value via the graph's mandatory-edge imbalance

\[
\Delta(v)=\#\{w:\operatorname{tail}(w)=v\}-\#\{w:\operatorname{head}(w)=v\},
\]

and checks that

\[
D=\sum_{v=0}^{8191}\Delta(v)p(v).
\]

There are exactly **479** vertices with \(\Delta(v)=+1\), **479** with \(\Delta(v)=-1\), and all remaining vertices have zero imbalance.

## 4. Universal lower bound

Consider **any** binary superstring \(S\) of length \(L\) containing all 1,161 mandatory words. The associated graph walk has \(L-13\) edges. Select one occurrence of each mandatory word. Their 1,161 edge transitions contribute a total change in potential equal to \(-4403\). Every other transition can increase the potential by at most one, by the lemma.

Thus

\[
p(\mathrm{end})-p(\mathrm{start})
\leq -4403+\bigl((L-13)-1161\bigr)
=-4403+(L-1174).
\]

Since \(0\leq p\leq13\), the net change of potential from start to end is at least \(-13\). Therefore

\[
-13\leq-4403+L-1174
\quad\Longrightarrow\quad
\boxed{L\geq 5564}.
\]

No assumption was made about the order of words, how many times a required factor occurs, or any particular string-merging algorithm. The lower bound is valid for **all** binary strings containing every required factor.

## 5. Upper-bound construction and equality checks

The companion file [`lyndon14_witness.txt`](lyndon14_witness.txt) contains an explicit binary string \(S\) of length **5,564**. Its SHA-256 hash as ASCII text (excluding the file's final newline) is

```text
31bb9576482c795a61811a5d678193218b5a67da2d48dce17659d7bce020f277
```

The standard-library verifier independently regenerates all **1,161** required words and checks that they are all contained in \(S\). Its first thirteen bits represent vertex **40** (potential **13**), and its last thirteen bits represent vertex **5631** (potential **0**).

An additional strong check certifies equality in the potential argument: choose the first occurrence of each mandatory Lyndon factor. There are exactly \(L-13-1161=4390\) remaining factor transitions, and **every one of these 4,390 transitions raises the potential by exactly one**. This also independently confirms the exact length.

Thus an explicit upper bound of 5,564 equals the universal lower bound of 5,564:

\[
\boxed{L_{14}=5564}.\quad\square
\]

## 6. Reproducibility

Place the following files in the same directory:

- `lyndon14_verify.py` — standard-library-only proof verifier;
- `lyndon14_seeds.txt` — the 358 weighted source vertices and heights;
- `lyndon14_witness.txt` — the 5,564-bit construction.

Run:

```bash
python3 lyndon14_verify.py
```

The verifier does not import SciPy, NumPy, an LP solver, or a graph package. It reconstructs \(p\) from the seed data and checks all of the proof's finite claims.

**Independent optimization cross-check (not needed for proof):** a separate 480×480 Hungarian assignment formulation with a free start and end also returned 4,390 supplementary edges, matching the min-cost graph flow and the potential certificate. It is included as `lyndon14_assignment_crosscheck.py` for additional reassurance, though it requires NumPy and SciPy.

## 7. Scope and priority

TheoremDB [P2600](https://theoremdb.org/statements/P2600/) concerns the analogous length-eight binary Lyndon superstring problem. This note extends the *family of questions* to length fourteen but does **not** establish that the length-fourteen instance had already been posed as an open research problem. Relevant background: Marcin Mucha, [*Lyndon Words and Short Superstrings*](https://arxiv.org/abs/1205.6787), SODA 2013.

This finite proof and its construction were developed with assistance from OpenAI's ChatGPT. Independent mathematical review, reproduction by others, and a more comprehensive literature search are needed before claiming first discovery, scholarly recognition, or publication priority. GitHub posting and automated checks are not substitutes for peer review.