---
layout: post
title: Connectivity and finiteness in modal graph logic
date: 2019-07-13 21:57
---
I read with interest Joel David Hamkins' recent blog post on [modal model theory](http://jdh.hamkins.org/modal-model-theory/).
This week, on a long plane flight home from Italy, I was inspired to play with the modal logic of graphs, in which one describes properties of graphs by simpler properties of their (induced) supergraphs. My interest is less in what this says about set theory and model theory, and more in how expressive this language is: which graph properties can it describe? Joel showed in his post how to describe $$k$$-colorability in this theory, but I thought it would be of interest to start with something simpler than an $$\mathsf{NP}$$-complete problem. And what could be simpler for graphs than testing whether a graph is connected or finite?

The basics of modal graph logic
===============================

[Modal logic](https://en.wikipedia.org/wiki/Modal_logic) is a logic of "possible worlds" with two operators on formulas, $$\Diamond F$$ (it is possible for $$F$$ to be true, in at least one possible world) and $$\Box F$$ (it is necessary for $$F$$ to be true, in all possible worlds).
Modal graph logic applies this idea to the first-order [logic of graphs](https://en.wikipedia.org/wiki/Logic_of_graphs), in which one can quantify over variables that represent graph vertices and use a binary predicate $$\sim$$ representing adjacency of pairs of vertices. I'll assume here that all graphs are simple and undirected (i.e., $$\sim$$ is irreflexive and commutative). A given graph $$G$$ models a given first-order formula $$F$$ (written as $$G\models F$$) if the formula becomes true when you evaluate it in the obvious way for the given graph. In the modal logic of graphs, the possible worlds are graphs containing $$G$$ as an induced subgraph. So $$\Diamond F$$ means that it is possible for $$F$$ to be modeled by one of these larger graphs and $$\Box F$$ means that it is necessary for $$F$$ to be modeled by all of these larger graphs.

In some ways this is enormously powerful: the class of all graphs containing $$G$$ is so big that it's not even a set, and it can encode arbitrarily complicated structures. In other ways this is more highly constrained than other graph logics like monadic second-order logic (in which one can describe and quantify sets of vertices or edges, but not more complicated structures like sequences of vertices or strategy trees over games defined on the graph). The issue is that in a possible world, one can't tell the vertices that were part of the base graph apart from the ones that were added later, except possibly for a finite set of vertices named in variables outside the modal operator. So while the possible worlds that model a given formula can be very large and complicated, it can be difficult to anchor these castles in the air to the base graph that you started with.

Joel's description of how to express $$k$$-colorability suggests a path around this difficulty: Suppose we want to test a hereditary property $$P$$ of graphs (one that extends from any graph to its induced subgraphs) such as colorability. Then we should look for a family of self-verifyingly-$$P$$ graphs: a family of graphs with property $$P$$ such that membership in the family can be tested by a first-order formula $$F$$ and such that every graph with property $$P$$ is an induced subgraph of a larger graph in this family. If we can find such a family and first-order formula $$F$$, then $$\diamond F$$ will describe property $$P$$ itself. For instance, for colorability, the self-verifyingly-$$k$$-colorable graphs are graphs in which each color class has a universal vertex, every vertex is adjacent to all but one of the universal vertices, and no two adjacent vertices are both non-adjacent to the same universal vertex.

Similar ideas can also work when the property is not hereditary (for instance, a graph has chromatic number 3 when it is 3-colorable but not 2-colorable) or when checking membership in the family of self-verifying graphs itself involves modal logic (as we'll see for testing finiteness).

Connectivity
============

Connectivity is not hereditary: every connected graph is part of a larger disconnected graph and vice versa. But the property that some particular pair of vertices $$u,v$$ is separated is hereditary: if $$u$$ is separated from $$v$$, the two vertices remain separated in any induced subgraph that contains them both. And while it's not possible to verify this directly in a first order formula, for all graphs, it is possible in a special family of disconnected graphs, the ones containing a _transitive vertex_, one whose neighborhood forms a connected component of the graph. We can define a formula

$$\operatorname{transitive}(w)\equiv \forall x\forall y\bigl((w\sim x\wedge x\sim y)\rightarrow w\sim y\bigr)$$

which characterizes these transitive vertices. (Here I am using $$\equiv$$ to mean syntactic equivalence of formulas or definition of the name of a formula, rather than its meaning in Joel's post, equivalence of models.) Then we can test whether $$u$$ is separated from $$v$$ by the formula

$$\operatorname{separated}(u,v)\equiv\Diamond\exists w\bigl(\operatorname{transitive}(w)\wedge u\sim w\wedge\lnot(v\sim w)\bigr).$$

(Here, the instance of "transitive" on the right hand side is not a unary predicate, even though it looks like one; it should be expanded by the definition of the "transitive" formula to produce the resulting "separated" formula. Think of it as being like a C preprocessor macro.)
If $$u$$ is indeed separated from $$v$$, there is a possible world modeling the formula, in which we add an extra vertex $$w$$ to the starting graph, adjacent to everything in the connected component of $$u$$. And in any possible world modeling the formula, $$u$$ is separated from $$v$$, and this must remain true in every induced subgraph of this possible world, including the base graph. Finally, a graph is connected if and only if it has no separated pair:

$$\operatorname{connected}\equiv\lnot\exists u\exists v\,\operatorname{separated}(u,v).$$

In MSO logic, one of the standard tools is the _method of syntactic interpretations_. This allows you to modify your base graph $$G$$ to form a different graph $$G'$$ (for any of certain standard types of modification) and test whether the resulting graph models a given formula $$F$$. To do this, you instead modify the formula (in certain purely mechanical ways derived from how you were modifying $$G$$) and test whether your original graph models the modified formula $$F'$$. The same thing works in first-order logic and in modal logic, and allows such modifications as adding or removing an edge between given vertices, removing any given vertex, restricting to a logically-specified induced subgraph, or adding a new vertex with a logically-specified adjacency relation. I'll write $$F_{G'}$$ for the modified formula that simulates formula $$F$$ on the modified graph $$G'$$. We can use this idea to extend connectedness to other properties; for instance, a graph is a forest if it has no cycle, and this is true if every edge removal disconnects it:

$$\operatorname{acyclic}\equiv\forall u\forall v\bigl(u\sim v\rightarrow\operatorname{separated}_{G-uv}(u,v)\bigr).$$

Finiteness
==========

Following the earlier outline,
I'd like to find a simple family of finite graphs for which their finiteness is
so obvious that it can be tested by a simple logical formula, and then embed
every finite graph into one of these simple finite graphs.

The first natural choice of such a family is the family of paths.
We can define a path to be a connected graph with exactly two degree-one vertices in which all remaining vertices have degree two. Checking the degrees is first order, but I'll spare you the messy details of the formula. All such graphs are finite, because a graph is connected if and only if every two vertices are a finite distance apart, and when the endpoints of a path are a finite distance apart there can be only finitely many other degree-two vertices between them. Any other vertices outside of this finite set must belong to a different component.

Not every finite graph can be embedded into a path. However, every finite graph has a perfect matching to the vertices of a path. To check the existence of an induced perfect matching between two sets of vertices in a graph, it's helpful to have an extra vertex $$v$$ that is not part of the matching, but that distinguishes one side of the matching (the neighbors of $$v$$) from the other side:

$$
\begin{align}
\operatorname{matched}(v)\equiv
\forall x\exists!y\Bigl(
&\bigl(x=v\rightarrow y=v\bigr) \wedge\\
&\bigl(x\sim v\rightarrow (x\sim y\wedge \lnot(v\sim y))\bigr) \wedge\\
&\bigl(\lnot(x=v\vee x\sim v)\rightarrow (x\sim y \wedge y\sim v)\bigr)
\Bigr).
\end{align}
$$

Here, $$\exists!$$ is shorthand for the [existence of exactly one thing](https://en.wikipedia.org/wiki/Uniqueness_quantification). With this test for an induced perfect matching in hand, we can check for a perfect matching to a finite path by

$$\operatorname{finite}\equiv\Diamond\exists v\bigl(
\operatorname{path}_{N(v)}\wedge
\operatorname{matched}(v)\bigr),$$

where $$N(v)$$ denotes the open neighborhood of $$v$$, the graph induced by the vertices adjacent to $$v$$.

I don't think it's possible to test finiteness in the same way in MSO.
We can define paths in MSO, and force them to have a perfect induced matching to the remaining vertices. But the recipe above breaks down at the point where it embeds the given graph into a supergraph, not generally possible in MSO. More generally I don't think it's possible in MSO to distinguish the family of finite complete graphs from their limit, the countable complete graph.

Additional properties
=====================

The same technology of paths and matchings can also be used to formulate not-very-natural properties of finite graphs that are definitely not expressible in MSO. For instance, we can check whether a graph $$G$$ is the disjoint union of two equal-length paths, by first checking that it is a forest with four degree-one vertices and the rest degree-two, and then checking that both paths can be simultaneously perfectly matched to a third path of remaining vertices (with an additional vertex used to distinguish the sides of the matching as above). When this structure exists, the whole graph forms a polyhedron in the form of a $$3\times n$$ grid with the sides of the grid connected to the distinguishing vertex, and this polyhedral structure can be used to prove that we cannot trick the formula by adding new paths connecting the original path endpoints. In contrast, MSO cannot express equality of path lengths, because (per [Courcelle's theorem](https://en.wikipedia.org/wiki/Courcelle%27s_theorem)) it can only express properties of path-like graphs that can be expressed as regular languages (over bounded-width path-decompositions of the graph), and equality of length is context-free but not regular for path-decompositions that concatenate the two paths separately.

It's also possible to express that the [degeneracy of a graph](https://en.wikipedia.org/wiki/Degeneracy_(graph_theory)) is at most some constant $$k$$ in modal logic. As special cases, the graphs of degeneracy zero are the independent sets (first-order expressible) and the graphs of degeneracy one are the forests, which we've already seen how to express. Otherwise, we can represent sequences of vertices by _ladders_, paths of degree-three vertices matched to independent sets of degree-two vertices, with the represented sequence being the other endpoints of these degree-two vertices. Adding a ladder to a graph of degeneracy at least two doesn't change its degeneracy, and we can express the existence of a degeneracy ordering of a finite graph (a sequence of the vertices such that all vertices have at most $$k$$ neighbors that are later in the sequence) by the addition of a ladder with a designated starting vertex that touches all non-ladder vertices.
Each non-ladder vertex $$v$$ should have at most $$k$$ neighbors with the property that, within the ladder, the ladder vertex nearest $$v$$ separates the top of the ladder from the ladder vertices nearest these neighbors.

We can [extend the concept of degeneracy from finite to infinite graphs]({{site.baseurl}}{% post_url 2019-01-17-orientations-infinite-graphs %})
by requiring that every finite subgraph have degeneracy at most $$k$$.
With this definition, we can identify a finite subgraph as the neighbors of a ladder, and then use the formula for finite-graph degeneracy on these neighbors.
This leads to a modal logic expression for infinite graph degeneracy in which the overall structure of the formula is that it is necessary that, whenever a vertex $$v$$ forms the start of a ladder, it should be possible for there to exist another ladder defining a degeneracy ordering for $$v$$'s ladder and its neighbors.

I suspect, although I haven't worked out all the details, that planarity testing is also expressible in modal logic. Here's the outline of an idea for proving this. First, we can check that the graph is finite, to avoid complications of which infinite graphs should be considered to be planar or what a drawing of an infinite planar graph might look like. Next, a graph is planar if and only if it is part of a maximal planar graph, one in which all edges belong to exactly two [peripheral triangles](https://en.wikipedia.org/wiki/Peripheral_cycle). A graph with this two-peripheral-triangle property is planar if and only if one can partition its edges into two subsets, one of which forms a spanning tree for the graph and the other of which forms a spanning tree for the dual graph of the peripheral cycles. (The two-peripheral-triangle property defines a surface embedding which, if non-planar, would have some leftover edges that are neither part of a spanning tree nor a complementary dual spanning tree; see my paper "[Dynamic generators of topologically embedded graphs](https://www.ics.uci.edu/~eppstein/pubs/p-dyngen.html)".) And it should be possible to describe this partition in a planarity-preserving way by decorating the edges on one side of the partition by additional small planar graphs (maybe even just attaching a triangle to each decorated edge). So all we need to check is that it's possible for the given graph to be part of a larger graph
that looks like a maximal planar graph with some decorated edges (ignoring the decorations, each edge belongs to two peripheral triangles) and that the decorations describe a spanning tree and a dual spanning tree. We already know how to describe spanning trees and dual spanning trees should also be possible using similar logic.

One natural and simple property that I don't see how to express in modal logic is regularity. One can ask: do each two vertices have the same degree? And equality of sets of vertices can be checked by the existence of perfect matchings, as in the two-equal-paths example. But how do we know, in a possible world, which neighbors of two given vertices are original and which are added? For the same reason, the property of having a perfect matching seems difficult to express in modal logic, even though it is easy in MSO$${}_2$$. Again, it seems difficult to impose any extra structure on a supergraph without losing too much information about which parts of the graph are original. 

Standard and nonstandard models
===============================

I have been (deliberately) naive here about what kind of set theory I am using to define my graphs, what "all induced supergraphs" means (do I consider graphs only over some set of candidate vertices, or the proper class of all graphs in some set theory), and whether there is always a "correct" value of $$G\models F$$ that our models of modal graph logic should produce for a given graph and formula. If these naive assumptions are not valid, the description of what these formulas express may be inaccurate.

In particular, the claim that a graph is connected if and only if every two vertices are a finite distance apart uses concepts of distance that go beyond the first-order theory of graphs. In non-standard models of set theory, or in standard models of set theory but with non-standard collections of possible worlds that are not really the collection of all induced supergraphs of a given graph, that claim may fail to be true. In such cases, the finiteness formula may determine that an infinite graph (one that models the first-order logical formulas stating that there exist at least $$k$$ distinct vertices, for every finite integer $$k$$) is finite. It's not a bug in the formula, just an indication that you need to be careful about your models. Or in computer science terms, [GIGO](https://en.wikipedia.org/wiki/Garbage_in,_garbage_out).