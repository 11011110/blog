---
layout: post
title: An uncolorable projective configuration
date: 2017-11-19 17:31
---
An [projective configuration](https://en.wikipedia.org/wiki/Configuration_(geometry)) is a collection of points and lines in the plane, so that each two points belong to the same number of lines and each two lines contain the same number of points.
When that same number is three for both points and lines, then the numbers of points and lines must be equal; call this number $$n$$ and call the configuration an $$n_3$$-configuration. Here's an example, with $$n=13$$:

![13-configuration]({{site.baseurl}}/assets/2017/13-configuration.svg)

What makes this particular configuration interesting is a property it shares with the [Fano $$7_3$$ configuration](https://en.wikipedia.org/wiki/Fano_plane) (which I can't draw with straight lines in the plane) but not with some other configurations that I can draw, such as the [Pappus $$9_3$$ configuration](https://en.wikipedia.org/wiki/Pappus_configuration) or [Desargues $$10_3$$ configuration](https://en.wikipedia.org/wiki/Desargues_configuration). That property is that, if I give the points two colors, as I did in the illustration, then at least one of the lines will be monochromatic. For instance, there's an all-red line in the illustration.
Let's call a configuration with this property "uncolorable", for short.

Uncolorability of the Fano configuration follows from the fact that every two points belong to a three-point line. If its seven points are colored with four red points and three yellow points, then each of the six pairs of red points must form a separate line with one yellow point, or else we would have a red line. But if they do, there is only one line left out of the seven that can cover all three pairs of yellow points, so we have a yellow line instead.
Similar reasoning shows that five-two and six-one splits also don't work.

If you have two uncolorable $$m_3$$- and $$n_3$$-configurations, you can glue them into a single uncolorable $$(m+n-1)_3$$-configuration, as follows: delete one point from the $$m_3$$-configuration and one line from the $$n_3$$-configuration, leaving three lines and three points with too few incidences. Then, move the points and lines around (preserving their other incidences) so that the three neighboring lines from the $$m_3$$ configuration each contain one of the three neighboring points from the $$n_3$$ configuration.
It may not be clear how to perform this geometrically in all cases, but at least the abstract pattern of incidences that one should obtain as a result is clear.

If we could color the resulting glued configuration, avoiding monochromatic lines, with the three gluing points not all given the same color, then the same coloring could be used on the $$n_3$$ configuration, and the deleted line would also be non-monochromatic.
On the other hand, if we could color the glued configuration, avoiding monochromatic lines and giving the three gluing points the same color as each other, then the same coloring could be used on the $$m_3$$ configuration. In this case, giving the same color as the gluing points to the deleted point preserves the non-monochromatic coloring of the lines.
So if the $$m_3$$- and $$n_3$$-configurations are both uncolorable without monochromatic lines, then the glued $$(m+n-1)_3$$-configuration is also uncolorable.

In 1894, Steinitz showed in his dissertation that any abstract $$n_3$$-configuration can be drawn in the plane with at most one line non-straight. Using this fact, for any abstract glued configuration, one can realize the $$n_3$$ configuration making the non-straight line be the deleted one. By projective duality, one can realize the $$m_3$$ configuration in such a way that all its triples of lines meet at the points of the configuration except for at one point, the deleted point.
Using a projective transformation to match up the three points of one configuration with the three lines of the other shows that every glued configuration can be realized by straight lines in the plane.

The configuration shown in the illustration is what you get when you glue together two copies of the Fano configuration. (In moving it around to make it more legible, I lost track of which points and lines came from which side of the gluing, and I don't know whether that can be reconstructed from the drawing or whether there are multiple valid partitions. The partition is certainly not given by the colors of the points.) Since the Fano configuration is uncolorable, so is this $$13_3$$-configuration, and so are the infinitely many configurations obtained by gluing together more than two Fanos.

([G+](https://plus.google.com/100003628603413742554/posts/KeDAzkeXPVe))