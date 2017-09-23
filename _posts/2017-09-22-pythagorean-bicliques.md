---
layout: post
title: Pythagorean bicliques
date: 2017-09-22 22:10
---
How many points on two perpendicular lines can all be at integer distances from each other? For instance, in the following drawing, we have five points on each line, all at integer distances.

{: style="text-align:center"}
![Pythagorean biclique formed by the nine points (0,0), (0,±20), (0,±36), (±15,0), (±48,0), and some of the integer distances between these points]({{site.baseurl}}/assets/2017/pythagorean-biclique.svg)

The answer is: a lot more. In their paper "Two triads of squares" ([_Math. Comp._ 1986](http://www.ams.org/journals/mcom/1986-46-174/S0025-5718-1986-0829644-0/)), J. Lagrange and J. Leech find two point sets like this with seven points on one line and nine on the other. They're harder to draw accurately, but the coordinates of the points in one of these sets are $$(0,0),$$ $$(0,\pm 9282000),$$ $$(0,\pm 60386040),$$ $$(0,\pm 2682260),$$ $$(\pm 22276800,0),$$ $$(\pm 7422030,0),$$ $$(\pm 8947575,0),$$ and $$(\pm 4414233,0).$$ The other one has coordinates of similar magnitude.
Lagrange and Leech also describe a construction for sets of five points on one line and infinitely many on the other, based on elliptic curves, which they credit to an earlier paper, "Elliptic curves and rational distance sets" ([_Proc. AMS_ 1954](http://www.ams.org/journals/proc/1954-005-01/S0002-9939-1954-0060262-1/)), by W. D. Peeples.

I was led to these papers by some computational experiments I ran today. One can define a graph $$G,$$ whose vertices are integers and whose edges connect pairs of integers that form the legs of a Pythagorean triangle. Of course it's infinite, but it's easy to use the formula for Pythagorean triangles to generate large subgraphs of it. In graph-theoretic terms, point sets such as the ones above correspond to bicliques (complete bipartite subgraphs) of $$G.$$ The vertices on one side of the biclique are used for the coordinates of the points on one line, and the vertices on the other side of the biclique are used for the points on the other line. For instance, the biclique corresponding to the drawing above is a copy of $$K_{2,2},$$ with $$15$$ and $$48$$ on one side, and $$20$$ and $$36$$ on the other.

As $$G$$ is somewhat sparse, I realized that it should be possible to find these bicliques by an algorithm I published some years ago for finding bicliques in sparse graphs ("Arboricity and bipartite subgraph listing algorithms", [_Inf. Proc. Lett._ 1994](http://doi.org/10.1016/0020-0190(94)90121-X)).
My new implementation of the biclique-finding algorithm is now in my Python library [PADS](http://www.ics.uci.edu/~eppstein/PADS/) as [Bicliques.py](http://www.ics.uci.edu/~eppstein/PADS/Bicliques.py). (Probably there's still some more optimization possible; I wanted to get it run correctly first, before working on making it fast.) With it, I found several seven-by-seven integer-distance sets of points on two lines, although none as big as the seven-by-nine ones of Lagrange and Leech. (Maybe those would have been reachable with a longer search...) And by searching the web for the numbers in one of those sets, I found the paper of Lagrange and Leech.

It appears to be open how big these sets can be. I didn't find any improvements to Lagrange and Leech among the later papers that cite them (of which there are not many). What I would like to be true is that for every $$n$$ one can find sets that have at least $$n$$ points on each line, but maybe that's too optimistic, and I have no good reason to believe it's true.

([G+](https://plus.google.com/100003628603413742554/posts/6yT2rQuvnBR))