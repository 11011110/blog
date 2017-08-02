---
layout: post
title: Pascal's triangle of point sets
date: 2017-07-01 16:34
---
Form a family of sets of $$\tbinom{n}{i}$$ points, as follows.

* When $$i=0$$ or $$i=n,$$ then $$\tbinom{n}{i}=1$$ and there is only one point.

* For any other choice of $$i,$$ place the points for $$\tbinom{n-1}{i-1}$$ below and to the left of the points for $$\tbinom{n-1}{i},$$ to form a single chain of points that is monotone in both their $$x$$ and $$y$$ coordinates. When placing these two subsets of points, use more space between them horizontally than vertically, so that all lines through pairs of points on the left side pass above the right side and all lines through pairs of points on the right side pass below the left side.

Like this:

{: style="text-align:center"}
![32-vertex Pascal's triangle of point sets]({{site.baseurl}}/assets/2017/pascal.svg)

This construction can be used to generate point sets with no large convex subsets. To see this, it's easier to start with two restricted types of convex subset, called "cups" and "caps". A cup is a subset of points that lies on the graph of a convex function, and a cap lies on the graph of a concave function. These are both convex subsets, but not all convex subsets are cups or caps. For instance, in the image above, the sets in the positions of the binomial coefficients $$\tbinom{n}{1}$$ are cups and the sets in the positions of $$\tbinom{n}{n-1}$$ are caps.

Then it turns out that the point set in position $$\tbinom{n}{i}$$ contains neither an $$(i+2)$$-cap nor an $$(n-i+2)$$-cup. For $$i=0$$ or $$i=n,$$ this is easy to see directly: it doesn't have enough points. For the other positions, the left side has no $$(i+1)$$-cap (by induction) so an $$(i+2)$$-cap would have to include at least two points of the right side, only possible if the cap is entirely on the right side. But the right side has no $$(i+2)$$-cap (by induction again), so the whole point set also has no such cap. The argument for cups is symmetric.

There's also no convex subset of $$n+1$$ points within any of these sets.
For, to make such a set, you would have to combine a cap on the left with a cup on the right, and the number of points you can get that way is too small.

But we can combine these sets to get even larger sets with no large convex polygons. Take each row of this triangle, and glue its point sets together in left-to-right order, again making the horizontal spacing wide enough that in each gluing step the lines through pairs on the left pass above the right and the lines through pairs on the right pass below the left:

{: style="text-align:center"}
![Gluing together one row of the triangle]({{site.baseurl}}/assets/2017/eszek.svg)

What convex subsets do these point sets have? We already know that within each of the subconfigurations of $$\tbinom{n}{i}$$ points there are no convex $$(n+1)$$-gons, so any larger convex polygon would have to combine points from two or more of these subconfigurations. But the best you can do is to take a cap from any one subconfiguration, a cup from another subconfiguration to its right, and single points from the subconfigurations between them. In all cases, this produces at most $$n+1$$ points.

Therefore, we have found point sets with

$$\sum_{i=0}^n \binom{n}{i}=2^n$$

points, having no convex $$(n+2)$$-gons. According to the conjectured solution to the [happy ending problem](https://en.wikipedia.org/wiki/Happy_ending_problem), every larger point set does have a convex $$(n+2)$$-gon, so (if the conjecture is true) this is the optimal construction for avoiding convex polygons using as many points as possible.

Some bibliographic notes: The number of points in these configurations was already suggested as a conjecture in the original 1935 paper on the happy ending problem by Erdős and Szekeres, hinting that they might have already known of a construction like this one, but they didn't actually publish such a construction until 1961. Unfortunately, the copy of their 1961 paper on the Erdős publication archive is missing the pages describing the construction, so I'm not sure how they did it. I finally found a description in [a 2000 survey by W. Morris and V. Soltan](https://doi.org/10.1090/S0273-0979-00-00877-6). Morris and Soltan cite a 1995 paper by Kalbfleisch and Stanton that corrects "some inaccuracies in the proof" of Erdős and Szekeres; they follow the presentation of the Erdős–Szekeres construction from a 1979 book of Lovász. The construction here is based on the one from Morris and Soltan, but with a couple of minor changes, namely the arrangement of the point sets into a triangle and the use of the same gluing technique for both phases of the construction.

([Comment thread on Google+](https://plus.google.com/100003628603413742554/posts/3fccYp7AV22))