---
layout: post
title: Circles crossing at equal angles
date: 2018-12-22 14:39
---
Let $$A$$, $$B$$, $$C$$, and $$D$$ be four circles, with pairs $$AB$$, $$BC$$, $$CD$$, and $$DA$$ crossing at equal angles (and no crossings among the other two pairs). Then it turns out that the two curvy quadrilaterals forming the inside and outside boundaries of the union of disks each have a circle through their four vertices:

{: style="text-align:center"}
![Four circles crossing at equal angles, and the two circles through their crossing points]({{site.baseurl}}/assets/2018/4circle-45.svg)

The proof of the theorem is not difficult, once you notice that it's invariant under Möbius transformations: the four given circles and their crossing angles transform to another four circles with the same crossing angles, preserving any cocircularities among the eight crossing points.
So start by finding a Möbius transformation that makes two opposite circles $$A$$ and $$C$$ become the same size as each other. Because of the equality of crossing angles, both of the other two circles must have centers on the perpendicular bisector to line $$AC$$. There's still a one-dimensional family of Möbius transformations remaining that preserves the position of $$A$$ and $$C$$ but moves the other circles along this bisector; use this remaining degree of freedom to move the other two circles so that their centers are equidistant from line $$AC$$. Then, because of the equality of crossing angles, circles $$B$$ and $$D$$ must have the same radii. So we have transformed the input to a position where the circles are centered at the vertices of a rhombus with opposite pairs having the same radius. By symmetry, the crossing points must lie on two rectangles, and the four corners of each rectangle are cocircular.

{: style="text-align:center"}
![Four circles crossing at equal angles at the corners of a rhombus, and the two rectangles through their crossing points]({{site.baseurl}}/assets/2018/4circle-rect.svg)

This can be extended to some configurations of circles where the opposite pairs cross each other rather than staying disjoint, but you have to be more careful about what happens when more than two circles cross at one point, and about determining which of the two supplementary angles at each crossing to use as the crossing angle of the two circles. If you're not careful, you get situations like the one below  where two degenerate circles (the coordinate axes) are crossed at equal angles by two more circles, but where the eight crossings do not form another two circles.

{: style="text-align:center"}
![Two degenerate circles (the coordinate axes) and two circles that cross them at equal angles, without forming two more sets of four cocircular points]({{site.baseurl}}/assets/2018/4circle-bad.svg)

Maybe the easiest way to state the more general result is that if a non-self-crossing quadrilateral with circular-arc sides has four equal interior angles at its vertices, then it is [cyclic](https://en.wikipedia.org/wiki/Cyclic_quadrilateral).
I used a special case of this, for right-angled quadrilaterals, in my paper "A Möbius-invariant power diagram and its applications to soap bubbles and planar Lombardi drawing" ([_Discrete Comput. Geom._ 2014](https://doi.org/10.1007/s00454-014-9627-0)).
This formulation also works for the special case when all four angles are zero, which was used in a mesh generation algorithm by Bern, Mitchell, and Ruppert ("Linear-size nonobtuse triangulation of polygons", [_Discrete Comput. Geom._ 1995](https://doi.org/10.1007/BF02570715)).

{: style="text-align:center"}
![A chain of four tangent circles and a fifth circle through their four points of tangency]({{site.baseurl}}/assets/2018/4circle-cusp.svg)

I don't know whether this theorem has appeared previously, but it's obviously related to [Miquel's six-circle theorem]({{site.baseurl}}{% post_url 2006-03-22-miquels-six-circles%}), which takes five circles (without assumption about angles) and produces a sixth in a configuration closely resembling what you get from the four given circles and two produced circles of this theorem.