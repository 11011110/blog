---
layout: post
title: Generating fibbinary numbers, three ways
date: 2021-10-02 13:53
---
I just added to Wikipedia two articles on the [Jordan–Pólya numbers](https://en.wikipedia.org/wiki/Jordan%E2%80%93P%C3%B3lya_number) and [fibbinary numbers](https://en.wikipedia.org/wiki/Fibbinary_number), two integer sequences used in [my recent paper on Egyptian fractions]({{site.baseurl}}{% post_url 2021-09-24-which-integer-sequences %}). Jordan–Pólya numbers are the products of factorials, while the fibbinary numbers are the ones with binary representations having no two consecutive 1's. The OEIS page on the fibbinary numbers, [A003714](https://oeis.org/A003714), lists many ways of generating this sequence algorithmically, of which most are boring or slow (generate all binary numbers and test which ones belong to the sequence; you can test if a variable `x` is fibbinary by checking that `x&(x>>1)` is zero). I thought it might be interesting to highlight two of those methods that are a little more clever and generate these numbers in small numbers of operations.

Some functional languages, and in part Python even though it's mostly not functional, have a notion of a stream, a potentially infinite sequence of values generated by a coroutine. In Python, you can program these using [simple generators](https://www.python.org/dev/peps/pep-0255/) and the `yield` keyword. I wrote here long ago about [methods for using generators recursively]({{site.baseurl}}{% post_url 2011-10-02-generating-permutations-with %}): a generator can call itself, manipulate the resulting sequence of values, and pass them on to its output. It's actually a very old idea, used for instance to generate [regular numbers](https://en.wikipedia.org/wiki/Regular_number) by Dijkstra [in his 1976 book _A Discipline of Programming_](http://web.cecs.pdx.edu/~black/AdvancedProgramming/Lectures/Smalltalk%20II/Dijkstra%20on%20Hamming%27s%20Problem.pdf). Reinhard Zumkeller used the same idea to generate the fibbinary numbers in Haskell, based on the observation that the sequence of positive fibbinary numbers can be generated, starting from the number 1, by two operations, doubling smaller values or replacing a smaller value $$x$$ with $$4x+1$$. Here is is, translated into Python:

{% highlight python %}
from heapq import merge

def affine(stream,a,b):
    for x in stream:
        yield x*a+b

def fibbinary():
    yield 1
    for x in merge(affine(fibbinary(),2,0),affine(fibbinary(),4,1)):
        yield x
{% endhighlight %}

It's elegant, but has a couple of minor flaws. First, it omits the number $$0$$, and while it can be modified to include $$0$$, the modifications make the code messier. But second, it takes more than a constant amount of time per element to generate each sequence element. A fibbinary number $$x$$ has to be generated from a sequence of smaller elements by repeated doubling and quadrupling, and that takes $$\log x$$ steps per element. Even if we assume those steps to take constant time each, generating the first $$n$$ elements in this way takes time $$\Theta(n\log n)$$. It's better than the $$\Theta(n^{\log_\varphi 2})\approx n^{1.44}$$ that you would get from generate-and-test, but still not as good as we might hope for. One way to fix this would be to memoize the generator, so that the recursive calls look at a stored copy of the sequence generated by the outer call rather than generating the same sequence redundantly, but this again makes the code messier and also takes more storage than necessary.

Instead, Jörg Arndt observed that you can generate each fibbinary number directly from the previous one by a process closely resembling binary addition. Adding one to a binary number sets the first available bit from zero to one, and zeros out all the smaller bits; here, a bit is available if it is already zero. Finding the next fibbinary number does the same thing, but with a different definition of availability: a bit is available if both it and the next larger bit are zero. We can find the available bit using binary addition on a modified word that fills in bits whose neighbor is nonzero. Using this idea, we can generate the fibbinary numbers in a constant number of bitwise binary word-level operations per number. Here it is again in Python, translated from Arndt's C++ and simplified based on [a comment by efroach76](https://mathstodon.xyz/@efroach76/107037399683569338):

{% highlight python %}
def fibbinary():
    x = 0
    while True:
        yield x
        y = ~(x >> 1)
        x = (x - y) & y
{% endhighlight %}

It's even possible to use the same idea to generate the fibbinary numbers in a constant amortized number of bit-level operations per number, although this ends up being a little less efficient in practice because high-level languages end up translating all these bit operations into word operations anyway.

{% highlight python %}
def fibbinary():
    x = 0
    while True:
        yield x
        y = 1
        while x & (y | (y<<1)) != 0:
            x &=~ y
            y <<= 1
        x |= y
{% endhighlight %}

The inner loop ends immediately at fibbinary numbers whose successor is odd (at positions given by the ones of the [Fibonacci word](https://en.wikipedia.org/wiki/Fibonacci_word)), whose fraction of the total is $$1-1/\varphi\approx 0.382$$, where $$\varphi$$ is the golden ratio. It ends in two steps for the remaining values when their next bit is odd, in the same proportion, and so on. So the average number of steps for the inner loop adds in a geometric series to $$O(1)$$.

([Discuss on Mastodon](https://mathstodon.xyz/@11011110/107034017632258123))