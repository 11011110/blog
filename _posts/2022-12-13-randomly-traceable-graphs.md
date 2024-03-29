---
layout: post
title: Randomly traceable graphs
date: 2022-12-13 11:41
---
In my recently-concluded graph algorithms course, one of my early homework assignments asked about undirected graphs with the following property: any oriented path that does not cover all vertices can be extended to form a Hamiltonian path. I phrased it in terms of depth-first search: which graphs have the property that, no matter where you start and no matter what order you explore the neighbors of each node, a depth first search tree will automatically produce a Hamiltonian path? The intent was to reinforce the idea that the same graph can have multiple depth first search trees depending on contingent issues of how the graph is represented. I called these "unicursal graphs".

This is also closely related to [some research I published in WADS 2019 on reconfiguring paths in graphs]({{site.baseurl}}{% post_url 2019-05-02-playing-model-trains %}), although in that work I was focusing on whether all paths of a certain length could be connected to each other by local moves and here the question is merely whether any path could be a dead end without any possible moves.

The homework asked only for an example of a graph that was unicursal but not complete. I had in mind two possibilities, the cycle graphs and the balanced complete bipartite graphs. One of the students in the graduate section of the class, Alvin Chiu, took the problem and ran with it, eventually proving that these are the only examples. Unfortunately, he also discovered that the result was in the literature already: Gary Chartrand and Hudson V. Kronk (1968), "Randomly traceable graphs", _SIAM J. Appl. Math._ 16 (4): 696–700, [doi:10.1137/0116056](https://doi.org/10.1137/0116056).

I think it's a cute result that deserves to be more widely known, so I thought I'd outline a proof here.

* The defining property is that any path can be extended to a Hamiltonian path. If you remove the first edge of a Hamiltonian path and extend the rest, the only possibility is to return to the first vertex of the initial path, by an edge that completes it to form a Hamiltonian cycle. So every path can be extended one step farther, to a Hamiltonian cycle.

* Find any cycle in your graph. If that is the whole graph, you have one of the three possibilities in the classification of these graphs; otherwise, it has at least one diagonal. By drawing an S-shaped path through this diagonal and around your starting cycle, and then completing it to another cycle, you can show that the graph must include a rotated copy of the diagonal. By repeating this operation you can show that it includes every rotated copy of every diagonal, and therefore that it forms a [circulant graph](https://en.wikipedia.org/wiki/Circulant_graph), a graph whose symmetries include a cyclic rotation of all the vertices.

  {: style="text-align:center"}
![Case analysis for randomly traceable graphs. Left: completion of an S-shaped path through the diagonal of a Hamiltonian cycle shows the existence of a rotated copy of the diagonal. Right: completion of a C-shaped path skipping the apex of a triangle shows that all vertices are adjacent to the apex.]({{site.baseurl}}/assets/2022/unicursal-cases.svg)

* If the graph contains a triangle, then (by extending the path through two sides of the triangle) you can arrive at a situation where the triangle is formed by three consecutive vertices of your Hamiltonian cycle, and includes a diagonal skipping the center vertex of the three. By drawing C-shaped paths around the cycle that use this diagonal to skip the center vertex, and then completing these paths to cycles, you can show that this center vertex is [universal](https://en.wikipedia.org/wiki/Universal_vertex): it has edges to everything else. By the circulant symmetry of the graph, it must be complete, the second of the three possibilities in the classification of these graphs.

* In the remaining case, any diagonal of a Hamiltonian cycle and its rotated copy form a four-vertex cycle. As in the previous case, by extending a path through three sides of the cycle you can arrive at a situation where some four-vertex cycle is formed by four consecutive vertices of a Hamiltonian cycle. A similar argument involving C-shaped paths shows that the two central vertices of the 4-cycle are adjacent to all other vertices, and by symmetry every two consecutive vertices of the Hamiltonian cycle are adjacent to all other vertices. This implies that there are at least $$n^2/4$$ edges, and by [Mantel's theorem](https://en.wikipedia.org/wiki/Mantel's_theorem) the graph can only be a balanced complete bipartite graph, the third of the three possibilities.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/109508139457197936))