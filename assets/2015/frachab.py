# Highly abundant numbers whose associated knapsack problem is
# solved optimally by the fractional knapsack problem

from PADS.Eratosthenes import primes
primeGenerator = primes()

from math import log

# list of quadruples [priority,prime,exponent,index]
active = []

def priority(p,e):
    """Priority of a prime p with given exponent e"""
    size = log(p)
    profit = log((p**(e+1)-1.)/(p**e-1))
    return profit/size
    
def expandActive():
    p = primeGenerator.next()
    active.append([priority(p,1),p,1,len(active)])

def frachab():
    """List of fractionally-optimal highly abundant numbers"""
    hab = 1
    expandActive()
    while True:
        yield hab
        q,p,e,i = max(active)
        hab *= p
        e = active[i][2] = e + 1
        active[i][0] = priority(p,e)
        if i == len(active) - 1:
            expandActive()

for hab in frachab():
    print hab

        