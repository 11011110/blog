import sys
from math import sqrt

# ==========================================================================
#		Geometric calculations
# ==========================================================================

def projective(xy):
    """Projective coordinates for cartesian point (x,y)."""
    x,y = xy
    return x,y,1

def cartesian(xyz):
    """Cartesian coordinates for projective point (x,y,z)."""
    x,y,z = xyz
    return x/z, y/z

def meet(s,t):
    """Line where two projective points meet or point where two lines meet."""
    return (s[1]*t[2]-s[2]*t[1], s[2]*t[0]-s[0]*t[2], s[0]*t[1]-s[1]*t[0])

def offset(L,delta):
    """Line offset from L by delta units."""
    a,b,c = L
    return a,b,c+delta*sqrt(a**2+b**2)

def distance(a,b):
    ax,ay = a
    bx,by = b
    return sqrt((ax-bx)**2 + (ay-by)**2)

def sides(a,b,c,d):
    return (a,b),(b,c),(c,d),(d,a)

def vertices(ab,bc,cd,da):
    return [cartesian(meet(K,L)) for K,L in (da,ab),(ab,bc),(bc,cd),(cd,da)]

def sidelengths(a,b,c,d):
    return [distance(p,q) for p,q in sides(a,b,c,d)]

# ==========================================================================
#		SVG output utility routines
# ==========================================================================

nestingLevel = None

def svgTag(s, deltaIndentation = 0):
	"""Send a single XML tag to the SVG file.
	First argument is the tag with all its attributes appended.
	Second arg is +1, -1, or 0 if tag is open, close, or both respectively.
	"""

	global nestingLevel
	if deltaIndentation < 0:
		nestingLevel -= 1
	if nestingLevel:
		sys.stdout.write('\t' * nestingLevel)
	sys.stdout.write('<')
	if deltaIndentation < 0:
		sys.stdout.write('/')
	sys.stdout.write(s)
	if not deltaIndentation:
		sys.stdout.write(' /')
	sys.stdout.write('>\n')
	if deltaIndentation > 0:
		nestingLevel += 1
	

def svgHeader(maxX, maxY):
	"""Start producing an SVG object.
	The output bounding box runs from (0,0) to (maxX,maxY).
	Must be followed by svg content and a call to svgTrailer().
	"""
	global nestingLevel
	if nestingLevel is None:
		sys.stdout.write('''<?xml version="1.0" encoding="iso-8859-1"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
 "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
''')
		nestingLevel = 0
	svgTag('svg xmlns="http://www.w3.org/2000/svg" version="1.1" '
		   'width="%dpt" height="%dpt" viewBox="0 0 %d %d"'
			% (maxX, maxY, maxX, maxY), 1)

def svgTrailer():
	"""End of SVG object."""
	svgTag('svg', -1)

def svgStyle(style):
	"""Start a group of svg items with the given style.
	Argument is a string in the form of a list of svg item attributes.
	Must be followed by svg content and a call to svgEndStyle().
	"""
	svgTag('g ' + style, 1)
	
def svgEdgeStyle(index):
	"""Look up edge style and call svgStyle with it."""
	svgStyle(globals()['edgeStyle' + str(index)])

def svgEndStyle():
	"""Finish group of styled svg items."""
	svgTag('g', -1)

def svgLine(start, end):
	"""Output line segment from start to end coordinates.
	Must be called within an svgStyle()/svgEndStyle() call pair.
	"""
	svgTag('line x1="%d" y1="%d" x2="%d" y2="%d"' % (start+end) )


# ==========================================================================
#		Main program, not even a command-line UI yet
# ==========================================================================

def drawquad(a,b,c,d):
    for p,q in [(a,b),(b,c),(c,d),(d,a)]:
        svgLine(p,q)

def interpolate(p,q,frac):
    px,py = p
    qx,qy = q
    return px*(1-frac)+qx*frac, py*(1-frac)+qy*frac

def drawmesh(outer,inner,nsides):
    for outside,inside in zip(sides(*outer),sides(*inner)):
        for i in range(nsides-1):
            out = interpolate(outside[0],outside[1],(i+1)*1.0/nsides)
            inn = interpolate(inside[0],inside[1],i*1.0/(nsides-2))
            svgLine(out,inn)

a = (100.0,0.0)
b = (0.0,700.0)
c = (800.0,250.0)
d = (750.0,73.0)

minx = min([px for px,py in a,b,c,d])
miny = min([py for px,py in a,b,c,d])
a,b,c,d = [(px-minx,py-miny) for px,py in a,b,c,d]
maxx = max([px for px,py in a,b,c,d])
maxy = max([py for px,py in a,b,c,d])
svgHeader(maxx,maxy)
svgStyle('fill="none" stroke="black"')
drawquad(a,b,c,d)
svgEndStyle()
svgStyle('fill="none" stroke="blue"')

nsides = 31 # should be odd number so center works correctly
perim = sum(sidelengths(a,b,c,d))
scale = perim/(nsides*1000.0)

a,b,c,d = [projective(p) for p in a,b,c,d]
ab,bc,cd,da = [meet(p,q) for p,q in sides(a,b,c,d)]
nest = []

while True:
    a,b,c,d = vertices(ab,bc,cd,da)
    sl = sidelengths(a,b,c,d)
    if sum(sl) > perim:
        break
    perim = sum(sl)
    nest.append((a,b,c,d))
    ab,bc,cd,da = [offset(L,scale*perim/side)
                   for L,side in zip((ab,bc,cd,da),sl)]

for i in range(nsides//2):
    outer = nest[2*i*len(nest)//nsides]
    inner = nest[2*(i+1)*len(nest)//nsides]
    drawmesh(outer,inner,nsides-2*i)
    drawquad(*inner)

svgEndStyle()
svgTrailer()
