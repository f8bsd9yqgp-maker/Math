# Exact shortest superstrings of equal-length Lyndon words: an all-length matching theorem

**Research manuscript (12 October 2026).** **Status:** complete mathematical proof candidate; independently review the argument, test the implementation, and audit prior art before asserting publication priority. Earlier finite certificates for lengths 8–16 are consistent with the theorem. The result is more general than the original binary all-length problem.

## Abstract

Let \(A\) be a totally ordered finite alphabet, and let \(W\) be a finite set of distinct Lyndon words, **all of the same length** \(n\). Let \(\operatorname{ov}(u,v)\) be the length of the longest proper suffix of \(u\) equal to a prefix of \(v\), taking value zero if no nonempty overlap exists. Construct the weighted bipartite graph with a left and right copy of each word and weight \(\operatorname{ov}(u,v)\) from left \(u\) to right \(v\). If \(H(W)\) is the maximum weight of a bipartite matching (zero-weight dummy assignments permitted), then

\[
\boxed{\operatorname{SCS}(W)=n|W|-H(W).}
\]

A maximum-weight matching gives a collection of **directed paths, never positive-weight directed cycles**, because positive overlap between distinct Lyndon words forces strict lexicographic increase. Concatenating those paths constructs an optimal superstring. Thus the problem is polynomial-time solvable in the number of input words using standard weighted bipartite matching. For the family consisting of *all* binary Lyndon words of any fixed length, this resolves the previous matching-connectivity conjecture **conditionally only on this proof being correct**; no external-review or novelty claim is made.

## 1. Overlap-order lemma

Recall the standard Lyndon characterization: a Lyndon word is lexicographically **strictly smaller than every nonempty proper suffix** of itself. Let \(u,v\) be distinct Lyndon words of the same length \(n\) with a nonempty proper suffix-prefix overlap \(x\), of length \(1\le |x|<n\). Then

\[
u < x=\operatorname{suffix}_{|x|}(u)=\operatorname{prefix}_{|x|}(v)<v.
\]

(The final strict inequality holds because a strict prefix is lexicographically smaller than its proper extension.) Consequently,

\[
\boxed{\operatorname{ov}(u,v)>0\ \Longrightarrow\ u<v.}
\]

In particular, the graph of **positive-overlap** arcs on any such set \(W\) is a DAG, with lexicographic order as a topological ordering. This step is independent of the binary alphabet.

## 2. Universal exact matching theorem

**Theorem.** Let \(W\) be any finite set of \(m\ge1\) distinct Lyndon words of a common length \(n\ge1\) over a totally ordered alphabet. Define \(H(W)\) as the maximum total \(\operatorname{ov}(u,v)\) over a set of directed arcs in which each word has at most one selected outgoing and one selected incoming arc. Then the minimum length of a string containing all words in \(W\) as factors is exactly

\[
\boxed{L(W)=mn-H(W).}
\]

**Lower bound.** In any candidate superstring \(S\), choose the first occurrence of every word, and list the words as \(w_1,\ldots,w_m\) in increasing order of their occurrence starting positions \(p_1<\cdots<p_m\). Their starting positions are distinct because the words have the same length and are distinct. For each consecutive pair let \(d_i=p_{i+1}-p_i>0\). If \(d_i<n\), the two occurrences overlap in \(n-d_i\) symbols, hence \(\operatorname{ov}(w_i,w_{i+1})\ge n-d_i\). If \(d_i\ge n\), trivially \(d_i\ge n-\operatorname{ov}(w_i,w_{i+1})\). Therefore

\[
\begin{aligned}
|S|&\ge n+\sum_{i=1}^{m-1}d_i\\
&\ge mn-\sum_{i=1}^{m-1}\operatorname{ov}(w_i,w_{i+1})\\
&\ge mn-H(W),
\end{aligned}
\]

since the \(m-1\) ordered consecutive arcs form a feasible bipartite matching and their total overlap cannot exceed the maximum weight \(H(W)\).

**Upper bound.** Take any maximum-weight bipartite matching. Discard zero-weight arcs: they do not contribute to its weight. The remaining edges give each word indegree at most one and outdegree at most one. Because a positive overlap forces \(u<v\), the resulting directed graph is **acyclic**. Its connected components are thus vertex-disjoint directed paths, including isolated vertices. For each path \(w_1\to\cdots\to w_k\), start with \(w_1\) and append each subsequent word omitting its overlapping prefix; the length is \(kn-\sum_{i<k}\operatorname{ov}(w_i,w_{i+1})\). Concatenate all the path strings in any order, without claiming any further compression. Every required word is present and the total length is exactly \(mn-H(W)\). Combined with the lower bound, this proves the theorem. \(\square\)

The theorem gives an **exact formula in terms of a finite maximum-weight matching**, not a simple elementary closed formula just in \(n\). A matching is computable in polynomial time in the explicitly listed input size (e.g. via the Hungarian algorithm).

## 3. Closing the originally missing path-connector lemma

We also give a direct proof tailored to the earlier de Bruijn-graph relaxation. For binary Lyndon words of fixed length \(n\ge2\):

* Every mandatory word begins in `0` and ends in `1`. Thus each length-\((n-1)\) vertex has at most one required incoming and one required outgoing edge; required edges form disjoint directed paths (cycles are impossible because each required edge increases the number of ones in its vertex by one).
* Denote these maximal mandatory paths by \(P_1,\ldots,P_r\), their starts by \(s_i\), their ends by \(t_i\), and the total number of required edges by \(q\).
* Set \(B=n-1\), and let \(d(a,b)\) be the shortest directed de Bruijn distance from \(a\) to \(b\). Every pair satisfies \(0\le d(a,b)\le B\). Define the augmented minimum-weight assignment on end-to-start connectors \(c_{ij}=d(t_i,s_j)\), with one free dummy row and one free dummy column; dummy-to-dummy is forbidden. Write its optimum \(M\).

**Lemma (cycles contain a maximum-cost connector).** Within each mandatory path, successive Lyndon edges overlap in \(n-1\) bits; the overlap-order lemma implies the edge labels are strictly increasing lexicographically. If an ordinary connector from \(t_i\) to \(s_j\) has cost \(d(t_i,s_j)<B\), the final length-\(n\) Lyndon word of \(P_i\) has a nonempty suffix-prefix overlap with the first Lyndon word of \(P_j\). Hence the final word of \(P_i\) is lexicographically less than the first word of \(P_j\). Thus a directed cycle of mandatory paths whose *every* connector has cost below \(B\) would imply a strict cyclic lexicographic increase, impossible. **Every closed cycle of an augmented assignment has at least one connector of cost exactly \(B\).**

**Lemma (zero-cost two-pair exchange).** Let \(\sigma\) be an optimal augmented matching containing a closed cycle distinct from the cycle containing the dummy node. Select a connector on that closed cycle, \(t_i\to s_j\), costing \(B\), and the dummy row's chosen edge \(\ast\to s_k\), costing \(0\). Swap their destination columns. The new two costs are \(d(t_i,s_k)\le B\) and \(0\), so the new assignment is no more expensive than \(\sigma\). Optimality of \(\sigma\) forces equality. Both new matches are admissible, and swapping images of two nodes in different permutation cycles merges those cycles into one. Thus the number of cycles decreases by one **without increasing the matching cost**.

Iterating this exchange produces a single augmented permutation cycle containing the dummy node. Deleting the dummy node gives an ordering of **every mandatory path exactly once**, connected by shortest de Bruijn paths of total cost \(M\). It spells one superstring of length \(B+q+M\).

**Matching lower bound justification.** In an arbitrary superstring walk, remove one occurrence of each mandatory edge; the remaining nonnegative integer flow has supplies at the ends \(t_i\) and the overall walk start, demands at the starts \(s_i\) and the overall walk end. Any integral-flow decomposition into paths and cycles yields, after discarding cycles and nonnegative paths involving the overall endpoints, an augmented matching of at most the supplementary edge count. If the overall start connects directly to the overall end, drop any one ordinary end/start pair from the full matching, which does not increase its cost. Otherwise one end is paired with the overall end, and the overall start is paired with one start, with the remaining \(r-1\) pairings between path endpoints. Replacing these connections by shortest paths can only reduce cost. Consequently, supplementary edges \(\ge M\), so any superstring length \(\ge B+q+M\).

Combining lower and upper bounds,

\[
\boxed{L_n=(n-1)+q_n+M_n\qquad\text{for every }n\ge2.}
\]

**This is the exact statement that the previous research note labeled an open conjecture.** The proof here supplies the previously missing zero-cost cycle-merging argument, with the Lyndon overlap-order lemma as its key ingredient. Independent mathematical review is still important.

## 4. Equivalence of the two matching formulas

Let \(H_n\) be the optimal total overlap in Section 2 for the full set of \(q_n\) binary Lyndon words of length \(n\). The same optimal length is now expressed as

\[
L_n=nq_n-H_n=(n-1)+q_n+M_n.
\]

Thus there is the explicit relation

\[
\boxed{M_n=(n-1)(q_n-1)-H_n.}
\]

This is independently checkable numerically and relates the earlier potential/flow certificates to the simpler weighted-overlap theorem.

## 5. Finite numerical checks

The new **independent maximum-overlap matching** computation (using the full list of Lyndon words rather than the path-connector matching) reproduced all exact lengths through \(n=17\). For \(n=18\), the path-connector matching, repeated zero-cost swaps, an explicit 86,295-bit string, and direct factor-coverage checks independently confirmed the construction and value against the relaxation, although the large full-word overlap-matching attempt exhausted memory in this environment; do not label that one as cross-validated by both implementations.

| n | Number of Lyndon words \(q_n\) | Optimal length \(L_n\) |
|---:|---:|---:|
| 2 | 1 | 2 |
| 3 | 2 | 4 |
| 4 | 3 | 6 |
| 5 | 6 | 14 |
| 6 | 9 | 24 |
| 7 | 18 | 50 |
| 8 | 30 | 94 |
| 9 | 56 | 185 |
| 10 | 99 | 359 |
| 11 | 186 | 715 |
| 12 | 335 | 1,415 |
| 13 | 630 | 2,804 |
| 14 | 1,161 | 5,564 |
| 15 | 2,182 | 11,037 |
| 16 | 4,080 | 21,902 |
| 17 | 7,710 | 43,421 |
| 18 | 14,532 | 86,295 |

Relevant scripts:

- `lyndon_all_lengths_matching_solver.py`: independent maximum-overlap matching solver and explicit construction.
- `lyndon_zero_cost_exchange_research.py`: path-endpoint matching, zero-cost cycle exchanges, and construction.
- Previously published independent, solver-free certificates for length 8–16.

## 6. Literature and research-integrity note

The Lyndon proper-suffix characterization is classical. See [Encyclopedia of Mathematics: Lyndon word](https://encyclopediaofmath.org/index.php?lang=en&title=Lyndon_word). General shortest-superstring optimization and Lyndon words appear together in Marcin Mucha, *Lyndon Words and Short Superstrings* (SODA 2013, [arXiv:1205.6787](https://arxiv.org/abs/1205.6787)), but that paper's abstract addresses general shortest-superstring approximation and does **not by itself establish priority** of the exact restricted-input result above. The binary length-8 instance appears in [TheoremDB P2600](https://theoremdb.org/statements/P2600/).

The proof is self-contained beyond the standard Lyndon characterization and elementary matching facts. Nonetheless, do **not** call it novel, accepted, or peer-reviewed without independent scholarly verification and a full prior-art search. The theorem's proof, rather than a finite sequence of optimizer outputs, is what would support the all-length claim.