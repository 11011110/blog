---
layout: post
title: Simplifying task-milestone diagrams
date: 2019-01-29 16:22
---
In my graph algorithms class last week, I covered critical path scheduling, as motivation for the linear-time algorithms for computing shortest and longest paths in directed acyclic graphs. In this scheduling problem, you are given a system of tasks, each with a predicted time to perform it, and constraints that some tasks should be done before others. Assuming that you have enough people working together to perform tasks in parallel, how quickly can you get everything done?

An optimal solution can be found by scheduling each task to start at a time given by the longest sequence of tasks leading up to it such that each consecutive pair in the sequence must be performed sequentially. The total length of the resulting schedule equals the length of the [critical path](https://en.wikipedia.org/wiki/Critical_path_method), the longest sequence of sequential tasks in the whole system. The example below could represent subtasks of a software project: design, implement, and test the software (A, B, and C), develop test cases (D), and document the results (E). Its critical path could be one of ABC, DE, AE, or DC, depending on the lengths of each task.

{: style="text-align:center"}
![Five tasks with ordering constraints]({{site.baseurl}}/assets/2019/pert1.svg)

It's easy enough to solve this problem directly, but to convert it to a path problem we need to have lengths on edges rather than times on vertices. It's also convenient to have a single starting vertex for all the paths.
Therefore, [Wikipedia's article on the critical path method](https://en.wikipedia.org/wiki/Critical_path_method) uses a different kind of graph, which I'll call a "task-milestone diagram" to distinguish it from the one above.
In this diagram, the vertices represent milestones, single points in time. The tasks to be performed are represented by edges, and the time to perform a task becomes the length of its edge. The goal of the scheduling problem now becomes one of choosing a time for each milestone, with enough time between pairs of milestones to perform each task.
The longest-path schedule, in which we place each milestone at a time given by the longest path to it from the start milestone, solves this problem optimally.

To convert a system of tasks and ordering constraints (without milestones) into an equivalent task-milestone diagram, make two new milestones for each task, one for when it starts and one for when it ends. Turn each task into an edge between its two milestones. Transform each ordering constraint (saying that task X should be performed earlier than task Y) into a length-zero edge from the end of task X to the beginning of task Y. Add two more milestones, for the start and end of the whole project. And add more length-zero edges from the project start to the start of each task that has no predecessors, and from the end of each task that has no successors to the project end milestone.

{: style="text-align:center"}
![Expanding each task vertex into two milestone vertices connected by a task edge]({{site.baseurl}}/assets/2019/pert2.svg)

In the resulting graph, the paths from the start to the end milestone consist of the same sequences of tasks as we had before: ABC, DE, AE, or DC, separated by length-zero edges.
And for computational purposes the expansion doesn't blow up the input size enough to cause any problems. But if we want to use this diagram for visualizing the resulting schedule, it's a little confusing because of all of those extra length-zero edges. They don't really represent tasks; they're just there to make sure that the paths connect the tasks in the correct order. Do we really need so many of them?

There are a couple of simple rules that can be used to reduce the number of length-zero edges:

* If two vertices both have only zero-length edges going out of them, and both have the same set of outgoing neighbors, they can be merged into a single vertex. Symmetrically, if two vertices both have only zero-length edges coming into them, and both have the same set of incoming neighbors, they can be merged.
* If a vertex has only one edge going out of it, of length zero, it can be merged with its outgoing neighbor. Symmetrically, if a vertex has only one edge coming into it, of length zero, it can be merged with its incoming neighbor.

For instance, the first rule will merge the milestones for the starts of tasks A and D, and the second rule will merge the resulting vertex into the start vertex. Repeatedly applying these rules produces the following simplified graph. Note that its start-to-end paths, ABC, DE, AE, and DC, are exactly the same as the potential critical paths that we started with. 

{: style="text-align:center"}
![Path-preserving simplification of the task-milestone diagram]({{site.baseurl}}/assets/2019/pert3.svg)

If we assume that the task edges all have non-negative length (as they do in the scheduling application) and that we only care about longest paths, there are even more simplifications that we can perform. These ones might change the set of all paths in the graph (as identified by their sequences of tasks) but they preserve the identities of the longest paths:

* If a zero-length edge goes from task X to task Y, and the graph contains another path between the same two tasks, remove the edge.

* If a zero-length edge goes from task X to Y, every other edge into Y or out of X has length zero, and every incoming neighbor of task Y has a path to every outgoing neighbor of task X, then merge X and Y into a single vertex.

In our example, there are no redundant edges for the first rule to remove, but the bottom edge meets the conditions of the second rule. Applying that rule produces an even simpler task-milestone diagram:

{: style="text-align:center"}
![Additional simplification preserving longest paths]({{site.baseurl}}/assets/2019/pert4.svg)

Our example has no instances of the first rule, but when it is used it removes paths from the graph. The removed paths can never be longest paths, because any path through the removed edge can be made longer by replacing that edge by a different path from X to Y.
When we perform the second rule, we may introduce new paths that were not already present, from a predecessor of Y, through the merged vertex, to a successor of X. For instance, the new graph has a path through only the two tasks AC, which was not one of the four paths we started with. But because these new paths replace portions of existing paths by two length-zero edges, they can never be the longest path, and the resulting compacted diagram can safely be used for scheduling.