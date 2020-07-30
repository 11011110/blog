---
layout: post
title: Polyhedra with convex unfoldings
date: 2020-07-29 22:18
---
My newest arXiv preprint is "Acutely triangulated, stacked, and very ununfoldable polyhedra" with Erik and Martin Demaine ([arXiv:2007.14525](https://arxiv.org/abs/2007.14525)). It's about polyhedra with acute-triangle faces that cannot be unfolded without cutting their surface into many separate polygons. I [already posted a video for the paper]({{site.baseurl}}{% post_url 2020-07-22-three-cccg-videos %}) so see that for more information.

Instead, I thought I'd go into a little more detail about a throwaway remark in the video and the paper (one that I already got an email query about). It says that [ideal hyperbolic polyhedra](https://en.wikipedia.org/wiki/Ideal_polyhedron) can always be unfolded (into the hyperbolic plane). These polyhedra are the hyperbolic convex hulls of finitely many limit points of the hyperbolic space; their faces are ideal polygons, glued together along entire hyperbolic lines. More strongly, if you cut an ideal polyhedron along any spanning tree of its vertices and edges, the result always unfolds into a convex ideal hyperbolic polygon. Here, for instance, is a net for an ideal cube:

{: style="text-align:center"}
![Net for an ideal cube]({{site.baseurl}}/assets/2020/ideal-cube-net.svg)

I don't know of a previous reference for this result, and the paper and video state it without proof (because it's an introductory remark and not the topic of the paper), but it's easy to prove a stronger statement by induction: any collection of ideal hyperbolic polygons (like the faces of an ideal polyhedron), when connected edge-to-edge in a complex with the connectivity of a tree (like the faces of any convex polyhedron when you cut it along a spanning tree), unfolds to an ideal convex polygon. As a base case, when you have one polygon in your collection, it unfolds to itself. When you have more than one, find a leaf polygon of the tree structure, remove it, and unfold the rest into a convex ideal polygon. Now add back the leaf. It needs to be connected to the rest of the complex along a hyperbolic line, which (by the induction hypothesis that the rest unfolds convexly) has the rest of the complex on one side and an empty hyperbolic halfplane on the other side. Any convex ideal polygon can be placed within this halfplane so that the side on which it should be glued matches up with the boundary line of the halfplane, with enough freedom to match up the points along this line that should be matched up.

This caused me to wonder: which Euclidean convex polyhedra have the same property, that cutting them along any spanning tree leads to a convex unfolding? The answer is: not very many. By [Descartes' theorem on total angular defect](https://en.wikipedia.org/wiki/Descartes%27_theorem_on_total_angular_defect), the angular defects at the vertices of a convex polyhedron add up to $$4\pi$$. If a polyhedron is to have all spanning trees produce a (weakly) convex unfolding, then each vertex has to have angular defect at least $$\pi$$, because otherwise cutting along a spanning tree that has a leaf at that vertex will make an unfolding that is non-convex at that vertex. And this is the only thing that can go wrong, because if all angular defects are at least $$\pi$$ then the unfolding will be convex at each of its vertices and cannot self-overlap.

So to answer the question about Euclidean polyhedra with all unfoldings convex, we need only look for ways to partition the total angular defect of $$4\pi$$ among some set of vertices so that each one gets at least $$\pi$$. If we know the defects of all the vertices and the distances between vertices, then by [Alexandrov's uniqueness theorem](https://en.wikipedia.org/wiki/Alexandrov%27s_uniqueness_theorem) the shape of the polyhedron will be determined. Since we're using Alexandrov, we should also consider a [dihedron](https://en.wikipedia.org/wiki/Dihedron) (two mirror-image convex faces glued at their edges) to be a special case of a polyhedron. This leaves, as the only cases:

- A triangular dihedron based on a right or acute triangle.

- A rectangular dihedron.

- A tetrahedron with angular defect exactly $$\pi$$ at each vertex.

{: style="text-align:center"}
![Convex unfoldings of dihedra and a disphenoid]({{site.baseurl}}/assets/2020/convex-unfoldings.svg)

The unfoldings of the dihedra have two copies of their face, mirrored across a joining edge. The tetrahedra with all-convex unfoldings are exactly the [disphenoids](https://en.wikipedia.org/wiki/Disphenoid), the tetrahedra whose four faces are congruent. They unfold either to a copy of the same face shape,
expanded by a factor of two in each dimension and creased into four copies along its [medial triangle](https://en.wikipedia.org/wiki/Medial_triangle), or a parallelogram, creased to form a strip of four congruent triangles. Their unfoldings were discussed by Jin Akiyama in his paper "Tile-makers and semi-tile-makers" (_American Mathematical Monthly_ 2007, [doi:10.1080/00029890.2007.11920450](https://doi.org/10.1080/00029890.2007.11920450), [jstor:27642275](https://www.jstor.org/stable/27642275)), as part of a broader investigation of polyhedra whose every unfolding tiles the plane.