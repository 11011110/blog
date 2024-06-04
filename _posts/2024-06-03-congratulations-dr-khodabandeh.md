---
layout: post
title: Congratulations, Dr. Khodabandeh!
date: 2024-06-03 22:01
---
'Tis the season for dissertation defenses and candidacy exams, and my doctoral student Hadi Khodabandeh successfully defended his dissertation today.

Hadi came to UCI from Sharif University in Iran. By now he has many strong publications, mostly on spanners, the topic of his dissertation. Much of this has been self-directed, with my contributions often limited to vague direction setting or (in one case where I am not a coauthor) not even as much as that. Spanners are sparse graphs, defined using points in a metric space as their vertices, and having graph distances that approximate the distance in the space. The spanner ones (so far), with links to some previous posts here with more detail, are:

* "On the edge crossings of the greedy spanner", ([SoCG 2021](https://doi.org/10.4230/LIPIcs.SoCG.2021.33)), shows that [a greedy construction produces spanners with few crossings and small separators]({{site.baseurl}}{% post_url 2020-02-17-spanners-have-sparse %}).

* "Online spanners in metric spaces" ([ESA 2022](https://doi.org/10.4230/LIPIcs.ESA.2022.18)), constructs spanners online, as points are added one by one to the input. The total weight of the spanner is nevertheless small, although there remains a gap between this weight and lower bounds from the same paper on how small it can be.

* "Distributed construction of lightweight spanners for unit ball graphs" ([DISC 2022](https://doi.org/10.4230/LIPIcs.DISC.2022.21), and announced at SPAA 2022), concerns [spanners in generalizations of Euclidean spaces to doubling metrics]({{site.baseurl}}{% post_url 2021-07-09-spanners-unit-ball %}), spaces where every ball can be covered by a bounded number of half-radius balls. The resulting spanners have bounded vertex degree, small total weight, and can be constructed efficiently by a distributed algorithm, even when restricted to use only short edges (and to approximate the best distance possible for restricted paths of this type).

* "Maintaining light spanners via minimal updates" (CCCG 2024, to appear; until then, see [arXiv:2403.03290](https://arxiv.org/abs/2403.03290)) is on spanners in both Euclidean and doubling spaces, for points subject to insertion and deletion. You would like to handle these operations quickly. We don't do that. But instead, we show that [these operations can be handled without much change to the spanner]({{site.baseurl}}{% post_url 2024-03-06-spanners-that-dont %}), again for a spanner that maintains high quality in other respects.

His other papers include works on healthcare monitoring, route monitoring in road networks, and networked applications of invertible Bloom filters. His next step is to go to Google in Sunnyvale, for work unlikely to concern spanners.

Congratulations, Hadi!