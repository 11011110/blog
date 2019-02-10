---
layout: post
title: Triply-Hamiltonian edge colorings
date: 2018-12-02 17:58
---
Mark Jason Dominus recently made a blog post about the interesting observation that the [regular dodecahedron can have its edges properly colored with three colors so that every two colors form a Hamiltonian cycle](https://blog.plover.com/math/dodecahedral-3-coloring.html). Here's another view of the same dodecahedral coloring:

{: style="text-align:center"}
![Triply-Hamiltonian edge coloring of a regular dodecahedron]({{site.baseurl}}/assets/2018/hamiltonian-dodecahedron.svg)

Mark's drawing is easier to recognize as the dodecahedron, but this drawing style makes clear the Hamiltonicity of one of the pairs of colors: just look at the outer cycle. As with every planar graph drawn like this as a Hamiltonian cycle plus some diagonals, the diagonals can be partitioned into two non-crossing subsets, belonging to the front and back sides of an embedding of the graph onto a [dihedron](https://en.wikipedia.org/wiki/Dihedron). I've shown this by casing the crossings to show which diagonal is front and which is back at each crossing. The diagonals subdivide the front and back into the faces of the planar embedding and you can trace through the faces to check that there are 12 pentagons, six on the front and six on the back.

This property of having a triply-Hamiltonian edge coloring is not special to the dodecahedron. It's known to be true of every 3-regular graph whose edge coloring is unique (up to permutation of colors). This class of graphs includes the graph of the tetrahedron ($$K_4$$) as well as the non-planar generalized Petersen graph $$G(9,2)$$.

{: style="text-align:center"}
![Triply-Hamiltonian edge coloring of the generalized Petersen graph G(9,2)]({{site.baseurl}}/assets/2018/generalized-Petersen-9-2.svg)

The proof that uniquely 3-edge colorable graphs must be triply Hamiltonian is easy: if not, some two colors would form a 2-regular subgraph with multiple connected components, and you could get a different edge coloring by swapping the colors in one of the components. And there cannot be any other Hamiltonian cycles in these graphs, because every Hamiltonian cycle leads to a coloring like the one in the first illustration that alternates colors around the cycle and uses the third color for the diagonals. The larger generalized Petersen graphs $$G(6k+3,2)$$ are still triply-Hamiltonian; they have exactly three Hamiltonian cycles but do not have a unique edge coloring.[^t82]

Two uniquely 3-edge colorable graphs can be glued together by removing one vertex from each graph and reattaching the neighbors of the removed vertices by three new edges.

{: style="text-align:center"}
![Gluing two 3-edge-colored graphs together)]({{site.baseurl}}/assets/2018/glue-edge-coloring.svg)

Starting from $$K_4$$ and $$G(9,2)$$, this produces infinitely many uniquely 3-edge colorable graphs. The ones glued from only copies of $$K_4$$ are planar (the duals of the [Apollonian networks](https://en.wikipedia.org/wiki/Apollonian_network)) but the ones involving $$G(9,2)$$ are nonplanar.[^bh15]
As far as I know, all uniquely 3-edge colorable graphs are generated from $$K_4$$ and $$G(9,2)$$ by this operation, with one exception: the two-vertex three-edge multigraph, which is the identity element for the operation.
If so, this would lead to a polynomial time algorithm for recognizing and coloring these graphs. The same operation also preserves triply-Hamiltonian edge colorings even when they aren't the unique 3-edge-coloring of the graph.

Another operation does not preserve unique 3-edge-coloring, but it does preserve triply-Hamiltonian edge coloring: take any two differently-colored edges of a single graph, subdivide them into three-edge paths, and connect the four new vertices in pairs.

{: style="text-align:center"}
![Subdividing two edges in a triply-Hamiltonian 3-edge-colored graph]({{site.baseurl}}/assets/2018/subdivide-edge-coloring.svg)

For instance, depending on how you choose the two edges, you can use this operation to get from the two-vertex multigraph to either the triangular prism or the non-planar complete bipartite graph $$K_{3,3}$$.

You can't get the dodecahedron or $$G(9,2)$$ by these operations (they have neither 4-cycles nor 3-edge cuts) but by using these operations, you can get infinitely many other triply-Hamiltonian graphs. In fact, it seems difficult to find 3-vertex-connected cubic graphs that are not triply-Hamiltonian!  So I'll conclude by giving two families of graphs that are not triply-Hamiltonian.

The first non-triply-Hamiltonian family is the family of [prism graphs](https://en.wikipedia.org/wiki/Prism_graph) over odd polygons: the pentagonal prism, heptagonal prism, etc. We have already seen that the first graph in this family, the triangular prism, is triply-Hamiltonian, but the rest are not. They only have one Hamiltonian cycle, up to symmetries of the graph: the cycle that uses all but one edge from each of the two non-quadrilateral faces of the prism, and connects the resulting two paths by two edges of one of the quadrilaterals. But the three-edge-coloring that you get from this Hamiltonian cycle has only two colors on some of the quadrilateral faces, so those pairs of colors do not themselves form Hamiltonian cycles.

The second non-triply-Hamiltonian family is the family of planar 3-regular bipartite graphs (including the cube, the rest of the prisms, and a lot more graphs besides). To see this, let $$G$$ be a planar 3-regular bipartite graph.
If $$G$$ is not Hamiltonian then obviously it is not triply-Hamiltonian; otherwise, draw $$G$$ as in the first illustration, with two colors alternating around an outer Hamiltonian cycle and the third color used for all the interior diagonals. And, as in the first illustration, partition the interior diagonals into the ones on the front and back sides of an embedding onto a dihedron.
These diagonals partition the front and back sides into the faces of a planar embedding.

The number of front faces is one more than the number of front diagonals, and the number of back faces is one more than the number of back diagonals, so the total number of faces is more than the total number of diagonals.
There are two kinds of vertex in each face: "inner vertices" incident to a diagonal edge of the face, and "outer vertices" incident to two edges of the outer Hamiltonian cycle that both belong to the face. Every face has an even number of inner vertices, so if the graph is to be bipartite every face must also have an even number of outer vertices (zero or at least two). Because there are two outer vertices per diagonal (on the other side of the dihedron from the diagonal) but more faces than diagonals, there must be at least one face with no outer vertices. But then this face has edges that alternate between only two colors, and these two colors cannot form a Hamiltonian cycle. Since we can apply this argument to every three-edge-coloring of a bipartite planar graph in which two of the colors form a Hamiltonian cycle, this proves that no planar bipartite graph can be triply Hamiltonian.

On the other hand, planarity is essential to this argument, as we have already seen an example of a triply-Hamiltonian bipartite graph, the graph $$K_{3,3}$$. By gluing copies of $$K_{3,3}$$ together, we can get arbitrarily large triply-Hamiltonian bipartite graphs, all of which must be nonplanar.

* Footnotes go here
{:footnotes}

[^t82]: Thomason, Andrew (1982), "[Cubic graphs with three Hamiltonian cycles are not always uniquely edge colorable](https://doi.org/10.1002%2Fjgt.3190060218)", _J. Graph Th._ 6 (2): 219–221.

[^bh15]: belcastro, sarah-marie, and Haas, Ruth (2015), "[Triangle-free uniquely 3-edge colorable cubic graphs](https://arxiv.org/abs/1508.06934)", _Contributions to Discrete Mathematics_ 10 (2): 39–44.

([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/101174690700738835), [G+](https://web.archive.org/web/20190210013507/https://plus.google.com/100003628603413742554/posts/BA3qxsSQv8N))