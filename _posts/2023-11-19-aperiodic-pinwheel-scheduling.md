---
layout: post
title: Aperiodic pinwheel scheduling using Beatty sequences
date: 2023-11-19 17:37
---
The [pinwheel scheduling](https://en.wikipedia.org/wiki/Pinwheel_scheduling) problem takes as input a collection of tasks, each taking unit time but needing to be repeated with some given maximum repeat time. The goal is to find a schedule: an infinite sequence of tasks to perform so that the gaps between each repetition of each task are no bigger than allowed. I drew the following illustration for Wikipedia, with the help of Adobe Illustrator's new AI-based vector drawing features; it shows tasks <span style="white-space:nowrap">A, B, and C</span> with repeat times <span style="white-space:nowrap">2, 4, and 5,</span> respectively, scheduled with the infinite repeating sequence ABACABAC... One real-world situation that this might model is scheduling equipment maintenance sessions, where certain kinds of equipment have different demands on how frequently they are maintained.

{: style="text-align:center"}
![A pinwheel scheduling instance]({{site.baseurl}}/assets/2023/pinwheel.svg)

But the name of the problem and the illustration are a little misleading. Periodic schedules, cycling through the same fixed subsequence of tasks, are allowed and always possible (when a schedule exists at all). But periodicity is not required. I want to describe a situation where aperiodicity can be helpful: it leads to a quick proof that certain kinds of inputs can always be scheduled.

The inputs in question are those with only two distinct repeat times, as studied by Holte et al. ["[Pinwheel scheduling with two distinct numbers](https://doi.org/10.1016%2F0304-3975%2892%2990365-M)", _Theor. Comput. Sci._ 1992]. You can describe these inputs by four numbers <span style="white-space:nowrap">$$n_1$$,</span> <span style="white-space:nowrap">$$n_2$$,</span> <span style="white-space:nowrap">$$r_1$$,</span> <span style="white-space:nowrap">and $$r_2$$,</span> where there are $$n_i$$ tasks with repeat <span style="white-space:nowrap">time $$r_i$$.</span> An obvious necessary condition for a schedule to exist is that the "density" $$n_1/r_1+n_2/r_2$$ must be at most one, and the main result of Holte et al. is that this density condition is also sufficient.

The easy case is when the density is exactly one. As an example, let <span style="white-space:nowrap">$$n_1=4$$,</span> <span style="white-space:nowrap">$$r_1=6$$,</span> <span style="white-space:nowrap">$$n_2=5$$,</span> and <span style="white-space:nowrap">$$r_2=15$$.</span> In order for the density to be one, the total density of the tasks of any type must be an integer multiple <span style="white-space:nowrap">of $$1/g$$,</span> where <span style="white-space:nowrap">$$g=\gcd(r_1,r_2)$$.</span> That forces each $$n_i$$ to be an integer multiple <span style="white-space:nowrap">of $$r_i/g$$.</span> You can group the tasks of <span style="white-space:nowrap">type $$i$$</span> into subsets of $$r_i/g$$ tasks, and schedule each subset as if it were a single task of repeat <span style="white-space:nowrap">time $$g$$,</span> reducing the problem to a trivial one in which all tasks have the same repeat time. In this case, aperiodicity is impossible.

This leaves the case when the density is less than one. Because of this density gap, it is possible to find an irrational number $$x_1$$ between $$r_1/n_1$$ <span style="white-space:nowrap">and $$1-r_2/n_2$$.</span> Then, symmetrically, $$x_2=1-x_1$$ will lie between $$r_2/n_2$$ <span style="white-space:nowrap">and $$1-r_1/n_1$$.</span> For any two irrational numbers summing to one, like $$x_1$$ <span style="white-space:nowrap">and $$x_2$$,</span> [Rayleigh's theorem](https://en.wikipedia.org/wiki/Beatty_sequence) states that the two [Beatty sequences](https://en.wikipedia.org/wiki/Beatty_sequence)

$$\left\lfloor\frac{j}{x_i}\right\rfloor,\quad j = 1, 2, 3, \dots$$

are complementary: each positive integer belongs to exactly one of these two sequences. For example, with <span style="white-space:nowrap">$$n_1=3$$,</span> <span style="white-space:nowrap">$$r_1=5$$,</span> <span style="white-space:nowrap">$$n_2=3$$,</span> <span style="white-space:nowrap">and $$r_2=8$$,</span> we may choose <span style="white-space:nowrap">$$x_1=(\sqrt5-1)/2\approx 0.618$$,</span> giving the two complementary Beatty sequences

$$1, 3, 4, 6, 8, 9, 11, 12, 14, 16, 17, 19, 21, 22, 24, 25, 27, \dots$$

(the [integer multiples of the golden ratio, rounded down](https://oeis.org/A000201)) and

$$2, 5, 7, 10, 13, 15, 18, 20, 23, 26, 28, 31, 34, 36, 39, 41, \dots$$

Now simply schedule all of the tasks with repeat time $$r_1$$ in time slots belonging to the first of these complementary Beatty sequences (choosing among these tasks in a periodic sequence), and schedule all of the tasks with repeat time $$r_2$$ in time slots belonging to the second sequence. For a task with repeat <span style="white-space:nowrap">time $$r_i$$,</span> this schedule will place the task in time slots whose spacing is sometimes $$\lfloor n_i/x_i\rfloor$$ and <span style="white-space:nowrap">sometimes $$\lceil n_i/x_i\rceil$$.</span> Because of the way we <span style="white-space:nowrap">chose $$x_i$$,</span> both of these are at <span style="white-space:nowrap">most $$r_i$$,</span> as required.

For the example with <span style="white-space:nowrap">$$n_1=3$$,</span> <span style="white-space:nowrap">$$r_1=10$$,</span> <span style="white-space:nowrap">$$n_2=2$$,</span> <span style="white-space:nowrap">$$r_2=3$$,</span> <span style="white-space:nowrap">and $$x_1=(\sqrt5-1)/2$$,</span> and with tasks labeled as <span style="white-space:nowrap">$$5a, 5b, 5c, 8a, 8b, 8c$$,</span> the schedule of tasks is

$$5a, 8a, 5b, 5c, 8b, 5a, 8c, 5b, 5c, 8a, 5a, 5b, 8b, 5c, 8c, 5a, 5b, \dots$$

So this method gives an aperiodic schedule, for any instance of pinwheel scheduling with two distinct repeat times and with density less than one, and an easy proof that having density at most one suffices for a schedule to exist when there are two repeat times.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/111440411902244020))