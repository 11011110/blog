---
layout: post
title: Gurobi versus the no-three-in-line problem
date: 2018-11-12 16:30
---
For the [no-three-in-line problem](https://en.wikipedia.org/wiki/No-three-in-line_problem), it has been known since the 1990s that $$n\times n$$ grids with $$n\le 46$$ have sets of $$2n$$ points with no three in line. Those results, by Achim Flammenkamp, were based on custom search software and a lot of compute time. I was curious to see how far one could get with more-modern but generic optimization codes, so this weekend I ran a little experiment.

I think that in this area, most general-purpose solvers can be reasonably divided into two categories: integer linear program solvers, and satisfiability solvers. For the no-three-in-line problem, we have $$0$$-$$1$$ integer variables ($$1$$ if a point is included, $$0$$ if it is excluded), linear constraints (the sum of variables on any line should be at most $$2$$), and a linear optimization criterion (maximize the sum of variables). So this led me to look at integer linear program solvers rather than satisfiability solvers. Based on [a comparison by Matt Strimas-Mackey](http://strimas.com/prioritization/ilp-performance/), I chose [Gurobi](http://www.gurobi.com/) over several open-source alternatives. Gurobi is not open source, but it is free for academic purposes.

This was my first experience with an ILP solver, and my impression was that everything "just worked". Gurobi was easy to download and install, easy to run, and easy to program following the model of their [simple Python example](http://www.gurobi.com/documentation/8.1/quickstart_windows/py_simple_python_example.html) in their Quick Start Guide.

On the other hand, although it worked quickly for small grids, it was far from being able to reach the grid sizes already solved by Flammenkamp. With the formulation of the problem that I used, the boundary between easy and difficult problems was between $$n=13$$ (five seconds to solve on my laptop) and $$n=14$$ (thirty minutes to solve). It's important to remember, though, that this was my first attempt at coding up anything as an integer linear program, and my first time using this system. So it's entirely likely that an expert user of the system would know some tricks that would let it get farther.

Perhaps it's also important to remember that for $$n=13$$ it's searching through a space of $$7.5\times 10^{50}$$ possible solutions, and for $$n=14$$ that blows up to approximately $$10^{59}$$. So the fact that it can solve these at all, and do so relatively quickly, is quite impressive.

In case anyone else wants to try it, here's my code:

{% highlight python %}
n = 14

from gurobipy import *
from fractions import gcd

# Construct the grid points and the lines through them
points = [(i,j) for i in range(n) for j in range(n)]
lines = {}
for p in points:
    for q in points:
        if p != q:
            a = p[1] - q[1]
            b = q[0] - p[0]
            c = p[0]*q[1] - p[1]*q[0]
            g = gcd(gcd(a,b),c)
            L = (a//g,b//g,c//g)
            if L not in lines:
                lines[L] = {p,q}
            else:
                lines[L].add(p)
                lines[L].add(q)

# Create an ILP with a 0-1 variable per grid point,
# maximizing the number of variables we set to 1
m = Model()
vars = {p: m.addVar(vtype=GRB.BINARY) for p in points}
m.setObjective(sum(vars[p] for p in points), GRB.MAXIMIZE)

# Add constraints for at most two points on each line
for L in lines:
    if len(lines[L]) > 2:
        m.addConstr(sum(vars[p] for p in lines[L]) <= 2)

# To speed things up tell it that we only care about perfect solutions
m.addConstr(sum(vars[p] for p in points) >= 2*n)

m.optimize()

for i in range(n):
    for j in range(n):
        s = "."
        if vars[i,j].x > 0.5:
            s = "O"
        print s,
    print
{% endhighlight %}

It's in Python 2 rather than Python 3 because somehow that's the default for my installation (probably because it's the default command-line python on my laptop).
The code after the optimize step produces a picture of the solution in crude ASCII graphics. Here's a prettier version of the $$14\times 14$$ solution:

{: style="text-align:center"}
![28 points in a 14x14 grid with no three in line]({{site.baseurl}}/assets/2018/no3il14x14.svg)

([G+](https://web.archive.org/web/20190210014916/https://plus.google.com/100003628603413742554/posts/aEhW29MVv2H), [$$\mathbb{M}$$](https://mathstodon.xyz/@11011110/101061128588762922))