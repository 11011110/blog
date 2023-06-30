---
layout: post
title: Linkage from a holiday-weekend road trip
date: 2023-06-30 16:24
---
* Talk slides for my talks at the recently-concluded Symposium on Computational Geometry and its satellite Workshop on Parameterized Algorithms for Geometric Problems <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/110556766029657315)):</span>

  * [Non-crossing Hamiltonian paths and cycles in output-polynomial time](https://www.ics.uci.edu/~eppstein/pubs/Epp-SoCG-23.pdf)

  * [Widths of geometric graphs](https://www.ics.uci.edu/~eppstein/pubs/Epp-WPAGP-23.pdf)

  The sessions were streamed on YouTube but as one big stream rather than separate talks. They are not yet public but the organizers have been working to get permissions for that.

* A topic of some discussions at SoCG this year <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/110556766029657315))</span> was the extent to which SoCG's lack of affiliation with a big society like ACM or IEEE has hurt researchers at institutions whose administrators look for quick and dirty indicators of respectability instead of examining the actual output and impact of those researchers. [Meanwhile, on Retraction Watch](https://retractionwatch.com/2023/06/15/plague-of-anomalies-in-conference-proceedings-hint-at-systemic-issues/): "Hundreds of conference papers published by the IEEE show signs of plagiarism, citation fraud and other types of scientific misconduct ... it indicates systemic issues with their peer review systems. ... IEEE keeps publishing proceedings riddled with tortured papers and other anomalies."

* Today's inexplicable referee comment <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/110567649831757567)):</span> "The References are too long and some are extremely long(!) Sometimes the authors cite many versions of the same paper in the same citation. Who needs all these details to find the paper?" This is for references formatted in the very basic plainurl style by bibtex, using almost-unchanged metadata from DBLP. The only thing resembling "many versions of the same paper" that I can see is that in two references I also included an arXiv link. I think the only other changes I made were to replace some hyphens by en-dashes.

* From the _Mathematical Intelligencer_: "[F things you (probably) didn’t know about hexadecimal](https://link.springer.com/article/10.1)" <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@leonardopacheco/110548901932435519)).</span>

* 1e-5 Schrafreiterstr., possibly [Munich's smallest house number](https://mathstodon.xyz/@murphy@troet.cafe/110568762075574488).

* [Éva Tardos wins 2023 Knuth Prize](https://news.cornell.edu/stories/2023/06/tardos-honored-2023-knuth-prize) <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/110594893943827297)).</span>

* "[All the ways to close a cardboard box](https://ww.closky.info/?p=126)" <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@markgritter/110601180810620076)),</span> by Claude Closky, an artist who takes care to get the combinatorics correct.

* The kittens have discovered that the kitchen bay window makes a nice sunny warm spot in the mornings <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/110613797453300598)).</span>

  {: style="text-align:center"}
![Two gray kittens lurk behind fresh basil, tomatoes, and garlic in a kitchen bay window decorated with blue glass bottles](https://www.ics.uci.edu/~eppstein/pix/kwk/KitchenWindowKittens-m.jpg){: style="border-style:solid;border-color:black" }

* [Official DOI shortener](https://shortdoi.org/) <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@peterrowlett/110610915309165007)),</span> Because if you're going to put cryptic non-transparent addresses in your references section, and you still want them to look like official DOIs, [doi:10/c257zs](https://doi.org/c257zs) is much better than [doi:10.1002/(SICI)1097-0037(200005)35:3<173::AID-NET1>3.0.CO;2-W](https://doi.org/10.1002/(SICI)1097-0037(200005)35:3%3C173::AID-NET1%3E3.0.CO;2-W).

* [17-animal inheritance puzzle](https://en.wikipedia.org/wiki/17-animal_inheritance_puzzle) <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/110631632114617893))</span> is now a Wikipedia Good Article. The same sort of problem, in which indivisible elements must be subdivided into fractions that don't fit the number of elements, also comes up all the time in elections with proportional representation. So instead of trying to divide 17 camels among three brothers, one might try to divide the 17 parliamentary seats of Gibraltar or of Antigua among three political parties. The [2023 Antigua election](https://en.wikipedia.org/wiki/2023_Antiguan_general_election) came close to the same subdivision as the one used in the inheritance puzzle.

* [Randomized acceptances](https://blog.computationalcomplexity.org/2023/06/randomized-acceptances.html) <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/110635278051683167)).</span> Problem: for the middle range of submissions to conferences or journals, acceptance is arbitrary and has high variance depending on which reviewers one is assigned. Solution (?): recognize that fact and replace the decision process in this range with something that is guaranteed to be arbitrary and have high variance: a random coin flip.

* Related to the entry above on the 17 camels, here's another example of two integer sequences that look the same for quite a few terms before diverging <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/110635717355858781)).</span> The two integer sequences [A085493](https://oeis.org/A085493) (these are the numbers that could replace 17 in the camel puzzle) and [A005153](https://oeis.org/A005153) (practical numbers) appear to differ from each other by one, but that pattern breaks after the first 20 or so numbers.

  $$69$$ is the smallest number $$n$$ with the following combination of properties:

  * It can be written as a sum of distinct divisors of $$n+1$$: $$69 = 1 + 2 + 7 + 10 + 14 + 35$$

  * Some smaller number  cannot be written as a sum of distinct divisors of $$n+1$$: there is no way of writing $$4$$ as a sum of distinct divisors of $$70$$

  So $$69$$ belongs to A085493 (it is a camel number) but $$69+1$$ does not belong to A005153 (it is not practical).