---
layout: post
title: Finding obstacle-avoiding point sets can be hard
date: 2018-08-07 22:05
---
My new preprint for today is my first follow-up paper to my book, [_Discrete Configurations in Discrete Geometry_](https://www.cambridge.org/eppstein), and the first published solution to one of its open problems. It's with [Daniel Lokshtanov](https://cs.ucsb.edu/people/faculty/lokshtanov) (in the process of moving from the University of Bergen to the University of California, Santa Barbara) and I hope to have another paper eventually with him on some more research we did related to the book, but for now there's only the one. It's called "The parameterized complexity of finding point sets with hereditary properties" ([arXiv:1808.02162](https://arxiv.org/abs/1808.02162)) and I'll be presenting it later this month at [IPEC in Helsinki](http://algo2018.hiit.fi/ipec/) while Daniel gets ready to move house.

The book is about finite sets of Euclidean points and their properties.
Many of the properties I'm interested in are defined by a constant number of _obstacles_, smaller point sets whose presence (in any combinatorially equivalent form) stops the property from being true. For instance a point set is in _general position_ if it avoids having three points in a line, and it is in _convex position_ if it also avoids having a triangle of three points surrounding a fourth point (this is [Carathéodory's theorem](Carathéodory's theorem (convex hull))). If you have a point set that's not in convex position, and you want to find a convex-position subset that's as large as possible, there's a known polynomial-time algorithm (Section 11.4 of my book). But what about other properties? How easily can you find the largest subset with a given property?

To study this from the point of view of parameterized complexity we should augment the problem with a numerical parameter that encapsulates all its difficulty. The problem is _fixed-parameter tractable_ when its running time is a polynomial in the input size (independent of the parameter) multiplied by a function of the parameter. For finding large obstacle-avoiding subsets, one natural choice for the parameter is how many points you have to remove. Can you eliminate all the copies of the obstacles by removing only $$r$$ points? This is always fixed-parameter tractable as a special case of more general hitting set problems. But the other choice is to make the parameter be the size of the subset you're seeking. Does a given input have a subset of $$k$$ points that avoids all the obstacles?

When I wrote the book, all the examples I knew for problems of finding $$k$$-point obstacle-avoiding subsets were either polynomial (like the $$k$$-point convex subset problem) or at least fixed-parameter tractable (as the problem of finding $$k$$ points in general position turns out to be). So I posed as an open problem the question of whether these problems are always fixed-parameter tractable. The answer turns out to be no. The new paper provides an example of a set of obstacles for which this problem is hard under standard complexity-theoretic assumptions.

Here are the three hard-to-avoid obstacles:

{: style="text-align:center"}
![Three obstacles for a hard property]({{site.baseurl}}/assets/2018/forbidden.svg)

And here's a rough picture of what a hard instance looks like:

{: style="text-align:center"}
![Hard instance for a hard property]({{site.baseurl}}/assets/2018/yard.png)

(The actual instances will have more than three horizontal lines, and only some of its triples of blue and yellow points will be collinear.)

We set the parameter $$k$$ to a value that forces every $$k$$-point obstacle-avoiding subset to include all red and blue points, plus one yellow point per horizontal line. It could not include more than three points per horizontal line, because the left obstacle prevents that, and it could not include all red points and two yellow points on the same line, because the middle obstacle prevents that.

The effect of the right obstacle is more subtle. In any subset that avoids it, the yellow points have to line up in the same way as the blue points. That is, whenever three lines have the property that their three blue points on each side line up (as they do in this example), the three yellow points in the middle must also line up. We use this property to show that instances of (partitioned) [subgraph isomorphism](https://en.wikipedia.org/wiki/Subgraph_isomorphism_problem), looking for one graph as part of another larger graph, can be translated into point sets like this. The three-point lines in the blue points will be arranged to represent triples of an edge and its two endpoints in the graph we are trying to find, and the three-point lines in the yellow points will correspond in the same way to triples of an edge and its two endpoints in the larger graph we are searching. The details of the reduction are a bit messy, though, because we have to use points with small integer coordinates and prove that the obstacles don't show up accidentally in some other way.

Those aren't the only results of the paper; it also shows that some natural classes of obstacles lead to tractable problems. For instance, this is true whenever none of the obstacles is collinear, whenever one of the obstacles is in convex position, or whenever there is only one obstacle. But we failed to completely classify which sets of obstacles lead to tractable problems and which don't (unlike the analogous questions for induced subgraphs of graphs, where a complete classification is known). So even though we knocked out one of the open problems from the book, there's definitely more research left to do in the same direction.