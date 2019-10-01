# Solve univariate recurrence
# To solve, e.g., the recurrence T(n) = T(n-3) + T(n-4) + T(n-5), use
# python recur.py 3 4 5

import sys
lo = 1.
sizes = map(int,sys.argv[1:])
hi = len(sizes)
nsteps = 64

for i in range(nsteps):
    mid = (lo+hi)/2
    test = sum(mid**-j for j in sizes)
    if test > 1:
        lo = mid
    else:
        hi = mid

print ("%0.5f" % ((lo+hi)/2)) + "<sup>n</sup>"
