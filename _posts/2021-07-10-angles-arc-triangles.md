---
layout: post
title: Angles of arc-triangles
date: 2021-07-10 11:06
---
Piecewise-circular curves or, if you like, arc-polygons are a very old topic in mathematics. Archimedes and Pappus studied the [arbelos](https://en.wikipedia.org/wiki/Arbelos), a curved triangle formed from three semicircles, and Hippocrates of Chios found that the [lune of Hippocrates](https://en.wikipedia.org/wiki/Lune_of_Hippocrates), a two-sided figure bounded by a semicircle and a quarter-circle, has the same area as an isosceles right triangle stretched between the same two points. The history of the [Reuleaux triangle](https://en.wikipedia.org/wiki/Reuleaux_triangle), bounded by three sixths of circles, stretches back well past Reuleaux to the shapes of of Gothic church windows and its use by Leonardo da Vinci for fortress floor plans and world map projections. But despite their long history and frequent use (for instance in the design of machined parts), there are some basic properties of arc-polygons that seem to have been unexplored so far.

I looked at one of these properties, [the ability of arc-triangles to tile the plane]({{site.baseurl}}{% post_url 2021-05-09-arc-triangle-tilings %}), in an earlier post. Another of these properties involves the feasible combinations of angles of these shapes. As is well known, in a straight-sided triangle in the plane, the three interior angles always sum to exactly $$\pi$$, and any three positive angles summing to $$\pi$$ are possible. Let $$T$$ be the set of triples of angles $$(\theta_1,\theta_2,\theta_3)$$ from triangles, and reinterpret these triples as coordinates of points in Euclidean space. Then $$T$$ is itself an equilateral triangle, with corners at the three points $$(\pi,0,0)$$, $$(0,\pi,0)$$, and $$(0,0\pi)$$. (More precisely, it's the relative interior of this triangle.)

What about arc-triangles? Are their angles similarly constrained? What shape do their triples of angles make? First of all, their angles don't have a fixed sum (except for the tilers, for which this sum is again $$\pi$$). The arbelos has three interior angles that are all zero, summing to zero. The Reuleux triangle has three angles of $$2\pi/3$$, summing to $$2\pi$$. [Boscovitch's cardioid]({{site.baseurl}}{% post_url 2021-05-15-linkage %}), below, uses three semicircles like the arbelos, but with one interior angle of $$2\pi$$ and two others equal to $$\pi$$, summing to $$4\pi$$. The [trefoil](https://en.wikipedia.org/wiki/Trefoil), a common architectural motif, bulges outward from its three corners, forming interior angles that are much larger, up to $$2\pi$$ each for a trefoil made from three $$5/6$$-circle arcs, for a total interior angle of $$6\pi$$.

{: style="text-align:center"}
![Boscovich's cardioid]({{site.baseurl}}/assets/2021/boscovich.svg)

Nevertheless, for a non-self-crossing arc-triangle, not all combinations of angles are possible. For instance, it's not possible to have one angle that is zero and two that are $$2\pi$$. My new preprint, "Angles of arc-polygons and lombardi drawings of cacti" ([arXiv:2107.03615
](https://arxiv.org/abs/2107.03615), with UCI students Daniel Frishberg and Martha Osegueda, to appear at CCCG) proves a precise characterization: beyond the obvious requirement that each angle $$\theta_i$$ be in the range $$0\le\theta_i\le 2\pi$$, we have only the additional inequalities

$$-\pi < \frac{\pi - \theta_i + \theta_{i+1} - \theta_{i+2}}{2} < \pi$$

where the index arithmetic is done modulo three. The formula in the middle of each of these inequalities is itself an angle, the angle of incidence between one of the circular arcs of the arc-triangle and the circle through its three corners. Where the straight triangles had an equilateral-triangle feasible region, the arc-triangles have a more complicated shape. The obvious constraints $$0\le\theta_i\le 2\pi$$ would produce a cubical feasible region $$[0,2\pi]^3$$, but the additional inequalities above cut off six corners of the cube, leaving a feasible region looking like this:

{: style="text-align:center"}
![The feasible region for triples of angles of arc-triangles]({{site.baseurl}}/assets/2021/feasible-arc-triangles.svg)

The motivating application for all of this is graph drawing, and more specifically Lombardi drawing, in which edges are circular arcs meeting at equal angles at each vertex. Using our new understanding of arc-polygons, we prove that every [cactus graph](https://en.wikipedia.org/wiki/Cactus_graph) has a planar Lombardi drawing for its natural embedding (the one in which each cycle of the cactus forms a face) but might not for some other embeddings, including the one below.

{: style="text-align:center"}
![An embedded cactus that has no planar Lombardi drawing]({{site.baseurl}}/assets/2021/badhat.svg)

But beyond graph drawing, I think that the long history and many applications of arc-polygons justifies more study of their general properties. For instance, what about arc-polygons with more than three sides? What can their angles be? Our paper has a partial answer, enough to answer the questions we asked in our Lombardi drawing application, but a complete characterization for arc-polygons of more than three sides is still open.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/106557711895868173))