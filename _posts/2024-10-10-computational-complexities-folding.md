---
layout: post
title: Computational complexities of folding
date: 2024-10-10 22:53
---
I turned my talks at OSME and JCGCG<sup>3</sup> this summer into a paper: "Computational Complexities of Folding", [arXiv:2410.07666](https://arxiv.org/abs/2410.07666). It includes the following results:

* Flat-foldability of crease patterns can be tested in time polynomial in the pattern size, exponential in the treewidth of a certain arrangement graph, and factorial in the ply of the folded pattern. The exponential dependence on treewidth is necessary under the strong exponential time hypothesis. This is intended as the journal version of [my CCCG 2023 paper]({{site.baseurl}}{% post_url 2023-06-21-flat-folding-map %}).

* The [nets of certain polyhedra](https://en.wikipedia.org/wiki/Net_(polyhedron)), despite being easy to construct, are hard to fold: the polyhedron they fold into has coordinates that cannot be computed, in an an algebraic computation tree model, allowing either the extraction of <span style="white-space:nowrap">$$n$$th</span> roots of previously-computed values for <span style="white-space:nowrap">arbitrary $$n$$,</span> or the extraction of roots of polynomials of bounded degree. [I posted about this 2015]({{site.baseurl}}{% post_url 2015-12-06-polyhedra-whose-vertex %}) but didn't otherwise publish it.

* For the "flaps and flips" model of origami reconfiguration, in which sheets of origami paper are taped by one edge to a tabletop, and we can change the position of one sheet at a time as long as all sheets lie flat at the end of each move, getting from one flat state to another is <span style="white-space:nowrap">$$\mathsf{PSPACE}$$-complete,</span> and counting the number of flat states is <span style="white-space:nowrap">$$\mathsf{\#P}$$-complete.</span> [I posted about its <span style="white-space:nowrap">$$\mathsf{PSPACE}$$-completeness</span> last August]({{site.baseurl}}{% post_url 2024-08-18-flaps-and-flips %}). The <span style="white-space:nowrap">$$\mathsf{\#P}$$-completeness</span> proof translates counting non-bipartite perfect matchings into [nondeterministic constraint logic](https://en.wikipedia.org/wiki/Nondeterministic_constraint_logic) and from there into flaps and flips.

* For infinite crease patterns, it is undecidable to determine whether a flat folding exists. This strengthens recent Turing-completeness results of Tom Hull and Inna Zakharevich in several ways:

  * The proof uses a finite square sheet of origami, with infinitely many creases on it, rather than the infinite half-plane of Hull and Zakharevich.

  * The crease patterns of Hull and Zakharevich always fold, so testing whether they fold is not hard (just say yes). Instead, their construction proves the undecidability of a more complicated problem: whether a finite perturbation of a periodic crease pattern can be folded so that the perturbation remains finite. The new preprint constructs repeating crease patterns for which foldability itself is hard.

  * Hull and Zakharevich use crease patterns in which the creases are labeled both by whether they are mountain or valley folds, and whether they are mandatory or optional. The new undecidability proofs do not need optional folds, and can work either with labeled or unlabeled crease patterns.

I haven't posted in detail about the undecidability results here, so maybe I should say a little more about them. They are heavily based on the [binary tilings](https://en.wikipedia.org/wiki/Binary_tiling) of the hyperbolic plane, and on the fact that a binary tiling with tiles in the form of <span style="white-space:nowrap">$$2\times 1$$ rectangles</span> fits very neatly into a square of origami paper:

{: style="text-align:center"}
![Binary tiling with columns of red tiles to be used as the states in a time-state diagram of a Turing machine]({{site.baseurl}}/assets/2024/tm-on-binary.svg){: style="width:100%;max-width:540px" }

The main idea of the proof is to form infinite crease patterns in which each tile of a binary tiling gets creased in the same way, with creases that simulate part of a logic circuit. The idea of using creases to simulate circuits was also used by Hull and Zakharevich, and before them in <span style="white-space:nowrap">$$\mathsf{NP}$$-completeness</span> proofs for finite flat-foldability by Bern and Hayes and by Akitaya et al. In fact, my preprint uses exactly the same circuit building blocks as Akitaya et al., with some extra care to show that they can produce arbitrary finite circuits within each tile that connect together across tile boundaries.

There are actually two variations of the proof. One variation shows that it is hard to test foldability for a fixed crease pattern or circuit within each tile, plus a partial folding of the pattern on finitely many creases. The second variation avoids the partial folding, at the expense of making the crease pattern within each tile vary.

The first variation is based on simulating Turing machines. In the binary tiling above, the successive states of a [universal Turing machine](https://en.wikipedia.org/wiki/Universal_Turing_machine) and its tape can be recorded in the red vertical stripes, ordered from left to right. The circuit within each tile ensures that the successive red stripes carry out the correct behavior of the Turing machine, that the blue tiles convey the state of the machine across from one stripe to the next, and that if the Turing machine ever halts the pattern will fail to fold. The initial partial folding sets the initial state of the Turing machine in the leftmost stripe. Since the [halting problem](https://en.wikipedia.org/wiki/Halting_problem) is hard, so is testing foldability of this crease pattern and partial folding.

When I spoke about this at JCDCG<sup>3</sup>, I had only this variation. Someone in the audience (unfortunately I forget who) asked whether the finite set of initial folds were necessary. Later in the conference, Stefan Langerman spoke about certain problems involving [Wang tiling](https://en.wikipedia.org/wiki/Wang_tile). These two things come together in the second variant of my undecidability proof for flat foldability.

In the Wang tiling problem, you are given a finite set of prototiles (usually square, with colored edges), and you are asked to tile the plane by translating these prototiles without rotation. The tiles are required to fit together, edge-to-edge, with matching edge colors. This is, famously, undecidable. It's easy to prove this if you're allowed to force one special starting tile to be included. Then, you can design Wang tiles that, if they tile, will form the time-space diagram of a Turing machine, with the one special tile used to fix its initial state. It's harder to prove, but still true, that Wang tiling is hard even without a fixed special tile. Stefan used this problem as the basis for a proof, with Erik Demaine, that it's undecidable to test whether three given polygons can tile the plane (allowing rotations), improving a previous result that tiling for five polygons is hard. Their preprint, "Tiling with three polygons is undecidable", was also recently uploaded as [arXiv:2409.11582](https://arxiv.org/abs/2409.11582).

{: style="text-align:center"}
![Binary Wang tiling]({{site.baseurl}}/assets/2024/binary-wang.svg){: style="width:100%;max-width:720px" }

One can ask about Wang tiling problems for other shapes of tiles, and [a 2007 paper of Jarkko Kari](https://doi.org/10.1007%2F978-3-540-74593-8_6) showed that Wang tiling is hard for the tiles of a binary tiling. A minor technicality is that a tiling of the entire hyperbolic plane and a tiling of an origami square are not quite the same thing, but one exists if the other does. An example of a binary tiling Wang tiling instance (with four prototiles) and a partial solution to it is shown above, with the matching edge colors shown as colored circles. It's easy to design finite logic circuits, for any binary Wang tiling instance, that fit within each tile, nondeterministically guess a color for each edge, check that each tile is colored to match a prototile, and fail to fold if not. The crease pattern formed by using creases to simulate these circuits, in each tile of a binary tiling, is flat foldable if and only if the given Wang tiling instance is solvable. Therefore, it's undecidable to test whether crease patterns that repeat in the pattern of a binary tiling can be folded flat, even when no partial folding is given.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/113287277159053755))