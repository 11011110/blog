---
layout: post
title: Small hyperbolic tiles
date: 2018-02-03 19:26
---
This is the [binary tiling](https://en.wikipedia.org/wiki/Binary_tiling), a tiling of the hyperbolic plane by congruent convex pentagons. (It's usually shown more like a quadtree, like the top image of the Wikipedia article, but the tiles in that version aren't convex and aren't polygons.) We now have a [complete classification of convex pentagons that tile the Euclidean plane](https://www.quantamagazine.org/pentagon-tiling-proof-solves-century-old-math-problem-20170711/), but as this example shows the hyperbolic case is more complicated.

{: style="text-align:center"}
![Binary tiling]({{site.baseurl}}/assets/2018/binary-tiling.svg)

The article on Wikipedia is quite new, added after another editor saw Ian Agol's nice answer to [a MathOverflow question asking for the smallest monohedral tile on the hyperbolic plane](https://mathoverflow.net/q/291452/440). Agol used the binary tiling to show the area can be made arbitrarily small (essentially, you can make the horizontal dimension of the tiles in this image arbitrarily small without much changing the vertical dimension nor the overall pattern of the tiling), and Douglas Zare added that, by making tiles with $$k$$ arcs on the top and $$k+1$$ on the bottom, you can also make the diameter arbitrarily small. The ones in the image above are drawn fairly wide, in the Poincaré halfplane model of the hyperbolic plane, in order to make their angles 60–120–60–120–120; the thinner ones have messier angles.

It turns out that these tilings have been known for quite a while, at least since a [1974 paper of Böröczky](http://real-j.mtak.hu/9373/) (but beware, the download is a huge pdf and the paper is in Hungarian). The tiling is less symmetric than it looks, as can be seen by encoding each tile's situation in the tiling by a binary sequence that describes whether the tiles directly above it extend left or right. There are countably many tiles in a tiling, but uncountably many sequences, so (like the Penrose tiles) there are actually infinitely many different tilings with the same tiles. Two tiles map to each other by a symmetry of their tiling when they have the same sequence, and belong to the same tiling when their sequences differ by a finite shift and a change of finitely many bits. The repeating sequences (the ones corresponding to binary representations of rational numbers) come from tilings with an infinite cyclic group of symmetries (but with unbounded fundamental domains) while the irrational numbers give completely aperiodic tilings.

Here are two related questions I don't know the answer to:

1. How can you draw the tiles of this tiling using only a compass and straightedge within the hyperbolic plane? Using the Euclidean model as in this image rather than staying within hyperbolic geometry is cheating. (What I actually want to know is how to draw it in [Cinderella](https://www.cinderella.de/tiki-index.php).)

2. Do there exist arbitrarily-small-diameter monohedral tiles on the sphere? (There do exist arbitrarily-small-area tiles, as the MathOverflow question already noted.)

([G+](https://plus.google.com/100003628603413742554/posts/QKj17nSEsZV))