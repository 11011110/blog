---
layout: post
title: Linkage from Montreal
date: 2025-07-31 14:06
---
* [3-colouring planar graphs](https://arxiv.org/abs/2507.03163) <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@DavidWood/114815217827923751)),</span> new preprint by Dujmović, Morin, Norin, and Wood showing that one can assign three colors to the vertices of any <span style="white-space:nowrap">$$n$$-vertex</span> planar graph in such a way that each monochromatic component has $$O(n^{4/9})$$ vertices, improving a previous  $$O(n^{1/2})$$ bound. The best lower bound known <span style="white-space:nowrap">is $$\Omega(n^{1/3})$$.</span>

* [Square](https://en.wikipedia.org/wiki/Square) <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/114869663672377723)),</span> now a Good Article on Wikipedia. The shape, not the algebraic operation.

* Cat in the bookshelves [again]({{site.baseurl}}{% post_url 2024-07-15-linkage-from-australia %}) <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/114878622738521637)).</span>

  {: style="text-align:center"}
![A gray cat with green eyes looks out from behind a row of books on a blue metal bookshelf, his chin resting on books that lean with his weight, and his body hidden behind the books.]({{site.baseurl}}/assets/2025/SmokeInBooks.jpg){: style="border-style:solid;border-color:black;width:100%;max-width:600px" }

* [A real-life domestic circle packing problem](https://mathstodon.xyz/@11011110/114882134838731800): arrange seven disks of diameter approximately 6.8cm in a rectangle of proportions approximately 16cm x 24cm.

  {: style="text-align:center"}
![A kitchen counter showing equipment for making espresso and orange juice: a coffee grinder, jars of coffee, scale, espresso machine, and orange juicer. Seven espresso cups, three glass and four white ceramic, are packed into a tray on top of the espresso machine. In the background are tiles with a pattern of linked circles and a shelf of blue glass bottles.](https://www.ics.uci.edu/~eppstein/pix/coffeestation/CoffeeStation-m.jpg){: style="border-style:solid;border-color:black;width:100%;max-width:600px" }

* [Optimal antimatroid sorting](https://arxiv.org/abs/2507.13994) <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/114893668280867148)),</span> new arXiv preprint by Benjamin Aram Berendsohn. For a long time I have been advocating that, for algorithmic problems involving constrained sequences, you should generalize the constraints from partial orders (an item can only be included after all its prerequisites) to antimatroids (an item can be included whenever any of multiple prerequisite sets are satisfied). This idea is not original to me: I got it from Jean-Claude Falmagne, who applied it to ordering the lessons in educational software long before he persuaded me to join his efforts.  Anyway, this preprint combines this principle with recent work on instance-optimal comparison sorting, where you want to take advantage of prior knowledge to speed up a sorting algorithm. I linked a paper on this, "[Fast and simple sorting using partial information](https://arxiv.org/abs/2404.04552)" by Haepler et al, [last year]({{site.baseurl}}{% post_url 2024-04-15-linkage %}).

  The new algorithm is again a variation of heapsort. It maintains a heap of the items that the antimatroid allows to be next in the order, and repeatedly uses the heap to find the minimum of these items and add it to the sorted order, possibly releasing more items to be next and adding them to the heap. The preprint shows that (with the same assumptions on the heap as Haeupler et al) this gives an optimal number of comparisons for the given antimatroid (whatever that optimum might be) and discusses how to implement it efficiently for various specific antimatroids. Antimatroids in turn can be generalized by greedoids; it is left as an open problem whether this algorithm and its analysis generalize.

* [Joseph Myers responds to media requests for comments on AI attempts at the International Mathematical Olympiad](https://mathstodon.xyz/@jsm28/114893210635408850).

* [Stability data for bold0mu mumu DDRawDDDDbold0mu mumu ((Raw((((bold0mu mumu CohCohRawCohCohCohCohbold0mu mumu PPRawPPPPbold0mu mumu 11Raw1111bold0mu mumu ))Raw))))](https://mathstodon.xyz/@oantolin/114888882558544362). Or, why you should listen when people advise you not to put formulas in section headings.

* [Canvas succumbs to the AI All The Things disease](https://www.chronicle.com/article/instructors-will-now-see-ai-throughout-a-widely-used-course-software) <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/114912255638012378),</span> [archived](https://archive.is/zjRtf)). Fortunately I already use Canvas as minimally as possible for my courses: they only get a landing page that tells the students to go to these other different sites for the course schedule, readings, assignments, online discussions (with real people!), and scores.

  The other reason I'm happy not to use Canvas for much is that my campus has instituted mandatory remote-access spyware as a condition for faculty access to Canvas, leading me to buy a bare-bones burner machine to be used only for spyware-restricted purposes from my office and preventing me from accessing anything they lock down like that from my home machines. Note that of course the campus has done nothing about providing funding for said burner machine. For background see [a faculty senate resolution](https://senate.universityofcalifornia.edu/_files/reports/assembly-to-president-resolution-on-trellix.pdf) to which the administration has not responded.

* [A neatly foldable rectangular framework](https://mathstodon.xyz/@robinhouston/114861548312159135) based on a 6-bar Bricard linkage

* [Brute-forcing Langley’s geometry problem with field extensions](https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/adventitious/) <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@simontatham@hachyderm.io/114874130350605831)),</span> Simon Tatham bludgeons the adventitious angle problem.

* [3d origami tessellation with raised hexagons from an equilateral triangle grid](https://pixelfed.social/p/dewibrunet/846050541012054290).

* [Why do d12 dice roll better than d20s?](https://mathstodon.xyz/@csk/114931260772358327)

* [Wikimedia brings a legal challenge to UK's Online Safety Act](https://wikimediafoundation.org/news/2025/07/17/wikimedia-foundation-challenges-uk-online-safety-act-regulations/) <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/114936859745612345),</span> [see also](https://medium.com/wikimedia-policy/wikipedias-nonprofit-host-brings-legal-challenge-to-new-online-safety-act-osa-regulations-0f9153102f29)), arguing that its identification requirements place an unacceptable risk of exposing Wikipedia editors to "data breaches, stalking, vexatious lawsuits or even imprisonment by authoritarian regimes".

* [Yao's principle](https://en.wikipedia.org/wiki/Yao%27s_principle) <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/114943454377678356))</span> is a minimax theorem equating the average-case complexity of deterministic algorithms on an input distribution that is worst-case against all deterministic algorithms, and the expected complexity of randomized algorithms on an individual input that is worst-case against that specific algorithm. Most commonly, it is used to prove lower bounds for randomized algorithms, by finding an input distribution that makes any deterministic algorithm look bad and then using the principle to argue that randomized algorithms cannot do any better. See the article for many specific applications. Now a Good Article on Wikipedia.

* [Structure of <span style="white-space:nowrap">$$k$$-matching-planar</span> graphs](http://arxiv.org/abs/2507.22395) <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@DavidWood/114945326927833766)),</span> preprint by Hendrey, Karol, and Wood on a new class of nearly-planar graphs, drawn so that for every edge $$e$$, the edges that cross $$e$$ do not include a large matching. These graphs have bounded average degree and product structure decompositions.