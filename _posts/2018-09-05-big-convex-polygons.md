---
layout: post
title: Big convex polygons in grids
date: 2018-09-05 08:45
---
How many corners can a convex polygon in a $$5\times 5$$ grid of points have?
My book [_Forbidden Configurations in Discrete Geometry_](https://www.ics.uci.edu/~eppstein/forbidden/) starts most of its sections with a small puzzle, and this is the one I used for Chapter 4. If you need a spoiler, it's also in the book, as Figure 11.3. More generally one can ask for the biggest convex polygon in an $$n\times n$$ grid, measuring the size of a polygon by its number of corners. I don't know how to solve this problem exactly for all $$n$$, but I can solve it for infinitely many choices of $$n$$, and give a solution that is within an additive constant of optimal for all $$n$$.

To explain the solution, let's start with a seemingly different problem: finding the minimum perimeter convex $$k$$-gon in an infinite grid. Again we will be able to solve it for infinitely many values of $$k$$, but not for all $$k$$. The optimal perimeter is not a nice number: each edge length is the square root of an integer, by Pythagoras, so the perimeter is the sum of many square roots. Being able to tell whether one sum of many square roots is smaller than another is [notoriously difficult](http://cs.smith.edu/~jorourke/TOPP/P33.html), but fortunately we won't need to do this.

If we don't care whether the result is a convex polygon, and instead seek the shortest convex [polygonal chain](https://en.wikipedia.org/wiki/Polygonal_chain) with $$k$$ edges, the problem becomes much easier. A polygonal chain is just a sequence of line segments meeting up end-to-end, and let's define it to be convex if the line segments consistently turn clockwise relative to each other at each endpoint (regardless of whether that might cause it to spiral around and cross itself). The sides of the shortest convex chain must be a set of $$k$$ directed line segments, no two parallel to each other (although they can be antiparallel) and are as short as possible subject to that constraint. So all we need to do is to generate line segments in order by length until we have enough of them.
Once we generate these $$k$$ shortest no-two-parallel line segments, we can construct a convex chain from them by sorting them by angle and then translating them so that they meet up end-to-end. For instance, here's the solution for $$k=9$$:

{: style="text-align:center"}
![Minimum-length 9-edge convex grid chain]({{site.baseurl}}/assets/2018/9-chain.svg)

Generating the $$k$$ shortest line segments can be simplified by moving the start of each line segment to the origin.
Then it becomes equivalent to finding the $$k$$ nearest _primitive_ grid points to the origin, the points that are not multiples of other nearer points.
In an earlier post I already looked at [generating the $$k$$ nearest grid points to the origin]({{site.baseurl}}{% post_url 2016-07-04-streaming-integer-points %}), without requiring them to be primitive. But the primitive line segments form a constant fraction of all of them. This fraction $$6/\pi^2$$ can be derived (at least heuristically) by observing that (for a random grid point within some specified distance of the origin) each prime $$p$$ has probability $$1/p^2$$ of dividing both coordinates. If we pretend that these probabilities are all independent, then the [Euler product](https://en.wikipedia.org/wiki/Euler_product)

$$\prod_{\text{prime }p} 1-\frac{1}{p^2} = 1\Big/\Bigl(\sum_{i=1}^{\infty}\frac{1}{i^2}\Bigr)$$

gives the probability of being primitive, and Euler's solution to the [Basel problem](https://en.wikipedia.org/wiki/Basel_problem) gives the sum as $$\pi^2/6$$. So if we generate a factor of $$\pi^2/6$$ more vectors than we need, sort them all by slope, and then eliminate duplicate slopes, we'll get the primitive line segments that we want.

In the example above, the chain ended up at a different point than where it started. But if it doesn't, we get a convex $$k$$-gon that has the minimum length among all convex $$k$$-chains, which must be the minimum-perimeter $$k$$-gon that we seek. To force the chain to close up into a polygon, pair up each primitive line segment with its antiparallel segment, the one with the same slope and opposite direction. If we generate segments in an order that makes each antiparallel pair consecutive, the resulting polygonal chain will close up. This works for every even $$k$$, but for odd $$k$$, there isn't always a way of choosing a minimum-length chain that closes up. In that case we need to do something trickier, and I don't know of any good construction for the shortest polygon that works for all odd $$k$$.

The next step towards the solution of the biggest grid polygon problem is to switch from the Euclidean length of line segments to their length in the [Manhattan metric](https://en.wikipedia.org/wiki/Taxicab_geometry). In this metric, the length of a line segment from $$(x_1,y_1)$$ to $$(x_2,y_2)$$ is $$\vert x_1-x_2\vert +\vert y_1-y_2\vert$$, the length of the shortest path that connects the endpoints using only horizontal and vertical segments. The algorithm for generating shortest convex polygonal chains is the same as before: generate the shortest $$k$$ line segments, no two parallel, sort them by slope, and connect them together into a single chain. The Manhattan metric has more ties in the sorted ordering of line segments, but this is not problematic — in fact it can help, by making it easier to choose sets of the $$k$$ shortest vectors that close up to form a convex polygon. When they do close up, we get a convex polygon with the shortest Manhattan perimeter. This can be made to happen for every even $$k$$ by generating antiparallel pairs of line segments consecutively.

The Manhattan perimeter may sound like a strange concept, but for convex polygons it has a very familiar description in terms of Euclidean geometry: it is the same as the perimeter of the [smallest bounding box](https://en.wikipedia.org/wiki/Minimum_bounding_box) of the polygon. Whenever this bounding box happens to be a square, it also gives us the smallest grid square that contains a convex $$k$$-gon. And if we happen to know that the same square doesn't contain a convex $$(k+1)$$-gon, we have found that k is the largest $$k$$-gon in this square, the solution to the problem we started with.

We were able to get convex chains to close up to polygons by grouping them in antiparallel pairs. We can get them to have square bounding boxes by grouping them in a different way: Form tuples of four equal-length vectors, all $$90^\circ$$ rotations of each other. If we generate segements in sorted order by Manhattan length, making sure to generate each 4-tuple consecutively, then whenever $$k$$ is a multiple of four the resulting polygon will be symmetric under 90 degree rotations so its bounding box will be a square. The minimum Manhattan length of a $$(k+1)$$-segment convex polygonal chain is larger by the length of the $$(k+1)$$st line segment, so the same square cannot contain a convex $$(k+1)$$-gon. This gives us our infinite family of biggest polygons in square grids, for $$k$$ divisible by four and for the grids whose perimeter is between the Manhattan perimeter of the optimal $$k$$-gon (inclusive) and the Manhattan length of the optimal $$(k+1)$$-chain (exclusive).

Using the same analysis we can also get a lower bound on the side length of the smallest square that contains a convex $$k$$-gon, for any $$k$$ regardless of whether $$k$$ is a multiple of four. To do so, compute the minimum Manhattan length of a $$(k+1)$$-segment convex polygonal chain, divide by four, and round up. When $$k$$ is $$2$$ mod $$4$$, and the Manhattan length $$\ell$$ of the $$k$$th-shortest line segment is odd, this lower bound again gives the correct answer for the minimum bounding square of a convex $$k$$-gon. The reason is that we can always choose the last two line segments to be the segment from the origin to $$(\lfloor\ell/2\rfloor,\lceil\ell/2\rceil)$$ and its reverse, very close to having slope $$1$$. With these line segments, we get a bounding rectangle whose two side lengths differ by one, and this rectangle fits into the square that you get by rounding up the perimeter to a multiple of four. The same idea (with $$(1,1)$$) also works for $$k=6$$, even though $$\ell$$ is even in this case.

Using this method, and making the easy observation that reducing $$k$$ can't increase the square size, gives the following table of shortest chains (in Manhatten length), lower bounds on the side length of the optimal square, and actual side length of the optimal square:

{:style="border: 1px solid black;padding: 10px;margin-left:auto;margin-right:auto"}
|:---------------:|:---------------:|:--------------:|:----------------:|
|&nbsp;$$k$$&nbsp;|&nbsp;chain&nbsp;|&nbsp;l.b.&nbsp;|&nbsp;square&nbsp;|
|:---------------:|:---------------:|:--------------:|:----------------:|
| 3               | 3               | 1              | 1                |
| 4               | 4               | 1              | 1                |
| 5               | 6               | 2              | 2                |
| 6               | 8               | 2              | 2                |
| 7               | 10              | 3              | 3                |
| 8               | 12              | 3              | 3                |
| 9               | 15              | 4              | __??__           |
| 10              | 18              | 5              | 5                |
| 11              | 21              | 6              | 6                |
| 12              | 24              | 6              | 6                |
| 13              | 27              | 7              | __??__           |
| 14              | 30              | 8              | 8                |
| 15              | 33              | 9              | 9                |
| 16              | 36              | 9              | 9                |
| 17              | 40              | 10             | __??__           |
|:---------------:|:---------------:|:--------------:|:----------------:|

&nbsp;

We can then find the biggest polygon in an $$n\times n$$ grid by searching this table for the largest $$k$$ whose square side is at most $$n$$. When there are question marks in the table, we can approximate the solution by using the largest $$k$$ that is not a question mark. Because every fourth row of the table is not a question mark, our approximation will be off by at most three from the true answer.

The puzzle from the book is the first question mark: can we fit a $$9$$-vertex convex grid polygon into a square with side length $$4$$? (Note that the side length, $$4$$, is one less than the number of grid points on a side, $$5$$.) Here's an answer to the second question mark, a $$13$$-vertex convex grid polygon fitting optimally into a square with side length $$7$$.

{: style="text-align:center"}
![Convex 13-gon in an 8x8 grid]({{site.baseurl}}/assets/2018/grid-13-gon.svg)

Because there is usually a lot of wiggle room to choose which line segments to use,
I would expect the lower bound to be tight for many more choices of $$k$$ than the ones identified above. But it's not always tight, and
the third question mark in the table, $$k=17$$, is the first case where it isn't. It's not possible to fit a $$17$$-gon into a square grid with side length 10, because the only way to get a  $$17$$-step convex polygonal chain of Manhattan length $$40$$ is to use all $$16$$ line segments with Manhattan length $$1$$, $$2$$, or $$3$$, and a single line segment (like the longest one in the $$13$$-gon) with Manhattan length $$4$$. But because the $$16$$ shorter line segments are a symmetric set, adding one more line segment to them can never produce a chain that closes up to form a polygon. The same thing happens for infinitely many other values of $$k$$. Determining a complete answer to when the lower bound is or isn't tight doesn't isn't obvious to me.

I suspect very little of this is actually new, although I don't know of references for these precise statements. The biggest polygon in a grid square was considered asymptotically by 
Dragan Acketa and Joviša Žunić ["On the maximal number of edges of convex digital polygons included into an $$m\times m$$-grid", [_JCTA_ 1995](https://doi.org/10.1016/0097-3165(95)90058-6)], who showed that

$$k\approx 2\pi\Bigl( \frac{n}{12} \Bigr)^{3/2}.$$


Imre Bárány and Maria Prodromou ["On maximal convex lattice polygons inscribed in a plane convex set", [_Israel J. Math._ 2006](https://doi.org/10.1007/BF02773612)] generalized this to other shapes than squares. The minimum perimeter version of the problem was already considered, again asymptotically, by Vojtěch Jarník ["Über Gitterpunkte in konvexen Kurven", _Math. Z._ 1926], the same Jarník as the namesake of the minimum spanning tree algorithm. For a survey of related problems see Bárány's "[Extremal problems for convex lattice polytopes: a survey](http://www.renyi.hu/~barany/cikkek/psurveyAMS.pdf)" [[_Contemp. Math._ 2009](https://doi.org/10.1090/conm/453/08796)].

([G+](https://web.archive.org/web/20190210023249/https://plus.google.com/100003628603413742554/posts/MFqdV8QKD65))