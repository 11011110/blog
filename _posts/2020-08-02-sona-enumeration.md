---
layout: post
title: Sona enumeration
date: 2020-08-02 23:48
---
The last of my CCCG 2020 papers is now on the arXiv: "New Results in Sona Drawing: Hardness and TSP Separation", [arXiv:2007.15784](https://arxiv.org/abs/2007.15784), with Chiu, Demaine, Diomidov, Hearn, Hesterberg, Korman, Parada, and Rudoy. (As you might infer from the long list of coauthors, it's a Barbados workshop paper.) The paper studies a mathematical formalization of the [lusona](https://en.wikipedia.org/wiki/Lusona) drawings of southwest Africa; in this formalization, a sona curve for a given set of points is a curve that can be drawn in a single motion, intersecting itself only at simple crossings, and surrounding each given point in a separate region of the plane, with no empty regions. The paper proves that it's hard to find the shortest one, hard even to find whether one exists when restricted to grid edges, and gives tighter bounds for the widest possible ratio between sona curve length and TSP tour length; see the preprint or [the video I already posted]({{site.baseurl}}{% post_url 2020-07-22-three-cccg-videos %}) for more information.

To save this post from being content-free, here's a research question that we didn't even state in the paper, let alone make any progress on solving: just how many of these curves can a given set of points have? A sona curve can be described as a 4-regular plane multigraph (satisfying certain extra conditions) together with an assignment of the given points to its bounded faces, so there are finitely many of these things up to some sort of topological equivalence. And because this is topological it shouldn't matter where the points are placed in the plane: the number of curves should be a function only of the number of points. I tried hand-enumerating the curves for up to three points but it was already messy and I'm not certain I got them all. (In an earlier version of this post I definitely didn't get them all — I had to update the figure below after finding more.) Here are the ones I found:

{: style="text-align:center"}
![Sona curves for up to three points]({{site.baseurl}}/assets/2020/sona-enum.svg)

If this hand enumeration is correct, then the numbers of sona curves for $$n$$ labeled points form an integer sequence beginning $$1, 3, 24,\dots$$ and the numbers for unlabeled points form a sequence beginning $$1, 2, 5,\dots$$ but I don't really know anything more than that for this problem.

Another research direction I don't know much about yet: given a topological equivalence class of sona drawings, how can we find a good layout for it as an explicit drawing? There's lots of research on drawing plane graphs nicely but it's not clear how much of it carries over to making nice sona curves.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/104624173377453724))