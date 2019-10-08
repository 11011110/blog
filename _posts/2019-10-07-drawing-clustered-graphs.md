---
layout: post
title: Drawing clustered graphs of bounded width
date: 2019-10-07 22:33
---
In [a paper from last year]({{site.baseurl}}{% post_url 2018-03-16-drawing-clustered-graphs %}) on [clustered planarity](https://en.wikipedia.org/wiki/Clustered_planarity), with Giordano Da Lozzo, Mike Goodrich, and Sid Gupta, we provided subexponential-time algorithms for arbitrary instances, and fixed-parameter tractable algorithms for instances whose embedded width and number of clusters are both bounded.

Now, in my newest preprint, "C-planarity testing of embedded clustered graphs with bounded dual carving-width" (with the same authors, [arXiv:1910.02057](https://arxiv.org/abs/1910.02057)), we've eliminated the dependence on the number of clusters (using a different width parameter) and found a fixed-parameter tractable algorithm with just a single parameter.

It was just in time: while our paper was in submission, last July, Rado Fulek and Csaba Tóth put up their own preprint, "Atomic embeddability, clustered planarity, and thickenability" ([arXiv:1907.13086](https://arxiv.org/abs/1907.13086)) announcing a solution to the clustered planarity problem in polynomial time without dependence on parameters. I [posted about it briefly at the time](https://mathstodon.xyz/@11011110/102537368093048271), and can't find much else more recent about it, but I assume it's in submission to somewhere good. So our results may be only of historic value...

Our paper was presented at IPEC 2019 (part of the [ALGO 2019 conference in Munich](http://algo2019.ak.in.tum.de/)) last month, and won IPEC best paper award. The late timing of the preprint is because (somewhat unusually for a CS conference) IPEC makes their proceedings versions due after the conference rather than before, so they can take into account feedback from the conference.
The arXiv version is more complete than the proceedings version will be, because of page limits in the proceedings, but we prepared it at the same time.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/102925193159020982))