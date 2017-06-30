from PADS.SVG import SVG
from cmath import phase
import sys

# ============================================================
#    Simple geometric calculations
# ============================================================

def distance(v,w):
    """Euclidean distance between two 3d points"""
    return ((v[0]-w[0])**2 + (v[1]-w[1])**2 + (v[2]-w[2])**2)**0.5

def length(v):
    """How far from the origin is this 3d point?"""
    return distance(v,(0,0,0))

def normalize(v):
    """Project a 3d point onto the unit sphere"""
    L = length(v)
    return (v[0]/L,v[1]/L,v[2]/L)

def midpoint(v,w):
    """Midpoint of geodesic between two spherical points"""
    return normalize([v[i]+w[i] for i in (0,1,2)])

def project(v):
    """Stereographic projection of 3d point onto complex plane"""
    return v[0]/(1-v[2]) + 1j*v[1]/(1-v[2])

def projective(q):
    """Convert complex numbers to projective coordinates"""
    return (q.real,q.imag,1)

def unprojective(v):
    """Convert projective coordinates to complex numbers"""
    x,y,z = v
    return x/z + y*1j/z

def meet(v,w):
    """Line through two projective points or vice versa"""
    return (v[1]*w[2]-v[2]*w[1],v[2]*w[0]-v[0]*w[2],v[0]*w[1]-v[1]*w[0])

def bisector(p,q):
    """Line bisecting two complex points"""
    midpoint = (p+q)/2              # First point on line
    offset = midpoint + (q-p)*1j    # Second point on line
    return meet(projective(midpoint),projective(offset))

def arcradius(p,q,r):
    """Radius of arc through complex points p,q,r"""
    bpq = bisector(p,q)
    bqr = bisector(q,r)
    center = unprojective(meet(bpq,bqr))
    return abs(center-p)


# ============================================================
#    Snub cube construction
# ============================================================

xi = ((17+3*(33)**0.5)**(1./3) - (-17+3*(33)**0.5)**(1./3) - 1)/3
x,y,z = normalize((-1,xi,1/xi))
vertices = [(x,y,z), (x,-z,y), (x,-y,-z), (x,z,-y)]
vertices = vertices + [(y,z,x) for x,y,z in vertices] + [(z,x,y) for x,y,z in vertices]
vertices = vertices + [(-x,-z,-y) for x,y,z in vertices]

edgelength = min(distance(vertices[0],vertices[i]) for i in range(1,24))
graph = {v : [w for w in vertices if 0.95 < distance(v,w)/edgelength < 1.05]
         for v in vertices}


# ============================================================
#    Draw as an SVG file
# ============================================================

bbox = 72*6     # Draw in a six inch square

# Need to multiply this by fudge factor for outer edge arcs
projectionRadius = 1.35 * max(abs(project(v)) for v in vertices)
scale = (bbox/2 - 10)/projectionRadius
offset = bbox*(1+1j)/2

def place(q):
    """Convert projection coordinates into drawing coordinates"""
    return q*scale + offset

# Start making a drawing
svg = SVG(bbox*(1+1j),sys.stdout)

# Show the edges
svg.group(style={"fill": "none", "stroke": "black"})
for v in graph:
    for w in graph[v]:
        p = project(v)
        r = project(w)
        if phase(p/r) > 0.01:
            q = project(midpoint(v,w))
            svg.arc(place(p),place(r),arcradius(p,q,r)*scale)
        elif phase(p/r) > -0.01 and abs(p) > abs(r):
            svg.segment(place(p),place(r))
svg.ungroup()

# Show the vertices
svg.group(style={"fill": "#BC1E47", "stroke": "black"})
for v in vertices:
    svg.circle(place(project(v)),4)
svg.ungroup()

svg.close()
