---
layout: post
title: Laminar 3-separators
date: 2018-10-20 17:20
---
My upcoming SODA paper with Bruce Reed, "Finding Maximal Sets of Laminar 3-Separators in Planar Graphs in Linear Time", is now online as [arXiv:1810.07825](https://arxiv.org/abs/1810.07825). It's about algorithms that work only on planar graphs, but one of its main motivations is as a subroutine in a different algorithm for a problem on non-planar graphs. How can that be?

First, maybe I should say something about what the paper itself is about.
In very rough terms, it's about finding tree-like structures of highly connected pieces in graphs that, overall, are not as well connected. We can measure the connectivity of a graph by its [vertex connectivity](https://en.wikipedia.org/wiki/K-vertex-connected_graph), the number of vertices you need to remove to disconnect the rest of the graph. A graph is $$k$$-vertex-connected if this number is at least $$k$$.

If a graph is $$1$$-connected but not $$2$$-connected, we can partition its edges into subsets called _blocks_ or _biconnected components_, by declaring two edges to be equivalent when they belong to a simple cycle. Each of these subsets of edges forms a $$2$$-connected subgraph (possibly just a single edge), and they meet each other at single vertices called _articulation vertices_. These subgraphs have a tree-like structure called the _block-cut tree_, a tree whose nodes are the blocks and the articulation vertices and whose edges connect blocks to their articulation vertices. Here's an illustration from Wikipedia (not by me):

{: style="text-align:center"}
![The blocks of a 1-connected graph. CC-BY image File:Graph-Biconnected-Components.svg by Zyqqh from Wikimedia Commons]({{site.baseurl}}/assets/2018/block-cut.svg)

Similarly, when a graph is $$2$$-connected but not $$3$$-connected, there's a tree-like structure called the [SPQR tree](https://en.wikipedia.org/wiki/SPQR_tree) that describes it.
The nodes of the SPQR tree are labeled by smaller graphs of one of three types (cycles, two-vertex multigraphs, or other $$3$$-connected graphs), and the original graph is constructed by gluing these smaller graphs together along shared edges and then deleting the glue edges. Every $$2$$-vertex separator is a glue edge in this structure, and it also encodes other useful information like (in the case that the underlying graph is planar) all the planar embeddings of the graph.

{: style="text-align:center"}
![SPQR tree]({{site.baseurl}}/assets/2018/spqr.svg)

For edge connectivity, this tree-like structure goes all the way up, to all values of $$k$$, using the [Gomory–Hu tree](https://en.wikipedia.org/wiki/Gomory%E2%80%93Hu_tree), but for vertex connectivity it gets messy quickly.
For graphs that are $$3$$-connected but not $$4$$-connected, we don't know of a nice uniquely-determined tree structure that describes all of the $$3$$-vertex separators. So we relaxed our goals a little and just asked for some of the $$3$$-vertex separators, all of the ones that we can fit into a single tree-like structure. More precisely, two separators are _laminar_ when each of the two subgraphs from one separator is either a subgraph or a supergraph of one of the two subgraphs from the other separator. What we're looking for is a set of cutsets that (like the four red and blue cutsets in the graph below) are all laminar with each other, but non-laminar with all the other non-chosen cutsets.

{: style="text-align:center"}
![Laminar 3-cutsets in a planar graph]({{site.baseurl}}/assets/2018/laminar.svg)

It turns out that we can list all $$3$$-cutsets, and all non-laminar pairs of $$3$$-cutsets, in time linear in the total number of cutsets and pairs, by adapting [an old algorithm of mine for subgraph isomorphism](https://doi.org/10.7155/jgaa.00014). We could then just look for a maximal independent set in a graph describing all non-laminar pairs.
But this can go badly wrong in some cases, like the [wheel graphs](https://en.wikipedia.org/wiki/Wheel_graph), which have quadratically many $$3$$-cutsets and quartically many non-laminar pairs.

{: style="text-align:center"}
![Non-laminar 3-cutsets in a wheel]({{site.baseurl}}/assets/2018/non-laminar.svg)

Fortunately, wheel-like subgraphs are the only thing that can go wrong, and when they exist, we can use them to divide the problem into subproblems. So the overall algorithm uses the same subgraph isomorphism algorithm to find wheel-like subgraphs, uses these subgraphs to divide the problem into subproblems where the wheels are all too small to cause any harm, constructs the non-laminarity graph in each subproblem, and looks for a maximal independent set in each such graph. In this way, we can find a maximal laminar family of $$3$$-cutsets in any planar graph in linear time.

We were looking at this because of some work Reed had done involving disjoint paths in graphs. But the even-more-indirect motivation involves nonplanar generalizations of the [planar separator theorem](https://en.wikipedia.org/wiki/Planar_separator_theorem), according to which every $$n$$-vertex planar graph can be partitioned into two pieces of roughly equal size by removing only $$O(\sqrt n)$$ vertices. There are lots of methods for finding these separators, and one of the original methods, by [Lipton and Tarjan in 1979](https://doi.org/10.1137/0136016), already leads easily to linear time algorithm for constructing them. More strongly, a recursive hierarchy of separators can be constructed in linear time as well, by [an algorithm of Mike Goodrich from 1995](https://doi.org/10.1006/jcss.1995.1076) that he needed for a parallel polygon triangulation algorithm.

The existence of separators of square root size has been generalized to every [minor-closed graph family](https://en.wikipedia.org/wiki/Graph_minor) by [Kawarabayashi and Reed (FOCS 2010)](https://doi.org/10.1109/FOCS.2010.22), but with a construction algorithm whose running time is $$O(n^{1+\epsilon})$$ for every $$\epsilon>0$$ rather than truly linear. Working with Zhentao Li, Kawarabayashi and Reed have announced a faster algorithm "in a forthcoming paper", but to achieve this they needed a subroutine for finding pairs of vertex-disjoint paths between two pairs of terminal vertices, in arbitrary graphs. They solve this disjoint paths problem in linear time (shaving an inverse-Ackermann factor from previous algorithms by Tholey) in a 2015 preprint, "Connectivity Preserving Iterative Compaction and Finding 2 Disjoint Rooted Paths in Linear Time" ([arXiv:1509.07680](https://arxiv.org/abs/1509.07680)). This preprint, in turn, uses the results from my new paper as a subroutine. (The weird timing of a 2015 preprint that uses results from a 2018 paper happened because it took Bruce and I a long time between being confident in our results and writing them up to the point where we felt comfortable publishing them.)

So anyway, how to find two disjoint paths between specified pairs of vertices? I don't think I can do justice to an 84-page paper in a blog post, so I'll just highlight a few key ideas. Kawarabayashi, Li, and Reed develop a [certifying algorithm](https://en.wikipedia.org/wiki/Certifying_algorithm), one that produces a proof that its answer is correct. When the paths exist, the proof can be just the two paths themselves. When they do not exist, it is a graph formed
by adding to the given graph a wheel whose four outer vertices are the four terminals, in alternating order, and then simplified by finding sets of up to three vertices that cut the wheel from the rest of the graph and replacing the part on the other side of the cutset by a complete graph on the cut vertices. If this proof graph is planar, then the two paths cannot exist, because together with the wheel they would form a $$K_5$$ subdivision.

{: style="text-align:center"}
![K5 subdivision caused by adding a wheel to two disjoint paths, and simplification by replacing subgraphs that are cut off by at most three vertices by cliques]({{site.baseurl}}/assets/2018/k5-subdivision.svg)

Their algorithm works by contracting edges of the given graph (not including edges between pairs of terminal vertices) to form a minor whose size is a constant fraction of the original graph, recursively finding an answer and a proof of the answer in the contracted graph, and then uncontracting and extending the answer to the original graph. If a pair of disjoint paths is found at any level of the recursion, it is straightforward to uncontract them into disjoint paths of the original problem. So the tricky part of the uncontraction step arises when the contracted graph has been reduced to a planar proof graph. My new preprint is used to provide some structure to the planar proof graph in this case. This structure is then used by Kawarabayashi, Li, and Reed in the uncontraction step, to show how to find either another planar proof graph or a pair of disjoint paths in the uncontracted graph.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/100930801764588334))