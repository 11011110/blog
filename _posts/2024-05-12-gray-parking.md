---
layout: post
title: Gray parking?
date: 2024-05-12 23:01
---
After another Good Article pass for an article on [ordered Bell numbers](https://en.wikipedia.org/wiki/Ordered_Bell_number), I thought it might be interesting to investigate Gray codes for the things counted by these numbers. That is, one would like to find a sequence (or preferably a cyclic sequence) through all of the things, making only a small change from thing to thing, preferably easy to compute.

A prototypical example is the [Steinhaus–Johnson–Trotter algorithm](https://en.wikipedia.org/wiki/Steinhaus%E2%80%93Johnson%E2%80%93Trotter_algorithm), which can list all the $$n!$$ permutations of $$n$$ things, in constant time per permutation, with two permutations differing only be a swap of adjacent elements. If, instead, one looks at the inverses of the permutations, then each two permutations in the sequence differ by adding one to one of the numbers in the permutation and subtracting one from another. This again causes a swap, but of elements with adjacent values rather than adjacent positions.

Permutations describe linear orderings of items, and the best-known thing counted by the ordered Bell numbers are weak orderings, linear orderings with ties. But unlike permutations its somewhat non-obvious how to represent these things in a format that can be output by an enumeration algorithm that makes only a small change from thing to thing. One could plausibly represent a weak ordering by the set of its dichotomies (partitions into two subsets that are consistently ordered relative to each other) and interpret a small change as meaning adding or removing a single dichotomy; I'll get back to that towards the end of this post.

Less well known, but more like permutations, are "unit interval parking functions". To describe these, let's start with [parking functions](https://en.wikipedia.org/wiki/Parking_function). A parking function is just a list of $$n$$ numbers from $$1$$ to $$n$$ (like a permutation), with the property that, when sorted, the $$i$$th number is at most $$i$$. There are exactly $$(n+1)^{n-1}$$ of these things, and they form a nice connected state space under even simpler operations than permutations: just add or subtract one from one of the numbers in the list. Here, for instance, are the $$16$$ parking functions for $$n=3$$:

{: style="text-align:center"}
![The 16 parking functions for n=3]({{site.baseurl}}/assets/2024/3-parking.svg)

I've colored these yellow when the sum of the list is odd, and blue when the sum of the list is even. Each step from one parking function to another changes the parity, so this is a bipartite graph. The number of vertices is odd when $$n$$ is even, making impossible a cyclic Gray code (a Hamiltonian cycle in this graph). Worse, in the case $$n=3$$ shown, there are nine blue vertices and only seven yellow vertices, making impossible a Gray code even if a cyclic sequence is not required: any Gray code would have to alternate between blue and yellow, only possible when their numbers are within one of each other. The imbalance gets worse with larger $$n$$: $$60$$ and $$65$$ vertices on each side for $$n=4$$, and $$640$$ and $$656$$ for $$n=5$$.

These are called parking functions because of the following thought experiment. Imagine that $$n$$ cars travel along a one-way street with $$n$$ parking spaces, each looking for a space to park. The $$i$$th car has a favorite parking spot, and will try to park in its spot, moving on to the next later spot if that is occupied. The parking functions describe exactly the systems of favorites that allow every car to park! If the preference of the $$i$$th car is given by the value in position $$i$$ of a parking function, then enough cars will have early-enough preferences to fill all of the spots; otherwise, one of the early spots will go unfilled and one of the cars with a later preference will not be able to find an open spot. In the image below, it looks like spots 1 and 3 are still free, but if you have a later preference you may fail to find a spot.

{: style="text-align:center"}
![One-way parking on Portobello Road, London]({{site.baseurl}}/assets/2024/portobello.jpg 'Cropped from a CC-BY-SA 2.0 licensed image by N. Chadwick, 1 May 2017, from the Geograph project collection, https://commons.wikimedia.org/wiki/File:Portobello_Rd_-_geograph.org.uk_-_5530747.jpg')

With this intuition in mind, a unit interval parking function is a parking function for which every car gets either its favorite spot or the next spot after it. These things correspond to weak orderings, with the cars that get their favorite spot ordered by their position along the street and the other cars tied with the ones before them. For this reason, the unit interval parking functions are counted by the ordered Bell numbers. For $$n=3$$, the only parking functions that are not unit interval parking functions are the ones where the last car wants the first parking spot but has to move along to the third:

{: style="text-align:center"}
![The 13 unit interval parking functions for n=3]({{site.baseurl}}/assets/2024/3-unit-parking.svg)

Here, again, the odd number means that a Hamiltonian path rather than a Hamiltonian cycle is necessary, and in this case it is possible. Is it possible for all $$n$$? I don't know! 
After checking up to $$n=8$$ that the even and odd unit interval parking functions are within one of having the same number, I was able to prove that this remains true for all $$n$$, leaving hope for a Hamiltonian path. So here's my proof.

For the representation of weak orders by sets of dichotomies, we again get a bipartite graph (split into odd and even by the parity of the number of dichotomies). The weak orders come from all the members of the [face lattice](https://en.wikipedia.org/wiki/Face_lattice) of a [permutohedron](https://en.wikipedia.org/wiki/Permutohedron) except for one face lattice member, the empty set, and adding or removing a dichotomy corresponds to moving up or down one step in this lattice. If the empty set were included, the even-dimensional and odd-dimensional faces would be equinumerous; this is just Euler's polyhedral formula, applied to the permutohedron. Without the empty set, there is one more even-dimensional face, because the empty set is odd-dimensional (dimension $$-1$$). So the numbers of dichotomies coming from the faces of different parities are off by one.

Now back to parking. When a car changes its preference by one but doesn't change its parking spot, this corresponds to splitting a tied set of cars into two subsets, or merging two consecutive tied sets of cars into one. When a car changes its preference by one and moves earlier, it must get its preferred spot in both parking assignments. The car that it displaces can only move one spot later, creating a new tie between these two previously un-tied cars. If these two cars trade spots in this way, nobody else can move or change whether it is part of a tie.  So this is also a change of one dichotomy. A change of preference that moves a car later can only be the reverse of this kind of change, the removal of a tie between two cars. So the state space of unit distance parking functions is a subgraph of the state space of dichotomies (it has the same vertices but fewer edges), so it has the same numbers of vertices on each side of its bipartition. Below is the same state space of unit interval parking functions showing in red the missing edges that would be included in the state space of dichotomies. The central vertex, 112, is the weak order in which everyone is tied, and its neighbors are the weak orders with exactly one dichotomy.

{: style="text-align:center"}
![Unit interval parking functions as a subgraph of the state space of dichotomies]({{site.baseurl}}/assets/2024/3-parking-subgraph.svg)

Because of this subgraph relation, if we found a Gray code for unit interval parking functions, it would also be a Gray code for weak orders under dichotomies, but not necessarily vice versa. I don't know whether either kind of Gray code exists for all $$n$$. These sorts of problems can be quite difficult; witness the 30 years between the formulation of the middle levels conjecture (about Gray codes for bisections of a set of odd size) and [its 2014 solution by Torsten Mütze](https://arxiv.org/abs/1404.4442). So I don't feel bad about throwing these questions out there, without a solution or a proof:

* Does the state space of unit interval parking functions always have a Hamiltonian path?

* Does the state space of weak orders under moves that add or remove a dichotomy always have a Hamiltonian path?

I should mention, by the way, that this is not the only notion of adjacency one can use for weak orderings. Another is a notation in which one specifies, for each element, its position in the total ordering of tied equivalence classes of elements (its _height_), using moves from one height vector to another that all arbitrary changes of the heights of a small number of elements. These height vectors are also called _Cayley permutations_. For this notation, Gray codes that change only one height at a time are impossible, but Gray codes that change up to two heights are known; see Baril, "[Gray code for Cayley permutations](https://www.math.md/files/csjm/v11-n2/v11-n2-(pp124-136).pdf)", and Jacques, Wong, and Woo, "Generating Gray codes for weak orders in constant amortized time", [doi:10.1016/j.disc.2020.111992](https://doi.org/10.1016/j.disc.2020.111992). But adding or removing dichotomies can change many heights, and changing one height can add or remove many dichotomies, so these are not the same.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/112432274878315185))