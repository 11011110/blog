---
layout: post
title: Big convex polyhedra in grids
date: 2019-02-09 15:07
---
I recently wrote here about [big convex polygons in grids]({{site.baseurl}}{% post_url 2018-09-05-big-convex-polygons %}), a problem for which we know very precise answers. This naturally raises the question: what about higher dimensions? How many vertices can be part of a convex polyhedron in an $$n\times n\times n$$ grid, or more generally a convex polytope in a $$d$$-dimensional grid of side length $$n$$? Here we do still know some pretty good answers, at least up to constant factors in spaces of constant dimension.

The problem is included in a 2008 survey by Imre Bárány,[^bar] according to whom the maximum number of vertices is

$$\Theta\left(n^{d-2+\frac{2}{d+1}}\right).$$

For instance, in three dimensional $$n\times n\times n$$ grids the maximum number of vertices is $$\Theta(n^{3/2})$$.

One way to find polyhedra with this many vertices is to take the convex hull of the points in a ball,[^bl] [^bd] or in scaled copies of any fixed smooth convex body. Another way, which should generate polyhedra with a somewhat less irregular appearance and (up to constant factors) the same number of vertices, is to take the [Minkowski sum](https://en.wikipedia.org/wiki/Minkowski_addition) of all line segments (up to scaling and translation) that will fit into a smaller grid, of side length $$O(n^{1/(d+1)})$$. For instance, the [truncated rhombicuboctahedron](https://en.wikipedia.org/wiki/Truncated_rhombicuboctahedron) below[^ruen] is the Minkowski sum of all the line segments that fit into a unit cube. Its 96 vertices lie in a $$10\times 10\times 10$$ grid. In general, this method produces a [zonohedron](https://en.wikipedia.org/wiki/Zonohedron) whose complexity can be analyzed in terms of a $$(d-1)$$-dimensional arrangement of $$O(n^{d/(d+1)})$$ hyperplanes. As long as this arrangement is not too degenerate (which it appears not to be, but I haven't worked out the details carefully) this should give
a number of vertices within a constant factor of the number coming from the convex hull construction.

{: style="text-align:center"}
![Truncated rhombicuboctahedron]({{site.baseurl}}/assets/2019/truncated-rhombicuboctahedron2.png)

A matching upper bound comes from a 1963 paper by G. K. Andrews,[^and] and Bárány writes that although several more proofs have been published none of them is easy. I'm not sure whether the difficulty is in getting the exact bound or in the fact that Andrews and the later proofs allow more general shapes with volume $$n^d$$ that don't fit into a grid, but it's not hard to get close to the right bound simply by counting the number of possible facets of a given volume $$v$$. By using [lattice basis reduction](https://en.wikipedia.org/wiki/Lenstra%E2%80%93Lenstra%E2%80%93Lov%C3%A1sz_lattice_basis_reduction_algorithm) the integer vectors in the hyperplane through any facet have a nearly-orthogonal basis whose product of lengths is proportional to $$v$$. By considering how this product of lengths can be broken down into factors of different scales, and counting how many integer vectors of those lengths exist, it follows that the number of possible facets of volume $$v$$ is $$O(v^d\log^{d-1} v)$$. Combining this with the $$O(n^{d-1})$$ surface area of a grid polytope gives the correct upper bound on the number of vertices up to a polylog factor.

What about when the dimension is not constant? An easy construction for high dimensions is to take all points with a fixed distance $$r$$ from the grid center. There are $$O(dr^2)$$ possible values for the distance, so this construction produces a convex polytope with $$\Omega(n^{d-2}/d)$$ vertices. It comes from a 1946 paper by Behrend, who uses this idea to find [dense sets of integers with no arithmetic progressions](https://en.wikipedia.org/wiki/Salem%E2%80%93Spencer_set).[^beh]
It is never worse to use the convex hull of the ball than the points on a sphere,
and a celebrated paper by Elkin from 2011 (in the appendix of the published version) gives another proof of the $$\Omega(n^{d-2+2/(d+1)})$$ bound for convex hulls of balls (for $$d\ge 5$$) in which the constant factor of the $$\Omega$$ is universal, not depending on $$d$$. So when $$n$$ is singly exponential in $$d$$, $$n^{2/(d+1)}$$ becomes constant and the convex hull technique produces $$\Omega(n^{d-2})$$ vertices, improving Behrend's construction for progression-free sets by the same $$d$$ factor.[^elk]

* Footnotes go here
{:footnotes}

[^and]: Andrews, George E. (1963), "A lower bound for the volume of strictly convex bodies with many boundary lattice points", _Trans. Amer. Math. Soc._ 106, pp. 270–279, [doi:10.2307/1993769](https://doi.org/10.2307/1993769), [MR0143105](https://mathscinet.ams.org/mathscinet-getitem?mr=0143105).

[^bar]: Bárány, Imre (2008), "Extremal problems for convex lattice polytopes: a survey", _Surveys on Discrete and Computational Geometry_, Contemporary Mathematics 453, Amer. Math. Soc., pp. 87–103, [doi:10.1090/conm/453/08796](https://doi.org/10.1090/conm/453/08796), [MR2405678](https://mathscinet.ams.org/mathscinet-getitem?mr=2405678).

[^bd]: Balog, Antal and Deshouillers, Jean-Marc (1999), "On some convex lattice polytopes". _Number Theory in Progress_, Vol. 2 (Zakopane-Kościelisko, 1997), de Gruyter, pp. 591–606, [MR1689533](https://mathscinet.ams.org/mathscinet-getitem?mr=1689533).

[^beh]: Behrend, F. A. (1946), "On sets of integers which contain no three terms in arithmetical progression", _Proc. Nat. Acad. Sci._ 32 (12), pp. 331–332, [doi:10.1073/pnas.32.12.331](https://doi.org/10.1073/pnas.32.12.331), [MR0018694](https://mathscinet.ams.org/mathscinet-getitem?mr=0018694).

[^bl]: Bárány, Imre and Larman, David (1998), "The convex hull of the integer points in a large ball", _Math. Ann._ 312 (1), pp. 167–181, [doi:10.1007/s002080050217](https://doi.org/10.1007/s002080050217), [MR1645957](https://mathscinet.ams.org/mathscinet-getitem?mr=1645957).

[^elk]: Elkin, Michael (2011), "An improved construction of progression-free sets", _Israel J. Math._ 184, pp. 93–128, [arXiv:0801.4310](https://arxiv.org/abs/0801.4310), [doi:10.1007/s11856-011-0061-1](https://doi.org/10.1007%2Fs11856-011-0061-1), [MR2823971](https://www.ams.org/mathscinet-getitem?mr=2823971). The paragraph describing Elkin's results was updated from an earlier more tentative version in the original post.

[^ruen]: Ruen, Tom (2014), "Truncated rhombicuboctahedron", CC-BY-SA 4.0, [File:Truncated rhombicuboctahedron2.png](https://commons.wikimedia.org/wiki/File:Truncated_rhombicuboctahedron2.png) on Wikimedia commons.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/101564963348879092))
