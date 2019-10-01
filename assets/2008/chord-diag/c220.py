# Draw the squaregraph dual to Ageev's 220-chord
# 5-chromatic triangle-free chord diagram

from cmath import pi, exp
from svgGraph import drawLayered, parseArgs

scale = 4.0

def c22():
    c = [object() for i in range(23)]
    return [ c[22],c[21],c[20],c[19],c[18],c[17] ], \
           [ c[16],c[17],c[1],c[11],c[10],c[15],c[16],c[18], \
             c[2],c[14],c[15],c[3],c[9],c[13],c[14],c[10], \
             c[8],c[12],c[13],c[11],c[19],c[7],c[12],c[20], \
             c[4],c[6],c[7],c[8],c[9],c[21],c[5],c[6],c[22] ], \
           [ c[5],c[4],c[3],c[2],c[1] ]

def mirrorcross(component):
    """
    Component should be a function returning a triple of lists.
    The first list in the triple is a sequence of parallel chords.
    The second list in the pair is part of a chord diagram forming
    two sequences of parallel chords, and the third list is the other
    sequence of parallel chords. Concatenating the three lists should
    produce a valid triangle-free chord diagram. The result is
    a pair of lists, suitable for terzarima.
    """
    a,b,c = component()
    d,e,f = component()
    d.reverse()
    e.reverse()
    f.reverse()
    return b+f+c+e,d+a

def c44():
    return mirrorcross(c22)

def terzarima(component,n):
    """
    Component should be a function returning a pair of lists.
    The first list in the pair is part of a chord diagram forming
    a sequence of parallel chords, and the second list is the resulting
    sequence of parallel chords. Concatenating the two lists should
    produce a valid triangle-free chord diagram.
    """
    c = [component() for i in range(n)]
    out = []
    for i in range(n):
        out += c[i][0]
        out += c[i-1][1]
    return out

chords = terzarima(c44,5)


# Process the diagram finding the first and last position of each chord
biggest_bit = 1
firstpos = {}
lastpos = {}
chordbit = {}
bitchord = {}
for i in range(len(chords)):
    if chords[i] in firstpos:
        lastpos[chords[i]] = i
        chordbit[chords[i]] = biggest_bit
        bitchord[biggest_bit] = chords[i]
        biggest_bit <<= 1
    else:
        firstpos[chords[i]] = i

# Make partial cube bitvector labels for each chord
chord_names = firstpos.keys()
upper = {}
for x in chord_names:
    upper[x] = chordbit[x]
    for y in chord_names:
        if firstpos[y] < firstpos[x] < lastpos[x] < lastpos[y]:
            upper[x] |= chordbit[y]

def vertices():
    yield 0
    for x in chords:
        yield upper[x]
        for y in chords:
            if firstpos[x] < firstpos[y] < lastpos[x] < lastpos[y]:
                yield upper[x] | upper[y]

def edges():
    for x in chords:
        yield (upper[x], upper[x] &~ chordbit[x])
        for y in chords:
            if firstpos[x] < firstpos[y] < lastpos[x] < lastpos[y]:
                yield (upper[x]|upper[y], (upper[x]|upper[y]) &~ chordbit[x])
                yield (upper[x]|upper[y], (upper[x]|upper[y]) &~ chordbit[y])

# Compute difference in vertex positions corresponding to each medium token
# All vectors are represented as complex numbers!
def normalize(vec):
	return scale * vec/abs(vec)

factor = 2.0j * pi / len(chords)
offset = {}
for x in chord_names:
    offset[x] = normalize(exp(factor*lastpos[x]) - exp(factor*firstpos[x]))

positions = {}
for v in vertices():
    pos = 0
    x = v
    while x:
        b = x &~ (x-1)
        pos += offset[bitchord[b]]
        x &=~ b
    positions[v] = pos

# Draw it!
		
keys, args = parseArgs()

if not keys.get('title',None):
    keys['title'] = 'Squaregraph'

drawLayered(positions, list(edges()), **keys)
