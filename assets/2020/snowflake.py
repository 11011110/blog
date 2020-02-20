from math import *
from random import seed,random
from PADS.SVG import *
import sys
import heapq

# ============== INITIALIZATION ==============
 
radius = 3
scale = 600
ratio = 3.65

def interleave(seq,multiplier):
    seq = iter(seq)
    initial = prev = seq.next()
    yield initial
    for x in seq:
        yield prev + (x-prev)*multiplier
        yield x
        prev = x
    yield prev + (initial-prev)*multiplier

koch = [1, -0.5-3**0.5*0.5j, -0.5+3**0.5*0.5j]
koch = list(interleave(koch,0.5+(0.5j/3**0.5)))
for i in range(3):
    koch = list(interleave(koch,0.5-0.25j))
    koch = list(interleave(koch,0.5+0.25j))

points = [(300+290*(x.real),300+290*(x.imag)) for x in koch]
npoints = len(points)

# ============== PATH-FINDING ==============

def dist2(p,q):
    return (p[0]-q[0])**2 + (p[1]-q[1])**2

def dist(i,j):
    return dist2(points[i],points[j])**0.5

graph = {i:[] for i in range(npoints)}

def graphdistance(i,j):
    """ A* """
    H = []
    D = {}
    heapq.heappush(H,(0,0,i))
    while H:
        prio,pathlength,point = heapq.heappop(H)
        if point not in D:
            if point == j:
                return pathlength
            D[point] = pathlength
            for neighbor in graph[point]:
                itslength = pathlength + dist(point,neighbor)
                itsprio = itslength + dist(neighbor,j)
                heapq.heappush(H,(itsprio,itslength,neighbor))
    return 2*ratio*scale

# ============== CONSTRUCTION ==============

distances = [(dist(i,j),i,j)
             for i in range(1,npoints) for j in range(i)]
distances.sort()

for d,p,q in distances:
    if d*ratio < graphdistance(p,q):
        graph[p].append(q)
        graph[q].append(p)

# ============== OUTPUT ==============

def complexify(i):
    x,y = points[i]
    return x + y*1j

svg = SVG(scale*(1+1j),sys.stdout)

svg.group(stroke=colors.black)
for i in range(npoints):
    for j in graph[i]:
        if i < j:
            svg.segment(complexify(i),complexify(j))
svg.ungroup()

svg.group(fill=colors.red,stroke=colors.black)
for i in range(npoints):
    svg.circle(complexify(i),radius)
svg.ungroup()

svg.close()