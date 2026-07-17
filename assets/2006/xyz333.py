from pyx import canvas,path,color
from math import sqrt,tan,asin

m3 = (0,1,2)

nonagon = [(i,j,k) for i in m3 for j in m3 for k in m3
           if i+j+k != 3 and max(i,j,k)-min(i,j,k) != 2]

torus = [(i,j,k) for i in m3 for j in m3 for k in m3 if (i+j+k)%3 != 0]

projplane = [(i,j,k) for i in m3 for j in m3 for k in m3
             if i+j+k != 2 and i+(2-j)+(2-k)!=2 and
             (2-i)+j+(2-k) != 2 and (2-i)+(2-j)+k != 2 and
             (i,j,k) != (1,1,1)]

points = [(i,j,k-3) for i,j,k in projplane] + nonagon + \
         [(i,j,k+3) for i,j,k in torus]

points.sort()
points.reverse()    # farthest first

def connected(p,q):
    a,b = min(p[2],q[2]),max(p[2],q[2])
    if a < 0 and b >= 0: return False
    if a < 3 and b >= 3: return False
    return sum([p[i]!=q[i] for i in (0,1,2)]) == 1

pov = (-10,4,0.3)
x,y,z = 2,1,0
radius = 0.05
scale = 10.0
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
c.writePDFfile("xyz333")