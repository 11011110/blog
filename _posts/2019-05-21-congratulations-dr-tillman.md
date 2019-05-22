---
layout: post
title: Congratulations, Dr. Tillman!
date: 2019-05-21 18:20
---
Today I participated in the successful dissertation defense of Bálint Tillman, a student of Athina Markopoulou in the [UCI Graduate Program in Networked Systems](http://www.networkedsystems.uci.edu/). 

Bálint has been investigating problems connected with the [Erdős–Gallai theorem](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Gallai_theorem), which states that it is possible to test whether a sequence of numbers is the degree distribution of a graph (the sequence of numbers of vertices of each possible degree) and if so, find a graph with that degree distribution, in polynomial time. The degree distribution can be extended to a matrix called the _joint degree distribution_, which specifies the number of pairs of adjacent vertices with each combination of degrees, and to higher-order tensors specifying the degrees of subgraphs with more than two vertices.

In his INFOCOM 2015 paper "[Construction of simple graphs with a target joint degree matrix and beyond](https://doi.org/10.1109/INFOCOM.2015.7218534)", Bálint showed that one can recognize the joint degree distributions of simple graphs, and reconstruct a graph with that distribution, in polynomial time. The algorithm works equally well when the vertices are distinguished in other ways than by degree and the input matrix specifies the target number of edges with each pair of degrees between each class of vertices. Later, in KDD 2017, he extended these results to directed graphs and at NetSci 2018 he showed how to find a realization with as few connected components as possible.

On the other hand, if one adds only a little bit of extra information to the joint degree distribution, such as the total number of triangles in the graph, it becomes NP-complete to recognize whether the input describes a valid graph and NP-hard to reconstruct a graph that realizes a given description. This comes from a poster by Bálint with Will Devanny and me at NetSci 2016, where we found the reduction from graph 3-coloring depicted below.

{: style="text-align:center"}
![NP-completeness reduction from 3-coloring to realizability of joint degree matrices with numbers of triangles]({{site.baseurl}}/assets/2019/jdm-tri-hard.svg)

To perform an NP-hardness reduction, one should start with a graph for which it's hard to test 3-colorability, and translate it into an instance of whatever other problem you want to prove hard. But instead let's pretend for now that we start with a little more information: a graph that's known to be 3-coloring, and a specific 3-coloring of it.
To turn this into a hard problem for realizability of joint distribution plus number of triangles, we add a triangle to the graph, representing the three colors, and connect each original graph vertex to the new triangle vertex for its color. Then we add enough hair (in the form of degree-one vertices) to the augmented graph to make all vertices have distinct degrees, except within the triangle of new vertices where all three degrees should be the same. Now take as the result of the reduction the pair $$(J,T)$$ of the joint degree distribution and number of triangles in the augmented graph.

But now the trick is that $$(J,T)$$ can be computed directly from your starting graph, without knowing its coloring or even whether it is colorable.
Because the degrees are distinct, and $$J$$ tells you the number of edges for each combination of degrees, any realization of $$(J,T)$$ must contain a copy of your starting graph augmented by a triangle. The graph and the triangle might be connected to each other differently than they were before, but their connection pattern must still correspond to a different valid 3-coloring, because otherwise you would form some extra triangles in the graph (one for each invalidly-colored edge) and not correctly match the value of $$T$$. So $$(J,T)$$ is realizable if and only if your starting graph has a $$3$$-coloring. This reduction proves that testing realizability of pairs $$(J,T)$$ is NP-complete.

There's even more material along these lines in Bálint's dissertation, but some of it is not yet published. I think the plan is to get all of that submitted over the summer before
Bálint starts a new position at Google.
Congratulations, Bálint!

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/102137081740561085))