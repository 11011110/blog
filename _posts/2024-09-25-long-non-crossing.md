---
layout: post
title: Long but non-crossing paths and cycles
date: 2024-09-25 21:44
---
A [polygonalization](https://en.wikipedia.org/wiki/Polygonalization) of a set of points in the plane is a non-self-crossing polygon using all the points as vertices. One way to prove that it always exists is to observe that the [traveling salesperson tour](https://en.wikipedia.org/wiki/Travelling_salesman_problem) is always a polygonalization, because any two crossed edges can be uncrossed in two different ways, one of which preserves the connectivity of the tour, and this cannot increase the tour length. So if minimizing tour length eliminates all crossings, surely maximizing tour length must introduce as many crossings as possible, right?

This is the subject of a recent paper by ten authors including myself: "[Noncrossing longest paths and cycles](http://people.scs.carleton.ca/~michiel/NoncrossingLongCycles.pdf)", by Greg Aloupis, Ahmad Biniaz, Jit Bose, Jean-Lou De Carufel, me, Anil Maheshwari, Saeed Odak, Michiel Smid, Csaba Tóth, and Pavel Valtr, most of whom worked together on this at the 10th Annual Workshop on Geometry and Graphs in Barbados last year. It was presented last week at Graph Drawing 2024, for which the [program has links to preliminary versions of all papers](https://graphdrawing.github.io/gd2024/pages/program/), at least until the published proceedings is ready.

Three points, or four points in non-convex position, have no crossings, but for larger numbers of points in general position a crossing is always possible. In [a recent paper in _Graphs and Combinatorics_](https://doi.org/10.1007/S00373-023-02734-9), Jose Luis Álvarez-Rebollar, Jorge Cravioto-Lagos, Nestaly Marín, Oriol Andreu Solé-Pi, and
Jorge Urrutia conjectured that sets of five or more points in general position always have crossings in their longest cycles (maximum traveling salesperson tours) and asked whether they also have crossings in their longest paths (maximum traveling salesperson paths). Our new work provides strong counterexamples to both questions: for <span style="white-space:nowrap">all $$n$$,</span> there exist sets of $$n$$ points in general position in the plane with a non-crossing longest cycle, and sets of $$n$$ points with a non-crossing longest path.

The path construction for even numbers of points is simplest. Its basic ideas are:

* All points will be placed close to the <span style="white-space:nowrap">$$x$$-axis,</span> with <span style="white-space:nowrap">$$x$$-coordinate</span> much larger <span style="white-space:nowrap">than $$y$$,</span> so that the differences in <span style="white-space:nowrap">$$x$$-coordinate</span> dominate their distances.

* If the <span style="white-space:nowrap">$$y$$-coordinates</span> are zero, and the points are placed with half of their $$x$$-coordinates positive and half negative, then the (many) equally longest paths all start and end at the two middle points, with their edges all crossing the <span style="white-space:nowrap">$$y$$-axis.</span> Edges that do not cross the axis can be paired off on both sides of the axis and replaced by longer pairs of edges that cross. Among paths where all edges cross the axis, the total length is the sum of distances to the axis, doubled for non-endpoints, so the endpoints should be the two middle points.

* We can use equally spaced <span style="white-space:nowrap">$$x$$-coordinates,</span> half positive and half negative, perturbed by very small <span style="white-space:nowrap">$$y$$-coordinates.</span> The longest path will continue to have all edges crossing the <span style="white-space:nowrap">$$y$$-axis,</span> but the perturbation will force one such path to be longest. (The construction for an odd number of points uses a slightly uneven placement that is not important for this post.)

* When we perturb two points, the length of their edge increases (compared to its length with zero <span style="white-space:nowrap">$$y$$-coordinates)</span> by an amount that can be calculated by the Pythagorean theorem to be

  $$\frac{\Delta_y^2}{2\Delta_x}\bigl(1+o(1)\bigr),$$

  where $$\Delta_x$$ <span style="white-space:nowrap">and $$\Delta_y$$</span> are the differences in <span style="white-space:nowrap">$$x$$- and $$y$$-coordinates,</span> assuming $$\Delta_x\gg\Delta_y$$.

* Our perturbation will assign exponentially increasing <span style="white-space:nowrap">$$y$$-coordinates</span> to the points, with the largest perturbations going to the points closest to the <span style="white-space:nowrap">$$x$$-axis,</span> except for leaving one of the two middle points unperturbed.

* Because of this exponential growth, the terms $$\Delta_y$$ in the length increase are up to a small error term the same as the <span style="white-space:nowrap">$$y$$-coordinates</span> themselves, regardless of the choice of path. But different paths can pair up different $$\Delta_y$$ terms with different $$\Delta_x$$ terms. To get the longest path, we should pair up the largest $$\Delta_y$$ term (coming from the edge incident to the highest point) with the smallest $$\Delta_x$$ term (coming from the non-middle vertex closest to the other side of the <span style="white-space:nowrap">$$x$$-axis),</span> and continue greedily choosing edges that at each step pair the highest remaining vertex with the non-middle vertex closest to the other side of the axis.

* The resulting unique longest path is uncrossed! Each edge connects two vertices that are consecutive when sorted by their <span style="white-space:nowrap">$$y$$-coordinates.</span> Because the edges span disjoint ranges of <span style="white-space:nowrap">$$y$$,</span> they cannot cross. In a not-to-scale view with untuned parameters, it looks something like the following.

{: style="text-align:center"}
![Schematic view of construction for a point set whose longest path has no crossings]({{site.baseurl}}/assets/2024/long-uncrossed-path.svg){: style="width:100%;max-width:720px" }

To construct uncrossed longest paths with odd numbers of points we choose <span style="white-space:nowrap">$$x$$-coordinates</span> a little more carefully, and then merely omit the topmost point. The cycle construction uses a similar idea, but in two variations depending on whether the number of points is supposed to be odd or even. For evenly many points we double each point except the first and last in the non-crossing path path and carefully place its two copies so that a thin polygon can zigzag in the same way as the path. For odd points we find a polygon that adds one vertex and two edges to the long path to connect it into a polygon. See the paper for details.