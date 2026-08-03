from SVG import SVG,colors
from math import cos,sin,pi
import sys

scale = 800
margin = 25
radius = 10
angles = [0, pi/4.7, pi/3, 10*pi/19, 4*pi/5]
dim = len(angles)

D = {1<<j:j for j in range(dim)}
Q = {i:[i^(1<<j) for j in range(dim)] for i in range(1<<dim)}
P = {0:0}   # place base point
for v in range(1,1<<dim):
    i = D[v&~(v-1)]
    P[v] = P[v^(1<<i)] + cos(angles[i]) - 1j*sin(angles[i])

minx = min(P[i].real for i in range(1<<dim))
maxx = max(P[i].real for i in range(1<<dim))
miny = min(P[i].imag for i in range(1<<dim))
maxy = max(P[i].imag for i in range(1<<dim))
placefactor = (scale-2*margin)/max(maxx-minx,maxy-miny)
bbox = (2+2j)*margin + (maxx-minx + 1j*(maxy-miny))*placefactor

def place(p):
    p -= (minx + 1j*miny)   # offset to origin
    return p*placefactor + (1+1j)*margin
    
svg = SVG(bbox,sys.stdout)

svg.group(fill="none",stroke=colors.black)
for v in Q:
    for w in Q[v]:
        if v < w:
            svg.segment(place(P[v]),place(P[w]))
svg.ungroup()

svg.group(fill=colors.lightblue,stroke=colors.black)
for v in Q:
    svg.circle(place(P[v]),radius)
svg.ungroup()
svg.close()