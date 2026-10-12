# Toward a general theorem for shortest binary Lyndon superstrings

**Research note — 12 October 2026**  
**Status:** unconditional universal structural and lower-bound theorems, an exact network-flow characterization of the *relaxation*, and an **unresolved** all-length optimality conjecture. Includes an independent exact certificate for length 16. **This is not a proof of a closed formula for all lengths.** The standard network-flow results used here are established mathematical techniques, and no priority or newness is claimed without external review.

## 1. Definitions

For each integer `n >= 2`, let `W_n` be the set of binary Lyndon words of length `n`, and let `q_n = |W_n|`. A word is Lyndon if it is lexicographically strictly smaller than every nontrivial cyclic rotation. The necklace-counting formula gives

\[
q_n=\frac1n\sum_{d\mid n}\mu(d)2^{n/d},
\]

where `mu` is the number-theoretic Möbius function. Let `L_n` be the minimum number of bits in any (linear) binary word containing every member of `W_n` as a contiguous factor.

Let `G_n` be the directed order-`n-1` binary de Bruijn graph. Its vertex set is all `(n-1)`-bit strings, and its directed edges are all `n`-bit strings, represented by

\[
e=x_1\cdots x_n:\qquad x_1\cdots x_{n-1}\longrightarrow x_2\cdots x_n.
\]

A length-`L` word spells a walk of `L-n+1` such edges. Call the edges labeled by `W_n` *mandatory*.

## 2. Universal structural theorem (unconditional)

**Theorem 1.** For every `n >= 2`:

1. Every `w in W_n` begins with `0` and ends with `1`.
2. The directed mandatory-edge subgraph of `G_n` is a vertex-disjoint union of directed simple paths (apart from vertices with no mandatory edges).
3. If `h(v)` counts the ones in an `(n-1)`-bit vertex, every mandatory edge `u -> v` satisfies `h(v) = h(u) + 1`.

**Proof.** A nonconstant binary Lyndon word must begin with `0` (otherwise a rotation beginning with `0` is smaller). It cannot end with `0`: the proper suffix consisting of its last `0` would be lexicographically smaller than the word, contrary to the standard equivalent characterization of Lyndon words as smaller than all their nonempty proper suffixes. So the first and last bits are `0` and `1`.

For a fixed vertex, there is at most one mandatory outgoing edge because its appended bit must be `1`. There is at most one mandatory incoming edge because its prepended bit must be `0`. Hence every nontrivial connected component is a directed path or directed cycle. Along a mandatory edge the first `0` is dropped and a final `1` is appended, increasing `h` by one. A directed cycle is therefore impossible. QED.

Let `S_n` and `T_n` be the sets of starts and ends, respectively, of the maximal mandatory paths. They have the same cardinality `r_n`.

## 3. An unconditional lower bound for every n

**Theorem 2.** For every `n >= 2`,

\[
\boxed{2q_n \le L_n \le 2^n+n-1.}
\]

**Proof.** The upper bound follows by linearizing any binary de Bruijn cycle of order `n`, which contains every binary `n`-word and hence every member of `W_n`.

For the lower bound, consider a word of length `L` containing all `q_n` required factors. Select one occurrence of each mandatory `n`-factor; they each increase the Hamming weight `h` of the current `(n-1)`-bit vertex by exactly `1`. Each other graph edge changes that weight by at least `-1`. The net weight change in the entire walk is at most `n-1`. Hence the number of nonmandatory occurrences must be at least `q_n-(n-1)`. Since `L-n+1` is the total number of factor occurrences, `L >= (n-1)+q_n+q_n-(n-1)=2q_n`. QED.

This is a true all-length theorem; it is weaker than the exact bounds obtained in the tested instances.

## 4. The path-endpoint matching relaxation

For two `(n-1)`-bit vertices `a,b`, let `d_n(a,b)` be their shortest directed distance in `G_n`. Explicitly,

\[
d_n(a,b)=\min\{k\in\{0,\ldots,n-1\}:\operatorname{suffix}_{n-1-k}(a)=\operatorname{prefix}_{n-1-k}(b)\}.
\]

Define the minimum matching cost

\[
M_n=\min_{\substack{s_0\in S_n,\ t_0\in T_n}}\ \min_{\sigma:T_n\setminus\{t_0\}\overset{\rm bij.}{\to} S_n\setminus\{s_0\}}\ \sum_{t\in T_n\setminus\{t_0\}}d_n(t,\sigma(t)).
\]

Equivalently, add a dummy row and column to the `r_n x r_n` distance matrix, put zero in each ordinary-to-dummy/dummy-to-ordinary position, prohibit dummy-to-dummy, and solve the resulting `(r_n+1) x (r_n+1)` minimum-weight assignment.

**Theorem 3 (unconditional matching lower bound).** For every `n >= 2`,

\[
\boxed{L_n\ge (n-1)+q_n+M_n.}
\]

**Proof.** After selecting one occurrence of every mandatory edge in a candidate superstring walk, its other edges form a nonnegative integral flow with node imbalances balancing the mandatory path endpoints and the start/end of the overall walk. Allowing disconnected components only relaxes this problem. Introduce one artificial unit source with a free zero-cost arc to every vertex and one artificial unit sink with a free zero-cost arc from every vertex. In the relaxed network, each end of a mandatory path is a supply of one unit and each start is a demand of one unit, alongside the artificial source/sink. Integral min-cost flow decomposes into supply-demand paths. The artificial source/sink allow one terminal on each side to remain unmatched. Since ordinary graph arcs cost one per step, replacing each connector by a shortest directed path never increases cost. A flow in which the artificial source connects to the artificial sink can instead delete any one of the remaining end-to-start matches without increasing cost. Therefore the relaxed optimum is exactly `M_n`. Any true connected superstring uses at least that many supplementary edges, giving the inequality. QED.

**Theorem 4 (exact potential dual).** Let `Delta(v)` be the mandatory outdegree minus mandatory indegree of `v`. Then

\[
\boxed{M_n=\max_{p:\;p(v)-p(u)\le1\ \forall (u\to v)\in E(G_n)}
\left(\sum_v\Delta(v)p(v)-\bigl[\max_v p(v)-\min_v p(v)\bigr]\right).}
\]

**Proof sketch.** Each feasible `p` has one-sided Lipschitz differences bounded above by the cost of each arc. Pairing it with the supplementary flow gives a lower bound equal to its mandatory-edge potential decrease less the worst possible endpoint difference. Conversely, formulate the relaxed problem of Theorem 3 as the integral min-cost flow with the artificial source and sink described above. Its linear-programming dual has vertex potentials `p`; its ordinary-edge constraints are `p(v)-p(u)<=1`, while optimizing over the artificial arcs subtracts `max(p)-min(p)`. Strong min-cost-flow LP duality gives equality. Directed de Bruijn diameter `n-1` ensures every feasible potential has range at most `n-1`; the dual optimum may be chosen integral. QED.

Theorem 4 explains the potential certificates for lengths 8–15: they are dual proofs of optimality of the *matching relaxation*. Connectivity plus an Euler trail is a separate issue.

## 5. The exactness criterion, and the unresolved general conjecture

**Theorem 5 (connected matching suffices).** If there exists a minimum-cost assignment attaining `M_n` such that, after replacing each assigned pair by a shortest directed path and adding all mandatory edges, the resulting directed multigraph has **connected undirected support**, then

\[
\boxed{L_n=(n-1)+q_n+M_n.}
\]

**Proof.** All vertices in the resulting graph are balanced except the omitted start, which has outdegree one larger than indegree, and the omitted end, which has indegree one larger than outdegree. A weakly connected directed multigraph with these balance conditions has an Euler trail from the omitted start to the omitted end. Its spelled binary word contains all mandatory factors and has exactly `n-1+q_n+M_n` bits. Theorem 3 proves no shorter word can work. QED.

**OPEN CONJECTURE (not proved):** For every `n >= 2`, at least one minimum-cost assignment has a connected realization as in Theorem 5. Equivalently, the matching lower bound is always sharp:

\[
\color{#a33}{\boxed{L_n\stackrel{?}{=}(n-1)+q_n+M_n\qquad(n\ge2).}}
\]

The conjecture is **not** established by the finite computations below. It would give an algorithm polynomial in the explicit number of Lyndon words (which grows exponentially with `n`), **not** an elementary closed-form expression in `n`.

**Why the gap matters.** For the two arbitrary length-five words `00011` and `01001`, the analogous matching relaxation predicts length `8` but the exact shortest superstring has length `10`: neither word overlaps the other, and the relaxed matching uses disconnected components. Therefore a connected-realization theorem is false for arbitrary binary word sets, even ones beginning `0` and ending `1`. Any proof of the all-length conjecture must use more than the endpoints' bit values; it must exploit genuine Lyndon structure.

## 6. Verified computational evidence, and a new 16-bit instance

The accompanying `lyndon_general_framework.py` constructs the assignment, expands its chosen shortest paths, checks vertex balance, verifies undirected connectivity, runs an Euler-trail algorithm when connected, and checks that all Lyndon factors occur in the resulting word. This solver-based exploration is **evidence, not a proof of the all-n conjecture**.

| n | q_n | paths r_n | matching cost M_n | general lower bound | chosen optimal assignment connected? |
|---:|---:|---:|---:|---:|:---:|
| 2 | 1 | 1 | 0 | 2 | yes |
| 3 | 2 | 1 | 0 | 4 | yes |
| 4 | 3 | 1 | 0 | 6 | yes |
| 5 | 6 | 2 | 4 | 14 | yes |
| 6 | 9 | 3 | 10 | 24 | no* |
| 7 | 18 | 6 | 26 | 50 | yes |
| 8 | 30 | 11 | 57 | 94 | no* |
| 9 | 56 | 20 | 121 | 185 | yes |
| 10 | 99 | 38 | 251 | 359 | yes |
| 11 | 186 | 71 | 519 | 715 | yes |
| 12 | 335 | 134 | 1,069 | 1,415 | yes |
| 13 | 630 | 252 | 2,162 | 2,804 | yes |
| 14 | 1,161 | 479 | 4,390 | 5,564 | yes |
| 15 | 2,182 | 905 | 8,841 | 11,037 | yes |
| **16** | **4,080** | **1,725** | **17,807** | **21,902** | **yes** |

`*` This particular assignment is disconnected. Separate previously constructed superstrings establish equality at lengths 6 and 8; this fact does *not* mean a connected optimal assignment cannot exist.

**Length-sixteen exact certificate.** For `n=16`, minimum cost matching is `17,807`, so Theorem 3 implies

\[
L_{16}\ge 15+4080+17807=\boxed{21902}.
\]

A connected expansion of the assignment yields a 21,902-bit Euler-trail word containing all 4,080 required Lyndon words, proving the matching upper bound. The three companion files give a *solver-free* independent check:

- `lyndon16_matching_dual.json` contains a permutation representing the assignment and integer row/column dual variables.
- `lyndon16_verify.py` enumerates the 4,080 Lyndon words, tests all `1726^2 = 2,979,076` dual inequalities and all assignment equalities, checks primal objective `17,807`, then confirms the witness length and every required factor.
- `lyndon16_witness_experiment.txt` contains the 21,902-bit word; its trimmed-ASCII SHA-256 is `da7df8615e48225b2932e7c7275851ce533ed48d8923b68a1078256c2d693cd8`.

The exact length-16 result is **computationally certified**, but its originality and scholarly status have not been externally checked.

## 7. Next mathematical obstacle

To prove the conjecture, it is enough to establish a **Lyndon-specific uncrossing/connectivity lemma**: among all minimum-weight terminal matchings on the mandatory-path endpoints in the order-`n-1` de Bruijn graph, there is one whose shortest-path expansion forms a weakly connected graph.

Possible routes:

1. Develop an exchange operation switching two matched end/start pairs without increasing distance, reducing the number of connected components; prove the required zero-cost exchange exists for Lyndon path endpoints.
2. Use lexicographic/necklace structure to prove every disconnected minimum matching has such an exchange.
3. Study optimal dual potentials and the strongly connected components of their tight-edge graph, showing that every mandatory path can be integrated into a single Euler trail.

**None of those three steps has been proved here.** This is the precise mathematical gap between our all-length theorems and the desired universal exactness theorem.

## 8. Background and novelty caution

- The existing exact length-eight question: https://theoremdb.org/statements/P2600/
- H. Fredricksen and J. Maiorana, *Necklaces of beads in k colors and k-ary de Bruijn sequences*, *Discrete Mathematics* 23 (1978), 207–210, DOI 10.1016/0012-365X(78)90002-X.
- M. Mucha, *Lyndon Words and Short Superstrings*, SODA 2013, https://arxiv.org/abs/1205.6787. That paper uses Lyndon words in the study of generic shortest-superstring approximation; it does not establish our conjecture.

Classical ingredients such as de Bruijn graphs, min-cost flow integrality, shortest-path distances, assignment duality, and Euler trails are standard. **Do not publish this document as a proved exact all-length formula.** It consists of valid general statements, an explicit open conjecture, and finite evidence to be independently reviewed.