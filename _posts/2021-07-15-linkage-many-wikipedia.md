---
layout: post
title: Linkage with many Wikipedia Good Articles
date: 2021-07-15 18:02
---
There are two reasons for the large number of Good Articles in this set. First, I had previously been trying to keep my nominations and reviews in balance, but there were too few nominations to review on topics of interest to me, and the inability to find things to review was preventing me from nominating other articles when they were ready. So I started nominating more often. And second, the Wikipedia Good Articles editors are having a drive this month to clean out old nominations, as they tend to do a couple of times per year.

* [Morphing fractal engraving vice jaws](https://www.thisiscolossal.com/2021/07/steve-lindsay-fractal-vise/) ([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/106506737270461558)). Circular arcs nested within circular arcs rotate to conform to whatever shape is being gripped.

*  Christian Lawson-Perfect sets up a new wiki, [Why start at $$x,y,z$$?](https://whystartat.xyz) ([$$\mathbb{M}$$](https://mathstodon.xyz/@christianp/106500170446647463)). Its aim is to collect ambiguous, inconsistent, or just plain unpleasant conventions in mathematical notation. My contribution: [big O notation](https://whystartat.xyz/wiki/Big_O_notation).

* [Pick's theorem ](https://en.wikipedia.org/wiki/Pick%27s_theorem) ([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/106523554824974108)). The area of a grid polygon equals its number of interior grid points, plus half the boundary points, minus one. Good Article #1.

* [The problem with combinatorics textbooks](https://igorpak.wordpress.com/2021/07/03/the-problem-with-combinatorics-textbooks/) ([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/106526891677914307)). Igor Pak on the difficulty of teaching combinatorics in a comprehensive way in a single term. Instead, he suggests teaching courses on narrower subtopics: "the more specific you make the combinatorics course the more interesting it is to the students".

* I recently returned from a relaxing early-long-weekend mini-vacation to Avila Beach ([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/106532239057852428)), with seafood sunset beach dinners (the coast faces south so the sun sets over land), wine tasting (near the setting of Sideways), and sulphur springs hot tub soaks. The photo below is a garden in a field of rusted pylons in the flood basin of San Luis Obispo Creek. I liked its contrast of natural growth and regular artificial forms.

  {: style="text-align:center"}
![Secret garden, Sycamore Springs Resort, Avila Beach](https://www.ics.uci.edu/~eppstein/pix/sycsprings/SecretGarden-m.jpg){: style="border-style:solid;border-color:black;"}

* [Viète's formula](https://en.wikipedia.org/wiki/Vi%C3%A8te%27s_formula) ([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/106535094271822431)), an infinite product of nested roots evaluating to $$2/\pi$$, "the first formula of European mathematics to represent an infinite process". Good Article #2.

* [The _New York Times_ on Erik and Marty Demaine's mathematical typefaces](https://www.nytimes.com/2021/06/25/science/puzzles-fonts-math-demaine.html) ([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/106545874983076062), [also](https://archive.ph/oJ8xG), [via](http://stormbear.com/carnival-of-mathematics-195-july-2021/)). 

* [Euclid–Euler theorem](https://en.wikipedia.org/wiki/Euclid%E2%80%93Euler_theorem) ([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/106554476459806645)). A 2-millenium-long collab in which Euclid proved that all Mersenne primes produce even perfect numbers, and Euler proved that all even perfect numbers come from Mersenne primes. But let's not forget [Ibn al-Haytham](https://en.wikipedia.org/wiki/Ibn_al-Haytham) (Alhazen), halfway between them in time, who conjectured Euler's result but couldn't prove it. Good Article #3.

* [Lyusternik's book _Convex Figures and Polyhedra_](https://mirtitles.org/2021/07/07/convex-figures-and-polyhedra-lyusternik/) ([$$\mathbb{M}$$](https://mathstodon.xyz/@jarban/106551202604578180)), one of the Mir translations from Russian to English, [available without restrictions on archive.org](https://archive.org/details/lyusternik-convex-figures-and-polyhedra).

* [Bucket queue](https://en.wikipedia.org/wiki/Bucket_queue) ([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/106570282017522543)). This priority queue is a bit out of fashion, but good for small integer priorities or for shortest paths when the ratio of longest to shortest edge is small. Good Article #4, despite a reviewer who had [somehow become convinced that deletion from doubly linked lists is nonconstant](https://en.wikipedia.org/wiki/WP:CHEESE). The issue is off-topic but real: updating objects in data structures often needs the objects to track their location in the structure; for instance, changing priorities in a binary heap requires each object to know its index. Most introductory material on these topics and even some standard library implementations (like Python's heapq) fail to address this complication.

* [Formalizing 100 theorems](https://www.cs.ru.nl/~freek/100/) ([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/106579903443188306)). Freek Wiedijk uses a rather arbitrary collection of 100 favorite theorems from some 1999 web page as a benchmark set for the progress of automatic proof assistants. I'm sad that Pick's theorem has seen so little love.

* [Greedy spanners in Euclidean spaces admit sublinear separators](https://arxiv.org/abs/2107.06490) ([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/106583477388316730)). My [SoCG'21 result with Hadi Khodabandeh that 2d greedy spanners have separators of size $$O(\sqrt{n})$$]({{site.baseurl}}{% post_url 2020-02-17-spanners-have-sparse %}) used crossing-based methods heavily dependent on planarity. This new preprint by Hung Le and Cuong Than uses different ideas to find separators of size $$O(n^{1-1/d})$$, optimal in any dimension $$d$$. Their work also extends from Euclidean spaces to doubling spaces.

* [Unique distancing](https://oscarcunningham.com/670/unique-distancing-problem/) ([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/106587574216525670)). How many points can you place in an $$n\times n$$ grid so that all pairwise distances are distinct? The linked post concerns whether $$n$$ points are possible (no for all but finitely many cases because there are too many pairs and too few sums of squares) but it also looks interesting to maximize the number of points.