---
layout: post
title: Triangulation thickens grids
date: 2022-02-13 22:54
---
If you zigzag back and forth through the columns (or rows) of an ordinary two-dimensional grid graph, following a pattern dignified with the fancy name "[boustrophedon](https://en.wikipedia.org/wiki/Boustrophedon)", you get a one-dimensional ordering of the vertices that can be used as the basis of a nice planar [arc diagram](https://en.wikipedia.org/wiki/Arc_diagram) of this graph.

{: style="text-align:center"}
![Boustrophedon layout of a 2d grid]({{site.baseurl}}/assets/2022/boustrophedon.svg){: style="width:100%;max-width:720px" }

The same idea works in 3d. You can divide a 3d grid graph into 2d layers, zigzag within each layer, and then reverse the same zigzagging order in alternating layers, to get another nice one-dimensional ordering of the vertices. It doesn't give a planar drawing (this graph is not planar), but it does allow it to be drawn without crossings on the four half-planes of a four-page [book embedding](https://en.wikipedia.org/wiki/Book_embedding). More generally, any $$d$$-dimensional grid graph can be drawn in the same way as a book embedding with $$2(d-1)$$ pages.

{: style="text-align:center"}
![Double boustrophedon layout of a 3d grid]({{site.baseurl}}/assets/2022/double-boustrophedon.svg){: style="width:100%;max-width:720px" }

I'm a coauthor on a new preprint showing that this one-dimensional layout is very sensitive to the way you connect nearby vertices in the 3d grid. If you modify the grid just a little bit, triangulating it by adding a diagonal to each grid square, then the resulting graph no longer has a book embedding with a constant number of pages. Instead, for a triangulated $$n\times n\times n$$ grid, $$\Theta(n^{1/3})$$ pages are necessary (and sufficient). The preprint is "Three-dimensional graph products with unbounded stack-number", with Robert Hickingbotham, Laura Merker, Sergey Norin, Michał T. Seweryn, and David R. Wood, [arXiv:2202.05327](https://arxiv.org/abs/2202.05327); the long coauthor list is because it comes from a collaboration that began at the Banff workshop on Graph Product Structure Theory last November.

There are many other related results packed into the same preprint, but rather than summarizing them all I'd rather take a step back and look at the big picture. The result that triangulated grids have high book thickness turns out to follow from a sequence of connections that is closely analogous to results about the high width of 2d grids, and I think the analogies between these connections are very interesting. For 2d grids:

* Two standard measures of one-dimensionality of graphs are [cutwidth](https://en.wikipedia.org/wiki/Cutwidth) and [pathwidth](https://en.wikipedia.org/wiki/Pathwidth). Both can be defined in terms of continuous maps from the graph (considered as a one-dimensional topological space) to a line. A graph has cutwidth at most $$c$$ if it has a map in which every point of the line belongs to the images of at most $$c$$ edges, and pathwidth at most $$p$$ if it has a map in which every point of the line belongs to the images of edges that have at most $$p$$ distinct vertices as their left endpoints.

* For a graph of maximum degree $$d$$, at most $$d$$ edges can share a left endpoint, so if the graph has cutwidth $$c$$ it has pathwidth at least $$c/d$$.

* A complete graph with $$n$$ vertices and $$\tbinom{n}{2}$$ edges, mapped continuously to a line, always has a point covered by $$\Omega(n^2)$$ edges, at the median vertex of the mapping.

* For a 2d grid graph, we can associate each vertex with a subgraph consisting of the union of the row and column of the grid containing that vertex.

  {: style="text-align:center"}
![Bramble associating each grid vertex with the union of its row and column]({{site.baseurl}}/assets/2022/grid-bramble.svg){: style="width:100%;max-width:450px" }

  This family of subgraphs is a [bramble](https://en.wikipedia.org/wiki/Bramble_(graph_theory)), meaning that all of the subgraphs are connected and touch each other. In this case, they all touch at shared vertices, but brambles also allow subgraphs to touch across edges. In the bramble for an $$n\times n$$ grid graph, each graph vertex or edge belongs to $$O(n)$$ subgraphs.

* We can map $$K_{n^2}$$ continuously onto the grid, vertex-to-vertex, by mapping each edge of $$K_{n^2}$$ onto a path through the two touching subgraphs for its endpoints. This map has low congestion: each grid vertex or edge is in the image of $$O(n)$$ vertices or edges of $$K_{n^2}$$.

* Any map of the grid to a line can be composed with the map from $$K_{n^2}$$ to the grid, giving a map of $$K_{n^2}$$ onto the line. Because of the low congestion of the map to the grid, a point of the line that is covered by $$\Omega(n^2)$$ edges of the complete graph must also be covered by $$\Omega(n)$$ edges of the grid. Since this is true for all maps to a line, the grid has pathwidth and cutwidth $$\Omega(n)$$.

Now let's do the same thing, stepped up a dimension!

* Instead of graphs, let's consider 2-dimensional simplicial complexes, systems of points, edges, and triangles. And instead of mapping them to a one-dimensional line, let's map them (topologically, not necessarily linearly) to a two-dimensional plane. We'll say that the mapping has high thickness if some point is covered by many triangles (corresponding to cutwidth), or by many vertex-disjoint triangles (corresponding to pathwidth).

* For a graph of maximum  degree $$d$$, at most $$\tbinom{d}{2}$$ triangles can share a vertex, so a point covered by many triangles will be covered by many vertex-disjoint triangles. More importantly, this is where the book thickness comes in: an argument related to the [Erdős–Szekeres theorem](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Szekeres_theorem) proves that, when a graph has a $$\theta$$-page book embedding, drawn with its vertices on a circle and its edges as chords of the circle, then at most $$\theta^3$$ vertex-disjoint triangles in the graph can contain any point within the circle. So if every mapping into the plane produces a system of triangles of thickness $$t$$, you also get book thickness $$\Omega(t^{1/3})$$.

* A complete simplicial complex with $$n$$ vertices, $$\tbinom{n}{2}$$ edges, and $$\tbinom{n}{3}$$ triangles, mapped to the plane, always leads to a point covered by $$\Omega(n^3)$$ triangles, by a result of Gromov. (This is closely related to the earlier work of Regina Liu on [simplicial depth](https://en.wikipedia.org/wiki/Simplicial_depth) but we want to allow any continuous mapping to the plane, whereas simplicial depth involves mappings that are linear on each edge and triangle.)

* For an $$n\times n\times n$$ grid graph, with its squares triangulated to form a 2d complex $$C$$, we can associate each vertex with a subcomplex of $$C$$ consisting of the union of the 2d grid planes containing that vertex. This family of subcomplexes has connected pairwise unions and simply connected triplewise unions, analogous to the properties of a bramble for a graph.

* We can map the complete simplicial complex onto the grid, vertex-to-vertex, by mapping each edge onto a path through the union of two subgraphs and each triangle onto a triangulated surface within the union of three subgraphs. This map has low congestion: each grid vertex, edge, or triangle is in the image of $$O(n^2)$$ vertices, edges, or triangles of the complete complex.

* Any map of the triangulated 3d grid onto the plane can be composed with the map from the complete 2-complex to the grid, giving a map of the complete complex onto the plane. Because of the low congestion of the map to the grid, a point of the plane that is covered by $$\Omega(n^3)$$ triangles of the complete complex must also be covered by $$\Omega(n)$$ triangles of the triangulated grid. Since this is true for all maps to a plane, the triangulated grid has book thickness $$\Omega(n^{1/3})$$.

For details, generalizations to triangulated products of trees and non-grid tessellations of space, matching upper bounds on book thickness, and more, please see the preprint.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/107795266201400204))