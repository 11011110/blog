---
layout: post
title: Hardness of planar Hamiltonian decomposition and linear arboricity
date: 2019-10-12 16:13
---
I was getting ready to start writing a paper proving that [Hamiltonian decomposition](https://en.wikipedia.org/wiki/Hamiltonian_decomposition) and [linear arboricity](https://en.wikipedia.org/wiki/Linear_arboricity) are both <span style="white-space:nowrap">$$\mathsf{NP}$$-complete</span> for planar graphs of maximum degree four. But then I realized that there's a trivial proof, based on known results:

1. Finding a Hamiltonian cycle is <span style="white-space:nowrap">$$\mathsf{NP}$$-complete</span> in 3-regular planar graphs.[^gjs]

2. A 3-regular graph has a Hamiltonian cycle if and only if its [line graph](https://en.wikipedia.org/wiki/Line_graph) has a Hamiltonian decomposition.[^k][^m]

3. The line graph of a 3-regular planar graph (its [medial graph](https://en.wikipedia.org/wiki/Medial_graph)) is a 4-regular planar graph.

4. A 4-regular graph has a Hamiltonian decomposition if and only if the subgraph formed by removing an arbitrarily chosen single vertex has linear arboricity two.

That's not enough for a paper, even though the linear arboricity result resolves a conjecture of Cygan, Hou, Kowalik, Lužar, and Wu (2012).[^c] So instead I'll just leave this here, together with two illustrations I already drew of the gadgets for my proof. It's a reduction from monotone planar 3-sat, in which the variables are connected in a cycle in the plane, the 3-sat clauses with all variables positive are on one side of the cycle, and the 3-sat clauses with all variables negative are on the other side. Here "planar" means that if you represent each variable and clause as a vertex, draw edges from each variable to each clause that uses it, and also draw edges connecting consecutive variables in the cycle, the result is a planar graph.

My reduction adds a special "truth-setting gadget" to the cycle of variables. It represents the variables by regions of the plane, bounded by edges that are forced to belong to the same cycle in any Hamiltonian decomposition. The truth-setting gadget also forms regions of the plane, again bounded by edges that belong to the same cycle. The truth-setting regions extend through the clause gadgets so that they can reach the other clause gadgets on the other sides of them. A variable or negated variable is true if its region's bounding edges are in the other cycle than the truth-setting gadget.

Here is the truth-setting gadget (the colored parts of the figure), and the (very simple) variable gadgets (gray shaded regions). Each variable gadget will have one loop of one color above the midline, and another loop of the opposite color below the midline.

  {: style="text-align:center"}
![Truth-setting and variable gadgets for a reduction from monotone planar 3-sat to Hamiltonian decomposition]({{site.baseurl}}/assets/2019/truth.svg)

And here is the clause gadget:

  {: style="text-align:center"}
![Clause gadget for a reduction from monotone planar 3-sat to Hamiltonian decomposition]({{site.baseurl}}/assets/2019/clause.svg)

The 4- and 8-vertex subunits in the light yellow disks force the partition into two parts of Hamiltonian cycles to be uniquely determined within each gadget, and the 5-vertex subunits between the variable and clause gadget allow the variable to either connect to the parts of the cycles within the clause gadget or to remain separate from them. To construct a Hamiltonian decomposition, you have to have at least one true variable per clause, so that the clause gadget can be connected to the other cycle than the one from the truth-setting gadget. The reduction produces a multigraph rather than a graph, but that's easy to fix by replacing some of the vertices by wheels.

Maybe the same idea of having a truth-setting gadget that passes through the clause gadgets can be useful in some other reductions?

* Footnotes go here
{:footnotes}

[^bh]:  Bondy, J. A. and Häggkvist, R. (1981), "Edge-disjoint Hamilton cycles in 4-regular planar graphs", _Aequationes Mathematicae_, 22 (1): 42–45, [doi:10.1007/BF02190157](https://doi.org/10.1007/BF02190157).

[^c]: Cygan, Marek, Hou, Jian-Feng, Kowalik, Łukasz, Lužar, Borut, and  Wu, Jian-Liang (2012), "A planar linear arboricity conjecture", _Journal of Graph Theory_ 69 (4): 403–425, [doi:10.1002/jgt.20592](https://doi.org/10.1002/jgt.20592).

[^k]: Kotzig, Anton (1957), "Aus der Theorie der endlichen regulären Graphen dritten und vierten Grades", _Časopis Pěst. Mat._ 82: 76–92. As cited by Bondy and Häggkvist.[^bh]

[^m]: Martin, Pierre (1976), "Cycles hamiltoniens dans les graphes 4-réguliers 4-connexes", _Aequationes Mathematicae_ 14 (1/2): 37–40, [doi:10.1007/BF01836203](https://doi.org/10.1007/BF01836203).

[^gjs]: Garey, M. R., Johnson, D. S., and Stockmeyer, L. (1974), "Some simplified <span style="white-space:nowrap">$$\mathsf{NP}$$-complete</span> problems", _Proc. 6th ACM Symposium on Theory of Computing (STOC '74)_, pp. 47–63, [doi:10.1145/800119.803884](https://doi.org/10.1145/800119.803884).