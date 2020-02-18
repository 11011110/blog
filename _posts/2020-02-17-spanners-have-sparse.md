---
layout: post
title: Spanners have sparse crossings
date: 2020-02-17 18:01
---
In a [2017 SIGSPATIAL paper](https://arxiv.org/abs/1709.06113) with Sid Gupta, Sid and I [modeled non-planar road networks as graph drawings whose edges intersect sparsely, and showed that this implies that these graphs have small separators]({{site.baseurl}}{% post_url 2017-09-19-graphs-with-sparse %}), allowing algorithms designed for planar graphs (such as linear-time shortest paths) to be extended to them. My latest preprint, with UCI student Hadi Khodabandeh, uses similar ideas of sparse edge intersections to show that [greedy geometric spanners](https://en.wikipedia.org/wiki/Greedy_geometric_spanner) also have small separators. The paper is ["On the edge crossings of the greedy spanner" (arXiv:2002.05854)](https://arxiv.org/abs/2002.05854).

Here, a spanner is a graph whose vertices are a given finite set of points in the plane, with the property that shortest paths in the graph (with distance measured geometrically along each edge) are a good approximation to shortest paths in the plane, the straight line segments between two given points. The graph is not allowed to have extra vertices, and we don't care about distances between points that are not in the given set. These things have all sorts of applications, for instance in approximation algorithms (you can approximate a geometric problem involving distances by solving a graph problem on the spanner). Of course, a [complete graph](https://en.wikipedia.org/wiki/Complete_graph) is a spanner in this sense, but it has a lot of edges. We'd like spanners that are sparser, and still accurately approximate all the distances.

You can get a constant-factor approximation with some planar graphs (like the Delaunay triangulation), and planar graphs are sparse and have [good separators](https://en.wikipedia.org/wiki/Planar_separator_theorem), among other properties. But the example of four points in a square shows that to get a distance ratio better than $$\sqrt 2$$ we need to allow edges to cross each other. A standard way of doing this is to use a greedy algorithm: just consider all pairs of points, in order, and add an edge when the graph you've built so far doesn't include a short-enough path between them. For any target distance ratio, this turns out to give spanners that are sparse (a linear rather than quadratic number of edges, and more strongly having bounded degree at each vertex) and low weight (within a constant factor of the minimum spanning tree). Versions of these spanners can be constructed in near-linear time, and work in Euclidean spaces of any bounded dimension.

Here, for instance, is a greedy spanner of 100 random points with distance ratio 2 (big enough that, in this example, there are no crossings):

{: style="text-align:center"}
![Greedy spanner with distance ratio 2]({{site.baseurl}}/assets/2020/greedy2.svg)

And here is a much more accurate greedy spanner on the same points, one with distance ratio 1.1:

{: style="text-align:center"}
![Greedy spanner with distance ratio 1.1]({{site.baseurl}}/assets/2020/greedy1.1.svg)

What we show is that for greedy spanners in the plane, each spanner edge is crossed by a bounded number of longer or equal-length edges. An edge can be crossed by an unbounded number of shorter edges, but our result implies that the [intersection graph](https://en.wikipedia.org/wiki/Intersection_graph) of the edges is itself a sparse graph. (In any subgraph of the intersection graph, the longest edge has bounded degree, so the graph as a whole has bounded [degeneracy](https://en.wikipedia.org/wiki/Degeneracy_(graph_theory)).) And that, in combination with the results of the SIGSPATIAL paper, implies that these graphs also have small separators: any $$n$$-vertex subgraph of a greedy spanner can be split into two smaller graphs of at most $$2n/3$$ vertices each by the removal of $$O(\sqrt{n})$$ vertices.

Unlike many of the other known results on greedy spanners, this works only in the plane. It doesn't make sense to talk about crossings in higher-dimensional greedy spanners, because for points in general position there won't be any crossings, even in the complete graph. So we don't know whether higher-dimensional greedy spanners have sublinear separators or not; it would be of interest to find out.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/103677400632411777))