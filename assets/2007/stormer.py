# Implementation of Stormer's theorem (Lehmer 1964 simplification)
# using exact integer arithmetic

import sys
from math import sqrt

def gcd(p,q):
    while q:
        p,q = q,p%q
    return abs(p)

def isqrt(n):
    """Approximate square root using only integer arithmetic"""
    i = 1
    while 1L<<i < n:
        i += i
    lo,hi = i>>1,i
    while hi - lo > 1:
        mid = (hi + lo)>>1
        if 1<<mid < n:
            lo = mid
        else:
            hi = mid
    r = 1<<(hi//2)
    s = 0
    while r != s:
        r,s = (r+n//r)>>1,r
    return r

def FloorQuadraticIrrational(a,b,c,d):
    """Exact calculation of int(r), where r=(a + b sqrt(c))/d."""
    def tooBig(x):
        y = (d*x)**2 - 2*a*d*x + a*a-b*b*c    # polynomial for which r is root
        if y == 0:
            raise ValueError("input is not irrational")
        return y > 0
    
    try:
        x = int((a+b*sqrt(c))/d)  # good start, but not exact for large a,b,c
    except OverflowError:
        x = (a+b*isqrt(c))//d
    e = 1                   # prepare doubling search for initial interval
    if tooBig(x):           # unlikely
        while tooBig(x-e):
            e += e
        lo,hi = x-e,x-(e>>1)
    else:                   # more likely case
        while not tooBig(x+e):
            e += e
        lo,hi = x+(e>>1),x+e
    while hi-lo > 1:
        mid = (hi+lo)>>1
        if tooBig(mid):
            hi = mid
        else:
            lo = mid
    return lo   

def SquareRootConvergents(root):
    """Generate sequence of convergents h,k for sqrt(root)."""
    h,hh = 1,0
    k,kk = 0,1
    a,b,c,d = 0,1,root,1
    while True:
        fqi = FloorQuadraticIrrational(a,b,c,d)
        h,hh = h*fqi+hh,h
        k,kk = k*fqi+kk,k
        yield (h,k)
        a -= d*fqi
        a,b,c,d = a*d,-b*d,c,a*a-c*b*b
        g = gcd(a,b)
        g = gcd(g,d)
        a,b,c,d = a//g,b//g,c,d//g

def Pell(D):
    """Generate sequence of solutions x,y for x**2 - D*y**2 = 1."""
    for x,y in SquareRootConvergents(D):
        if x**2 - D*y**2 == 1:
            break   # use continued fraction only to get first soln
    a,b = x,y
    while True:     # generate pairs of the form (a+b sqrt(D))**i
        yield x,y
        x,y = a*x+D*b*y,b*x+a*y

def subsets(L):
    def binary(x,seq):
        for L in seq:
            yield L
            L.append(x)
            yield L
            L.pop()
    seq = [[]]
    for x in L:
        seq = binary(x,seq)
    return seq

def product(L):
    p = 1
    for x in L:
        p *= x
    return p

def IsSmooth(q,primes):
    for p in primes:
        while q % p == 0:
            q //= p
    return q == 1

def Stormer(primes):
    nterms = max(3,(max(primes)+1)>>1)
    for S in subsets(primes):
        if S == [2]:   # skip empty set
            continue
        xy = Pell(2*product(S))
        for i in range(nterms):
            x,y = xy.next()
            if IsSmooth(y,primes):
                z = (x - 1) >> 1
                yield z,z+1
            elif i == 0:
                break

if len(sys.argv) < 2 or "-h" in sys.argv or "--help" in sys.argv:
    print "This program lists pairs x, y of consecutive numbers"
    print "the prime factors of which are all among the given primes"
    print
    print "Usage: stormer p1 p2 p3 ..."
    sys.exit(0)

primes = [int(s) for s in sys.argv[1:]]
for i in range(len(primes)):
    for j in range(i):
        if gcd(primes[i],primes[j]) != 1:
            raise ValueError("%d and %d are not distinct primes" % (primes[i],primes[j]))

L = list(Stormer(primes))
L.sort()
for pair in L:
    print "%d, %d" % pair
