---
layout: post
title: Polyhedra without disjoint faces 
date: 2020-10-18 17:06
---
Some research I've been doing led me to consider the (prism,$$K_{3,3}$$)-minor-free graphs. It's not always easy to go from [forbidden minors](https://en.wikipedia.org/wiki/Forbidden_graph_characterization) to the graphs that forbid them, or vice versa, but in this case I think there's a nice characterization, which I'm posting here because it doesn't fit into the research writeup: these are the graphs whose nontrivial triconnected components are $$K_5$$, [wheel graphs](https://en.wikipedia.org/wiki/Wheel_graph), or the graph $$K_5-e$$ of the [triangular bipyramid](https://en.wikipedia.org/wiki/Triangular_bipyramid). The illustration below shows an example of a graph with this structure, with its nontrivial triconnected components colored red and yellow. There's a simpler and more geometric way to say almost the same thing: the only convex polyhedra that do not have two vertex-disjoint faces are the pyramids and the triangular bipyramid.

{: style="text-align:center"}
![A (prism, K_{3,3})-minor-free graph, with its nontrivial triconnected components colored red and yellow]({{site.baseurl}}/assets/2020/prism-k33-free.svg)

Some definitions: 

* Here by the prism graph I mean the graph of the triangular prism. Any other prism has this one as a minor, and so is irrelevant as a forbidden minor. However, the pyramids in this structure can have any polygon as their base, corresponding to wheel graphs with arbitrarily many vertices.

* $$K_{3,3}$$ is a complete bipartite graph with three vertices on each side of its bipartition, famous as the [utility graph](https://en.wikipedia.org/wiki/Three_utilities_problem), one of the two forbidden minors for planar graphs. The triangular prism graph and $$K_{3,3}$$ are the only two [3-regular graphs](https://en.wikipedia.org/wiki/Cubic_graph) with six vertices.

{: style="text-align:center"}
![The prism graph and K_{3,3}]({{site.baseurl}}/assets/2020/prism-k33.svg)

* The triconnected components of a graph are the graphs associated with the nodes of its [SPQR tree](https://en.wikipedia.org/wiki/SPQR_tree), or of the SPQR trees of its biconnected components. These are cycle graphs, dipole multigraphs, or 3-connected graphs, and by "nontrivial" I mean the ones that are not cycles or dipoles. A triconnected component might not be a subgraph of the given graph, because it can have additional edges that correspond to paths in the given graph. For instance, subdividing the edges of any graph into paths, or more generally replacing edges by arbitrary series-parallel graphs, does not change its set of nontrivial triconnected components.

* I'm using "face" in the usual three-dimensional meaning, a two-dimensional subset of the boundary of the polyhedron. For higher-dimensional polytopes, "face" has a different meaning that also includes vertices and edges, and "facet" would be used to refer to the $$(d-1)$$-dimensional faces, but using that terminology seems overly pedantic here.

Sketch of proof of the characterization of polyhedra without two disjoint faces: Consider any polyhedron without disjoint faces. If one face shares an edge with all the others, it's a [Halin graph](https://en.wikipedia.org/wiki/Halin_graph), a graph formed by linking the leaves of a tree into a cycle; if the tree is a star, it's a pyramid, and otherwise contracting all but one of the interior edges of the tree, and then all but four of the cycle edges, will produce a prism minor. In the remaining case, some two faces share only a vertex $$v$$, which must have degree four or more. Each face that is disjoint from $$v$$ must touch all that faces incident to $$v$$, which can only happen when there is one face disjoint from $$v$$ (a pyramid) or two faces disjoint from $$v$$, neither of which has an edge disjoint from the other one (a bipyramid).

Sketch of a lemma that every convex polyhedron with two disjoint faces has a prism minor: glue a pyramidal cap into each of the two faces, producing a larger convex polyhedron which by either [Steinitz's theorem](https://en.wikipedia.org/wiki/Steinitz%27s_theorem) or [Balinski's theorem](https://en.wikipedia.org/wiki/Balinski%27s_theorem) is necessarily 3-connected, and find three vertex-disjoint paths between the apexes of the attached pyramids. The parts of these paths outside the two glued pyramids, together with the boundaries of the two faces, form a subdivision of a prism.

Sketch of proof of the characterization of (prism,$$K_{3,3}$$)-minor-free graphs: The nontrivial triconnected components are exactly the maximal triconnected minors of the given graph, so if either of the two triconnected forbidden minors is to be found in the given graph, it will be found in one of the triconnected components. $$K_5$$ and the triangular bipyramid are too small to have one of the forbidden minors. The only 3-connected minors of the pyramid graphs are smaller pyramids, obtained by contracting one of the cycle edges of the pyramid, so these also do not have a forbidden minor. Therefore the graphs of the stated form are all (prism,$$K_{3,3}$$)-minor-free.

In the other direction, suppose that a graph is (prism,$$K_{3,3}$$)-minor-free.
Each triconnected component is a minor, so it must also be (prism,$$K_{3,3}$$)-minor-free. What can these components look like? Forbidding $$K_{3,3}$$ as a minor rules out nonplanar components other than $$K_5$$, by a theorem of Wagner[^wagner] and Hall.[^hall] So the remaining components that we need to consider are triconnected planar graphs with no prism minor. These cannot have two disjoint faces by the lemma, and so they can only be pyramids or the triangular bipyramid.

* Footnotes go here
{:footnotes}

[^wagner]: K. Wagner. Über eine Erweiterung des Satzes von Kuratowski. _Deutsche Mathematik_, 2:280–285, 1937.

[^hall]: D. W. Hall. A note on primitive skew curves. _Bulletin of the American Mathematical Society_, 49(12):935–936, 1943. [doi:10.1090/ S0002-9904-1943-08065-2](https://doi.org/10.1090/ S0002-9904-1943-08065-2).