---
layout: post
title: A straight line through every face
date: 2022-11-21 22:08
---
While updating my online publications list for something else I noticed that I had neglected to discuss one of my papers from earlier this fall: "Geodesic paths passing through all faces on a polyhedron" (with Demaine, Demaine, Ito, Katayama, Maruyama, and Uno), in the [booklet of abstracts from JCDCG<sup>3</sup> 2022](https://www.rs.tus.ac.jp/jcdcggg/JCDCG3-2022Proceedings(r2).pdf), the Japanese Conference on Discrete and Computational Geometry, Graphs, and Games.

The paper is kind of telegraphic, but the question it considers is easily stated. On the surface of a polyhedron, the analogue of a straight line is a geodesic, the shortest curve between two points. Which polyhedra have geodesics that cross through all of their faces? Maybe the 2d version is easier to explain: any two points on a convex polygon split the polygon into two arcs, and a geodesic is the shorter of the two. Which polygons have at least one geodesic that includes a segment from each edge?

{: style="text-align:center"}
![Geodesics through all edges of a kite and a trapezoid]({{site.baseurl}}/assets/2022/2d-univ-geodesics.svg){: style="width:100%;max-width:600px" }

The endpoints of such a geodesic $$A$$ must be in different edges, because if they were in the same edge then the complementary arc $$\bar A$$ would be a straight line segment, shorter than any other arc. Those two edges must be adjacent, because otherwise $$\bar A$$ would include an edge missed by $$A$$. And these two adjacent edges must be longer than the sum of all the other edges, so that $$A$$ (a superset of the other edges) can be the shorter than $$\bar A$$ (a subset of the two adjacent edges). That turns out to be an exact characterization: a convex polygon has two points whose geodesic passes through all edges, if and only if it has two adjacent edges that together have more than half the perimeter. For these polygons, the arc $$A$$ can be chosen to have its endpoints near the outer vertices of the two long adjacent edges. So this is possible for all triangles, for any quadrilateral that is not a parallelogram, and for many other polygons of arbitrarily many sides. But it does not work for any centrally symmetric polygon, because each two adjacent sides are at least matched in length by the two opposite sides.

When we first discussed this problem (five years ago at a Barbados workshop), we started with the idea that no polyhedron with two parallel faces can have a geodesic through all faces. In particular, this would imply that the only regular polyhedron with a geodesic through all faces is a regular tetrahedron. But it's not true! Instead, if $$P$$ is any polygon with a geodesic through all edges, then long-enough right prisms over $$P$$ have geodesics through all faces.

Geodesics on the surface of a convex polyhedron may be easier to understand by unfolding the polyhedron into a [net](https://en.wikipedia.org/wiki/Net_(polyhedron)), a flat system of polygons in the plane, drawing the line segment between the endpoints of the geodesics in the net, and then folding it back up. The complication is that the line segment needs to stay inside the net, and there may be many different nets with different line segments.

Suppose $$P$$ is a polygon with a geodesic $$A$$ through all edges, like the yellow kite above. The prism over $$P$$ has two copies of $$P$$, connected by rectangles. It can be unfolded by unrolling the rectangles into one long rectangular strip, and connecting the two copies of $$P$$ to the top and bottom of the strip, as shown below. (The lightly shaded copy of $$P$$ is an alternative placement on the top of the strip; you should only keep one of the two top copies.) To make a curve through all faces on a prism over $$P$$,
attach each copy of $$P$$ along one of its two adjacent long edges, and arrange the rectangular strip with these two attached copies at opposite ends. Then, connect a point on the top copy of $$P$$, near the start of $$A$$ on that copy, to another point on the bottom copy of $$P$$, near the end of $$A$$ on that copy. The resulting curve is shown below as the red segment on its net.

{: style="text-align:center"}
![A geodesic through all faces of an unfolded prism over a kite (red) and a different curve that is not a geodesic (blue)]({{site.baseurl}}/assets/2022/prism-univ-geodesic.svg){: style="width:100%;max-width:600px" }

The red curve is definitely shorter than the curve that you would get by applying the same construction to $$\bar A$$, which would be drawn in its unfolding as a segment with the same height but greater width. But what we have to worry more about is the blue curve in the figure, which cuts through one of the rectangular sides of the prism before cutting straight across one of the copies of $$P$$. Could such a curve be shorter? It isn't in the figure (I measured), but what about more generally?

When the height of the prism is small, the blue curve can be shorter. But in the limit as the height of the prism gets much larger than the size of $$P$$, it cannot. The length of curves like the blue one, in the limit, approaches the height of the prism plus the height of the endpoint above the central rectangular region. Instead, in the limit, the length of curves like the red one approaches the height of the prism: the horizontal component of the curve contributes negligibly to its length. So for tall enough prisms the red curve is shorter than any curve like the blue one, and we have a universal geodesic. (You might think that attaching the top and bottom face in the middle of the rectangular strip would produce a shorter geodesic, and for the illustrated prism maybe it does, but as long as the endpoints are much closer to the edge of $$P$$ than to the corner of $$P$$, the same argument also applies to these alternative curves.)

Wataru Maruyama, a student of Hiro Ito and a coauthor of the paper, succeeded in proving that the other regular polyhedra indeed do not have universal geodesics. We could also prove that every tetrahedron or right prism over a triangle does have one. On the other hand, much more remains unknown. In particular, we do not have an answer to the following question: is there a centrally symmetric polyhedron with a universal geodesic?

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/109386054076782254))