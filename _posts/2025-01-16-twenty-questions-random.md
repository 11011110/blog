---
layout: post
title: Twenty questions with a random liar
date: 2025-01-16 17:32
---
I have another new arXiv preprint: "Computational geometry with probabilistically noisy primitive operations", [arXiv:2501.07707](https://arxiv.org/abs/2501.07707), with Mike Goodrich and his student Vinesh Sridhar. Many computational geometry algorithms are designed around the use of _primitives_, subroutines that access the coordinate data of the input and convert it into combinatorial information, with the assumption that all access to the input goes through these primitives. For instance, a key primitive often used for computing convex hulls (and central to [my book on forbidden configurations](https://ics.uci.edu/~eppstein/forbidden/)) takes as input an ordered triple of points in the plane and determines whether they are ordered clockwise around the triangle they generate, counterclockwise, or collinear. The premise of the new preprint is that this primitive could randomly produce the wrong result, with some constant probability, independent of any past errors or successes.

(The title of this post comes from [a related paper by Dhagat, Gács, and Winkler, from SODA 1992](https://dl.acm.org/doi/abs/10.5555/139404.139409), using a different model in which the primitive is incorrect adversarially rather than randomly.)

You might like to perform a bigger computation using these noisy primitives, with high probability of a correct overall outcome despite their errors. An easy way to get more accurate results would be to repeat each primitive many times and take its majority outcome. Repeating a logarithmic number of times would make the failure probability polynomially small, so small that you could make a polynomial number of calls to these repeated primitives and have a good chance of never seeing an error. That polynomially small failure probability is what we mean by "high probability". But this trivial repetition strategy has a cost: it slows everything down by a logarithmic factor. The goal of our preprint is to find geometry problems for which more sophisticated methods can avoid this slowdown. We achieve this no-slowdown goal for some problems (like constructing convex hulls) and show that it is not possible for others (like finding closest pairs of points, which has a linear-time conventional algorithm but requires $$\Omega(n\log n)$$ noisy primitives).

Although we think the application of this model to computational geometry is new, the model of randomly erroneous primitives is not new. It has been applied for instance to comparison-based algorithms for sorting and searching, where the primitive is a comparison between two input numbers. 

You might well wonder whether this is just an intellectual puzzle, or whether there is some application for algorithms designed to work with faulty comparison primitives. One application comes from a paper by Manu Viola on [communication complexity](https://en.wikipedia.org/wiki/Communication_complexity): "The communication complexity of addition", _Combinatorica_ 2015, [doi:10.1007/s00493-014-3078-3](https://doi.org/10.1007%2Fs00493-014-3078-3). In one of the problems studied by Viola, two communicating parties (Alice and Bob) each hold an <span style="white-space:nowrap">$$n$$-bit</span> binary number. They want to know whose number is bigger, and they don't care about the secrecy of their numbers, but they would like to find out the result of this numerical comparison by exchanging as few bits of information as possible. You could do this by having Alice tell Bob her whole number, but this would take $$n$$ bits of communication. It turns out that Alice and Bob can do much better than this.

Viola considers an algorithm in which Alice and Bob collaborate to perform a binary search for the first bit position where their numbers differ from each other. Once they both know this, they also know who has a 0 in that position and who has a 1, and therefore whose number is larger. If Alice and Bob could test, for a <span style="white-space:nowrap">given $$k$$,</span> whether their numbers are the same in the first $$k$$ bits, then they could compare their numbers by using $$\log_2 n$$ of these tests. So the question becomes: how can Alice and Bob perform an equality test of two bitstrings using only very few bits? And when phrased in this way, the obvious answer is: hashing! Do some initial computation to generate a random hash function, then do the equality tests on the hashes of the two bitstrings. These hash values could potentially be much shorter than $$n$$ bits, reducing the communication needed per test. But there's a chance of an error when the two strings collide, hashing to the same value even when they're unequal.

In a model of computation where Alice and Bob have a shared source of randomness, this method can be made to work with hash functions whose hash values have only a constant number of bits, performing each equality test with a constant number of bits of communication but with a constant probability of error. The trivial repetition strategy would then give an equality test with high probability of correctness but $$O(\log n)$$ bits of communication, making the binary search use $$O(\log^2 n)$$ bits of communication. Alternatively, using <span style="white-space:nowrap">$$O(\log n)$$-bit</span> hash values would again get high probability of correctness (low probability of a hash collision) but again lead to $$O(\log^2 n)$$ bits of communication in the binary search. Instead, Viola replaces a standard binary search by a search algorithm that uses a logarithmic number of calls to a noisy primitive, the primitive that uses one hash value with a constant number of bits. This allows Alice and Bob to find which of their numbers is bigger, using only $$O(\log n)$$ bits of communication.

The main idea of Viola's noisy binary search algorithm is for each step of the search to walk up or down in a binary search tree, stepping downward on the basis of noisy comparisons and stepping upward when a test result makes it appear that you've made a mistake somewhere earlier. Of course that test result could itself be erroneous! But if you balance the error probabilities correctly you'll walk downward more often than you walk upward, and by adding logarithmically-long tails below the leaves of the search tree you can have high confidence that when you reach the end of one of these tails it will be the correct one. This same idea of walking upward and downward based on test results and apparent mistakes turns out to be key to our geometric algorithms, as well, but with the twist that the structure we are walking around in is a directed acyclic graph rather than a tree. (For those familiar with randomized incremental algorithms in geometry, it's the history DAG of a randomized incremental construction.)

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/113841175021741305))