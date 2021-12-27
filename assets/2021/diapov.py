# ==========================================================================
#		Calculate vertex positions, output-independent
# ==========================================================================

spread = range(-10,10)
vertices = [(i,j,k,l) for i in spread for j in spread for k in spread for l in (-i-j-k,1-i-j-k) if l in spread]

def project(v):
    i,j,k,l = v
    return i+j-k-l, i-j+k-l, i-j-k+l

# ==========================================================================
#		Produce 3d pov output
# ==========================================================================

# Basic scene with fog

print """#version 3.5;#include "colors.inc"global_settings {  assumed_gamma 1}// ----------------------------------------camera {  location  <9.2,13.8,15.4>  right     x*image_width/image_height  look_at   <0,0,0>  angle     30}light_source {  <-20, 7, 20>  color rgb <1.3,1.3,1.3>}light_source {  <10,10,15>  color rgb <0.4, 0.4, 0.4>}fog {  fog_type 1  distance 100  color White}"""

for v in vertices:
    if sum(v) == 0:
        delta = 1
    else:
        delta = -1
    w,x,y,z = v
    for u in [(w+delta,x,y,z), (w,x+delta,y,z), (w,x,y+delta,z), (w,x,y,z+delta)]:
        if delta > 0 or u not in vertices:
            print """cylinder {
  <%d, %d, %d>, <%d,%d,%d>, 0.15
  texture {
    pigment {color Blue}
    finish { reflection {0.04} ambient 0 diffuse 1 }
  }
}""" % (project(v)+project(u))

for v in vertices:
    print """sphere {
  <%d,%d,%d>,0.3
  texture {
    pigment {color Red}
    finish { reflection {0.04} ambient 0 diffuse 1 }
  }
}""" % project(v)
