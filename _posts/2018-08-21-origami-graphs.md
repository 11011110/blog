---
layout: post
title: Origami graphs
date: 2018-08-21 07:21
---
A couple of months ago I wrote here about [origami folding patterns in which each crease runs all the way across the paper]({{site.baseurl}}{% post_url 2018-06-22-vertex-free-flat %}). That's now detailed in an appendix of my new preprint "Realization and Connectivity of the Graphs of Origami Flat Foldings" ([arXiv:1808.06013](https://arxiv.org/abs/1808.06013), to appear at [Graph Drawing](https://dccg.upc.edu/gd2018/)). But as the title suggests, the main part of the paper is about a somewhat different topic.

If you fold a piece of paper so that, in its folded state, it lies flat again (like the [bird base](https://commons.wikimedia.org/wiki/File:Bird_base.svg) from which an origami crane is made, but unlike the crane itself), and then you unfold the paper again and look at the creases that were used when it was in its folded state, those creases form straight line segments across the paper that continue until they meet other creases or the edge of the paper. They look like a planar graph! The question is: which graphs can you get in this way?

{: style="text-align:center"}
![Bird base (as illustrated by Fred the Oyster at https://commons.wikimedia.org/wiki/File:Bird_base.svg) and its unfolded graph.]({{site.baseurl}}/assets/2018/bird-base.png)

The new paper contains two main results: every tree with even degree (at least four) at its internal vertices can be the graph of an origami folding, and every graph of an origami folding is 2-vertex-connected and 4-edge-connected. This seems contradictory, as trees are only 1-connected, but the resolution to the contradiction comes from using different mathematical models for how you construct a graph from a folding pattern.

[Maekawa's theorem](https://en.wikipedia.org/wiki/Maekawa%27s_theorem) implies that, at every point where creases come together the degree must be even and at least four. So the only way to get a leaf of a tree would be for it to be a point where the crease reaches the edge of the paper. To simplify the problem mathematically, we instead consider infinite sheets of paper, and look for folding patterns that form trees having infinite rays as their leaves. Cutting the paper into a square that surrounds all the other vertices of the drawing would then make a finite tree with leaves along the edges of the square. Sort of like the following drawing:

{: style="text-align:center"}
![Locally but not globally flat foldable tree]({{site.baseurl}}/assets/2018/tree-counterexample.svg)

This drawing obeys not only Maekawa's theorem, but also [Kawasaki's theorem](https://en.wikipedia.org/wiki/Kawasaki%27s_theorem), according to which the alternating sum of angles at each vertex must be zero. That's enough to allow it to fold flat locally, at each vertex (ignoring the rest of the pattern). But it is not globally flat foldable! If you try it, you will discover that the four diagonal creases that extend as rays from the center of the drawing must be folded in the usual way that you would quarter a sheet of paper, jamming one of the creases into the middle of another one. So far so good. But no matter which of these four diagonal creases you choose as the inner one, it will get in the way of the additional folds attached to the other crease that surrounds it.

Despite this tricky example, Maekawa's condition on the vertex degrees turns out to be the only obstacle to drawing trees as flat-foldable folding patterns. The trick is to surround each crease with a buffer zone of unfolded paper, preventing two creases from being folded right up against each other like in the example, so that there is always more room to attach more creases to each one.

The other result on connectivity again uses an infinite sheet of paper but it forms a graph from a folding pattern by adding one more vertex at infinity, to be the endpoint of all of the creases that form rays, rather than giving each ray its own separate ending vertex. So when you do this to a tree folding pattern, all the leaves end up being merged into a single supervertex, giving a series-parallel graph. The graphs that you get in this way from trees with degree-four internal vertices have vertex connectivity exactly 2 and edge connectivity exactly 4, showing that the connectivity bounds in the paper are tight.

For some other geometric graph realization questions, like the question of [which graphs are the graphs of convex polyhedra](https://en.wikipedia.org/wiki/Steinitz%27s_theorem), connectivity tells the whole answer. A graph is the graph of a convex polyhedron if and only if it is planar and 3-vertex-connected. It would be nice to get a similar complete characterization for the graphs of origami flat folding patterns, but I don't know of one.