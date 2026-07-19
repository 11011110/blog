---
layout: post
title: Integer complexity and cographs
date: 2026-07-19 12:38
---
The [integer complexity](https://en.wikipedia.org/wiki/Integer_complexity) of a number $$n$$ is the minimum number of ones needed to express $$n$$ as a parenthesized combination of sums and products of ones. For instance, 10 has complexity 7 as it can be expressed using seven ones, but not fewer:

$$10 = (1+1+1)(1+1+1)+1.$$

The largest number with complexity $$k$$ can be obtained by breaking up the sequence of $$k$$ ones into subsequences of two and three ones (with as many threes as possible) and multiplying. For instance, for ten ones, you can't do this with three groups of three (because you get an ungrouped one left over) but you can with two, giving

$$(1+1+1)(1+1+1)(1+1)(1+1)=36.$$

While looking at the integer complexity article on Wikipedia today, it occurred to me that I had seen the same formula for the maximum complexity before. It is the upper bound on [the number of maximal cliques]({{site.baseurl}}{% post_url 2010-06-28-listing-maximal-cliques %}) in an $$n$$-vertex graph. [This upper bound was proven in 1965 by Moon and Moser](https://doi.org/10.1007%2FBF02760024), and in fact [the OEIS sequence for the largest number with complexity $$k$$](https://oeis.org/A000792) cites Moon & Moser but without an explanation. 

It turns out there's a stronger connection, obtained through a class of graphs called [cographs](https://en.wikipedia.org/wiki/Cograph). These are the graphs that can be obtained from a single-vertex graph by operations that take the disjoint union of two smaller cographs, or that complement another cograph (replacing edges by non-edges and vice versa). The resulting structure can be represented by a "cotree", a rooted tree with its leaves labeled by vertices and its interior nodes labeled by 0 or 1, with 0 meaning to take the disjoint union of the subtree graphs and 1 meaning to complement the disjoint union. Adjacent interior nodes with the same label can be merged, giving a unique cotree representation for which the labels alternate on root-to-leaf paths.


{: style="text-align:center"}
![A cotree and the corresponding cograph]({{site.baseurl}}/assets/2008/Cotree_and_cograph.svg)

Every maximal clique in a cograph can be obtained recursively through its cotree. At a 1-node, choose a maximal clique in each child, recursively. And at a 0-node, choose a maximal clique in exactly one child, recursively. It follows that the number of maximal cliques is obtained by [reinterpreting the cotree as an expression tree]({{site.baseurl}}{% post_url 2008-05-13-cographs-as-free %}), multiplying the numbers of maximal cliques at the children of a 1-node, or by summing the numbers of maximal cliques at a 0-node. Each leaf node has only one maximal clique, itself. So for instance if I take the cotree above and interpret it as an expression tree with a sum for each 0-node and a product for each 1-node I get the expression

$$(a+bc+de)(f+g)$$

which (substituting one for each variable) evaluates to six. Through this correspondence, the integer complexity of $$n$$ is exactly the minimum number of vertices of a cograph that has $$n$$ maximal cliques.

This naturally raises the question: what is the minimum number of vertices in a graph that has $$n$$ maximal cliques, without requiring it to be a cograph? Is it ever smaller than the integer complexity? Yes! According to OEIS, the integer complexity of 23 is 11, as obtained for instance through the expression

$$\bigl((1+1+1+1+1)(1+1)+1\bigr)(1+1)+1.$$

But there is a 10-vertex graph with 23 maximal cliques: Just remove any two edges from the complete bipartite graph $$K_{5,5}$$. So the largest numbers with given integer complexity can be obtained by clique-counting in arbitrary graphs, and the integer complexity can always be obtained by clique-counting in cographs, but some integer complexities are not the same as what you get by clique-counting in arbitrary graphs.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/116948477791846477))