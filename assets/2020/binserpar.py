from math import pi
from cmath import rect
from PADS.SVG import *
import sys

levels = 6
outer = 1<<levels
nspokes = 1<<(levels+1)

def goodforlevel(i,j):
    i |= 1<<(levels-1)  # cut off for sparsest level
    return (i &~ (i-1)) == (j &~ (j-1))
    i &=~ (i-1)         # mask of relevant bits for test
    j &=~ (j-1)         # compute same mask
    return i == j

vertices = [(i,j) for i in range(nspokes) for j in range(1,outer)
            if goodforlevel(i,j)]

def edgeto(pos,spoke):
    cutoff = spoke | (1<<(levels-1))
    spokebit = cutoff &~ (cutoff-1)
    return (spoke,(pos &~ (spokebit - 1)) | spokebit)

def edgesfor(v):
    spoke,pos = v
    if not spoke&1:
        return []
    return [edgeto(pos,(spoke-1)%nspokes),edgeto(pos,(spoke+1)%nspokes)]

graph = {v:edgesfor(v) for v in vertices}

# ============== OUTPUT ==============
 
radius = 2.5
scale = 800
inner = 0.5

def place(v):
    spoke,pos = v
    theta = 2*pi*spoke/nspokes
    r = inner + (1-inner)*pos/outer
    q = rect(r,theta)
    x,y = 400+395*(q.real),400+395*(q.imag)
    return x + y*1j

svg = SVG(scale*(1+1j),sys.stdout)

svg.group(stroke=colors.black)
for v in graph:
    for w in graph[v]:
        svg.segment(place(v),place(w))
svg.ungroup()

svg.group(fill=colors.red,stroke=colors.black)
for v in graph:
    svg.circle(place(v),radius)
svg.ungroup()

svg.close()