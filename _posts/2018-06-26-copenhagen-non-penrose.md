---
layout: post
title: Copenhagen and the non-Penrose pentagonal paving
date: 2018-06-26 13:56
---
Copenhagen is a city of oddly-shaped spires, but if you look down you might also see something interesting.

{: style="text-align:center"}
![Amagertorv, Copenhagen](http://www.ics.uci.edu/~eppstein/pix/copenhagen/Amagertorv-m.jpg){: style="border-style:solid;border-color:black;"}

This is [Amagertorv](https://en.wikipedia.org/wiki/Amagertorv), one of Copenhagen's central squares, famous for its [Stork Fountain](https://en.wikipedia.org/wiki/Stork_Fountain). Bjørn Nørgaard's pavement design, a bit covered in grime after 25 years, is also interesting, with paving stones arranged in neat regular pentagons. When I saw this, I had recently read of [Helsinki's Penrose-tiled pavement](https://plus.google.com/100003628603413742554/posts/LLTz5yRgcnA) and was excited to think that maybe there was a rival Penrose-tiled nordic capital. Could the Amagertorv tiles also be a Penrose tiling? Sadly, no.

The pattern of the tiles becomes clearer if one looks at them from above, say in Google maps' satellite view.

{: style="text-align:center"}
![Amagertorv, satellite view from Google maps]({{site.baseurl}}/assets/2018/Amagertorv-from-Google-maps.jpg)

We can already see that the tiling is not aperiodic, but is it necessarily so?
Or maybe the same stones could have been rearranged somehow to form a Penrose tiling? Still, the answer is no.

The paving stones consist of dark triangles and light spacers that, together, form regular pentagons, red stones that form $$36^\circ$$–$$144^\circ$$ rhombi (usually called "diamonds" in the context of Penrose tiling), and several other smaller stones that connect them together into a seamless pavement.

{: style="text-align:center"}
![Pentagon-diamond tiling with 5-way dihedral symmetry]({{site.baseurl}}/assets/2018/Amagertorv.svg)

The smaller connecting stones force the dark-light pentagons and red diamonds to meet at only two types of vertex: a degree-four vertex with three pentagons and the sharp corner of a diamond, and a degree-three vertex with two pentagons and the acute corner of a diamond.

The Penrose tilings include two tilings with five-fold dihedral symmetry. If we try to replicate the same symmetry with these regular pentagons and diamonds, we must put a pentagon in the center, adjacent to five other pentagons. But once these choices have been made, the whole tiling is fixed: the remaining tiles must spread out in five periodically-tiled wedges from the center, as I have shown above. By leaving a hole at the center of symmetry (covered with the Stork Fountain), Nørgaard found a different symmetric solution, with ten narrower periodically-tiled wedges, but I think this only has cyclic symmetry and not dihedral symmetry. (That is, it is slightly different from its mirror reflection, and so has only the same total number of symmetries as the five-fold tiling.) Because the pentagon and diamond tiles (with their two types of constrained vertices) have no symmetric but aperiodic tiling, they cannot be made to form arbitrary Penrose tilings.

{: style="text-align:center"}
![Pentagon-diamond tiling with 10-way cyclic symmetry and a central hole]({{site.baseurl}}/assets/2018/StorkFountain.svg)

For more from Copenhagen, see [my online gallery](https://www.ics.uci.edu/~eppstein/pix/copenhagen/), including the glowing nostrils of [Gefjon's oxen](Gefion Fountain), a [Nine Men's Morris](https://en.wikipedia.org/wiki/Nine_Men%27s_Morris) board built into the corner of the city hall, and an engraving of a Danish king of whom all but the head has been transformed into calligraphy.
