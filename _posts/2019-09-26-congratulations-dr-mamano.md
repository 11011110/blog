---
layout: post
title: Congratulations, Dr. Mamano!
date: 2019-09-26 21:05
---
Today [Nil Mamano](https://www.ics.uci.edu/~nmamano/) successfully passed his dissertation defense. Nil has been a doctoral student at UCI, jointly supervised by Mike Goodrich and myself.

His dissertation, _New Applications of the Nearest-Neighbor Chain Algorithm_, includes material from several papers I've discussed here before:
[stable matching for points in grids]({{site.baseurl}}{% post_url 2017-04-11-stable-grid-matching %}),
[geographic clustering using stable matching with road network distances]({{site.baseurl}}{% post_url 2017-06-29-stable-redistricting-in %}),
[data structures for nearest neighbors in planar networks]({{site.baseurl}}{% post_url 2018-03-14-finding-nearest-open %}),
[stable-marriage Voronoi diagrams]({{site.baseurl}}{% post_url 2018-04-26-stable-marriage-voronoi %}), and
[the equivalence of local and global optimization for a wide range of combinatorial optimization problems]({{site.baseurl}}{% post_url 2019-02-21-mutual-nearest-neighbors %}).

A common theme running through much of this work is the use of the [nearest-neighbor chain algorithm](https://en.wikipedia.org/wiki/Nearest-neighbor_chain_algorithm) to find pairs of objects that are mutual nearest neighbors (a local definition of optimality) more quickly per pair than one could find the closest pair of objects (global optimality). A greedy algorithm based on this principle will find pairs in a different order than one that uses global closest pairs, but for many problems this ordering makes no difference in the eventual result. For these problems, once a pair become mutual nearest neighbors, they remain so until chosen, so the family of allowable sequences of choices made by the algorithm forms an [antimatroid](https://en.wikipedia.org/wiki/Antimatroid).

As you might imagine, this makes for a long dissertation; unlike some other places, UCI has no upper limit on dissertation length. In fact, we briefly thought that Nil had unnecessarily included everything he'd done here in his dissertation, but it's not even close to true. He also has publications on
[graph watermarking]({{site.baseurl}}{% post_url 2016-06-01-robust-graph-isomorphism %}) and [knight's tours]({{site.baseurl}}{% post_url 2019-01-31-linkage %}) that didn't fit with the main theme and were not included, as well as some even earlier publications on [simulated annealing for biological network alignment](http://sana.ics.uci.edu/) with UCI professor Wayne Hayes, started while he was an exchange student here, before he joined the doctoral program and the theory group.

I think Nil already has a strong record of research and would do well continuing in that direction, but he has decided that he doesn't want to, and I wouldn't want to pressure him to change that decision even if I thought it would be successful. He tells me that he has a love-hate relation with research: he loves doing it, but he hates that (for him) to do it well, he has to make it the most important thing in his life. Instead, now that he has completed his doctorate, he will be looking for a job in industry.

Anyway, congratulations, Nil!

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/102862578075877620))