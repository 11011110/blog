---
layout: post
title: The graphs of stably matchable pairs
date: 2020-10-19 20:29
---
The [stable matching problem](https://en.wikipedia.org/wiki/Stable_marriage_problem) takes as input the preferences from two groups of agents (most famously medical students and supervisors of internships), and pairs up agents from each group in a way that encourages everyone to play along: no pair of agents would rather go their own way together than take the pairings they were both given. A solution can always be found by the [Gale–Shapley algorithm](https://en.wikipedia.org/wiki/Gale%E2%80%93Shapley_algorithm), but there are generally many solutions, described by the [lattice of stable matchings](https://en.wikipedia.org/wiki/Lattice_of_stable_matchings). Some pairs of agents are included in at least one stable matching, while some other pairs are never matched. In this way, each instance of stable matchings gives rise to a graph, the _graph of stably matchable pairs_. This graph is the subject and title of my latest preprint, [arXiv:2010.09230](https://arxiv.org/abs/2010.09230), which asks: Which graphs can arise this way? How hard is it to recognize these graphs, and infer a stable matching instance that might have generated them? How does the graph structure relate to the lattice structure?

For some answers, see the preprint. One detail is connected to [my previous post, on polyhedra with no two disjoint faces]({{site.baseurl}}{% post_url 2020-10-18-polyhedra-without-disjoint %}) (even though there are no polyhedra in the new preprint): the (prism,$$K_{3,3}$$)-minor-free graphs discussed there come up in proving an equivalence between outerplanar graphs of stably matchable pairs and lattices of [closures](https://en.wikipedia.org/wiki/Closure_problem) of [oriented trees](https://en.wikipedia.org/wiki/Polytree). Instead of providing any technical details of any the other results in the paper, though, I thought it would be more fun to show a few visual highlights.

The following figure shows a cute mirror-inversion trick (probably already known, although I don't know where or by whom) for embedding an arbitrary bipartite graph as an induced subgraph of a regular bipartite graph. I use it to show that graphs of stably matchable pairs have no forbidden induced subgraphs:

{: style="text-align:center"}
![Embedding a bipartite graph as an induced subgraph of a regular bipartite graph]({{site.baseurl}}/assets/2020/regularize.svg){: width="60%" }

This next one depicts a combinatorial description of a stable matching instance having a $$6\times 5$$ grid as its graph, in terms of the top and bottom matchings in the lattice of matchings, the "rotations" that can be used to move between matchings in this lattice, and a partial order on the rotations. For what I was doing in this paper, these rotation systems were much more convenient to work with than preferences.

{: style="text-align:center"}
![Rotation system describing a system of stable matchings having a 6x5 grid as its graph]({{site.baseurl}}/assets/2020/5x6.svg){: width="80%" }

All the main ideas for a proof of NP-completeness of recognizing these graphs, by reduction from [not-all-equal 3-satisfiability](https://en.wikipedia.org/wiki/Not-all-equal_3-satisfiability), are visible in the next picture. The proof now in the paper is significantly more complicated, though, because the construction in this image produces nonplanar graphs but I wanted a proof that would also apply in the planar case.

{: style="text-align:center"}
![NP-completeness reduction from NAE3SAT to recognizing graphs of stably matchable pairs]({{site.baseurl}}/assets/2020/nae3sat-to-matching.svg)

The last one shows a sparse graph that can be represented as a graph of stably-matching pairs (because it's outerplanar, bipartite, and biconnected) but has a high-degree vertex. If we tried to test whether it could be realized by doing a brute-force search over preference systems, the time would be factorial in the degree, but my preprint provides faster algorithms that are only singly exponential in the number of edges.

{: style="text-align:center"}
![Outerplanar graph of stably matchable pairs with a factorial number of potential preference systems]({{site.baseurl}}/assets/2020/factorial.svg)
