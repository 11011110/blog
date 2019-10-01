# Test the dilation center of a triangle against known triangle centers.
# The dilation center of triangle ABC is the point o minimizing
#    max_{p,q in {A,B,C}} (d(p,o)+d(q,o))/d(p,q),
# as studied in arXiv:cs.CG/0412025
#
# D. Eppstein, UC Irvine, July 9, 2008

# The given edge lengths of a scalene triangle
# per http://faculty.evansville.edu/ck6/encyclopedia/search.html
a = 6.0
b = 9.0
c = 13.0

# Find distances d, e, f from the vertices to the dilation center
# Using a numerical binary search
lo = 0.0
hi = 1.1
for i in range(64):
    mid = (lo+hi)/2
    
    # Interpreting mid as a scale factor, find edge lengths d,e,f with
    # that scale so that (d+e):a :: (d+f):b :: (e+f):c
    d = (a+b-c)*mid
    e = (a+c-b)*mid
    f = (b+c-a)*mid

    # Piero della Francesca's formula for 144 V^2
    # from http://www.mathpages.com/home/kmath424.htm
    # (we want d,e,f to lie flat in the plane,
    # corresponding to a zero-volume tetrahedron).
    A,B,C,D,E,F = a*a,b*b,c*c,d*d,e*e,f*f
    gross_squared_vol = A*F*(-A+B+C+D+E-F) + B*E*(A-B+C+D-E+F) + \
      C*D*(A+B-C-D+E+F) - ((A+F)*(B+E)*(C+D)+(A-F)*(B-E)*(C-D))/2.0

    # Binary search step
    if gross_squared_vol < 0:
        lo = mid
    else:
        hi = mid

# Area of a triangle with given side lengths
def heron(a,b,c):
    s = (a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**0.5

# Compute trilinear coordinates from areal coordinates
x = heron(d,e,a)/a
y = heron(d,f,b)/b
z = heron(e,f,c)/c

# Normalize per http://faculty.evansville.edu/ck6/encyclopedia/search.html
k = 2*heron(a,b,c)/(a*x+b*y+c*z)

print k*x
