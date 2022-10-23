---
layout: post
title: Repeated vertices in TSP tours
date: 2022-10-22 17:22
---
This week my graph algorithms course covered the traveling salesperson problem, which I usually describe in two equivalent forms:

- Given a distance matrix representing a metric space, find a cycle that passes through each point of the space exactly once, of minimum total length

- Given a connected positively-weighted undirected graph, find a closed walk that passes through each vertex at least once, of minimum total length

To go from a distance matrix to a graph, we just use the complete graph, and skip any repeated vertices in its closed walk. To go from a graph to a distance matrix, compute all pairs shortest distances, and then form a closed walk by concatenating the shortest paths between consecutive vertices of the non-repeating cycle. But this concatenation may create many unavoidable repeated vertices. For instance, if your graph is an <span style="white-space:nowrap">$$n$$-vertex</span> star, then any closed walk through all the vertices must return to the central vertex $$n-1$$ times, like the blue curve past all of the vertices in the nine-vertex star below.

{: style="text-align:center"}
![A closed walk through all vertices of the star $$K_{1,8}$$ visits the central vertex eight times.]({{site.baseurl}}/assets/2022/star-tour.svg)

It occurred to me to wonder: how many repetitions might be necessary, in total? The multigraph of edges used by the closed walk (with one copy for each time the walk uses each edge) is Eulerian, meaning that it connects all the vertices and has even degree at all of them. Any Eulerian multigraph has a closed walk visiting all the vertices, its Euler tour. Among these graphs, the TSP multigraph must be minimal: if it had an Eulerian subgraph we could walk on that instead. And any minimal Eulerian multigraph can be turned into a simple graph and weighted in such a way that all edges are used with their given multiplicities in the optimal TSP walk. So another, more combinatorial, way of asking the same question is: how many edges can a minimal Eulerian multigraph have?

The answer: <span style="white-space:nowrap">$$2n-2$$.</span> More precisely, a graph is said to be [$$(a,b)$$-sparse](https://en.wikipedia.org/wiki/Dense_graph) if every <span style="white-space:nowrap">$$k$$-vertex</span> subgraph has at most $$ak-b$$ edges. In this sense, the minimal Eulerian graphs are <span style="white-space:nowrap">$$(2,2)$$-sparse.</span>

If you were given an Eulerian graph that is not <span style="white-space:nowrap">$$(2,2)$$-sparse,</span> it could not be minimal Eulerian. To see this, choose a minimal subset of $$k$$ vertices that has more than $$2k-2$$ edges. By deleting edges, you can find a subgraph that is <span style="white-space:nowrap">$$(2,2)$$-tight:</span> it has exactly $$2k-2$$ edges, and every subgraph is <span style="white-space:nowrap">$$(2,2)$$-sparse.</span> A result of Nash-Williams from the 1960s states that a subgraph like this can always be decomposed into two spanning trees. But if you combine one of the deleted edges with a path between its endpoints in one of the trees, you get a cycle that you can remove without changing the parity of the vertex degrees. Removing this cycle still leaves a subgraph that is connected through the other spanning tree. Because there is a cycle you can remove leaving an Eulerian subgraph, your starting graph is not minimal.

The bound of $$2(n-1)$$ on the number of edges in a minimal Eulerian multigraph cannot be made any smaller. One way to construct a minimal Eulerian multigraph with exactly this many edges (maybe the only way) is just to double all of the edges in a tree.

Instead of counting edges, another way to define sparse graphs involves forbidden [shallow minors](https://en.wikipedia.org/wiki/Shallow_minor). However, this does not work for minimal Eulerian graphs: they have no forbidden shallow minors. For instance, if you subdivide the edges of any Eulerian graph, such as a complete graph on an odd number of vertices, you will get a minimal Eulerian graph that has the complete graph as a depth-1 minor.

{: style="text-align:center"}
![Subdividing the edges of the complete graph $$K_7$$ produces a minimal Eulerian graph with $$K_7$$ as a 1-shallow minor.]({{site.baseurl}}/assets/2022/subdivided-K7.svg)

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/109214811068499556))