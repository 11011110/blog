---
layout: post
title: Two applications of maximum matching
date: 2020-02-22 17:55
---
This quarter I'm teaching a course on graph algorithms (an upper-division elective, so only around 200 students; our required classes are much bigger) and we've reached the part of the course where we discuss [matching](https://en.wikipedia.org/wiki/Matching_(graph_theory)). Motivating bipartite matching, perfect matching, weighted matching, and stable matching are all easy enough but I wanted a few more examples of applications of non-bipartite [maximum-cardinality matching](Maximum cardinality matching), so I asked my colleague Vijay Vazirani who responded with two cute ones that I wasn't already familiar with.

His first suggestion was two-processor scheduling. To keep things simple and concrete let's assume that we have a collection of equal-length tasks, with a partial ordering (or DAG) describing their timing constraints. If we have one processor to perform them on (or one person to perform them), the obvious solution is to schedule them according to a linear extension of the partial order (a topological ordering of the DAG), allowing them to all be performed with no delays, in total time equal to the number of tasks. But now suppose that there are two processors or people performing the tasks, so we can process two tasks at a time and, ideally, finish twice as quickly. We would like to find a schedule with as many compatible pairs of tasks as we can, saving as many time slots as there are pairs. Two tasks are compatible if they are incomparable in the partial order (there is no path between them in the DAG), so it looks like we simply need to find a maximum matching in the incomparability graph of the partial order. This doesn't quite work because two matched pairs can "cross",
unable to both be used in the same schedule because each pair contains an element constrained to be earlier than an element of the other pair. But when this happens, it's possible to uncross them and get another matching that's at least as good, eventually reaching a matching without any crossings that can be topologically ordered to give an optimal schedule. The connection between this scheduling problem and matching appears to come from Fujii, Kasami, and Ninamiya, "[Optimal sequencing of two equivalent processors](https://doi.org/10.1137/0117070)", _SIAM J. Appl. Math._ 1969; for fast algorithms for this special case of matching see H. Gabow, "[An almost-linear algorithm for two-processor scheduling](https://doi.org/10.1145/322326.322335)", _JACM_ 1982.

Another application, closer to the real world, comes from a problem of matching kidney donors to kidney donor recipients. But we don't use the obvious bipartite graph of donors and recipients. Most kidney transplant recipients enter the matching process paired up already with a friend or relative who is willing to donote one of their kidneys, because otherwise there wouldn't be enough kidneys to go around. But usually these donor-recipient pairs are incompatible with each other, so they need to find another donor-recipient pair such that the donors from each pair are compatible with the recipients from the other pair. Then, all four people get together at the same hospital and trade kidneys. More complicated exchanges of three or more pairs are not done, because that would require simultaneous operations with six or more people and significantly greater chances that one of them will back out at the last minute. So to save as many lives as possible, we need a maximum matching on a graph whose vertices are donor-recipient pairs and whose edges represent double compatibility of pairs. There's a big literature on kidney exchange but the source for the connection to maximum matching appears to be A. E. Roth, T. Sönmez, and M. U. Ünver, "[Pairwise kidney exchange](https://www.nber.org/papers/w10698.pdf)", _J. Econ. Th._ 2005.
If pairwise compatibility is an equivalence relation then the matching part is trivial (it's just matching in a [disjoint union of cliques](https://en.wikipedia.org/wiki/Cluster_graph)) but this framework is flexible enough to handle arbitrary non-transitive compatibility relations.

I learned of the kidney donor matching application a little too late to incorporate it into my introductory lecture on matching, so I used the other one. But next time I'll be prepared with both!

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/103705828147671738))