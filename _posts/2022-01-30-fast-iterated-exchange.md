---
layout: post
title: Fast iterated exchange transformations via normal curves
date: 2022-01-30 17:34
---
Soon after I posted my preprint ["The Complexity of Iterated Reversible Computation" (arXiv:2112.11607)](https://arxiv.org/abs/2112.11607) last month (see [previous post "Raytracing diamonds"]({{site.baseurl}}{% post_url 2021-12-23-raytracing-diamonds %})), Mark Bell emailed me to observe that one of the problems I mentioned in it, iterated integer interval exchange transformations, could be solved in polynomial time by reinterpreting it as a problem on normal curves in triangulated surfaces and plugging in known results from computational topology. Here is a more detailed expansion of that observation.

First, some terminology, with a picture to help make sense of it:

{: style="text-align:center"}
![Integer interval exchange transformation represented as a normal curve on a triangulated surface]({{site.baseurl}}/assets/2022/normal-interval-exchange.svg)

Interval exchange transformation
: An [interval exchange transformation](https://en.wikipedia.org/wiki/Interval_exchange_transformation) is a transformation of an interval, obtained by dividing it up into subintervals, permuting the subintervals, and concatenating them back together in the permuted order to obtain the starting interval. They have been widely studied in the theory of dynamical systems. The picture above is derived from an interval exchange transformation on four subintervals $$a$$, $$b$$, $$c$$, and $$d$$ (top edge of the rectangle), permuted into the new order $$b$$, $$d$$, $$c$$, $$a$$ (bottom edge of the rectangle).

Integer interval exchange transformation
: In order to obtain a transformation on a discrete set rather than a continuous interval, we restrict our attention to intervals of the number line, interval exchange transformations that map integers to integers on the number line, and the action of those transformations on the integers. More specifically, we can consider the $$N$$ integers from $$0$$ to $$N-1$$, for some $$N$$. The one in the picture has $$N=15$$, with the integer positions on the number line shown as vertical blue line segments.

: An integer interval exchange transformation can be specified by listing the largest integer in each interval, in permuted order: here, this permuted list is $$5, 14, 6, 3$$. If there are $$k$$ intervals, this specification has bit-length $$O(k\log N)$$ and so to achieve polynomial time we will want a time bound that is polynomial in $$k$$ and $$\log N$$.

Iterated interval exchange transformation
: Given a number $$n$$, a starting value $$x$$, and a specified integer interval exchange transformation $$f$$, repeatedly apply $$f$$, $$n$$ times. What is the value $$f^{(n)}(x)$$ that results? For instance, the transformation shown takes $$0\to 11\to 6\to 8\to\cdots$$, so $$f^3(0)=8$$.

Surface
: The surfaces I have in mind are compact two-dimensional [oriented manifolds](https://en.wikipedia.org/wiki/Orientability) without boundary: topologically like a plane at every point, but globally having a different topology. They can be classified as the sphere, torus, two-handled torus, etc., but we won't need this classification. The rectangle in the figure can be interpreted as a surface if we glue the pairs of labeled edges together. The left and right sides of the rectangle, when glued together, make a cylinder. The top and bottom edges of the rectangle are glued according to the labeling shown, rather than just wrapping directly from top to bottom.

Triangulated surface
: Subdivide the surface into triangles, meeting edge-to-edge, as in the figure. For topological purposes the geometry of the surface is unimportant: all you need to know is the triangles and how they meet edge-to-edge.

Normal curve
: A normal curve, on a triangulated surface, is a curve that does not cross itself, does not pass through any triangle vertices, and when entering a triangle on one edge always leaves on a different edge. After gluing the rectangle to form a surface, the blue lines link up to form a normal curve.

Normal arc
: A normal curve can have more than one connected component; when it does, a single component is called an arc. The blue normal curve turns out to be an arc: it has only one component.

Normal coordinates
: The normal coordinates of a normal curve describe the curve by specifying, for each edge of a topological triangulation, how many times the normal curve crosses each edge. The normal coordinates on the labeled horizontal edges are $$N_a=4$$, $$N_b=2$$, $$N_c=1$$, and $$N_d=8$$. The normal coordinates on the vertical edges are all zero; the other edges interior to the rectangle have nonzero normal coordinates, which are just the numbers of times each edge is crossed by the blue curve.

: Not all assignments of numbers to triangulation edges work. For a triangle with edges $$x$$, $$y$$, and $$z$$, the normal coordinates $$N_x$$, $$N_y$$, and $$N_z$$ must obey the [triangle inequality](https://en.wikipedia.org/wiki/Triangle_inequality). You can read off how the curve crosses the triangle from these numbers: it has $$N_x+N_y-N_z$$ segments that cross from edge $$x$$ to edge $$y$$, etc. The triangle inequality ensures that these numbers of segments are all non-negative. A curve topologically equivalent to the given curve can be obtained by placing the given number of tick-marks on each edge and connecting them by non-crossing segments according to this formula.

Edge coordinates
: The edge coordinate of a point where a normal curve crosses an edge is just its position along the crossings on that edge.

Arc coordinates
: The arc coordinate of a point where a normal curve crosses an edge is its position among all of the crossings along the normal curve, in the order they are reached by that curve, after choosing an arbitrary starting point to have coordinate zero.

With all of this as setup, and with the algorithms on normal curves from a paper by Jeff Erickson and Amir Nayyeri, ["Tracing Compressed Curves in Triangulated Surfaces", _DCG_ 2013](https://doi.org/10.1007/s00454-013-9515-z), the rest is easy:

* Given an interval exchange transformation, construct a surface in the form depicted: a triangulated rectangle, divided into some number $$s$$ of horizontal stripes, with the input intervals to the transformation subdividing the top of the rectangle and the outputs subdividing the bottom. Triangulate it as shown in the figure, so that each vertical line through the rectangle crosses exactly one diagonal per slice, and so that the central horizontal line across the rectangle forms an unsubdivided edge. Each step up or down from this central line allows the number of horizontal subdivisions to double, so it suffices to let $$s=2\lceil\log_2 k\rceil$$, producing a triangulation with $$O(k)$$ triangles. Glue the left and right sides of the rectangle together, and glue top and bottom according to the labeling from the transformation.

* Compute the normal coordinates of the normal curve formed by the vertical integer lines in the rectangle. The normal coordinate of any edge is how far apart horizontally its endpoints are within the rectangle.

* Given the number $$x$$ whose iterates we want to compute, let $$p_x$$ be the point of the central horizontal line, $$x$$ steps from the left. Each iteration of the exchange transformation can be obtained by advancing $$2s$$ units upward along the curve, starting from $$p_x$$, and wrapping around halfway through from the top of the rectangle to the bottom.

* Find the normal arc containing $$p_x$$ and its normal coordinates (Erickson and Nayyeri, Theorem 6.2). Its length $$X$$ (measured as a number of crossings) is just the sum of these normal coordinates.

* Convert the known edge coordinate of $$p_x$$ to an arc coordinate (Erickson and Nayyeri, Theorem 6.3), add $$2ns$$ (modulo $$X$$) to this arc coordinate, convert the resulting arc coordinate back into an edge coordinate in its arc (Erickson and Nayyeri, Theorem 6.4), and then back into an edge coordinate in the whole curve. This edge coordinate is the number we want to compute, $$f^{(n)}(x)$$.

The topological subroutines used by this algorithm all take time quadratic in the size of the triangulation and logarithic in the number of crossings of the normal curve, so for the triangulation and normal curve constructed above this time bound is $$O(k^2\log N)$$.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/107714613861230488))