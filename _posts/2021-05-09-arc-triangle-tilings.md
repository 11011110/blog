---
layout: post
title: Arc-triangle tilings
date: 2021-05-09 16:20
---
Every triangle tiles the plane, by 180° rotations around the midpoints of each side; some triangles have other tilings as well. But if we generalize from triangles to arc-triangles (shapes bounded by three circular arcs), it is no longer true that everything tiles. Within any large region of the plane, the lengths of bulging-outward arcs of each radius must be balanced by equal lengths of bulging-inward arcs of each radius, and the only way to achieve this with a single tile shape is to keep that same balance between convex and concave length on each tile. Counting line segments as degenerate cases of circular arcs, this gives us three possibilities:

* Ordinary triangles, with three straight sides, which always tile in the ordinary way.

  {: style="text-align:center"}
![Tiling by ordinary triangles]({{site.baseurl}}/assets/2021/ordinary-triangle-tiling.svg)

* Arc-triangles with two congruent curved sides (one bulging out and one in) and one straight side. These always tile, by matching up the curved sides to form strips of triangles bounded by their straight sides. Some of these arc-triangles also have other tilings.

  {: style="text-align:center"}
![Tiling by arc-triangles with two curved sides]({{site.baseurl}}/assets/2021/wave-triangle-tiling.svg)

* Arc-triangles with three sides of the same curvature, the shorter two having equal total length to the longest side. The long side must bulge outwards and the other two sides must bulge inwards. Again, these always tile, although the tiling cannot be edge-to-edge.

  {: style="text-align:center"}
![Tiling by arc-triangles with three curved sides]({{site.baseurl}}/assets/2021/scale-triangle-tiling.svg)

The ordinary triangles tile by translation and rotation, and the three-curved-side arc-triangles tile by translation only, without even needing rotations. However, the two-curved-side triangles generally need reflections for their tilings. If tilings by translation and rotation are desired, then only some of these tile: I think only the ones with angles of $$\pi/3$$, $$\pi/2$$, or $$2\pi/3$$ at the vertex between the two curved sides.

{: style="text-align:center"}
![Tiling by arc-triangles with two curved sides, without reflection]({{site.baseurl}}/assets/2021/pinwheels.svg)

A curious property of the arc-triangles that tile is that they all have interior angles summing to $$\pi$$, something that is not true of most arc-triangles. On the other hand, it is easy to find arc-triangles with angles summing to $$\pi$$ that do not tile, so the angle sum does not completely characterize the tilers among the arc-triangles.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/106207851143984141))