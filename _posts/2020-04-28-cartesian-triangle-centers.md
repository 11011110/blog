---
layout: post
title: Cartesian triangle centers
date: 2020-04-28 21:24
---
The usual definition of a Euclidean [triangle center](https://en.wikipedia.org/wiki/Triangle_center) is a point defined from a triangle in a way that is [equivariant](https://en.wikipedia.org/wiki/Equivariant_map) under [similarity transformations](https://en.wikipedia.org/wiki/Similarity_(geometry)), meaning that applying the transformation to a triangle and then constructing its center produces the same point as constructing the center first and then transforming it. These include familiar points defined from triangles like the [orthocenter](https://en.wikipedia.org/wiki/Orthocenter) (where perpendiculars to the sides meet), [incenter](https://en.wikipedia.org/wiki/Incenter) (the center of the inscribed circle), and [circumcenter](https://en.wikipedia.org/wiki/Circumcenter) (the center of the circumscribed circle). What I have in mind in this post is a similarly-defined concept, but with a different group of transformations than similarity: the combination of any two separate linear transformations to the two coordinate axes of the [Cartesian plane](https://en.wikipedia.org/wiki/Cartesian_plane), or transformations that swap the (transformed) axes. Another way of describing these transformations is that they preserve axis-parallel lines and relative area. They also preserve other lines and parallelism of lines.

One of the standard Euclidean triangle centers turns out to be a Cartesian center as well: the centroid has as its coordinates the average of the three triangle vertex coordinates, and this coordinatewise calculation (independent of the ordering of the three vertices) shows it to be equivariant under Cartesian transformations. It is also the point where the three lines through each vertex and opposite side midpoint meet.

{: style="text-align:center"}
![Centroid of a triangle]({{site.baseurl}}/assets/2020/centroid.svg)

Similarly, we can find a Cartesian triangle center from the coordinatewise median of the three vertices.

{: style="text-align:center"}
![Median of a triangle]({{site.baseurl}}/assets/2020/median.svg)

The center of the axis-parallel bounding box is also a Cartesian triangle center, again computed coordinatewise as the average of the minimum and maximum coordinates.

{: style="text-align:center"}
![Bounding-box center of a triangle]({{site.baseurl}}/assets/2020/bbcenter.svg)

But a Cartesian triangle center does not have to be determined coordinatewise in this way. As an example, denote the three triangle vertices by $$p_1,p_2,p_3$$ and consider the point $$q$$ with the property that the axis-parallel bounding boxes of the three line segments $$qp_i$$ all have equal area. For two points $$p_i$$ and $$p_j$$, the locus of points for which the two bounding boxes have equal area is a line through the other two corners of the bounding box of segment $$p_ip_j$$. (To see this, consider a linear transformation that takes this bounding box to a square, and apply symmetry.) The three lines defined in this way from the three pairs of vertices of a non-degenerate triangle always meet in a point, the center we are seeking. And it's equivariant under Cartesian transformations because these transformations preserve the ratios of areas of bounding rectangles.

{: style="text-align:center"}
![Point of equal bounding boxes of a triangle]({{site.baseurl}}/assets/2020/equalbb.svg)

You can tell it's not a coordinatewise center because, in the figure above, the triangle vertices have equally spaced $$y$$-coordinates, from which it follows that all coordinatewise centers lie on the horizontal line with median $$y$$-coordinate, but this center doesn't.

In general, the geometry of the plane with Cartesian instead of Euclidean transformations does not seem to have been very thoroughly explored. These examples show, I think, that there are interesting things to find there.