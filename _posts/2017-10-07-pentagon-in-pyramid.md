---
layout: post
title: The pentagon in the pyramid
date: 2017-10-07 17:10
---
Sliced okra has a pentagonal cross-section:

{: style="text-align:center"}
![Pentagonal slices of okra]({{site.baseurl}}/assets/2017/pentagon-in-pyramid/okra.jpg 'CC-BY-SA image Okra sliced.JPG by Yes.aravind from Wikimedia commons')

But did you know that you can also get a regular-pentagon slice from a square pyramid? Here it is in top view. The yellow color shows the interior of the pyramid after slicing it, while the blue is the original pyramid surface. (For years, in my office, I've had a print by Wulf Barsch showing the pyramids of Egypt, lit blue by the night.)

{: style="text-align:center"}
![Pyramid sliced with a regular pentagon cross-section, top view]({{site.baseurl}}/assets/2017/pentagon-in-pyramid/sliced-pyramid.svg)

You probably already did know that a cube or regular octahedron can be sliced perpendicular to an axis of symmetry, to give a regular hexagon. Again, in top view:

{: style="text-align:center"}
![Cube and octahedron sliced with a regular hexagon cross-section, top view]({{site.baseurl}}/assets/2017/pentagon-in-pyramid/hexes.svg)

The same thing works to get a square slice from a tetrahedron, or a decagonal slice from a dodecahedron or icosahedron. But these all rely heavily on the symmetry of the underlying shape: the cube has a six-fold symmetry (simultaneously rotate by 60° around a long diagonal and reflect across a perpendicular plane) that becomes a symmetry of its hexagonal slice. The pyramid does not have a five-fold symmetry. So how do we get something more symmetric by slicing it?

The trick is that the pyramid is only really half of the underlying symmetric shape that you're slicing. To get a regular pentagon, the pyramid that you should start with is not the Egyptian one, but a taller pyramid, the Johnson solid with one square face and four equilateral-triangle faces. This shape is what you get if you slice a regular octahedron in half along its equator; the equator becomes the square face.

The octahedron still is not pentagonally symmetric. But as Schönemann wrote in 1873, you can get the twelve vertices of a regular icosahedron by subdividing each of the twelve edges of an octahedron in the golden ratio, so that the subdivision points on each octahedron face form an equilateral triangle (the blue triangles in the image below). These eight triangles form eight of the faces of the faces of the icosahedron; the other twelve faces are interior to the octahedron. This icosahedron-in-octahedron is dual to another polyhedral pair, a cube formed by selecting eight out of the twenty vertices of a regular dodecahedron.

{: style="text-align:center"}
![Icosahedron in an octahedron]({{site.baseurl}}/assets/2017/pentagon-in-pyramid/icosahedron-in-octahedron.svg)

([Here's another more three-dimensional view](http://steiner.math.nthu.edu.tw/d3/d2/quick-and-dirty/Smallest%20Octahedron%20Containing%20the%20Icosahedron.html). See also [John Baez's tidbits of geometry](https://johncarlosbaez.wordpress.com/2012/03/15/tidbits-of-geometry/).)

The neighbors of any one vertex in an icosahedron form a regular pentagon. And although this pentagon isn't a slice of the octahedron, it is a slice of the half-octahedron pyramid.

This connection between pentagons and pyramids is apparently an exercise from a 1986 Russian mathematics book by I. F. Sharygin, which asks for the height of the pyramid having a regular pentagonal cross-section. I found it in "[Putting the Icosahedron into the Octahedron](http://forumgeom.fau.edu/FG2017volume17/FG201710index.html)", Paris Pamfilos, _Forum Geometricorum_ 2017, who replaces an algebraic calculation of the pyramid height by a couple of applications of [Menelaus's theorem](https://en.wikipedia.org/wiki/Menelaus%27_theorem) and from the result rediscovers Schönemann's inscription of an icosahedron within the octahedron. But I think it's simpler to go the other way: inscribe an icosahedron within an octahedron, and use it to find the pentagonal cross-section.

(See the [G+ post](https://plus.google.com/100003628603413742554/posts/EvRgzZgzEww) for discussion, including some Blender renders by Kram Einsnulldreizwei and a paper model by Gerard Westendorp)