---
layout: post
title: Spanners for unit ball graphs in doubling spaces
date: 2021-07-09 09:06
---
My student Hadi Khodabandeh had a paper with me on spanners earlier this year at SoCG, in which we showed that [the greedy spanner algorithm for points in the Euclidean plane produces graphs with few crossings and small separators]({{site.baseurl}}{% post_url 2020-02-17-spanners-have-sparse %}). Now we have another spanner preprint: ["Optimal spanners for unit ball graphs in doubling metrics", arXiv:2106.15234](https://arxiv.org/abs/2106.15234).

[Doubling metrics](https://en.wikipedia.org/wiki/Doubling_space) are a generalization of Euclidean spaces. Like Euclidean spaces, they have a dimension, the _doubling dimension_, but it might not be an integer. Even the doubling dimension of the Euclidean plane itself is $$\log_2 7\approx 2.807355$$; this means that every circular disk of radius $$r$$ in the plane can be covered by seven closed disks of radius $$r/2$$.

{: style="text-align:center"}
![Seven disks of radius $$r/2$$ cover a single disk of radius $$r$$]({{site.baseurl}}/assets/2021/doubling-dim.svg)

Analogously, the _doubling constant_ of a metric space (if it exists) is the smallest number $$c$$ such that every closed metric ball (the set of points within some radius $$r$$ of a fixed point) can be covered by $$c$$ balls of half the radius. The _doubling dimension_ is the binary logarithm of the doubling constant. A metric space is a _doubling metric_ or _doubling space_ if it has a doubling constant and doubling dimension. This is true for all Euclidean spaces: for instance, if you cover a ball with a grid of hypercubes, sized small enough that their long diagonal has length at most the radius of the ball, you obtain doubling constant at most $$\lceil 2\sqrt{d}\rceil^d$$, although it seems difficult to compute the precise doubling constant in general.

{: style="text-align:center"}
![Nine disks of radius $$r/2$$ cover a square grid that covers a single disk of radius $$r$$]({{site.baseurl}}/assets/2021/grid-doubling.svg)

The hyperbolic plane provides a natural example of a space that is not a doubling space: arbitrarily large-radius disks require arbitrarily many half-radius disks to cover them.

Many results in computational geometry can be generalized to doubling metrics, but not always, and sometimes with difficulty. That includes results on spanners, as we consider in our paper. A spanner of a weighted graph is a subgraph whose shortest path distances approximate the distances in the full graph, and often for spanners of metric spaces one uses the complete graph, weighted by the metric distance between each pair of points. But here, we are using a different graph, the unit ball graph. The unit ball graph, for points in a continuous space, has an edge whenever two unit balls centered at two of the points have a nonempty intersection, and it can be extended to discrete point sets by instead including an edge whenever two points are at distance at most 2 (or, as in our paper, distance at most 1; scaling doesn't really change anything). The weights are the same as in the complete graph. If a spanner accurately approximates all edge weights, it approximates all paths.

The unit ball graph has fewer edges to approximate than the complete graph. But that actually makes it harder to approximate, because by the same token there are fewer edges that can be used in the spanner. Despite that, the greedy spanner algorithm still produces a spanner, but one of its key properties is lost when going from Euclidean to doubling spaces: Euclidean greedy spanners have bounded degree, but greedy spanners in doubling spaces do not. Instead, our paper provides different spanner algorithms that apply to unit ball graphs, approximate paths in these graphs arbitrarily well, have bounded degree, have total weight a constant times that of the minimum spanning tree, and can be constructed efficiently in a distributed model of computing. I think the details are too technical to go into here, so see the paper for more.