---
layout: post
title: Stretch, average stretch, and expected stretch of spanning trees
date: 2020-04-19 18:10
---
The graph below is a [series-parallel graph](https://en.wikipedia.org/wiki/Series-parallel_graph). It can be put together from four smaller series-parallel graphs, each constructed recursively in the same way, by performing a series composition of two pairs and then a parallel composition of the two results.

{: style="text-align:center"}
![Series-parallel graph for which all spanning trees have high stretch]({{site.baseurl}}/assets/2020/binserpar.svg)

This family of graphs (although not the radial layout I'm using for it) comes from a paper "Cuts, trees and $$\ell_1$$-embeddings of graphs", by Anupam Gupta, Ilan Newman, Yuri Rabinovich, and Alistair Sinclair, _Combinatorica_ 2004, [doi:10.1007/s00493-004-0015-x](https://doi.org/10.1007/s00493-004-0015-x) (see Figure 3, p. 261). They used it to show a lower bound on the average stretch of any spanning tree for these graphs.

Here, given a graph $$G$$, any edge $$e$$ of $$G$$, and any subgraph $$H$$ of $$G$$, the stretch of $$e$$ with respect to $$H$$ is how much farther you have to go in $$H$$ to find a path connecting the endpoints of $$e$$, relative to the unit distance between these endpoints in $$G$$. For instance, in a cycle graph $$C_n$$, every spanning tree is formed by deleting one edge from the cycle. The deleted edge has stretch $$n-1$$ (you have to go the long way around to connect its endpoints), but all other edges have stretch $$1$$, so the average stretch is $$2(n-1)/n<2$$. More strongly, if you choose the edge to delete randomly, the resulting distribution over spanning trees of $$C_n$$ gives every edge expected stretch $$2(n-1)/n<2$$.

But for the series-parallel graphs of Gupta, Newman, Rabinovich, and Sinclair, such low stretch is not possible. If there are $$n$$ vertices, then there are $$m=\tfrac{3}{2}n-2$$ edges. Each edge has stretch at least one.
There are $$m/4$$ four-cycles, each of which has at least one missing edge,
with stretch at least three; added to the one unit of stretch that we've already counted, the extra stretch from these missing edges is at least $$m/2$$.
Removing one edge from each four-cycle leaves $$m/16$$ eight-cycles, each of which has at least one more missing edge. The edge that is removed in this way, and the other missing edge from the same four-cycle, have stretch at least seven, adding another ten units per eight-cycle, or $$10m/16$$ overall, to the total stretch. And so on; at each level of recursion the number of cycles goes down by a factor of four, but the number of edges that need to be cut to break each cycle doubles, as does their length. Therefore, the contribution per level of the recursive construction ends up being linear, and the total stretch is $$\Omega(n\log n)$$. Thus, as Gupta et al. show, the average stretch for their graphs is $$\Omega(\log n)$$.

This result is the background to my newest preprint, "Low-stretch spanning trees of graphs with bounded width" (with Cora Borradaile, Erin Chambers, Will Maxwell, and Amir Nayyeri, [arXiv:2004.08375](https://arxiv.org/abs/2004.08375), to appear at SWAT). From the result of Gupta, we know that having bounded treewidth is not enough to ensure bounded average stretch, or bounded expected stretch. What is? We show that bounded bandwidth is enough to find a distribution over spanning trees with bounded expected stretch, and that bounded cutwidth is enough to find a single spanning tree with bounded average stretch.

This leaves open the question for pathwidth. It was known from another previous work, "Pathwidth, trees, and random embeddings" (James Lee and Tasos Sidiropoulos, _Combinatorica_ 2013, [doi:10.1007/s00493-013-2685-8](https://doi.org/10.1007/s00493-013-2685-8)) that graphs of bounded pathwidth can be mapped to a random distribution over trees with bounded expected stretch per edge, but the trees of this distribution are not spanning trees. Our new paper includes a conjecture that bounded-pathwidth graphs have distributions over spanning trees with constant average stretch, which if true would generalize our results for both bandwidth and cutwidth.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/104028326751044483))