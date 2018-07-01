"""CircularLombardi - draw circular Lombardi drawings of regular graphs
David Eppstein, UC Irvine, October 2010

For usage information type "python CircularLombardi.py"
without any additional arguments.
"""

from pyx import canvas,path,color
from optparse import OptionParser
from math import *
import sys

# ============================================================
#   Pre-determined graphs by name
# ============================================================

namedGraphs = {
    # 3-regular
    "bidiakis": ['[-4,6,4;-]^2'],
    "ccc3": ['[2,9,-2;-]^4'],
    "cube3": ['[3;-]^4'],
    "f26a": ['[7;-]^13'],
    "franklin": ['[5;-]^6'],
    "frucht": ['[2,-4,-2,2,-5,-2,2,3,-2,4,-3,5]'],
    "heawood": ['[5;-]^7'],
    "mcgee": ['[-7,12,7]^8'],
    "truncoct": ['[3,-7,7,-3]^6'],
    "trunctet": ['[2,6,-2]^4'],
    "wagner": ['4^8'],
    "k44": ['-a', '3^8', '1^8'],
#    "k44": ['[-3;-]^4', '[3;-]^4'],
    
    # 4-regular
    "chvatal": ['[6,-3,6;-]^2', '[-3,3]^6'],
    "cube4": ['[7,5;-]^4', '[3;-]^8'],
    "holt": ['-a', '[3,6,12]^9', '[2,2,5]^9'],
    "folkman": ['[5,-5,-7,7]^5', '[-5,-7;-]^5'],
    "paley9": ['-a', '[2,-1,-1]^3', '3^9'],
    # An axbToroidal Grid: Cartesian Product of 2 cycles of size a and b
    #   Generic form: [1,1,1-a]^b, b^(a*b)]
    "torus33": ['-a', '[1,1,-2]^3', '3^9'],    # Also Paley9 really
    "torus44": ['-a', '[1,1,1,-3]^4', '4^16'],  # Also cube4 really
    "torus55": ['-a', '[1,1,1,1,-4]^5', '5^25'],
    "torus35": ['-a', '[1,1,-2]^5', '5^15'],

    # Not sure if worth keeping but I spent time getting a matching :-)
    # "torus44b": ['[3,-3,-5,-3,3,5,3,-3]^2', '[7,5,3,9,7,-3,-5,-7]^2'],
                        
    # 5-regular
    "clebsch": ['[-6,-6;-]^4', '[3,5,3,-7]^4'],
    "cube5": ['[3,5,3,-3;-]^4', '[7,13,11,9,7,5,3,-7;-]^2', '[15,-3,-5,-7,-9,-11,-13,-15;-]^2'],
    "icosahedron": ['[3;-]^6', '[4,2]^6'],

    # 6-regular
    "shrikhande": ['[5,5,5,-3]^4', '4^16'],
    "paley13": ['3^13', '4^13'],
}

# ============================================================
#   Command-line options
# ============================================================

parser = OptionParser()

parser.add_option("-f","--format", dest="show_format", action="store_true",
                  help = "describe the graph input format and exit")

parser.add_option("-a","--acyclic", dest="acyclic",
                  action="store_true", default=False,
                  help = "avoid the default assumption of a Hamiltonian cycle")

parser.add_option("-n","--names", dest="show_names", action="store_true",
                  help = "show a description of graph names and exit")

parser.add_option("-s","--scale", dest="scale", action="store",
                  type="float", default="1.0",
                  help = "size of overall drawing relative to default")

parser.add_option("-r","--radius",dest="radius", action="store",
                  type="float", default="1.0",
                  help = "radius of vertices relative to default")

parser.add_option("-c","--color",dest="color", action="store",
                  type="string", default="red",
                  help = "vertex color (e.g. blue or 76B3DF)")

parser.add_option("-o","--outline", dest="outline", action="store_true",
                  help = "avoid drawing outlines around vertices")

# Hack to fix up unbracketed args with numerical values
# so optparse doesn't think they're options
for i in range(1,len(sys.argv)):
    if sys.argv[i][0] == '-' and sys.argv[i][1] in '0123456789':
        caret = sys.argv[i].find('^')
        if caret < 0:
            sys.argv[i] = '[' + sys.argv[i] + ']'
        else:
            sys.argv[i] = '[' + sys.argv[i][:caret] + ']' + sys.argv[i][caret:]

options,args = parser.parse_args()

def abort(message):
    print >>sys.stderr,message
    sys.exit(-1)

if options.show_names:
    if len(args) == 1:
        graphName = args[0]
    else:
        graphName = None
    if args:
        if graphName not in namedGraphs:
            print '''Graph name''',args[-1],'''is not recognized.
Run
    python CircularLombardi --names
without any command line arguments to get a list of recognized names.'''
        else:
            print graphName,"is equivalent to",namedGraphs[graphName]
            sys.exit(0)
    print '''This program has built into it a set of graph names that may
be used as the command-line argument to specify the graph to be
drawn. They are:
'''
    graphs = namedGraphs.items()
    graphs.sort()
    graphs = [("Name","Description"),("====","===========")] + graphs
    for name,description in graphs:
        print "    " + name + " "*(20-len(name)),
        if type(description) == list:
            for x in description:
                print x,
            print
        else:
            print description
    sys.exit(0)

if options.show_format:
    print '''The graph should be described as a sequence of strings,
each of which specifies either a 1-factor (perfect matching) or 2-factor
of the given graph. By default, the graph is the union of these factors
with a Hamiltonian cycle, but the -a option causes it to be the union
only of the specified factors.

Each string has the format [x,y,z] or [x,y,z]^e where x, y, z, etc are
all numbers, much as in the standard LCF notation for 3-regular Hamiltonian
graphs (for which see http://en.wikipedia.org/wiki/LCF_notation).
As in LCF notation, if e is present it specifies a repetition count:
[x,y,z]^3 is the same as [x,y,z,x,y,z,x,y,z]. The brackets are optional,
and (after the repetition counts are expanded) each string should have
the same number of values in it, which is the number of vertices in the graph.

The value at position i of one of the input strings indicates the set of
neighboring vertices to the vertex at position i (in cyclic order) in
the drawing of the graph. If x is the number at position i, then vertex i
will be adjacent to vertex (i + x) mod n. For a string that specifies a
matching, the value at position (i + x) mod n should be -x, indicating a
reciprocal link. For a string that specifies a 2-factor, the value at
position (i + x) mod n should be the offset of the other neighbor of
that vertex, the neighbor that is not at position i.

The edges within a single factor will all be drawn with the same angle
of incidence to the circle on which the vertices all lie. In general,
factors that are earlier in the argument list will be drawn closer
to the center of the circle, and the default Hamiltonian cycle will be
drawn as close as possible to parallel to the circle.

If the vertex degree is congruent to 2 mod 4 and the default Hamiltonian
cycle is not included, at least two of the input strings must specify
matchings. In this case, the first input string that specifies a matching
will be drawn with its edges perpendicular to and inside the circle,
and the second one will be drawn with its edges perpendicular to and
outside the circle.
'''
    sys.exit(0)

if not args:
    print '''This program draws regular graphs in Lombardi style:
the edges are circular arcs that meet at equal angles at each vertex.
To use it, type
    python CircularLombardi.py [graph] >output.svg
to a command line, where [graph] is replaced by a description
of the graph to be drawn.

For help with the input format for graph descriptions, type
    python CircularLombardi.py --format

For a list of other command line options, type
    python CircularLombardi.py --help
'''
    sys.exit(0)

# ============================================================
#   Input format decryption
# ============================================================

if len(args) == 1 and args[0] in namedGraphs:
    args = namedGraphs[args[0]]
    if args[0] in ['-a', '--acyclic']:  # Quick and dirty option re-parse
        options.acyclic = True
        args = args[1:]

def decodeLCF(lcf):
    """Translate LCF string into a sequence of numbers."""
    caret = lcf.find("^")
    if caret < 0:
        caret = lcf.find("]")
    if caret >= 0 and caret < len(lcf)-1:
        exponent = int(lcf[caret+1:])
        lcf = lcf[:caret]
    else:
        exponent = 1
    if lcf.startswith("["):
        lcf = lcf[1:]
    if lcf.endswith("]"):
        lcf = lcf[:-1]
    while lcf.find(';') >= 0:
        semi = lcf.find(';')
        lcf = lcf[:semi] + ',' + lcf[semi+1:]
    lcf = [x.strip() for x in lcf.split(",")]
    palindrome = False
    if lcf[-1] == "-":
        palindrome = True
        lcf.pop()
    lcf = [int(x) for x in lcf]
    if palindrome:
        fcl = [-x for x in lcf]
        fcl.reverse()
        lcf += fcl
    return lcf*exponent
    
def computeDegree(lcf):
    if 0 in lcf:
        raise Exception("Self-loops not allowed")
    n = len(lcf)
    matched = [(lcf[i] + lcf[(i+lcf[i])%n])%n == 0 for i in range(n)]
    if n % 2 == 0:  # Fix up halfway-across matching, sign irrelevant
        h = n//2
        for i in range(h):
            if abs(lcf[i]) == h and abs(lcf[i+h]) == h:
                matched[i] = matched[i+h] = True
    if matched == [False]*n:
        return 2
    elif matched == [True]*n:
        return 1
    else:
        raise Exception("Inconsistent degrees in factor")

factors = []
degrees = []
for x in args:
    try:
        factors.append(decodeLCF(x))
        degrees.append(computeDegree(factors[-1]))
    except Exception, e:
        abort("Invalid input format: %s" % e)

lengths = [len(x) for x in factors]
if lengths != [lengths[0]]*len(lengths):
    abort("Not all factors have the same lengths")
vertices = lengths[0]

if options.acyclic:
    degree = sum(degrees)
else:
    degree = sum(degrees) + 2

# ============================================================
#   Assign edges to angles
# ============================================================

innermost = -degree
if (degree % 4 == 2 and not options.acyclic) or (degree % 4 == 0 and options.acyclic):
    innermost += 2
elif 1 not in degrees:
    abort("Unable to draw perpendicular to the circle without a 1-factor.")

angles = range(innermost,degree+1,4)

# Find angle closest to 0 to use for Hamiltonian cycle
HamiltonianAngle = None
if not options.acyclic:
    HamiltonianAngle = min((abs(x),x) for x in angles)[1]

def anglefactors():
    """Generate pairs (angle,list of factor indices)."""
    used = [False]*len(factors)
    for a in angles:
        if a == HamiltonianAngle:
            yield a,[]
            continue
        elif abs(a) == degree:
            targetdegree = 1
        else:
            targetdegree = 2
        factorsubset = []
        for i in range(len(factors)):
            if not used[i] and degrees[i] <= targetdegree:
                used[i] = True
                factorsubset.append(i)
                targetdegree -= degrees[i]
        yield a,factorsubset

def anglegraphs():
    """Generate pairs (angle,subgraph to draw with that angle)."""
    for a,f in anglefactors():
        if not f:
            yield a,[[(i+1)%vertices,(i-1)%vertices] for i in range(vertices)]
        else:
            G = [[] for i in range(vertices)]
            for i in f:
                for j in range(vertices):
                    G[j].append((j+factors[i][j])%vertices)
            yield a,G

def anglecycles():
    """Generate pairs (angle,list of cycles to draw with that angle)."""
    for a,G in anglegraphs():
        used = [False]*vertices
        cycles = []
        for i in range(vertices):
            if not used[i]:
                cycle = [i]
                while True:
                    used[cycle[-1]] = True
                    for neighbor in G[cycle[-1]]:
                        if not used[neighbor]:
                            break
                    if used[neighbor]:
                        break
                    cycle.append(neighbor)

                cycles.append(cycle)
        yield a,cycles

def angleedges():
    """Generate pairs (angle,edge to draw with that angle)."""
    for a,C in anglecycles():
        for cycle in C:
            if len(cycle) == 2:
                x,y = cycle
                delta = (y-x)%vertices
                if delta+delta > vertices:
                    x,y = y,x
                yield a,x,y
            else:
                for i in range(len(cycle)):
                    yield a,cycle[i-1],cycle[i]

# ============================================================
#   Generate graphical objects
# ============================================================

radius = vertices / (2 * pi)    # arclen 1 around circle
maxRadius = radius

points = [radius * e**(2j*pi*(-0.25+(+0.5+i)/vertices)) for i in range(vertices)]

def straight(a,x,y):
    # Should this be drawn as a straight line segment?
    return a*vertices == -((y-x)%vertices)*2*degree or \
           (a - 2*degree)*vertices == -((y-x)%vertices)*2*degree

def distance(p,q):
    """Euclidean distance from p to q"""
    return ((p.real - q.real)**2 + (p.imag - q.imag)**2)**0.5

def arcs():
    """Return sequence of vertex,vertex,radius triples"""
    global maxRadius
    for a,x,y in angleedges():
        if not straight(a,x,y):
            t = pi*a/(2*degree) + pi*((y-x)%vertices)/vertices
            d = distance(points[x],points[y])
            if t < 0:
                y,x = x,y
                t = -t
            rad = d/(2*sin(t))
            if a > 0:
                far = abs((points[x]+points[y])/2 + rad*(1-cos(t)))
                maxRadius = max(maxRadius,far)
            if t > pi:
                x,y = y,x
            elif t > pi/2:
                rad = -rad
                x,y = y,x
            yield points[y],points[x],rad

def segments():
    """Return sequence of vertex pairs to be connected by line segments"""
    global maxRadius
    for a,x,y in angleedges():
        if straight(a,x,y):
            if a < 0:
                yield points[x],points[y]
            else:
                # connect through infinity on a line
                # draw as two line segments with length = distance
                yield points[x],2*points[x]-points[y]
                yield points[y],2*points[y]-points[x]
                maxRadius = max(maxRadius,abs(2*points[x]-points[y]))

# ============================================================
#   Draw the layout
# ============================================================

# Dummy pass through arcs to find max radius
for a in arcs():
    pass
for a in segments():
    pass
scale = 25 * options.scale
vertexRadius = 5 * options.radius * options.scale
bbox = maxRadius*scale + vertexRadius + 1
bbox = 1+int(bbox)

print '''<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" 
  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg width="%s" height="%s" viewBox="-%s -%s %s %s"
     xmlns="http://www.w3.org/2000/svg" version="1.1">''' % \
  (2*bbox+1,2*bbox+1,0,0,2*bbox+1,2*bbox+1)

def place(p):
    """Convert unit-free complex to pixel-scaled real coordinates"""
    return p.real*scale+bbox+1,p.imag*scale+bbox+1

print '  <g style="fill:none; stroke:black">'

for p,q in segments():
    print '    <line x1="%0.2f" y1="%0.2f" x2="%0.2f" y2="%0.2f" />' % \
        (place(p)+place(q))

for p,q,r in arcs():
    la = 0
    if r < 0:   # flag for large arc
        la = 1
        r = -r
    print '    <path d="M %0.2f,%0.2f A %0.2f,%0.2f 1 %s %s %0.2f,%0.2f" />' % \
        (place(p)+(scale*r,scale*r,la,la)+place(q))

print '  </g>'
print '  <g style="fill:%s; stroke:%s">' % (options.color, (options.outline and "none" or "black"))

for v in points:
    print '    <circle cx="%0.2f" cy="%0.2f" r="%s" />' % \
        (place(v)+(vertexRadius,))

print '  </g>'
print '</svg>'
