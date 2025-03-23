---
layout: post
title: The ancient Greek mathematics of distorted airplane propeller photos
date: 2025-03-22 18:35
---
When [Hippias of Elis](https://en.wikipedia.org/wiki/Hippias) studied the curve that came to be known by his name, the [quadratrix of Hippias](https://en.wikipedia.org/wiki/Quadratrix_of_Hippias), some 24 centuries ago, it is unlikely that he had in mind the distorted photographs of airplane propeller blades produced by a camera with a [rolling shutter](https://en.wikipedia.org/wiki/Rolling_shutter).

{: style="text-align:center"}
[![Rolling shutter phenomenon on a grounded Yak TD, CC-BY 2.0 image by Soren Ragsdale, 9 January 2009, https://commons.wikimedia.org/wiki/File:Rolling_shutter_n%C3%A4idis.png]({{site.baseurl}}/assets/2025/distorted-propeller.png)](https://commons.wikimedia.org/wiki/File:Rolling_shutter_n%C3%A4idis.png)

This strange-looking effect is produced when an imaging device (a camera, scanner, etc) creates an image one line at a time, in quick succession, so that the lines of the image are produced at slightly varying times. In the image above, I believe the scan lines are vertical, but I can't tell whether they were scanned left-to-right or right-to-left. In either case, the airplane propeller spins so quickly that it is at a noticeably different position from one scan line to the next. What you see as its distorted image consists of the points where, progressing through this imaging process, the scan line intersects the rotating line of the propeller blade.

Alternatively, in a three dimensional space where two of the dimensions are the horizontal and vertical coordinates of the photo and the third is time, the spinning propeller blade traces out a [helicoid](https://en.wikipedia.org/wiki/Helicoid), extending out from the image plane in the time dimension, and the scan line simultaneously traces out an inclined plane. The image you see of the propeller is the cross-section of the helicoid where it is sliced by this scan plane.

{: style="text-align:center"}
[![Helicoid, CC-BY-SA 3.0 image by Krishnavedala, 20 May 2011, https://commons.wikimedia.org/wiki/File:Helicoid.svg]({{site.baseurl}}/assets/2025/helicoid.svg){: style="width:100%;max-width:480px" }](https://commons.wikimedia.org/wiki/File:Helicoid.svg)

Hippias constructed his curve as the locus of points of intersection of two moving lines, one rotating (like the propeller blade) and the other translating (like the scan line). The only important difference between his definition and the distorted propellor photo is that these two lines should coincide, at the point in time when the scan line crosses the propeller axis. If, instead, the propeller is at an angle when the scan line crosses the axis, you'll get a curve resembling the quadratrix but tilted asymmetrically, the way the one in the photo is.

{: style="text-align:center"}
[![Animation of the construction of a quadratrix as the point of intersection of a rotating line and a translating line, CC-BY-SA 3.0 image by Zorgit, 14 September 2008, https://commons.wikimedia.org/wiki/File:Quadratrix_animation.gif]({{site.baseurl}}/assets/2025/quadratrix-animation.gif){: style="width:100%;max-width:400px" }](https://commons.wikimedia.org/wiki/File:Quadratrix_animation.gif)

An alternative construction of the quadratrix, by [Pappus of Alexandria](https://en.wikipedia.org/wiki/Pappus_of_Alexandria), intersects a helicoid and an inclined plane, before projecting the result onto a plane perpendicular to the axis of the helicoid. To get the quadratrix rather than something tilted, the line on the helicoid that passes through the intersection point of the axis and the inclined plane must be contained in this plane.

Nowadays, we might instead view the quadratrix as a piece of the graph of the function $$y=x\cot x$$ (scaled below to pass through the $$x$$-axis at odd integers). The difference between this graph, below, and the rolling-shutter image of a perfectly-aligned propeller blade, is that together with the graph of the function you would also see an image of the blade in a vertical ray, coinciding with the $$y$$-axis. In the photo that I started with, this ray is tilted slightly to the right.


{: style="text-align:center"}
[![Graph of the function y=x cot pi/2 x, CC-BY 3.0 image by Kmhkmh, 3 May 2011, https://commons.wikimedia.org/wiki/File:Quadratrixfunktion.svg]({{site.baseurl}}/assets/2025/xcotx.svg){: style="width:100%;max-width:600px" }](https://commons.wikimedia.org/wiki/File:Quadratrixfunktion.svg)

As for what Hippias was actually thinking about when he studied this curve: we don't really know because his writings are lost. What we know about him comes from other ancient Greek mathematicians writing centuries later. But the standard theory is that he was using it to trisect angles. If you happen to have one of these curves handy, you can use it to find the correspondence between positions of the rotating propeller line and positions of the moving scan line. If two positions of the propeller define an angle, then it can be trisected by trisecting a line segment between the two corresponding positions of the scan line, a much easier task. Of course, the impossibility of trisecting angles by compass and straightedge means that you cannot construct the trisectrix by compass and straightedge, but you can still construct infinitely many points on it and approximate the trisection arbitrarily closely. The quadratrix can also be used to square the circle, that is, to construct a square whose area equals the area of a given circle, and that's where it gets its name: squaring a circle is called quadrature. We don't think Hippias was thinking about this, either: this use of the quadratrix is credited to [Dinostratus](https://en.wikipedia.org/wiki/Dinostratus), maybe 70 years after Hippias's work.