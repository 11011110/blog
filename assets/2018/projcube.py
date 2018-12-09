""" Find projections of hypercubes onto small 2d grids.
David Eppstein, UC Irvine, 2018-12-08."""

from PADS.Permutations import SteinhausJohnsonTrotter
from fractions import gcd

def plot(points):
    """Convert set of complex numbers to 2d ASCII-art drawing"""
    points = list(points)
    lox = min(q.real for q in points)
    loy = min(q.imag for q in points)
    points = {q-lox-loy*1j for q in points}
    hix = max(q.real for q in points)
    hiy = max(q.imag for q in points)
    for x in range(int(hix)+1):
        for y in range(int(hiy)+1):
            if x+y*1j in points:
                print 'O',
            else:
                print '.',
        print

def sums(vec,n=None):
    """All sums of zero or more elements of vec[0:n]"""
    if n is None:
        n = len(vec)
    if n == 0:
        yield 0
    else:
        for q in sums(vec,n-1):
            yield q
            yield q+vec[n-1]

def assignSigns(q,n=None):
    """All signings of a single permutation"""
    if n is None:
        n = len(q)
    while n > 0 and q[n-1] == 0:
        n -= 1
    if n == 0:
        yield q
    else:
        for r in assignSigns(q,n-1):
            yield r
        q[n-1] = -q[n-1]
        for r in assignSigns(q,n-1):
            yield r
        q[n-1] = -q[n-1]

def signedPermutations(seq):
    """All signed permutations in a given sequence"""
    for p in SteinhausJohnsonTrotter(seq):
        q = list(p)
        for r in assignSigns(q):
            yield r

def collinear(base,points,n=None):
    """Check whether a set of points (complex numbers) have 2+base collinear"""
    if n is None:
        n = len(points)
    lines = set()
    for i in range(n):
        p = points[i]
        x = int((p-base).real)
        y = int((p-base).imag)
        g = gcd(x,y)
        if g == 0:
            return True
        lines.add((x//g,y//g))
    return len(lines) != n

def generalPosition(points):
    """Check whether a set of points (complex numbers) have 3 collinear"""
    for n in range(2,len(points)):
        if collinear(points[n],points,n):
            return False
    return True

def maxfreq(seq):
    """How often does the most frequent element of seq occur?"""
    d = {}
    for x in seq:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1
    return max(d[x] for x in d)
            
def rulers(n,t,m=-1):
    """Sets of n numbers with at most two copies of each sum, total at most t, max m"""
    if n == 0:
        yield []
        return
    limit = t+1
    if m >= 0:
        limit = min(limit,m+1)
    for x in range(limit):
        for r in rulers(n-1,t-x,x):
            q = r + [x]
            if maxfreq(sums(q)) <= 2:
                yield q

sloppy=list(rulers(5,18))

for i in range(len(sloppy)):
    xcoords = sloppy[i]
    for possy in sloppy[:i+1]:
        for ycoords in signedPermutations(possy):
            gens = [xcoords[i]+ycoords[i]*1j for i in range(len(xcoords))]
            if not collinear(0,gens):
                points = list(sums(gens))
                if generalPosition(points):
                    plot(points)
                    print
