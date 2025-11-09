---
layout: post
title: Hanoi graphs redrawn
date: 2025-11-08 22:02
---
A Hanoi graph is an abstract representation of the well-known [Tower of Hanoi](https://en.wikipedia.org/wiki/Tower_of_Hanoi) puzzle, in which one stacks disks of different sizes on several pegs (usually three peg). Initially the disks are all on one peg, and one must get them all to another peg by moving one disk at a time, without ever placing a bigger disk on a smaller disk. The vertices of the graph are all valid states of the puzzle: placements of disks on pegs in sorted order with the largest at the bottom and smallest at the top. Its edges represent valid moves of the puzzle. For any puzzle with $$p$$ pegs and $$n$$ disks, there is a Hanoi graph parameterized by $$p$$ and $$n$$, with $$p^n$$ vertices.

{: style="text-align:center"}
![Photo of a wooden Tower of Hanoi puzzle. CC-BY-SA 3.0 image by User:Evanherk from https://commons.wikimedia.org/wiki/File:Tower_of_Hanoi.jpeg]({{site.baseurl}}/assets/2025/hanoi/evanherk.jpg)

[The last time I posted here about Hanoi graphs]({{site.baseurl}}{% post_url 2020-05-03-hanoi-vs-sierpinski %}), the impetus was a [paper from FUN 2020](https://arxiv.org/abs/2005.00179) showing that their [treewidth](https://en.wikipedia.org/wiki/Treewidth) was approximately $$(p-2)^n$$, to within factors polynomial in $$n$$. My new preprint with the same authors (Daniel Frishberg and William Maxwell), "On the expansion of Hanoi graphs", [arXiv:2510.18010](https://arxiv.org/abs/2510.18010), eliminates the polynomial factor: the treewidth is $$\Theta\bigl((p-2)^n\bigr)$$. As the title suggests, the main idea of the preprint is a change in perspective, from treewidth to [expansion](https://en.wikipedia.org/wiki/Expander_graph), which turns out to be easier to bound more precisely. The two parameters are closely related to the existence of small cuts that separate the graph, but in kind of a dual way: the treewidth is large if there exists a big subset of vertices that cannot be disconnected by a small cut, and small if every big subset has a small cut. On the other hand, the expansion is large if every big subset of vertices cannot be disconnected by a small cut, and small if there exists a big subset with a small cut.

This change in perspective got me thinking about more literal changes in perspective, in visualizations of Hanoi graphs. As my previous post discussed, 3-peg Hanoi graphs are typically visualized with a layout resembling a [Sierpiński triangle](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle), arranged so that every edge has unit length:

{: style="text-align:center"}
![Hanoi graph with 3 pegs and 3 disks, arranged in a Sierpiński triangle. Every vertex of the graph is labeled with a top-down view of its arrangement of disks on pegs.]({{site.baseurl}}/assets/2025/hanoi/hanoi-sierpinski.svg)

In some ways this arrangement is very convenient. It makes it easy to find shortest paths (just go as straight as you can through the diagram), and to see that the optimal path from corner to corner of the diagram has length $$2^n$$. With a little more care you can tell, only looking at the recursive structure of the drawing, which disk is moving in each edge of the graph: each edge is the midpoint of one side of a recursive triangle in the drawing, and the size of the moving disk corresponds to the size of this triangle. But if you're trying to follow a path in this graph, although you can tell which disk you should move at each step, it's less obvious where to move it to. And if you're looking at a state of a Tower of Hanoi puzzle, it's difficult to find it on the diagram. There is a correspondence between pegs of the puzzle and vertices of recursive triangles, but this correspondence twists at each level of the drawing, making it difficult to follow.

Wouldn't it be easier to use a different layout, where an arrangement of disks on pegs directly controls the position of the corresponding vertex in the drawing? Just find the center of mass of the disks and use that point as the position of the vertex. For this to produce a two-dimensional layout, the pegs should be arranged in a triangle, like the ones in the diagram above. This will give an arrangement with many similar copies of the same triangle, because changing one disk to each of the three pegs it can go on changes the overall center of mass by a scaled copy of the triangle of pegs. The position of a vertex in each of these triangles directly corresponds to the position of the disk on its pegs, and the weight of a disk controls the size of its triangles. With power-of-two disk weights, one can reproduce a layout like the Sierpiński triangle layout, but with the vertices permuted. Instead I've chosen more quickly growing exponential weights to spread the recursive triangles farther apart and to create triple crossing points at each level of the drawing.

{: style="text-align:center"}
![Hanoi graph with 3 pegs and 3 disks, arranged by centers of mass with exponentially decreasing disk weights. Every vertex of the graph is labeled with a top-down view of its arrangement of disks on pegs.]({{site.baseurl}}/assets/2025/hanoi/hanoi-redrawn.svg)

In this layout, the length of an edge tells you the size of disk to move, and the direction of an edge tells you the direction to move it. For instance, the three big edges that cross in the center of the layout correpond to moves of the biggest of the three disks (the red disk), in the direction of the edge. Therefore, following paths is very easy. The cost that you pay for this benefit is that shortest paths are now much less obvious to find.

From this layout, another standard fact about Hanoi graphs becomes visually apparent: if you disallow horizontal disk moves and horizontal edges, you get a Hamiltonian path through all $$3^n$$ moves of the state space. For the versions of the puzzle with three pegs in a row, this restriction can be made by only allowing moves between consecutive pegs. The book [_The Tower of Hanoi – Myths and Maths_](https://doi.org/10.1007/978-3-0348-0237-6) (Hinz, Klavžar, Milutinović, and Petr) calls this restricted version the "Linear Tower of Hanoi" or "Three-in-a-row Tower of Hanoi" but these names make less sense for the center-of-mass layout, where we need a nonlinear peg arrangement, and for the multi-peg restricted puzzles I'll describe later.

{: style="text-align:center"}
![Removing all horizontal edges from the center-of-mass layout produces a Hamiltonian path.]({{site.baseurl}}/assets/2025/hanoi/hanoi-ham.svg)

To get a Hamiltonian cycle rather than a Hamiltonian path, you can combine three recursively-constructed Hamiltonian paths in the three outer recursive triangles of this layout. The moves of this Hamiltonian cycle can be described by the following very simple rule: only move disks to or from the peg containing the largest disk. If you do only that, and avoid reversing any individual move, you will automatically follow a Hamiltonian cycle through all states.

The Hamiltonian path formed by avoiding horizontal moves can also be used as the linear arrangement of vertices in an [arc diagram](https://en.wikipedia.org/wiki/Arc_diagram) of the Hanoi graph. It again has an interesting recursive structure:

{: style="text-align:center"}
![Arc diagram of the Hanoi graph, arranged in order along its Hamiltonian path of horizontal-avoiding moves.]({{site.baseurl}}/assets/2025/hanoi/hanoi-arcdiag.svg)

Here's a 5-disk 3-peg Hanoi graph, drawn with a center-of-mass layout and unlabeled vertices.

{: style="text-align:center"}
![Center-of-mass layout for a 3-peg 5-disk Hanoi graph.]({{site.baseurl}}/assets/2025/hanoi/hanoi-5level.svg)

My previous post only succeeded in drawing a 4-peg Hanoi graph for two disks. But you can use the same center-of-mass idea, with the same exponentially decreasing disk weights, to produce a 3-dimensional layout of the 4-peg Hanoi graphs. Here's what it looks like (with a perspective projection from 3d back into the plane) for two disks:

{: style="text-align:center"}
![Center-of-mass layout for a 4-peg 2-disk Hanoi graph.]({{site.baseurl}}/assets/2025/hanoi/4hanoi-2.svg)

For three disks:

{: style="text-align:center"}
![Center-of-mass layout for a 4-peg 3-disk Hanoi graph.]({{site.baseurl}}/assets/2025/hanoi/4hanoi-3.svg)

And for four disks:

{: style="text-align:center"}
![Center-of-mass layout for a 4-peg 3-disk Hanoi graph.]({{site.baseurl}}/assets/2025/hanoi/4hanoi-4.svg)

In these drawings, the vertices are arranged into four recursive tetrahedra at the four corners of a larger tetrahedron. Two of these tetrahedra, at the top left and bottom right of the drawings, are closer to the viewpoint (as indicated by larger vertices), and the other two are farther away. The triangular faces of the outer tetrahedron and of all the recursive tetrahedra form copies of the 3-peg layout. The edges connecting the four recursive tetrahedra form six sheets of parallel edges; each sheet connects two parallel edges of two recursive tetrahedra. These six sheets cross each other near the middle of the drawing, enclosing a cubical empty box in the middle.

I think it works better than I could reasonably expect for such a nonplanar and well-connected graph, and might be better yet with an interactive 3d view rather than a static projected 2d view. But I still have no idea how to effectively visualize Hanoi graphs with five or more pegs and three or more disks.

Another question, motivated by the structure of Hamiltonian cycles in 3-peg Hanoi graphs: the Hanoi graph is not regular, but it can be made into a $$(p-1)$$-regular graph by only allowing moves to and from the peg containing the big disk. If another peg is non-empty, its smallest disk can be moved onto the big disk, and otherwise the smallest disk on the peg of the big disk can be moved to it. For two pegs, this gives a Hamiltonian cycle of the state space. What is the structure of these restricted Hanoi graphs for more than two pegs? Here's an example, the 3-regular 64-vertex restricted Hanoi graph for four pegs and three disks.

{: style="text-align:center"}
![Center-of-mass layout for a 4-peg 3-disk Hanoi graph, restricted to only allow moves to and from the peg containing the big disk.]({{site.baseurl}}/assets/2025/hanoi/4hanoi-restricted.svg)

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/115518260635104754))