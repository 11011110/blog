---
layout: post
title: Report from CCCG
date: 2019-08-10 15:34
---
After [WADS]({{site.baseurl}}{% post_url 2019-08-07-report-from-wads %}), I stayed in Edmonton for [CCCG](https://sites.ualberta.ca/~cccg2019/). The two conferences have not always been in the same places, but this year they were co-located, and the plan is to continue that pattern in odd years (when WADS is held). As far as I know there are no plans to move CCCG to Scandinavia for SWAT in the even years.

Like WADS, CCCG had three invited speakers. In past years, two were named the Paul Erdős Memorial Lecture and the Ferran Hurtado Memorial Lecture. This year, sadly, the third one has also been named, as the Godfried Toussaint Memorial Lecture.

* The Erdős Lecture was by Vida Dujmović, who spoke on her breakthrough work with several other Barbados workshop participants showing that [every planar graph is a subgraph of a strong product of a path graph and a bounded-treewidth graph](https://arxiv.org/abs/1904.04791), from which it follows that these graphs have bounded [queue number](https://en.wikipedia.org/wiki/Queue_number), that they can be embedded into 3d grids of linear volume, and many other nice properties. The timing of the lecture invitation to Vida was good, as the breakthrough happened after she had already agreed to speak!

* The Toussaint Lecture was by Joseph O'Rourke. Joe spoke on [polyhedral unfolding](https://en.wikipedia.org/wiki/Net_(polyhedron)), the problem of cutting the boundary of a polyhedron into a surface that can unfold into a simple polygon in the plane. One of the points of his talk was to rationalize some of the terminology in this area. The standard version of the problem asks for (in his new terminology) an _edge-unfolding_, a set of cuts along edges of the polyhedron, forming a spanning tree for its vertices, such that the resulting cut surface unfolds to a flat polygon. But one can also ask for an anycut-unfolding, using cuts that do not have to follow the edges. Or one can ask for an edge-unzipping or anycut-unzipping, in which the cuts must form a single (Hamiltonian) path through the vertices of the polyhedron. In this terminology [Dürer's conjecture](http://www.openproblemgarden.org/op/d_urers_conjecture) becomes the statement that every convex polyhedron has an edge-unfolding, and the example I recently posted of a [zipless polycube]({{site.baseurl}}{% post_url 2019-07-29-zipless-polycube %}) shows that not every polycube has an edge-unzipping. Another well-known open question in this area asks whether every polycube whose boundary forms a topological sphere has an edge-unfolding. Joe conjectured that with high probability the convex hull of many random points on a sphere does not have an anycut-unzipping.

* Mark de Berg presented the Hurtado Lecture. His topic involved subexponential algorithms for disk intersection graphs and [unit disk graphs](https://en.wikipedia.org/wiki/Unit_disk_graph). At STOC 2018 he had a paper on [finding the maximum independent set in disk graphs](https://arxiv.org/abs/1803.10633) in time $$2^{O(\sqrt n)}$$, matching the time for planar graphs. In planar graphs, you can use the [planar separator theorem](https://en.wikipedia.org/wiki/Planar_separator_theorem): for each of the $$2^{O(\sqrt n)}$$ independent subsets of the separator, recurse on both sides. This turns out to work in disk graphs by replacing the usual size bound on the separator (it should have $$O(\sqrt n)$$ vertices) with a decomposition into a union of cliques $$C_i$$ with $$\sum\log(\vert C_i\vert+1)=O(\sqrt{n})$$. The separators can be found analogously to classical circle-packing methods for planar separators. Each clique can contribute one vertex to any independent set from which it follows that the separator again has $$2^{O(\sqrt n)}$$ independent subsets. The same idea works for other problems like dominating sets in unit disk graphs (where the unit assumption is used to get a bounded contribution from each clique), and generalizes to fat objects in higher dimensions. The time bound is optimal assuming the [exponential time hypothesis](https://en.wikipedia.org/wiki/Exponential_time_hypothesis). And in FOCS 2018 de Berg obtained similar [ETH-tight time bounds for the Euclidean traveling salesperson problem](https://arxiv.org/abs/1807.06933) by using separators of point sets with the property that few points are very close to the separator boundary.

I can't find links for all the contributed papers, but you can find them in the [complete proceedings](https://sites.ualberta.ca/~cccg2019/cccg2019_proceedings.pdf). Among them:

* In "Three-Coloring Three-Dimensional Uniform Hypergraphs", Biniaz, Bose, Cardinal, and Payne prove that, for $$n$$ points in the plane and a fixed triangle shape, one can $$3$$-color the points so that every scaled and translated copy of the triangle containing six or more points has more than one color. It was already known that if you change "six or more" to "two or more" you need four colors, and if you change it to "nine or more" you need only two colors.

* Audrey St. John's talk on "Redundant Persistent Acyclic Formations for Vision-Based Control of Distributed Multi-Agent Formations" (with Burns, Klemperer, and Solyst) was beset by technical difficulties, but from it I learned that there is a theory of directed bar-and-joint frameworks, analogous to undirected rigidity theory, called "persistence theory", and that the [pebble game]({{site.baseurl}}{% post_url 2013-12-07-kinematic-chains-and %}) for testing rigidity of an undirected framework produces an orientation of the network that is persistent. She used the analogy of a flock of geese, walking in formation: each goose pays attention only to the other geese in front, but the whole formation can keep its shape as the leading goose moves arbitrarily. Her goal is to get robots to do the same thing.

* In "Chirotopes of Random Points in Space are Realizable on a Small Integer Grid", Cardinal, Fabila-Monroy and Hidalgo-Toscano prove that, with high probability, random point sets in $$\mathbb{R}^d$$ can be rounded to a grid of polynomial size without changing their order type.

* We had enough folding and unfolding papers to spill out over more than one section. Among them, I particularly liked "Efficient Segment Folding is Hard" by Klute, Parada, Horiyama, Korman, Uehara and Yamanaka. The question they asked is: given disjoint line segments on a piece of paper, when can you make a sequence of simple folds (that is, for a given fold line, folding all the layers of the paper that are crossed by the line), with each fold on a line through one of the segments that misses all the other segments? It turns out to be $$\mathsf{NP}$$-complete. If you do allow fold lines to pass through other segments, folding sequences can be infinite, and it's unknown whether every set of segments has a finite sequence.

* Pilar Cano spoke on generating triangulations of point sets in an affine-invariant way ("Affine invariant triangulations" with Bose and Silveira). The main trick is to use covariance to choose a canonical affine transformation for the points, after which you can use Delaunay, minimum weight, or your favorite other triangulation algorithm. But there are necessarily some general position assumptions (as there already are for using Delaunay triangulation without the affine invariance): for points in a parallelogram, there is no affine-invariant way of choosing which diagonal to use.

The excursion was to the [Royal Alberta Museum](https://royalalbertamuseum.ca/), where I skipped the special exhibit on Vikings (having gone to museum exhibits on them in Copenhagen a year earlier) and instead learned much about Great Plains geology and the historical mistreatment of the [Métis](https://en.wikipedia.org/wiki/M%C3%A9tis), local people descending both from First Nations and Europeans. (The First Nations themselves were of course also badly mistreated, but I had more of an idea of that already.)

From the business meeting, we heard that the acceptance ratio was a little higher than last year, but still approximately $$75\%$$. Two papers were withdrawn because the authors had visa issues, double the number from last year, and several others were presented by non-authors after their authors were unable to attend. One possible improvement would be to move the submission and acceptance dates earlier to provide authors more time to obtain visas. The main topic of discussion was the conference's status as a conference: should papers at CCCG continue to count as publications (in which case why are they still limited to only six pages) or should they be considered as preliminary announcements of papers that can still be sent to other more prestigious symposia? One possible compromise involves giving authors a choice: either publish your paper in the proceedings or give up the proceedings slot but still present your work in some other way (possibly as a poster, as GD does).

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/102595225020207137))