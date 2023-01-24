---
layout: post
title: Doubled planar drawings of doubled planar graphs
date: 2023-01-23 18:17
---
If you start with a planar graph, and make two copies of each vertex, you should be able to draw the result as two planar graphs, right? But it's more complicated than just copying a drawing of your starting graph, because you get four copies of each edge, and you have to put them all somewhere.

For instance, the graph $$K_{2,2,2}$$ is planar (it's the graph of an octahedron). Doubling it gives $$K_{4,4,4}$$. And $$K_{4,4,4}$$ can indeed be drawn as two planar graphs, but not as two octahedra. Here it is as two octagonal bipyramids:

{: style="text-align:center"}
![The complete tripartite graph K_{4,4,4} drawn as  the union of two octagonal bipyramids]({{site.baseurl}}/assets/2023/bipyramidal-K444.svg)

And here it is drawn as two planar graphs in a different way:

{: style="text-align:center"}
![Another drawing of the complete tripartite graph K_{4,4,4} as the union of two planar graphs]({{site.baseurl}}/assets/2023/nested-quad-K444.svg)

Drawings like this, where a nonplanar graph is presented as the union of two planar graphs, are called _biplanar_. Another word for the same idea is _thickness_: the thickness of a graph is the number of planar subgraphs needed to cover all of its edges, and a graph is biplanar if it has thickness two. A famous unsolved problem in graph theory, [Ringel's Earth–Moon problem](https://en.wikipedia.org/wiki/Earth%E2%80%93Moon_problem), asks how many colors are necessary to color biplanar graphs. The name comes from the idea that you might want to color a pair of maps of countries that all have space colonies on the Moon, using the same color for each country and its colony. The map of their adjacencies on the Earth gives you one planar graph, and the map of adjacencies between their colonies on the Moon gives you the other.  $$K_{4,4,4}$$ is not a very interesting example for this question, because it only needs three colors; some other biplanar graphs need as many as nine. On the other hand, we only know how to prove that twelve colors are always enough, so there's a pretty big gap. Ellen Gethner published [a nice survey on the problem](https://doi.org/10.1007%2F978-3-319-97686-0_11) in 2018, including also some other material on biplanar graphs.

One of Gethner's conjectures from that survey is that doubled planar graphs (or as she calls them, 2-blowups) are always biplanar. The conjecture is plausible, because the number of edges is within the right range to be biplanar. If the starting planar graph has $$n$$ vertices, it has $$3n-6$$ edges, and its blowup has $$2n$$ vertices and $$12n-24$$ edges. This is fewer than $$12n-12$$, the limit on the number of edges for biplanar graphs with $$2n$$ vertices. And for a wide class of planar graphs, even those with the maximum possible number of edges, I can prove that their blowups are indeed biplanar. This works whenever the dual graph can be partitioned into two induced paths. In the original graph, these paths form strips of faces connected end-to-end, and in the biplanar drawing of the blowup they become sequences of nested quadrilaterals. For instance, $$K_{4,4,4}$$ is the blowup of the octahedral graph $$K_{2,2,2}$$, whose dual graph is a cube, and the cube can be partitioned into two induced paths:

{: style="text-align:center"}
![Partition of a cube into two induced paths]({{site.baseurl}}/assets/2023/cube-path-partition.svg)

The second of the biplanar drawings of $$K_{4,4,4}$$ above comes from this dual induced path partition.

Despite this positive evidence, the conjecture turns out to be false. My latest preprint, "On the biplanarity of blowups", [arXiv:2301.09246](https://arxiv.org/abs/2301.09246), constructs counterexamples, planar graphs whose blowups are not biplanar. The general idea of the construction is very similar to one of my earlier papers, on [polyhedral graphs that cannot be realized as convex polyhedra with isosceles-triangle faces]({{site.baseurl}}{% post_url 2020-09-01-isosceles-polyhedra %}). Both papers are based on the construction of a [Kleetope](https://en.wikipedia.org/wiki/Kleetope), a polyhedron formed from another polyhedron by attaching a pyramid to each face.
If you repeat the Kleetope construction, you get a polyhedron enclosed by multiple layers of pyramids, and any drawing or geometric realization of this layered polyhedron also gives you a drawing or realization of the simpler polyhedra underneath those layers.
Each time you layer on more pyramids, any possible biplanar drawing of the result gets more and more constrained, until with enough layers it becomes completely impossible.

Because not all planar blowups are biplanar, the question arises: which ones are, and which ones aren't? Is there an efficient algorithm that takes as input a planar graph, produces a biplanar drawing of its blowup if such a drawing exists, and tells you when such a drawing doesn't exist? I don't know.