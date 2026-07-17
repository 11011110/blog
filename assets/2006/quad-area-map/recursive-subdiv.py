import sys

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

def midpoint(s,t):
    """Midpoint of two Cartesian or Projective points."""
    return tuple([(cs+ct)/2 for cs,ct in zip(s,t)])

def meet(s,t):
    """Line where two projective points meet or point where two lines meet."""
    return (s[1]*t[2]-s[2]*t[1], s[2]*t[0]-s[0]*t[2], s[0]*t[1]-s[1]*t[0])

def slope(L):
    """Point at infinity on projective line."""
    return meet(L,(0,0,1))

def areaCenter(a,b,c,d):
    """Area center of quadrilateral defined by four Cartesian points."""
    a,b,c,d = projective(a), projective(b), projective(c), projective(d)
    return cartesian(meet(meet(midpoint(a,c),slope(meet(b,d))),
                          meet(midpoint(b,d),slope(meet(a,c)))))

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
#		Subdivide and draw subdivided quadrilateral
# ==========================================================================

def subdivrecur(a,b,c,d,nlevels):
    if nlevels > 0:
        e = areaCenter(a,b,c,d)
        ab = midpoint(a,b)
        bc = midpoint(b,c)
        cd = midpoint(c,d)
        da = midpoint(d,a)
        for p in ab,bc,cd,da:
            svgLine(p,e)
        subdivrecur(a,ab,e,da,nlevels-1)
        subdivrecur(b,bc,e,ab,nlevels-1)
        subdivrecur(c,cd,e,bc,nlevels-1)
        subdivrecur(d,da,e,cd,nlevels-1)

def subdivide(a,b,c,d,nlevels):
    minx = min([px for px,py in a,b,c,d])
    miny = min([py for px,py in a,b,c,d])
    a,b,c,d = [(px-minx,py-miny) for px,py in a,b,c,d]
    maxx = max([px for px,py in a,b,c,d])
    maxy = max([py for px,py in a,b,c,d])
    svgHeader(maxx,maxy)
    svgStyle('fill="none" stroke="black"')
    for p,q in [(a,b),(b,c),(c,d),(d,a)]:
        svgLine(p,q)
    svgEndStyle()
    svgStyle('fill="none" stroke="blue"')
    subdivrecur(a,b,c,d,nlevels)
    svgEndStyle()
    svgTrailer()

# ==========================================================================
#		Main program, not even a command-line UI yet
# ==========================================================================

a = (100.0,0.0)
b = (0.0,700.0)
c = (800.0,250.0)
d = (750.0,73.0)

subdivide(a,b,c,d,5)
