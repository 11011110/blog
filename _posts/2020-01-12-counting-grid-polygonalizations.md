---
layout: post
title: Counting grid polygonalizations
date: 2020-01-12 13:33
---
A _polygonalization_ of a point set is a simple polygon having all the points as its vertices. Another way to think about it is that it's a non-crossing Hamiltonian cycle in a complete geometric graph. [My recent work on the hardness of counting polygon triangulations]({{site.baseurl}}{% post_url 2019-03-12-counting-polygon-triangulations %}) was motivated in large part by the problem of counting polygonalizations. Counting polygonalizations should also be hard, but I don't know how to prove it, and I was hoping that proving other similar problems hard might either lead to more insights or at least provide something to prove a reduction from.

More recently I've been attacking the problem from a different direction: looking at the number of polygonalizations for special point sets that are structured enough to make it possible to compute the answer easily while not being completely trivial. The point sets I chose were the $$3\times n$$ integer grids. Smaller grids are uninteresting: $$1\times n$$ grids don't have any polygonalizations and $$2\times n$$ grids have only one, the outer rectangle.

In a $$3\times n$$ grid, any polygonalization must touch the outer points of the grid in clockwise order. And any subset of the inner $$n-2$$ points that are between the same pair of outer points can only be connected in consecutive order. So, to describe a polygonalization, we only need to determine for each inner point which pair of outer points it is between. One way to do this is to assign letters to the consecutive pairs of outer points (for instance $$labc\dots r$$ along the upper left, top, and upper right, and $$LABC\dots R$$ along the lower left, bottom, and lower right).
Then, identify each polygonalization with a sequence of letters describing the positions of its $$n-2$$ inner points, in their left-to-right order.

{: style="text-align:center"}
![Polygonalizations of a 2x5 grid labeled by the positions of the three inner points in the cyclic sequence of outer points]({{site.baseurl}}/assets/2020/gridcycles.svg)

This gives a one-to-one correspondence between polygonalizations and strings, where:

* Each string has length $$n-2$$.
* The letters of the strings are drawn from the alphabet $$labc\dots rLABC\dots R$$.
* If a letter appears in a string, all its appearances are consecutive.
* The subsequence of letters from $$labc\dots r$$ appear in that order, as does the subsequence of letters from $$LABC\dots R$$.
* It is not allowed to have both $$l$$ and $$L$$, nor to have both $$r$$ and $$R$$.

These conditions are a little messy, but it's possible to set up a recurrence for the number $$S_z^x(y)$$ of strings that don't use the left and right side symbols, with $$x$$ choices for the top (lower case) symbols, $$z$$ choices for the bottom (upper case) symbols, and $$y$$ labeled points in the middle.
In the recurrence below, $$i$$ represents the number of symbols in the last contiguous block of equal letters, and $$x'$$ or $$z'$$ represents the number of letters that remain available with values earlier in the alphabetic order than the one that was used for this block. The recurrence is:

$$
S_z^x(y) = \sum_{i=1}^y \left(
\sum_{x'=0}^{x-1} S_z^{x'}(y-i) +
\sum_{z'=0}^{z-1} S_{z'}^{z}(y-i) \right),
$$

with base case $$S_z^x(0)=1$$. Then the total number of polygonalizations can be found by splitting up the overall length $$n-2$$ of the string into substrings of left, top or bottom, and right symbols, using this recurrence to count the number of ways of filling in the middle part, multiplying by two for each nonempty left or right part (because there is a choice of upper or lower case for each of these parts), and summing over all splits. [My code to do this]({{site.baseurl}}/assets/2020/gridcycles.py) tells me that the sequence of numbers of polygonalizations for $$3\times n$$ grids, for $$n=2,3,4,\dots$$, is

$$1, 8, 62, 532, 4846, 45712, 441458, 4337468, 43187630, \dots$$

(not yet in OEIS but I will submit it).

The next question is: how quickly does this sequence grow? It's singly exponential (because that's true of all 2d non-crossing geometric graph counting problems) but what is the base of the exponential? We can make a rough estimate by ignoring faxtors that are polynomial or smaller. The first estimate I tried was wrong: it was that there are roughly $$2^n$$ ways of choosing whether each letter is upper or lower case, most of which assign roughly half of the letters to each case, and roughly $$(3\sqrt{3}/2)^n$$ ways of choosing an upper or lower case substring of length $$n/2$$, for a total of $$13.5^n$$ choices. But this is an overestimate, because it doesn't take into account the requirement that each letter be contiguous. It would allow strings like $$aBa$$ which don't correspond to polygonalizations, and that turns out to matter in the estimation.

To get a better estimate, we need to break down how we choose a string in a different way:

* First, choose how many of the lower case letters are actually used, and then which subset of them is used.
* Second, do the same thing with the upper case letters.
* Finally, repeat $$n-2$$ times choosing for each letter of the string whether it repeats the previous letter, takes the next lower case letter from the chosen subset, or takes the next upper case letter from the chosen subset, making sure that the first choice is not a repeat and that the total number of next-letter choices matches the number of different letters to choose from.

There are polynomially many choices for how many letters of each type to use,
so the total number of choices is within a polynomial factor of the number of choices after we fix these numbers of letters to a single value, the one that maximizes the number of remaining choices. And we can estimate the number of remaining choices using Stirling's approximation. Estimating the number of polygonalizations in this way shows that it is within a polynomial factor of $$q^n$$, where

$$
q=\max_{0 < p < 1/2}\left(
p^{-4p} (1-p)^{-2(1-p)} (1-2p)^{-(1-2p)}
\right)
$$

and where the number of letters we use from each case is $$pn$$. Here, some magic happens: It doesn't look like $$p$$ and $$q$$ should have nice simple formulas, but they do. With $$\varphi=\tfrac{1+\sqrt{5}}{2}$$ (the golden ratio), we get a maximum at $$p=2-\varphi$$, for which $$q=\varphi^5$$. So our sequence is approximately asymptotic to $$\varphi^{5n}$$.

Probably if you go through the same estimation process more carefully, you can recover the polynomial factor as well. I wasn't so careful; instead I just computed how far off from $$\varphi^{5n}$$ the numbers in my sequence are, fit a line to these factors on a log-log scale, and observed that its exponent was approximately 1. So, the polynomial factor is $$n$$, and numerically the sequence of numbers of polygonalizations above is a very good fit to

$$\frac{\varphi^{5n}}{66n}.$$

Why the golden ratio? I don't know.