---
layout: post
title: Counting paths in convex polygons
date: 2022-09-21 17:32
---
Let's count non-crossing paths through the all points of a convex polygon.
There is a very simple formula for this, $$n2^{n-3}$$ undirected paths through an $$n$$-gon, but why? Here's a simple coloring-based argument that immediately gives this formula.

Choose a coloring for the points of the polygon, red and blue, and choose a starting point for the path. Build a path, starting from this point, by the following rule: if you are at a red point, go to the next available point clockwise, and if you are at a blue point, go to the next available point counterclockwise.

{: style="text-align:center"}
![Generating a non-crossing path through all points of a convex polygon, by using a 2-coloring of the points to determing the direction of each step]({{site.baseurl}}/assets/2022/colored-ham.svg)

There are $$n2^n$$ choices of starting point and coloring, but each path is counted eight times, because the colors of the last two points on the path don't make a difference to  where it goes, and because each path is also traced in the opposite direction using the other end as its starting point. Dividing $$n2^n$$ by eight gives the formula.

This same idea also works to count non-crossing paths that are allowed to skip some of the points of the polygon. Now, color each point red, blue, or yellow. Use the same rule for building a path, but ignore the yellow points: start on a red or blue point, and when searching for an available point only go to another red or blue point.

{: style="text-align:center"}
![Generating a non-crossing path through some points of a convex polygon, by using a 3-coloring of the points to determing the direction of each step]({{site.baseurl}}/assets/2022/colored-path.svg)

There are $$3^n$$ choices of coloring. They have different numbers of choices of starting point, but by cyclically permuting the colors you can group them into $$3^{n-1}$$ triples of colorings that together have exactly $$2n$$ available (non-yellow) starting points. Each path is counted eight times just like before, so this argument would seem to give the formula $$2n\cdot 3^{n-1} / 8$$ for the number of paths. But it's not quite right. For one thing, it's not even an integer.

The problem is, what happens when you color all but one of the points yellow, and that one remaining point red or blue? You get a sequence of one point only: does that count as a path? If we count these as length-zero paths (as I would prefer), then they are undercounted, because they do not have two ends, and they only have one point whose coloring (red or blue) is irrelevant, rather than the usual two points. When we divide by eight we make their contribution too small. If we don't count them (as [OEIS tells me](http://oeis.org/A261064) was the definition used in a 2020 Bulgarian mathematics contest) then they are overcounted, because they contribute to the formula and shouldn't.

Adjusting for these one-point paths gives two alternative formulas:

$$\frac{n}{4}(3^{n-1}+3)$$

if we are counting one-point zero-length paths, or

$$\frac{n}{4}(3^{n-1}-1),$$

the formula from OEIS, if we are not counting them.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/109039364670401641))