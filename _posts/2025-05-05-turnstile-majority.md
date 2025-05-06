---
layout: post
title: Turnstile majority
date: 2025-05-05 18:15
---
A famous [algorithm of Boyer and Moore for the majority problem](Boyer–Moore majority vote algorithm) finds a majority element in a stream of elements while storing only two values, a single tentative majority element $$m$$ and a counter $$c$$. Every time it seems a stream value equal to $$m$$, it increments the counter, and every time it sees an unequal element, it decrements the counter. If this would cause the counter to go negative, it replaces $$m$$ by the value that it sees and resets the counter to one. At the end of the algorithm, if there is any element that repeats for more than half of the items in the stream, then that element will be the one stored in $$m$$. But otherwise, the result of the algorithm is undefined. Here's a visualization I made of the algorithm for its Wikipedia article, with the data stream running across the bottom, the height of the graph showing the stored counter, and the icons on the graph showing the stored stream value:

{: style="text-align:center"}
![Example of the stream values and counters maintained by the Boyer–Moore majority vote algorithm]({{site.baseurl}}/assets/2025/Boyer-Moore.svg){: style="width:100%;max-width:720px" }

The task solved by this algorithm is almost impossible: it is impossible for an algorithm with sublinear memory to determine whether there is a majority element. So although you would like the algorithm to tell you whether its value $$m$$ has a majority, it cannot. But when there is a majority, the algorithm will find it, using a tiny amount of memory.

This became the prototypical example of a streaming algorithm in the _cash register model_ of streaming algorithms. These algorithms must handle a stream of elements, each entering the stream and never leaving, and they must produce a meaningful result using memory substantially less than it would take to record the entire stream. But there is another important model, the _turnstile model_, in which the data stream consists of a sequence of additions and removals of elements, analogous to the way a turnstile counts people going into and out of a building. It turns out that there is another algorithm, almost as simple, for maintaining a majority element in the turnstile model. I suspect that it may have been rediscovered and published multiple times, but if so I don't know where it was published.

{: style="text-align:center"}
![A turnstile. Ingolf. Warszawa - metro linia M2 - stacja Świe¸tokrzyska. CC-BY-SA licensed image, March 26 2015. URL https://commons.wikimedia.org/wiki/File:
Warszawa_-_Metro_-_%C5%9Awi%C4%99tokrzyska_(17009062241).jpg]({{site.baseurl}}/assets/2025/Turnstile.jpg){: style="width:100%;max-width:540px" }

As a warmup, when there are only two distinct values in a turnstile stream, then the Boyer–Moore algorithm works, almost without change! When removing an element unequal to $$m$$, increment the counter, when removing an element equal to $$m$$, decrease the counter, and if this would cause the counter to go negative, replace $$m$$ with the other stream value and reset the counter to one. For cash register streams with more than two distinct values, the algorithm's counter is best interpreted as an approximation to the frequency of $$m$$, but in turnstile streams with only two values it gives the exact margin of victory of one value over the other.

Then for multi-valued turnstile streams, with the values represented as binary numbers with $$w$$ bits per number, just maintain $$w$$ copies of the two-candidate Boyer–Moore algorithm, one copy $$(m_i,c_i)$$ for each bit position $$i$$. If there is a majority element, then it will overwhelm the voting for each bit, and its binary representation will be given by the majority bits. If there is no majority element, then the majority bits may be set in an inconsistent way to come from different elements, and the result is undefined, just as it was in the original Boyer–Moore algorithm.

You might expect the memory required by this method to be $$O(w)$$, with one counter per bit position, but actually it is $$O(\log n)$$. We can pack the bits $$m_i$$ into a single word of memory. All of the counters together require $$w\lceil\log_2 n\rceil$$ bits of memory, which can be packed into $$\lceil\log_2 n\rceil$$ words. I think the most convenient way to pack the counters into words is to make a word $$b_j$$ for the $$j$$th bit position of each counter, and to use bitwise binary operations to simultaneously increment or decrement all of the counters.

{: style="text-align:center"}
![Transposing an array of binary counters to pack them into fewer machine words]({{site.baseurl}}/assets/2025/packed-counters.svg){: style="width:100%;max-width:640px" }

An important generalization of the Boyer–Moore majority algorithm, the [Misra–Gries summary](https://en.wikipedia.org/wiki/Misra%E2%80%93Gries_summary), maintains some number $$k$$ of value–counter pairs, at each step incrementing one counter, replacing one value, or simultaneously decrementing all of the counters. It can be used to estimate the frequency of any value with an additive error at most $$n/(k+1)$$, or to list a superset of the elements that occur more than $$n/(k+1)$$ times. I don't know how to do these things with the bit-parallel turnstile majority algorithm above. They can be done in the turnstile model, with high probability by a randomized sketching method, the [count-min sketch](https://en.wikipedia.org/wiki/Count%E2%80%93min_sketch), but not as simply.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/114458368876060103))