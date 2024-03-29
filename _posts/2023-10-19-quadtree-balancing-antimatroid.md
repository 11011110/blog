---
layout: post
title: The quadtree-balancing antimatroid
date: 2023-10-19 17:08
---
Today's [computational geometry lecture](https://ics.uci.edu/~eppstein/164/) involved the use of balanced quadtrees in finite element mesh generation, the topic of Chapter 14 of [the Book of the Four Marks](http://link.springer.com/book/10.1007/978-3-540-77974-2). Here, a quadtree is just a recursive subdivision of a square into smaller squares, obtained by some rule for deciding when to divide one square into four. In the mesh generation application, you start of by performing this sort of subdivision for "crowded" squares (containing more of the boundary of the region to be meshed than just one or two adjacent edges) and for squares within which you expect the physical properties you are simulating to have complicated behavior (like turbulence or shock waves) where smaller regions are needed for better accuracy.

{: style="text-align:center"}
![An unbalanced quadtree generated from a polygon by splitting squares crossed by two non-adjacent edges of the polygon]({{site.baseurl}}/assets/2023/qt-mesh.svg)

The next step is to "balance" the mesh, using a different splitting rule: split a square when its side length is more than twice as long as an adjacent square.

{: style="text-align:center"}
![Converting an unbalanced quadtree into a balanced quadtree by splitting squares adjacent to much-smaller squares]({{site.baseurl}}/assets/2023/balanced.svg)

Once your quadtree is balanced, then (modulo some messy case analysis to make the mesh conform to the boundary of the region you are meshing) you can triangulate it by adding one more point in the middle of each square, connected to all the boundary vertices of that square. You only get nicely-shaped isosceles right triangles.

{: style="text-align:center"}
![Subdividing a balanced quadtree into isosceles right triangles by adding a vertex at the center of each square, connected to the boundary vertices of its square]({{site.baseurl}}/assets/2023/triangulate-qt.svg)

Usually we skip over the algorithmic aspects of the balancing step, because it's easy. You just keep track of a "ready list" of squares that are unbalanced (they need to be split because they have a too-small neighbor), and repeatedly pull off and split any square from this ready list until the list becomes empty. The order in which we choose these squares doesn't matter: at each step, the square we choose can be any member of the ready list. But why doesn't this arbitrary choice matter?

The title of this post gives it away: it's an [antimatroid](https://en.wikipedia.org/wiki/Antimatroid). More generally, we can mix the first part (where we split crowded or too-big squares) and the second part (where we split unbalanced squares) and still get an antimatroid. Start with one square, the outer square of the quadtree. Add a square to the ready list whenever it has become part of the quadtree and is crowded, too-big, or unabalanced. Then, repeatedly pull off a square from the ready list, split it, and check whether this causes its children or neighbors to be added to the ready list. Stop when the ready list becomes empty.

Antimatroids can be defined either as sequences (the sequence in which you pull squares from the ready list) or as families of sets (the sets of squares that you can have already split, at any time in this process). For an algorithm that uses ready lists in this way, you get an antimatroid whenever the only way to leave the ready list is to be pulled from it by the algorithm, and the condition for being added to the ready list depends only on the set of things you have already pulled, and not on its ordering. For quadtree balancing, this is true. The only way for a square on the ready list to leave the list is for it to be pulled and split. A square enters the ready list when it exists in the quadtree and is crowded, too-big, or unbalanced, and these conditions depend only on the set of squares present in the current quadtree, not on how we reached that set.

The advantage of analyzing quadtree balancing, or other ready-list algorithms, in this way, is it automatically gives us the freedom to choose how we manage the ready list. It doesn't matter whether we use a stack, a queue, or some other collection, because the order in which we pull things off the ready list doesn't change the result. We will always split the same set of squares and end up with the same quadtree.

This may seem like an obvious fact, but the proof is a little subtle. One way is to prove that any two sequences of steps of the algorithm (run until its ready list becomes empty) have the same set of elements, by induction on $$x+y-2s$$, where $$x$$ is the length of the first sequence, $$y$$ is the length of the second sequence, and $$s$$ is the length of the longest prefix that they have in common. As a base case, if $$x+y-2s=0$$, the sequences are equal so they have the same elements. Otherwise, at the first point of difference, one run of the algorithm chose one element $$a$$ while the other run chose a different element $$b$$. (It could not stop early, because at that step the ready list was non-empty: it contains $$a$$.) The second run must choose $$a$$ some time later in the sequence, because that's the only way to remove it from the ready list. You can get a third valid run of the algorithm by moving $$a$$ up from wherever it appears in the second run to just before $$b$$. After this move, $$a$$ is still ready when it is removed (because it was ready in the first run) as are all subsequent elements (because all of the choices that caused them to become ready in the second run are also present in the third run). The third run obviously uses the same elements as the second run, and also has the same elements as the first run by the induction hypothesis, so the first and second run have the same elements, as was to be proven.

Not at all difficult, but you can see why it would get tedious to have to go through the same proof over and over again for quadtrees and [stable matching and topological sorting]({{site.baseurl}}{% post_url 2023-09-30-linkage-start-academic %}) and [simulating chip-firing systems]({{site.baseurl}}{% post_url 2021-06-12-carrying-chip-firing %}) and [hierarchical clustering]({{site.baseurl}}{% post_url 2019-02-21-mutual-nearest-neighbors %}) and [graph degeneracy]({{site.baseurl}}{% post_url 2018-11-15-linkage %}) and graph reachability and ...

Saying "it's an antimatroid!" saves you from that tedium. It's an antimatroid, so using an algorithm that pulls things from a ready list works and gives you the same result regardless of the order that it chooses.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/111264471182298247))