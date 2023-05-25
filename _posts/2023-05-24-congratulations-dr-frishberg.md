---
layout: post
title: Congratulations, Dr. Frishberg!
date: 2023-05-24 21:06
---
My student Daniel Frishberg successfully passed his dissertation defense today!

I've written here already about several of our joint papers:
* "[New applications of nearest-neighbor chains: Euclidean TSP and motorcycle graphs]({{site.baseurl}}{% post_url 2019-02-21-mutual-nearest-neighbors %})" (with Mamano, Efrat, Goodrich, Kobourov, Matias, and Polishchuk, [ISAAC 2019](https://doi.org/10.4230/LIPIcs.ISAAC.2019.51))
* "[Simplifying activity-on-edge graphs]({{site.baseurl}}{% post_url 2019-01-29-simplifying-task-milestone %}) (with Havvaei, [SWAT 2020](https://doi.org/10.4230/LIPIcs.SWAT.2020.24))
* "[On the treewidth of Hanoi graphs]({{site.baseurl}}{% post_url 2020-05-03-hanoi-vs-sierpinski %})" (with Maxwell, [FUN 2020](https://doi.org/10.4230/LIPIcs.FUN.2021.13) and [_Theor. Comput. Sci._ 2022](https://doi.org/10.1016/j.tcs.2021.12.014))
* "[Angles of arc-polygons and Lombardi drawings of cacti]({{site.baseurl}}{% post_url 2021-07-10-angles-arc-triangles %})" (with Osegueda, [CCCG 2021](https://projects.cs.dal.ca/cccg2021/wordpress/wp-content/uploads/2021/08/CCCG2021.pdf) and [_Comp. Geom. Theory & Applications_ 2023](https://doi.org/10.1016/j.comgeo.2023.101982))
* "[Improved mixing for the convex polygon triangulation flip walk]({{site.baseurl}}{% post_url 2022-07-21-flipping-until-lost %})" (ICALP 2023, to appear)
* "[Rapid mixing of the hardcore Glauber dynamics and other Markov chains in bounded-treewidth graphs]({{site.baseurl}}{% post_url 2021-11-14-random-independent-sets %})" (not yet published)

Several more are on the way but not yet announced. As is typical for our students, the earlier ones involved more of my intervention, the last two were mostly Daniel's work, and I'm not even likely to be a coauthor on the upcoming ones: the pattern we want to see developing in a new doctorate. The dissertation incorporates the last two of the papers listed above. Most of our students combine three papers to form a dissertation, and the Hanoi graph work would have fit thematically, but just with the two Daniel included it already had plenty of material.

The ICALP reviewers told us that we've been underselling one of the results in that paper, on the expansion of the associahedron, so I thought I'd elaborate on that a little more here. An [associahedron](https://en.wikipedia.org/wiki/Associahedron) is a graph whose vertices represent triangulations of a convex polygon (or binary search trees on a given set of keys) and whose edges represent "flips" that remove and replace one diagonal in a triangulation (or that perform a single binary tree rotation). There's a lot we don't know about associahedra still, including how to calculate shortest paths ("flip distance") between vertices efficiently.

![Flip graph of a hexagon]({{site.baseurl}}/assets/2006/fg6.png)
{: style="text-align:center"}

The version of expansion we're using is [edge expansion](https://en.wikipedia.org/wiki/Expander_graph),

$$\min_{X\subset V(G)}\frac{\vert\partial X\vert}{\min(\vert X\vert,\vert V(G)\setminus X\vert)},$$

where $$\partial X$$ represents the set of edges having one endpoint in $$X$$. There are many other graphs of local moves in state spaces that, like the associahedron, can also be given the structure of the vertices and edges of a convex polytope, and in many such cases these have constant expansion. In fact, Milena Mihail and Umesh Vazirani conjectured some time prior to 1992 that every polytope whose vertex coordinates are all 0 or 1 has expansion at least one (for this history see e.g. Kaibel, "On the Expansion of
Graphs of 0/1-Polytopes", [arXiv:math/0112146](https://arxiv.org/abs/math/0112146)), and it was a big breakthrough in 2018 when [Nima Anari, Kuikui Liu, Shayan Oveis Gharan, and Cynthia Vinzant proved it for flip graphs of matroids](https://gilkalai.wordpress.com/2018/12/12/nima-anari-kuikui-liu-shayan-oveis-gharan-and-cynthia-vinzant-solved-the-mihail-vazirani-conjecture/) ([arXiv:1811.01816](https://arxiv.org/abs/1811.01816)). The associahedra are not 0-1 polytopes, but one can still ask what their expansion is. The ICALP paper gets within a logarithmic factor of the right answer: it proves that the expansion is $$\Omega\bigl(1/(\sqrt n\log n)\bigr)$$ and $$O(1/\sqrt n)$$. The lower bound is the part that fits into the machinery of Daniel's thesis, but it is the upper bound that the referees told us we were underselling. It is the first time we have seen that the expansion of the associahedron is smaller than a constant.

To prove this upper bound (in appendix C of [arXiv:2207.09972](https://arxiv.org/abs/2207.09972)), we merely have to find a partition of the space of all triangulations into two subsets with few edges connecting them. This partition is defined very simply, as follows:

* For each triangulation, look at the triangle containing the center point of the polygon.
* This triangle has three sides. Define their "length" combinatorially, as the number of polygon sides they cut off. Thus, the three lengths sum to $$n$$, and the shortest is at most $$n/3$$.
* Put a triangulation into one side of the partition when its central triangle has a very short side, of length less than $$n/6$$, and into the other side of the partition otherwise.

There are always three flips that move one of the vertices of the central triangle, unless the short side is only one edge long. But short motions of these vertices are likelier than long ones, enough so to keep the expansion small. The details involve doing some sums with Catalan numbers.

The next step for Daniel will be to start an assistant professor position at Cal Poly in San Luis Obispo in the fall.

Congratulations, Daniel!