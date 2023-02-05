---
layout: post
title: Greedy orderings with transposition
date: 2021-06-29 12:02
---
I'm a big fan of using [antimatroids](https://en.wikipedia.org/wiki/Antimatroid) to model vertex-ordering processes in graphs such as the construction of [topological orderings](https://en.wikipedia.org/wiki/Topological_sorting) in [directed acyclic graphs](https://en.wikipedia.org/wiki/Directed_acyclic_graph) and perfect elimination orderings in [chordal graphs](https://en.wikipedia.org/wiki/Chordal_graph). In each case a vertex can be removed from the graph and added to the order when it obeys a local condition: its remaining neighbors are all outgoing for topological orderings, or all adjacent for perfect elimination orderings. Once this condition becomes true of a vertex it remains true until the vertex is added to the order, the defining property of an antimatroid. Because of this property, a greedy algorithm for finding these orderings can never make a mistake: if there exists an ordering of all of the vertices, it is always a safe choice to add any vertex that can be added.

But there are some greedy vertex-ordering processes that do not form antimatroids, even though they do have the same inability to make mistakes. Two of these are the dismantling orders of [cop-win graphs](https://en.wikipedia.org/wiki/Cop-win_graph) and the reverse construction orders of [distance-hereditary graphs](https://en.wikipedia.org/wiki/Distance-hereditary_graph). I wrote about cop-win graphs [here in 2016]({{site.baseurl}}{% post_url 2016-08-18-game-of-cop %}); a graph is cop-win if a cop can always land on the same vertex as a robber when they take turns either moving from a vertex to a neighboring vertex or staying put. In distance-hereditary graphs, all induced subgraphs have the same distances; [these graphs also have nice confluent drawings]({{site.baseurl}}{% post_url 2005-10-11-delta-confluent-drawing-paper %}). Both of these classes of graphs can be recognized by greedy algorithms that remove one vertex at a time until either getting stuck (for graphs not in the class) or succeeding by reaching a single-vertex graph. But although the conditions for removing vertices in these algorithms are local, they are not antimatroidal.

# An example graph

{: style="text-align:center"}
![A six-vertex graph with six vertices A, B, C, D, E, and F, and seven edges AD, BC, BD, BE, CE, and EF]({{site.baseurl}}/assets/2021/Ptolemaic.svg)

The graph shown above happens to be chordal, distance-hereditary, and cop-win, making it a convenient example both of how to order the vertices of these graph classes and of why the distance-hereditary and cop-win orderings are not antimatroidal.

* In chordal graphs, a perfect elimination ordering can be constructed by repeatedly removing _simplicial vertices_, vertices whose neighborhoods form a clique. For an elimination ordering of the example graph, vertices $$A$$, $$C$$, and $$F$$ are already available to be listed: $$A$$ and $$F$$ only have one neighbor (automatically a clique), and $$C$$ has two neighbors forming a two-vertex clique. The other vertices will become available later in the removal process, once enough of their neighbors have been removed and all remaining vertices become adjacent. For instance, once $$A$$ has been removed, $$D$$ will become available, and once $$C$$ has been removed, $$B$$ will become available. Once this removal process makes a vertex simplicial, it remains simplicial until removed, so elimination orderings form an antimatroid.

* Distance-hereditary graphs can be constructed from a single vertex by repeatedly adding leaf vertices (with one neighbor connecting to previous vertices) or twins (duplicates of previous vertices). Reversing this process, these graphs can be deconstructed by repeatedly removing leaves or twins. The graph above has no twins, but $$A$$ and $$F$$ are leaves, and can be removed immediately. If $$A$$ is removed, $$C$$ and $$D$$ become false twins (not adjacent to each other), and either of them can be removed. Similarly, if $$F$$ is removed, $$B$$ and $$E$$ become true twins (adjacent to each other), after which one can be removed, but not both: after removing $$F$$ and $$B$$, $$E$$ is no longer a leaf or a twin (because its twin, $$B$$, has gone), and must remain until later steps. Because the removal orders can start $$FB$$ or $$FE$$ but not $$FBE$$, they are not described by an antimatroid.

* Similarly, cop-win graphs can be dismantled by repeatedly removing a vertex $$v$$ that is dominated by another vertex $$w$$, meaning that the neighborhood of $$v$$ (including $$v$$ itself) is a subset of the neighborhoood of $$w$$. In the given graph, $$A$$ is dominated by $$D$$, $$B$$ is dominated by $$E$$, $$C$$ is dominated by both $$B$$ and $$E$$, and $$F$$ is dominated by $$E$$. So any one of these four dominated vertices starts out as removable. But if we remove first $$F$$ and then $$E$$ (dominated by $$B$$ after the removal of $$F$$) we can no longer remove $$B$$. So because the ability to be removed can go away before the removal happens, we do not have an antimatroid.

There's another complication here as well. For both distance-hereditary graphs and cop-win graphs, removing leaves and twins or dominated vertices will never eliminate all graph vertices. Instead, both removal processes stop when we reach a single remaining vertex. But this is different from antimatroids, where all elements must be included in all orderings.

# Some axiomatics

To understand why greedy orderings still work in these cases, I think it's helpful to start by understanding why they work for antimatroids, as a general class of structures. The following is not quite the usual system of axioms for antimatroids, but they can be defined as non-empty formal languages (that is, sets of strings over a finite alphabet) with the following properties:

Hereditary:

: Every prefix of a string in the language is also in the language. Thinking about this in the other direction: every string in the language can be built up by adding one character at a time, starting from the empty string, at all times remaining within the language.

Normal:

: Every character occurs at most once in any string in the language. An element can only be added to the sequence of elements once. Because we are assuming the alphabet to be finite, this means that the language itself is also finite.

Oblivious:

: If $$S$$ and $$T$$ are permutations of each other in the language, then for every character $$x$$, $$Sx$$ is in the language if and only if $$Tx$$ is in the language. This means that what can be added next depends only on the set of characters that have been added already, forgetting about the order in which they were added.

Anti-exchange:

: If $$S$$ is a string, $$x$$ and $$y$$ are different characters, and $$Sx$$ and $$Sy$$ both belong to the language, then so does $$Sxy$$. Adding $$x$$ doesn't prevent $$y$$ from being added later. This is the key property of an antimatroid and the one that is violated by the distance-hereditary and cop-win orderings.

Usually a stronger version of obliviousness is used, stating that when $$S$$ and a permutation of $$Sx$$ are in the language, then $$Sx$$ is in the language, but it's not immediately obvious why this should be true for the vertex-ordering processes I'm considering here, so I've gone with a weaker version. We'll see later that the stronger version is implied by a combination of this and other properties. It is standard to also require that all characters be usable, but I haven't done this, because I want to understand the behavior of antimatroidal greedy algorithms on graphs not in the given graph class, for which they get stuck before ordering the whole graph. But this is not important, because one could instead redefine the alphabet to consist only of usable characters.

Given a language that satisfies all of these properties, one can show that all non-extendable strings are equally long and use the same alphabet as each other. For, if we have two different non-extendable strings $$S$$ and $$T$$, we can morph $$S$$ into $$T$$ one step at a time, never shortening it or changing its character set, by finding the first position at which $$S$$ and $$T$$ differ, finding the character $$t$$ that $$T$$ has at that position (necessarily also used later in $$S$$ because it was usable at that position and would have remained usable until it was used), and repeatedly using the anti-exchange axiom to swap $$t$$ for the previous character in $$S$$ until it has been swapped into a match with $$T$$. The oblivious property ensures that the part of the string after the swap remains valid. So $$S$$ cannot be shorter than or miss any characters from $$T$$, nor vice versa.

Instead of the anti-exchange axiom, the distance-hereditary and cop-win orderings satisfy a weaker property, based on the notion of swapping two characters.

Transposition:

: Suppose $$S$$ is a string, $$x$$ and $$y$$ are different characters, and $$Sx$$ and $$Sy$$ both belong to the language, but $$Sxy$$ does not. Then for all $$T$$ not containing $$x$$ or $$y$$, $$SxT$$ is in the language if and only if $$SyT$$ is also in the language, and $$SxTy$$ is in the language if and only if $$SyTx$$ is also in the language.

The last part of the transposition property, about $$SxTy$$ and $$SyTx$$, is only included because we used a weak version of obliviousness; if we used the stronger version, it would follow from the earlier part of the transposition property.

# Cop-win and distance-hereditary orderings have the transposition property

Let's suppose we're trying to dismantle a cop-win graph by repeatedly removing dominated vertices, in the hope of getting down to a single vertex. After we've removed some vertices already in a sequence $$S$$, two vertices $$x$$ and $$y$$ might become included in the set of dominated vertices. This can happen in several different ways:

* It might be the case that $$x$$ is dominated by a vertex that is not $$y$$, and that $$y$$ is dominated by a vertex that is not $$x$$. When this happens, they can be removed in either order: removing one won't change the fact that the other is dominated by whatever other vertex dominated it already.
* It might be the case that $$x$$ is dominated by $$y$$, and $$y$$ is dominated by a third vertex $$z$$. But then $$x$$ is also dominated by $$z$$, and again they can be removed in either order. When one is removed, the other is still dominated by $$z$$.
* The only remaining case is that $$x$$ and $$y$$ are each dominated only by the other of these two vertices. In this case, we can remove one or the other but not both. But if $$x$$ and $$y$$ dominate each other, they have the same neighbors (they are twins), and there is a symmetry of the remaining subgraph swapping $$x$$ and $$y$$. So in this case, any continuation of the removal sequence $$S$$ can have $$x$$ replaced by $$y$$ and vice versa, and still be a valid continuation. This is exactly what the transposition property states.

The argument for distance-hereditary orderings is even easier. If $$x$$ and $$y$$ are not twins of each other, then removing one won't affect the removability of the other. If they are twins, then they are symmetric and any continuation of the removal sequence can exchange $$x$$ for $$y$$ without changing its validity.

# Orderings with transposition form greedoids

If we can't obtain an antimatroid from the cop-win or distance-hereditary graphs, we might at least hope for a more general structure, a greedoid. The key property of greedoids (viewed as hereditary normal languages rather than their usual definition as set systems) is the following axiom:

Exchange:
: If $$S$$ is a string in the language of a greedoid, and $$T$$ is a longer string in the same language, then there is a character $$x$$ in $$T$$ such that $$Sx$$ is a string in the language.

This implies that all maximal strings in the language have the same length, and in the cop-win and distance-hereditary cases it implies that all greedy dismantling or deconstruction sequences reach a single vertex without getting stuck along the way. The greedoid exchange property also immediately implies the strong version of the obliviousness property, by plugging in a permutation of $$Sx$$ as the string $$T$$ in the exchange property.

To prove that indistinguishability implies the exchange property, let $$S$$ be any string in an indistinguishable (hereditary normal oblivious) language, and let $$T$$ be a longer string, which we might as well assume to be maximal. If $$S$$ is a prefix of $$T$$, then obviously we can satisfy the exchange property: just take the prefix of $$T$$ that has one more character.

Otherwise, I claim that we can replace $$T$$ by a different string $$T'$$ of the same length that agrees with $$S$$ for more positions. To find $$T'$$, let $$y$$ be the first character of $$S$$ that differs from the corresponding character of $$T$$; this must exist by the assumption that $$S$$ is not a prefix of $$T$$. Obviously, at the position of $$y$$ in $$S$$, we could have added it to $$T$$, but instead some other character was chosen. Maybe, $$y$$ remained available to be chosen throughout the remaining positions of $$T$$, until it actually was chosen. If so, just as in the antimatroid case, we could repeatedly swap $$y$$ with its predecessor in $$T$$ until reaching a string $$T'$$ where $$y$$ is in the correct position. Alternatively, maybe at some point during the construction of sequence $$T$$, we chose a character $$z$$ causing $$y$$ to become unavailable. In this case, by the transposition property, we can swap $$y$$ for $$z$$ in $$T$$ and then as before repeatedly swap $$y$$ with its predecessor in $$T$$ until reaching a string $$T'$$ where $$y$$ is in the correct position.

By repeatedly replacing $$T$$ by equally long strings that agree with more and more positions of $$S$$, we eventually reach a string for which $$S$$ is a prefix, and can append one more character. This construction of $$T'$$ from $$T$$ does not include any new characters that weren't already in $$S$$ or $$T$$, so the appended character must have come from $$T$$, proving the exchange axiom.

The use of the transposition property to form greedoids is standard; these greedoids are called transposition greedoids, and are described e.g. by Björner and Ziegler in their introduction to greedoids in the book _Matroid Applications_. Another [book chapter on transposition greedoids](https://doi.org/10.1007/978-3-642-58191-5_10), in the book _Greedoids_ by Korte, Schrader, and Lovász, includes another graph-theoretic example where the elements are edges of series-parallel graphs. The part that appears to be less standard is the use of this property to explain the ability of greedy algorithms to recognize cop-win and distance-hereditary graphs. I looked, but was unable to find publications observing that these two classes of graphs lead to greedoids or transposition greedoids, despite some suspiciously-similar terminology ("twins", "dismantling") on both sides. If anyone knows of such publications, I'd appreciate hearing of them, so that I could add this connection to their Wikipedia articles.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/106495619434427598))