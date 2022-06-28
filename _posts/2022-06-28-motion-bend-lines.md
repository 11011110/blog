---
layout: post
title: The motion of bend lines on smooth surfaces
date: 2022-06-28 16:25
---
You may have played with a paper yoyo, a strip of paper wrapped around a stick so that when you flick it with your wrist, it extends outward into a long tube. Here's one, [the only example I could find on Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Arcade_Paper_Laser,_August_8th_2016.jpeg):

{: style="text-align:center"}
![Arcade Paper Laser, public domain image by Zhonghua88, 8 August 2016, from Wikimedia Commons]({{site.baseurl}}/assets/2022/paper-yoyo.jpg){: style="width:100%;max-width:720px" }

If you've used one, then the way they work is simple and intuitive. But if you know a little bit about the [mathematics of paper folding](https://en.wikipedia.org/wiki/Mathematics_of_paper_folding) and [developable surfaces](https://en.wikipedia.org/wiki/Developable_surface), and think about it, it starts to seem a little strange.

Paper can bend or fold, but not stretch. When a flat sheet of paper is bent into a smooth but not flat surface (as it is in all states of the paper yoyo), it bends along straight "bend lines" that extend all the way across the surface, and that are forced to remain straight. You may be familiar with the way that a slice of pizza will droop if you try to hold it flat from its crust, but will remain straight if you bend it lengthwise: the bend lines are holding it in a rigid shape. Or, if you roll a poster into a cylinder, you can wave it around like a light saber, again making it much more rigid than the unrolled poster (at least until you hit it into something hard enough to crumple it).

In the rolled-up state of the paper yoyo, it's again rolled into a cylinder, with bend lines parallel to the cylinder axis. If we mark some of those bend lines and unroll it flat, it might look something like this:

{: style="text-align:center"}
![Bend lines in a rolled paper yoyo]({{site.baseurl}}/assets/2022/paper-yoyo-rolled.svg){: style="width:100%;max-width:720px" }

But then, what happens when you extend it? The paper cannot stretch from its rectangular shape into a parallelogram. Instead, as it extends, the bend lines continuously rotate on the surface of the paper. Near the point where they attach to the stick, the non-perpendicular bend lines cause the paper to flare out a little from its cylindrical shape, but it is surrounded by more wrapped paper constraining it from flaring very widely, so the bend lines must still stay near their original orientations. Farther along the yoyo, the bend lines can twist to bigger angles:

{: style="text-align:center"}
![Bend lines in a rolled paper yoyo]({{site.baseurl}}/assets/2022/paper-yoyo-extended.svg){: style="width:100%;max-width:720px" }

So although the bend lines of a smoothly bent sheet of paper are rigid along their length, they can slide and twist continuously within the sheet, as the sheet flexes continuously while remaining smooth. This twisting motion of bend lines is essential for understanding the seemingly-knotted surface below, two round disks connected by a thin band tied in an overhand knot:

{: style="text-align:center"}
![Knotted paper dumbbell shape]({{site.baseurl}}/assets/2022/knotted-dumbbell.svg)

If you want to unknot it while keeping it smooth rather than crumpling it, you will obviously have to make the disks smaller by rolling them up somehow, perhaps into a cylinder around one of their diameters. But if you do that, you will put a bend line through or near the diameter, which will act like a rigid rod. And if you attach the knotted center band to two rigid rods, of length equal to the diameter of the disks, you definitely cannot untie it. The rods are too long to poke all the way through the knot before getting stuck.

On the other hand, this surface can be untied while keeping it smooth! The trick is that, after you have rolled up one of the disks to make a rigid cylinder, with the tied band at one end, you can twist the roll, so that its bend lines rotate around the disk. As you do, the point where the band is tied will slide from one end of the cylinder to the other. And you can make this sliding motion coincide with the motion of the cylinder through a hole in the tied band, untying it.

This and similar examples are the focus of my third new CCCG preprint, "Locked and unlocked smooth embeddings of surfaces", [arXiv:2206.12989](https://arxiv.org/abs/2206.12989). In the phrasing of the title, the two disks with a tied center band, above, are unlocked: they can be reconfigured to a flat state while remaining smooth. My paper also shows that any compact shape with a continuous shrinking motion into itself, like the polygon below, is unlocked.

{: style="text-align:center"}
![Polygon with a continuous shrinking motion]({{site.baseurl}}/assets/2022/generalized-star.svg){: style="width:100%;max-width:600px" }

On the other hand, there exist surfaces that, while topologically equivalent to their flat state, cannot be made flat through a continuous sequence of smooth embeddings. The simplest one that I found consists of a central square mat, rolled up into a cylinder and held into its cylindrical shape by two loops, entangled with each other in a pattern based on the Borromean rings:

{: style="text-align:center"}
![Locked shape consisting of a rolled square mat with two entangled loops]({{site.baseurl}}/assets/2022/tied-roll.svg)

There is actually quite a lot of freedom in the pattern of bend lines of the central square. They can twist until the bend line through the center of the square gets halfway to the corners of the square:

{: style="text-align:center"}
![Twisted bend lines in the rolled square mat]({{site.baseurl}}/assets/2022/bent-roll.svg)

But after that point, the entangled loops block the twisting from going any farther. They cannot be disentangled from each other without being pulled around the rigid central bend line, and they are too short for that to be possible, so the surface is locked.

It's not clear to me whether all simple polygons are unlocked, or whether it's possible to make locked polygons without holes. I also don't have any algorithmic results in this area; it seems likely that testing whether a surface is locked or unlocked is hard, but I don't know how to prove it.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/108557742866716208))