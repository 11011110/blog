---
layout: post
title:  How good is greed for the no-three-in-line problem?
date:   2021-04-28 18:23
---
The [37th European Workshop on Computational Geometry (EuroCG 2021)](http://eurocg21.spbu.ru/) was earlier this month, but its [book of abstracts](http://eurocg21.spbu.ru/wp-content/uploads/2021/04/proceedings.pdf) remains online. This has an odd position in the world of academic publishing: the "abstracts" are really short papers, so it looks a lot like a published conference proceedings. However, it declares that you should really pretend that it's not a proceedings, in order to allow the same work to go on to another conference with a published proceedings, getting around the usual prohibitions on double publication. Instead, its papers "should be considered a preprint rather than a formally reviewed paper". But I think that doesn't preclude citing them, with care, just as you might occasionally cite arXiv preprints. The workshop's lack of peer review and selectivity is actually a useful feature, allowing it to act as an outlet for works that are too small or preliminary for publication elsewhere. In North America, the [Canadian Conference on Computational Geometry](http://cccg.ca/) performs much the same role, but does publish a proceedings; its [submission deadline](https://projects.cs.dal.ca/cccg2021/the-call-for-papers-is-out/) is rapidly approaching.

Anyway, one of the EuroCG not-really-a-published-paper things is mine: "Geometric dominating sets – A minimum version of the no-three-in-line problem", with Oswin Aichholzer and Eva-Maria Hainzl. As the title suggests, it's related to the [no-three-in-line problem](https://en.wikipedia.org/wiki/No-three-in-line_problem), in which one must place as many points as possible in a grid so that no three are collinear. I've written about the same problem here [several]({{site.baseurl}}{% post_url 2018-11-10-random-no-three %}) [times]({{site.baseurl}}{% post_url 2018-11-12-gurobi-vs-no %}) [already]({{site.baseurl}}{% post_url 2018-12-08-general-position-hypercube %}). On an $$n\times n$$ grid, there's an easy upper bound of $$2n$$ on the number of points, but it's widely conjectured that the actual number is a smaller linear function of $$n$$. It was a big step forward when Erdős showed that $$n\bigl(1-o(1)\bigr)$$ points can be placed, and this was later improved to $$\tfrac{3}{2}n\bigl(1-o(1)\bigr)$$.

These big no-three-in-line sets are constructed algebraically, but what if we try something simpler, a greedy algorithm that just adds points one by one (in a random or systematic order) until getting stuck? This question was already asked in the 1970s by Martin Gardner, and studied by several other authors since. But it is, if anything, even more frustratingly unknown than the no-three-in-line problem itself. We don't know whether, in general, it's possible to get stuck with fewer points than the maximum solution to the no-three-in-line problem, or even whether it's possible to get stuck with fewer than $$2n$$ points for infinitely many values of $$n$$. For some values of $$n$$ we do know smaller stuck solutions, though: for instance, here's one with $$28$$ points on a $$36\times 36$$ grid.

{: style="text-align:center"}
![A 28-point greedy solution to the no-three-in-line problem on a 36x36 grid]({{site.baseurl}}/assets/2021/greedy-no3-36x36.svg)

It was known that greedy solutions always have $$\Omega(\sqrt{n})$$ points, and one of our main results is to improve this bound to $$\Omega(n^{2/3})$$. The known $$\Omega(\sqrt{n})$$ lower bound is easy to see: A single line through two selected points can cover at most $$n$$ other grid points, so you need $$n$$ lines to cover the whole grid, and you need $$\Omega(\sqrt{n})$$ points to determine this many lines. With fewer points, there won't be enough lines through your points to cover the whole grid, and your greedy solution won't be stuck. Our new $$\Omega(n^{2/3})$$ bound looks more carefully at the tradeoff between numbers of lines and numbers of points per line. It can be divided into two cases:

* Suppose, first, that the selected point set has the property that, for any selected point $$p$$, the lines through $$p$$ cover fewer than $$n^{4/3}$$ grid points. Because each selected point covers few grid points, we need to select many points to cover the whole grid: at least $$\Omega(n^{2/3})$$ points.

* Suppose on the other hand that the lines through some point $$p$$ cover at least  $$n^{4/3}$$ grid points. Parameterize these lines by the $$L_\infty$$ distance to the closest grid point (regardless of whether that point is one of the selected ones). Then there are $$O(k)$$ lines with parameter $$k$$, each of which covers $$O(n/k)$$ grid points. Summing over small values of $$k$$ shows that, even if we use lines that cover as many grid points as possible, we need  $$\Omega(n^{2/3})$$ lines through $$p$$ to cover this many grid points. Each of these lines is determined by another selected point, so we need $$\Omega(n^{2/3})$$ selected points.

The actual proof in the paper takes into account that not all the grid points near $$p$$ are the nearest on their line, and does the summation over small values of $$k$$ more carefully, to get more precise constant factors in the bounds. Our paper also includes another variation of the problem in which we allow our selected points to be collinear but require the lines through them to cover all unselected points. There, we can make a little progress: we show that $$n$$ points, or in some cases slightly fewer than $$n$$ points, are sufficient. The same $$\Omega(n^{2/3})$$ lower bound is still valid for this case, but there's still a big gap between the lower bound and the upper bound.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/106146843522019241))