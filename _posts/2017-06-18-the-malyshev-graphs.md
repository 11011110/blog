---
layout: post
title: The Malyshev graphs
date: 2017-06-18 15:21
---
Some time ago [I reposted a question]({{site.baseurl}}{% post_url 2014-04-05-graphs-with-many %}) from MathOverflow about whether [graphs with many cycles have long cycles with doubled edges as minors](https://mathoverflow.net/q/161006/440). The answer turned out to be no, with a counterexample found by Anton Malyshev for a related question about [paths and doubled-path minors](https://mathoverflow.net/a/162668/440).
Malyshev's graphs can be formed by starting from a pair of vertices (such as the central two vertices in the drawing below) and then repeatedly adding two more vertices adjacent to the two previously-added vertices:

{: style="text-align:center"}
![32-vertex Malyshev graph]({{site.baseurl}}/assets/2017/malyshev32.svg)

Lately I've been thinking about the same graphs again, because they have an interesting combination of properties:

* They are planar, and 2-degenerate, and triangle-free, like the [triangle-free penny graphs]({{site.baseurl}}{% post_url 2017-02-19-triangle-free-penny %}) and the [squaregraphs]({{site.baseurl}}{% post_url 2009-05-28-squaregraphs %}).

* Unlike [both of those other types of graphs]({{site.baseurl}}{% post_url 2017-06-13-how-many-edges %}), an $$n$$-vertex Malyshev graph has exactly $$2n-4$$ edges, the maximum possible for a planar triangle-free graph.

* They have high diameter, linear in the number of vertices.

* They are bipartite, and are maximal among the planar bipartite graphs.

* They are very far from being 3-connected, so if the vertices are labeled they have many distinct planar embeddings, showing that being maximal planar bipartite is very different from being maximal planar.

* They have both bounded treewidth and bounded face size, like the [nested triangles graph](https://en.wikipedia.org/wiki/Nested_triangles_graph) and the [Apollonian networks](https://en.wikipedia.org/wiki/Apollonian_network) but unlike many other planar graphs.

* They are permutation graphs.

One way to see this last property is to recognize that the drawing above is exactly the form that one gets for [a method of drawing planar bipartite permutation graphs that I described in an earlier post]({{site.baseurl}}{% post_url 2012-12-12-planar-bipartite-permutation %}), and in fact to make this drawing I used the same program as the one that I used in that post.

Another way to see it is to find a permutation representation for these graphs.
We want a sequence of permutation elements where each two elements are out-of-order with only the two ahead of them and the two behind them, like this:

{: style="text-align:center"}
![A permutation representing the 32-vertex Malyshev graph]({{site.baseurl}}/assets/2017/malperm32.svg)

We can convert this to [my notation for bipartite permutation graphs]({{site.baseurl}}{% post_url 2012-12-08-notation-for-321-avoiding %}) by scanning this picture from left to right, looking at the direction of the line segments at the top and bottom of the picture at each position in this scan, and recording that pair of directions by a character that slants in the same direction at its top and bottom. In this case, the result is the string "&gt;&gt;\\\\//\\\\//\\\\//\\\\//\\\\//\\\\//\\\\//&lt;&lt;". And that's what I gave my permutation-graph-drawing code as input, to get it to produce the top picture.

([Discussion on Google+](https://web.archive.org/web/20190217225323/https://plus.google.com/100003628603413742554/posts/DSxNzbEd3gK))