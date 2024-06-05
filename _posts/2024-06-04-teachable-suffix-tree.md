---
layout: post
title: Teachable suffix tree construction
date: 2024-06-04 18:56
---
I often cover [suffix trees](https://en.wikipedia.org/wiki/Suffix_tree) in my algorithm and data structure classes, but until now haven't generally covered the algorithms to build them. These are data structures describing the suffixes of a string (start at any position of the string and continue until the end), useful in many string algorithms.

There's a linear-time construction algorithm by Martin Farach-Colton ([FOCS 1997](https://scholar.archive.org/work/mpnlr2uxyvhvvfkyy4rw4pa5ly)) that works by divide and conquer: it recursively builds a suffix tree for half of the suffixes, uses it to build a second suffix tree for the other half, and then merges the two trees. I can get through the part about building the second tree, but merging the two trees is a mess and I've never been able to do more than convey a vague flavor of the algorithm. The students learn that there is an algorithm, and that it's complicated, but not really more than that.

But this week, Mike Goodrich pointed me to a simplified construction for [suffix arrays](https://en.wikipedia.org/wiki/Suffix_array), a related but much simpler structure. In its most basic form, a suffix array is just a list of the positions at which each suffix starts (that is, the numbers from 0 up to the length of the given string), sorted alphabetically by the suffixes starting at those positions. The algorithm comes from "Linear work suffix array construction" by Kärkkäinen, Sanders, and Burkhardt ([JACM 2006](https://scholar.archive.org/work/mp3eztz6rrgddapyuerr4e76zi), based on a 2003 conference paper by two of the authors) and, although I didn't see it in their paper, it turns out to work for suffix trees as well, much more simply than Farach-Colton's algorithm.

Given an input string $$S$$, of length $$n$$, over an ordered alphabet $$\Sigma$$, Kärkkäinen et al. start by forming a new alphabet $$\Sigma^3$$ consisting of the triples of characters that appear consecutively in $$S$$ (allowing padding at the ends of $$S$$). A linear time radix sort can be used to renumber the letters in $$\Sigma^3$$ in an order-preserving way, preventing the alphabet size from blowing up as we recurse.
Over this new alphabet, $$S$$ has three representations $$S_0$$, $$S_1$$, and $$S_2$$, each of length $$n/3$$, depending on whether you break it up into triples starting at a position that is 0 mod 3, 1 mod 3, or 2 mod 3. The suffixes of $$S$$ that start at a position that is $$i$$ mod 3 will also be suffixes of $$S_i$$, so this partitions the $$n$$ suffixes that we are trying to sort into three subsets of $$n/3$$ suffixes.

The suffix array construction algorithm of Kärkkäinen et al. is:

* Construct alphabet $$\Sigma^3$$ and the three strings $$S_0$$, $$S_1$$, and $$S_2$$.

* Recursively sort the suffixes of the combined string $$S_1S_2$$, of length $$2n/3$$. The concatenation does not affect the ordering (it just adds extra junk to the suffixes of $$S_1$$, after the end-of-string character) so this gives us the combined ordering of $$2/3$$ of the suffixes of $$S$$. But we still need to order the remaining suffixes, from $$S_0$$.

* Each suffix of $$S_0$$ can be represented as a pair $$(c,s)$$ where $$c$$ is a single character of $$\Sigma$$ and $$s$$ is a suffix of $$S_1$$. Since we now know the orderings of both the characters of $$\Sigma$$ and (from the result of the recursion) the suffixes of $$S_1$$, we can radix sort these pairs to sort the suffixes of $$S_0$$.

* Now we can merge the suffixes of $$S_1$$ and $$S_2$$ with the suffixes of $$S_0$$, using a single pass of the merge subroutine from merge sort. This takes a linear number of comparisons between suffixes, but there's a trick to make these comparisons take constant time. To compare suffixes of $$S_0$$ and of $$S_1$$, represent both of them as pairs $$(c,s)$$ where $$c$$ is a single character and $$s$$ is a suffix of $$S_1$$ or of $$S_2$$ respectively. To compare suffixes of $$S_0$$ and of $$S_2$$, represent both of them as triples $$(c,c',s)$$ where $$c$$ and $$c'$$ are single characters and $$s$$ is a suffix of $$S_2$$ or of $$S_1$$ respectively. Just compare these pairs or triples lexicographically. We already know (and don't really need) the comparisons between all other kinds of suffixes.

It takes linear time at the outer level of the recursion, with a single recursive call to a problem of size $$2n/3$$, for total linear time. But now almost the same thing works for suffix trees:

* Construct $$\Sigma^3$$, $$S_0$$, $$S_1$$, and $$S_2$$, in the same way.

* Recursively construct the suffix tree of $$S_1S_2$$, and preprocess it for lowest common ancestor queries.

* Compute the sorted list of its leaves (the suffix array of $$S_1S_2$$), and merge with $$S_0$$ as above to get a suffix array of $$S$$.

* Build the suffix tree by adding the leaves in sorted (left-to-right) order, maintaining at each step the compressed trie of the leaves added so far. To add each leaf, walk up the tree from its predecessor in the sorted order until finding the point where the tree should add a new branch. Each node is internal to only one of these walks, so the total number of steps in these walks is linear.

* In order to tell when to stop walking, what we need to know is the length of the longest common prefix between each suffix and its predecessor in the sorted order. The same comparison trick used in the merge works again here. If both suffixes come from $$S_1$$ or $$S_2$$, you can find their longest common prefix by a single lowest common ancestor query (and then a constant number of comparisons as cleanup to go from $$\Sigma^3$$ back to $$\Sigma$$). Otherwise, you can break both prefixes into pairs $$(c,s)$$ or both into triples $$(c,c',s)$$ with suffixes from $$S_1$$ or $$S_2$$, for which you can again find longest common prefixes using at most one lowest common ancestor query.

That's all there is to it! Of course you need to know about [lowest common ancestors in trees](https://en.wikipedia.org/wiki/Lowest_common_ancestor) but at this point in my data structures course we've already covered that. The rest is simple enough that I could cover it all (including the definition and uses of suffix arrays and suffix trees as well as their construction) in a single 80-minute lecture.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/112561663066489406))