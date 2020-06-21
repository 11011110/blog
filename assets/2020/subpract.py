from PADS.Eratosthenes import PracticalNumbers, primes, FactoredIntegers

reused = {}
def reuse(generator):
    if generator not in reused:
        reused[generator] = generator(),list()
    g,L = reused[generator]
    i = 0
    while True:
        if i >= len(L):
            L.append(g.next())
        yield L[i]
        i += 1

def mex(L):
    L = set(L)
    i = 0
    while i in L:
        i += 1
    return i

def options(n,subsetgen):
    for s in reuse(subsetgen):
        if s > n:
            return
        yield n-s

def nimvalues(subsetgen):
    values = []
    while True:
        values.append(mex(values[i] for i in options(len(values),subsetgen)))
        yield values[-1]

def ppositions(subsetgen):
    ppos = set()
    def isp(n):
        for i in options(n,subsetgen):
            if i in ppos:
                return False
        return True
    
    n = 0
    while True:
        if isp(n):
            ppos.add(n)
            yield n
        n += 1

def IsHardyRamanujan(factorization):
    n,e = 0,0
    rp = reuse(primes)
    while n < len(factorization):
        p = rp.next()
        if p not in factorization:
            return False
        if n > 0 and factorization[p] > e:
            return False
        e = factorization[p]
        n += 1
    return True

def HardyRamanujanNumbers():
    for n,F in FactoredIntegers():
        if IsHardyRamanujan(F):
            yield n

def SeriesParallel():
    return iter([1, 2, 4, 10, 24, 66, 180, 522, 1532, 4624, 14136, 43930, 137908, 437502, 1399068, 4507352, 14611576, 47633486, 156047204, 513477502, 1696305728, 5623993944, 18706733128, 62408176762, 208769240140, 700129713630, 2353386723912])

def Dime():
    for p in reuse(primes):
        yield p-1

nv = reuse(Dime) # or ppositions(HardyRamanujanNumbers) etc
last = 0
for i in range(100):
    print nv.next()
