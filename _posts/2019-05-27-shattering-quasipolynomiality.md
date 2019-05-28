---
layout: post
title: Shattering and quasipolynomiality
date: 2019-05-27 17:07
---
An inadequately-explained phenomenon in computational complexity theory is that there are so few natural candidates for [$$\mathsf{NP}$$-intermediate problems](https://en.wikipedia.org/wiki/NP-intermediate), problems in $$\mathsf{NP}$$ but neither in $$\mathsf{P}$$ nor be $$\mathsf{NP}$$-complete. Of course, if $$\mathsf{P}=\mathsf{NP}$$ there are none, and the [dichotomy theorem](Schaefer's dichotomy theorem) implies that there are no intermediate Boolean constraint satisfaction problems. But there are a lot of other types of problems in $$\mathsf{NP}$$, and a theorem of Ladner[^l] shows that there should be an infinite hierarchy of degrees of hardness within $$\mathsf{NP}$$. So where are all the members of this hierarchy, and why are they so shy?

The same thing happens not just for $$\mathsf{P}$$ but for other related complexity classes like [$$\#\mathsf{P}$$](https://en.wikipedia.org/wiki/%E2%99%AFP). There should be many $$\#\mathsf{P}$$-intermediate classes but we know even fewer than for $$\mathsf{NP}$$. [I recently posted](https://mathstodon.xyz/@11011110/102118180704402052) about a discussion I had with Igor Pak on this issue, in which we suggested to each other two number-theoretic candidates for being $$\#\mathsf{P}$$-intermediate, the [Euler totient function](https://en.wikipedia.org/wiki/Euler%27s_totient_function) and the [prime-counting function](https://en.wikipedia.org/wiki/Prime-counting_function) (see also [Igor's StackExchange question on this](https://cstheory.stackexchange.com/q/43954/95)). But although they're in $$\#\mathsf{P}$$, neither of these functions is very combinatorial.

So anyway, the point of all this is to discuss more candidates for being $$\#\mathsf{P}$$-intermediate that are, I think, natural and combinatorial. They're part of a family of problems that include a couple of related candidates for being $$\mathsf{NP}$$-intermediate, and even a candidate for being $$\Sigma_2^P$$-intermediate. These problems come from computational learning theory, or alternatively they can be seen as coming from mathematical logic, hereditary graph theory, and the theory of the [Rado graph](https://en.wikipedia.org/wiki/Rado_graph). And they're all at what is in some sense the shallow end of the intermediate problems: they're solvable in quasi-polynomial time, meaning $$2^{(\log n)^{O(1)}}$$, but not known to be solvable in polynomial time. So this is pretty strong evidence that they're not complete for their respective complexity classes, but weaker evidence than usual that they're not polynomial.

In learning theory, a family of sets $$\mathscr{F}$$ is said to _shatter_ another set $$S$$ (not necessarily belonging to $$\mathscr{F}$$) if every subset of $$S$$, including the empty set and $$S$$ itself, can be obtained by intersecting $$S$$ with some member of $$\mathscr{F}$$. The [Vapnik–Chervonenkis dimension](https://en.wikipedia.org/wiki/Vapnik%E2%80%93Chervonenkis_dimension) of $$\mathscr{F}$$ is just the size of the largest set that is shattered by  $$\mathscr{F}$$. If we let $$m=\vert\mathscr{F}\vert$$ (the number of sets in the family) and $$n=\vert\bigcup\mathscr{F}\vert$$ (the number of distinct elements in those sets), then the dimension is clearly at most $$\log_2 m$$, because sets of size larger than $$\log_2 m$$ have too many subsets for them all to be formed by intersection with a member of $$\mathscr{F}$$. Therefore, the following problem can be solved in quasipolynomial time, by a brute-force search of the $$O(n^{\log_2 m})$$ small-enough subsets of $$\bigcup\mathscr{F}$$:[^lmr]

VC-dimension (largest shattered set)
: Input: family of sets $$\mathscr{F}$$, number $$d$$

  Output: true if $$\mathscr{F}$$ shatters a set of size $$\ge d$$, false otherwise.

The same quasipolynomial time bound applies to the following related problems,
the first of which is also in $$\mathsf{NP}$$ and the second of which is in $$\#\mathsf{P}$$:

Smallest non-shattered set
: Input: family of sets $$\mathscr{F}$$, number $$k$$

  Output: True if there exists a subset $$S$$ of $$\bigcup\mathscr{F}$$
  of size $$\le k$$ that is not shattered by $$\mathscr{F}$$, false otherwise.

Number of shattered sets
: Input: family of sets $$\mathscr{F}$$

  Output: the number of sets shattered by $$\mathscr{F}$$.

For the first two problems, being non-$$\mathsf{NP}$$-complete hinges on the assumption that $$\mathsf{P}\ne\mathsf{NP}$$, but for the number of shattered sets, being non-$$\#\mathsf{P}$$-complete (under [counting reductions](https://en.wikipedia.org/wiki/Polynomial-time_counting_reduction)) is unconditional: the output doesn't provide enough bits of information to encode the answers to all other $$\#\mathsf{P}$$ problems.
The VC-dimension is hard to approximate under a form of the [exponential time hypothesis](https://en.wikipedia.org/wiki/Exponential_time_hypothesis), strongly suggesting that it cannot be computed exactly in polynomial time.[^mr]

To see that the two existence problems can sometimes both have answers that are logarithmic, it's helpful to turn to the theory of random graphs, and of _the_ random graph, the [Rado graph](https://en.wikipedia.org/wiki/Rado_graph). This graph obeys a collection of _extension axioms_ according to which, for every two disjoint finite subsets of vertices, there exists another vertex adjacent to everything in the first subset and to nothing in the second subset. Using these axioms, we can build up induced copies of any finite or countable subgraph, one vertex at a time, using a greedy algorithm. Based on this property, let's define a subset $$S$$ of the vertices in an undirected graph to be _extensible_ if, for every partition of $$S$$ into two disjoint subsets, there exists another vertex outside $$S$$ that is adjacent to everything in the first subset and to nothing in the second subset. This is nothing more than being shattered by the neighborhoods of the vertices outside $$S$$. So we have the following corresponding problems.

Largest extensible set
: Input: Undirected graph $$G$$, number $$d$$

  Output: true if $$G$$ has an extensible set of size $$\ge d$$, false otherwise.

Smallest non-extensible set
: Input: Undirected graph $$G$$, number $$k$$

  Output: true if $$G$$ has a non-extensible set of size $$\le k$$, false otherwise.

Smallest missing induced subgraph
: Input: Undirected graph $$G$$, number $$k$$

  Output: true if there is a graph $$H$$ on at most $$k$$ vertices that
  is not an induced subgraph of $$G$$, false otherwise.

Number of extensible sets
: Input: Undirected graph $$G$$

  Output: The number of extensible sets of vertices of $$G$$.

The smallest missing induced subgraph size naturally falls into the complexity class $$\Sigma_2^P$$ of problems for which you can guess a solution (the missing subgraph) but then verifying it involves solving a co-$$\mathsf{NP}$$ problem (is this subgraph missing).
It is greater than the size of the smallest non-extensible set, because if you try to build up a given induced subgraph by adding one vertex at a time greedily you can only get stuck at a non-extensible set. There must be a missing induced subgraph of size at most $$2\log_2 n\bigl(1+o(1)\bigr)$$, because there are $$2^{\binom{k}{2}}$$ isomorphism classes of $$k$$-vertex labeled graphs and fewer than $$n^k=2^{k\log_2 n}$$ ways of choosing which of the $$k$$ labeled vertices correspond to vertices of $$G$$, so for larger values of $$k$$ than this bound there are more labeled graphs than placements of them as induced subgraphs. Another way of thinking about the smallest missing induced subgraph problem is that we are asking for the largest $$k$$ for which $$G$$ is [$$k$$-universal](https://en.wikipedia.org/wiki/Universal_graph): it contains all graphs on at most $$k$$ vertices as induced subgraphs.

The smallest non-extensible set and the smallest missing subgraph are both easy on any hereditary class of graphs, because these classes always have a missing subgraph of size $$O(1)$$. On the other hand, if $$G$$ is chosen uniformly at random among the $$n$$-vertex graphs, then any small subset of its vertices is extensible with high probability, so the smallest non-extensible set has expected size $$\log_2 n-O(\log\log n)$$.

If these problems are not $$\mathsf{NP}$$- and $$\#\mathsf{P}$$-complete, what are they? Papadimitriou and Yannakakis[^py] define a complexity class $$\mathsf{LOGNP}$$, and show that VC-dimension is $$\mathsf{LOGNP}$$-complete. Presumably, because it's so similar, the same is true for the largest extensible set. Maybe it's possible to prove completeness for the smallest missing induced subgraph in an analogue of $$\Sigma_2^P$$ at the level of $$\mathsf{LOGNP}$$, and to prove completeness for the number of shattered sets and number of extensible sets in an analogue of $$\#\mathsf{P}$$ at this level.

* Footnotes go here
{:footnotes}

[^l]: Ladner, Richard (1975), "[On the structure of polynomial time reducibility](https://doi.org/10.1145/321864.321877)", _J. ACM_ 22 (1): 155–171.

[^lmr]: Linial, Nathan, Mansour, Yishay, and Rivest, Ronald L. (1991), "[Results on learnability and the Vapnik–Chervonenkis dimension](https://doi.org/10.1016/0890-5401(91)90058-A)", _Inf. Comput._ 90 (1): 33–49.

[^mr]: Manurangsi, Pasin, and Rubinstein, Aviad (2017), "[Inapproximability of VC dimension and Littlestone’s dimension](http://proceedings.mlr.press/v65/manurangsi17a.html)", _Proc. 2017 Conf. Learning Theory (COLT 2017)_, Proceedings of Machine Learning Research 65, pp. 1432–1460.

[^py]: Papadimitriou, Christos H., and Yannakakis, Mihalis (1996), "[On limited nondeterminism and the complexity of the V–C dimension](https://doi.org/10.1006/jcss.1996.0058)", _J. Comput. Syst. Sci._ 53 (2): 161–170.