---
layout: post
title: Playing with model trains and calling it graph theory
date: 2019-05-02 19:03
---
You've probably played with model trains, for instance with something like the [Brio](https://en.wikipedia.org/wiki/Brio_(company)) set shown below.[^fn] And if you've built a layout with a model train set, you may well have wondered: is it possible for my train to use all the parts of my track?

{: style="text-align:center"}
![Brio train set]({{site.baseurl}}/assets/2019/brio-33133.jpg)

For instance, in the layout shown in this image, if your train starts on the far right, moving downward, it will be stuck in a loop that it can never escape. There are no choice points where the train can switch to another track until it returns to the Y at the right, moving in the same direction. On the other hand, if you allow yourself to reverse the train, it can reverse back through the other entrance to the Y and reach the rest of the track. It's also possible for a long-enough train to block itself, preventing it from escaping certain parts of the track that a short train could negotiate more easily.

My newest preprint, "Reconfiguring Undirected Paths" (with Demaine, Hesterberg, Jain, Lubiw, Uehara, and Uno, [arXiv:1905.00518](https://arxiv.org/abs/1905.00518), considers an abstract model for such problems, in which the train track is modeled as an undirected graph and the train is a simple path in the graph. You can slide the train by adding an edge to one end of the path and removing an edge from the other end; we don't distinguish which end of the train is which, so it can slide in both directions. The vertices of the graph model points where you can choose which of several directions to slide the train. Because it's an undirected graph, these are like the three-way and four-way junctions in the middle of the image (allowing the train to enter and exit along any pair of track segments) rather than the Y junctions at the far right (where a train that enters at one of the two top edges of the Y has to exit the bottom).

For instance, in a $$2\times 3$$ grid graph, the different positions of a length-$$3$$ path and the ways that one position can shift into another can be visualized as the state space shown below.

{: style="text-align:center"}
![PSPACE-hardness reduction for path reconfiguration]({{site.baseurl}}/assets/2019/path-reconfig-states.svg)

Testing whether a long train can slide from one position to another turns out to be PSPACE-complete, even on graphs of bounded bandwidth, by a reduction from [nondeterministic constraint logic](https://en.wikipedia.org/wiki/Nondeterministic_constraint_logic). Here's an example of an NCL problem transformed by our reduction into a path-sliding problem:

{: style="text-align:center"}
![PSPACE-hardness reduction for path reconfiguration]({{site.baseurl}}/assets/2019/path-reconfig-redux.svg){: width="80%"}

Our main results are a [fixed-parameter tractable algorithm](Parameterized complexity) parameterized by train length (so it's fast for short trains) and a linear time algorithm when the graph is a tree. Both cases are based on the same intuition, that the problem becomes easier if we can maneuver the train onto a long enough path. For the parameterized version, if the graph has a path twice as long as the train that can be reached from the starting position of the train, and another long path that can reach the ending position, then we can maneuver the train onto the first long path, send it on an express route directly from the first long path to the second one, and then maneuver it from there into its final position. On the other hand, until we find these long paths, we can restrict our attention to a subgraph with no long paths; this implies that it has bounded [tree-depth](Tree-depth) and makes searching within the subgraph easy. The linear time tree algorithm similarly involves a lot of back-and-forth maneuvering of the train to free up longer and longer segments of it until the whole train is freed to move from the start to the goal.

A shorter version of our paper will appear at [WADS](http://wads.org/) this summer.
While it was in submission to WADS, a related preprint appeared on arXiv: "The Parameterized Complexity of Motion Planning for Snake-Like Robots", by Gupta, Sa'ar, and Zehavi ([arXiv:1903.02445](https://arxiv.org/abs/1903.02445)). They show that for a graph-theoretic model of the [Snake video game](https://en.wikipedia.org/wiki/Snake_(video_game_genre)), getting the snake from one position to another is fixed-parameter tractable in the length of the snake. For this problem, snakes are again paths in graphs, but they can move only in one direction, and the techniques they use to prove fixed-parameter tractability involve sparsifying the state space instead of maneuvering into long paths. [Sid Gupta was my student]({{site.baseurl}}{% post_url 2018-08-06-congratulations-dr-gupta %}) at UCI before taking his current postdoc in Israel, but I haven't talked to him about this, so I think their work must be independent and its appearance at about the same time a coincidence.

* Footnotes go here
{:footnotes}

[^fn]: Searching on tineye finds that this image was on Amazon in 2008. Presumably it was supplied to them by Brio?