---
layout: post
title: One-face torus
date: 2024-03-28 10:00
---
In the graduate version of my just-concluded graph algorithms course, one of the exam questions asked the students to find the faces of a topological embedding of the complete bipartite graph $$K_{2,3}$$ (the embedding in which the two degree-three vertices have the same clockwise order of neighbors as each other), compute its Euler characteristic, and determine from the result whether the embedding is planar. Some of the students found it confusing (it was intended to be the hardest problem on the exam) so I thought I'd post an answer here.

It turns out that there is a single 12-sided face. I think it's easier to draw a picture than to describe in text. Below, the two white vertices are the degree-three vertices of $$K_{2,3}$$, and the colors indicate the other three vertices. When a vertex appears multiple times on the boundary of a surface, that means those copies are glued together to form a single vertex in the embedding. The upper left shows a standard form of the torus in which the top and bottom edges of a square sheet of paper are curled around and glued to each other to form a paper tube, and then the left and right edges are glued to form a torus. On the right, it's cut into pieces and reassembled into a rectangle, which is however _not_ glued edge-to-edge in the same way. You have to roll it with a twist so that the colors match up when you glue it.

{: style="text-align:center"}
![One-face embedding of the complete bipartite graph K_{2,3} on a torus]({{site.baseurl}}/assets/2024/K23-torus.svg)

You could also stretch the bottom left shape into a regular hexagon, with the white vertices at its corners and the colored vertices in the middle of each side. Then you would glue it opposite edge to opposite edge to form a torus, just like the starting square. But somehow gluing opposite edges of a hexagon to make a torus seems much less intuitive to me than gluing opposite edges of a square.

You can read off the clockwise ordering from the upper right: each white vertex is surrounded by three neighbors in the clockwise order blue, green, red. The 12-vertex face cycle that the students were supposed to find is what you see on the lower right. Because there are five vertices, six edges, and one face, the Euler characteristic is $$5-6+1=0$$. This is not $$2$$, so the surface is non-planar. (It's a torus, but I didn't require the students to say that.)