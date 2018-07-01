"""LombardiSpirograph - draw rotationally symmetric drawings in Lombardi style
David Eppstein, UC Irvine, March 2010

For usage information type "python LombardiSpirography.py"
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
    "andrasfai4": "11-ad",
    "andrasfai5": "14-gad",
    "andrasfai6": "17-dag",
    "andrasfai7": "20-jdag",
    "antihole7": "7-cb",
    "antihole8": "8-dab",
    "antihole9": "9-cab",
    "antiprism4": "4-a1-a",
    "antiprism5": "5-a1-a",
    "antiprism6": "6-a1-a",
    "brinkmann": "7-c2-1-b",
    "c5xc6": "15-c5-c",
    "cogwheel3": "3-x-1-0",
    "cogwheel4": "4-x-1-0",
    "cogwheel5": "5-x-1-0",
    "cogwheel6": "6-x-1-0",
    "complete5": "5-ab",
    "complete6-a": "6-cab",
    "complete6-b": "5-x-ab",
    "complete6-c": "3-a02-a",  # minimum-crossing drawing
    "complete7": "7-bac",
    "complete8-a": "8-dcab",
    "complete8-b": "7-x-bac",
    "crown5": "10-ac",
    "crown6": "6-a04-a",
    "crown7": "14-cae",
    "cube": "4-a-a",
    "cuboctahedron": "4-a1-1-a",
    "dodecahedron-a": "5-a-1-0-a",
    "dodecahedron-b": "10-a-b",
    "desargues": "10-a-c",
    "durer": "6-a-b",
    "dyck": "8-a-2-0-c",
    "f40": "10-a-4-0-a",
    "grotzsch": "5-x-1-b",
    "hypercube": "8-c2-a",
    "icosahedron": "3-a01-01-1-a",
    "icosidodecahedron": "10-a1-2-b",
    "k33": "6-ca",
    "k44": "8-ca",
    "k55": "10-eac",
    "k66": "12-eac",
    "mobiuskantor": "8-a-c",
    "nauru": "12-a-e",
    "octahedron": "3-a1-a",
    "paley13": "13-dac",
    "pappus": "6-c2-0-a",
    "prism3": "3-a-a",
    "prism5": "5-a-a",
    "prism6": "6-a-a",
    "petersen": "5-a-b",
#   "shrikhande": "8-ba1-bc",   # requires arcs to pass through vertices
    "sun3": "3-a1-0",
    "sun4": "4-ba1-0",
    "sun5": "5-ba1-0",
    "sun6": "6-cba1-0",
    "tetrahedron-a": "3-x-a",
    "tetrahedron-b": "4-ba",
    "utility": "6-ca",
    "wagner": "8-da",
    "wheel4": "4-x-a",
    "wheel5": "5-x-a",
    "wheel6": "6-x-a",
}

# ============================================================
#   Command-line options
# ============================================================

parser = OptionParser()

parser.add_option("-f","--format", dest="show_format", action="store_true",
                  help = "describe the graph input format and exit")

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

options,args = parser.parse_args()

def abort(message):
    print >>sys.stderr,message
    sys.exit(-1)

graphName = "-".join(args).lower()

if options.show_format:
    if graphName:
        abort("--format option does not take any arguments")
    print '''The graph should be described as a sequence of alphanumeric words,
separated either by spaces or by blank lines. The first word gives the
order of symmetry of the drawing (the number of vertices in each
concentric layer) and each subsequent word describes the vertices in
a single layer of the graph.

Each word after the first takes the form of a (possibly empty) sequence
of letters followed by a (possibly empty) number. The letters describe
edges connecting two vertices in the same layer: "a" for a connection
between consecutive vertices in the same layer, "b" for a connection
between vertices two steps away from each other, etc. The letters should
be listed in the order the connections should appear at the vertex,
starting from the edge closest to the center of the drawing and
progressing outwards. Only connections that span less than half the circle
are possible, except that the first layer may have connections spanning
exactly half the circle.

The numeric part of a word describes the connection from one layer to the
next layer. If this number is zero, then vertices in the inner layer are
connected to vertices in the next layer radially by straight line segments.
Otherwise, pairs of vertices from the inner layer, the given number of
steps apart, are connected to single vertices in the outer layer. A nonzero number written with a leading zero (e.g. "01" in place of "1") indicates that, as well as connections with the given number of steps, there should also be a radial connection from the inner layer to the next layer that has vertices
aligned with it; this may not necessarily be the layer immediately outward.

In the innermost layer, the special word "x" may be used to indicate that
the layer consists of a single vertex at the center of the drawing. "x0" indicates that this central vertex is connected both to every vertex in
the adjacent layer and also to every vertex in the next layer that is
staggered with respect to the inner two layers.
'''
    sys.exit(0)

if options.show_names:
    if graphName:
        if graphName not in namedGraphs:
            print '''Graph name''',graphName,'''is not recognized.
Run
    python LombardiSpirograph --names
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
        print "    " + name + " "*(20-len(name)) + description
    sys.exit(0)

if not graphName:
    print '''This program draws rotationally-symmetric graphs in Lombardi style:
the edges are circular arcs that meet at equal angles at each vertex.
To use it, type
    python LombardiSpirograph.py [graph] >output.svg
to a command line, where [graph] is replaced by a name or description
of the graph to be drawn.

For a list of available graph names, type
    python LombardiSpirograph.py --names

For help with the input format for graph descriptions, type
    python LombardiSpirograph.py --format

For a list of other command line options, type
    python LombardiSpirograph.py --help
'''
    sys.exit(0)

# ============================================================
#   Command line parsing
# ============================================================

if graphName in namedGraphs:
    graphName = namedGraphs[graphName]

try:
    # Split command line argument into symmetry and level descriptors
    nameComponents = graphName.split("-")
    symmetry = int(nameComponents[0])
    vertexDescriptors = nameComponents[1:]
    levels = len(vertexDescriptors)
    
    # Parse out the X for the descriptor at the inner level
    central = [False]*levels
    radialzero = False
    if vertexDescriptors[0] == "x":
        vertexDescriptors[0] = ""
        central[0] = True
    elif vertexDescriptors[0] == "x0":
        vertexDescriptors[0] = ""
        central[0] = True
        radialzero = True
    
    # Parse out the letters for the circulant at each level
    circulant = [None]*levels
    for i in range(levels):
        circulant[i] = [ord(x) - ord('a') + 1 for x in vertexDescriptors[i]
                        if x >= "a" and x < "x"]
        vertexDescriptors[i] = vertexDescriptors[i][len(circulant[i]):]

    # Parse out the numbers for which other vertex at this level
    # connects to the same vertex at the next level
    connector = [0]*levels
    radial = [False]*levels
    for i in range(levels):
        if vertexDescriptors[i]:
            connector[i] = int(vertexDescriptors[i])
            if connector[i] and vertexDescriptors[i][0] == "0":
                radial[i] = True
    if radialzero:
        radial[0] = True
except:
    abort('''Unable to parse command line arguments.
For usage type "python LombardiSpirography.py help"''')

# ============================================================
#   Sanity checks
# ============================================================

if connector[-1]:
    abort("Outer level should not specify connector to next level")

threshold = symmetry
for c in circulant:
    for offset in c:
        if offset * 2 > threshold:
            abort("Circulant specification goes too far")
        threshold = symmetry - 1

for offset in connector:
     if offset >= symmetry:
#    if offset * 2 > symmetry:
        abort("Connector specification goes too far")

# ============================================================
#   Preliminary calculations
# ============================================================

stagger = [False]*levels
s = False
for i in range(levels):
    stagger[i] = s
    if connector[i] % 2:
        s = not s
if central[0] and radial[0]:
    stagger[0] = True

inRadial = [False]*levels
for i in range(levels):
    if radial[i]:
        conn = [j for j in range(i+1,levels) if stagger[i] == stagger[j]]
        if not conn:
            abort("No layer outward of %s with same stagger" % i)
        radial[i] = conn[0]
        inRadial[conn[0]] = True

indegree = [1]*(levels+1)
for i in range(levels):
    if connector[i]:
        indegree[i+1] += 1
    if inRadial[i]:
        indegree[i] += 1
indegree[0] = indegree[levels] = 0

# Fudge factor for some angle computations
incount = [indegree[i]+1 for i in range(levels)]
if circulant[0] and circulant[0][0]*2 == symmetry:
    incount[0] = 0

degree = [0]*levels
for i in range(levels):
    if central[i]:
        degree[i] = symmetry
    else:
        degree[i] = indegree[i] + indegree[i+1]
        degree[i] += 2*len(circulant[i])
        if i == 0 and symmetry % 2 == 0 and symmetry // 2 in circulant[i]:
            degree[i] -= 1

for i in range(levels):
    mid = -1
    if degree[i] % 2 == 0:      # Even degree:
        if i == 0:
            if levels == 1:     # Only a single level
                if len(circulant[i]) % 2 == 1:
                    mid = len(circulant[i])//2
            else:
                if len(circulant[i]) % 2 == 0:
                    mid = len(circulant[i])//2
        elif i < levels - 1:
            if len(circulant[i]) % 2 == 1:
                mid = len(circulant[i])//2
        elif len(circulant[i]) % 2 == 0:
            mid = len(circulant[i])//2 - 1
    if mid >= 0 and mid < len(circulant[i]) and circulant[i][mid] != 1:
        abort("Central circulant edge can only be adjacent")

# Test which edges within a single level follow line segments instead of arcs
straightCirculant = [[False]*len(circulant[i]) for i in range(levels)]
for i in range(levels):
    for j in range(len(circulant[i])):
        if 2*(degree[i]*circulant[i][j]+symmetry*(2*j+incount[i])) \
                == degree[i]*symmetry:
            straightCirculant[i][j] = True

# ============================================================
#   Calculate vertex placements and connector radii
# ============================================================

def cot(x):
    """Cotangent(x). Why is this not in math?"""
    return tan(pi/2-x)

def distance(p,q):
    """Euclidean distance from p to q"""
    return ((p.real - q.real)**2 + (p.imag - q.imag)**2)**0.5

radius = [0]*levels     # how far from origin to make each layer
conrad = [0]*levels     # distance point to ctr of curvature of connector
straightConnector = [False]*levels
for i in range(levels):
    if central[i]:
        radius[i] = 0
    elif i == 0:
        radius[i] = symmetry / (2 * pi)     # arclen 1 around initial circle
    elif connector[i-1] == 0:
        factor = (1 + 2 * pi / symmetry)
        if i > 1 and not circulant[i-1]:
            if connector[i-2] % 2 != 0:
                factor = (1 + factor)/2     # hack dodecahedron less exponential
            elif radius[i-2]:
                factor = min(factor,2-radius[i-2]/radius[i-1])
                    # hack pappus and dyck to be less exponential
        radius[i] = max(1,radius[i-1] * factor)
        # same radial length as previous arclen
    else:
        # calculate some angles
        #  p = inner point at level i-1
        #  q = unknown location of point at level i
        #  o = origin
        #  O = point on line op on the other side of p
        #  c = center of curvature of connecting arc
        correction = 1
        if radial[i-1]:
            correction = 2
        poq = pi*connector[i-1]/symmetry
        pcq = (inRadial[i]+1)*pi/degree[i] - correction*pi/degree[i-1] + poq
        Opq = correction*pi/degree[i-1] + pcq/2
        try:
            radius[i] = radius[i-1] / ((cot(poq)-cot(Opq))*sin(poq))
        except:
            abort("Unable to make connecting arcs from level %s to level %s" \
                 % (i-1,i))
        if abs(pcq) < 0.01:
            straightConnector[i-1] = True
        else:
            scr = distance(radius[i-1],radius[i]*e**(1j*poq))/2
            conrad[i-1] = scr/sin(pcq/2)
    if i > 0 and radius[i] < radius[i-1]:
        abort("Inverted levels")

# ============================================================
#   Generate graphical objects
# ============================================================

def rotations(level):
    if central[level]:
        return [1j]
    return [1j*e**(pi*1j*i/symmetry)
            for i in range(int(stagger[level]),2*symmetry,2)]

def vertices():
    """Return sequence of complex numbers representing vertex positions"""
    for i in range(levels):
        for r in rotations(i):
            yield radius[i]*r

def segments():
    """Return sequence of vertex pairs to be connected by line segments"""
    if circulant[0] and circulant[0][0]*2 == symmetry:
        # cross-edges in center
        for i in range(circulant[0][0]):
            r = radius[0]*e**(pi*2j*i/symmetry)
            yield 1j*r,-1j*r
    for i in range(levels):
        if indegree[i] == 1:
            for r in rotations(i):
                yield radius[i-1]*r,radius[i]*r
        for j in range(len(circulant[i])):
            if straightCirculant[i][j]:
                p = radius[i]
                q = p * e**(pi*2j*circulant[i][j]/symmetry)
                for r in rotations(i):
                    yield p*r,q*r
        if straightConnector[i]:
            p = radius[i]
            q = radius[i+1]
            poq = e**(1j*pi*connector[i]/symmetry)
            for r in rotations(i):
                yield p*r,q*poq*r
                yield p*r,q*r/poq
        if radial[i]:
            for r in rotations(radial[i]):
                yield radius[i]*r,radius[radial[i]]*r

maxRadius = radius[-1]

def circulants():
    """Return sequence of all arcs within a single level
    and compute maxRadius as we do"""
    global maxRadius
    for i in range(levels):
        if central[i]:
            continue
        rot = rotations(i)
        p = radius[i] * rot[0]
        for j in range(len(circulant[i])):
            if straightCirculant[i][j]:
                continue
            step = circulant[i][j]
            if step*2 == symmetry:
                continue
            q = radius[i] * rot[step]
            d = distance(q,p)
            theta = pi*step/symmetry # angle p-origin-circle center
            psi = pi*(2*j+incount[i])/degree[i]   # angle o-p-cc
            bulgy = theta + psi > pi/2
            if bulgy:
                psi -= pi/2
            else:
                psi += pi/2
            rad = abs(d/(2 * sin(pi - theta - psi)))
            phi = pi/2 - theta - psi         # angle q-p-cc
            if bulgy:
                rtoc = radius[i]*cos(theta) - rad*sin(phi)
                maxRadius = max(maxRadius,rtoc+rad)
            for k in range(symmetry):
                r = e**(pi*2j*k/symmetry)
                if not bulgy:
                    yield (p*r,q*r,rad)
                elif theta + psi < pi/2:
                    yield (q*r,p*r,rad)
                else:
                    yield (p*r,q*r,-rad)

def connectors():
    """Return sequence of all arcs from one level to the next"""
    for i in range(levels):
        if connector[i] and not straightConnector[i]:
            p = radius[i]
            q = radius[i+1]
            poq = e**(1j*pi*connector[i]/symmetry)
            for r in rotations(i):
                if conrad[i] > 0:
                    yield q*poq*r,p*r,conrad[i]
                    yield p*r,q*r/poq,conrad[i]
                else:
                    yield p*r,q*poq*r,-conrad[i]
                    yield q*r/poq,p*r,-conrad[i]

def arcs():
    """Return sequence of vertex,vertex,radius triples"""
    for arc in circulants():
        yield arc
    for arc in connectors():
        yield arc


# ============================================================
#   Draw the layout
# ============================================================

# Dummy pass through arcs to find max radius
for a in arcs():
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

for v in vertices():
    print '    <circle cx="%0.2f" cy="%0.2f" r="%s" />' % \
        (place(v)+(vertexRadius,))

print '  </g>'
print '</svg>'
