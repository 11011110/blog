from SVG import SVG,colors
import sys

epoints = [((2**i-i),5*(2**i+1)) for i in range(1,14)]
points = [(0,0)] + epoints + [(80000,0)] + [(x,-y) for x,y in reversed(epoints)]

bbox = 840+840j
svg = SVG(bbox,sys.stdout)

def coord(p):
    x,y = p
    return 20+420j + x/100 + y*1j/100

svg.polygon([coord(p) for p in points]+[coord(points[0])],fill="none",stroke=colors.black)

svg.group(fill=colors.red,stroke=colors.black)
for p in points:
    svg.circle(coord(p),4)
svg.ungroup()

svg.close()