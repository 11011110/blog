---
layout: post
title: Congratulations, Dr. Afshar!
date: 2023-02-17 16:06
---
Ramtin Afshar, a doctoral student in the UC Irvine Center for Algorithms and Theory of Computation advised by Mike Goodrich, passed his defense today, becoming Mike's 25th completed doctoral student. Ramtin's dissertation, _Exact Learning of Graphs from Queries_, was based on papers from [ESA 2020](https://doi.org/10.4230/LIPIcs.ESA.2020.3), [LATIN 2022](https://doi.org/10.1007/978-3-031-20624-5_18), and [STACS 2022](https://doi.org/10.4230/LIPIcs.STACS.2022.4), all of which involved asking questions to find out the structure of an unknown graph.

A possibly familiar example here is the [traceroute](https://en.wikipedia.org/wiki/Traceroute) program, used to debug internet connections by finding a path from one networked computer to another. It uses a feature of internet protocols that allow packets to "time out" if they make too many hops, returning an error message back to the originating computer when they do. By setting the timeout to a parameter $$k$$, you can force the timeout to happen at the <span style="white-space:nowrap">$$k$$th</span> step of a shortest path to another computer, and by doing so find out who is at that <span style="white-space:nowrap">$$k$$th</span> step. You might think that you would need to trace the routes between all pairs of computers on the network to find out where its edges are (and this does work, with a quadratic number of <span style="white-space:nowrap">$$k$$th-step</span> queries), but Ramtin and his coauthors (Goodrich and two other UCI students, Pedro Matias and Martha Osegueda) showed that with some natural assumptions on the network topology, only a near-linear number of queries is needed.

Beyond the papers used in his thesis, Ramtin is a coauthor on more papers in [SPIRE 2020](https://doi.org/10.1007/978-3-030-59212-7_12) on related problems of string reconstruction, in [SPAA 2020](https://doi.org/10.1145/3350755.3400229) on reconstructing evolutionary trees or other binary trees, and in [SEA 2022](https://doi.org/10.4230/LIPIcs.SEA.2022.9) on learning road maps from shortest path hop counts. His traceroute work in STACS 2022 was also the subject of a brief announcement at [SPAA 2021](https://doi.org/10.1145/3409964.3461822).

His next step is to work for Google in the San Francisco Bay Area, involving a temporary two-body problem while his wife finishes her own studies at the University of Southern California.

Congratulations, Ramtin!