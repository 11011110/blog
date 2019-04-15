---
layout: post
title: Monochromatic grids in colored grids
date: 2019-04-14 17:02
---
Color the points of an $$n\times n$$ grid with two colors. How big a monochromatic grid-like subset can you find? By "grid-like" I mean that it should be possible to place equally many horizontal and vertical lines, partitioning the plane into $$k\times k$$ cells each of which contains a single point.

So for the coloring of the $$8\times 8$$ grid below, there are several $$4\times 4$$ monochromatic grid-like subsets. The image below shows one, and the completely red and blue southwest and northeast quadrants provide two others.
The blue quadrant prevents any red grid-like subset from being larger than $$4\times 4$$, and vice versa, so these are the largest grid-like subsets in this grid. 

{: style="text-align:center"}
![Monochromatic grid-like subset in a colored grid]({{site.baseurl}}/assets/2019/subgrid.svg)

It's not hard to prove that there always exists a monochromatic grid-like subset of size at least $$\lfloor \sqrt{n} \rfloor\times \lfloor \sqrt{n} \rfloor$$.
Just use vertical and horizontal lines to partition the big grid into blocks of that size. If one of those blocks is monochromatic, then it's the grid-like subset you're looking for. And if not, you can choose a red point from each block to get a grid-like subset of the same size.

In the other direction, there exist colorings of an $$n\times n$$ grid for which the largest monochromatic grid-like subset has size only a little bigger, $$O(\sqrt{n\log n})\times O(\sqrt{n\log n})$$. To find such a coloring, partition the big grid into square blocks of size $$O(\sqrt{n/\log n})\times O(\sqrt{n/\log n})$$, and make each block monochromatic with a randomly chosen color.

{: style="text-align:center"}
![Coloring a grid by dividing into square blocks and coloring each block randomly]({{site.baseurl}}/assets/2019/blocked-coloring.svg)

Now, consider any partition by axis-parallel lines into (irregular) rectangles, each containing one of the points of a grid-like subset.  Only one row or column of the rectangles can cross each line of the partition into square blocks, so the number of rectangles that include parts of two or more square blocks is $$O(\sqrt{n\log n})\times O(\sqrt{n\log n})$$. Any remaining rectangles of the partition must come from a grid-like subset of square blocks that are all colored the same as each other. But with a random coloring, the expected size of this largest monochromatic subset of square blocks is $$O(\log n)\times O(\log n)$$. Therefore, the number of rectangles that stay within a single square block is limited to the total number of points in this grid-like subset of square blocks, which is again $$O(\sqrt{n\log n})\times O(\sqrt{n\log n})$$.

I'm not sure how to eliminate the remaining $$O(\sqrt{\log n})$$ gap between these two bounds, or which way it should go.

One application of these ideas involves the theory of [superpatterns](https://en.wikipedia.org/wiki/Superpattern), permutations that contain as a [pattern](https://en.wikipedia.org/wiki/Permutation_pattern) every smaller permutation up to some size $$n$$.
If $$\pi$$ is a superpattern for the permutations of size $$n$$, then we can obtain a point set by interpreting the position and value of each element of $$\pi$$ as Cartesian coordinates. This point set includes a grid-like subset of size $$\lfloor \sqrt{n} \rfloor\times \lfloor \sqrt{n} \rfloor$$, coming from a permutation of size $$n$$ that translates to a grid-like set of points.
If the elements of the superpattern are colored with two colors, there still exists a monochromatic grid-like subset of size $$O(n^{1/4})\times O(n^{1/4})$$.
And this monochromatic grid-like subset corresponds to a superpattern, for permutations of size $$O(n^{1/4})$$. So, whenever the elements of a superpattern are colored with two (or finitely many) colors, there remains a monochromatic subset of elements that is still a superpattern for permutations of some smaller but non-constant size.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/101927319466372642))