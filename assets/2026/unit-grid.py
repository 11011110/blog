from SVG import SVG,colors
from math import cos,sin,pi
import sys

scale = 800
margin = 25
radius = 10
deltas = [(3,4),(4,3),(-3,4),(-4,3)]
dim = 8

G = {(i,j):[(i+x,j+y) for x,y in deltas if 0 <= i+x < dim and 0 <= j+y < dim]
     for i in range(dim) for j in range(dim)}

placefactor = (scale-2*margin)/(dim-1)
bbox = (1+1j)*scale

def place(p):
    return (p[0]+1j*p[1])*placefactor + (1+1j)*margin
    
svg = SVG(bbox,sys.stdout)

svg.group(fill="none",stroke=colors.black)
for v in G:
    for w in G[v]:
        svg.segment(place(v),place(w))
svg.ungroup()

svg.group(fill=colors.lightblue,stroke=colors.black)
for v in G:
    svg.circle(place(v),radius)
svg.ungroup()
svg.close()