---
layout: post
title: General-position hypercube projections
date: 2018-12-08 16:40
---
I recently posted about finding solutions to the [no-three-in-line problem](https://en.wikipedia.org/wiki/No-three-in-line_problem) of finding large general-position subsets of grids, by [using the probabilistic method]({{site.baseurl}}{% post_url 2018-11-10-random-no-three %}) or by [throwing an integer linear program solver at the problem]({{site.baseurl}}{% post_url 2018-11-12-gurobi-vs-no %}). Another potential method for finding solutions involves finding large general-position subsets in higher dimensions, where it's easier (there's more room to move the points out of the way of each other), and then projecting back down while being careful not to introduce any new collinearities.

A particularly nice family of general-position subsets is given by the hypercubes. The vertices of a $$d$$-dimensional hypercube can be described as the points in $$d$$-dimensional space all of whose coordinates are zeros and ones. There's no way for three such points to lie on a line, because the middle of the three points would have to have fractional coordinates somewhere between the zero-one coordinates of the outer two points. So for the purposes of the no-three-in-line problem these points are in general position.

A projection of a hypercube onto the integer grid can be described (up to translations) by choosing $$d$$ two-dimensional vectors and letting the projected points be all sums of subsets of these vectors. There are $$2^d$$ subsets (including the empty subset and the subset of all vectors), and their sums give $$2^d$$ points in the plane. It's always possible to choose a $$d$$-tuple of vectors that causes these $$2^d$$ points to remain in general position, but the question is how small we can make these vectors in order to make the projection stay within a small grid.

For $$d\in\{2,3,4\}$$ the answer is that we can fit the points into a grid of size $$2^{d-1}\times 2^{d-1}$$. This is optimal because any smaller grid would cause more than two points to lie on the same horizontal or vertical grid line.

{: style="text-align:center"}
![hypercubes of dimension 2, 3, and 4, projected in general position into optimally-small grid squares]({{site.baseurl}}/assets/2018/gen-pos-cubes.svg)

The simplicity of the $$4$$-dimensional projection ($$16$$ points in an $$8\times 8$$ grid with no three in line) makes me wonder whether this solution was the one Dudeney was trying to avoid in his [1917 statement of the problem](https://archive.org/stream/amusementsinmath00dude#page/94/mode/2up), when he added the extra condition that the solutions (described in terms of pawns on a chessboard) must include pawns at e4 and d5.

Unfortunately the $$5$$-dimensional hypercube doesn't have a general-position projection onto a $$16\times 16$$ grid. The best [my search software]({{site.baseurl}}/assets/2018/projcube.py) could find were several different $$18\times 19$$ solutions. Here's one of them:

{: style="text-align:center"}
![hypercube of dimension 5, projected in general position into an 18x19 grid]({{site.baseurl}}/assets/2018/5cube-18x19.svg)

Beyond these specific examples, it would be interesting to obtain asymptotic bounds on how big a grid is needed for all hypercubes.

([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/101208363611245952), [G+](https://plus.google.com/100003628603413742554/posts/iADVC9CsL1b))
