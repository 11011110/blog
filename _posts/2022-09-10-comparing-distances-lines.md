---
layout: post
title: Comparing distances along lines
date: 2022-09-10 17:26
---
I've written here several times about [Gilbert tessellations](https://en.wikipedia.org/wiki/Gilbert_tessellation), most recently in [last year's post about cellular automata that naturally generate them]({{site.baseurl}}{% post_url 2021-11-02-gilbert-tessellations-cellular %}). These are polygonal subdivisions of the plane, generated from the tracks of particles moving at the same speed, where the particles start as oppositely-moving pairs with random locations and directions, and continue moving until they crash into the track of another particle. Here's Wikipedia's illustration of these things, generated in 2012 by Claudio Rocchini:

{: style="text-align:center"}
[![A Gilbert tessellation, by Claudio Rocchini]({{site.baseurl}}/assets/2018/Gilbert-tessellation.svg)](https://commons.wikimedia.org/wiki/File:Gilbert_tessellation.svg)

Suppose someone gives you a picture like this and tells you it's a Gilbert tessellation, like I just did. How can you tell that it's genuine? The starting positions of the particles are not marked on the picture, so what needs to be done is to infer their locations (or a system of points that could be their locations) and to check that particles, starting at those locations and moving along the lines, crash in the order that the picture shows. Wherever two segments intersect in the picture, one of them ends, and it must be the case that the starting position on the segment that ends is farther away than the starting position on the other segment. Otherwise, it would have been the other particle that crashed and the other segment that ended.

One can set up a big system of inequalities where each variable describes the starting position of one of the particles, for instance by giving its distance from one end of its segment. Each inequality comes from an intersection of two segments and asks for the particle on one segment to be farther than the particle on the other segment. The distance between two positions $$x$$ and $$y$$ on the same segment, parameterized linearly, is <span style="white-space:nowrap">just $$\vert x-y\vert$$.</span> So when a particle on <span style="white-space:nowrap">line $$j$$</span> crashes into a track on <span style="white-space:nowrap">line $$i$$</span> we get an inequality like

$$\vert x_i-e_{ij}\vert\le \vert x_j-e_{ji}\vert,$$

where $$x_i$$ is the starting positions of the particle on <span style="white-space:nowrap">line $$i$$,</span> $$e_i$$ is the known position on <span style="white-space:nowrap">line $$i$$</span> of its intersection with <span style="white-space:nowrap">line $$j$$,</span> $$\vert x_i-e_{ij}\vert$$ is the distance from the starting position to the intersection, and the smaller distance for the particle on <span style="white-space:nowrap">line $$i$$</span> means that it gets to the intersection first, causing the other particle to crash into its track. We also have some inequalities specifying that each starting position lies between the endpoints of its line segment. This almost looks like a linear program (or rather a linear programming feasability problem, with only linear constraints but no objective function), but the absolute values make it nonlinear. We can get rid of them by two tricks:

* Because the left absolute value occurs on the left hand side of a <span style="white-space:nowrap">$$\le$$ constraint,</span> it is equivalent to replace it by two constraints, one for each choice of sign:

  $$x_i-e_{ij}\le \vert x_j-e_{ji}\vert,$$

  and

  $$e_{ij}-x_i\le \vert x_j-e_{ji}\vert.$$

* Because <span style="white-space:nowrap">line $$j$$</span> ends at its intersection with <span style="white-space:nowrap">line $$i$$,</span> we know on which side of the intersection to find the starting <span style="white-space:nowrap">point $$x_j$$,</span> and therefore, we know the sign <span style="white-space:nowrap">of $$x_j-e_{ji}$$.</span> We can use this knowledge to replace $$\vert x_j-e_{ji}\vert$$ by either $$x_j-e_{ji}$$ or $$e_{ji}-x_j$$ (whichever of these two expressions is guaranteed to be non-negative), eliminating the right absolute value.

Once these replacements have been made, we have a linear program with two variables per inequality, which can be solved in (strongly) polynomial time.

But all this made me wonder: can we always turn a system of inequaties between linear distances like this into a linear program? Suppose we have an arbitrary system of variables $$x_i$$ and an arbitrary system of <span style="white-space:nowrap">inequalities $$\vert x_i-e_{ij}\vert\le \vert x_j-e_{ji}\vert$$,</span> not coming from Gilbert tessellation recognition. Can we determine whether such a system has a solution, efficiently? Can we maybe turn any system of inequalities like this into a linear program, and solve it that way?

No! The problem is <span style="white-space:nowrap">$$\mathsf{NP}$$-complete.</span> The illustration below shows the key gadget, a system of six inequalities for two variables (each shown with a small blue double wedge in the plane pointing towards the points that obey the inequality). These inequalities have only the three red points shown as their solutions. You might want only one inequality per pair of variables, but in that case you can get the same effect by replacing each inequality by a pair of inequalities involving an additional dummy variable. The <span style="white-space:nowrap">$$\mathsf{NP}$$-completeness</span> proof is a reduction from graph 3-coloring that translates each vertex into one of these gadgets, and represents the color of a vertex by the choice of which red point is used to solve these inequalities. I haven't shown the edge gadgets, but it's easy to find more inequalities to use for a pair of vertices, to force them to have different red points as their solutions. For instance, the <span style="white-space:nowrap">inequality $$\vert x_i\vert\ge\vert y_j-1\vert$$</span> fails only for two vertices that both use the same red point $$(0,0)$$.

{: style="text-align:center"}
![Vertex gadget for reduction from 3-coloring to linear distance comparison, consisting of six inequalities abs(x) ≤ abs(y-4), abs(x+2) ≥ abs(y-2), abs(x-2) ≥ abs(y-2), abs(x+1) ≥ abs(y+1), abs(x-1) ≥ abs(y+1), and abs(x) ≤ abs(y+2), that force the two variables (x,y) to have one of the three combinations of values (3,1), (-3,1), or (0,0)]({{site.baseurl}}/assets/2022/vertex-gadget.svg)

So somehow, the geometry of Gilbert tessellations is essential for the ability to convert their recognition problem into a linear program, and solve it efficiently.