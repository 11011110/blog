# Draw Ageev's 220-chord 5-chromatic triangle-free chord diagram

from cmath import pi,sin,cos,tan
import sys
outputFile = sys.stdout

scale = 400.0
margin = 10.0
nestingLevel = 0

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
firstpos = {}
lastpos = {}
for i in range(len(chords)):
    if chords[i] in firstpos:
        lastpos[chords[i]] = i
    else:
        firstpos[chords[i]] = i

# ==========================================================================
#		SVG output utility routines
# ==========================================================================

def svgTag(s, deltaIndentation = 0):
	"""Send a single XML tag to the SVG file.
	First argument is the tag with all its attributes appended.
	Second arg is +1, -1, or 0 if tag is open, close, or both respectively.
	"""

	global nestingLevel
	if deltaIndentation < 0:
		nestingLevel -= 1
	if nestingLevel:
		outputFile.write('\t' * nestingLevel)
	outputFile.write('<')
	if deltaIndentation < 0:
		outputFile.write('/')
	outputFile.write(s)
	if not deltaIndentation:
		outputFile.write(' /')
	outputFile.write('>\n')
	if deltaIndentation > 0:
		nestingLevel += 1
	

def svgHeader(maxX, maxY):
	"""Start producing an SVG object.
	The output bounding box runs from (0,0) to (maxX,maxY).
	Must be followed by svg content and a call to svgTrailer().
	"""
	global nestingLevel
	if nestingLevel is None:
		outputFile.write('''<?xml version="1.0" encoding="iso-8859-1"?>
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

def svgEndStyle():
	"""Finish group of styled svg items."""
	svgTag('g', -1)

# Actual output code
total_size = 2*(scale+margin)
svgHeader(total_size,total_size)

svgStyle('fill="none" stroke="black" stroke-dasharray="2,4"')
svgTag('circle cx="%d" cy="%d" r="%s"' % (scale+margin,scale+margin,scale))
svgEndStyle()

svgStyle('fill="none" stroke="blue"')

def circulate(pos):
    theta = 2*pi*pos/len(chords)
    x = int(abs(scale+margin+scale*cos(theta)))
    y = int(abs(scale+margin+scale*sin(theta)))
    return x,y

for chord in firstpos.keys():
    px,py = circulate(firstpos[chord])
    qx,qy = circulate(lastpos[chord])
    b = 0
    if firstpos[chord] <= 0.25 * len(chords) and lastpos[chord] >= 0.75* len(chords): b = 1
    r = int(abs(scale*tan(pi*(firstpos[chord]-lastpos[chord])/len(chords))))
    svgTag('path d="M%d,%d A%d,%d 0 0,%d %d,%d"' % (px,py,r,r,b,qx,qy))

svgEndStyle()
svgTrailer()
