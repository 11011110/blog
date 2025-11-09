from PADS.SVG import *
import sys

tet = [(i,j,k) for i in [-1,1] for j in [-1,1] for k in [-1,1] if i*j*k>0]
def place(state):
    placement = [0,0,0]
    for j in range(ndisks):
        for i in range(3):
            placement[i] += weights[j]*tet[state[j]][i]
    return placement

def disks(n):
    if n == 0:
        yield []
        return
    for d in disks(n-1):
        for i in range(4):
            yield d+[i]

restricted = True

def moves(state):
    disk = ndisks - 1
    free = {0,1,2,3}
    while disk >= 0:
        if state[disk] in free:
            free.remove(state[disk])
            for f in free:
                move = list(state)
                move[disk] = f
                if (not restricted or state[disk] == state[0] or f == state[disk]):
                    yield move
        disk -= 1

ndisks = 3
viewpoint = 9.394857
viewwidth = 1.9
radius = 8

scale = 400

weights = [1]
for i in range(ndisks-2):
    weights.append(weights[-1]/3)
weights.append(weights[-1]/2)

vertices = [place(d) for d in disks(ndisks)]
edges = [(place(d),place(e)) for d in disks(ndisks) for e in moves(d)]

svg = SVG(scale*(2+2j),sys.stdout)

def perspectivefactor(z):
    return viewpoint/(viewpoint-z)

def view(p):
    x,y,z = p
    return (x + 1j*y)*(scale/viewwidth)*perspectivefactor(z) + scale*(1+1j)

def drawvert(v):
    svg.circle(view(v),radius*perspectivefactor(v[2]))

def drawedge(e):
    svg.segment(view(e[0]),view(e[1]))

drawers = [(v[2],1,v,drawvert) for v in vertices] +\
          [(max(e[0][2],e[1][2]),0,e,drawedge) for e in edges]

oldb = -1
for z,b,o,d in sorted(drawers):
    if b != oldb:
        if oldb != -1:
            svg.ungroup()
        if b:
            svg.group(fill=colors.red)
        else:
            svg.group(stroke=colors.black)
        oldb = b
    d(o)

svg.ungroup()
svg.close()