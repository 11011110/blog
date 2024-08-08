---
layout: post
title: Range voting considered harmful
date: 2024-08-07 18:09
---
Many of Wikipedia's articles on voting systems appear to me to have been overrun by advocacy for range voting. This is a system in which each voter rates each candidate on a numerical scale, often presented to the voters as representing their utility or the strength of their preference for each candidate. The ratings for each candidate are independent, in the sense that giving a rating to one candidate does not put any limits on the ratings that are allowed for a different candidate. The ratings from all the voters are then added, and the candidate with the highest sum wins. But in my experience (having seen it in action in polarized committees) range voting is a bad system, because there are multiple modes of using it and the system will give a disproportionate advantage to some of those modes.

In a range voting system, one can obviously vote truthfully, by assigning scores that represent one's best estimate of a preference for each candidate. But, like other voting systems, range voting presents an opportunity for strategic voting, in which voters choose their scores based on how it affects the outcome, with the knowledge that this may not accurately reflect their actual preferences. Being strategic is not in any way illegal and cannot be prevented, but different voters may choose to vote truthfully or strategically according to their own motivations or understanding of the situation:

* The goal for an individualist voter is to have the outcome reflect their own preferences. I think this is likely the case for most voters in most political elections. For such a voter, the rational choice is to vote strategically.

* Collectivist voters have preferences, but their goal is to have the outcome reflect the overall preferences of the whole electorate rather than their own. A collectivist voter, who believes that other voters are also collectivist, should vote truthfully in order to more accurately assess the preferences of the electorate.

* Norm-following voters may believe that systems like range voting are associated with certain norms of social behavior, for instance that one should vote truthfully regardless of one's goal for the overall election. For these voters, following those norms is more important than obtaining their preferred goal.

* Naive voters may see descriptions of the voting system as collecting their preferences, and vote truthfully without realizing that there is any alternative.

* Effort-avoiding voters may vote truthfully because they think it is easier than voting strategically. Alternatively, they might assign high scores to candidates they like and low scores to candidates they dislike, because that is even easier.

The problem with range voting is not so much that these options are possible; they are possible with all systems. But unlike other voting systems, range voting makes it so blatantly obvious how to vote strategically that strategic voting can become commonplace, leaving the truthful voters at a severe disadvantage. Many of the sources used to advocate range voting discuss it as if most or all voters are likely to be truthful, but there is no inherent reason for honesty (unlike other systems where honesty has the advantage of being much easier) and my experience is that expecting truthfulness from most or all range voters is naive to the point of disingenuousness.

The obvious way to vote strategically in range voting is to assign a top score to all candidates for whom you want to increase the probability of winning, and a bottom score to all other candidates, avoiding any of the middle score values. But rather than recounting anecdotes I thought it might be more interesting to formulate a simple model where this obvious strategic choice can be proven to be optimal, and moreover where the optimal choice of which candidates to score up or down can be calculated directly.

We have to make some assumptions to get going, and the following are somewhat artificial, but I think not too strange. The intuitive idea is that it is only the relative score between the top two candidates that would matter in an election, if only the voter knew who those two candidates were going to be. One can define the [regret](https://en.wikipedia.org/wiki/Regret_(decision_theory)) of a strategic voter to be how much the voter would prefer to have adjusted the scores of these two candidates, in retrospect, and then ask for an outcome that minimizes this regret. Essentially the same thing is formulated below in positive rather than negative terms.

* To normalize things, all voter scores are real numbers in the interval [0,1]. (It does not affect the argument whether these scores are arbitrary in this interval or limited to some discrete values.)

* There is a fixed pool of candidates to vote for, among whom we will pick a single winner; the rest are losers.

* Each voter has either a known preference ordering among all candidates.

* Each voter has some information about the likely election outcomes, which we formulate as a probability distribution over which pair of candidates is likely to be the top two. 

* When a given pair of pair of candidates is the top two, each voter would prefer to have assigned their favorite of these two candidates a score of 1 and the other candidate a score of 0. We define the regret of the voter to be the total difference between these ideal scores and the voter's actual scores.

* The goal of each voter is to vote in a way that minimizes their expected regret.

Really the only important aspect of these assumptions is that the value a strategic voter wants to optimize (the expected regret) is a linear function of their chosen scores. For  linear optimization, each score should be an extreme: 0 or 1. The regret-minimizing scores for a given voter are not necessarily monotonic in the voter's preferences, though; for instance, if a voter prefers $$p > q > r > s$$ but there is an overwhelming probability of seeing either $$pq$$ or $$rs$$ as the top two,  then the voter should score 1 for $$p$$ and $$r$$, and 0 for $$q$$ and $$s$$.

There's an easy method for a voter to determine which scores should be 0 and which should be 1, to achieve the minimum expected regret. For each candidate, sum over pairs of candidates to determine the probabilities that the candidate will be the favorite of the top two candidates, or the less-favorite of the top two candidates. If a candidate is more likely to be favorite than less-favorite, assign score 1; otherwise assign score 0.

So at least with these assumptions, in range voting, the strategic voters will always choose 0 and 1 for all their votes. One could try to put all the other voters on a more equal footing by telling them all to use 0 and 1. That is exactly what a different system, [approval voting](https://en.wikipedia.org/wiki/Approval_voting), does.
Alternatively, one could require the strategic voters (and everyone else) to spread out their scores more evenly, by providing a regularly-spaced set of score values and requiring each value to be used only for a single candidate. That is exactly what a different system, the [Borda count](https://en.wikipedia.org/wiki/Borda_count), does. 
But if we use range voting, and all voters are strategic, we get approval voting anyway, regardless of what we call it, and the only effect of calling it range voting is to give voters options that they will not use. And if we have a mix of strategic and truthful voters, the truthful voters are put at a disadvantage. Either way, range voting promises something different to the voters than what it delivers. If you think it's the system you should use, choose Borda or approval instead. If you don't like approval voting, then exactly the same disadvantages accrue to strategic range voting, because it ends up being the same as approval voting.

To be fair, there is one situation where I think range voting can work: where all participants are collectivist. In that situation, range voting collects more nuanced information than approval voting, exactly what the voters want to do. But although the assumption of collectivism might be true of some academic program committees and grant panels, I don't think it's true of most single-winner political elections.

Or, if you are strategic and think that your faction is going to be clever enough to vote strategically and your opponents are more likely to vote honestly, giving you an unfair advantage, then continue to advocate for range voting.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/112923756640262841))