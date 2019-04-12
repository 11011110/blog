---
layout: post
title: Coloring kinggraphs
date: 2019-04-11 21:28
---
Draw a collection of quadrilaterals in the plane, meeting edge to edge, so that they don't surround any open space (the region they cover is a topological disk) and every vertex interior to the disk touches at least four quadrilaterals. Is it always possible to color the corners of the quadrilaterals with four colors so that all four colors appear in each quadrilateral?

{: style="text-align:center"}
![4-colored kinggraph]({{site.baseurl}}/assets/2019/colored-kinggraph.svg)

The graph of corners and quadrilateral edges is a [squaregraph](https://en.wikipedia.org/wiki/Squaregraph) but this question is really about coloring a different and related graph, called a kinggraph, that also includes as edges the diagonals of each quad. It's called that because one example of this kind of graph is the [king's graph](https://en.wikipedia.org/wiki/King's_graph) describing the possible moves of a chess king on a chessboard.

{: style="text-align:center"}
![The king's graph]({{site.baseurl}}/assets/2019/kings-graph.svg)

The king's graph, and kinggraphs more generally, are examples of 1-planar graphs, graphs drawn in the plane in such a way that each edge is crossed at most once. The edges of the underlying squaregraph are not crossed at all, and the diagonals of each quad only cross each other. Squaregraphs are bipartite (like every planar graph in which all faces have an even number of edges), so they can be colored with only two colors. 1-planar graphs, in general, can require six colors (for instance you can draw the complete graph $$K_6$$ as a 1-planar graph by adding diagonals to the squares of a triangular prism) and this is tight.
And you can easily 4-color the king's graph by using two colors in alternation across the even rows of the chessboard, and a different two colors across the odd rows. So the number of colors for kinggraphs should be somewhere between these two extremes, but where?

One useful and general graph coloring method is based on the [degeneracy](https://en.wikipedia.org/wiki/Degeneracy_(graph_theory)) of graphs. This is the largest number $$d$$ such that every subgraph has a vertex with at most $$d$$ neighbors; one can use a [greedy coloring algorithm](https://en.wikipedia.org/wiki/Greedy_coloring) to color any graph with $$d+1$$ colors. Kinggraphs themselves always have a vertex with at most $$3$$ neighbors, but unfortunately they do not have degeneracy $$3$$. If you form a king's graph on a $$4\times 4$$ chessboard, and then remove its four corners, you get a subgraph in which all vertices have at least four neighbors.
This turns out to be as large as possible: every kinggraph has degeneracy at most four. This is because, if you consider the zones of the system of quads (strips of quads connected on opposite pairs of edges), there always exists an "outer zone", a zone with nothing on one side of it (see the illustration, below). You can remove the vertices of the outer zone one at a time, in order from one end to the other, always removing a vertex of degree at most four, and then repeat on another outer zone until the whole graph is gone. So the degeneracy and greedy coloring method shows that you can 5-color every kinggraph, better than the 6-coloring that we get for arbitrary 1-planar graphs.

{: style="text-align:center"}
![An outer zone]({{site.baseurl}}/assets/2019/outer-zone.svg)

This turns out to be optimal! For a while I thought that every kinggraph must be 4-colorable, because it was true of all the small examples that I tried. But it's not true in general, and here's why. If you look at the zones of the 4-colored kinggraph above, you might notice a pattern. The edges that connect pairs of quads from the same zone have colorings that alternate between two different pairs of colors. For instance, we might have a zone that has red–yellow edges alternating with blue–green edges, or another zone that has red–blue edges alternating with green–yellow edges. This is true whenever a kinggraph can be 4-colored. But there are only three ways of coloring a zone (that is, of partitioning the four colors into two disjoint pairs, which alternate along the zone). And when two zones cross each other, they must be colored differently. So every 4-coloring of a kinggraph turns into a 3-coloring of its zones. But the graph that describes the zones and its crossings is a triangle-free [circle graph](https://en.wikipedia.org/wiki/Circle_graph), and vice versa: every triangle-free circle graph describes a kinggraph. And triangle-free circle graphs may sometimes need as many as five colors, in which case so does the corresponding kinggraph.

I posted [an example of a squaregraph whose circle graph needs five colors]({{site.baseurl}}{% post_url 2008-03-23-ageevs-squaregraph %}) on this blog in 2008. Here's a slightly different drawing of the same graph from [a later post]({{site.baseurl}}{% post_url 2009-05-29-congratulations-dr-wortman %}).
Because its circle graph is not 3-colorable, the corresponding kinggraph is not 4-colorable.

{: style="text-align:center"}
![A squaregraph whose kinggraph is not 4-colorable]({{site.baseurl}}/assets/2009/cd220c.svg)

There are simpler examples of squaregraphs whose circle graph needs four colors. As long as the number of colors of the circle graph is more than three, the number of colors of the kinggraph will be more than four.

On the other hand, if you can color the circle graph with three colors, then it's also possible to translate this 3-coloring of zones back into a 4-coloring of the kinggraph. Just remove an outer zone, color the remaining graph recursively, add the removed zone back, and use the color of the zone you removed to decide which colors to assign to its vertices. Unfortunately, I don't know the computational complexity of testing whether a circle graph is 3-colorable. There was a conference paper by Walter Unger in 1992 that claimed to have a polynomial time algorithm, but without enough details and it was never published in a journal. I think we have to consider the problem of finding a coloring as still being open.

The same method also leads to an easy calculation of the number of 4-colorings (in the same sense) of the usual kind of chessboard with $$n\times n$$ squares, or of a king's graph with $$(n+1)^2$$ vertices. In this case, the zones are just the rows and columns of the chessboard. We can use one color for the rows and two for the columns, or vice versa, so the number of 3-colorings of the zones (accounting for the fact that the 2-colorings get counted twice) is $$3(2^{n+1}-2)$$. And once the coloring of the zones is chosen, the coloring of the chessboard itself is uniquely determined by the color of any of its squares, so the total number of chessboard colorings is $$12(2^{n+1}-2)$$.