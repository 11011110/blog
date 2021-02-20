---
layout: post
title:  Loops, degrees, and matchings
date:   2021-02-19 18:57
---
A student in my graph algorithms class asked how [self-loops](Loop (graph theory)) in undirected graphs affect the vertex degrees and matchings of a graph. The standard answer is that a self-loop adds two to the degree (because each edge has two endpoints) and that they are useless in matching because matchings should have at most one incidence to each vertex, not two. But that's just a convention; one could reasonably declare that the contribution of a self-loop to the degree is one, and I'm pretty sure I've seen sources that do just that. With that alternative convention, it should be possible to include a self-loop in a matching, and use it to match only a single vertex.

However, this turns out not to make much difference to many matching problems, because the following simple transformation turns a problem with self-loops (allowed in matchings in this way) into a problem with no self-loops (so it doesn't matter whether they are allowed or not). Simply form a [double cover](https://en.wikipedia.org/wiki/Covering_graph)$$^*$$ of the given graph (let's call it the "loopless double cover") by making two copies of the graph and replacing all corresponding pairs of loops by simple edges from one copy to the other. In weighted matching problems, give the replacement edges for the loops the sum of the weights of the two loops they replace; all other edges keep their original weights.

{: style="text-align:center"}
![The loopless double cover of a graph and of one of its loopy matchings]({{site.baseurl}}/assets/2021/loopless-double-cover.svg)

Then (unlike the [bipartite double cover](https://en.wikipedia.org/wiki/Bipartite_double_cover), which also eliminates loops) the cardinality or optimal weight of a matching in the loopy graph can be read off from the corresponding solution in its loopless double cover. Any matching of the original loopy graph can be translated into a matching of the loopless cover by applying the same loopless cover translation to the matching instead of to the whole graph; this doubles the total weight of the matching and the total number of matched vertices. And among matchings on the loopless cover, when trying to optimize weight or matched vertices, it is never helpful to match the two copies differently, so there is an optimal solution that can be translated back to the original graph without changing its optimality.

This doesn't quite work for the problem of finding a matching that maximizes the total number of matched edges, rather than the total number of matched vertices. These two problems are the same in simple graphs, but different in loopy graphs. However, in a loopy graph, if you are trying to maximize matched edges, you might as well include all loops in the matching, and then search for a maximum matching of the simple graph induced by the remaining unmatched vertices. Again, in this case, you don't get a problem that requires any new algorithms to solve it.

In the case of my student, I only provided the conventional answer, because really all they wanted to know was whether these issues affected how they answered one of the homework questions, and the answer was that the question didn't involve and didn't need loops. However it seems that the more-complicated answer is that even if you allow loops to count only one unit towards degree, and to be included in matchings, they don't change the matching problem much.

$$^*$$ This is only actually a covering graph under the convention that the degree of a loop is one. For the usual degree-2 convention for loops, you would need to replace each loop by a pair of parallel edges, forming a multigraph, to preserve the degrees of the vertices.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/105762400402127534))