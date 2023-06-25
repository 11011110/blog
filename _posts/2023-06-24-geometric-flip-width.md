---
layout: post
title: Geometric flip-width revisited
date: 2023-06-24 18:07
---
I recently posted here about the [flip-width of geometric graphs]({{site.baseurl}}{% post_url 2023-02-20-geometric-graphs-unbounded %}), and to readers of that post, my new preprint "Geometric Graphs with Unbounded Flip-Width" ([arXiv:2306.12611](http://arxiv.org/abs/2306.12611), with Rose McCarty, to appear in CCCG 2023) will look very familiar. It even has the same title! However, the process of turning it into a paper led to some improvements. Let me summarize them briefly here.

First, a reminder of the main concept, flip-width. This is defined using a pursuit–evasion game in which a robber tries to escape cops by following paths in a graph. At each turn, the cops have made a fixed number of "flips" to the graph. Each flip applies to a subset of vertices (possibly overlapping with other flips), removes edges from its adjacent vertices, and adds edges connecting its non-adjacent vertices. A turn consists of three steps: the cops announce what they will flip next, the robber moves along a path of length at most $$s$$, and then the cops undo their current flips and perform the new flips that they announced. The goal of the cops is to leave the robber stuck on an isolated vertex, while the goal of the robber is to escape forever. If a class of graphs has a function $$f(s)$$ such that $$f(s)$$ cops can win against a robber of speed $$s$$, then it has bounded flip-width. If there is a speed $$s$$ for which arbitrarily many cops may be needed to catch a speed-$$s$$ robber, then the class has unbounded flip-width.

Beyond a more careful attention to detail and rigor, new developments are:

* Three-dimensional Delaunay triangulations have unbounded flip-width. This uses a construction from another recent blog post on [isohedral Delaunay complexes]({{site.baseurl}}{% post_url 2023-02-25-isohedral-delaunay-complexes %}).

* [Beta-skeletons](https://en.wikipedia.org/wiki/Beta_skeleton) have unbounded flip-width. There are actually two different kinds of beta-skeleton but the interesting case is for parameter values $$\beta<1$$, for which the two definitions agree.

* Another type of geometric graph for which we can prove unbounded flip-width, not mentioned in the previous post, is the rectangle of influence graphs. These connect pairs of points in their plane when their axis-aligned bounding box is empty of other points. We find a recursive construction for rectangle of influence graphs containing hypercube induced subgraphs of arbitrarily large dimension, which in turn have unbounded flip-width. As with the beta-skeletons, definitions for rectangle of influence graphs disagree (about what to do with points on the boundary of the bounding box) but our hypercube construction doesn't need that ambiguity.

  {: style="text-align:center"}
![Hypercube in a rectangle of influence graph]({{site.baseurl}}/assets/2023/empty-rectangle.svg)

* For most of the families of geometric graphs that we study, the robber can escape by stepping across only one edge per turn ($$s=1$$). This is a big improvement over the $$s=4$$ from the blog post, and a much more natural speed limitation. The exception is for three-dimensional Delaunay triangulations; for these $$s=2$$ works but we don't know about $$s=1$$. An $$s=2$$ escape strategy for all of these graphs is very simple: move to a "lane" (one of two special types of vertex in the "interchange" graphs constructed in the previous blog post) that has two-edge paths to many other lanes. The $$s=1$$ strategy is different, and for some of the geometric graphs is based on hypercube subgraphs rather than interchanges.

* An appendix extends the results on all of these graph classes (even 3d Delaunay triangulations) from unbounded flip-width to monadic independence, meaning that it is possible to use _transductions_, a certain kind of translation system defined using logical formulas, to get arbitrary graphs from graphs in these classes. The main ideas (from Szymon Toruńczyk) are to use Ramsey theory to simplify the interchange subgraphs into two cases, "sparse" and "dense", to use the structure of these graphs to find a logical translation from the dense case to the sparse case, and to find a subdivision of any given graph as an induced subgraph of a sparse interchange.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/110602049050780927))