---
layout: post
title: The metro map metaphor for treewidth
date: 2025-09-04 01:01
---
Harry Beck's [1931 map of the London Underground transit system](https://www.ltmuseum.co.uk/collections/stories/design/transforming-tube-map-harry-becks-iconic-design) has been justly heralded. It abstracted the messiness of above-ground geography into simple lines in restricted directions and made a complex system visually understandable. Since Beck's breakthrough, metro maps around the world have followed similar styles.

The same style can work for many other kinds of visualization as well. Already in 2001 researchers were introducing "metro maps as metaphors" for links between web pages, again thought of as a system that one navigates from stop to stop.[^web] By 2004 the idea had expanded to the summarization of complex documents such as theses, business plans, and course syllabi.[^abs] More abstract structures to which this idea has been applied include set systems and hypergraphs.[^set] Google Scholar currently gives my some 618 results for a search with the terms "metro map" and "metaphor".

In many of these early maps, the lines of the abstract metro system all run along distinct paths, but in Beck's 1931 map some lines ran parallel for short distances or, in the case of the District and Picadilly lines, for much of their lengths. The idea of using this sort of parallelism in abstract metro map visualizations was given a big boost by the 2009 xkcd "[Movie Narrative Charts](https://xkcd.com/657/)" visualization of character interaction timelines in _The Lord of the Rings_, _Star Wars_, and some other films.

{: style="text-align:center"}
![Movie Narrative Charts, from https://xkcd.com/657/. As stated in the image, "These charts show movie character interactions. The horizontal axis is time. The vertical grouping of the lines indicates which characters are together at a given time."]({{site.baseurl}}/assets/2025/xkcd-657.png)

Real-world metro maps have crossings where the metro lines cross, of course; that can't really be controlled. But where lines run in parallel bundles, and then diverge, you can also have crossings at the points of divergence that may or may not be necessary. This depends on how the lines are ordered within each parallel bundle, and graph drawing researchers have studied how to optimize this ordering to minimize crossings.[^cross]

One of the latest entrants in this long line of abstract metro map research is my new preprint "[Visualizing treewidth](https://arxiv.org/abs/2508.19935)", with Alvin Chiu, Thomas Depian, Michael T. Goodrich, and Martin Nöllenburg, to appear at _Graph Drawing_. As the title suggests, the abstract structure we're visualizing is a [tree decomposition](https://en.wikipedia.org/wiki/Tree_decomposition). This can be thought of in terms of a metro map for a metro system whose overall structure looks like a tree, without loops (unlike even 1931-era London). The vertices of the graph form the lines of the metro map, connecting from station to station in parallel bundles along the edges of this tree, with some lines having internal branches rather than just being a path (as the 1931 District and Picadilly lines did). The stations of the map are called "bags" in tree decomposition terminology; these are where certain pairs of these vertices interact to form edges, but two vertices can also pass through a station without interacting with each other. Therefore, we need to go beyond the metro map metaphor and draw some additional structure within each station, showing which pairs of lines have edges and which do not.

Here's a simple example, from Figure 2 of the preprint, showing a conventional node-link diagram of a graph above a metro-map style diagram of one of its tree decompositions. Each of the seven stations of the metro map (the bags of the decomposition) has a graph drawn within it, the induced subgraph of the vertices whose lines pass through that station. Some lines visit only one station and are drawn only as a vertex within that station. The width of a decomposition is the maximum number of lines per station (minus one, for historical reasons); here the width is three because all seven stations have four lines running through them. This is an optimal tree decomposition: the four central vertices of the graph form a clique and must be present together in at least one station. Therefore the treewidth of this graph is also three.

{: style="text-align:center"}
![A graph with ten vertices, drawn in standard node-link diagram style, with each vertex given a different color, and a metro-map style visualization of its tree decomposition, with seven stations (bags), and with each vertex shown as a metro line in its color. The graph diagrams within each bag are the induced subgraphs of the vertices whose lines pass through that station."]({{site.baseurl}}/assets/2025/metro-tree-decomp.svg)

For several variations on this drawing style and many more examples, including tree decompositions of several famous graphs, see the new paper.

* Footnotes go here
{:footnotes}

[^web]: Sandvad, Grønbæk, Sloth, and Knudsen (2001), "[A metro map metaphor for guided tours on the web](https://doi.org/10.1145/371920.372079)", _WWW_; Bang (2001), "[Knowledge sharing in a learning resource centre by way of a metro map metaphor](https://files.eric.ed.gov/fulltext/ED459765.pdf)", _Libraries and Librarians: Making a Difference in the Knowledge Age_, both reporting on a system in use at the University of Aarhus.

[^abs]: Nesbitt (2004), "[Getting to more abstract places using the metro map metaphor](https://doi.org/10.1109/IV.2004.1320189)", _Int. Conf. Inf. Vis._

[^set]: Jacobsen, Wallinger, Kobourov, and Nöllenburg (2020), "[MetroSets: Visualizing sets as metro maps](https://doi.org/10.1109/TVCG.2020.3030475)", _TVCG_; Frank et al. (2021), "[Using the Metro-Map Metaphor for Drawing Hypergraphs](https://doi.org/10.1007/978-3-030-67731-2_26)", _SOFSEM_.

[^cross]: Bekos, Kaufmann, Potika, and Symvonis (2007), "[Line crossing minimization on metro maps](https://doi.org/10.1007/978-3-540-77537-9_24)", _Graph Drawing_; Nöllenburg (2009), "[An improved algorithm for the metro-line crossing minimization problem](https://doi.org/10.1007/978-3-642-11805-0_36)", _Graph Drawing_; Argyriou, Bekos, Kaufmann, and Symvonis (2010), "[On metro-line crossing minimization](https://doi.org/10.7155/jgaa.00199)", _JGAA_; Fink and Pupyrev (2013) "[Metro-line crossing minimization: Hardness, approximations, and tractable cases](https://arxiv.org/abs/1306.2079)", _Graph Drawing_.