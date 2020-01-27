# Projective plane embedded in 3d so that all faces are orthogonal polygons.
# The overall graph is bipartite even though all faces are even.
# D. Eppstein, Jun 2006

from pyx import canvas,path,color
from math import sqrt,tan,asin

points = [
    (0, 0, 0),
    (0, 0, 1),
    (0, 1, 1),
    (0, 1, 2),
    (1, 1, 2),
    (1, 0, 2),
    (1, 0, 1),
    (1, 2, 1),
    (2, 2, 1),
    (2, 2, 2),
    (2, 0, 2),
    (2, 0, 3),
    (3, 0, 3),
    (3, 2, 3),
    (3, 2, 2),
    (3, 3, 2),
    (0, 3, 2),
    (0, 3, 3),
    (0, 2, 3),
    (0, 2, 0),
    (1, 2, 0),
    (1, 3, 0),
    (1, 3, 3),
    (1, 1, 3),
    (2, 1, 3),
    (2, 1, 0),
    (2, 3, 0),
    (2, 3, 1),
    (3, 3, 1),
    (3, 1, 1),
    (3, 1, 0),
    (3, 0, 0)
]

points = []
for i in range(4):
    for j in range(4):
        points.append((i,j,(-i-j)%4))
        points.append((i,j,(1-i-j)%4))

points.sort()
points.reverse()    # farthest first

def connected(p,q):
    return sum([p[i]!=q[i] for i in (0,1,2)]) == 1

pov = (-20,6,6.5)
x,y,z = 2,1,0
radius = 0.05
scale = 20.0
vertexColor = [color.rgb.red]
edgeColor = [color.rgb.black]

def distance(p,q):
    return sqrt(sum([(p[i]-q[i])**2 for i in (x,y,z)]))

def perspective(loc):
    dz = loc[z]-pov[z]
    return (loc[x]-pov[x])*scale/dz, (loc[y]-pov[y])*scale/dz

def vertex(p):
    lx,ly = perspective(p)
    prad = scale*1.1*tan(asin(radius/(distance(p,pov))))
    c.fill(path.circle(lx,ly,prad),vertexColor)

def edge(p,q):
    d = distance(p,q)/radius
    v = [(p[i]-q[i])/d for i in (0,1,2)]
    p = [p[i]-v[i] for i in (0,1,2)]
    q = [q[i]+v[i] for i in (0,1,2)]
    lx1,ly1 = perspective(p)
    lx2,ly2 = perspective(q)
    c.stroke(path.line(lx1,ly1,lx2,ly2),edgeColor)
c = canvas.canvas()

for p in points:
    for q in points:
        if q > p and connected(p,q):
            edge(p,q)
    vertex(p)
c.writePDFfile("dyck")