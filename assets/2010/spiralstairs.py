# ==========================================================================
#		Calculate vertex positions, output-independent
# ==========================================================================

spread = range(-10,10)
vertices = [(i,j,k,l) for i in spread for j in spread for k in spread for l in (-i-j-k,1-i-j-k) if l in spread]

fundamental_unit = [
    (0,0,0), (2,1,0), (1,2,0), (3,3,0),
    (0,1,1), (2,0,1), (1,3,1), (3,2,1),
    (1,1,2), (3,0,2), (0,3,2), (2,2,2),
    (1,0,3), (3,1,3), (0,2,3), (2,3,3),
]

copies = range(-5,6)

vertices = set()
for i in copies:
    for j in copies:
        for k in copies:
            for (p,q,r) in fundamental_unit:
                vertices.add( (4*i+p,4*j+q,4*k+r) )

def distsquared(p,q):
    return sum((p[i]-q[i])**2 for i in range(len(p)))

# ==========================================================================
#		Produce 3d pov output
# ==========================================================================

# Basic scene with fog

print """#version 3.5;
#include "colors.inc"
global_settings {
  assumed_gamma 1
}
// ----------------------------------------
camera {
  location  <0.45,0.55,15.4>
  right     x*image_width/image_height
  look_at   <0,0,0>
  angle     30
}
light_source {
  <2.5, 5.5, 18.5>
  color rgb <0.8,0.8,0.8>
}
light_source {
  <10.5,10.5,15.5>
  color rgb <0.4, 0.4, 0.4>
}
light_source {
  <5.5,3.5,20.5>
  color rgb <0.4, 0.4, 0.4>
}
fog {
  fog_type 1
  distance 100
  color White
}"""

for v in vertices:
    for i in (-1,0,1):
        for j in (-1,0,1):
            for k in (-1,0,1):
                if i**2 + j**2 + k**2 == 2:
                    w = (v[0]+i,v[1]+j,v[2]+k)
                    if w in vertices:
                        print """cylinder {
  <%d, %d, %d>, <%d,%d,%d>, 0.1
  texture {
    pigment {color Blue}
    finish { reflection {0.04} ambient 0 diffuse 1 }
  }
}""" % (v+w)

for v in vertices:
    print """sphere {
  <%d,%d,%d>,0.2
  texture {
    pigment {color Red}
    finish { reflection {0.04} ambient 0 diffuse 1 }
  }
}""" % v
