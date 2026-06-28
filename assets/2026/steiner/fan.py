from SVG import SVG,colors
import sys

epoints = [((2**i-i),5*(2**i+1)) for i in range(1,14)]
points = [(0,0)] + epoints + [(80000,0)] + [(x,-y) for x,y in reversed(epoints)]

bbox = 600+600j
svg = SVG(bbox,sys.stdout)

def coord(p):
    x,y = p
    return 20+300j + x*5 + y*1j*5

steiner = (3.23041167, 0)

svg.group(fill="none",stroke=colors.black)
svg.polygon([coord(p) for p in points]+[coord(points[0])])
for p in points:
    svg.segment(coord(p),coord(steiner))
svg.ungroup()

svg.group(fill=colors.red,stroke=colors.black)
for p in points:
    svg.circle(coord(p),4)
svg.ungroup()

svg.circle(coord(steiner),4,fill=colors.blue,stroke=colors.black)

svg.close()