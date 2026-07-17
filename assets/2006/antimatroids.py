# Reverse search for generating all antimatroids over k elements
# D. Eppstein, UC Irvine, 17 Jun 2006

# number of antimatroids with k labeled elements, k = 0, 1, 2, ...:
# 1, 1, 3, 22, 485, 59386

nelements = 5
nsets = 1 << nelements
top = 1L << (nsets - 1)
singletons = sum([1L<<(1<<i) for i in range(nelements)])
all = (1L << nsets) - 1

def bits(x):
    while x:
        b = x &~ (x - 1)
        yield b
        x &=~ b

def ispower(x):
    nbits = 0
    for b in bits(x):
        nbits += 1
        if nbits > 1:
            return False
    return nbits

logs = dict([(1L<<i,i) for i in range(nsets)])
def stringForSet(S):
    L = [str(logs[b]) for b in bits(logs[S])]
    return '{' + ','.join(L) + '}'

def stringForFam(S):
    return ", ".join([stringForSet(b) for b in bits(S)])

preds = {}
succs = {}
supersets = {}
subsets = {}
for i in range(nsets):
    p = 0
    for b in bits(i):
        p |= 1L << (i^b)
    preds[1L<<i] = p
    s = 0
    for b in bits((nsets-1)^i):
        s |= 1L << (i^b)
    succs[1L<<i] = s
    s = 0
    for j in range(nsets):
        if i & j == i:
            s |= 1L<<j
    supersets[i] = s
    s = 0
    for j in range(nsets):
        if i & j == j:
            s |= 1L<<j
    subsets[i] = s

excludes = {}
for i in range(nelements):
    x = 0
    for j in range(nsets):
        if (1L<<i) & j == 0:
            x |= (1L<<j)
    excludes[1L<<i] = x

def singlePred(S,b):
    """Does b have a single predecessor in S?"""
    return ispower(preds[b] & S)

def powersetbetween(lb,ub,S):
    between = supersets[lb] & subsets[ub]
    return between == between & S

def parent(S):
    """Add one set to S to form a larger antimatroid."""
    if S == all:
        return None
    
    ub = pos = nsets - 1
    lb = 0
    b = 0
    while True:
        # Invariant: not powersetbetween(lb,ub), lb subset pos subset ub
        # and either powersetbetween(pos,ub) or powersetbetween(pos|b,ub)

        # First test whether there is a powerset above pos.
        # if so, we can step downwards one step safely.
        if powersetbetween(pos,ub,S):
            for b in bits(pos &~ lb):
                if S & (1L<<(pos &~ b)):
                    break
            else:
                return None     # shouldn't happen!
            pos &=~ b
            continue
        
        # Here with powersetbetween(pos|b,ub) but not powersetbetween(pos,ub).
        # If the top subset not containing b, ub&~b, is in S,
        # then we can restrict to a smaller subfamily.
        if S & (1<<(ub &~ b)) != 0:
            lb = pos
            ub = pos = ub &~ b
            continue
            
        # Here with ub &~ b not part of S.
        # So if u is the union of the non-b supersets of pos,
        # it is missing some element q, and we can safely add u|q.
        above = S & supersets[pos] & subsets[ub] & excludes[b]
        u = logs[max(bits(above))]
        for b in bits(ub &~ u &~ b):
            return S | (1L << (u | b))
    
def succsOk(S,b):
    """Do successors of b have another predecessor in S &~ b?"""
    for q in bits(succs[b] & S):
        if singlePred(S,q):
            return False
    return True

def children(S):
    for b in bits(S):
        if b != top and singlePred(S,b) and \
                succsOk(S,b) and parent(S &~ b) == S:
            yield S &~ b

stack = [all]
nantimatroids = 0
while stack:
    x = stack.pop()
    nantimatroids += 1
#    print parent(x),'->',x,':',stringForFam(x)
    for y in children(x):
        stack.append(y)

print nantimatroids