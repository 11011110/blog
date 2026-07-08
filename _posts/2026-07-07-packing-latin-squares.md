---
layout: post
title: Packing Latin squares into sudoku puzzles
date: 2026-07-07 18:17
---
I have another new preprint, the result of a research project with UC Irvine undergraduate Cindy Zhang: "[Sudoku grids that require many clues](https://ics.uci.edu/~eppstein/pubs/p-manyclues.html)" ([arXiv:2607.05728](https://arxiv.org/abs/2607.05728), to appear at [JCDCG<sup>3</sup> 2026](https://sites.google.com/view/jcdcggg2026)). The main result is, I think, surprising: When generalized to $$n^2\times n^2$$ grids, almost all sudoku puzzles must be almost entirely covered by clues, leaving only a logarithmic fraction of cells blank. This implies an average case time for solving randomly chosen puzzles that is exponential in $$n^4/\log n$$, significantly better than the exponential in $$n^4$$ that one gets for formulating the problem as an [exact cover problem](https://en.wikipedia.org/wiki/Exact_cover) without using this bound on blank cells or the exponential in $$n^4\log n$$ that one gets for a brute force search.

The formatting requirements for JCDCG<sup>3</sup> are in one way quite free-form and in another way very strict: each submission can have only two a4 pages, and the font must be at least 10pt in size, but otherwise you can do what you want. I took advantage of this freedom to experiment with the LaTeX "Cochineal" font (`\usepackage[cochineal]{newtx}` in LuaLaTeX or XeLaTeX), not so much because it is more compact than Computer Modern (although it is), but because I was tired of the bulbous artificial-looking letterforms of Computer Modern and wanted an old-style font that reminded me more of the appearance of handwritten manuscripts. But even with a more compact font, and a two-column format, the paper is necessarily quite telegraphic and didn't have room for illustrations. So I thought this posting would be a good place to illustrate a construction from the paper for packing $$n^2$$ disjoint Latin squares into an $$n^2\times n^2$$ sudoku puzzle. This is not needed for the main result, but helpful for small $$n$$. With this construction we find a large family of $$9\times 9$$ sudoku puzzle solutions that, regardless of how you specify clues with those solutions, require 18 clues (more than the minimum 17 clues for some sudoku puzzles), and $$16\times 16$$ sudoku puzzle solutions that require 80 clues (well more than the conjectured minimum 56 clues for some puzzles).

As a reminder, an $$n\times n$$ Latin square fills its $$n^2$$ cells with the numbers from $$1$$ to $$n$$ (or any $$n$$ distinct things) in such a way that each row and each column has one copy of each of these numbers, almost the same as sudoku but without the number of distinct values being square and without the additional requirement that square blocks of cells contain distinct values. Our construction finds sudoku puzzles of size $$n^2\times n^2$$ (for an arbitrary choice of $$n$$) within which one can pick out $$n^2$$ smaller non-overlapping $$n\times n$$ Latin squares of cells. One can then argue that each of these smaller Latin squares needs enough clues, just in its own subset of cells, to specify it unambiguously, forcing the larger sudoku puzzle to require $$n^2$$ times as many clues.

The construction begins by coloring the $$n^2$$ digits of the sudoku puzzle so that there are $$n$$ digits of each color. Each of the $$n\times n$$ Latin squares packed into the puzzle will use digits of a single color. Within each $$n\times n$$ block of the sudoku puzzle, each row of the block will use digits of a single color.

{: style="text-align:center"}
![Assignment of n colors to n^2 digits so that each color is assigned n digits]({{site.baseurl}}/assets/2026/sudoku-digits.svg)

Next, group the $$n\times n$$ blocks of the sudoku puzzle into rows of blocks
($$n$$ contiguous rows of cells of the puzzle). For each row of blocks, choose an $$n\times n$$ Latin square whose $$n$$ values are our colors, and use this Latin square to assign colors to the rows of cells within each $$n\times n$$ block.

{: style="text-align:center"}
![Assignment of colors to the rows of each 3x3 block of a sudoku puzzle]({{site.baseurl}}/assets/2026/sudoku-distrib.svg)

Finally, group the $$n\times n$$ blocks of the sudoku puzzle into columns of blocks
($$n$$ contiguous rows of cells of the puzzle). Within each column of blocks, each color is assigned to an $$n\times n$$ (non-contiguous) subarray of puzzle cells. Choose a Latin square whose values are the digits of that color. The illustration shows what this looks like for a single subarray, the yellow one in the rightmost column of blocks.

{: style="text-align:center"}
![Packing a Latin square into a sudoku puzzle]({{site.baseurl}}/assets/2026/sudoku-latin.svg)

Repeat for each color in each column of blocks, and you have a solved sudoku puzzle packed with $$n^2$$ Latin squares, just waiting for you to select which of its cells will be revealed as clues and which will be left blank for the puzzle solver to deduce.

{: style="text-align:center"}
![Solved sudoku puzzle packed with nine 3x3 Latin squares]({{site.baseurl}}/assets/2026/sudoku-packed.svg)

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/116881760189593176))