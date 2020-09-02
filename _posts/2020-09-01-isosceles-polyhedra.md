---
layout: post
title: Isosceles polyhedra
date: 2020-09-01 23:18
---
My latest arXiv preprint is "On polyhedral realization with isosceles triangles", [arXiv:2009.00116](http://arxiv.org/abs/2009.00116). As the title suggests, it studies polyhedra whose faces are all isosceles triangles. Despite several new results in it, there's a lot I still don't know. The paper finds a sort-of-new[^1] infinite family of polyhedra with congruent isosceles faces, shown below, but I don't know if there are any more such families.

{: style="text-align:center"}
![Twisted augmented bipyramid with isosceles-triangle faces]({{site.baseurl}}/assets/2020/twisted.svg)

One of the other previously known families, shown below, has two integer parameters (the numbers of sides on the two half-bipyramids it combines), but I don't know whether the same double parameterization is possible for the new family.

{: style="text-align:center"}
![Combination of two half-bipyramids with isosceles-triangle faces]({{site.baseurl}}/assets/2020/biarc.svg){: width="80%" }

In 2001, Branko Grünbaum published an example of a polyhedron that could not be realized with congruent faces, even non-convexly,[^2] but it can be realized as a convex polyhedron with all faces isosceles (or equilateral), as shown below. I don't know whether there are polyhedra that cannot be realized with all faces isosceles, if one allows the realization to be non-convex (but non-self-crossing and combinatorially equivalent to a convex polyhedron) and the faces to be non-congruent.

{: style="text-align:center"}
![Grünbaum's example of a polyhedron that cannot be realized with congruent faces, realized convexly with isosceles and equilateral triangle faces]({{site.baseurl}}/assets/2020/grunbaum.svg)

My new preprint proves that there exist polyhedra (iterated Kleetopes) that cannot be realized as convex polyhedra with isosceles faces. But the construction is a little non-explicit and I don't know how complicated these polyhedra need to be. For instance, I don't know whether there is a convex isosceles-face realization of the double Kleetope of the octahedron, shown below.

{: style="text-align:center"}
![Double Kleetope of an octahedron]({{site.baseurl}}/assets/2020/kkoct.svg)

Grünbaum's example can be realized convexly with only two edge lengths, and my non-isosceles-faced polyhedra require at least three edge lengths in any convex realization. I don't know whether the number of required edge lengths can be unbounded, or whether non-convex realizations ever require three lengths (although certain stacked polyhedra require at least two).

* Footnotes go here
{:footnotes}

[^1]: The family of polyhedra from the first image is only "sort-of-new" because the same combinatorial structure was previously described as a triangulation of the sphere by congruent spherical isosceles triangles: Dawson, Robert J. MacG. (2005), "[Some new tilings of the sphere with congruent triangles](https://archive.bridgesmathart.org/2005/bridges2005-489.html)", Renaissance Banff. In exchange for re-purposing Dawson's triangulation, my paper describes another infinite family of spherical triangulations by congruent spherical isosceles triangles, not given by Dawson, based on applying a similar $$2\pi/3$$ twist to an infinite family of non-convex bipyramids with congruent isosceles faces like the one below. Again, I don't know whether there are other such families of spherical triangulations.

      {: style="text-align:center"}
![Non-convex polyhedron with congruent isosceles-triangle faces]({{site.baseurl}}/assets/2020/nwb.svg)

[^2]: Grünbaum, Branko (2001), "[A convex polyhedron which is not equifacettable](https://sites.math.washington.edu/~grunbaum/Nonequifacettablesphere.pdf)", _Geombinatorics_ 10: 165–171. I don't know how to access old papers on this journal in general, but fortunately Grünbaum made his one available on his web site.