---
layout: post
title: 2-adic numbering for binary tilings
date: 2024-10-28 19:41
---
I've posted quite a bit about the binary tiling of the hyperbolic plane recently, including
[what you get when you shrink its vertical edges]({{site.baseurl}}{% post_url 2023-04-16-fractal-arbelos %}),
a related ["nowhere-neat" tessellation]({{site.baseurl}}{% post_url 2023-10-15-linkage %}),
the [connection to Smith charts and Escher]({{site.baseurl}}{% post_url 2023-11-30-linkage %}),
a [method to 3-color its tiles]({{site.baseurl}}{% post_url 2024-09-30-linkage-start-another %}),
a [half-flipped variation of the tiling]({{site.baseurl}}{% post_url 2024-10-06-half-flipped-binary %}),
and [its applications in proving that folding origami is hard]({{site.baseurl}}{% post_url 2024-10-10-computational-complexities-folding %}). But I thought there might be room for one more post, in honor of the [Wikipedia binary tiling article's](https://en.wikipedia.org/wiki/Binary_tiling) new Good Article Status. This one is about something I wanted to include in the Wikipedia article, but couldn't, because I couldn't find published sources describing it: a way of numbering tiles that encodes their position in a tiling and instantly proves the assertion in the article that there are uncountably many binary tilings.

The basic idea is very simple: in the binary tiling (in its conventional view as a pattern of similar squares or rectangles in the Poincaré half-plane), if you look directly upward from any tile, some of the tiles above it will extend farther to the left, and some of them will extend farther to the right. We will encode this by a binary sequence, where a 1 encodes a tile that extends to the left, and a 0 encodes a tile that extends to the right. (This seems backwards, but there's a reason for this choice that will become clear soon.) To make it backwards in a different way, I want to write this sequence in right-to-left order, so that for instance the encoding ...1100 means that the closest two tiles above it extend to the right, and the next two extend to the left. Here's a picture with some examples. The label in each square only encodes the tiles that you can see in the picture, but the tiling itself can continue above these squares in multiple different ways, resulting in different continuations of these labels.

{: style="text-align:center"}
![Numbering the tiles of a binary tiling]({{site.baseurl}}/assets/2024/2-adic-numbering-binary.svg){: style="width:100%;max-width:720px" }

If you read the binary sequences in a single row, left-to-right, they should look familiar: they're just the binary encodings of the non-negative integers 0, 1, 2, 3, ... in order. That's why I chose the backwards order of binary digits and backwards choice of what 0 and 1 mean: with the digits in the other order we would get the [bit-reversal permutation](https://en.wikipedia.org/wiki/Bit-reversal_permutation) of these numbers and with the other choice of what 0 and 1 mean they would count down rather than counting up.

The binary representation of an ordinary integer eventually terminates, with all higher-order binary digits equal to zero for a non-negative integer (or equal to one for a [two's-complement](https://en.wikipedia.org/wiki/Two%27s_complement) negative integer). But the binary sequences coming from a binary tiling might not terminate in this way. Any binary sequence is possible, and uniquely determines the entire tiling surrounding a tile with that sequence as its label. To find the tiling from a binary sequence, just place tiles directly above the labeled tile, as the sequence dictates, and then fill in everything else below them in the only way possible. There are uncountably many binary sequences (for instance, each two real numbers in the unit interval have different binary expansions), but only countably many of them can show up as the labels in a single binary tiling. For this reason we know that there are uncountably many different binary tilings.

But because we're ordering the binary sequences right-to-left, they're not the binary expansions of real numbers. And because they aren't eventually zero, they're not the binary expansions of ordinary integers. Instead, they're the binary expansions of a more exotic number system, the [2-adic integers](https://en.wikipedia.org/wiki/P-adic_number). You can think of the arithmetic of these numbers as just like ordinary binary arithmetic except that it continues infinitely to the left, in the same way that ordinary binary arithmetic on real numbers continues infinitely to the right.

The 2-adic integers contain the ordinary integers (sometimes called in this context rational integers) but they also contain any rational number whose denominator is odd. These can be recognized as the 2-adic numbers whose binary expansion is eventually repeating. More precisely, when a 2-adic number has a repeating pattern of length $$i$$ that repeats the binary expansion of the integer $$n$$, it can be thought of as equal to the rational number $$-n/(2^i-1)$$. As an example that is eventually repeating but not purely repeating, the rational number $$\tfrac13$$ is a 2-adic integer with a binary expansion ...0101011 that, after the rightmost 1, repeats with a period-2 pattern. (Try multiplying it by 3 in binary and watch all the nonzero bits get carried away!)

We can encode many convenient properties of the tiling in properties of these numbers:

* Two tiles of the same tiling have a non-reflective symmetry of the tiling that takes one to the other, if and only if they are labeled by the same 2-adic integer.

* The image of a tile labeled $$x$$, in the reflection of the tiling, has the label $$-x-1$$, the 2-adic integer with all bits flipped.

* The left neighbor of a tile labeled $$x$$ is labeled $$x-1$$, and the right neighbor is labeled $$x+1$$. The two neighbors below a tile labeled $$x$$ are labeled $$2x$$ and $$2x+1$$.

* Each 2-adic integer is either odd or even (according to its last binary digit, just like ordinary integers). If a tile is labeled by an even number $$x$$, it is on the left side of the tile above it, which is labeled $$x/2$$. If a tile is labeled by an odd number $$y$$, it is on the right side of the tile above it, which is labeled $$(x-1)/2$$.

* Two labels $$x$$ and $$y$$ appear together in the same tiling if and only if one of the two labels can be obtained from the other by multiplying by a power of two and then adding a rational integer. This is true if and only if their binary sequences are eventually equal (after removing finite prefixes of possibly different lengths), with one exception: negative and positive rational integer labels do belong to the same tiling, but have binary sequences that are eventually all zero or eventually all one.

* A tiling has a one-dimensional group of symmetries, obtained by scaling the Poincaré half-plane drawing by a factor of $$2^i$$, if and only if its labels are rational numbers whose binary expansions have period $$i$$. For instance the unique tiling for which scaling by 2 is a symmetry is the one where all the labels are rational integers.

Based on this labeling, we can count the number of distinct tilings (counting reflections as distinct) for which scaling by $$2^i$$ is a symmetry: they are the number of distinct binary sequences of length $$i$$, up to rotations, minus one. The minus one is because of the rational integer labels. For instance, there are two tilings for which multiplication by four ($$i=2$$) is a symmetry, with repeating patterns 00 = 11 (the rational integers) and 01 = 10 (integers $$\pm\tfrac13$$), which is its own mirror reflection. There are three tilings for which multiplication by eight is a symmetry: the rational integers again, and two mirror-image tilings with repeating patterns 001 and 011.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/113388018892402836))