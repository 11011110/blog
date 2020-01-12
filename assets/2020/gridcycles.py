from math import log

memo = {}
def K(x,y,z):
    """Number of strings of length y from two sorted alphabets of lengths x,z"""
    if (x,y,z) in memo:
        return memo[(x,y,z)]
    if y == 0:
        result = 1
    else:
        # i = length of the last block of equal characters in the string
        # xx or zz = the largest remaining character in its alphabet
        result = sum(K(xx,y-i,z) for xx in range(x) for i in range(1,y+1)) +\
                 sum(K(x,y-i,zz) for zz in range(z) for i in range(1,y+1))
    memo[(x,y,z)] = result
    return result

def GC(n):
    """Number of polygonalizations of 3xn grid"""
    sum = 0
    for i in range(n-1):    # number of points in K(...) can be up to n-2
        mid = K(n-1,i,n-1)
        for left in range(n-1-i):
            right = n-2-i-left
            contrib = mid
            if left:
                contrib *= 2
            if right:
                contrib *= 2
            sum += contrib
    return sum

def exponent(p):
    return p**(-4*p) * (1-p)**(-2*(1-p)) * (1-2*p)**(-1*(1-2*p))

base = ( (1+5**0.5)/2 )**5

for n in range(2,50):
    print n,(base**n/(66*n))/GC(n),GC(n)