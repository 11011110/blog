---
layout: post
title: Snowflake spanners
date: 2020-02-19 23:01
---
[My previous post]({{site.baseurl}}{% post_url 2020-02-17-spanners-have-sparse %}) gave an example of a largish random point set where the [greedy geometric spanner](https://en.wikipedia.org/wiki/Greedy_geometric_spanner) for distance ratio 2 had no crossings, while the spanner for the lower distance ratio had many (linearly many) crossings. And you might think from that example that there is some threshold for which distance ratios above the threshold always have planar greedy spanners, or even that the threshold is at or below 2. But it's not true.

To see why not, we have to turn to an idea from an earlier paper of mine, "[Beta-skeletons have unbounded dilation](https://arxiv.org/abs/cs.CG/9907031)" (_CGTA_ 2002). In it, I used a flattened variant of the [Koch snowflake fractal](https://en.wikipedia.org/wiki/Koch_snowflake) to find bad examples for a different kind of spanner, and the same thing works here too. The intuitive idea is that these fractals form curves that, locally, look nice to a spanner algorithm (just connect consecutive pairs of points along the curve). But they pack a lot of length into a small area, forcing the spanner algorithm to eventually add some shortcuts to the curve. If we can control where it adds the shortcuts, maybe we can make pairs of shortcuts cross.

In fact the Koch snowflake itself almost works, but it has some closest pairs that are non-consecutive along the curve, allowing the greedy spanner algorithm to choose those pairs instead of the consecutive curve points that we want it to choose. If we flatten the snowflake just a little bit, that complication goes away. If we choose the distance ratio of the spanner large enough, we can make it so that the greedy spanner algorithm doesn't add any shortcuts until it reaches pairs of points that are opposite each other on the curve. And if we make it just barely large enough for that to be true, it will be forced to add those shortcuts once it does reach that distance in the sorted ordering of the distances. For instance, here's a point set and its non-planar greedy spanner generated in this way with spanning ratio 4:

{: style="text-align:center"}
![Greedy spanner of snowflake-like curve with distance ratio 4]({{site.baseurl}}/assets/2020/snowflake.svg)

This pretty picture, with the three crossing shortcuts between opposite pairs of points, doesn't quite generalize to arbitrary-order snowflake-like curves, unfortunately. It will always be possible to find a distance ratio $$d$$ such that the greedy algorithm adds one of these three shortcuts, as the first shortcut it needs to add. But then once it has added it, that shortcut can make the other two opposite pairs of points closer to each other in the spanner than they were, so that the greedy algorithm doesn't need to add them. We might only get one of these three crossing edges, instead of all three. (In fact, for the point set shown here, this is exactly what happens for spanning ratio 4.5.)

Instead, let's look for a slightly lower distance ratio $$d'$$, for which the first shortcuts added by the greedy spanner algorithm cut off two lobes of the snowflake instead of three. For the same points as above, $$d'=3.65$$ works:

{: style="text-align:center"}
![Greedy spanner of snowflake-like curve with distance ratio 3.5]({{site.baseurl}}/assets/2020/snowflake2.svg)

These two-lobe shortcuts are shorter than the three-lobe shortcuts, so they're considered earlier by the greedy algorithm. There are two crossing equilateral triangles of two-lobe shortcuts (forming a Star of David pattern) and the greedy algorithm has to include two edges from each equilateral triangle. This is because, for each of these potential shortcuts, the greedy spanner won't include a better path between its endpoints until it has either that shortcut itself or the two other shortcuts of the same triangle. No matter which two shortcuts we choose from each of the two equilateral triangles, we get either two crossings or, as here, three crossings.

For any order of flattened Koch snowflake, there's a distance ratio $$d'$$ producing a greedy spanner that looks like this picture, with two or three crossings. And by choosing a snowflake of high-enough order, we can make $$d'$$ become arbitrarily large. Or, to put it another way, the greedy spanner algorithm can generate crossings for arbitrarily large distance ratios.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/103689972863017904))