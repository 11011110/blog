---
layout: post
title: A fractal arbelos
date: 2023-04-16 18:04
---
If you nest a triangle in a hexagon in a dodecagon, etc., doubling the number of sides each time, you get a triangulation. This sequence of nested polygons was already known to Archimedes, who took it all the way up to 96 sides in order to calculate an accurate [approximation of $$\pi$$](https://en.wikipedia.org/wiki/Approximations_of_%CF%80).

{: style="text-align:center"}
![Triangle in a hexagon in a dodecagon in a circle]({{site.baseurl}}/assets/2023/archimedes.svg){: style="width:100%;max-width:540px" }

Replacing each triangle by an [arbelos](https://en.wikipedia.org/wiki/Arbelos), the shape between one outer semicircle and two inner ones, and keeping the same pattern, with each triangle connected to one bigger one and two smaller ones, we get a nice tessellation of a semicircle, which can be extended outward in the same way to tile a halfplane. Alternatively, you can think of these as forming a triangulation of the [hyperbolic plane](https://en.wikipedia.org/wiki/Hyperbolic_geometry) by [ideal triangles](https://en.wikipedia.org/wiki/Ideal_triangle). Under this reinterpretation, the distinction between bigger and smaller goes away; all the triangles are the same size.

{: style="text-align:center"}
![A fractal arbelos]({{site.baseurl}}/assets/2023/fractal-arbelos.svg)

It looks like a [uniform tessellation of the hyperbolic plane](https://en.wikipedia.org/wiki/Uniform_tilings_in_hyperbolic_plane), but it's not: it has at most a one-dimensional group of symmetries, not the full two-dimensional group that a uniform tiling would have. There is a uniform tessellation generated by reflections across the sides of an ideal triangle, but it's not this one:

{: style="text-align:center"}
![Uniform tessellation by reflected ideal triangles]({{site.baseurl}}/assets/2023/uniform-ideal.svg 'PD image by Saric from Wikimedia commons, File:Ideal-triangle hyperbolic tiling.svg'){: style="width:100%;max-width:540px" }

They have the same combinatorial structure (their dual graphs form the same infinite 3-regular tree), but their geometry is different. You can tell they're not the same because in the uniform tessellation, each triangle is adjacent to its reflection across each of its sides. In the fractal arbelos, if you reflected any triangle across its top side, the other two sides would reflect into vertical rays, but we don't see any vertical rays. Instead, the fractal arbelos is what you get when you contract the vertical sides of the [aperiodic binary tiling of the hyperbolic plane](https://en.wikipedia.org/wiki/Binary_tiling) (below) into points at infinity, leaving the other sides straight (in the hyperbolic plane).

{: style="text-align:center"}
![The binary tiling]({{site.baseurl}}/assets/2018/binary-tiling.svg)

Now let's take it down to only some fixed level, rather than recursing infinitely all the way down, and number the vertices in binary.

{: style="text-align:center"}
![Fewer levels of the fractal arbelos, with its vertices numbered in binary]({{site.baseurl}}/assets/2023/numbered-arbelos.svg)

We can read off a lot of information from these numbers:

* Each numbered point, with number $$x$$, is connected by arcs to other numbers $$x\pm 2^i$$, where $$2^i$$ is less than or equal to the smallest power of two used in the binary representation of $$x$$ (its rightmost one-bit). In the special case $$x=0$$, any power of two is allowed.

* Each numbered point, with nonzero number $$x$$, is the middle point of exactly one arbelos-shaped tile. If $$p$$ is the largest power of two in the binary representation of $$x$$, then the two smaller tiles under this one are numbered $$x\pm p/2$$. The larger tile above it is either $$x+p$$ or $$x-p$$, depending on whether the next bit in the binary representation of $$x$$ is a $$0$$ or a $$1$$, respectively.

The same numbering system can be extended to all tiles in the halfplane, using [dyadic rationals](https://en.wikipedia.org/wiki/Dyadic_rational) in place of integers. The one-dimensional symmetry group is then apparent from the numbers: it's just multiplication or division by finite powers of two.

If the existence of a special point $$0$$, with no arbelos above it, is a concern, then you can replace $$0$$ by any [2-adic integer](https://en.wikipedia.org/wiki/P-adic_number) whose left-infinite binary representation has infinitely many zeros and infinitely many ones, and number from there in the same way. You can either choose a number with a periodic binary representation (in which case you still get a one-dimensional symmetry group) or an aperiodic representation (producing a tiling with no symmetries at all).

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/110211494756432130))