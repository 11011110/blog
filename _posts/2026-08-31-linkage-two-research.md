---
layout: post
title: Linkage with two research problems
date: 2026-08-31 16:24
---
In case you've been worrying that the recent publicity blitz of LLM solutions to open mathematics problems is causing us to run short, there are two more mixed in among my usual links here. Because I haven't solved them, they are not very precisely formulated, and I don't know how difficult or interesting they are nor even whether someone else might have already considered them; that's often the way at the start of research.

* I think maybe I need to start bringing my DSLR along again when I go to the beach <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/117108262940488743))</span> rather than relying on my cell phone camera (Pixel 6 Pro, yes I know it's getting old now). Here's what it thinks a crashing wave looks like, without additional processing except for a bit of a crop. To me it more resembles the kind of molded privacy glass that one uses for a bathroom window.

  {: style="text-align:center"}
![Overprocessed photo of a crashing wave]({{site.baseurl}}/assets/2026/OverprocessedWave.jpg){:  style="border-style:solid;border-color:black;background-color:black;width:100%;max-width:720px"}

* [Amazon buys rare books to destructively scan them for AI training](https://www.404media.co/we-tracked-a-shipment-of-rare-books-it-ended-at-an-amazon-ai-training-facility/) <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@johncarlosbaez/117111373092143051)).</span>

* [An abbreviation of abbreviation, misspelling of misspelling, and more of the kind](https://wikis.world/@depthsofwiktionary/117096718248310681) from the depths of Wiktionary.

* [Rotating points on four circles form a polygon of constant length](https://mathstodon.xyz/@JimPropp/117117710043800216) by Jim Propp, inspired by [Chuck Hoberman's "Nested Loops" exhibit at the Museum of Mathematics](https://www.youtube.com/watch?v=e4sARevLYJA).

* [A cursed triangle](https://mas.to/@428/117109514953494212) in the [Moulton plane](https://en.wikipedia.org/wiki/Moulton_plane).

* If you've been working with tagged pdf files in Adobe Acrobat <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/117140732416380434)),</span> you may have noticed an annoying banner that it displays at the top of the window whenever it opens a tagged pdf file: "This file claims compliance with the PDF/A standard and has been opened read-only to prevent modification". If this banner were only in the default view of Acrobat it might be more easily ignored, but it has no checkbox to make it go away and remains visible even in presentation mode (like, if you're trying to present a lecture using a tagged pdf file). The only obvious way to make it go away is to click a button labeled "enable editing", which you might think you don't want to do.

  [It turns out that you can disable these banners entirely](https://
bwsd.wordpress.com/2025/06/14/remove-this-file-claims-compliance-with-the-pdf-a-standard-banner-from-adobe-acrobat/). In the preferences window for Acrobat, go to the "Documents" page and change the setting for "PDF/A View Mode" from "Only for PDF/A documents" to "Never". I suspect that this also disables the automatic read-only setting for these files but I don't think that's a problem.

* [Editorial board of _Games and Behavior_, the journal of the Game Theory Society, resigns](https://gametheorysociety.org/message-from-herve-moulin-geb-editor/) <span style="white-space:nowrap">([$$\mathbb{M}$$](https://fediscience.org/@fortnow/117142004895290206)),</span> after its publisher Elsevier replaces its editor-in-chief without consultation with the board, for "closer alignment with Elsevier strategic priorities". The link leads me to wonder: where is the involvement of the society itself in these decisions?

* I created this image over a year ago for my CCCG 2025 talk "[Decremental greedy polygons and polyhedra without sharp angles](https://
ics.uci.edu/~eppstein/pubs/p-decremental.html)" <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/117157302983232987)),</span> but I don't think I posted it (or the talk slides) online until now. This is what you get from the following process: start with the infinite set of integer points in the positive quadrant, and then repeatedly clip off the point that makes the sharpest angle on the convex hull. As you do this, at certain points you will reach curves for which the sharpest angle is less sharp than for any earlier curve; those are the ones shown in blue. The yellow quarter-circle is added separately for comparison.

  {: style="text-align:center"}
![A 172x172 corner of the integer grid in the positive quadrant, with blue curves showing the grid polygons whose sharpest angle is less sharp than all the curves below them. The grid is overlaid with a radius-171 yellow quarter-circle closely matching the shape of the innermost blue curve.]({{site.baseurl}}/assets/2026/quarterplane-clipping.svg){:  style="background-color:white;width:100%;max-width:720px"}

  ***Research problem 1:*** I don't understand why the blue curves are so irregularly spaced nor why some of them appear so visually close to quarter-circles. Explain?

* [Physics papers are written in LaTeX](https://www.
youtube.com/watch?v=KhWwuQ7qf5A) <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/117164959072134948)),</span> video by Angela Collier. I doubt anyone here doesn't already know all this, but it's a good explainer of why researchers in mathematics/physics/theoretical computer science/linguistics etc. almost universally prefer LaTeX to Word, how the two differ, and why you can infer that a paper in Word was probably not written by a professional. Also with an entertaining rant about why Word is bad, how it's getting both worse and more expensive, and why you should not pay for it.

* [Digit Party: Three years of lying about high scores](https://doi.org/10.1080/10724117.2026.2675898) <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@VinceVatter/117157819125658014)),</span> and how authors Robert Brignall and Vince Vatter switched to integer linear programming in order to finally compute exact high scores for [their online digit-clustering puzzle, digit.party](https://digit.party/).

* [A set of five 60-sided go-first dice](https://
wire.auburn.edu/content/ocm/2026/08/08141416-eric-harshbarger-dice.php) <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/117175466021416824),</span> [via](https://
boingboing.net/2026/08/28/fountain-pen-go-first-dice.html)), found in 2023 by Paul Meyer through efforts coordinated by Auburn University lecturer Eric Harshbarger. These are five dice, labeled so that no two include the same numbers, with equal probabilities of rolling the highest number in all combinations of up to five dice. More strongly [Wikipedia states that these dice are "permutation fair"](https://
en.wikipedia.org/wiki/Go_First_Dice): each permutation of the rolling players is equally likely. Now their discovery is commemorated by a giant set of these dice installed in the Auburn University STEM + Agricultural Sciences Complex.

* [Tsuidoku](https://
tsuidoku.com/) <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/117181324283502155)),</span>a sudoku variant in which you must fill in the usual 9x9 sudoku grid with both nine digits and nine colors, and must end up with one of each digit-color combination.

  To me the biggest drawback is that the solved puzzles tend to have a stripy pattern like the patterns visible in the [sudoku grids packed with 3x3 Latin squares from my recent blog post]({{site.baseurl}}{% post_url 2026-07-07-packing-latin-squares %}) (both in their colors and digits) and when you detect this pattern it makes the puzzle much easier to solve. Also I'm not a fan of the style of gameplay that announces your mistakes immediately and lets you correct them; I think it makes puzzles trickier (and therefore more interesting) when you have to figure out that you've made a mistake yourself and undo back to where you made it. I checked that the nine colors appear distinguishable under the most common form of color blindness (at least to my normal vision eyes using a simulator) but their color contrast was not great, and there are three pairs of indistinguishable colors under blue-blind color blindness (tritanopia).

  All that said, I think the higher levels are tricky enough to be interesting. And (***research problem 2***) I am intrigued by the question of whether the stripiness is an implementation flaw or a necessary emergent feature of these game rules at this board size.

* [Video on the motion and rigidity of hyperboloids made from sticks](https://youtu.be/CJCL92W8Z9w) <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@henryseg/117179099074922279)),</span> by Sabetta Matsumoto, Tim Reinhardt, Jürgen Richter-Gebert, and Henry Segerman, in part centered on a large public artwork with this form, [Mae West](https://en.wikipedia.org/wiki/Mae_West_(sculpture)) in Munich.

* [Hyperchoreography](https://lycium.github.io/hyperchoreography/) <span style="white-space:nowrap">([$$\mathbb{M}$$](https://mathstodon.xyz/@RefurioAnachro/117189814134094236)),</span> solutions for $$n$$-body problems in more than three dimensions.