---
layout: post
title: An unflippable polygon
date: 2020-01-29 19:23
---
We have neither a polynomial-time algorithm for counting the [polygonalizations of a point set]({{site.baseurl}}{% post_url 2020-01-12-counting-grid-polygonalizations %}), nor a proof that the problem is hard. Given this lack of knowledge, it is natural to ask whether the number of polygonalizations can at least be approximated efficiently. A well-known principle in this area states that approximate counting is almost the same as approximately-uniform random generation (an algorithm for one can often be converted to an algorithm for another). And a standard method for randomly generating combinatorial objects is to set up a [Markov chain](https://en.wikipedia.org/wiki/Markov_chain) whose states are the objects and whose [stationary distribution](https://en.wikipedia.org/wiki/Stationary_distribution) is the [uniform distribution](https://en.wikipedia.org/wiki/Discrete_uniform_distribution). A long-enough random walk in this Markov chain will then lead to a state that is approximately uniformly distributed. The hard part, though, is finding a Markov chain for which one can prove that "long enough" is only polynomially many steps; that is, it [_mixes rapidly_](https://en.wikipedia.org/wiki/Markov_chain_mixing_time).

For polygonalizations, a natural family of moves to consider are the _flips_ in which we remove two edges from a polygon through the given points and replace them by a different two edges. There are two possible pairs of replacement edges, but one of the two never works: it would reconnect the two paths formed by removing the two edges into two cycles, instead of a single cycle. The other replacement sometimes works, and sometimes produces two crossed edges, also disallowed. Before we ask whether a Markov chain with these moves mixes rapidly, though, we need to ask whether it is even connected. Can we get from every polygon to every other polygon through the same set of points by making a sequence of flips?

This question was already considered in 2002 by Carmen Hernando, Michael E. Houle, and [Ferran Hurtado](https://en.wikipedia.org/wiki/Ferran_Hurtado) in their paper "On local transformation of polygons with visibility properties" ([_Theor. Comput. Sci._ 289 (2): 919–937, 2002](https://doi.org/10.1016/S0304-3975(01)00409-1)). Unfortunately, they shows that it is not always possible. In particular, they found the following polygon, from which no flip is possible:

{: style="text-align:center"}
![Unflippable polygonalization, redrawn from an example of Hernando, Houle, and Hurtado]({{site.baseurl}}/assets/2020/unflippable-polygon.svg)

More, the same polygon also cannot be changed by another kind of step that Hernando et al. call a VE-flip, in which one removes three edges, two of which are attached to the same point, and replaces them by a different three edges. In effect, this step moves the point to a different part of the polygon while leaving the cyclic sequence of the other points unchanged.

Hernando et al. ask whether there is any finite bound on the number of edges one may need to remove and replace in each step, in order to be able to convert any polygon into any other polygon on the same points. As far as I know, this 18-year-old problem remains open.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/103570191718435766))