---
layout: post
title: Year-end linkage
date: 2019-12-31 21:23
---
* [Reign in graphs](https://www.shapeways.com/shops/jankrhaugland) ([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/103321651787290257)). Interesting collection of 3d models of graphs

* [Zentralblatt going open access](https://euro-math-soc.eu/news/19/12/17/zbmath-become-open-access) ([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/103324328632714865)). I mostly use a mix of Google Scholar (for searching), MathSciNet (for more targeted searches, reviews, and high-quality bibtex), and DBLP (for bibtex of CS papers not in MathSciNet) but maybe this will convince me to add ZB into the mix.

* [Christian Lawson-Perfect can't explain why the Wikipedia article for "Author" was illustrated by a Ukrainian copyright certificate for a supposed proof of Fermat's last theorem](https://mathstodon.xyz/@christianp/103328394093228909). It seems to have been added in good faith there, but maybe as self-promotion to the "Copyright" article. Whatever, it's now on "[Pseudomathematics](https://en.wikipedia.org/wiki/Pseudomathematics)" where it belongs.

* [Xor filters](https://lemire.me/blog/2019/12/19/xor-filters-faster-and-smaller-than-bloom-filters/) ([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/103338548071725282), [preprint](https://arxiv.org/abs/1912.08258), [via](https://news.ycombinator.com/item?id=21840821)): A new alternative to Bloom filters and cuckoo filters for approximate set membership with a controlled rate of false positives and no false negatives. It's fast and (for realistic error rates) uses fewer bits than Bloom or cuckoo. Cuckoo still wins if you need your sets dynamic, though: you can insert or delete elements easily, while Bloom can only insert and xor can't handle any change.

* [Visualizations of several maze-generation algorithms](https://www.jamisbuck.org/mazes/) ([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/103349055666314448), [via](https://news.ycombinator.com/item?id=21828903)). They all appear to generate random tree-like mazes in a square grid, but with different probability distributions on the trees. E.g. Kruskal and Prim generate minimum spanning trees for random weights, different from the uniformly random trees of Aldous–Broder and Wilson, and many others appear quite different from both.
The alternative algorithm at the main link of the via link is probably not the best choice.

* [It's easy for mathematical physics crackpottery to get published in a prestigious-sounding pay-to-publish journal from an actually-prestigious publisher, _Nature Scientific Reports_](https://twitter.com/johncarlosbaez/status/1208768265830354945) ([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/103355963066100289)).
In the ensuing discussion, Flavio Nogueira reports that [editors rejected papers only to see them published anyway](https://twitter.com/F_S_Nogueira/status/1208787145911152640). Should we start treating _Nature_ as a predatory publisher?

* [Convex hull of a simple polygon](https://en.wikipedia.org/wiki/Convex_hull_of_a_simple_polygon) ([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/103360225573578914)). I've been working on cleaning up Wikipedia's main convex hull article (not yet finished) and added this one to fill in some details. The problem has an interesting history: it's been known to be solvable in linear time since 1979, and many different algorithms for the same problem have been published before and since, but most of them are wrong.

* [Open convex hull of a closed set](https://mathoverflow.net/q/349228/440) ([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/103365014241600450)). I can prove that (in Euclidean spaces) such sets are always Cartesian products of a line with a lower-dimensional set. But is there a reference in the literature for this, so I can add it to the Wikipedia article? If you know, please leave an answer on the MathOverflow link.

* [David Bachman, Saul Schleimer and Henry Segerman finally explain what their cohomology fractals are](https://youtu.be/fhBPhie1Tm0) ([$$\mathbb{M}$$](https://mathstodon.xyz/@henryseg/103341309414601843)).

* [Turkish supreme court rules that the country's two-year block on Wikipedia is unconstitutional](https://www.theguardian.com/world/2019/dec/26/turkish-court-wikipedia-block-lifted) ([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/103378814260578782), [also](https://news.ycombinator.com/item?id=21888759), [also](https://www.washingtonpost.com/world/europe/court-rules-turkey-violated-freedoms-by-banning-wikipedia/2019/12/26/880f263c-27de-11ea-9cc9-e19cfbc87e51_story.html), [also](https://www.nytimes.com/2019/12/26/world/europe/wikipedia-ban-turkey.html)).

* [Famous fluid equations spring a leak](https://www.quantamagazine.org/mathematician-makes-euler-equations-blow-up-20191218/) ([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/103384319532164607)). We still don't know whether the differential equations governing fluid flow lead to consistent and unique solutions for all time. But if you simplify the equations to throw away viscosity and compressability, and you allow the initial state of the fluid to have discontinuous boundaries between volumes of fluid with very different motion, you can cause it to reach a point at which it spins infinitely quickly.

* [Relative convex hull](https://en.wikipedia.org/wiki/Relative_convex_hull) ([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/103390220528024772)). Another new article related to my revision of the Wikipedia convex hull article. These are the shapes you get by stretching a rubber band around one set while fencing it inside a polygon. You don't always get a simple polygon as a result, but it's "weakly simple".

* [Science under attack: How Trump is sidelining researchers and their work](https://www.nytimes.com/2019/12/28/climate/trump-administration-war-on-science.html) ([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/103393997740330853)). The fact that this link was [flagged and censored from ycombinator hacker news](https://news.ycombinator.com/item?id=21905957) is also interesting, in its own way. Fortunately my RSS aggregator copied the link before it was taken down.

* [Are reputation management operatives scrubbing Wikipedia articles](https://en.wikipedia.org/wiki/Wikipedia:Wikipedia_Signpost/2019-12-27/Special_report) ([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/103399857216270322)). Answer: duh. The linked report has details of one such case, involving Theranos.

* [New open-access journal _Compositionality_](https://johncarlosbaez.wordpress.com/2019/12/30/compositionality-first-issue/) ([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/103406379623694356)), on the mathematics of "how complex things can be assembled out of simpler parts". It's not a good fit for my own research, and the word "fuzzy" in the title of one of the initial papers is kind of a red flag for me, but I think it's a good thing that the move towards diamond-model open access is continuing.