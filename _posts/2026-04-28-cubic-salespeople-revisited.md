---
layout: post
title: Cubic salespeople revisited
date: 2026-04-28 19:09
---
Good news: Email from Knuth. Bad news: It begins "is there a bug in your paper?" The paper in question is "[The traveling salesman problem for cubic graphs](https://ics.uci.edu/~eppstein/pubs/p-cubic-tsp.html)" (WADS 2003 and JGAA 2007). Of course the bug report is accurate, but fortunately it can be easily patched.

My paper has algorithms for finding a minimum-weight Hamiltonian cycle (when it exists), in an $$n$$-vertex graph of maximum degree three, in time $$O(2^{n/3})$$, and for listing all Hamiltonian cycles in time $$O(2^{3n/8})$$. Both have since been improved by others. Maciej Liśkiewicz and Martin R. Schuster gave an algorithm for the minimum-weight cycle with time $$O(1.2553^n)$$ in their paper "[A new upper bound for the traveling salesman problem in cubic graphs](https://doi.org/10.1016/j.jda.2014.02.001)" [_J. Discrete Algorithms_ 2014], and Heidi Gebauer gave an algorithm for listing all cycles in time $$O(1.276^n)$$ in her paper "[Enumerating all Hamilton cycles and bounding the number of Hamilton cycles in 3-regular graphs](https://doi.org/10.37236/619)" [_Elect. J. Combinatorics_ 2011]. Despite these improvements, I think it's interesting enough to examine what the issue was with my paper and how to work around it.

The bug is in the case analysis for the algorithm to list all Hamiltonian cycles. The minimum-weight algorithm includes a case where a triangle is contracted into a single vertex. However, for some reason the cycle-listing algorithm omitted that case, and then later tried to assume there were no triangles, but without a valid justification for this assumption. It's not impossible that the rest of the analysis goes through without using the assumption of no triangles, but working out the details looks messy.

Both algorithms in the paper work with a more general problem in which, together with an input graph, one is given "forced edges" which are required to be included in any Hamiltonian cycle. This allows certain simplifications in which, for instance, paths through degree-two vertices or paths of multiple forced edges can be compressed into single forced edges. It's important when listing cycles that the input is a simple graph, not a multigraph, because multigraphs can have as many as $$O(2^{n/2})$$ Hamiltonian cycles. So, when this sort of compression produces a forced edge that's parallel to an unforced edge, the unforced edge can be deleted, and when it produces two parallel forced edges, there can be no Hamiltonian cycle and the algorithm backtracks. After these simplifications, one can assume that the graph is simple and 3-regular rather than merely having maximum degree three, and that no two forced edges are adjacent. But it might still have some triangles.

With that as background, it is indeed possible to eliminate the triangles. Here are the missing cases to do so.

* If a triangle includes a forced edge, then the opposite edge entering the triangle should also become forced. (The paper included a case with the opposite implication, but this direction is needed to preserve the forcing information after the contraction of a triangle, below.) So in the image below, if either of the two thick edges is forced, the other one should be too.

{: style="text-align:center"}
![A triangle with an internal forced edge and an opposite external forced edge]({{site.baseurl}}/assets/2026/triforce.svg)

* If there exists a triangle that does not share any of its edges with another triangle, contract it. Hamiltonian cycles in the contracted graph correspond one-for-one with Hamiltonian cycles in the uncontracted graph, and (with no shared edges) this contraction will not create any parallel edges.

{: style="text-align:center"}
![Contracting a triangle to a single vertex]({{site.baseurl}}/assets/2026/delta-y.svg)

* If there exist two triangles that share an edge, then there are two paths through their four vertices that might extend to Hamiltonian cycles. If only one of these two paths is consistent with the forced edges within this subgraph, add the rest of its edges to the forced set; their contraction will eliminate the triangles. Otherwise, make two recursive branches, each with one of the two paths added to the forced set. Each branch eliminates four previously-unforced edges, consistent with the analysis of the other cases in this part of the paper.

{: style="text-align:center"}
![Two alternative forced paths through a pair of triangles sharing an edge]({{site.baseurl}}/assets/2026/zigzag.svg)

As far as I know, another problem from the same paper remains open. The paper constructs a family of cubic graphs that have $$2^{n/3}$$ Hamiltonian cycles, but the cycle-listing algorithm proves only that the number of cycles is always $$O(2^{3n/8})$$, a bigger number. Gebauer's paper improves the upper bound, but it still does not match the lower bound. Is $$2^{n/3}$$ the maximum number of Hamiltonian cycles in an $$n$$-vertex 3-regular graph?

{: style="text-align:center"}
![Construction for a family of cubic graphs with many Hamiltonian cycles]({{site.baseurl}}/assets/2026/manyham.svg)

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/116485577355514561))