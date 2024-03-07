---
layout: post
title: Spanners that don't change much
date: 2024-03-06 23:11
---
I have another preprint on the arXiv today with my student Hadi Khodabandeh: "Maintaining light spanners via minimal updates", [arXiv:2403.03290](https://arxiv.org/abs/2403.03290).

Like my other work with Hadi, this is on geometric spanners: sparse graphs on a given set of points in a metric space, whose shortest path distances accurately approximate the metric distances between the points. There are a lot of detailed properties spanners could be expected to have, and a lot of existing constructions that achieve some (but not all) of those properties:

- The accuracy with which they approximate distances can be adjusted, to be within a factor $$1+\varepsilon$$ of the true distance for any $$\varepsilon>0$$.

- They can be _light_, having total weight within a constant factor (depending on $$\varepsilon$$) of the minimum spanning tree weight, the minimum possible weight for any connected graph whose edge lengths come from the geometry.

- Their number of edges can be linear in the number of points (again with a constant of proportionality depending on $$\varepsilon$$) or more strongly each vertex in the graph can have bounded or small degree.

- They may be constructible in general families of spaces, such as the [spaces of bounded doubling dimension](https://en.wikipedia.org/wiki/Doubling_space), instead of being limited to Euclidean spaces.

- It may be possible to update the spanner dynamically, as points are added or removed from the space, in a small amount of time (say logarithmic) for each point change.

For instance, the [greedy geometric spanner](https://en.wikipedia.org/wiki/Greedy_geometric_spanner) has adjustable accuracy, constant lightness, and bounded degree, in spaces of bounded doubling dimension, but it is not dynamic. A different spanner construction of Gao, Guibas, and Nguyen [[_JoCG_ 2006](https://doi.org/10.1016/j.comgeo.2005.10.001)] is dynamic, with lightness and degree that are small but unbounded, and only in Euclidean spaces. And after several earlier related results, Gottlieb and Roditty  [[_ESA_ 2008](https://doi.org/10.1007/978-3-540-87744-8_40)] found a fast dynamic spanner construction with adjustable accuracy and bounded degree in spaces of bounded doubling dimension, but still with unbounded lightness.

Our contribution is to relax the requirement of fast updates. Instead of measuring the complexity of an update by how much computation time it takes, we measure how much change it makes to the spanner. The spanners from the new preprint are accurate, light, have bounded degree, and work in doubling spaces; the amount of change per update is small (amortized constant per insertion and logarithmic per deletion) but the time per update can still be large.

The question of whether one can achieve all the things (dynamic, accurate, light, bounded degree, in doubling spaces) remains open. But from the fact that not much change to the spanner is needed per update, finding that change quickly seems more in reach.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/112053189195340711))