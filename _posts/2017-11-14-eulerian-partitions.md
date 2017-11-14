---
layout: post
title: Eulerian partitions
date: 2017-11-14 14:51
---
Did you know that, for every embedded planar graph, it's possible to partition the edges into two subsets, one of which forms an Eulerian subgraph of the given graph and the other of which forms an Eulerian subgraph of the dual?

Here by "Eulerian" I mean that all vertex degrees are even, but I allow disconnected subgraphs and vertices of degree zero. In fact, by Euler's formula, there must be at least two degree-zero vertices somewhere (both in the primal, both in the dual, or split between the two graphs). The dual might have self-loops or parallel edges, but the result still holds as long as we count the degree of a self-loop as being two. I also allow either of the two sets of edges in the partition to be empty.

For example, the graph of the dodecahedron can be covered by three cycles, two of length five on two opposite faces and one of length ten between them. These three cycles form an Eulerian subgraph, and the remaining ten edges give an Eulerian subgraph of the dual consisting of two 5-cycles and two isolated vertices.

{: style="text-align:center"}
![Partition of the edges of a dodecahedron into Eulerian subgraphs in the primal and dual graph]({{site.baseurl}}/assets/2017/dodec-edge-partition.png)

Probably this is an exercise in a graph theory textbook somewhere, but I don't know the reference. I also don't know a direct proof for this fact. Instead, I can show that it follows from a related Eulerian partition problem on arbitrary graphs. This time, we partition vertices instead of edges. Every graph has a partition of its vertices into two subsets such that the two subgraphs induced by these two sets are both Eulerian. For instance, here's a partition of the dodecahedron into an induced pair of 5-cycles (two opposite faces of the dodecahedron), and a complementary induced 10-cycle (the equator midway between these two faces):

{: style="text-align:center"}
![Partition of the vertices of a dodecahedron into Eulerian induced subgraphs]({{site.baseurl}}/assets/2017/dodec-vertex-partition.svg)

You can go from a vertex partition of a planar graph to an edge partition by letting the primal Eulerian subgraph of the edge partition be the union of the two induced subgraphs in the vertex partition. As you go around any face of the planar graph, the vertices must alternate between the two sides of the vertex partition, implying that the remaining edges (the ones not part of either induced subgraph) must have an even number around every face, and form an Eulerian subgraph of the dual. In the other direction, suppose you have a partition of the edges of a planar graph into Eulerian and dual-Eulerian subgraphs. Then you can 2-color the faces of the dual-Eulerian subgraph, and this 2-coloring gives you a partition of the vertices of the given graph which partitions the Eulerian side into two induced subgraphs.

Because it doesn't talk about dual graphs, the vertex partition formulation makes sense for any graph. Most small graphs are pretty easy, but it makes an amusing puzzle to find a partition into two even-degree induced subgraphs for the [Clebsch graph](https://en.wikipedia.org/wiki/Clebsch_graph), the graph you get from a four-dimensional hypercube by adding its long diagonals.

{: style="text-align:center"}
![Construction of the Clebsch graph from a hypercube]({{site.baseurl}}/assets/2017/Clebsch-hypercube.svg)

Here's an algorithm for finding Eulerian vertex partitions, and an algorithmic proof that these partitions always exist.

1. While the graph contains an odd-degree vertex $$v$$, complement the neighborhood of $$v$$ (adding an edge between every two non-adjacent neighbors, and removing the edge between every two adjacent neighbors) and then remove $$v$$ from the graph.

2. Once all remaining vertices have even degree, use the trivial vertex partition on the remaining Eulerian graph: put all vertices into one side of the partition, and make the other side be the empty set.

3. Add back the vertices that were removed, in the reverse of the removal order. For each such vertex $$v$$, after adding it back, complement the neighborhood of $$v$$ again (restoring the graph to the state it was in just prior to the removal of $$v$$) and then look at how the neighbors of $$v$$ are partitioned. Because $$v$$ has an odd total number of neighbors, one side of the partition must have an odd number of neighbors and the other side must have an even number. Place $$v$$ on the side of the partition that has an even number of neighbors.

Consider what happens to the degree of a vertex $$w$$ in its induced subgraph, when a vertex $$v$$ that has $$w$$ as its neighbor is added back to the graph. If $$w$$ is on the odd side of the partition of the neighbors of $$v$$, then complementing the neighborhood of $$v$$ will cause an even number of vertices (the other ones on the same side of the partition) to change between being induced neighbors and non-neighbors of $$w$$. Since $$w$$ had an even number of induced neighbors before this complement operation, it continues to have an even number of them after the operation. On the other hand, if $$w$$ is on the even side, complementing the neighborhood of $$v$$ will cause an odd number of vertices to change between being induced neighbors and non-neighbors of $$w$$, changing the degree of $$w$$ in its induced subgraph to change from even to odd. But then, $$v$$ will be added to the induced subgraph as a neighbor of $$w$$, causing its degree to become even again. And of course, since we added $$v$$ to the even subset of its neighbors, its own degree in the induced subgraph also becomes even. Because we have a valid Eulerian partition after step 2 and the partition remains valid after each successive step, the algorithm terminates with a valid partition of the whole graph.

This is vaguely reminiscent of [an unpublished paper on counting spanning trees](http://www.ics.uci.edu/~eppstein/pubs/Epp-TR-96-14.pdf) that I wrote some years ago. In that paper, I connected the spanning tree counting problem to the existence of a different kind of Eulerian vertex partition: a partition such that the subgraph of edges that connect one side of the partition to the other should have even degree everywhere. These kinds of partitions don't always exist, but the paper showed that they exist if and only if the graph has an even number of spanning trees. It makes me wonder whether there's a stronger connection here than just vague resemblance, and whether there's some interesting structure to the set of all Eulerian partitions of a graph.