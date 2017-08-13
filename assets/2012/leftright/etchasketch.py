import sys
word = sys.argv[-1]
scale=3

def trace(word):
    x,y = 0,0
    dx,dy = 1,0
    yield x,y
    x,y = x+dx,y+dy
    yield x,y
    for c in word:
        if c == "0":
            dx,dy = -dy,dx
        elif c == "1":
            dx,dy = dy,-dx
        else:
            print >>sys.stderr,"Unexpected character " + str(c) + " in input!"
            sys.exit(1)
        x,y = x+dx,y+dy
        yield x,y

xx = [x for x,y in trace(word)]
yy = [y for x,y in trace(word)]
dx = -min(xx)+1
dy = -min(yy)+1
rx = max(xx)-min(xx)+2
ry = max(yy)-min(yy)+2
print '''<?xml version="1.0" encoding="iso-8859-1"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
 "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="%dpt" height="%dpt" viewBox="0 0 %d %d">''' %(rx*scale,ry*scale,rx*scale,ry*scale)
print '  <polyline fill="none" stroke="black" points="'
for x,y in trace(word):
    print "%d,%d" %((x+dx)*scale,(y+dy)*scale),
print '"/>'
print '</svg>'
