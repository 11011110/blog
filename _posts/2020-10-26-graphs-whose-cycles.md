---
layout: post
title: Graphs whose cycles all touch 
date: 2020-10-26 16:16
---
An interesting recent question on MathOverflow asks about [graphs in which all cycles touch](https://mathoverflow.net/q/374793/440). Here, touching is meant in the same sense as a [bramble](https://en.wikipedia.org/wiki/Bramble_(graph_theory)) in graph structure theory: every two cycles either share a vertex or contain the two endpoints of an edge from one cycle to the other. The graphs with this property include all the complete graphs (girth 3), complete bipartite graphs (girth 4), and theta graphs (arbitrarily high girth but very simple structure). As originally phrased, it asked whether there exists $$g$$ such that graphs of girth $$\ge g $$ with all cycles touching have bounded treewidth. Partial results given there by Tony Huynh and me show that the condition of bounded treewidth can be replaced by bounded vertex cover number or a bounded number of vertex-disjoint cycles without changing the answer.

This led me to look for graphs that have high girth, all cycles touching, and as many vertex-disjoint cycles as I could construct. So far, the best I have found is four vertex-disjoint cycles, as shown in graphs of the following form:

{: style="text-align:center"}
![A graph with four vertex-disjoint long cycles, and all cycles touching]({{site.baseurl}}/assets/2020/4-disjoint-touching-cycles.svg)

It consists of four theta graphs (the pairs of blue vertices connected by multiple long paths of yellow vertices, with the eight blue pole vertices of the theta graphs connected into two four-vertex paths. I've drawn it with yellow paths of length 16, and three paths per theta, but these numbers are arbitrary. One can easily find four vertex-disjoint cycles, within each of the four thetas, ignoring the edges between the pole vertices.

There is no cycle using only the blue pole vertices, so every cycle in the overall graph must include at least one complete yellow path connecting its two poles. Therefore, every cycle is at least as long as this yellow path length. These paths can be made arbitrarily long, so the graphs constructed in this way can have arbitrarily large girth.

The six edges of the two four-vertex paths between the pole vertices include an edge between each of the six pairs of pole vertices. But each cycle uses at least one pair of pole vertices, so this implies that every two cycles touch, either by sharing a pole vertex or by each containing one endpoint of one of these path edges.

Therefore the graphs constructed in this way have arbitrarily large girth, have all cycles touching, and contain four vertex-disjoint cycles. It also has feedback vertex number four. The MathOverflow question asks whether the four vertex-disjoint cycles can be replaced by an arbitrarily large number of cycles, or equivalently whether the feedback vertex number can be increased, but at this point I don't even know whether either number can be replaced by five.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/105103937279022043))