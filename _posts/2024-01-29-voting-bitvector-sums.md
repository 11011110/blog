---
layout: post
title: Voting with bitvector sums
date: 2024-01-29 22:52
---
As has happened in the past, there has been a recent scandal involving Hugo award voting. And [as has happened in the past]({{site.baseurl}}{% post_url 2014-08-18-condorcet-hugo-and %}), this has caused me to completely ignore the particulars of the scandal and instead focus on the voting algorithms involved.

We'll get to the voting further down in the post, but first I want to discuss a seemingly unrelated problem: addition of bitvectors. The following algorithm problem and its solution seem so simple and basic that surely they were already known, but I don't know of a reference: given an input consisting of $$n$$ binary numbers, determine for each $$i$$ the number of nonozero bits in position $$i$$ of the numbers. Or, another way of specifying the same problem: given a collection of <span style="white-space:nowrap">$$\{0,1\}$$-vectors</span> packed into binary numbers, compute their vector sum.

The second specification contains the seeds of my answer, which applies more generally to finding the vector sum of vectors with <span style="white-space:nowrap">$$2^j$$-bit</span> unsigned integer coefficients, packed into larger words:
* Use shifting and masking to zero out the coefficients in alternating positions, resulting in two equally-long lists of vectors with <span style="white-space:nowrap">$$2^{j+1}$$-bit</span> coefficients (in which the upper bits are all zero).
* Use integer addition to sum groups of $$2^j+1$$ of these vectors. This is a small enough group size that nothing can overflow, so the result is two shorter lists of packed vector sums, one for the coefficients in even positions and the other for the coefficients in odd positions.
* Recursively sum these shorter lists and interleave the results.

Starting with $$n$$ bitvectors, we get approximately $$2n/3$$ vectors of two-bit quantities, then $$4n/15$$ vectors of four-bit quantities, then $$8n/255$$ vectors of eight-bit quantities, etc. Each stage reduces the total length by at least a constant factor, until you get down to subproblems of one or two packed vectors. You could stop there and solve those subproblems directly, or you could continue recursing, taking time proportional to the subproblem dimension. Either way, the result is that we can solve this problem, for <span style="white-space:nowrap">$$b$$-dimensional</span> bitvectors, in <span style="white-space:nowrap">time $$O(n+b)$$.</span>

I implemented this in Python, without early stopping:

{% highlight python %}
import functools

@functools.cache
def mask(i,j):
    """Bitmask for alternating 2^j-bit subwords of a 2^i-bit words"""
    pi = 1<<i
    pj = 1<<j
    x = (1<<pj)-1
    while pj < pi:
        pj += pj
        x = (x << pj) | x
    return x

def sumby(L,n):
    """Given sequence of binary values, return seq of sums of n-tuples"""
    return [sum(L[i:i+n]) for i in range(0,len(L),n)]

def packedvecsum(L,i,j):
    """Find vector sum of 2^j-bit vectors packed into 2^i-bit words"""
    if i==j:
        return [sum(L)]
    M = mask(i,j)
    n = (1<<(j+1))+1    # how many to bundle together
    X = packedvecsum(sumby([x&M for x in L],n),i,j+1)
    M <<= 1<<j
    Y = packedvecsum(sumby([(x&M)>>(1<<j) for x in L],n),i,j+1)
    return [pair[i] for pair in zip(X,Y) for i in (0,1)]    # transpose+flatten

def countbits(L):
    """How many nonzeros are in each bit position?
    Input must be a list of non-negative integers"""
    m = max(L)
    i = 0   # count #bits in input values
    while m > (1 << (1<<i)):
        i += 1
    return packedvecsum(L,i,0)
{% endhighlight %}

So what does this all have to do with Hugo? The connection is not the final award voting, but the nomination stage of the awards, which (since the previous scandal) has switched to a system of [single transferable voting](https://en.wikipedia.org/wiki/Single_transferable_vote) with fractional allocations. As I understand it, each person who votes in the nomination phase can name up to a quota of five candidates, with their one vote split equally among however many candidates they pick. Then, while there are too many candidates remaining, one is eliminated. The remaining candidates split the single votes of each nominator in the same way (getting a fractional amount from each voter inverse to the number of candidates remaining on that voter's ballot) until the slate is down to its desired size. In the Hugo system, the quota of allowed votes per voter is five, but the slate size is six; it's the votes per voter that matters for this post. [The choice of who to eliminate is done in a complicated way](https://electowiki.org/wiki/E_Pluribus_Hugo) involving finding the two candidates with the fewest fractional votes and breaking the tie according to which of the two appeared on the fewest ballots, but that's also not important here. Part (but not the only part) of the current scandal is that [this system was not followed correctly](https://camestrosfelapton.wordpress.com/2024/01/30/a-preliminary-analysis/): it is not possible for the published vote totals after each elimination step to have come from a valid run of this system. It is unclear whether this means that an attempt at following the system was made, but performed badly, or whether the nominations were chosen some other way, and then voting numbers were falsified to justify them, again done badly.

Anyway, the type of question I like to ask about this system is: how quickly can we implement it? Or rather, more theoretically: what is the best possible <span style="white-space:nowrap">$$O$$-notation</span> for the worst-case time of an implementation, under reasonable assumptions about the magnitudes of the various parameters of the system? Here the parameters are the number of <span style="white-space:nowrap">voters ($$n$$),</span> the number of initial <span style="white-space:nowrap">candidates ($$k$$),</span> and the quota of how many candidates each voter can vote <span style="white-space:nowrap">for ($$q$$).</span> I'm going to assume <span style="white-space:nowrap">$$n\gg k\gg q$$.</span> There are also some annoying issues of fractional roundoff but we can eliminate those by multiplying all votes <span style="white-space:nowrap">by $$q!$$,</span> so each candidate gets an integer number of multiplied votes.

With these assumptions, the naive or most obvious algorithm would be: tally all the votes, remove a candidate, tally all the votes again, remove a candidate, etc. The input size (the system of ballots) <span style="white-space:nowrap">is $$qn$$.</span> Most of the $$k$$ initial candidates may end up removed, and each removal takes time $$O(qn)$$ to tally the votes. Thus the total time <span style="white-space:nowrap">is $$O(qkn)$$.</span>

You can do better by keeping a list of the voters for each candidate, and only adjusting the vote contributions from voters for eliminated candidates, rather than recalculating the entire vote after each elimination. Adjusting the contributions for one voter takes <span style="white-space:nowrap">time $$O(q)$$,</span> and a total of $$O(qn)$$ adjustments need to be performed. (In the worst case, most voters will have most of their candidates eliminated.) So the total time <span style="white-space:nowrap">is $$O(q^2n)$$,</span> already an improvement because we have traded a bigger parameter for a smaller one.

The algorithm that I have in mind improves on this by batching the adjustments, using bitvector sums:

* Make a list of the voters for each candidate, as above
* Represent each ballot by a bitvector
* Keep a count for each voter of how many candidates they have left on their ballot
* When a candidate is eliminated, go through their voters, subtract one from those voters' counts, and group the affected voters by their remaining counts. In each group, apply the bitvector sum algorithm, giving a count, for each candidate, of the number of voters whose points should be redistributed to that candidate. Combine the number of candidates remaining per ballot with the count of votes for each candidate to adjust all the vote totals.

The total number of ballots affected by eliminations <span style="white-space:nowrap">is $$O(qn)$$,</span> as before. Each affected ballot is included in a group of equal-count ballots. Each group uses a bitvector sum calculation that <span style="white-space:nowrap">(if $$k\le b$$)</span> takes time time proportional to the size of the group plus the number of candidates. There are a total of $$kq$$ groups formed throughout the algorithm, $$q$$ per candidate. Thus the time is proportional to the total size of all groups, $$O(qn)$$, plus $$O(k)$$ per group, <span style="white-space:nowrap">or $$O(qk^2)$$.</span> giving total time <span style="white-space:nowrap">is $$O(qn+qk^2)$$.</span> The $$qn$$ term is unavoidable (it is the input size) and the $$qk^2$$ term is probably better than the <span style="white-space:nowrap">previous $$q^2n$$.</span> If $$k$$ can be larger than $$b$$, this time bound needs a little adjustment to account for the fact that the vector sums will no longer be linear in their number of vectors, giving total time <span style="white-space:nowrap">$$O(qn\lceil k/b\rceil+qk^2)$$.</span> If $$k=O(b)$$ <span style="white-space:nowrap">and $$k^2=O(n)$$,</span> this is linear in the input size, unlike any of the non-bitvector-based algorithms.

If you have a really big word size you could also use packed vectors of more than one bit, and multiply each affected ballot by its adjustment amount, avoiding the need to group affected ballots by their numbers of remaining candidates. I don't think the assumption of huge word size and fast multiplication makes as much sense as the assumption that $$k^2=O(n)$$, though, so I haven't analyzed that variation in any detail.

As for what algorithm the implementors of software for tallying votes in this system should use in practice: the simplest naive algorithm, because it's least likely to be buggy and most likely to convince others of its correctness. All this theory is just theory. The actual parameters of the problem are such that anything will work quickly enough; speed is not the issue.