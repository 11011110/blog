---
layout: post
title: Vertex-free flat folding
date: 2018-06-22 23:21
---
The diagram below shows an origami folding pattern for a sheet of triangular paper. The internal segments of the triangle should all be folded, but I haven't specified whether they should be mountain folds or valley folds. This diagram is unusual among origami folding patterns, not only for the shape of the paper, but for the fact that all of the creases go all the way across the paper without crossing each other or terminating at a vertex (a point interior to the paper where multiple creases meet).
We know how to tell whether a folding pattern with a single vertex (and no other creases) is foldable, using [Kawasaki's theorem](https://en.wikipedia.org/wiki/Kawasaki%27s_theorem) and [Maekawa's theorem](https://en.wikipedia.org/wiki/Maekawa%27s_theorem).
And when there is more than one vertex, [flat foldability is NP-complete](http://portal.acm.org/citation.cfm?id=313852.313918).
But what about when there are zero vertices, like in this example?

{: style="text-align:center"}
![Triangular vertex-free impossible folding pattern]({{site.baseurl}}/assets/2018/unfoldable-triangle.svg)

In the case of this diagram, it turns out to be impossible. No matter how you choose which of the creases should be mountain folds, and which should be valley folds, and no matter which creases you fold above which other ones, you will not be able to use all the creases shown (and only the creases shown) and make it fold flat.

If the diagram could fold flat, two of its three big triangular flaps would have to be on the same side of the central equilateral triangle. But when this happens, the two flaps get in each other's way, so that they can't both be folded flat.
If the more clockwise of the two flaps were folded closer to the central triangle, its obtuse shoulder would lie across the crease of the other flap, blocking it from folding. And if the counterclockwise flap were folded closer to the central triangle, its sharp tip would (after folding the crease separating the tip from the flap) again lie across the crease of the other flap, blocking it from folding. So no flat folding is possible.

On the other hand, I have a proof (too inelegant for this <s>margin</s> blog post) that for square or circular paper, every vertex-free folding pattern (without a preassigned mountain-valley assignment) can be flat-folded.

I think it would be interesting to characterize more generally which shapes of paper have this property, that all vertex-free patterns are flat-foldable, but it seems difficult. It's not only about the fact that the equilateral triangle has acute angles (although that seems to be important), for instance, because you could trim the corners of the diagram above and get a 120-degree hexagon folding pattern that is still not foldable.

Beyond these mathematical questions, it might also be amusing to consider what recognizable shapes can be made from flat-folded vertex-free origami patterns on square paper. [Joseph Wu's one-fold stegosaurus](http://www.josephwu.com/Files/PDF/stegosaurus.pdf) is a nice example.

([G+](https://web.archive.org/web/20190210055311/https://plus.google.com/100003628603413742554/posts/VXhf4HfmYeP))