"""Count simple cycles on a width*n grid.
The technique is to set up a transfer matrix to describe a recurrence
that counts the number of partial cycles to the left of some column of
the grid in terms of the possible states within a single column.
Then, we simply multiply an initial vector (representing the leftmost
blank column) by powers of this matrix and look at the entry in the
resulting vector that represents a blank column after a completed cycle."""

import sys

# Union-find data structure from http://www.ics.uci.edu/~eppstein/PADS/
from UnionFind import UnionFind

try:
    width = int(sys.argv[-2])
    itercount = int(sys.argv[-1])
except:
    print "Width and number of entries must be given as command line arguments!"
    sys.exit(0)

def gencols(w):
    """Generate all possible columns of a simple cycle in a width*n grid.
    A column is represented as a tuple such as [1,0,1,0,2] where the
    zeros represent cells that are outside the cycle and the nonzeros
    represent cells that are inside, grouped into connected components
    according to the connectivity of the present and earlier rows.
    The all-zero vector represents blank columns to the left of the cycle;
    the special value None represents blank columns to the right."""
    if w == 1:
        yield [0]
        yield [1]
        yield None
    else:
        for parent in gencols(w-1):
            if parent:
                for symbol in range(max(parent)+2):
                    if parent[-1] == symbol or parent[-1]*symbol == 0:
                        yield parent + [symbol]
            else:
                yield parent

columns = list(gencols(width))

def statecount(initial,transition,sequence):
    """Count the number of times a DFA reaches each state"""
    counts = dict((x,0) for x in transition)
    state = initial
    for x in sequence:
        state = transition[state][x]
        counts[state] += 1
    return counts

def symbolize(P,Q):
    """Convert positions of P and Q to single input symbols"""
    for i in range(width):
        yield (P[i] != 0) + 2*(Q[i] != 0)
    yield 0     # one last transition to stable final state

compatibility = {
    # DFA for testing compatibility of two states P and Q
    #
    # Each key in this dict is a state of the DFA.
    # The value for the key is a four-letter string,
    # whose four letters are the next state for each possible
    # value in the symbolize() input sequence.
    
    "0": "0123",    # start state, P and Q both blank
    "1": "01X3",    # nonempty in P, empty in Q
    "2": "IX23",    # nonempty in Q -- possible start of island?
    "3": "01C3",    # nonempty both
    "X": "XXXX",    # we saw a degree-four vertex in the boundary
    "I": "0123",    # we saw an island (component of Q disconnected from P)
    "C": "0XCB",    # nonempty in Q -- possible start of bridge?
    "B": "01C3",    # we saw a bridge (two components in P connected by Q)
}

def compatible(P,Q):
    """Test whether two columns can be adjacent."""

    # First deal with the special end-of-cycle column
    if P is None:
        return Q is None
    elif Q is None:
        return max(P) == 1
    
    # Next check that the two columns don't combine to form degree 4 vertices
    C = statecount("0", compatibility, symbolize(P,Q))
    if C["X"]:
        return False
    
    # Do the counts of bridges and islands match up
    # (indicating that this combination does not form a hole)?
    if max(Q) != max(P) + C["I"] - C["B"]:
        return False

    # Use a union-find data structure to compute the components of P+Q
    U = UnionFind()
    for i in range(1,max(P)+1):
        U[(0,i)]
    for i in range(width):
        if Q[i]:
            U[(1,i)]
            if i > 0 and Q[i-1]:
                U.union((1,i-1),(1,i))
            if P[i]:
                U.union((1,i),(0,P[i]))

    # Make sure that the components of Q are what they say they are
    components = {} # map set names in U to numbers of components in Q
    for i in range(width):
        if Q[i]:
            if U[(1,i)] in components:
                if Q[i] != components[U[(1,i)]]:
                    return False
            elif Q[i] != len(components)+1:
                return False
            else:
                components[U[(1,i)]] = Q[i]

    # Make sure that every component of P is actually represented in the union
    U[None]
    for i in range(width):
        U.union((1,i),None)    # glom together everything nonzero in Q
    for i in range(1,max(P)+1):
        if U[(0,i)] != U[None]:
            return False    # found a component of P not part of the glom
    return True

M = [[int(compatible(P,Q)) for Q in columns] for P in columns]
A = M[0]

staterange = range(len(A))

for i in range(itercount):
    A = [sum(A[i]*M[i][j] for i in staterange) for j in staterange]
    print str(A[-1]) + ",",

print
