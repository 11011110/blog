# Check whether continued fraction for powers of pi is a good fit
# for the Gauss-Kuzmin distribution, using the chi-squared test
# (on the rounded binary logarithms of the values).
# This just packages up the data for R to do the test itself

from math import log

data = [
    [ 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 2, 1, 1, 2, 2, 2, 2, 1, 84, 2, 1, 1, 15, 3, 13, 1, 4, 2, 6, 6, 99, 1, 2, 2, 6, 3, 5, 1, 1, 6, 8, 1, 7, 1, 2, 3, 7, 1, 2, 1, 1, 12, 1, 1, 1, 3, 1, 1, 8, 1, 1, 2, 1, 6, 1, 1, 5, 2, 2, 3, 1, 2, 4, 4, 16, 1, 161, 45, 1, 22, 1, 2, 2, 1, 4, 1, 2, 24, 1, 2, 1, 3, 1, 2, 1 ], # https://oeis.org/A001203
    [ 1, 6, 1, 2, 47, 1, 8, 1, 1, 2, 2, 1, 1, 8, 3, 1, 10, 5, 1, 3, 1, 2, 1, 1, 3, 15, 1, 1, 2, 2, 1, 3, 2, 7, 1, 9, 18, 30, 2, 145, 1, 1, 17, 9, 1, 1, 1, 1, 7, 12, 1, 2, 1, 12, 1, 1, 4, 1, 5, 1, 1, 2, 3, 4, 1, 3, 2, 9, 1, 20, 11, 14, 3, 1, 1, 7, 1, 1, 1, 1, 2, 268, 2, 1, 25, 3, 8, 1, 6, 1, 1, 22, 1, 1 ], # https://oeis.org/A058284
    [ 159, 3, 7, 1, 13, 2, 1, 3, 1, 12, 2, 2, 4, 34, 2, 43, 3, 1, 3, 2, 1, 1, 5, 1, 1, 4, 1, 5, 4, 2, 4, 11, 3, 3, 1, 1, 2, 1, 7, 2, 1, 1, 3, 1, 12, 3, 1, 9, 2, 1, 8, 23, 1, 45, 1, 1, 2, 1, 23, 3, 2, 2, 2, 1, 2, 2, 1, 1, 2, 2, 1, 16, 1, 15, 1, 2, 4, 1, 2, 1, 12, 8, 1, 8, 2, 1, 7, 2, 2, 4, 1, 11, 2, 23 ], # https://oeis.org/A058285
    [  2, 2, 3, 1, 16539, 1, 6, 7, 6, 8, 6, 3, 9, 1, 1, 1, 18, 1, 4, 1, 13, 1, 2, 1, 127, 1, 1, 1, 4, 1, 6, 1, 1, 1, 10, 10, 1, 1, 2, 1, 2, 1, 5, 1, 1, 10, 1, 3, 2, 1, 1, 4, 9, 1, 7, 70, 1, 13, 1, 2, 6, 1, 2, 24, 5, 2, 6, 1, 1, 1, 8, 1, 1, 11, 2, 1, 1, 4, 3, 1, 3, 2, 2, 1, 7, 1, 4, 1, 22, 2, 1, 2, 3, 1 ], # https://oeis.org/A058286
]

# Compute bucket probabilities

def gk(n):
    # What is GK probability of given value?
    return -log(1-1./(1+n)**2)/log(2.)

nbuckets = 6

def bucket(n):
    # Group values by log2, in range 0..5
    return min(nbuckets-1,int(log(n+0.01)/log(2)))

bucketprobs = [0]*nbuckets
i = 0
while True:
    i += 1
    b = bucket(i)
    if b == nbuckets - 1:
        break
    bucketprobs[b] += gk(i)
bucketprobs[-1] = 1. - sum(bucketprobs)

def test(seq):
    counts = [0]*nbuckets
    for x in seq:
        counts[bucket(x)] += 1
    print("counts <- c(%s)" % str(counts)[1:-1])
    print("res <- chisq.test(counts, p = c(%s))" % str(bucketprobs)[1:-1])
    print("res")

alldata = data[0]+data[1]+data[2]+data[3]
test(alldata)
