---
layout: post
title: Halloween linkage
date: 2024-10-31 18:17
---
* [John Pai's art combines woven metal latticework texture with geometric forms](https://www.thisiscolossal.com/2024/09/john-pai-steel-sculptures/) <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mastodon.art/@colossal/113143894369926019)).</span>

* [Adding the dots from multiple top surfaces allows the design of dice with fewer total dots](https://mathenchant.wordpress.com/2024/10/17/industrious-dice/) <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@JimPropp/113324323559401192)).</span>

* [Pentagonal bipyramids lead to the smallest flexible embedded polyhedron](https://arxiv.org/abs/2410.13811) <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/113338585218318077)),</span> new preprint by 
Matteo Gallet, Georg Grasegger, Jan Legerský, and Josef Schicho. Convex polyhedra are rigid, but some special non-convex polyhedra have at least one continuous degree of freedom. (More than one degree of freedom can be obtained in a trivial way by gluing such polyhedra.) The [Bricard octahedra](https://en.wikipedia.org/wiki/Bricard_octahedron) have the same combinatorial structure as a regular octahedron, and can sort of flex, but only if you allow faces that can cross through each other. You can avoid the crossings, for instance by making little gussets near where they would happen, at the expense of making the shape more complicated.

  It was believed that Steffen's polyhedron, with 9 vertices, 21 edges, and 14 triangular faces, was the simplest possible non-self-intersecting flexible polyhedron. For instance, Demaine and O'Rourke's book _Geometric Folding Algorithms_ (p. 347) writes "As it was later proven that all triangulated polyhedra of eight vertices are rigid, Steffen’s example is minimal in this sense." But it was apparently not proven, and the new preprint claims a better example: an 8-vertex polyhedron formed from a pentagonal bipyramid by subdividing one triangle into three. This seems a bizarre choice because this subdivision does not affect flexibility. But it can act as a gusset pulling two parts of the boundary away from each other, changing a self-crossing bipyramid into a non-self-crossing subdivided bipyramid.

* [The fight to make public the scanned data of public-domain 3d artworks in French museums](https://cosmowenman.substack.com/p/secret-3d-scans-in-the-french-supreme) <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/113344045798055289),</span> [via](https://lobste.rs/s/ziwp61/secret_3d_scans_french_supreme_court)), including Rodin's sculptures.

* University library programs that pay a flat licensing fee for commercially published textbooks, in order to keep costs down for students, are [disincentivizing and hijacking the funds from programs to produce open-access course materials](https://www.chronicle.com/article/two-campaigns-to-reduce-textbook-costs-are-often-at-odds-can-they-co-exist) <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/113347844448642194),</span> [archived](https://archive.is/uQgER)). These fees do not typically offer students any savings when some of their materials are open-access, and do not typically allow students continued access to the materials once their courses are over.

* My RSS reader crashed hard recently; I was behind by two major versions and had to upgrade <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/113354010205270499)).</span> The new version found a few subscriptions from 2017 from an even older version, and I thought I had lost all more recent subs for good, but eventually I found a recent copy of the subscription list buried in a container down eight levels of file hierarchy below my home directory, thanks to [a ten-year-old blog post](https://rubenerd.com/where-netnewswire-4-0-stores-app-data/).

  So anyway, let that be an excuse for some RSS evangelism. RSS is not dead! Find an RSS reader and use it collect all the blogs and magazines and newspapers and other online sources that you want to keep up with. You can't read everything, but if you're going to be enclosed in a bubble, let it be one where you are your own gatekeeper. A couple of explainers, with recommendations for RSS readers: [_The Verge_](https://www.theverge.com/24036427/rss-feed-reader-best), [_Wired_](https://www.wired.com/story/best-rss-feed-readers/) ([archived](https://archive.is/hxKF9)).

* [SODA 2025 accepted papers](https://www.siam.org/conferences-events/siam-conferences/soda25/program/accepted-papers/) <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@sioum/113345823129376708)).</span>

* [Predators on predatory journals](https://blog.cabells.com/2024/01/16/unmasking-a-predator-predatoryreports-org/amp/) <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/113366818576575751)).</span> Cabells is as far as I know a legitimate commercial journal analytics company that sells access to a database of predatory journals, which they call "Predatory Reports". This posting by Cabells reports on an unrelated site calling themselves (at that time) "predatoryreports.org", maintaining their own separate list and seeking large fees from journal publishers in exchange for removal from the list. I found out about this through [a Wikipedia discussion](https://en.wikipedia.org/wiki/Talk:MDPI) where another editor stated that the publication of this post by Cabells, some nine months ago, had led to a shakeup, of sorts: the predator-of-predators changed the word "reports" in their name to "journals". Sure enough, now predatoryreports.org redirects to Cabells as it should, but the splash screen for predatoryjournals.org looks pretty much the same as the screenshot from the Cabells post.

* [Shapes of polyhedra and triangulations of the sphere](https://arxiv.org/abs/math/9801088) <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@johncarlosbaez/113369111554515465)),</span> a 1998 paper by William Thurston, provides the following general procedure for making convex polyhedra (or equivalently by [Alexandrov's uniqueness theorem](https://en.wikipedia.org/wiki/Alexandrov%27s_uniqueness_theorem) topological spheres with cone singularities) that can be tiled with equilateral triangles, meeting 5 or 6 at a vertex. Draw a (possibly non-convex) 11-gon in a triangular lattice such that equilateral triangles pointing inward from its vertices do not intersect except at the 11-gon vertices. Then the part of the 11-gon between the triangles is a [net](https://en.wikipedia.org/wiki/Net_(polyhedron)) for a tiled polyhedron (its [star unfolding](https://en.wikipedia.org/wiki/Star_unfolding)), and every tiled polyhedron can be generated in this way.

  {: style="text-align:center"}
![A non-convex 11-gon with vertices in a triangular grid, with disjoint inward-pointing equilateral triangles (green), generates a net (yellow) for a convex polyhedron tiled by equilateral triangles]({{site.baseurl}}/assets/2024/11-gon-net.svg){: style="width:100%;max-width:720px" }

* [AI tool used widely to transcribe medical conversations "is prone to making up chunks of text or even entire sentences" including "racial commentary, violent rhetoric and even imagined medical treatments"](https://apnews.com/article/ai-artificial-intelligence-health-business-90020cdf5fa16c79ca2e5b6c4c9bbb14) <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@gregeganSF/113376179143790756)).</span> Because of course it does. The study this news story is based on appears to be "[Careless Whisper: Speech-to-Text Hallucination Harms](https://arxiv.org/abs/2402.08021)" by Allison Koenecke, Anna Seo Gyeong Choi, Katelyn X. Mei, Hilke Schellmann, and Mona Sloane.

* [Bob Hearn's magnetic snap-together 3d-printed stellations of the icosahedra](https://www.youtube.com/watch?v=pxsT-uavzug) and [Scott Vorthmann's app inspired by these models](https://www.vzome.com/app/59icosahedra/) <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@robinhouston/113368481741273225)).</span>

* [Dan Piponi rants about Mario Livy feeding quasi-religious misunderstandings of the Fibonacci numbers and the golden ratio](https://mathstodon.xyz/@dpiponi/113364102159249491) by jumping back and forth between examples of other topics such as logarithmic spirals and text about the golden ratio, causing people to think the examples involve the golden ratio when they don't. Piponi concludes that "it's deliberate deception in order to sell books".

* [A lower bound for the quickhull convex hull algorithm that disproves the quickhull precision conjecture](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4989035) <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/113400094218315111)),</span> a new SSRN preprint by Mike Goodrich. Mike tells me that he didn't actually intend to post this as a preprint but must have clicked the wrong button trying to submit it to an Elsevier journal. But I think that making it public in this way, even accidentally, is relatively harmless, this time. Oh, the result? It's about [quickhull](https://en.wikipedia.org/wiki/Quickhull), an algorithm for 2d convex hulls. It is known that
  - Quickhull on worst-case inputs with unbounded coordinates takes $$O(n^2)$$ time, and no better bound is possible.
  - Quickhull on random points in a convex region takes $$O(n)$$ expected time.
  - Quickhull on points with integer coordinates of polynomial size takes $$O(n\log n)$$ time.
  - Quickhull on inputs whose hull has $$h$$ edges takes $$O(nh)$$ time.

  There was a conjecture from 1996 that the last two of these bounds could be combined: that quickhull on points with  integer coordinates of polynomial size and $$h$$ hull edges takes $$O(n\log h)$$ time. The conjecture is wrong.  Quickhull is a divide-and-conquer algorithm that recursively partitions its input in a certain way. The optimality of $$O(n^2)$$ can be shown using $$n$$ points with exponential coordinates, causing these splits to be highly uneven.  The new counterexample is the same construction with $$h$$ points, for $$h$$ small enough to produce polynomially-large coordinates, plus $$n-h$$ points that get carried along for the ride through $$h$$ levels of recursion. This shows that the combination of known time bounds $$O\bigl(\min(nh,n\log n)\bigr)$$ is optimal for this case.

* [Pillow box design](https://arxiv.org/abs/2410.17593) <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/113404741149929214)),</span> new arXiv preprint by Jun Mitani. You've probably seen and used pillow boxes, even if you don't know the name. They are those ubiquitous small cardboard packages, sort of like a flattened tube with a convex lens-shaped cross-section, with inwardly-curving end caps. They can be folded from a single rectangular sheet of cardboard, with less wasted material than folding a cuboid box, and the curved folds make them quite rigid even when they are made from thin material. In this preprint, Mitani studies the mathematics behind their design, also connecting them to the [teabag problem](https://en.wikipedia.org/wiki/Paper_bag_problem) asking how much volume can be enclosed between two squares glued edge-to-edge.