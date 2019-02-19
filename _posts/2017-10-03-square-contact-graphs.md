---
layout: post
title: Square contact graphs
date: 2017-10-03 21:48
---
I've [already written here about contact graphs of squares]({{site.baseurl}}{% post_url 2014-02-23-schramms-monster-packing %}), the graphs you get from non-overlapping squares in the plane by making a vertex per square and an edge when two squares share pieces of their edges. But now I have a new preprint on the subject: "Square-Contact Representations of Partial 2-Trees and Triconnected Simply-Nested Graphs" (with Da Lozzo, Devanny, and Johnson, [arXiv:1710.00426](https://arxiv.org/abs/1710.00426), to appear at [ISAAC 2017](https://saki.siit.tu.ac.th/isaac2017/)).

Here's an example, of a different kind of graph than the ones in the preprint. The squares in the image below (four of which are too big to fit and are visible near the frame of the image)...

{: style="text-align:center"}
![Contact representation of Greek cross heptacube]({{site.baseurl}}/assets/2017/gcsq.svg)

...have the same pattern of contacts as the adjacencies of the following graph, a heptacube shaped like a three-dimensional Greek cross:

{: style="text-align:center"}
![Greek cross heptacube]({{site.baseurl}}/assets/2017/gc7cube.svg)

By being more careful to keep each gap between squares close to square itself (filling such gaps with four-tuples of squares that are only slightly bigger than a third of the width of the gap) it is possible to repeat this construction for any number of additional levels, representing any [polycube](https://en.wikipedia.org/wiki/Polycube) in which the connections between cubes are tree-like.

One thing that makes these particular graphs easier than some to represent is that they have no triangles. Triangles can be a problem with square contact graphs, because the three squares representing the vertices of the triangle have to touch each other snugly, with no space in between them. That makes the packing of squares more highly constrained, but it also means there is nowhere to put more squares that might represent vertices inside the triangle. So planar graphs that have a triangle with something inside it (either a separating triangle, or a triangle as the outer face).

That turns out to be the only obstacle for representing some other tree-like planar graphs, the ones in the preprint. Series-parallel graphs can be represented by square contacts unless they contain a subgraph $$K_{1,1,3}$$, a series-parallel graph that has a separating triangle in all of its planar embeddings. And Halin graphs can be represented unless they equal $$K_4$$, a Halin graph that always has a triangle as its outer face. Proving that these conditions are necessary is easy, but proving that they are sufficient is a nasty induction.

Unfortunately, for less-restricted classes of graphs, triangles aren't the only obstacle.
Separating four-cycles can also be a problem, even though the polycubes have lots of them. [Schramm's monster theorem]({{site.baseurl}}{% post_url 2014-02-23-schramms-monster-packing %}), the subject of my previous post, shows that every maximal planar graph without separating four-cycles has an improper square contact representation, one where sometimes adjacent squares touch at their corners rather than at their edges. But when there's a separating four-cycle, the representation that you get from the monster theorem might collapse that cycle to four squares all meeting at their corners (like the [Four Corners](https://en.wikipedia.org/wiki/Four_Corners), a spot in the US where four states meet) and everything inside the cycle gets squished to a point.

The simplest example that I know of for this phenomenon is the [square antiprism](https://en.wikipedia.org/wiki/Square_antiprism). It's a planar graph with two quadrilateral faces and eight triangles. To represent it by square contacts, of course you have to put one of the quadrilaterals as the outside face, because a triangle as the outside face would already leave no space for anything else. But if the outside face is a quadrilateral, the gap inside its four squares must be square, and the only way to pack the inner four squares with the right adjacency is to make an improper representation with the four corners touching. If you augment the graph with one more vertex in its inner quadrilateral, there is nowhere for the corresponding square to go and no representation at all.

{: style="text-align:center"}
![The improper representation of a square antiprism, and a graph with no square contact representation]({{site.baseurl}}/assets/2017/nested-quads.svg)

Our preprint only handles some special classes of graphs. We have identified both nonempty triangles and separating antiprisms as obstacles to representation, but they seem unlikely to be the only ones. As we write, "a characterization of the graphs having proper contact representations by squares remains elusive".