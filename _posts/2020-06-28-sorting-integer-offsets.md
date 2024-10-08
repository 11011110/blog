---
layout: post
title: Sorting with integer offsets
date: 2020-06-28 17:54
---
Here's a cute exercise for the next time you're teaching radix sorting in an algorithms class:

Suppose you're given as input a set of real numbers $$\{x_i\mid 0\le i\lt n\}$$, and an integer parameter $$k$$. Describe an algorithm for sorting the $$kn$$ numbers $$\{x_i+j \mid 0\le i\lt n, 0\le j\lt k\}$$ in time $$O(kn+n\log n)$$. You can assume that standard arithmetic operations on real numbers (including comparisons and rounding down to an integer) take constant time per operation.

Models of computation that mix constant-time real arithmetic and rounding operations can be problematic, as by building up and then rounding numbers with unlimited precision you can access a level of computational power beyond what actual computers can do, but I don't think that's a concern here. If someone wants to use bit-packing tricks to implement a crazy but fast sorting algorithm in this model, they're beyond the level of this exercise.

The same method (which I'm not going to describe, to preserve its value as an exercise) more generally allows you to take as input pairs $$(x_i,m_i)$$ and sort the numbers $$\{x_i+j \mid 0\le i\lt n, 0\le j\lt m_i\}$$ in time $$O(M+n\log n)$$ where $$M=\sum m_i$$. But it relies heavily on the fact that you're adding integers to the $$x$$'s. For a problem that can't be handled in this way, consider instead sorting the numbers $$\{jx_i \mid 0\le i\lt n, 0\le j\lt m_i\}$$ where we multiply instead of adding. Or, if you prefer to view this as a type of [$$X+Y$$ sorting](https://en.wikipedia.org/wiki/X_%2B_Y_sorting) problem, take logs in your favorite base and sort the numbers $$\{x_i+\log j \mid 0\le i\lt n, 0\le j\lt m_i\}$$. It's not at all obvious to me whether this can be done in the same $$O(M+n\log n)$$ time bound.

The motivation for looking at all this is [a question about how to implement the greedy set cover quickly](https://cstheory.stackexchange.com/q/47120/95). You can find the unweighted [greedy set cover](https://en.wikipedia.org/wiki/Set_cover_problem#Greedy_algorithm) in linear time (linear in the sum of the sizes of the input sets; this is an exercise in CLRS), and you can approximate the weighted greedy set cover very accurately in linear time using similar ideas. If you could sort $$jx_i$$ quickly you could use the sorted order to compute the weighted greedy set cover exactly in the same time as the sorting algorithm. Which is totally useless because the greedy cover is already an approximation, so a fast and accurate approximation to the greedy cover is good enough. But I think the question of sorting $$jx_i$$ is interesting despite its uselessness in this application.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/104424777130789257))