---
layout: post
title: Footprints in the snow
date: 2019-08-17 14:42
---
Given an abstract optimization problem with multiple solutions, how much partial information about a solution do you have to know in order to uniquely identify that solution? That has been the topic of some of my earlier research, on [how many creases of an origami folding pattern you have to force to be mountain or valley folds in order to cause the remaining folds to go the way you want]({{site.baseurl}}{% post_url 2014-10-08-forced-creases-in %}). And it's the topic of my new preprint "Tracking paths in planar graphs" ([arXiv:1908.05445](https://arxiv.org/abs/1908.05445), with Mike Goodrich, James Liu, and Pedro Matias).

There's an old story about how to design the footpaths on a college campus: wait for it to snow, see where the heaviest sets of footprints cross the snow from building to building, and then once the snow melts place paths in those same places. But what if you live somewhere like Irvine where it never snows? Or what if you want to perform some other type of data analysis on a data set of the paths that people take? For instance, in order to design improvements to the road networks used by commuter traffic, it would be helpful to figure out where all the traffic actually goes each day. How can you collect that data?

Our paper takes the point of view that you can attach sensors to the network that record the times and identities of people passing by them, but that these sensors are expensive. The goal is (for a given network with designated start and destination vertices $$s$$ and $$t$$) to place as few of these sensors as possible at graph vertices, in such a way that every simple $$st$$-path is uniquely identified by the sequence of sensors that it passes through.

The problem turns out to be $$\mathsf{NP}$$-complete, even on planar networks. But there's a simple approximation ratio based on the idea that the optimal number of sensors is always going to be proportional to the number of faces in the network. Each face (in the sequence of biconnected components between $$s$$ and $$t$$) has to have at least one sensor, to distinguish paths that go one way around the face from paths that go the other way around. It turns out that placing one sensor at a vertex shared by many faces doesn't work — those faces still need a proportional number of additional sensors. And our approximation algorithm ensures that the number of sensors is at most proportional to the number of faces.

We also use [Courcelle's theorem](https://en.wikipedia.org/wiki/Courcelle%27s_theorem) to prove that the exact solution is fixed-parameter tractable in the clique-width of the graph. Like most or all uses of Courcelle's theorem, the resulting algorithm is impractical, so it would be of interest to find a more direct algorithm, perhaps for a weaker parameter.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/102634545213040458))