---
layout: post
title: Relevant neighbors
date: 2021-10-13 23:05
---
I have a new preprint, ["Finding Relevant Points for Nearest-Neighbor Classification", arXiv:2110.06163](https://arxiv.org/abs/2110.06163), to appear in January at the [SIAM Symposium on Simplicity in Algorithms (SOSA22)](https://www.siam.org/conferences/cm/conference/sosa22). It's about points in Euclidean spaces of dimension three or more, but I thought it would make a good warm-up to discuss here the one-dimensional version of the same problem, solved (together with the 2d version) by Bremner, Demaine, Erickson, Iacono, Langerman, Morin, and Toussaint in their paper ["Output-sensitive algorithms for computing nearest-neighbour decision boundaries", _Discrete Comput. Geom._ 2005](http://dx.doi.org/10.1007/s00454-004-1152-0).

So in this problem, you have a collection of real-valued data points with known discrete classifications (say, a finite set of colors), and you want to guess the color of new points whose color is not already given. Nearest neighbor classification means simply that, to guess the color of $$x$$, you find the closest known point $$y$$ and guess that $$x$$ has the same color as $$y$$. One easy way to do this would be to store the known points in a sorted list and use binary search. There's lots more to say about this (for instance its use in combination with [random projections](https://en.wikipedia.org/wiki/Random_projection) for high-dimensional approximate nearest neighbors) but for today I want to focus on the size of this sorted list. We can store a list that is potentially much smaller, but always produces the same results, by keeping only points that have a neighbor with a different classification.

{: style="text-align:center"}
![One-dimensional nearest neighbor classification on a full data set and the data set trimmed to its relevant points]({{site.baseurl}}/assets/2021/1d-nnc.svg)

These points with differently-classified neighbors are the "relevant points" of the preprint title. Another way of describing them is that a point is relevant if deleting it would change the classification of some other (unknown) points in space that might later be queried. Among the set of decision boundaries, the ones separating parts of space with different classifications are the ones defined by relevant points. So if we store a nearest-neighbor data structure with only relevant points, we will get the same answer as if we store all known points. But because we're storing fewer points, it will take less memory and less time (especially if the reduced memory allows it to fit into cache).

If you have the points given to you in sorted order, then it's easy enough to scan through them in that order, keeping track of which pairs have different classifications, and produce a filtered sequence of the relevant ones. Here it is in Python (with apologies for the low-contrast syntax coloring):

{% highlight python %}
def relevant(seq,classify):
    """Filter points whose classification differs from a neighbor.
    Arguments are a sequence of points, and a function to classify
    each point. The return value is an iterator for the filtered sequence."""
    prevpoint = prevclass = prevlisted = None
    for x in seq:
        xclass = classify(x)
        if prevlisted != None and xclass != prevclass:
            if not prevlisted:
                yield prevpoint
            yield x
            prevlisted = True
        else:
            prevlisted = False
        prevpoint = x
        prevclass = xclass
{% endhighlight %}

However, as Bremner et al observed, sorting an input to make it usable by this scan does more work than necessary, because we don't need the sorted ordering of all the other points between the relevant ones. Instead, we can use an idea resembling [quickselect](https://en.wikipedia.org/wiki/Quickselect), where we modify the quicksort algorithm to stop recursing in subproblems where sorting is unnecessary. For finding relevant points, these subproblems are the homogeneous ones, in which all points have the same classification as each other. Bremner et al combined this idea with a version of quicksort that always partitions its subproblems at the exact median, in order to achieve a good worst-case time bound, but if we're happy with expected analysis we can use the same random-pivoting idea as the more usual form of quicksort:

{% highlight python %}
def quickrelevant(seq,classify):
    """Same output as relevant(sorted(list(seq)),classify).
    We assume the input sequence is sortable and has no repeat values."""

    def supersequence():
        """Generate sorted supersequence of relevant points by quicksort-like
        recursive subdivision, stopping at homogeneous subproblems.
        We include the endpoints of each subproblem, even though some might
        not be relevant, so the results should be cleaned up using relevant().
        We use an explicit stack to handle the recursion, avoiding the need
        to pass yielded outputs back through a call stack."""

        liststack = [list(seq)]
        while liststack:
            L = liststack.pop()
        
            # Base cases of recursion: lists of zero or one item
            if not L:
                continue
            if len(L) == 1:
                yield L[0]
                continue
            
            # Test whether L is homogeneous
            # and if so only generate its extreme values
            homogeneous = True
            firstclass = classify(L[0])
            for i in range(1,len(L)):
                if firstclass != classify(L[i]):
                    homogeneous = False
                    break
            if homogeneous:
                yield min(L)
                yield max(L)
                continue
            
            # Divide and conquer with random pivot
            pivot = L[random.randrange(0,len(L))]
            low = []
            high = []
            for x in L:
                if x < pivot:
                    low.append(x)
                else:
                    high.append(x)
            liststack.append(high)
            liststack.append(low)

    return relevant(supersequence(),classify)
{% endhighlight %}

The time complexity of this algorithm can be analyzed much like [the analysis of quickselect]({{site.baseurl}}{% post_url 2007-10-09-blum-style-analysis-of %}), by observing that the time is proportional to the number of comparisons with pivots, computing the probability that each possible comparison happens, and summing. In quicksort, two distinct elements at distance $$d$$ from each other in the final sorted output are compared whenever one of them is the first to be chosen as a pivot in the interval between them, which happens with probability exactly $$2/(d+1)$$. In quickrelevant, this same probability holds for pairs that are separated by one of the decision boundaries. But pairs of elements that are within the same homogeneous block are less likely to be compared, because of the possibility that the recursion will stop before it separates or compares them.

If a pair of elements lies within a single block, has distance $$d$$ separating them, and is $e$ units from both ends of the block, then it will only be compared if one of the two elements is first to be chosen in at least one of the two intervals of length $$d+e$$ extending from the two elements towards an end of their block. This happens with probability at most $$4/(d+e)$$, because there are two ways of choosing which element to pick first as the pivot and two ways of choosing which extended interval it is first in.

If we sum up these probabilities, for pairs involving a single element that is $$e$$ units from its nearest block boundary among a set of $$n$$ elements, we get $$O\bigl(\log(n/e)\bigr)$$ as the expected contribution to the total time for that one element. If we sum the contributions from the elements within a block, for a block of length $$\ell_i$$, we get a total expected contribution from that block of $$O\bigl(\ell_i\log(n/\ell_i)\bigr)$$. And if we have $$k$$ relevant points and $$O(k)$$ blocks, and we sum over all blocks, the total time is maximized when all the blocks are of equal size, $$\Theta(n/k)$$, for which we get total time $$O(n\log k)$$.

For quicksort and quickselect, it's possible to be more careful in the analysis, derive exact formulas for the probability of making each comparison, and from them get an analysis of the expected number of comparisons that does not use $$O$$-notation for its leading term; see my linked post on the quickselect analysis. Probably it's possible here too but it looks messier. Maybe it would make a good undergraduate research project. One thing to be careful of is that the comparisons are not over in the homogeneous case; finding the min and max simultaneously, in a block of length $$\ell_i$$, takes roughly $$3\ell_i/2$$ comparisons. But that should only be a lower-order term compared to the $$O(n\log k)$$ leading term of the analysis.