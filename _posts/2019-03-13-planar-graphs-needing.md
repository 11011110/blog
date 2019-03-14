---
layout: post
title: Planar graphs needing many lines
date: 2019-03-13 18:37
---
As I said in [my previous post]({{site.baseurl}}{% post_url
2019-03-12-counting-polygon-triangulations %}) my two SoCG papers both
involved trying and failing to prove something else, and writing down
what I could prove instead. For the one that appears today, "Cubic
planar graphs that cannot be drawn on few lines" ([arXiv:1903.05256](http://arxiv.org/abs/1903.05256)),
that something else was Open Problem 16.14 of my book, which can be
rephrased as: does there exist a family of planar graphs that cannot be
drawn planarly with all vertices on a constant number of convex curves?

Instead I expand on something that was already known, the existence of
planar graphs that cannot be drawn with all vertices on a constant
number of lines.

There were two previously known methods for constructing such graphs:

* Use a [planar
3-tree](https://en.wikipedia.org/wiki/Apollonian_network). This
is a planar graph formed by recursively subdividing triangles into three
smaller triangles. If the vertices are drawn on some family of lines,
the line through the subdivision point must miss one of the three
smaller triangles, so by induction you can be forced to use a
non-constant number of lines. But the bound you get is only logarithmic.[^book]

{: style="text-align:center"}
![Planar 3-tree]({{site.baseurl}}/assets/2019/planar-3-tree.svg)

* Use a maximal planar graph whose dual graph has no long paths.
In a maximal planar graph, any line through many vertices can be
translated into a path through many dual vertices. So if there is no
long dual path there must be many lines. This gives a polynomial lower
bound on the number of lines, but with a tiny exponent.[^dual]

The new paper finds a third method:

* Use a graph that has many disjoint collections of many nested cycles.
Drawing a big set of nested cycles on a small
number of lines necessarily uses up one of the crossing points of the lines.
So if there are more nests than crossing points, one of them will have
to use many lines.

{: style="text-align:center"}
![Graph with many disjoint collections of many nested cycles]({{site.baseurl}}/assets/2019/spiderwebs.svg)

This leads to stronger polynomial bounds, but also (more importantly I
think) wider families of planar graphs that need non-constant numbers of
lines. For instance, it works for series-parallel graphs of maximum
degree three, which are far from being maximal planar. And even though
every tree can be drawn with its vertices on two lines, adding a single
vertex to a tree can produce a graph that requires a non-constant number
of lines.

{: style="text-align:center"}
![Tree plus one vertex requiring a non-constant number of lines]({{site.baseurl}}/assets/2019/apex-tree.svg)

* Footnotes go here
{:footnotes}

[^book]: [_Forbidden Configurations in Discrete Geometry_](https://www.ics.uci.edu/~eppstein/forbidden/), Theorem 16.13.

[^dual]: Ravsky, Alexander, and Verbitsky, Oleg (2011), "[On collinear sets in straight-line drawings](https://doi.org/10.1007/978-3-642-25870-1_27)", _37th Int. Worksh. Graph-Theoretic Concepts in Computer Science (WG 2011)_, LNCS 6986, Springer, pp. 295–306; Chaplick, Steven, Fleszar, Krzysztof, Lipp, Fabian, Verbitsky, Oleg, and Wolff, Alexander (2016), "[Drawing graphs on few lines and few planes](https://doi.org/10.1007/978-3-319-50106-2_14)", _24th Int. Symp. Graph Drawing and Network Visualization (GD 2016)_, LNCS 9801, Springer, pp. 166–180.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/101747562081254313))