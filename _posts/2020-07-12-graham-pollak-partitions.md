---
layout: post
title: Graham–Pollak partitions
date: 2020-07-12 15:46
---
As you've probably already seen, Ron Graham recently died. I first met him many years ago at Xerox PARC; what I remember from that meeting is this old guy easily beating me at ping-pong, and I was startled to learn (while working to beef up [his Wikipedia article](https://en.wikipedia.org/wiki/Ronald_Graham) after his death) that that was exactly Graham's first impression of Paul Erdős. We've chatted about research, most recently in [2018 in Barbados](https://www.ics.uci.edu/~eppstein/pix/bellairs18/index.html), but somehow never published anything together; on the other hand, Graham's work in computational geometry, Ramsey theory, and approximation algorithms has certainly had a strong influence on me. Anyway, as part of the project of improving his Wikipedia article, I put together a separate new article on [the Graham–Pollak theorem](https://en.wikipedia.org/wiki/Graham%E2%80%93Pollak_theorem), the theorem that partitioning the edges of an $$n$$-vertex complete graph into complete bipartite subgraphs requires at least $$n-1$$ subgraphs. And while doing that, I started to wonder about what the optimal partitions look like, and how many there are.

In _Proofs from THE BOOK_, Aigner and Ziegler describe a simple construction for an $$(n-1)$$-subgraph partition: just order the vertices of the complete graph, and make a star connecting each vertex (except the last) to its later neighbors.
But there are a lot more partitions than that. For instance, you can take any rooted binary tree whose leaves are the vertices of the complete graph, and form a partition in which each complete bipartite subgraph connects the left and right descendants of one of the interior nodes of the tree. The ordered star partition is the special case of this where each internal node has one leaf child.

{: style="text-align:center"}
![Graham–Pollak partitions from binary trees]({{site.baseurl}}/assets/2020/graham-pollak-hierarchy.svg)

Even these are not the only possibilities. For instance, a four-vertex complete graph can be partitioned into $$K_{1,2}$$ subgraphs in this triskelion pattern:

{: style="text-align:center"}
![Graham–Pollak partitions from binary trees]({{site.baseurl}}/assets/2020/graham-pollak-triskelion.svg)

More generally, whenever one has a partition of $$K_n$$, one can form a partition of a larger complete graph by partitioning its vertices into $$n$$ subsets, applying the partition of $$K_n$$ to the edges that go from one subset to another, and then recursively partitioning the edges within each subset. This is already enough to show that there is a rapidly growing number of these partitions, but not enough to count them more precisely.

This still leaves many questions. How many Graham–Pollak partitions does $$K_n$$ have, as a function of $$n$$? How complicated can they be? If we define a state space whose states are Graham–Pollak partitions, and whose state transitions correspond to re-partitioning the subgraph formed by two of the complete bipartite graphs, is it connected? Can a graph traversal of this state space list all the Graham–Pollak partitions faster than a brute force search? What does a random partition look like?

It's too bad Ron's no longer around to help answer some of them.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/104503441875881282))