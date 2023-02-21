---
layout: post
title: Geometric graphs with unbounded flip-width
date: 2023-02-20 21:20
---
At the recent [Workshop on Geometry and Graphs](https://wogag.org/) in Barbados, most of the technical activity involved working in small groups on research problems, but there was also a nice survey talk by [Rose McCarty](https://web.math.princeton.edu/~rm1850/) on flip-width.[^r] This is a new and very general notion of width in graphs, introduced by [Szymon Toruńczyk](https://www.mimuw.edu.pl/~szymtor/).[^t] It is defined in terms of a certain cops-and-robbers game on graphs, and intended to capture the structure inherent in many types of graphs and to unify [bounded expansion](https://en.wikipedia.org/wiki/Bounded_expansion) and [twin-width](https://en.wikipedia.org/wiki/Twin-width).

For instance, many algorithmic graph problems, such as searching for small patterns in larger graphs ("[subgraph isomorphism](https://en.wikipedia.org/wiki/Subgraph_isomorphism_problem)") can be formulated more abstractly in terms of of checking whether a graph models a given formula in the first-order [logic of graphs](https://en.wikipedia.org/wiki/Logic_of_graphs). Such problems are [fixed-parameter tractable](https://en.wikipedia.org/wiki/Parameterized_complexity) when parameterized either by expansion or twin-width, and it is hoped that the same thing will extend to flip-width. Very recent partial results in this direction extend model checking algorithms from bounded expansion to "structurally nowhere dense classes",[^dms] but these classes do not even include everything with bounded twin-width, let alone flip-width.

For the purposes of this post, the only thing we need to know about bounded expansion is that graph families with this property must be sparse: in their graphs, the number of edges must be at most linear in the number of vertices.[^no] On the other hand, although graph families with bounded twin-width can be dense, they are limited in a different way: the number of graphs in the family, on a set of $$n$$ unlabeled vertices, can only be singly exponential <span style="white-space:nowrap">in $$n$$.[^st]</span> One way to get a family of graphs that have bounded flip-width but not bounded expansion nor bounded twin-width is to take the union of two families, one dense with bounded twin-width and the other numerous with bounded expansion. For instance, take the graphs that are either [cographs](https://en.wikipedia.org/wiki/Cograph) or [3-regular](https://en.wikipedia.org/wiki/Cubic_graph). But this is not a very natural family of graphs. Rose asked: is there a natural family of graphs with bounded flip-width but unbounded twin-width and expansion? For instance, there are many standard types of geometric graphs for which the twin-width and expansion are unbounded; could any of these have bounded flip-width?

# Cops and robbers

Like [treewidth](https://en.wikipedia.org/wiki/Treewidth) and bounded expansion, flip-width can be defined using a certain [cops-and-robbers game](https://en.wikipedia.org/wiki/Pursuit%E2%80%93evasion) on graphs.[^t]

The games used for treewidth and expansion involve "cops with helicopters", chasing a robber on a given graph. At each point in the game, the cops occupy a limited number of graph vertices. Then, at each move, the cops announce where they will move next, the robber moves to escape them along a path through the currently-unoccupied vertices, and then the cops fly directly to their new locations. The cops win if one of them lands on the robber's current vertex, and the robber wins by evading the cops indefinitely. The treewidth of a graph is the maximum number of cops that a robber can evade, moving arbitrarily far on each move. A family of graphs has bounded expansion if and only if there is some function $$f$$ such that only $$f(r)$$ cops are needed to catch a robber who can move at most $$r$$ steps per move.[^t2]

As Rose described, the same game can be described in a different way. Instead of occupying a vertex, the cops set up roadblocks on all the edges incident to it. On each move, the cops announce which vertices will be blockaded next. Then, the robber moves along un-blockaded edges. Finally, the cops remove their current blockades and put up new blockades at the vertices they announced. The cops win by leaving the robber at an isolated vertex, unable to move.

{: style="text-align:center"}
![Police roadblock in Washington, DC, January 15, 2021]({{site.baseurl}}/assets/2023/roadblock.jpg 'CC-BY image by Mike Licht from Wikimedia commons, File:Inaugural preparation, January 15th Roadblock (50840138737).jpg'){: style="width:100%;max-width:540px" }

Flip-width is defined in the same way, but with more powerful cops. Instead of blockading a single vertex, they are allowed to perform a "flip" of a subset of vertices. This complements the subgraph within that subset: pairs of vertices that were connected become disconnected, and vice versa. So blockading a single vertex, for instance, can be accomplished by two flips: one flip of the vertex and its neighbors, and one flip of just the neighbors. The first flip disconnects the given vertex, and the second flip restores the original connectivity among the neighboring vertices. It doesn't matter in which order these two flips (or any set of flips) is performed.

{: style="text-align:center"}
![Isolating a vertex by two flips]({{site.baseurl}}/assets/2023/flip-isolate.svg){: style="width:100%;max-width:720px" }

In the flipping game used to define flip-width, at any point in the game, the cops will have performed some limited number of flips. Then in each move, the cops announce which sets of vertices they will flip next. The robber moves along a path in the current flipped graph, to evade these flips. Then, the cops undo their current flips and perform the new flips that they announced. The cops win if they leave the robber at an isolated vertex, unable to move, and the robber wins by avoiding this fate indefinitely. A family of graphs has bounded flip-width if there is some function $$f$$ such that only $$f(r)$$ flips per move are needed to catch a robber who can move at most $$r$$ steps per move.

For the purposes of having bounded flip-width, two graphs that differ from each other only by a finite number $$\varphi$$ of flips are essentially the same. If the cops can win on one, they can win on the other with only $$\varphi$$ more flips per move. They only need to start by performing those $$\varphi$$ flips to convert the second graph into the first one, and then leave those flips in place while they perform the winning strategy on the converted graph. So, for instance, the graphs that differ by a single flip from a 3-regular graph have bounded flip-width, but are again not a very natural class of graphs.

# Interchanges

Continuing the road network metaphor, and in the spirit of the [havens](https://en.wikipedia.org/wiki/Haven_(graph_theory)) used to model escape strategies in the treewidth game, let's define a structure I call an _interchange_, having pairwise connections between many points, which a robber can use to make a getaway from few enough cops.

{: style="text-align:center"}
![High Five Interchange at the intersection of I-635 and U.S. Route 75 in Dallas, Texas, looking towards the southwest]({{site.baseurl}}/assets/2017/HighFive.jpg 'cropped from https://commons.wikimedia.org/wiki/File:High_Five.jpg by fatguyinalittlecoat on flickr, under a CC-BY 2.0 license'){: style="width:100%;max-width:540px" }

More precisely, define an interchange of order $$n$$ to consist of the following components:

* Certain designated vertices, which we call _lanes_. The interchange should have $$n$$ lanes, arranged into a sequence. These are colored blue in the following illustrations.

* More designated vertices, called _ramps_. Each ramp is associated with a pair of lanes. When two lanes are $$n-3$$ or fewer steps apart in the sequence, they have an associated ramp. (We don't require ramps for pairs of the outermost lanes because they would not be helpful to the robber in the game.) The ramps are colored red in the following illustrations.

* An edge between each ramp and its two associated lanes.

* Optional edges between any two lanes or between any two ramps. These will be unused by the robber and do not affect the robber's strategy. The optional edges mean that the class of all interchanges is huge, too large to have bounded twin-width. But more importantly for us, they allow us to construct geometric realizations of these graphs without worrying about whether or not the construction causes certain pairs of vertices to become adjacent.

* For a ramp that connects lanes $$x$$ and $$y$$, optional edges to other lanes between $$x$$ and $$y$$ in the sequence (edges to lanes outside that range are not allowed).

The image below shows an example, with the lanes blue, ramps red, optional edges yellow, and required edges black. The blue lanes are ordered in a sequence from left to right, but otherwise the placement of vertices is not meaningful; it's the graph structure that matters.

{: style="text-align:center"}
![Interchange of order 5]({{site.baseurl}}/assets/2023/5-interchange.svg){: style="width:100%;max-width:540px" }

As we show next, large-enough interchanges can be used by the robber to escape any fixed number of cops.

# Escaping through junctions

Call a set of lanes _equivalent_, after certain flips have been made, if they are all treated the same by each flip: all included in the flipped set, or all excluded.
Define a _junction_ to be a triple of equivalent lanes that are connected to each other by paths through one or two ramps, after the flips are made. Then:

* Every four equivalent lanes have at least one junction. For, if the lanes are $$a,b,c,d$$ (in sequence order) then the <span style="white-space:nowrap">$$a$$–$$b$$</span> ramp either continues to connect $$a$$ to $$b$$, or it is flipped and instead connects <span style="white-space:nowrap">$$c$$ to $$d$$.</span> A third connection is provided either by the <span style="white-space:nowrap">$$b$$–$$c$$</span> ramp or its flip, which connects <span style="white-space:nowrap">$$a$$ to $$d$$.</span>

* In every six equivalent lanes, at least three of the lanes belong to two otherwise-disjoint junctions. I'll skip the messy case analysis showing this.

* Every two junctions are connected by at least one ramp between two of their lanes. If the junctions are $$a,b,c$$ and $$d,e,f$$, listed in the sequence order of all the lanes, then they have either $$a,b,e,f$$ or $$d,e,b,c$$ as a subsequence (depending on the ordering between <span style="white-space:nowrap">$$b$$ and $$e$$).</span> In either case they are connected by the <span style="white-space:nowrap">$$b$$–$$e$$</span> ramp or its flip.

* By the same argument, every two triples of equivalent lanes are connected by at least one ramp.

These connections imply that, in an interchange that is big enough to guarantee the existence of junctions, the robber can win by always moving to a lane that will become part of a junction after the announced flips happen.

In more detail, suppose that the cops and a robber play the flipping game, with $$t$$ flips per move and $$r\ge 6$$, and that the graph includes an interchange of <span style="white-space:nowrap">order $$3\cdot 2^{2t}+1$$.</span> This interchange is big enough to ensure that some four lanes are equivalent both in the current and announced set of flips. These four lanes include a junction under the announced flips. The robber can move to this new junction using at most two ramps within the current junction and then one more ramp to cross between the two triples of lanes. With an interchange that is a little larger, of <span style="white-space:nowrap">order $$5\cdot 2^{2t}+1$$,</span> the robber can win with $$r\ge 4$$, by moving to a lane that will become part of two otherwise-disjoint junctions, so that two other equivalent lanes will be reachable by only one ramp.

This strategy shows that, if a graph class contains arbitrarily large interchanges, it does not have bounded flip-width. We will use this idea to show that many natural classes of geometric graphs do not have bounded flip-width.

# Geometric graphs

In each of the following types of geometric graph, it is possible to form arbitrarily large interchanges, as illustrated.

* [Interval graphs](https://en.wikipedia.org/wiki/Interval_graph) and [permutation graphs](https://en.wikipedia.org/wiki/Permutation_graph). Just make a left-to-right sequence of small disjoint blue intervals for the lanes, and connect them by longer red intervals for the ramps. Each red interval contains all of the blue intervals that it intersects, and permutation graphs are the same thing as [interval containment graphs](https://www.graphclasses.org/classes/gc_288.html). In contrast, the [unit interval graphs](https://en.wikipedia.org/wiki/Indifference_graph) are known to have bounded twin-width,[^tw3] from which it follows that they also have bounded flip-width.

  {: style="text-align:center"}
![Interval graph forming an interchange of order 6]({{site.baseurl}}/assets/2023/interval-interchange.svg)

* Circle graphs. These have the permutation graphs as a special case, but there's also a direct construction.

  {: style="text-align:center"}
![Circle graph forming an interchange of order 6]({{site.baseurl}}/assets/2023/circle-interchange.svg){: style="width:100%;max-width:540px" }

* Intersection graphs of axis-aligned line segments, no two collinear. Use long horizontal segments for the lanes, ordered vertically, and span them by vertical ramps.

  {: style="text-align:center"}
![Axis-aligned line segments forming an interchange of order 6]({{site.baseurl}}/assets/2023/line-segment-interchange.svg)

* Intersection graphs of axis-parallel unit squares. Place the blue lane squares with their top right corners on a diagonal line, close enough together that any consecutive interval of them can be covered by a red ramp square.

  {: style="text-align:center"}
![Squares forming an interchange of order 6]({{site.baseurl}}/assets/2023/square-interchange.svg){: style="width:100%;max-width:540px" }

* Unit disk graphs. This one is unfortunately difficult to see clearly because the details are tiny with respect to the overall form, even for the $$n=6$$ example shown. Anyway, place $$n$$ blue unit disks tangent to the outside of a circle of radius $$1+\varepsilon$$ (yellow in the figure), so that their points of tangencies span an arc of diameter less than $$2$$. Then place red unit disks with their centers inside the yellow circle, so that their intersections with the circle form arcs that look like the interval graph model above. Because their radius is smaller than the yellow circle, the red disks will bulge out of the yellow circle a little bit. They intersect the blue points of tangency in the pattern that we want, but the parts that bulge out may have some unwanted contacts with the other blue disks. To prevent this, make $$\varepsilon$$ very small. As you decrease $$\varepsilon$$, the red bulges will shrink towards the yellow circle, but the blue disks won't change their positions or angles very much, so for sufficiently small values of $$\varepsilon$$ there will be no unwanted contacts.

  {: style="text-align:center"}
![Unit disks forming an interchange of order 6]({{site.baseurl}}/assets/2023/disk-interchange.svg)

* Unit distance graphs. Place the blue vertices equally spaced along an interval of length less than two and the red vertices that connect them on the points where unit circles centered on the blue vertices cross each other.

  {: style="text-align:center"}
![Unit distance graph forming an interchange of order 6]({{site.baseurl}}/assets/2023/unit-distance-interchange.svg)

* Visibility graphs of simple polygons. Place the blue vertices in sequence order on a horizontal line, the red vertices that connect pairs of consecutive blue vertices in order on a parallel line above them, and the remaining red vertices in an arbitrary order on a parallel line below them. Draw a triangle between each red vertex and the two blue vertices it should connect, and take the union of the triangles. Fill any holes that might have been formed in taking the union. The resulting polygon has additional vertices but that doesn't affect the existence of an interchange. (This construction is simplified from an earlier construction by Rose, of visibility graphs that can be flipped to contain subdivisions of complete graphs.) 

  Visibility graphs are [cop-win graphs](https://en.wikipedia.org/wiki/Cop-win_graph), meaning that a single cop wins a different cop-and-robber game in which both players can either move along a graph edge or stand still.[^lsv] But this doesn't say anything about the flipping game: any graph can be made into a cop-win graph by adding a single [universal vertex](https://en.wikipedia.org/wiki/Universal_vertex), without changing whether it has bounded flip-width.

  {: style="text-align:center"}
![Polygon whose visibility graph forms an interchange of order 6]({{site.baseurl}}/assets/2023/visibility-interchange.svg)

* Four-dimensional convex polytopes. I'm not even going to try to draw this one, but the construction is easy to describe in words. Just take the [barycentric subdivision](https://en.wikipedia.org/wiki/Barycentric_subdivision) of a [neighborly polytope](https://en.wikipedia.org/wiki/Neighborly_polytope). Neighborly polytopes have edges and vertices forming complete graphs; the barycentric subdivision of any polytope is another polytope.[^es] It has a vertex for each face of the original polytope, and an edge for each incidence between faces of different dimensions. Arrange the vertices of the neighborly polytope into an arbitrary sequence as lanes; use the subdivision vertices coming from its edges as ramps. In this way the ramps will be connected only to their two associated lanes and to other subdivision points, but not to any other lanes. 

# Where now?

We're still missing a natural class of graphs with bounded flip-width, unbounded twin-width, and unbounded expansion. The known classes of geometric graphs looked promising as a direction to look for such classes, but these constructions rule that out in surprisingly many cases. 

It still might be possible that the number of cops needed to catch a robber on these graphs could be low. The interchange construction only proves that it is at least logarithmic. But I don't know of any useful algorithmic consequences of having a low but unbounded number of cops needed to catch a bounded-speed robber.

# Notes and references

* Footnotes go here
{:footnotes}

[^r]: Rose also helped me edit a preliminary version of this post. Thanks, Rose! Any remaining errors are my fault.

[^dms]: Jan Dreier, Nikolas Mählmann, and Sebastian Siebertz (2023), "First-order model checking on structurally sparse graph classes", [arXiv:2302.03527](https://arxiv.org/abs/2302.03527)

[^es]: Günter Ewald and Geoffrey C. Shephard (1974), "Stellar subdivisions of boundary complexes of convex polytopes", _Math. Ann._ 210: 7–16, [doi:10.1007/BF01344542](https://doi.org/10.1007/BF01344542).

[^lsv]: Anna Lubiw, Jack Snoeyink, and Hamideh Vosoughpour (2017), "Visibility graphs, dismantlability, and the cops and robbers game", _CGTA_ 66: 14–27, [arXiv:1601.01298](https://arxiv.org/abs/1601.01298)

[^no]: Jaroslav Nešetřil and Patrice Ossona de Mendez (2012), "5.5: Classes with bounded expansion", _Sparsity: Graphs, Structures, and Algorithms_, pp. 104–107, Springer, Algorithms and Combinatorics, vol. 28, [doi:10.1007/978-3-642-27875-4](https://doi.org/10.1007/978-3-642-27875-4)

[^st]: Pierre Simon and Szymon Toruńczyk (2021), "Ordered graphs of bounded twin-width", [arXiv:2102.06881](https://arxiv.org/abs/2102.06881)

[^t]: Szymon Toruńczyk (2023), "Flip-width: cops and robber on dense graphs", [arXiv:2302.00352](https://arxiv.org/abs/2302.00352)

[^t2]: See Corollary 3.6 of Toruńczyk (2023)[^t]

[^tw3]: See Lemma 13 of  Édouard Bonnet, Colin Geniet, Eun Jung Kim, Stéphan Thomassé, and Rémi Watrigant, "Twin-width III: Max Independent Set and Coloring", [arXiv:2007.14161v2](https://arxiv.org/abs/2007.14161v2) (this lemma is not in the _ICALP_ 2021 version and numbered differently in other arXiv versions)

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/109901138706218444))