---
layout: post
title: Triforce toroids
date: 2024-03-16 15:00
---
Recent edits to the Wikipedia article on [toroidal polyhedra](https://en.wikipedia.org/wiki/Toroidal_polyhedron) led me to [a 1997 geometry.research discussion thread, "Polyhedra of positive genus"](https://groups.google.com/g/geometry.research/c/4gvG8ZieFuE/m/JMUg64WIF3AJ?pli=1), in which John Conway describes a toroidal polyhedron with 36 equilateral-triangle sides, and suggests that this might be the fewest sides possible for a toroidal [deltahedron](https://en.wikipedia.org/wiki/Deltahedron).

Conway's description is clear enough: start with a central regular octahedron (eventually to become the hole in the torus). Find a cycle of six triangles separating two opposite faces of the central octahedron, and glue three octahedra and three tetrahedra in alternation around these faces. Fill in the six gaps between these glued-on polyhedra with six more tetrahedra, and remove the central octahedron. Following these instructions, I made one for myself with snap-together plastic triangles:

<div><table style="margin-left:auto;margin-right:auto">
<tr style="text-align:center;vertical-align:middle">
<td style="padding:10px"><img
src="https://www.ics.uci.edu/~eppstein/pix/triforce/1-m.jpg" style="border-style:solid;border-color:black;"
alt="Conway's triforce toroid, bumpy side of hole"></td>
<td style="padding:10px"><img
src="https://www.ics.uci.edu/~eppstein/pix/triforce/2-m.jpg" style="border-style:solid;border-color:black;"
alt="Conway's triforce toroid, triforce side of hole"></td></tr>
<tr style="text-align:center;vertical-align:middle">
<td style="padding:10px"><img
src="https://www.ics.uci.edu/~eppstein/pix/triforce/3-m.jpg" style="border-style:solid;border-color:black;"
alt="Conway's triforce toroid, tetrahedral edge-on view, bumpy side up"></td>
<td style="padding:10px"><img
src="https://www.ics.uci.edu/~eppstein/pix/triforce/4-m.jpg" style="border-style:solid;border-color:black;"
alt="Conway's triforce toroid, octahedral edge-on view, triforce side up"></td></tr></table></div>

The upper left view looks down the hole, from the side where the three octahedra glued onto the hole appear most prominently, looking like three square pyramids tilted slightly away from the central hole. On the upper right, we see the hole from the other side. The three triangular faces closest to the central hole in this view lie flat in the plane, in the shape of the [Triforce](https://en.wikipedia.org/wiki/Triforce) from the Zelda games. Extending beyond them, we see three sets of three coplanar triangles. The other two views are edge-on, near a tetrahedron and octahedron (respectively) glued onto the central octahedral hole.

You might see the existence of coplanar triangles, or of coplanar adjacent triangles, as a flaw in this shape. Bonnie Stewart's book [_Adventures Among the Toroids_](https://en.wikipedia.org/wiki/Adventures_Among_the_Toroids) does: it defines a polyhedron as being "aplanar" when no two adjacent faces share a plane. On p.60 of my copy (the 1980 2nd edition), Stewart describes a toroid very similar to Conway's, but with extra tetrahedral bumps attached to make it planar. However, it still has the three coplanar triforce triangles. These are allowed by Stewart's definitions, because they are not adjacent to each other.

These polyhedra have different numbers of triangles meeting at their vertices: sometimes more than six, sometimes less than six. As far as I know a question I posted about in 2009 using the same snap-together triangles, [whether there exists a toroidal deltahedron with six triangles per vertex]({{site.baseurl}}{% post_url 2009-02-03-flat-equilateral-tori %}), remains open, as does Conway's question about whether his polyhedron has the fewest sides of any toroid with equilateral triangle sides.