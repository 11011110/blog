---
layout: post
title: Layered pathwidth and its obstacles
date: 2018-10-22 15:00
---
There is a strong connection between the structural properties of the graphs in [minor-closed families of graphs](https://en.wikipedia.org/wiki/Graph_minor), and the properties of the graphs that are not in those families, their [forbidden minors](https://en.wikipedia.org/wiki/Forbidden_graph_characterization).
A famous example of this is the proof by [Robertson and Seymour (1986)](https://doi.org/10.1016/0095-8956(86)90030-4) that a minor-closed family of graphs has bounded [treewidth](https://en.wikipedia.org/wiki/Treewidth) if and only if at least one planar graph is not in the family. This is closely related to an earlier [theorem of Halin on grid minors in infinite graphs](https://en.wikipedia.org/wiki/Halin%27s_grid_theorem), and [Chekuri and Chuzhoy (STOC 2014)](https://arxiv.org/abs/1305.6577) have proven a polynomial relation between the treewidth and the size of the excluded planar graph.

Another result of [Robertson and Seymour (1983)](https://doi.org/10.1016%2F0095-8956%2883%2990079-5), the first in their long sequence of papers on graph minors, states that a minor-closed family of graphs has bounded [pathwidth](https://en.wikipedia.org/wiki/Pathwidth) if and only if at least one tree is not in the family. I'm less sure of the provenance, but it's also known that a minor-closed family of graphs has bounded [tree-depth](https://en.wikipedia.org/wiki/Tree-depth) if and only if at least one path is not in the family.

My own most heavily-cited non-algorithmic result (from [Algorithmica 2000](https://doi.org/10.1007/s004530010020)) has the same flavor, but is a little more complicated to explain. It states that a minor-closed family of graphs has bounded local treewidth if and only if at least one [apex graph](https://en.wikipedia.org/wiki/Apex_graph) is not in the family. An apex graph is what you get by adding one vertex to a planar graph.

{: style="text-align:center"}
![An apex graph]({{site.baseurl}}/assets/2018/apex-graph.svg)

"Bounded local treewidth" means that, for each vertex $$v$$, and each number $$d$$, the treewidth of the subgraph within distance $$d$$ of $$v$$ can be bounded by a function of $$d$$. Later, [Dujmović, Morin, and Wood (JCTB 2017)](https://doi.org/10.1016/j.jctb.2017.05.006) showed that the same is true for linear local treewidth (the function of $$d$$ is linear) and for bounded layered treewidth.
Layered treewidth is a concept defined by simultaneously choosing a [tree decomposition](https://en.wikipedia.org/wiki/Tree_decomposition) (a tree whose nodes, called bags, represent sets of vertices, with each vertex belonging to the bags of a connected subtree and each edge having both endpoints in at least one bag) and a layering (a partition of the vertices into a sequence of subsets called layers, such that each edge connects vertices in the same or consecutive layers).  The layered width of a (tree decomposition, layering) pair is the largest intersection of a bag and a layer.

In a paper with Bannister, Devanny, Dujmović, and Wood (described in [this earlier post]({{site.baseurl}}{% post_url 2015-06-30-new-preprint-on %}) and [to appear in Algorithmica](https://doi.org/10.1007/s00453-018-0487-5)) we introduced an analogous concept, layered pathwidth.
This is just the width of a (tree decomposition, layering) pair whose tree decomposition is a path of bags. In the example below, the rows of the grid are the layers, and the columns are the bags. Each vertex belongs to one layer and a contiguous subsequence of bags, and each grid cell (the intersection of a layer and a bag) contains at most two vertices. Each edge belongs to a single bag and spans at most two consecutive layers. So the layered pathwidth for this example is two.

{: style="text-align:center"}
![Layered path decomposition]({{site.baseurl}}/assets/2018/layered-path-decomp.svg)

My newest preprint, "Minor-closed graph classes with bounded layered pathwidth" (with Vida Dujmović, Gwenäel Joret, Pat Morin, and David Wood, [arXiv:1810.08314](https://arxiv.org/abs/1810.08314)) proves the same style of forbidden-minor characterization for this concept: a minor-closed family of graphs has bounded local pathwidth, linear local pathwidth, or bounded layered pathwidth if and only if at least one apex-tree is not in the family. An apex-tree is a graph like the one below formed by adding a single vertex to a tree.

{: style="text-align:center"}
![An apex tree]({{site.baseurl}}/assets/2015/ApexTree.svg)

By analogy, one would expect that the forbidden minors for bounded local tree-depth would be the fan graphs formed by adding one vertex to a path. I don't know a reference for this, but it turns out to be true! In one direction, if a minor-closed family of graphs includes all of the fans, then it includes graphs whose radius from the center of the fan is one, but whose tree-depth is logarithmic in the size of the fan (because that's the tree-depth of the path from which the fan was formed). In the other direction, I want to show that if a family of graphs excludes a $$k$$-vertex fan, then the tree-depth of its radius-$$r$$ graphs is at most $$(k-1)^r$$.

To prove this, suppose that we are given a graph such that the radius from some central vertex $$v$$ is $$r$$. Perform a depth-first search from $$v$$, and let $$\ell$$ be the length of the longest path in the depth-first search tree. Then the graph has tree-depth at most $$\ell$$, and we want to show that if $$\ell$$ is at least $$(k-1)^r$$ then the graph contains as a minor a fan with $$k$$ vertices.
If the path includes $$k-1$$ consecutive vertices at distance exactly $$r$$ from $$v$$, then the fan is easy to find: just contract all closer vertices into $$v$$. Otherwise, contract each vertex at distance $$r$$ from $$v$$ into one of its path neighbors. This compresses the path by removing groups of at most $$k-2$$ consecutive vertices,
so we get a path of $$(k-1)^{r-1}$$ vertices (other than $$v$$) that are all now at distance at most $$r-1$$ from $$v$$. Repeat, either finding enough consecutive vertices at the maximum distance or shrinking the path by a factor of $$k-1$$ and the distance by one, until eventually finding a fan. When we shrink to distance one from $$v$$, we will necessarily have found a fan, because we still have at least $$k-1$$ vertices left in the shrunken path and they are all adjacent to $$v$$.

But the tree-depth one gets from this argument is very far from linear.
And I don't know what layered tree-depth should mean, or whether (if it is defined properly) bounded layered tree-depth and bounded local tree-depth of minor-closed families are the same, as they are for treewidth and pathwidth.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/100942192280467337))