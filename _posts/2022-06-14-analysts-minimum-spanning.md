---
layout: post
title: The analyst's minimum spanning tree
date: 2022-06-14 08:47
---
Infinite sets of points in the Euclidean plane, even discrete sets, do not always have [Euclidean minimum spanning trees](https://en.wikipedia.org/wiki/Euclidean_minimum_spanning_tree). For instance, consider the points with coordinates

$$\left(i, \pm\left(1+\frac1i\right)\right),$$

for positive <span style="white-space:nowrap">integers $$i$$.</span> You can connect the <span style="white-space:nowrap">positive-$$y$$</span> points and the <span style="white-space:nowrap">negative-$$y$$</span> points into two chains with edges of length less than two, but then you have to pick one edge of length greater than two to span from one chain to the other. Whichever edge you choose, the next edge along would always be a better choice. So a tree that minimizes the multiset of its edge weights (as finite minimum spanning trees do) does not exist for this example. And as the same example shows, the sum of edge weights may be infinite, so how can we use minimization of this sum to define a tree?

{: style="text-align:center"}
![Discrete infinite set of points with no Euclidean minimum spanning tree]({{site.baseurl}}/assets/2022/ladder-no-mst.svg)

Despite that, here's a construction that works for any [compact set](https://en.wikipedia.org/wiki/Compact_space), even one with infinitely many components, and that generalizes easily to higher-dimensional Euclidean spaces. I think it deserves to be called the Euclidean minimum spanning tree. Given a compact <span style="white-space:nowrap">set $$C$$,</span> consider every partition $$C=A\cup (C\setminus A)$$ of $$C$$ into two disjoint nonempty compact subsets. For each such partition, find a line segment $$s_A$$ of minimum length with endpoints in $$A$$ <span style="white-space:nowrap">and $$C\setminus A$$,</span> breaking ties lexicographically by coordinates. By the assumed compactness of $$A$$ <span style="white-space:nowrap">and $$C\setminus A$$,</span> such a line segment exists. Let $$T_C$$ be the union of $$C$$ itself and of all line segments obtained in this way. For example, the union of a triangle, square, and circle shown below has three partitions into two nonempty compact subsets, separating one of these three shapes from the other two. Two of these partitions choose the diagonal pink segment as their shortest connection, and the third partition chooses the horizontal pink segment. So in this case, $$T_C$$ consists of the three blue given shapes and two pink segments.

{: style="text-align:center"}
![Minimum spanning tree of a circle, square, and triangle]({{site.baseurl}}/assets/2022/trisquircle.svg)

When $$C$$ is a finite point set, $$T_C$$ is just a Euclidean minimum spanning tree. When $$C$$ has finitely many connected components, like the example above, $$T_C$$ is again a minimum spanning tree, for the component-component distances. In the general case, $$T_C$$ still has many of the familiar properties of Euclidean minimum spanning trees:

* It consists of the input and a collection of line segments connecting pairs of input points, by construction.

* It is a [connected set](https://en.wikipedia.org/wiki/Connected_space). Topologically, this means that it cannot be covered by two disjoint open sets that both have a nonempty intersection with it. (This is different from being path-connected, a stronger property.) Any nontrivial open disjoint cover of $$C$$ would be spanned by a line segment from one set to the other, and no new disjoint covers can separate these line segments from their endpoints.

* For any added <span style="white-space:nowrap">segment $$s_A$$,</span> the intersection of two disks with that segment as radius (a "lune") has no point of $$C$$ in its interior. Any interior point would form one end of a shorter connecting segment between $$A$$ <span style="white-space:nowrap">and $$C\setminus A$$,</span> with the other end at an endpoint <span style="white-space:nowrap">of $$s_A$$.</span> No two added segments can cross without violating the empty lune property.

  {: style="text-align:center"}
![The empty lune of an edge]({{site.baseurl}}/assets/2022/vesica.svg)

* For any added <span style="white-space:nowrap">segment $$s_A$$,</span> the open rhombus with angles $$60^\circ$$ and $$120^\circ$$ having $$s_A$$ as its long diagonal is disjoint from the rhombi formed in the same way from the other segments. Any two overlapping rhombi would allow the longer of the two segments they come from to be replaced by a shorter segment crossing the same compact partition, on a three-segment path connecting its endpoints via the other segment endpoints. Because these non-overlapping rhombi cover a region of bounded area, the squared segment lengths have a bounded sum, and only finitely many segments can be longer than any given length threshold.

  {: style="text-align:center"}
![An infinite minimum spanning tree and its empty rhombi]({{site.baseurl}}/assets/2022/ivy-rhombs.svg)

* The union of $$C$$ with any subset of added segments is compact. If $$p$$ is a limit point of a <span style="white-space:nowrap">sequence $$\sigma_i$$</span> of points in this union, it must either lie in the empty rhombus of a segment (in which case it can only be a point of the same segment), or it is a limit point of a sequence of points <span style="white-space:nowrap">in $$C$$,</span> obtained by replacing each point in $$\sigma_i$$ that is interior to a segment by the nearest segment endpoint. This replacement only increases the distance from the replaced point to $$p$$ by a constant factor, which does not affect convergence. By compactness the replaced sequence converges to a point <span style="white-space:nowrap">in $$C$$.</span>

* For <span style="white-space:nowrap">any $$i$$,</span> the set $$T_i$$ of the largest $$i$$ added segments (with the same tie-breaking order) are edges of a minimum spanning tree for a family of $$i-1$$ sets. To construct these sets, find the components of the union of $$C$$ with all shorter segments, and intersect each component <span style="white-space:nowrap">with $$C$$.</span> None of these components can cross between $$A$$ and $$C\setminus A$$ for any <span style="white-space:nowrap">edge $$s_A\in T_i$$.</span> Because adding $$T_i$$ connects all these components, there can be at most $$i-1$$ components. Each edge in $$T_i$$ is shortest (with a consistent tie-breaking rule) across some partition of the components, one of the ways of determining the edges in a finite minimum spanning tree. In particular, $$T_C$$ is minimally connected: removing any edge $$s_A\in S_i$$ separates some of the components from each other.

* $$T_C$$ has the minimum sum of squared edge lengths of all collections of line segments between points of $$C$$ that <span style="white-space:nowrap">connect $$C$$.</span> To see this, consider any other connecting set $$X$$ of line segments with a finite sum of squared edge lengths. Truncate the sorted sequence of edges of $$T_C$$ to a finite initial <span style="white-space:nowrap">sequence $$T_i$$</span> such that the rest of the sequence has negligible sum of squares. Because $$T_i$$ is a minimum spanning tree of its components, and $$X$$ connects those same components (perhaps redundantly), the sequence of edge lengths in $$T_i$$ is, step for step, less than or equal to the sorted sequence of lengths <span style="white-space:nowrap">in $$X$$.</span>

There may exist other sets of line segments that connect $$C$$ with the same sum of squared edge lengths but they all are minimally connected, with the same sequence of edge lengths, the same empty lune and empty rhombus properties, and the same property that their initial sequences form finite minimum spanning trees of their components.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/108476695929961897))