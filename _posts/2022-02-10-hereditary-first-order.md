---
layout: post
title: Hereditary first order graph properties can be hard
date: 2022-02-10 17:40
---
Many natural classes of undirected graphs are [hereditary](https://en.wikipedia.org/wiki/Hereditary_property), meaning that if you delete vertices from any graph in the class, the induced subgraph that you get always remains in this class. Every hereditary class of graphs can be defined by its [forbidden induced subgraphs](https://en.wikipedia.org/wiki/Forbidden_graph_characterization), the minimal graphs that do not belong to the class. When there are only finitely many of these forbidden subgraphs, it is possible to define the class by a formula in the first-order [logic of graphs](https://en.wikipedia.org/wiki/Logic_of_graphs) describing the graphs that do not have these subgraphs, and to test membership in the class in polynomial time by searching for a forbidden subgraph. Examples include:

* The [threshold graphs](https://en.wikipedia.org/wiki/Threshold_graph), whose forbidden subgraphs are a four-vertex path, four-vertex cycle, or four-vertex perfect matching.

* The [cographs](https://en.wikipedia.org/wiki/Cograph), whose single forbidden subgraph is a four-vertex path.

* The [triangle-free graphs](https://en.wikipedia.org/wiki/Triangle-free_graph), whose single forbidden subgraph is a <span style="white-space:nowrap">triangle $$K_3$$.</span>

* The [claw-free graphs](https://en.wikipedia.org/wiki/Claw-free_graph), whose single forbidden subgraph is the four-vertex <span style="white-space:nowrap">tree $$K_{1,3}$$.</span>

* The [line graphs](https://en.wikipedia.org/wiki/Line_graph), which have a forbidden subgraph characterization with nine forbidden subgraphs:

{: style="text-align:center"}
![The nine forbidden induced subgraphs of line graphs]({{site.baseurl}}/assets/2022/nonline.svg)

However, there might be infinitely many forbidden subgraphs. In many such cases, it is still possible to recognize these graphs in polynomial time, often by a greedy algorithm that removes vertices one at a time based on some local structure. Additionally, in these cases, it is often possible to describe the property of being one of the forbidden subgraphs by a first-order formula, so that the graph class is the class of graphs none of whose subgraphs model that formula. For instance:

* The [<span style="white-space:nowrap">$$d$$-degenerate</span> graphs](https://en.wikipedia.org/wiki/Degeneracy_(graph_theory)) are graphs in which no non-empty induced subgraph has all vertices of degree greater <span style="white-space:nowrap">than $$d$$.</span> They can be recognized in polynomial time as the graphs reducible to empty by repeatedly removing low-degree vertices.

* The [distance-hereditary graphs](https://en.wikipedia.org/wiki/Distance-hereditary_graph) are graphs in which every induced subgraph with two or more vertices has a degree-one vertex, or twins, two vertices with equal closed or open neighborhoods. They can be recognized in polynomial time by repeatedly removing degree-one vertices or merging twins.

* The [chordal graphs](https://en.wikipedia.org/wiki/Chordal_graph) are graphs with no induced cycle of more than three vertices, or the graphs in which every non-empty induced subgraph has a simplicial vertex, a vertex whose neighbors are all adjacent. They can be recognized in polynomial time by repeatedly removing simplicial vertices.

* The [perfect graphs](https://en.wikipedia.org/wiki/Perfect_graph) are graphs with no odd induced cycle of more than three vertices, or its complement. They can be recognized in polynomial time but the algorithm is complicated.

Obviously, not all hereditary classes are like that; one could, for instance, forbid induced cycles whose lengths belong to an undecidable set of integers, and get a hereditary class of graphs whose recognition problem is again undecidable. But this led me to wonder: is there a connection between the first-order recognizability of the forbidden subgraphs and the polynomial recognizability of the graph class itself? Could it be that every hereditary class defined by a first-order set of forbidden subgraphs is polynomially recognizable?

No!

The counterexample I found is the family of graphs whose forbidden subgraphs are the non-empty [cubic (3-regular) graphs](https://en.wikipedia.org/wiki/Perfect_graph). Let's call these the cubic-free graphs. Being cubic is easily expressed in first-order logic, so the forbidden subgraphs for the cubic-free graphs are first-order recognizable. However, under standard assumptions, the cubic-free graphs themselves are not polynomially recognizable: their recognition problem is <span style="white-space:nowrap">$$\mathsf{coNP}$$-complete.</span> Put another way, the problem <small>CUBIC INDUCED SUBGRAPH</small> asking whether a given graph has a non-empty cubic induced subgraph is <span style="white-space:nowrap">$$\mathsf{NP}$$-complete.</span>

I found lots of references in the literature to problems of finding non-empty cubic subgraphs (not required to be induced subgraphs; see Garey & Johnson GT32), or to finding cubic induced subgraphs with some constraint on their size, but not to the <small>CUBIC INDUCED SUBGRAPH</small> problem itself. So instead, I found an <span style="white-space:nowrap">$$\mathsf{NP}$$-completeness</span> reduction myself, from [<small>3-DIMENSIONAL MATCHING</small>](https://en.wikipedia.org/wiki/3-dimensional_matching), in which the input is a 3-uniform hypergraph (meaning that each hyperedge touches three hypervertices) and one must find a subset of the hyperedges that touches every hypervertex exactly once. An example of my reduction is shown below, from which I think the general case should be more clear.

{: style="text-align:center"}
![NP-completeness reduction from 3-dimensional matching to cubic induced subgraph]({{site.baseurl}}/assets/2022/3dm23is.svg)

The input hypergraph is shown with its hypervertices as large blue disks and its hyperedges as medium-sized yellow disks. Inside each of these disks is shown part of a graph, a gadget into which that piece of the hypergraph is translated to form a piece of a <small>CUBIC INDUCED SUBGRAPH</small> instance. The example hypergraph used in the image is 4-regular (every hypervertex touches four hyperedges) but that's not essential. Once you start making choices of which vertices to include or exclude in an induced subgraph, you can make a chain of inferences from that choice:
* If you have included a vertex that has only three non-excluded neighbors, you must include all three of them.
* If you have included a vertex that has three included neighbors, you must exclude all its other neighbors.
* If some vertex has fewer than three neighbors that are not excluded, you must exclude it.

It follows from this sort of reasoning that the only non-empty cubic induced subgraphs are like the ones shown by the dark red vertices in these gadgets: a vertex for each of the the hyperedges in a matching (such as the matching of dark-yellow hyperedges), and a corresponding subset of the vertices in every hypervertex gadget. Because finding a cubic induced subgraph is <span style="white-space:nowrap">$$\mathsf{NP}$$-complete,</span> its complementary problem, testing whether a graph is cubic-free, is <span style="white-space:nowrap">$$\mathsf{coNP}$$-complete.</span>