---
layout: post
title: Report from LATIN
date: 2022-11-13 13:04
---
I just returned from the 15th [Latin American Symposium on Theoretical Informatics (LATIN 2022)](https://pakal.cs.cinvestav.mx/latin2022/), held this year in Guanajuato, Mexico. LATIN is a regional conference that is only offered every two years, like WADS in Canada and SWAT in Scandinavia. I had a paper in the first one, in 1992, but this is only the second one I've attended, after [2016 in Ensenada]({{site.baseurl}}{% post_url 2016-04-16-photos-from-latin %}). This time, I was one of four invited speakers, speaking about reversible computing. [My talk slides are online](https://www.ics.uci.edu/~eppstein/pubs/Epp-LATIN-22.pdf), and I think that a talk video should be uploaded by the conference in a week or so.

In Guanajuato, the conference was held at [CIMAT, the Centro de Investigación en Matemáticas](https://en.wikipedia.org/wiki/Centro_de_Investigaci%C3%B3n_en_Matem%C3%A1ticas). This is a large center with a permanent research staff and frequent visitors, similar for instance to the Mathematical Sciences Research Institute in Berkeley, California. Wikipedia tells me that it also offers advanced mathematics courses and postdoctoral degrees. It's set high on a hill over the town and has a crazy architecture, seemingly designed with a combination of the idea of what a space for mathematicians should look like, and the organic architecture of Guanajuato itself: staircases leading in every directions leading to narrow angular alleys or in some cases to nowhere, lots of repeated geometric shapes and patterns, and saturated with a coral red-orange color. I was inspired to use some of the conference break times to explore the center and take some photographs:

<div><table style="margin-left:auto;margin-right:auto">
<tr style="text-align:center;vertical-align:middle">
<td style="padding:10px"><a href="https://www.ics.uci.edu/~eppstein/pix/cimat/1.html"><img
src="https://www.ics.uci.edu/~eppstein/pix/cimat/1-s.jpg" style="border-style:solid;border-color:black;" width=288 height=162
alt="CIMAT"></a></td>
<td style="padding:10px"><a href="https://www.ics.uci.edu/~eppstein/pix/cimat/2.html"><img
src="https://www.ics.uci.edu/~eppstein/pix/cimat/2-s.jpg" style="border-style:solid;border-color:black;" width=193 height=256
alt="CIMAT"></a></td>
<td style="padding:10px"><a href="https://www.ics.uci.edu/~eppstein/pix/cimat/3.html"><img
src="https://www.ics.uci.edu/~eppstein/pix/cimat/3-s.jpg" style="border-style:solid;border-color:black;" width=193 height=256
alt="CIMAT"></a></td>
</tr>
<tr style="text-align:center;vertical-align:middle">
<td style="padding:10px"><a href="https://www.ics.uci.edu/~eppstein/pix/cimat/4.html"><img
src="https://www.ics.uci.edu/~eppstein/pix/cimat/4-s.jpg" style="border-style:solid;border-color:black;" width=250 height=199
alt="CIMAT"></a></td>
<td style="padding:10px"><a href="https://www.ics.uci.edu/~eppstein/pix/cimat/5.html"><img
src="https://www.ics.uci.edu/~eppstein/pix/cimat/5-s.jpg" style="border-style:solid;border-color:black;" width=193 height=256
alt="CIMAT"></a></td>
<td style="padding:10px"><a href="https://www.ics.uci.edu/~eppstein/pix/cimat/6.html"><img
src="https://www.ics.uci.edu/~eppstein/pix/cimat/6-s.jpg" style="border-style:solid;border-color:black;" width=193 height=256
alt="CIMAT"></a></td>
</tr>
<tr style="text-align:center;vertical-align:middle">
<td style="padding:10px"><a href="https://www.ics.uci.edu/~eppstein/pix/cimat/7.html"><img
src="https://www.ics.uci.edu/~eppstein/pix/cimat/7-s.jpg" style="border-style:solid;border-color:black;" width=193 height=256
alt="CIMAT"></a></td>
<td style="padding:10px"><a href="https://www.ics.uci.edu/~eppstein/pix/cimat/8.html"><img
src="https://www.ics.uci.edu/~eppstein/pix/cimat/8-s.jpg" style="border-style:solid;border-color:black;" width=287 height=162
alt="CIMAT"></a></td>
<td style="padding:10px"><a href="https://www.ics.uci.edu/~eppstein/pix/cimat/9.html"><img
src="https://www.ics.uci.edu/~eppstein/pix/cimat/9-s.jpg" style="border-style:solid;border-color:black;" width=193 height=256
alt="CIMAT"></a></td>
</tr>
</table></div>

The conference activities were all in a single session in a single conference room, and
the center is located some distance from downtown (maybe an hour by foot), with shuttles to our hotels provided only at the start and end of each day. I think this worked very well to bring all the participants together and helped make the conference a success. The topic of the conference is very broad and diverse (all of theoretical computer science) but I was pleasantly surprised how many times I went to a session whose topic I didn't think I cared much about and found a talk that was interesting to me.

The [proceedings are already online](https://doi.org/10.1007/978-3-031-20624-5), published through Springer LNCS, and the conference web site promises free access until the end of November. Besides mine, the invited talks included Jeff Ullman on abstraction in parsing formal languages, Merav Parter on the connections between graph connectivity and the ability of distributed algorithms to resist passive and active attackers, and Mauricio Osorio on the use of non-monotonic and paraconsistent logic to model the ability of human reasoners to work with inconsistent and changing beliefs. There was also an initial day of tutorial sessions that I missed, and a roundtable memorial discussion for [Héctor García-Molina](https://en.wikipedia.org/wiki/H%C3%A9ctor_Garc%C3%ADa-Molina), focused more on his mentorship than his research.

The contributed papers were organized by topic, both in the conference sessions and in the proceedings, but the order of topics differed between the sessions and the proceedings. Among the contributed talks, some that stood out to me (listed in proceedings order) were:

* "[Median and hybrid median $$K$$-dimensional trees](https://doi.org/10.1007/978-3-031-20624-5_3)" by Amalia Duch, Conrado Martínez, Mercè Pons, and Salvadour Roura. If you are given a geometric point set all at once, you can construct a $$K$$-d tree by median bisection with strict rotation through the dimensions, giving provably fast time bounds for certain types of range trees. What if the points come to you incrementally, but in random order? It turns out that some choices of dimension to cut work better than strict rotation.

* "[Near-optimal search time in $$\delta$$-optimal space](https://doi.org/10.1007/978-3-031-20624-5_6)", by Tomasz Kociumaka, Gonzalo Navarro, and Francisco Olivares. This is on [grammar-based compression](https://en.wikipedia.org/wiki/Grammar-based_code) of text in such a way that the compressed text can be used as an index for fast substring lookups. It turns out that this can be done with compressed size roughly proportional to the "substring complexity"

  $$\delta=\max_k\left\{\frac{d_k(S)}{k}\right\},$$

  where $$d_k(S)$$ is the number of distinct length-$$k$$ substrings of a given string.

* "[Klee's measure problem made oblivious](https://doi.org/10.1007/978-3-031-20624-5_8)", by Thore Thießen and Jan Vahrenhold. The main result is on the problem of computing the volume of the union of rectangles in the plane, or of hyperrectangles in higher dimensions. A known $$O(n\log n+n^{d/2})$$ algorithm of Chan is made oblivious, meaning that its data access pattern depends only on $$n$$ and not on the data. This allows the algorithm to be used in cloud computing in a privacy-preserving way. But beyond this specific computation, the paper presents a general approach that can be applied to many other geometric divide-and-conquer algorithms.

* "[Pathlength of outerplanar graphs](https://doi.org/10.1007/978-3-031-20624-5_11)", by Thomas Dissaux and Nicolas Nisse. This is a variant of the more well-known [pathwidth](https://en.wikipedia.org/wiki/Pathwidth) parameter in which one measures the maximum distance between vertices in a bag of a path-like tree-decomposition instead of the size of the bag. It can be computed exactly in outerplanar graphs but the runtime is impractically large, $$O(n^{11})$$. The authors find a much faster algorithm that gets within additive error one.

* "[Obtaining approximately optimal and diverse solutions via dispersion](https://doi.org/10.1007/978-3-031-20624-5_14)", by Jie Gao, Mayank Goswami, C. S. Karthik, Meng-Tsung Tsai, Shih-Yu Tsai, and Hao-Tsung Yang. An example of the type of problem solved here is to find many low-weight spanning trees such that the sum of their Hamming distances (as sets of edges) is as large as possible. Curiously, the authors were unable to extend their results from spanning trees to TSP tours (without repetition, on metric complete graphs). The tree-doubling heuristic turns trees into tours but their diversity could be lost if you shortcut repeated vertices incautiously.

* "[Multidimensional Manhattan preferences](https://doi.org/10.1007/978-3-031-20624-5_17)", by Jiehua Chen, Martin Nöllenburg, Sofia Simola, Anaïs Villedieu, and Markus Wallinger. Given voter preferences for candidates, when is it possible to embed both voters and candidates into a Manhattan metric space so that the preferences are ordered by distance?

* "[Binary completely reachable automata](https://doi.org/10.1007/978-3-031-20624-5_21)", by David Casas and Mikhail V. Volkov. This is on a generalization of [reset automata](https://en.wikipedia.org/wiki/Synchronizing_word) which, when started in an unknown state, can be taken to any single state by an well-chosen input sequence. Here, one instead wants to find a collection of sequences that take the set of all states to each other set of states. For two-symbol automata, the existence of such a collection can be determined in polynomial time.

* "[Embedding arbitrary Boolean circuits into fungal automata](https://doi.org/10.1007/978-3-031-20624-5_24)", by Augusto Modanese and Thomas Worsch. This concerns the [abelian sandpile model](https://en.wikipedia.org/wiki/Abelian_sandpile_model), a cellular automaton in which each cell has a small number of grains of sand and when it has enough, "topples", sending one grain to each neighbor. Is there any way to determine what happens more quickly than step-by-step simulation? In one dimension, yes, and in three dimensions, no, but 2d remains open. This paper proves $$\mathsf{P}$$-completeness for a variation in which toppling is done to the vertical neighbors and to the horizontal neighbors in alternating steps, rather than in both directions in each step.

* "[On the zombie number of various graph classes](https://doi.org/10.1007/978-3-031-20624-5_32)", by Jit Bose, Jean-Lou De Carufel, and Tom Shermer. This is on a variation of the pursuit-evasion game studied for [cop-win graphs](https://en.wikipedia.org/wiki/Cop-win_graph), where a set of cops pursue a robber along the edges of the graph, alternating moves in which the players can either move along one edge or stay put. A "zombie" is a cop who always shambles towards the robber, rather than more cleverly moving away when that might be needed to corner the robber.

* "[Patterns in ordered (random) matchings](https://doi.org/10.1007/978-3-031-20624-5_33)", by Andrzej Dudek, Jarosław Grytczuk, and Andrzej Ruciński. A typical result: in a [chord diagram](https://en.wikipedia.org/wiki/Chord_diagram_(mathematics)) with $$n$$ chords, there must be a subset of $$\Omega(n^{1/3})$$ of the chords that all nest, all cover disjoint arcs, or all cross. Can such a basic variation of the [Erdős–Szekeres theorem](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Szekeres_theorem) really be new?

* "[Tree $$3$$-spanners on generalized prisms of graphs](https://doi.org/10.1007/978-3-031-20624-5_34)", by Renzo Gómez, Flávio Miyazawa, and Yoshiko Wakabayashi. A tree $$k$$-spanner is a spanning tree of a graph such that every graph edge can be replaced by a path of at most $$k$$ edges in the tree. $$2$$-spanners are easy and $$k$$-spanners are hard for $$k\ge 4$$ but the complexity of finding $$3$$-spanners has been open since 1995.

* "[A general approach to Ammann bars for aperiodic tilings](https://doi.org/10.1007/978-3-031-20624-5_35)", by Carole Porrier and Thomas Fernique. Two of the many constructions for [Penrose tilings](https://en.wikipedia.org/wiki/Penrose_tiling) are the cut and project method, in which the tiling is formed from the square faces in a 2d tube through a 5d hypercube tiling, and the method of Ammann bars, in which the prototiles are decorated with line segments that must link up to form the lines of a line arrangement. So far the cut and project method has appeared to be much more fertile, leading to many other types of aperiodic tiling. The authors find a general method for showing that some of these other tilings also can be constructed using Ammann bars. [The arXiv version](https://arxiv.org/abs/2205.13973) has more including a link to [SAGE code for generating these tilings as svg images](https://github.com/cporrier/Cyrenaic).

* "[Improved parallel algorithms for generalized Baumslag groups](https://doi.org/10.1007/978-3-031-20624-5_40)", by Caroline Mattes and Armin Weiß. One of the pluses of having such a broad conference is that it brings together people with highly varied research specialties and produces synergies between areas that might otherwise not connect. This paper has the same flavor, bringing together parallel computational complexity theory and [combinatorial group theory](https://en.wikipedia.org/wiki/Combinatorial_group_theory).

* "[Complexity results on untangling red-blue matchings](https://doi.org/10.1007/978-3-031-20624-5_41)", by Arun Kumar Das, Sandip Das, Guilherme da Fonseca, Yan Gerard, and Bastien Rivier. Suppose you have a red-blue matching between $$n$$ red and $$n$$ blue points in the plane, and you want to remove all crossings by re-matching pairs of crossing edges. How many of these flips does it take? There are many unsolved questions. The problem may seem a little artificial (because you can get to an uncrossing matching directly rather than by flipping) but the real motivation is to understand how to turn an approximate TSP tour with crossings into a shorter uncrossed TSP tour, where the use of flips seems more essential.

The best paper award (named in memory of Alejandro López-Ortiz) was given to "[Theoretical analysis of `git` bisect](https://doi.org/10.1007/978-3-031-20624-5_10)" by Julien Courtiel, Paul Dorbec, and Romain Lecoq (who unfortunately could not present it). The conference also has a "test of time" award, named for [Imre Simon](https://en.wikipedia.org/wiki/Imre_Simon), which went to "[Optimal succinctness for range minimum queries](https://doi.org/10.1007/978-3-642-12200-2_16)" by Johannes Fischer from 2010.

All in all, a very successful conference, and one I'm very happy to have traveled to.

([Discuss on Mastodon](https://mathstodon.xyz/web/@11011110/109338576841926898))