---
layout: post
title:  Pick's shoelaces
date:   2021-04-17 23:23
---
Two important methods for computing area of polygons in the plane are [Pick's theorem](https://en.wikipedia.org/wiki/Pick%27s_theorem) and the [shoelace formula](https://en.wikipedia.org/wiki/Shoelace_formula). For a simple lattice polygon (a polygon with a single non-crossing boundary cycle, all of whose vertex coordinates are integers) with $$i$$ integer points in its interior and $$b$$ on the boundary, Pick's theorem computes the area as

$$A=i+b/2-1.$$

The shoelace formula has various formulations, but in the version I'm going to use, it is a sum over oriented edges of the polygon. Let $$(x,y)\to (x',y')$$ denote an edge of the polygon that connects the two points $$(x,y)$$ and $$(x',y')$$, oriented in the clockwise direction around the polygon so that if you travel from $$(x,y)$$ to $$(x',y')$$ along this line segment, then the interior of the polygon will be on your right. Then, according to the shoelace formula, the area is

$$A= \frac{1}{2}\sum_{(x,y)\to (x',y')}(x'-x)(y'+y).$$

The shoelace formula looks messier than Pick's formula but it's much easier for computers to evaluate, both because polygons are generally represented in computers by their boundary rather than by the points they contain, and because there are often many fewer boundary edges than interior lattice points. It also doesn't need the coordinates to be integers. But since these two formulas produce the same value, it would be interesting to see a more direct relation between them, explaining one formula in terms of the other.

Proof of the shoelace formula
=============================

It is convenient to shift the polygon to lie entirely above the $$x$$-axis, without changing its area or number of grid points. After this shift, the nonzero terms $$\tfrac{1}{2}(x'-x)(y'+y)$$ of the shoelace formula can be interpreted as the signed areas of trapezoids, extending vertically down from each non-vertical edge $$(x,y)\to (x',y')$$ to the $$x$$-axis. The reason for doing this shift is to orient all of the trapezoids the same way, downwards from their edges, and to avoid complications with edges that cross the $$x$$-axis.

{: style="text-align:center"}
![Trapezoids extending downward from each edge of a polygon]({{site.baseurl}}/assets/2021/pick-trapezoids.svg)

Now consider what you would see from a generic point in the upper half-plane, if you looked straight upwards. (By "generic", I mean that the point isn't on an edge or directly below a vertex, because these would introduce additional and unimportant cases to our analysis.) Your line of site would pass through a sequence of zero or more polygon edges, whose trapezoids have positive sign when the line passes from inside the polygon to outside and negative sign when the line passes from outside to inside. Because of this alternation between inside and outside, between positive and negative, a point outside the polygon sees equally many edges of each sign, but a point in the polygon sees one more positive edge than negative.

Another way of expressing the same counts of signed edges above each point involves the _characteristic functions_ of the polygon and the trapezoids, functions that are 1 inside each shape and zero outside it. The area of a shape is just the integral of its characteristic function. We'll leave these functions undefined on the boundary of the shapes, but that's ok because the boundary points contribute nothing to the total area. Then because of the cancellation between positive and negative signs, at the generic points where all of these functions are defined, the characteristic function of the polygon equals the signed sum of  characteristic functions of trapezoids. By the sum rule for integrals, the area of the polygon equals the signed sum of trapezoid areas. With a little more complication, the same argument can also be made to work directly for unshifted polygons.

Counting lattice points in trapezoids
=====================================

Can we use the same argument to prove Pick's theorem, in the form that the shoelace formula equals Pick's formula?  We'd like to interpret each term of the shoelace formula as a count over grid points, decompose the polygon in the same way into a sum of trapezoids, and argue that counting points in each trapezoid and then summing produces the same result as summing the trapezoids and then counting points. The difficulty is that now we can't ignore the points on the axis or on boundary of the trapezoids, because their contribution to the count is nonzero.

First, let's see how we can interpret each shoelace term as a grid point count.
Rotating a trapezoid around the midpoint of its defining edge produces another trapezoid whose union with the first trapezoid is an axis-aligned rectangle. Pick's theorem is easy to see for these rectangles, in the simplified form that the area is the sum of one unit for integer points inside the rectangle, half a unit for integer points on its edges, and a quarter of a unit for integer points at its vertices. These fractional numbers of units are merely the amounts of rectangle area nearest to each point.

{: style="text-align:center"}
![The area of a lattice trapezoid equals the sum of units of lattice points: a whole unit for points in the trapezoid, half a unit on the boundary, and a quarter unit for the four corners]({{site.baseurl}}/assets/2021/pick-rectangle.svg)

For the trapezoids we will use the same assignment of units to lattice points: one unit for points in the trapezoid, half on its boundary, and a quarter at its vertices, regardless of the actual trapezoid angles at those vertices. The figure above shows each point decorated in blue with its number of units.
The equality of area with total units still holds true, because both the area of the trapezoid and the total number of units for its integer points are half that of the rectangle. Each point off the edge that contributes its units to the trapezoid has a reflection that does not contribute its units. And each point on the edge contributes half its units to the trapezoid and half to the reflection. So the same terms $$\tfrac{1}{2}(x'-x)(y'+y)$$ of the shoelace formula also count the contributions of units in each trapezoid to Pick's formula.

Pick's formula from sums of trapezoids
======================================

We know how much each lattice point contributes to Pick's formula: one unit if it is inside the polygon, half if it is on the boundary, or zero if it is outside. We also know how much each lattice point contributes to each trapezoid of the shoelace formula: one unit if it is interior to the trapezoid, half if it is on an edge, a quarter if it is on a corner, and none if it is exterior. In order to prove that Pick's formula and the shoelace formula are equal, we want to show that all points make equal contributions. And for most points, this turns out to be true.

The vertical ray from any point $$p$$ may pass through the boundary of the polygon in multiple ways: $$p$$ itself may lie on the boundary, the ray may cross an edge of the boundary, it may pass through a vertex of the boundary that has edges to its left and right, or it may brush past the boundary at a vertex that has edges only to the left or only to the right. We can skip over these last "brush past" cases, because the two trapezoids from these edges have opposite signs and cancel each other in the total trapezoid contribution of $$p$$. If $$p$$ lies on an edge, then it gets a (positive or negative) contribution of $$1/2$$, and when $$p$$ is a vertex of the polygon with edges extending left and right, then it gets the same contribution in two quarters. The remaining cases make a contribution of $$\pm 1$$, and as for the area calculation they alternate in sign. Canceling these alternating contributions shows that $$p$$ always has a total contribution from its trapezoids equal to its contribution to Pick's formula.

I thought at first that the points on the $$x$$-axis might need a different calculation, because they get only half as much from each trapezoid. But half zero is still zero; they contribute nothing to the sum of trapezoids and nothing to the Pick formula. The points that do need special treatment are the polygon vertices at which the two incident edges do not extend to the left and right, either because one is vertical or because both extend in the same direction. The contribution to Pick's formula for these vertices is still $$1/2$$, but the total contribution from the trapezoids is either an integer (if the incident edges extend in the same direction) or a quarter-integer (if one edges is vertical). So we'll have to count how much we've missed at those points.

Consider driving around the polygon clockwise, in the same direction that we oriented the edges. As you drive, you can make a right turn (from rightward to vertically down, vertically down to leftward, etc), a double-right u-turn, a left turn, or a double-left turn. Points at which the polygon makes an angle but continues in the same general left-to-right or right-to-left direction don't count as turns. Then at each right turn Pick's formula will run a deficit of 1/4 unit in total contributions, compared to the sum of trapezoids. A double-right u-turn gives a deficit of 1/2 unit, the same as two right turns. A left turn gives 1/4 more unit to Pick than to the sum of trapezoids, and a double-left gives 1/2 more unit. To return to your starting direction, you must make four more right turns than left, so the total difference in contributions from these terms comes out to exactly the $$-1$$ correction term in Pick's formula.

{: style="text-align:center"}
![Differences in contributions at turning points of the e polygon]({{site.baseurl}}/assets/2021/pick-deficits.svg)

In summary, when we sum contributions over all points, the points inside the polygon contribute one unit to Pick's formula and one unit to the sum of trapezoids. The points outside the polygon contribute zero to both. The points on the boundary that are not turns contribute $$1/2$$ to both. And the points on the boundary that are turns contribute different amounts to Pick's formula and to the sum of trapezoids, with the total of these differences equalling the $$-1$$ correction term in Pick's formula. Therefore, the overall value of Pick's formula equals the sum of point contributions in trapezoids, which equals the signed sum of trapezoid areas, which equals the polygon area.

Generalizations of Pick's formula
=================================

The same idea lets us generalize Pick's formula to a polygon with holes, defined as a connected region of the plane whose boundary is a disjoint union of simple polygons. The shoelace formula for area in the version we're using here, and its proof, need no change for this generalization. For each hole, we should drive counterclockwise rather than clockwise, to stay consistent with the orientation we have given the edges; the same argument shows that each hole produces a positive, rather than negative, total difference between the contributions to Pick's formula and to the shoelace formula. Therefore, for a polygon with $$h$$ holes, the total area becomes

$$A=i+b/2+h-1.$$

The basic idea for all this, by the way, comes from the paper "Pick's theorem", by Branko Grünbaum and G. C. Shephard ([_Amer. Math. Monthly_ 1993](https://doi.org/10.2307/2323771)). Rather than using the trapezoid version of the shoelace formula, Grünbaum and Shephard use a version of the formula that sums, over each edge of the polygon, the signed area of the triangle formed by each edge plus the origin. I think this makes the analysis a little messier, but it's otherwise much the same as the analysis here. The formula for polygons with holes can be found in "On the compactness of subsets of digital pictures" by Sankar and Krishnamurthy ([_CGIP_ 1978](https://doi.org/10.1016/s0146-664x(78)80021-5)) but without the careful definition of polygons with holes that is necessary to avoid problems here.

Grünbaum and Shephard also generalize Pick's formula in a slightly different direction: rather than allowing separate holes in their polygons, they define polygons to have only one boundary polygon, but they allow that polygon to cross itself. Their version of Pick's theorem for this kind of generalized polygons sums a certain half-integral index of each lattice point (essentially, the winding number of the polygon around that point, averaged between open and closed versions of the polygon), with a correction term coming from the turning number of the whole polygon. It should be possible to combine both generalizations, and allow polygon boundaries that both cross and have multiple components. There's a little ambiguity about which way the boundary is connected at vertices of degree higher than two, though, which would need to be resolved somehow if such vertices are to be allowed, because different choices are likely to cause pieces of the boundary to have different orientations leading to different areas.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/106084926459254807))