---
layout: post
title: Dehn rank revisited
date: 2022-06-22 18:22
---
In [a recent post]({{site.baseurl}}{% post_url 2022-04-03-dissection-into-rectangles %}), I discussed dissection of orthogonal polygons into each other by axis-parallel cuts, translation, and gluing. Each polygon has a value associated with it, called its [Dehn invariant](https://en.wikipedia.org/wiki/Dehn_invariant), that cannot be changed by dissection, so two polygons that can be dissected into each other must have equal invariants. And for past usage of Dehn invariants, that was pretty much all we looked at: are they equal or not? But my post pointed out that these invariants actually have a lot of structure (you can think of them as matrices, after an arbitrary choice of basis) and this structure is geometrically meaningful. Matrices (or tensors) have a rank, and the rank of the Dehn invariant is a lower bound on  the number of rectangles into which a polygon can be dissected. This in turn has implications on the ability of a polygon or its dissections to tile the plane.

Now it's a paper: "Orthogonal dissection into few rectangles", [arXiv:2206.10675](https://arxiv.org/abs/2206.10675), to appear at CCCG. The results of the paper are stronger: instead of just using the Dehn rank as a lower bound, I proved that it always equals the minimum number of rectangles into which a given polygon can be dissected, and can be used to compute this number of rectangles efficiently. The two main steps of the proof are:

* constructing a set of the right number of rectangles for any given tensor, by a direct geometric construction that turns an algebraic realization of the rank (a combination of positive and negative rectangles) into a geometric representation without the negativity, and

  {: style="text-align:center"}
![Construction of a set of rectangles realizing a given tensor as their Dehn invariant]({{site.baseurl}}/assets/2022/dehn-realizability.svg){: style="width:100%;max-width:540px" }

* finding a dissection for any two polygons with equal invariants, by induction on the dimensions of the matrix describing their invariants.

  {: style="text-align:center"}
![Induction step for proving the existence of a dissection between polygons with equal Dehn invariants]({{site.baseurl}}/assets/2022/dehn-dissectability.svg){: style="width:100%;max-width:540px" }

The images above are taken from the illustrations for the proofs of these two results from the paper, and maybe will provide a little insight into how they might be proven. For details, see the paper. Instead, here, I wanted to highlight a different, related problem, that I wasn't able to prove as much about.

Mostly when mathematicians talk about Dehn invariants, it's for 3d dissections: cutting polyhedra up along planes, translating and rotating the pieces, and gluing them back together. The 3d Dehn invariant combines lengths and angles of polyhedron edges in the same way that the 2d invariant combines widths and heights of rectangles. Therefore, 3d Dehn rank is a lower bound on the number of edges you can dissect something into. It's easy to construct polyhedra with arbitrarily large rank, and these polyhedra are forced to have arbitrarily large numbers of edges, no matter how you try to cut them up and reassemble them.

However, the 3d Dehn rank is not exactly equal to the minimum number of edges after dissection. A cube has Dehn invariant zero (with rank zero), but the minimum number of edges of a polyhedron you can dissect it into is four, for a [space-filling tetrahedron](https://www.jstor.org/stable/2689983) of the same volume. A regular tetrahedron is not space-filling, has a Dehn invariant of rank one, and already has the minimum number of edges among anything you can dissect it into. In both cases the rank is unequal to the minimum number of edges. Also, the rank is different in these cases but the minimum number of edges is the same.

Nevertheless, I was hoping that the rank of the Dehn invariant would be usable as a constant-factor approximation to the minimum number of edges after dissection. To prove this, I'd need to find a polyhedron, having the same Dehn invariant as any given polyhedron, but with a number of edges proportional to the rank. The existence of a dissection would then follow from known results. But finding this few-edge polyhedron would have to use some knowledge of the starting polyhedron (unlike my set-of-rectangles construction), because not all tensors are realizable as Dehn invariants. So far, I haven't been able to find any construction of these few-edge polyhedra.

So: does every polyhedron, of Dehn rank $$r$$, have an equivalent polyhedron with $$O(r)$$ edges? Or are there some polyhedra that cannot be dissected into another polyhedron with few edges, even though their Dehn invariants have low rank?

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/108524203085266737))