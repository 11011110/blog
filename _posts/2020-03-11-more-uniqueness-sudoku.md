---
layout: post
title: More on uniqueness in Sudoku
date: 2020-03-11 00:06
---
[My first post on this blog]({{site.baseurl}}{% post_url 2005-07-20-updated-python-library %}), lo these nearly 15 years ago, discussed a program I had written to try to solve Sudoku puzzles deductively (rather than by the easier computational method, backtracking), with the goal of being able to automatically grade the puzzles and automatically generate explanations for how to solve a given puzzle. And a few months later I posted again, on [deduction rules that take advantage of the assumption that a puzzle has a unique solution]({{site.baseurl}}{% post_url 2005-10-15-assuming-uniqueness-in %}), by ruling out choices that would cause any solution consistent with them to become non-unique. Since then, that part of my solver has been relatively stable, although I have added other rules for [Nishio]({{site.baseurl}}{% post_url 2012-02-23-solving-single-digit-sudoku %}) and [2SAT]({{site.baseurl}}{% post_url 2009-04-26-sudoku-and-2sat %}) and posted here about [more general uniqueness deduction rules in map-coloring puzzles]({{site.baseurl}}{% post_url 2019-07-28-any-order-puzzle %}).

I've also occasionally been using my program to generate puzzles for me to work on, and today it found an interesting test case, a puzzle that it thought would be much more difficult than it turned out to be for me. This mis-rating happened because the uniqueness deduction rules I'm using in my own deductions are stronger than the ones in my program (although some of its other rules are stronger than I typically apply myself). In its initial state, the puzzle looks like:

{: style="text-align:center"}
![Sudoku puzzle]({{site.baseurl}}/assets/2020/ambig-sudoku-givens.svg)

My program tells me that it's at the second highest level of difficulty that it knows about: it has to resort to using 2SAT, but it can successfully solve it that way. (The highest level is for puzzles where it is forced to use backtracking.) Usually, for me, puzzles at that level require me to use written notes to keep track of the deductions, rather than doing it all in my head, but not this time. Using more-or-less standard reasoning, one can fill in the cells of the puzzle to reach the state:

{: style="text-align:center"}
![Partially solved Sudoku puzzle]({{site.baseurl}}/assets/2020/ambig-sudoku-partial.svg)

This is where my program gets stuck and has to resort to more powerful deduction rules. But as a human solving this puzzle, here is what I see: In row 3, the two empty cells must contain the pair of digits 3 and 5. In the center right block of nine cells, the two empty cells must again be 3 and 5. And in the center block of cells, the 5 digit is confined to three cells aligned with those two pairs of empty cells. If the 3 digit were also confined to the same three cells in the center block, it and the five would have to occupy the two diagonally aligned cells out of the three, because otherwise they would line up and prevent one of the other pairs of 3-5 cells from having any value. But then the 3-5 cells in row 3, the center block, and column 7 would form a closed system (shown by the red squares below): nothing else outside those cells could affect which of those six cells contains 3, and which contains 5. Within that closed system, there are two solutions, obtained from each other by swapping the locations of the 3 and the 5. But that would violate the assumption of uniqueness.

{: style="text-align:center"}
![Closed system of cells in a partially solved Sudoku puzzle]({{site.baseurl}}/assets/2020/ambig-sudoku-closed.svg)

Even if the 7 in the center cell weren't there, the same reasoning would apply. Since this closed system with a non-unique solution would happen automatically if we confine the digit 3 to the same three center-block cells as the digit 5, the digit 3 must be elsewhere in the center block, which can only mean that it is in column 4. Once we make this deduction, the rest of the puzzle falls into place.

My program only has built into it a couple of ad-hoc rules to prevent closed systems of four cells with two solutions, and it misses the one in this example because it involves six cells. It's making me think that I need a more general description of the possible closed systems (at least the ones involving only two digit values, like this), in order to match the deductions I'm making by hand and make my program's difficulty estimates more accurate.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/103803219892010865))