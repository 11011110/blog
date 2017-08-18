---
layout: post
title: Two new Graph Drawing preprints
date: 2017-08-17 22:42
---
I have two new preprints on arXiv, from my two papers [accepted to Graph Drawing](https://gd2017.ccis.northeastern.edu/accepted-papers/).

* "Triangle-free penny graphs: degeneracy, choosability, and edge count" ([arXiv:1708.05152](https://arxiv.org/abs/1708.05152)) is a conference-paper version of [an earlier post here]({{site.baseurl}}{% post_url 2017-02-19-triangle-free-penny %}), which showed that the triangle-free penny graphs are 2-degenerate. The main article is short but also expands on a comment I made on that post, a bound on the largest possible number of edges in these graphs that is close to the known lower bound. In an appendix, I also included material from two later posts here: [some analogous results for squaregraphs]({{site.baseurl}}{% post_url 2017-06-13-how-many-edges %}), and a counterexample showing that [the same results do not extend to arbitrary 2-degenerate triangle-free planar graphs]({{site.baseurl}}{% post_url 2017-06-18-the-malyshev-graphs %}).

* "The effect of planarization on width" ([arXiv:1708.05155](https://arxiv.org/abs/1708.05155)) is an extended version of [my answer to a cstheory question by Bart Jansen](https://cstheory.stackexchange.com/q/35974/95). Bart asked whether it is possible to draw $$K_{3,n}$$ and then replace every crossing by a vertex, in such a way that the resulting planar graph has low pathwidth. The answer is no: every planarization of a drawing of $$K_{3,n}$$ has pathwidth $$\Omega(n)$$. The proof idea from that answer turns out to generalize to treewidth as well as pathwidth, and I also looked at the same question for many other graph width parameters.  Some of these parameters behave like treewidth and pathwidth, blowing up when you planarize even as simple a graph as $$K_{3,n}$$, while others stay bounded when you planarize a bounded-width graph. Here's one of the figures from the planarization paper, a carving decomposition of $$K_{3,3}$$ and its planarization:

{: style="text-align:center"}
![Carving decomposition of K_{3,3} and its planarization]({{site.baseurl}}/assets/2017/carving-decomposition.svg)

Graph Drawing has a policy of maintaining a shadow proceedings on arXiv.org, with the same content as the official proceedings, so I think we should be seeing quite a few more of these from other authors as the early-September proceedings deadline approaches.

([G+](https://plus.google.com/100003628603413742554/posts/BKV2aEL3dxm))