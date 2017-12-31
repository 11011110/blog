---
layout: post
title: Folding polyominoes into (poly)cubes
date: 2017-12-30 21:06
---
Here's a trio of paper puzzles for you to print out, cut out, and fold. The goal is to fold each of these three shapes so that it covers the entire surface of a cube, whose sides are the same size as the squares in each shape. The uncolored areas in two of the shape and the thick black line in the third are holes that you should cut out from the middle of each shape before folding. They come from [a blog post by Nikolai Beluhov](https://nbpuzzles.wordpress.com/2014/06/08/cube-folding/), which also has a trickier variation of the top one in which illustrations printed onto certain squares of the shape should become visible once you fold it into a cube.

{: style="text-align:center"}
![Three polyominoes to be folded into cubes]({{site.baseurl}}/assets/2017/Beluhov-folding-puzzles.svg)

These puzzles were the starting point for my latest preprint, "Folding polyominoes into (poly)cubes" ([arXiv:1712.09317](https://arxiv.org/abs/1712.09317), with Aichholzer, Biro, Demaine, Demaine, Fekete, Hesterberg, Kostitsyna, and Schmidt).
We published it in CCCG 2015, but I don't seem to have posted about it at that time. The preprint is of the extended journal version. One complication with studying the problem mathematically (rather than just posting it as a puzzle) is that we have to specify more carefully what we mean by folding a polyomino to form the surface of a cube or polycube, rather than just letting the puzzler figure out which kinds of folds are needed to make the puzzle work. We ended up defining nine different models of what kinds of folds are allowed and (with a lot of case analysis) showing them all to be different from each other in terms of which shapes they allow to fold to cubes.

The corresponding algorithmic problems turn out to be a bit messy. We developed a dynamic programming algorithm for folding tree-like polyominoes to cover the surface of constant-sized polycubes in the simplest of our folding models, but weren't able to handle more complicated folding models, primarily because it wasn't clear how to extend an abstract mapping from the polyomino to the cube surface into a valid 3d embedding. The difficulties here are somewhat related to the [map folding problem](https://en.wikipedia.org/wiki/Map_folding), where it is unknown even how to determine whether a square grid with a fixed assignment of mountain or valley to its folds can be folded flat.

([G+](https://plus.google.com/100003628603413742554/posts/WhxN1Nb4kkg))