---
layout: post
title: Dissection into rectangles and tensor rank
date: 2022-04-03 18:45
---
It's easy to cut a Greek cross into pieces that can be reassembled into a rectangle:

{: style="text-align:center"}
![Dissection of a Grek cross to a 4x5 rectangle]({{site.baseurl}}/assets/2022/cross2rect.svg){: style="width:100%;max-width:540px" }

Here's another example. The three yellow rectangles below have dimensions <span style="white-space:nowrap">$$2^{2/3}\times 1$$,</span> <span style="white-space:nowrap">$$2^{1/3}\times 2^{1/3}$$,</span> <span style="white-space:nowrap">and $$1\times 2^{2/3}$$.</span> (The order of multiplication matters here!) Put them together, and you get the blue stealth aircraft shape. Can you cut this shape into pieces and reassemble them into a single rectangle?

{: style="text-align:center"}
![Union of three irrational rectangles]({{site.baseurl}}/assets/2022/trirect.svg){: style="width:100%;max-width:720px" }

The answer is yes; any polygon can be cut and reassembled into a rectangle, or into any other polygon of the same area. This is the [Wallace–Bolyai–Gerwien theorem](https://en.wikipedia.org/wiki/Wallace%E2%80%93Bolyai%E2%80%93Gerwien_theorem). But the Greek cross dissection above uses only axis-parallel cuts and translation of the pieces. To get a single rectangle from the stealth shape, you're going to need a more general class of operations that cut it at odd angles and rotate the pieces. It's impossible to make a rectangle from this shape using only axis-parallel cuts and translation. And even for the Greek cross, although you can make a rectangle as shown, it's impossible to make a square using only axis-parallel cuts and translation.

To see why, we need to understand the [Dehn invariant](https://en.wikipedia.org/wiki/Dehn_invariant). As usually defined, this is a value that can be determined for any three-dimensional polyhedron. It's called an invariant because it stays unchanged when you cut up the polyhedron into polyhedral parts and reassemble the pieces into something else, allowing odd-angled cuts and rotations. In order for one polyhedron to have a dissection into another, they must both have the same volume and the same Dehn invariant. This can be used to show, for instance, that you cannot dissect a regular tetrahedron into a cube. But as several authors have described, a version of the same method also applies to axis-parallel dissections of orthogonal <span style="white-space:nowrap">polygons.[^s] [^b]</span>

To evaluate the Dehn invariant of an orthogonal polygon, the first step is to represent the polygon in Cartesian coordinates, and to find a _rational basis_ for its coordinates, a system of numbers such that every coordinate has a unique representation as a linear combination of basis elements with rational-number coefficients. This is just a basis, in the usual meaning of the word from linear algebra, when we interpret the real numbers as being a vector space over the rational numbers. In the example of the stealth shape, we can use the same basis for both the <span style="white-space:nowrap">$$x$$- and</span> <span style="white-space:nowrap">$$y$$-coordinates,</span> the set of numbers <span style="white-space:nowrap">$$\{1,2^{1/3},2^{2/3}\}$$.</span> The choice of basis is arbitrary (as long as it can represent all coordinates, without any redundancy) and will affect the rest of the calculation but not the conclusions we draw from it. If we're comparing two shapes, we can use a common basis that can represent the coordinates from both; it won't hurt if some of the basis elements are only used for one of the two shapes. So for instance, if the Greek cross is made out of unit squares, the square we'd like to dissect it into has side length $$\sqrt5$$ and we can use the basis $$\{1,\sqrt 5\}$$ to compare the cross to the square.

Next, we decompose the given shape into rectangles through its vertices (like the yellow rectangles that we've already used to decompose the stealth shape). Express the width and height of each rectangle as a rational combination of basis elements; in our example, each rectangle is just a product of two basis elements, but sometimes more complex combinations might be required. If we multiply the expression for the width of a rectangle by the expression for the height of a rectangle, we get an expression for the area of the whole rectangle as a sum of terms $$a\cdot b_x\cdot b_y$$ where $$a$$ is a rational number and $$b_x$$ and $$b_y$$ are <span style="white-space:nowrap">$$x$$-basis</span> and <span style="white-space:nowrap">$$y$$-basis</span> elements, respectively. Adding these expressions for every rectangle in the decomposition gives a similar expression for the area of the whole shape. Since we're separating out the terms for each product of basis elements, it's convenient to write it out as a matrix. For the Greek cross and same-area square, with the basis $$\{1,\sqrt 5\}$$ for both <span style="white-space:nowrap">$$x$$ and $$y$$,</span> we get the matrices

$$\begin{pmatrix} 5 & 0 \\ 0 & 0 \end{pmatrix} \qquad\text{and}\qquad
\begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix},$$

respectively. For the stealth shape, with the basis $$\{1,2^{1/3},2^{2/3}\}$$ for both <span style="white-space:nowrap">$$x$$ and $$y$$,</span> we get the matrix

$$\begin{pmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{pmatrix}.$$

That's the Dehn invariant! Because the Greek cross and square have different invariants, they cannot be dissected into each other (for this restricted axis-parallel translation-only form of dissection). But what about the dissection of the stealth shape into a single rectangle? How can we apply this analysis when there are infinitely many possible rectangles to try?

Here it's convenient to move from the notion of bases and matrices to a more [coordinate-free](https://en.wikipedia.org/wiki/Coordinate-free) formulation of the same thing using [abstract tensors](https://en.wikipedia.org/wiki/Tensor_(intrinsic_definition)). When we're expressing the area of an $$x\times y$$ rectangle as a product of rational linear combinations of basis elements, what we're really doing is constructing the element $$x\otimes y$$ of the [tensor product](https://en.wikipedia.org/wiki/Tensor_product) <span style="white-space:nowrap">$$\mathbb{R}\otimes_{\mathbb{Q}}\mathbb{R}$$.</span> Then when we add the expressions arising from the decomposition into rectangles, to form a matrix describing the whole shape, this is just addition of these elements within the tensor product. The subscript $$\mathbb{Q}$$ in the tensor notation corresponds to the fact that we're interpreting real numbers as forming a vector space over the field $$\mathbb{Q}$$ of rational numbers. (Some sources use a subscript $$\mathbb{Z}$$ but this is not an important difference here.)

One thing we know about matrices is that they have a [rank](https://en.wikipedia.org/wiki/Rank_(linear_algebra)), the dimension of the vector space generated by their rows or columns. But tensors also have a notion of rank. The rank of a tensor is the minimum number of terms needed to express it as a sum of products

$$x_1\otimes y_1+x_2\otimes y_2+\cdots,$$

where the $$x_i$$ and $$y_i$$ can be any elements of the spaces that are being tensored together (they are not required to be basis elements). For tensor products of three or more spaces, the rank is still defined in the same way, but it can get very tricky to calculate. This is a big part about why the time bounds for fast matrix multiplication are still so mysterious: they involve tensors of order three. But for the order-two tensor space $$\mathbb{R}\otimes_{\mathbb{Q}}\mathbb{R}$$, we're saved by linear algebra: the rank of a tensor of order two is just the rank of a matrix representing it, for any basis over the appropriate field <span style="white-space:nowrap">(here $$\mathbb{Q}$$).</span>

Suppose that we could dissect a <span style="white-space:nowrap">polygon $$P$$,</span> using axis-parallel cuts and translations, into a collection of $$k$$ rectangles. Then the sum of the tensor expressions for those rectangles would be an expression of the Dehn invariant <span style="white-space:nowrap">of $$P$$,</span> as a sum of $$k$$ products. Therefore, the rank of the Dehn invariant of $$P$$ would have to be at <span style="white-space:nowrap">most $$k$$.</span> But for our stealth shape, we know the rank: we have expressed its Dehn invariant as a matrix of rank three. Therefore, to dissect it into rectangles, we need at least three rectangles.

Another use of the polyhedral Dehn invariant, besides dissection of one shape into another, involves tiling. Any polyhedron that tiles space must have Dehn invariant zero, and any polyhedron with Dehn invariant zero can be dissected into a different polyhedron that tiles space. For the axis-parallel polygonal Dehn invariant we're looking at here, things don't work out quite so neatly. The Greek cross can tile, but has nonzero Dehn invariant. More, any axis-parallel polygon can be cut into multiple rectangles, and these can tile space aperiodically by grouping them into rows of the same type of rectangle. 

{: style="text-align:center"}
![Aperiodic tiling by three irrational rectangles]({{site.baseurl}}/assets/2022/trirect-row-tiling.svg){: style="width:100%;max-width:600px" }

So the Dehn invariant cannot be used to prove that such a thing is impossible, because it is always possible. If we could rotate pieces, we could also form these three rectangles into a single-piece axis-parallel hexagon that can tile the plane:

{: style="text-align:center"}
![Periodic tiling by a hexagon formed from three irrational rectangles]({{site.baseurl}}/assets/2022/trirect-flip-tiling.svg){: style="width:100%;max-width:720px" }

But this is not possible without rotation. Every periodic tiling of the plane has a [fundamental region](https://en.wikipedia.org/wiki/Fundamental_domain) in the shape of an axis-parallel hexagon, like the hexagons in this periodic tiling.  If one or more copies of a polygon could be cut up by axis-parallel cuts and reassembled by translations to form a single polygon that can tile the plane periodically, it would also be possible to dissect copies of the polygon (possibly a larger number of copies of it) into an axis-parallel hexagon. But these hexagons have a Dehn invariant with rank at most two (they can be cut into two rectangles), while any number of copies of our stealth shape combine to have rank three (making more copies just multiplies the matrix by a scalar). Because the Dehn invariants have different ranks, no dissection is possible.

This same rank analysis can also be applied to the more familiar polyhedral form of the Dehn invariant. For that form, a polyhedron whose Dehn invariant has high rank cannot be dissected into another polyhedron with fewer edges than the rank.

* Footnotes go here
{:footnotes}

[^s]: John Stillwell (1998), _[Numbers and Geometry](https://doi.org/10.1007/978-1-4612-0687-3)_, Springer, p. 164.

[^b]: David Benko (2007), "[A new approach to Hilbert's third problem](https://www.jstor.org/stable/27642302)", _Amer. Math. Monthly_ 114 (8): 665–676.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/108071296947021436))