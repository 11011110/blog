---
layout: post
title: Serpentine belts
date: 2019-08-22 21:19
---
Many car engines use a [serpentine belt](https://en.wikipedia.org/wiki/Serpentine_belt), passing across multiple pulleys and [tensioner wheels](https://en.wikipedia.org/wiki/Tensioner), to transmit mechanical power and timing information from the car's crankshaft to its alternator, engine fan, water pump, air conditioning, steering pump, and other systems. Another (usually separate) belt, the [timing belt](https://en.wikipedia.org/wiki/Timing_belt_(camshaft)), similarly connects the crankshaft to the camshaft, which controls and drives the timing of the engine's valves.
The [Volvo bus engine](https://commons.wikimedia.org/wiki/File:Belt_drive_systen_01.JPG) below shows both of these belts:

{: style="text-align:center"}
![Timing and serpentine belts of a Volvo bus engine; CC-BY-SA photo by Miya.m from https://commons.wikimedia.org/wiki/File:Belt_drive_systen_01.JPG]({{site.baseurl}}/assets/2019/Volvo-bus-engine-belts.jpg){: style="border-style:solid;border-color:black;" width="60%"}

But suppose you encounter such an engine with its belt removed. How can you tell where to run the belt to connect it all back together again? There may be many different orderings in which you can connect a given set of wheels by a belt. On a real engine (such as the one in a Ford Escort on which I loosely modeled the top image below), you might get a little more information from which of the wheels are ribbed (inside the belt) and which are smooth (outside the belt) but even that extra information won't always give you a unique solution:

{: style="text-align:center"}
![Two serpentine belts for the Ford Escort]({{site.baseurl}}/assets/2019/escort.svg)

Connecting wheels with belts like this is the topic of my latest preprint, "Existence and hardness of conveyor belts" ([arXiv:1908.07668](https://arxiv.org/abs/1908.07668), with a large group of co-authors merging groups from the University of Washington and the Bellairs workshops). The name isn't really accurate, because most conveyor belts have simpler geometry, but that's what the question was called in past work. At least we managed to avoid the misspelling "conveyer" of some of that work.

To be tight, a belt for a system of disjoint disks (representing the pulleys and wheels) must be a smooth simple closed curve, made by connecting arcs of the disks with [bitangents](https://en.wikipedia.org/wiki/Tangent_lines_to_circles#Tangent_lines_to_two_circles) between pairs of disks. It was already known that some systems of disks have no belt, and conjectured that unit disks always have one. Our work shows that it's $$\mathsf{NP}$$-complete to tell whether a belt exists, that they do exist for certain special systems of disks (e.g. when no vertical line crosses multiple disks), and that by adding a linear number of extra disks one can always make a belt exist.

The question of how many different belts can connect the same system of disks (posed to me by co-author Sara Billey) was to a large extent the inspiration for [my earlier paper on counting triangulations]({{site.baseurl}}{% post_url 2019-03-12-counting-polygon-triangulations %}). If counting simple polygons through a set of points is hard, then so is counting belts for tiny disks. And when I couldn't prove that counting simple polygons is hard, I turned to other problems for which the proof was easier.

As part of this project I wrote [a little Python program to draw systems of disks and their belts]({{site.baseurl}}/assets/2019/drawbelts.py), used for the image above and for some of the images in the paper. It doesn't find which belts are possible itself; instead, you have to specify the belt by listing the disks that it touches in order (allowing repetitions although some of the versions of the problem that we studied do not) and specifying for each disk which direction it turns when the belt touches it (equivalently, whether it is inside or outside the belt). To use it, you'll need my [PADS Python library](https://www.ics.uci.edu/~eppstein/PADS/), or at least [the package in it for generating SVG files](https://www.ics.uci.edu/~eppstein/PADS/SVG.py).