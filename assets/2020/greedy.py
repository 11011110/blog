from math import *
from random import seed,random
from PADS.SVG import *
import sys
import heapq

# ============== INITIALIZATION ==============

ratio = float(sys.argv[-1]) # specify ratio on command line, bomb if not there

seed(12345)
 
npoints = 100
radius = 3
exclusion = 18     # prevent points from being too close
scale = 600

def dist2(p,q):
    return (p[0]-q[0])**2 + (p[1]-q[1])**2

def dist(i,j):
    return dist2(points[i],points[j])**0.5

points = []
while len(points) < npoints:
    p = (random()*scale,random()*scale)
    if min(p) < exclusion or max(p) > scale-exclusion:
        continue
    if points:
        nn = min(dist2(p,q)**0.5 for q in points)
        if nn < exclusion:
            continue
    points.append(p)

# ============== PATH-FINDING ==============

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