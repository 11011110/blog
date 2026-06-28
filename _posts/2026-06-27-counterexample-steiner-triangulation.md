---
layout: post
title: A counterexample for Steiner triangulation
date: 2026-06-27 17:52
---
I've been hesitating in writing up a blog post about my latest preprint, "[Minimum-weight Steiner triangulation of convex polygons
requires interior Steiner points](https://ics.uci.edu/~eppstein/pubs/p-mwst2.html)" (with my student Zahra Hadizadeh, [arXiv:2606.25302](https://arxiv.org/abs/2606.25302), to appear at CCCG) because, despite being a completely concrete two-dimensional construction, its exponential scale makes it difficult to visualize. In the paper we included an illustration using logarithmic coordinates but I didn't find that entirely satisfactory so I'm trying again in a different way here.

The new paper is about a problem from a much older paper of mine, "[Approximating the minimum weight Steiner triangulation](https://ics.uci.edu/~eppstein/pubs/p-mwst.html)" (SODA 1992 and _Discrete Comput. Geom._ 1994), on "Steiner triangulation", adding points to a geometric input to reduce the total edge length of a triangulation of the input. The added points are called Steiner points. The old paper proved that one could get within a constant factor of the minimum possible total edge length, for various kinds of inputs including point sets and convex polygons, using a method based on quadtrees. For convex polygons, you do sometimes need to add Steiner points; for instance the trapezoid below is optimally triangulated with one Steiner point (blue) on its long parallel side.

{: style="text-align:center"}
![A wide isosceles trapezoid with long and short parallel sides. Its minimum-weight Steiner triangulation includes a Steiner point at the midpoint of the long parallel side.]({{site.baseurl}}/assets/2026/steiner/trap.svg){:  style="width:100%;max-width:540px"}

However, in my earlier work I could only find examples of convex polygons whose optimal Steiner points were on the polygon boundary. When that is the case, the "weak dual" of the triangulation (the graph of triangles and their adjacencies with other triangles) forms a tree. This tree structure should make finding the best triangulation with this structure easier, amenable to dynamic programming algorithms, although there are some difficulties with numerics and nonlinear functions that would need to be overcome. In the older paper, I conjectured that 
interior Steiner points would never be needed and therefore that we could find optimal Steiner triangulations of convex polygons in polynomial time. The result of the new paper is that the conjecture is false: we construct a polygon whose optimal triangulation requires interior Steiner points.

To understand our counterexample, I think it might be helpful to start with a counter-counterexample, showing why it's not easy to construct counterexamples. More precisely, it's not possible to have an optimal interior Steiner point with at most six neighbors and a convex neighborhood. If you had a triangulation like that, you could find a better triangulation with fewer Steiner points by contracting the low-degree Steiner point into its closest neighbor.

{: style="text-align:center"}
![A steiner triangulation of a hexagon (blue shaded triangles) and its shorter non-Steiner triangulation obtained by contracting the Steiner point into its closest neighbor (red shaded triangles)]({{site.baseurl}}/assets/2026/steiner/hex.svg){:  style="width:100%;max-width:420px"}

In the example above, the Steiner point is $$S$$ and the closest of its six neighbors is $$A$$. Contracting $$AS$$ turns the blue shaded triangulation around $$S$$ into the red shaded triangulation, replacing the six edges $$SA$$, $$SB$$, $$SC$$, $$SD$$, $$SE$$, and $$SF$$ by the three edges $$AC$$, $$AD$$, and $$AE$$. Each added edge can be shown to be shorter than a pair of removed edges by using the triangle inequality and the assumption that $$A$$ is the nearest neighbor to $$S$$:

$$AC\le AS+SC\le BS+SC,$$

$$AD\le AS+SD,$$

$$AE\le AS+SE\le FS+SE.$$

Combining these inequalities gives

$$AC+AD+AE\le (BS+SC)+(AS+SD)+(FS+SE)$$

so the contracted non-Steiner triangulation is shorter than the Steiner triangulation.

This argument breaks down when a Steiner point has seven or more neighbors, because then there aren't enough removed edges to pair them up and use the triangle inequality. We found our counterexample to the conjecture by looking for neighborhoods for which, instead, contracting the Steiner point to its nearest neighbor produces a worse triangulation. The resulting convex polygon has an approximate kite shape, with exponentially-spaced sequences of vertices along the short sides of the kite (which are rounded slightly to make the result convex). It has 28 vertices, most of which cluster together near the point where the two short sides of the kite meet:

{: style="text-align:center"}
![The counterexample to the convex polygon Steiner triangulation conjecture, whole polygon view]({{site.baseurl}}/assets/2026/steiner/kite.svg){:  style="width:100%;max-width:540px"}

The next image is a close-up of this cluster, scaled by a factor of approximately 40, with the Steiner point (blue) and its incident edges also shown.

{: style="text-align:center"}
![The counterexample to the convex polygon Steiner triangulation conjecture, close-up view of the leftmost vertex, Steiner point, and triangulation edges]({{site.baseurl}}/assets/2026/steiner/fan.svg){:  style="width:100%;max-width:540px"}

Most of the edges incident to the Steiner point extend rightward, so
contracting the Steiner point into its nearest neighbor to the left would 
lengthen these edges. The same contraction would eliminate the three edges connecting the Steiner point to its three nearest neighbors, but those eliminated edges are very short relative to the number of lengthened edges.
A numerical calculation shows that, in fact, the Steiner triangulation is better than the triangulation obtained by connecting all vertices to the nearest neighbor of the Steiner point. More strongly, because of the exponential spacing of the points, that turns out to be the optimal non-Steiner triangulation. So for this polygon, there is a Steiner triangulation with an interior point that is better than any non-Steiner triangulation.

That's not quite enough to disprove the conjecture. The harder part of the paper, extending to multiple pages of appendices, is proving that there is no good Steiner triangulation using only boundary Steiner points. Therefore, the Steiner triangulation with this one interior Steiner point is better than any Steiner triangulation using only boundary Steiner points. It's (numerically) the optimal triangulation with a single symmetrically placed Steiner point. We didn't prove that it's the optimal Steiner triangulation, because (however implausible it might be) there might be some other way of placing interior Steiner points that is even better. But it's enough to disprove the conjecture, and prove that some convex polygons require interior Steiner points in their minimum-weight Steiner triangulations.