---
layout: post
title: H-trees are not trees
date: 2026-04-01 21:09
---
A sheet of [a4 paper](https://en.wikipedia.org/wiki/International_standard_paper_sizes#A_series) has aspect ratio $$1:\sqrt2$$. This means you can crease it along the shorter of its two midlines to get two rectangles with the same aspect ratio (of a5 size) and continue in the same way recursively.

{: style="text-align:center"}
![A-series paper sizes. CC-BY-SA image https://commons.wikimedia.org/wiki/File:A_size_illustration.svg by Sven, 26 June 2006.]({{site.baseurl}}/assets/2026/htree/paper-sizes.svg){: style="width:100%;max-width:480px" }

Now, whenever you subdivide one rectangle into two smaller rectangles in this recursion, connect the centerpoints of the two new rectangles by a line segment. The union of all of these line segments is a fractal, the [H-tree](https://en.wikipedia.org/wiki/H_tree).

{: style="text-align:center"}
![An H-tree]({{site.baseurl}}/assets/2026/htree/htree.svg)

It comes arbitrarily close to any point of the initial rectangle, so its closure is the whole rectangle and its fractal dimension is two. But the points that belong to the H-tree (normalized with one corner of the rectangle at the origin) all have at least one coordinate that is a [dyadic rational](https://en.wikipedia.org/wiki/Dyadic_rational) multiple of one of the rectangle sides. So as a subset of a countable union of axis-parallel lines, the H-tree has measure zero.

At each finite level of recursive construction (using closed line segments) the union of the segments is a kind of topological tree called a [dendroid](https://en.wikipedia.org/wiki/Dendroid_(topology)). Roughly this means that its a connected compact set with a unique arc connecting each two points. The full H-tree is not compact (it is not closed: its closure is a different set, the whole rectangle). But this is not the only way that it is not tree-like: it no longer has the property of having a unique arc connecting each two points! This is because it has certain simple closed curves as subsets, within which you can connect pairs of points in two different ways around the curve.

{: style="text-align:center"}
![A simple closed curve in an H-tree]({{site.baseurl}}/assets/2026/htree/hloop.svg)

In this it differs from some other [fractal space-filling trees](https://en.wikipedia.org/wiki/Space-filling_tree) like the one below, which might be called an X-tree. An X-tree can be formed by recursively subdividing a square into four smaller squares, adding an open line segment for the diagonal of each square. Or, instead, you could form an X-tree the way my code drew it: start with a grid of a power of two size, draw the diagonals of the whole grid, and then remove (or redraw as white) the grid points whose coordinates have binary representations ending in differing numbers of $$0$$ bits. You can find arcs of the X-tree whose two ends get arbitrarily close to each other, but they do not form simple closed curves because their limit point is missing. Instead, in the H-tree, a branch of the tree can have an interior point of another segment as its limit point, so the limit point is not missing.

{: style="text-align:center"}
![An X-tree]({{site.baseurl}}/assets/2026/htree/xtree.svg)

Looking again at the H-tree, one can see additional tree-like structures in the negative space where the H-tree isn't.

{: style="text-align:center"}
![The forest forming the skeleton of the complement of an H-tree]({{site.baseurl}}/assets/2026/htree/hdual.svg)

It's common to see planar surfaces divided up by pairs of interdigitating trees: the two trees of a river network and of the ridgelines separating the river's branches are a familiar example.

{: style="text-align:center"}
![A 1690 map of the middle Rhine watershed. By Christoph Riegel from Landesarchiv Saarbrücken, https://commons.wikimedia.org/wiki/File:LASB_K_Hellwig_0096.jpg]({{site.baseurl}}/assets/2026/htree/middle-rhine.jpg){: style="width:100%;max-width:600px" }

I've used this idea of interdigitating trees in [several of my research papers](https://ics.uci.edu/~eppstein/pubs/graph-cotree.html) and in [several]({{site.baseurl}}{% post_url 2007-12-16-recent-reading-roundup %}) [old]({{site.baseurl}}{% post_url 2007-12-28-formal-knot-theory %}) [posts]({{site.baseurl}}{% post_url 2017-02-28-linkage %}) here. The complement of a tree would have a tree-like skeleton (for instance the X-tree has a $$45^\circ$$-rotated X-tree-like dual skeleton). But because the H-tree is not a tree, its interdigitated forest has many separate fractal trees. These trees are not exactly the same as the connected components of the complement of the H-tree: like the H-tree itself their points have one coordinate that is a dyadic rational multiple of the initial rectangle side, so they miss many points of the outer rectangle. But I think they have the same closures as the connected components.