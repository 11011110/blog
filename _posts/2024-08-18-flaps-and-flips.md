---
layout: post
title: Flaps and flips
date: 2024-08-18 21:38
---
My [recent talk at OSME](https://ics.uci.edu/~eppstein/pubs/Epp-OSME-24.pdf) mostly surveyed known material on the computational difficulties of origami folding problems, some of which I've already discussed here: [the impossibility of finding closed-form formulas for the coordinates of folded polyhedra]({{site.baseurl}}{% post_url 2015-12-06-polyhedra-whose-vertex %}) and [the fine-grained complexity of flat folding]({{site.baseurl}}{% post_url 2023-06-21-flat-folding-map %}). But it also included some new results, showing that it's hard to get from one folded state to another by changing one fold at a time, in the following toy folding problem, which I call "flaps and flips".

An instance of this problem consists of some sheets of square origami paper, all the same size, spread out flat on a tabletop. Each of the sheets of paper (a "flap") is taped to the tabletop along one of its edges, making a flexible hinge that allows it to "flip" to a different position, as long as the hinge stays attached to the table along the same line segment. No other flap can come between this hinge and the table, but that is the only restriction on how the flaps can be placed. For instance, there can be cycles in their above-below relations, as with the central red, pink, and green flaps below.

{: style="text-align:center"}
!["Flaps and flips": origami squares taped to a tabletop]({{site.baseurl}}/assets/2024/flaps-and-flips.jpg){: style="width:100%;max-width:540px" }

What you're allowed to do is to move one flap at a time to a different position, keeping its hinge in place. In the example above, the bottom blue flap can be flipped to the other side of its hinge. But the moving flap doesn't have to stay rigid, like a sheet of glass. For instance, it would also be allowed to flip the green flap down, even though another flap partly covers it and its hinge. These are the only two flips possible in the state shown, because the other flaps all have part of their hinges covered, fixing them in place. However, flipping the blue or green flap frees up other flaps that can flip in turn. It would also be allowed to flip a flap by moving it above or below others, keeping its hinge fixed, but allowing or disallowing that possibility turns out not to be important.

Now, for a given system of flaps and hinges, can you get from every flat state to every other flat state by a sequence of flips? Or if I give you two different flat states of the same system of flaps and hinges, can you get from one to the other? If you can, how many moves will it take? It turns out to be very difficult to answer these questions  <span style="white-space:nowrap">($$\mathsf{PSPACE}$$-complete),</span> and the number of moves may be exponential!

As usual, the proof of hardness involves showing that this problem can simulate another problem known to be hard. That other problem is [nondeterministic constraint logic](https://en.wikipedia.org/wiki/Nondeterministic_constraint_logic). Instances of nondeterministic constraint logic take the form of 3-regular directed graphs, with the edges colored blue and red, and with an odd number of blue edges at each vertex. Every vertex must either have at least one blue edge directed into it, or both red edges directed into it. The moves you're allowed to make, in this system, are to reverse one edge at a time, maintaining these constraints. For instance, in the illustration below, some of the red edges can be reversed, but none of the blue ones can, so there is no way to get from the orientation shown to its mirror image. Getting from one orientation of the edges to another, or testing whether all orientations are connected, is known to be  <span style="white-space:nowrap">$$\mathsf{PSPACE}$$-complete,</span> even when the graph is planar and has bounded bandwidth.

{: style="text-align:center"}
![Example of a nondeterministic constraint logic instance]({{site.baseurl}}/assets/2024/cube-match-ncl.svg){: style="width:100%;max-width:720px" }

So to prove <span style="white-space:nowrap">$$\mathsf{PSPACE}$$-hardness</span> (the more difficult part of <span style="white-space:nowrap">$$\mathsf{PSPACE}$$-completeness)</span> for the flaps and flips problem, all we need to do is to show how to represent directed edges, and the two types of vertex with one blue edge and three blue edges, using flaps. But this turns out to be easy, using the three gadgets depicted below for an arrow, blue-red-red vertex, and blue-blue-blue vertex.

For an arrow, just lay out a sequence of flaps, each of which will (when flipped to one side or the other) cover part of the hinge of its neighboring flap in the sequence. If you think of this sequence as forming a directed edge, the arrowhead points to the uncovered hinge at one end. To reverse the edge, you can flip its flaps in order, from the arrowhead to the tail. The intermediate states of these flips will leave the edge having two tails and no arrowheads, but that isn't problematic.

{: style="text-align:center"}
![Gadget for translating arrow of nondeterministic constraint logic into flaps and flips]({{site.baseurl}}/assets/2024/ff-arrow.svg){: style="width:100%;max-width:720px" }

For a blue-red-red vertex, arrange the flaps at the ends of the three edges so that the blue flap can overlap both red hinges, but each red flap can only overlap the blue hinge, as shown. If the blue flap hinge is covered, the blue flap itself must be flipped away from the vertex. In terms of the underlying nondeterministic constraint logic instance, this means that the blue edge points in, as required. If the blue flap is not flipped away, it covers the two red flaps, and the two red edges point in. So this arrangement of flaps has exactly the same behavior as a blue-red-red vertex is required to have: its allowed states are exactly the ones where the blue edge points in, the two red edges both point in, or both of those things happen.

{: style="text-align:center"}
![Gadget for translating red-red-blue vertex of nondeterministic constraint logic into flaps and flips]({{site.baseurl}}/assets/2024/ff-and.svg){: style="width:100%;max-width:720px" }

The blue-blue-blue vertex is shown in two arrangements below, but only one of these can be made with paper and tape. In the left part of the illustration, three flaps at the ends of three blue edges are flipped towards the vertex, corresponding to the forbidden state where the three edges are all directed outward from the vertex. Each flap overlaps the hinge of a different flap, forming a cyclic system of above-below relations that cannot be realized in the central area where all three flaps overlap. However, if at least one flap is flipped away from the vertex (corresponding to the arrow pointing in), it is realizable, as shown on the right. And in this state, with one arrow pointing in, the other two arrows can flip freely, unobstructed by the flipped-out flap or each other.

{: style="text-align:center"}
![Gadget for translating blue-blue-blue vertex of nondeterministic constraint logic into flaps and flips]({{site.baseurl}}/assets/2024/ff-or.svg){: style="width:100%;max-width:720px" }

So to get a hard instance for the flaps and flips problem, or one that takes many moves to solve, just take a hard instance of nondeterministic constraint logic and translate it in this way. Any move you make in the resulting flaps and flips problem can be translated back into moves for nondeterministic constraint logic, so if you could solve one problem you could solve the other.

What I'd like to prove is something a little closer to actual origami: that for a single folded sheet of paper, it can be hard to get from one folded state to another using moves that change only a small part of the folding at a time: maybe only a bounded number of creases, or a single above-below relation, or only the creases along a single line segment of the folded model. It is possible to make origami crease patterns that fold to something resembling a tabletop with flaps attached, so maybe this could be used to simulate flaps and flips, simulating nondeterministic constraint logic, simulating arbitrary polynomial-space computation.

{: style="text-align:center"}
![Crease pattern for folding flaps on a single sheet of paper]({{site.baseurl}}/assets/2024/flap-cp.svg){: style="width:100%;max-width:720px" }

{: style="text-align:center"}
![Flaps folded from a single sheet of paper]({{site.baseurl}}/assets/2024/flap-3d.svg){: style="width:100%;max-width:540px" }

The last two images are from the [origami maze font generator](https://erikdemaine.org/fonts/maze/) by Erik Demaine, Martin Demaine, and Jason Ku, using just punctuation as text: `',''`. Check it out and design yourself crease patterns that fold to your favorite message!