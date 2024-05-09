---
layout: post
title: Random perfection
date: 2024-05-08 22:13
---
The Wikipedia article on [perfect graphs](https://en.wikipedia.org/wiki/Perfect_graph) is now a Good Article! Along the way, the reviewer asked me whether random graphs are likely to be perfect. I didn't have a published source for that, so you won't find it in the article. But as with most properties of random graphs, the answer depends how dense you want the graph to be. In the usual [Erdős–Rényi–Gilbert](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93R%C3%A9nyi_model) $$G(n,p)$$ model of random graphs, we fix $$n$$ vertices and include each edge independently of the others with probability $$p$$. This turns out to have two phase transitions, between graphs that are likely to be perfect and graphs that are likely to be imperfect, one when the edge probability is $$\tfrac1n$$ and another when it is $$1-\tfrac1n$$. More precisely, if I'm not mistaken (which I could easily be):

- For $$\min\{p,1-p\}=o(\tfrac1n)$$, the resulting graph is perfect with high probability. This means that the probability of perfection goes to one in the limit as $$n$$ gets large.

- For $$\min\{p,1-p\}=\tfrac{c}{n}\pm o(\tfrac1n)$$ with $$0<c<1$$, the resulting graph is perfect or imperfect with probability bounded away from both $$0$$ and $$1$$. The probability of getting an imperfect graph varies monotonically and continuously from $$o(1)$$ in the limit as $$c\to 0$$ to $$1-o(1)$$ in the limit as $$c\to 1$$.

- For $$\min\{p,1-p\}=\tfrac{c}{n}\pm o(\tfrac1n)$$ with $$c\ge 1$$, and for $$\min\{p,1-p\}=\omega(\tfrac1n)$$, the resulting graph is imperfect with high probability.

Some parts of this are easy, others less so. Or at least, I didn't know enough probability theory to make them easy.

# The easy parts

The symmetry between $$p$$ and $$1-p$$ follows immediately from the facts that [perfect graphs are closed under complementation](https://en.wikipedia.org/wiki/Perfect_graph_theorem), and $$G(n,p)$$ becomes $$G(n,1-p)$$ under complementation. So we only need to look carefully at one of the two phase transitions, the one around $$p=\tfrac1n$$.

The cases with $$c<1$$ are well-studied and well-understood. Random graphs in this regime are used, for instance, to model the basic form of [cuckoo hashing](https://en.wikipedia.org/wiki/Cuckoo_hashing). When $$c=0$$ the result is a forest with high probability (and therefore perfect). See, for instance, _Introduction to Random Graphs_ (Frieze and Karonski), Section 2.1: "Sub-critical phase". 

When $$0<c<1$$ the result is with high probability a [pseudoforest](https://en.wikipedia.org/wiki/Pseudoforest) with at most one cycle per connected component, exactly the condition under which cuckoo hashing works. With probability bounded away from zero it's not just a pseudoforest, but a forest, and therefore perfect. To show that with probability bounded away from zero it's imperfect, let's look at the 5-vertex induced cycles (5-holes). The expected number of these turns out to be roughly $$\tfrac{c^5}{10}$$, a constant depending on $$c$$ but not on $$n$$ (see below for a more careful calculation of the number of holes of all sizes) and a similar calculation finds that the expected number of pairs of 5-holes is again roughly constant. By the [second moment method](https://en.wikipedia.org/wiki/Second_moment_method), the probability of seeing at least one 5-hole (and therefore being imperfect) is bounded away from zero.

When $$p=\omega(n)$$ one can partition the vertices into $$\omega(n)$$ subsets within which there is a bounded probability of the subset inducing an imperfect graph. With high probability, one of them does, and the whole graph is imperfect. And when $$p=\tfrac{c}{n}$$ with $$c>1$$ one can choose arbitrarily a subset of $$1/p$$ vertices,
whose induced subgraph follows the $$c=1$$ case, which we will handle next. This same sampling trick also shows that for $$0<c< 1$$, the probability of getting an imperfect graph varies monotonically and continuously with $$c$$, but we still need the $$c=1$$ case to know that this probability approaches one as $$c\to 1$$.

# Now we know how many holes

That leaves the case of $$c=1$$ and $$p\approx\tfrac1n$$, which I claim is imperfect with high probability. This is going to be a long sequence of steps so this might be a good time to introduce some notation. Let $$\mathcal{G}=G(n,p)$$ be the distribution we're drawing from, and let $$\mathsf{imperfect}$$ be the event that a graph is not perfect. We want to find a lower bound showing that

$$P_\mathcal{G}[\mathsf{imperfect}]=1-o(1),$$

where $$P_\mathcal{G}$$ is the probability of this event under distribution $$\mathcal{G}$$. We will do this by looking at odd induced cycles, up to some fixed length threshold $$t$$; let $$\mathsf{hole}$$ be the event that one of these short odd induced cycles exists. Then our first step is an easy one:

$$P_\mathcal{G}[\mathsf{imperfect}]\ge P_\mathcal{G}[\mathsf{hole}],$$

because a hole causes a graph to be imperfect, but it might be imperfect for other reasons (longer induced odd cycles, or their complements). Unfortunately, $$P_\mathcal{G}[\mathsf{hole}]$$ is difficult to calculate, but a related quantity, $$E_\mathcal{G}[\#\mathsf{holes}],$$ turns out to be much easier. Here, $$E_\mathcal{G}$$ means to take the expected value of a random variable $$\#\mathsf{holes}$$ that counts the number of odd induced cycles, again up to the same threshold $$t$$, for a graph drawn from $$\mathcal{G}$$.

By linearity of expectation, we can analyze separately the holes of each size and then sum their expected values. For a cycle of length $$k$$, this is $$\tfrac{1}{2k}$$, up to multiplicative error $$1\pm o(1)$$, because there are roughly $$n^k$$ linearly ordered $$k$$-tuples of vertices, each cyclic ordering (up to reversal) comes from $$2k$$ linear orders, and a cyclically ordered $$k$$-tuple has roughly $$n^{-k}$$ probability of appearing as a cycle. All of those "roughly"s, and the omitted calculation of the probability that when a cycle appears it is induced, are where the $$o(1)$$ error term comes from. The biggest contribution to this error term is that we are not assuming the edge probability is $$\frac1n$$, but only that it is within $$o(1)$$ of this. This contribution blows up proportionally to the lengths of the cycles, preventing us from allowing $$t$$ to vary with $$n$$.

If we count the expected number of induced 5-cycles, 7-cycles, 9-cycles, etc., all the cycle lengths that could prevent our graph from being perfect, we get (up to the same error)

$$\frac{1}{10}+\frac{1}{14}+\frac{1}{18}+\cdots+\frac{1}{2t}.$$

If this series were continued infinitely it would diverge, like the harmonic series (but with one term for every four of the harmonic series). Instead, when truncated at $$2t$$ in this way it has logarithmic growth, again like the harmonic series. This dominates the error term in our calculations so far, which we can summarize as:

$$E_\mathcal{G}[\#\mathsf{holes}]=\frac14\log t-O(1),$$

where log is the natural logarithm and the $$O(1)$$ term does not depend on $$t$$. Thus, with our choice of the hole length threshold $$t$$, we can make the expected number of holes arbitrarily large.

If the events that odd cycles appear were independent of each other, we would almost be done. [A very easy union bound in probability]({{site.baseurl}}{% post_url 2024-04-15-linkage %}) states that, for independent events whose expected number is $$\mu$$, the probability of getting at least one event is $$\ge 1-e^{-\mu}$$. Thus, for a "fake graph process" $$\mathcal{F}$$, a choice of an independent random event for each potential hole that has the same probability and same expected number as in $$\mathcal{G}$$, we would have

$$P_{\mathcal{F}}[\mathsf{hole}]\ge 1-\kappa t^{-1/4},$$

for some fixed constant $$\kappa$$. (I am deliberately avoiding $$O$$-notation here because we need to preserve the dependence on $$t$$, which would be lost as merely a constant if we used $$O$$-notation with $$n$$ as the variable.) This probability can be made arbitrarily close to one by making $$t$$ larger, almost what we want to prove, but for the wrong probability distribution, $$\mathcal{F}$$ instead of $$\mathcal{G}$$. In $$\mathcal{G}$$, most pairs of potential induced cycles are edge-disjoint and produce independent events. But when cycles overlap, they produce events that might be positively correlated (if they share an edge) or that might be disjoint (if both cycles cannot be simultaneously induced). All the rest of the work will be in showing that these dependences are small enough that they don't affect the probabilities of holes very much, and therefore that $$\mathcal{G}$$ also has a probability of holes that can be made arbitrarily close to one.

# Here's where I start complicating likely more than necessary

Two potential holes (cyclically ordered subsets of up to $$t$$ vertices that might induce an odd cycle) define independent events if they share at most one vertex. If two holes that are not independent appear in a random graph, they form a subgraph with at most $$2t-2$$ vertices and with fewer edges than vertices. The expected number of such subgraphs, and by [Markov's inequality](Markov's inequality) the probability of seeing even one of them, is $$O(\tfrac1n)$$. So we will not give up much by considering only random graphs in which the holes that appear are independent.

If we draw a graph that has a hole, but does not have two non-independent holes, then it has a unique non-empty maximal independent set of holes. And when something is unique, the probability that it exists is the same as its expected number. That is,

$$
\begin{aligned}
P_{\mathcal{G}}[\mathsf{imperfect}]
&\ge P_{\mathcal{G}}[\mathsf{hole}]\\
&\ge P_{\mathcal{G}}[\mathsf{MIS} \wedge \mathsf{no~overlap}]\\
&= E_{\mathcal{G}}[\#\mathsf{MIS} \cdot \mathsf{no~overlap}].
\end{aligned}$$

Here, multiplying by an event in the expected value means to multiply by $$1$$ or $$0$$ depending on whether or not the event happens. The formulas above are not quite the same as using conditional probability or conditional expectation, because we're still drawing a graph from the full distribution $$\mathcal{G}$$ rather than restricting the distribution to the graphs with no overlap, but that doesn't make much difference.

But maximal independent sets are a little tricky to count. Independent sets, without maximality, are easier. We can convert one into the other using some tricks with binomial coefficients. If there is one maximal independent set of size $$j$$, there are $$\tbinom{j}{i}$$ independent sets of size $$i$$. The alternating sum of binomial coefficients with fixed $$j$$ and variable $$i$$ is zero; this is just the [binomial expansion](https://en.wikipedia.org/wiki/Binomial_theorem) of $$(1-x)^j$$. If we leave out the $$i=0$$ term, we get one instead. Therefore, letting $$\#\mathsf{IS}_i$$ be the number of independent sets of exactly $$i>0$$ holes, we have:

$$\begin{aligned}
P_{\mathcal{G}}[\mathsf{imperfect}]
&\ge E_{\mathcal{G}}[\#\mathsf{MIS} \cdot \mathsf{no~overlap}]\\
&=\sum_{i>0} (-1)^{i+1} E_{\mathcal{G}}[\#\mathsf{IS}_i \cdot \mathsf{no~overlap}].
\end{aligned}$$

The partial sums of the alternating sum of binomial coefficients are just the binomial coefficients $$\tbinom{j-1}{i}$$, again with alternating signs. Leaving out the $$i=0$$ term doesn't affect the sign except on the last term. So if we truncate the alternating sum above to an odd number of terms, we will get an overestimate for the probability, and if we truncate to an even number of terms, we will get an underestimate. (This observation is, more or less, what the [Bonferroni inequalities](https://en.wikipedia.org/wiki/Bonferroni_inequalities) say.) We want an underestimate, so introducing a parameter $$s$$ for (half) the number of terms to keep, we have:

$$P_{\mathcal{G}}[\mathsf{imperfect}]
\ge \sum_{i=1}^{2s} (-1)^{i+1} E_{\mathcal{G}}[\#\mathsf{IS}_i \cdot \mathsf{no~overlap}].$$

The reason to truncate in this way is to limit the size of the independent sets, enabling the elimination of that pesky $$\mathsf{no~overlap}$$ term. If we see an independent set of $$i$$ holes in a graph from $$\mathcal{G}$$, it has $$O(it)$$ edges, each of which is part of another (overlapping) hole with probability $$O(\tfrac1n)$$. And as before the probability of an unrelated overlap is also $$O(\tfrac1n)$$. So by the union bound the probability that this independent set (conditioned on when it appears) is part of a graph with overlap is $$O(\tfrac{st}{n})$$. Eliminating the no overlap term only changes this independent set's contribution to the expectation by a multiplicative factor of $$1\pm O(\tfrac{st}{n})$$. All terms in the sum have multiplicative factors of the same form, so we can pull this factor out of the sum, giving:

$$P_{\mathcal{G}}[\mathsf{imperfect}]
\ge \bigl(1- O(\tfrac{st}{n})\bigr)\, \sum_{i=1}^{2s} (-1)^{i+1} E_{\mathcal{G}}[\#\mathsf{IS}_i].$$

# The triumphant return of the fake graph process

The fake graph process $$\mathcal{F}$$ does not describe actual graphs. Its states are sets of holes (chosen with the same individual probabilities as in $$\mathcal{G}$$) that are not guaranteed to be consistent with each other as part of a graph. And even if they are consistent, the process does not tell us enough to specify the rest of the graph, the part that is not in the chosen holes. Nevertheless it is a lot like $$\mathcal{G}$$ in some ways, including having a low probability of overlapping holes. It is also alike in its independent sets of holes having the same probabilities of existence, and therefore the same expected numbers. So when we have a formula using these expected numbers, we can substitute one process for another:

$$P_{\mathcal{G}}[\mathsf{imperfect}]
\ge \bigl(1- O(\tfrac{st}{n})\bigr)\, \sum_{i=1}^{2s} (-1)^{i+1} E_{\mathcal{F}}[\#\mathsf{IS}_i].$$

Now all we have to do is reverse the steps by which we got from the probability of a hole to this alternating sum of expected values, to reach the probability of a hole in $$\mathcal{F}$$, which we already know is close to one. But before we do, now (while we haven't imposed any conditions and everything is independent) is a good time to invoke [Chernoff bounds](https://en.wikipedia.org/wiki/Chernoff_bound). We need to change the truncated alternating sum from being an underestimate into an (eventual) overestimate, so that in the reversed steps the inequalities will still tend in the correct direction. We can do this by truncating to one more or one fewer step (it doesn't matter which); the difficulty is bounding how much this change in truncation can change the sum. Recall that the expected number of holes in $$\mathcal{F}$$ (allowing overlaps) is $$\tfrac14\log t-O(1)$$. By the multiplicative form of the Chernoff bound, the probability of seeing some large number $$j$$ of holes, larger than this expectation, is less than

$$\left(\frac{e\cdot\tfrac14\log t-O(1)}{j}\right)^j.$$

When there are exactly $$j$$ holes, there can be at most $$\tbinom{j}{i}$$ independent sets of size $$i$$. Multiplying this by the bound on the probability of seeing that many holes, and summing over all large $$j$$, gives us a bound on the top term in the alternating sum:

$$E_{\mathcal{F}}[\#\mathsf{IS}_{2s}]\le
\sum_{j\ge 2s}\binom{j}{2s}\left(\frac{e\cdot\tfrac14\log t-O(1)}{j}\right)^j.$$

For large enough values of $$s$$ (at least proportional to $$\log t$$), the exponential growth in the binomial coefficients is cancelled by the superexponential shrinkage in the probability bound, and this formula is dominated by its initial $$j=2s$$ term. For even larger values of $$s$$ (near-logarithmic in $$n$$), this formula becomes $$o(\tfrac1n)$$. This additive error term will be smaller than the multiplicative error term that we already have. So, by setting $$s$$ to be this big, we can drop the top term from the alternating sum, expand out the factor of $$s$$ appearing outside the sum, and achieve

$$P_{\mathcal{G}}[\mathsf{imperfect}]
\ge \bigl(1- O(\tfrac{\log n}{n})\bigr)\, \sum_{i=1}^{2s-1} (-1)^{i+1} E_{\mathcal{F}}[\#\mathsf{IS}_i].$$

As in $$\mathcal{G}$$, for each independent set contributing to this alternating sum, the probability that it is part of a system of holes with an overlap is $$O(st/n)$$, so if we impose the condition of no overlap we will only change its contribution to the alternating sum by another factor of the same magnitude as the error term we already have:

$$P_{\mathcal{G}}[\mathsf{imperfect}]
\ge \bigl(1- O(\tfrac{\log n}{n})\bigr)\, \sum_{i=1}^{2s-1} (-1)^{i+1} E_{\mathcal{F}}[\#\mathsf{IS}_i\cdot\mathsf{no~overlap}].$$

Because we now have an odd number of terms, this alternating sum is an upper bound on the untruncated alternating sum:

$$
\begin{aligned}
P_{\mathcal{G}}[\mathsf{imperfect}]
&\ge \bigl(1- O(\tfrac{\log n}{n})\bigr)\, \sum_{i>0} (-1)^{i+1} E_{\mathcal{F}}[\#\mathsf{IS}_i\cdot\mathsf{no~overlap}]\\
&=\bigl(1- O(\tfrac{\log n}{n})\bigr)E_{\mathcal{F}}[\#\mathsf{MIS}\cdot\mathsf{no~overlap}]\\
&=\bigl(1- O(\tfrac{\log n}{n})\bigr)P_{\mathcal{F}}[\mathsf{MIS}\wedge\mathsf{no~overlap}].
\end{aligned}$$

The events of an MIS with no overlap and of an overlap are disjoint, and together cover all draws from $$\mathcal{F}$$ that have holes. But the probability of an overlap is small, $$O(\tfrac1n)$$, and we have already bounded the probability of a hole.

$$
\begin{aligned}
P_{\mathcal{F}}[\mathsf{MIS}\wedge\mathsf{no~overlap}]
&=P_{\mathcal{F}}[\mathsf{hole}]-P_{\mathcal{F}}[\mathsf{overlap}]\\
&\ge 1-\kappa t^{-1/4}-O\left(\frac1n\right).\\
\end{aligned}$$

Plugging this into our inequalities and simplifying, we have:

$$P_{\mathcal{G}}[\mathsf{imperfect}]\ge 1-\kappa t^{-1/4}-o(1).$$

We can make this arbitrarily close to $$1$$ by fixing an appropriate choice of $$t$$ and letting $$n$$ be sufficiently large. Therefore, the probability of being imperfect, for a random graph with edge probability $$\approx\tfrac1n$$, is $$1-o(1)$$.

This situation, where we have a system of events in which each event is dependent with a low expected weight of other events, and we get an outcome similar to one where the events are entirely independent, reminds me a little of the [Lovász local lemma](https://en.wikipedia.org/wiki/Lov%C3%A1sz_local_lemma). I wonder whether there's a more general result about union lower bounds for nearly-independent distributions hiding here, or more likely whether someone has already published the more general result that I would need and I just don't know about it yet.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/112409464896457680))