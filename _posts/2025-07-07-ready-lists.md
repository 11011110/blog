---
layout: post
title: Ready lists
date: 2025-07-07 21:35
---
Beginning computer science students learn about stacks, queues, and priority queues, different ways of organizing and ordering a collection of tasks to be performed. But more basic than any of those, and less frequently taught and formalized, is the _ready list_, a collection of tasks to be performed whose ordering is not important. All it needs to do is to allow new tasks to be added to the collection and to find and remove an arbitrary task from the collection.

Standard algorithms that work with ready lists include:

Reachability

: Input: a directed or undirected graph and a starting vertex in the graph

: Output: the set of vertices that can be reached from the starting vertex

: Algorithm:
  * Initialize a set of reachable vertices, and a ready list of reachable but unprocessed vertices, both initially containing only the starting vertex.
  * While the ready list is non-empty:
    * Find and remove a vertex $$v$$ from the ready list
    * For each outgoing neighbor $$w$$ of $$v$$ that is not already in the reachable set, add $$w$$ to both the reachable set and the ready list.
  * Return the reachable set

Topological ordering

: Input: a directed acyclic graph

: Output: a sequence of vertices, ordered so all edges go from earlier to later in the ordering

: Algorithm:
  * Initialize a ready list of vertices with no incoming edges
  * While the ready list is non-empty:
    * Find and remove a vertex $$v$$ from the ready list
    * Delete $$v$$ from the graph and output $$v$$
    * Add to the ready list any former neighbor of $$v$$ which, after the deletion, has no more incoming edges

Stable matching

: Input: A set of job applicants and a set of employers, with each applicant having a preference ordering among the employers and each employer having a preference ordering among the applicants

: Output: A stable matching

: Algorithm:
  * Initialize a ready list of job offers from each employer to its top applicant
  * While the ready list is non-empty:
    * Find and remove an offer from employer $$X$$ to applicant $$A$$
    * If $$A$$ prefers their current situation over $$X$$, add to the ready list a new job offer from $$X$$ to $$X$$'s next applicant.
    * Otherwise, match $$A$$ and $$X$$; if $$A$$ was previously matched, remove that match and add to the ready list a new job offer from $$A$$'s previous employer to its next applicant

In the cases of reachability and stable matching, the ordering chosen by the ready list is unimportant: you will always get the same reachable set and the same matching. In the case of topological ordering, you may get different orderings but regardless of order you will always output the same set of vertices for any given graph, even if the graph is not acyclic.

This invariance is usually proven algorithm-by-algorithm, but it is true very generally for a class of algorithms with three simple properties: First, an item that is added to the ready list stays there until it is processed. Second, each item is added to the ready list only once. And third, the condition for adding an item to the ready list should be a monotonic combination of which other items have already been processed: if a certain combination of processed items triggers an addition, then any superset of the same combination should trigger the same addition. The trigger for reachability is that some neighbor is processed, and the trigger for topological ordering is that all incoming neighbors are processed. For stable matching, the trigger for an offer from $$X$$ to $$A$$ is that $$X$$'s previous applicant has already received both an offer from $$X$$ and an offer from another employer that they prefer over $$X$$.

These three properties are enough to prove that the sequences in which items can be processed by an algorithm of this type form an [antimatroid](https://en.wikipedia.org/wiki/Antimatroid). The key axiom of antimatroid sequences that we need to prove is that, if two sequences $$S$$ and $$T$$ can both be generated, and $$S$$ contains an item not in $$T$$, then $$S$$ contains an item $$x$$ that can be processed next after $$T$$, producing a sequence $$Tx$$. To prove this, simply let $$x$$ be the first item that belongs to $$S$$ but not $$T$$, and apply the monotonic trigger property.

In any antimatroid, all sequences that cannot be extended consist of the same set of items. Again, this is easy to prove: if two sequences had different sets of items, then one would contain an item by which the other could be extended. To translate this into terms more familiar to the beginning computer science students: if a ready list obeys the three properties given above, and we run an algorithm using it until the ready list becomes empty, then all runs of the algorithm process the same set of items.

While exploring this I ran into another basic algorithm that in its usual form is based on integer priority queues but can be transformed into a ready list algorithm:

Degeneracy

: Input: An undirected graph

: Output: A subgraph whose minimum degree is as large as possible

: Algorithm:
  * Initialize an empty ready list
  * While the graph is non-empty:
    * If the ready list is empty, set $$d$$ to the minimum degree in the graph, set $$S$$ to be an empty set, and add to the ready list all vertices of degree $$d$$
    * Find and remove a vertex $$v$$ from the ready list
    * Delete $$v$$ from the graph and add $$v$$ to $$S$$
    * Add to the ready list any former neighbors of $$v$$ for which this removal decreases the degree to $$\le d$$
  * Output the subgraph induced in the original input graph by $$S$$

This can be made to run in linear time but the details of that are beyond the scope of this post. Proving monotonicity of the condition for triggering addition to the ready list is a little less obvious here. For each integer $$k$$ we can define a subgraph called the $$k$$-core, the union of all subgraphs whose minimum degree is at least $$k$$. The output is the $$d$$-core. The monotonic trigger for any vertex $$v$$ to be added to the ready list is that all vertices not in the $$k$$-core have already been processed, where $$k$$ is the largest value for which the $$k$$-core contains $$v$$, and that $$v$$ has at most $$k$$ unprocessed neighbors.

Abstractly, the decreasing degrees of the vertices can be seen as a kind of element quality that decreases as other elements are removed; we seek the subset maximizing the minimum quality of any of its elements. My latest preprint, "Decremental greedy polygons and polyhedra without sharp angles" ([arXiv:2507.04538](https://arxiv.org/abs/2507.04538), to appear at this year's Canadian Conference on Computational Geometry) looks at a general class of problems like this, and identifies several more. One of the simplest of these is to find a polygon through a subset of the points that maximizes the minimum interior angle.

{: style="text-align:center"}
![A set of points spaced roughly evenly on four crossing circles, and its max-min angle polygon, the 24 points on one of the circles]({{site.baseurl}}/assets/2025/maxmin-angle.svg){: style="width:100%;max-width:720px" }

So here is the algorithm; I think the similarities between this and the degeneracy algorithms are obvious.

Max-min angle polygon

: Input: A set of points in $$\mathbb{R}^2$$

: Output: A polygon with the points as vertices whose sharpest angle is as large as possible

: Algorithm:
  * Initialize an empty ready list
  * While the set of points is non-empty:
    * If the ready list is empty, set $$\theta$$ to the minimum angle of a convex hull vertex of the remaining points, set $$S$$ to be an empty set, and add to the ready list all convex hull vertices of angle $$\theta$$
    * Find and remove a point $$p$$ from the ready list
    * Delete $$p$$ from the points and add $$p$$ to $$S$$
    * Add to the ready list any convex hull vertices for which this removal decreases the angle to $$\le\theta$$
  * Output the convex hull of $$S$$

This can be made to run in time $$O(n\log n)$$; for details see the preprint. I'll finish with one more from the full version of the paper, on cycles in directed graphs.

Bottleneck cycle

: Input: A directed graph with weighted edges

: Output: A cycle whose minimum edge weight is as large as possible

: Algorithm:
  * Initialize a ready list of the edges out of all vertices that have no incoming edges, and the edges into all vertices that have no outgoing edges
  * Initialize an empty set $$S$$
  * While the set of graph edges is non-empty:
    * If the ready list is empty, set $$w$$ to the minimum weight of a remaining edge, set $$S$$ to be an empty set, and add to the ready list all edges of weight $$w$$
    * Find and remove an edge $$(u,v)$$ from the ready list
    * Delete edge $$(u,v)$$ from the graph and add it to $$S$$
    * If $$u$$ has no more outgoing edges, add to the ready list all its incoming edges.
    * If $$v$$ has no more incoming edges, add to the ready list all its outgoing edges.
  * Find and output any cycle in the subgraph of edges in $$S$$

For this one, a direct implementation on a graph with $$n$$ vertices and $$m$$ edges would take time $$O(m\log n)$$, not really better than the obvious binary search. However, it can be made to run in linear time for graphs with edges already sorted by length, and this presorted version can be used as a subroutine in a different algorithm for graphs with unsorted edges, in time $$O(m\log^* n)$$. In turn, bottleneck cycles can be used as a subroutine in an algorithm for finding the max-min angle closed polygonal curve for 3d points, allowing the curve to pass repeatedly through points and segments, in time $$O(n^3\log^* n)$$. For details see the preprint.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/114815823766596754))