# A sharp exact bound for binary length-ten Lyndon superstrings

**Research note — October 12, 2026**

**Theorem.** A binary string containing every binary Lyndon word of length ten as a contiguous factor has length **at least 359**. An explicit string of length **359** attains the bound. Therefore, the exact optimum is **359**.

**Status and provenance.** This is an AI-assisted, computationally cross-verified proof with a self-contained finite certificate and witness. Independent human mathematical review, bibliographic comparison, and publication-priority evaluation are pending. The length-ten question is the next natural instance of the length-eight problem listed in TheoremDB, not a claim that it has itself been registered as an open question.

## 1. The 99 mandatory words as graph edges

A Lyndon word is lexicographically strictly smaller than any nontrivial cyclic rotation. There are precisely 99 binary Lyndon words of length ten. Indeed the standard Möbius formula gives `(2^10 - 2^5 - 2^2 + 2)/10 = 99`.

In the order-nine binary de Bruijn graph, vertices are the 512 nine-bit words. A ten-bit word `a1...a10` is the directed edge

`a1...a9 -> a2...a10`.

Numerically, the two outgoing neighbors of a vertex `u` are `2u mod 512` and `(2u+1) mod 512`.

Every string of length `L >= 10` traces a walk of `L-9` edges. Its ten-bit factors are precisely those edges.

## 2. A simple explicit potential

For nine-bit vertices `a` and `v`, let `d(a,v)` denote their shortest **directed** path distance. Equivalently,

`d(a,v) = min{k in {0,...,9} : suffix_(9-k)(a) = prefix_(9-k)(v)}`.

Define

`Z = {101, 105, 115, 121, 147, 149, 151, 155, 157, 159, 167, 179, 181, 205, 207, 213, 215, 221, 235, 237, 245, 247, 251, 253, 343, 347, 351, 367, 375, 379, 383, 439, 447, 479, 511}`.

Define the integer-valued potential

`p(v) = min(9, 4+d(49,v), 6+d(69,v), 6+d(71,v), min_{z in Z} d(z,v))`.

**Lemma (one-sided Lipschitz bound).** `0 <= p(v) <= 9` for every vertex, and for every edge `u -> v` one has `p(v)-p(u) <= 1`.

**Proof.** Directed distances satisfy `d(a,v) <= d(a,u)+1` for every edge `u -> v`: append that edge to a shortest path to `u`. Adding any constant preserves this inequality. The constant function 9 also satisfies it. Finally, the pointwise minimum of functions all satisfying this inequality satisfies the same inequality. Every term is nonnegative and one term is 9. QED.

## 3. Sum over the compulsory edges

Let `W` be the 99 Lyndon edges. Write `Delta(v)` for the number of edges in `W` leaving `v`, minus the number entering `v`. Exhaustive enumeration gives 38 vertices with `Delta=+1`, 38 with `Delta=-1`, and 436 with `Delta=0`; in particular, no vertex has a larger absolute imbalance.

For the 38 positive vertices, the potential values have multiplicities:

| Potential | Count, Delta=+1 |
| ---: | ---: |
| 9 | 27 |
| 6 | 1 |
| 5 | 1 |
| 4 | 1 |
| 3 | 2 |
| 2 | 6 |

For the 38 negative vertices:

| Potential | Count, Delta=-1 |
| ---: | ---: |
| 6 | 2 (vertices 69, 71) |
| 4 | 1 (vertex 49) |
| 0 | 35 (the vertices in `Z`) |

Thus the *total drop* contributed by one occurrence of each required edge is

```
D = sum_{w in W} [p(tail(w)) - p(head(w))]
  = sum_v Delta(v) p(v)
  = (27*9 + 1*6 + 1*5 + 1*4 + 2*3 + 6*2) - (2*6 + 1*4)
  = 260.
```

The companion verifier regenerates every word, imbalance, potential and sum from the given formulas; there are no imported data files and no optimization-solver dependency.

## 4. Universal lower bound

Let a string `S` of length `L` contain all the words in `W`. Its de Bruijn walk has `L-9` edges. Choose one occurrence of each of the 99 distinct mandatory words. Their potential changes sum to `-260`. There are `(L-9)-99 = L-108` other edges, each increasing the potential by *at most* 1.

Hence

`p(end) - p(start) <= -260 + (L-108) = L-368`.

On the other hand, `0 <= p <= 9` implies `p(end)-p(start) >= -9`. Combining these inequalities gives

`-9 <= L-368`, so **`L >= 359`**.

This applies to *every possible arrangement* of the required words, including arrangements that break and interleave their natural overlap paths.

## 5. Upper-bound witness

The following explicit **359-bit** binary string contains every required length-ten binary Lyndon word:

```text
00001111011100010010011101101000001010111110000100101111011000001100111101010001011101110000111001100110101010001111101100011010010000101101111000110010110101000111010110000101001110000001101111110000000101111111000001110111110000001001111110100000000011111111100001100010011011101000101010111000011010111000110110111000100010110011000001000111100100101011011
```

Its SHA-256 digest (ASCII encoding, no newline) is:

`069988f9ac17fd67023ca63e67df0e036ef6f387964f8f218a545de51276793b`

The verifier checks the full 99-word target list against the string, using Python substring search. It also confirms that the potential starts at 9, ends at 0, and that all 251 edges outside the 99 selected required occurrences gain **exactly +1** potential: all inequalities in the lower-bound proof are saturated.

The witness was found by identifying the 38 directed paths formed by the required edges and searching for an ordering minimizing shortest directed connections between consecutive path endpoints. That search is **not** used as evidence for the universal lower bound; the displayed witness itself is all that the upper bound needs.

Therefore **the exact minimum is 359**. QED.

## 6. Independent verification

Run:

```bash
python3 lyndon10_verify.py
```

The program uses the Python standard library only. In particular it:

1. Regenerates all 99 Lyndon words from their defining rotation condition.
2. Calculates all potential values using the explicit distance formula.
3. Independently recomputes the distances by breadth-first search for each of the 38 sources appearing in the potential, checking agreement.
4. Checks all 1,024 de Bruijn transitions.
5. Verifies all 512 vertex imbalances and the mandatory drop of 260.
6. Checks that the witness has length 359 and contains all 99 target words.
7. Checks the extra-edge and start/end equality conditions.

## 7. Related work and research status

- TheoremDB, **P2600**, "Shortest superstring of the binary Lyndon words of length eight" — [problem record](https://theoremdb.org/statements/P2600/).
- Marcin Mucha, *Lyndon Words and Short Superstrings*, SODA 2013, [arXiv:1205.6787](https://arxiv.org/abs/1205.6787), on the larger shortest-superstring topic.
- Fredricksen and Maiorana, *Necklaces of beads in k colors and k-ary de Bruijn sequences*, Discrete Mathematics 23 (1978), 207–210 — a separate de Bruijn construction theorem.

These references establish context, not authorship or priority for this exact length-ten value. The construction and proof certificate here were developed with OpenAI ChatGPT assistance. Independent specialist review and a more thorough prior-art audit are still needed before asserting novelty or acceptance.