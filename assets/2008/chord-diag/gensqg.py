# Generate isomorphism classes of chord diagrams

# without the triangle-free restriction, this is
# http://www.research.att.com/~njas/sequences/A054499

def TFCD(i):
    # triangle free chord diagrams with i chords,
    # up to isomorphism
    if not i:
        yield []
        return
    for D in TFCD(i-1):
        children = []
        for E in augment(D):
            if triangle_free(E):
                E = canonicalize(E)
                if E not in children and parent(E) == D:
                    children.append(E)
                    yield E

def normalize(D):
    # find lexicographically smallest renumbering of D
    renumbering = {}
    for x in D:
        if x not in renumbering:
            renumbering[x] = len(renumbering)
    return [renumbering[x] for x in D]

def reflection(D):
    # mirror diagram
    E = list(D)
    E.reverse()
    return normalize(E)

def rotations(D):
    # all rotations of a diagram
    for i in range(len(D)):
        yield normalize(D[i:] + D[:i])

def symmetries(D):
    # all symmetries of a diagram
    for E in rotations(D):
        yield E
    D = reflection(D)
    for E in rotations(D):
        yield E

def canonicalize(D):
    if not D:
        return []
    return min(symmetries(D))

def parent(D):
    E = [x for x in D if x != D[0]]
    return canonicalize(E)

def triangle_free(D):
    # test whether D has three mutually crossing chords
    # D must be normalized, but not necessarily canonicalized
    unclosed = unblocked = 0
    n = len(D)//2
    for x in D:
        bit = 1L << (n - x - 1)
        if bit&unclosed == 0:
            unclosed |= bit
            unblocked |= bit
        elif bit&unblocked == 0:
            return False
        else:
            # block all chords that still cross x except the latest one
            latest_to_cross = ubbit = unblocked &~ (unblocked - 1)
            while ubbit != bit:
                unblocked &=~ ubbit
                ubbit = unblocked &~ (unblocked - 1)
            unblocked |= latest_to_cross
            unblocked &=~ bit
            unclosed &=~ bit
            
            # unblock the chord blocked by x
            outer_chords = unclosed &~ (bit - 1)
            last_outer_chord = outer_chords &~ (outer_chords - 1)
            unblocked |= last_outer_chord
    return True

def augment(D):
    # all diagrams formed by adding one more chord to D
    # results are normalized but not canonicalized
    n = object()
    for i in range(len(D)+1):
        for j in range(i,len(D)+1):
            yield normalize(D[:i] + [n] + D[i:j] + [n] + D[j:])
            
def connected(D):
    # is this canonicalized chord diagram connected?
    for E in rotations(D):
        bits = 0
        numzeros = 0
        for x in E:
            bits ^= (1L<<x)
            if bits == 0:
                numzeros += 1
        if numzeros != 1:
            return False
    return True

for i in range(10):
    count = 0
    print "Triangle-free connected chord diagrams of length %d:" % i
    for D in TFCD(i):
        if connected(D):
#           print D
            count += 1
    print "total:",count
    print
