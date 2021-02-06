print """#version 3.5;
#include "colors.inc"
global_settings {
  assumed_gamma 1
}
// ----------------------------------------
camera {
  location  <1.7,0,30>
  right     x*image_width/image_height
  look_at   <0,0,0>
  angle     30
}
light_source {
  <1.7,0,31>
  color rgb <0.1,0.1,0.1>
}
"""
for i in range(5):
    for j in range(5):
        print """light_source {
  <%0.2f,%0.2f,%0.2f>
  color rgb <0.04,0.04,0.04>
}
""" % (10.666 + 0.1*i, 0.1*j,38)

from math import pi,cos,sin

h=20
k=5
s=0.8
def endpoints(x,y):
    x = s*x
    y = s*y
    return (x-k*y,h,y+k*x),(x+k*y,-h,y-k*x)

for (r,n,c) in [(0,1,"White"),(1.8,15,"Yellow"),(4,24,"Orange"),(7,32,"Red")]:
    for i in range(n):
        x = r*cos(2*pi*i/n)
        y = r*sin(2*pi*i/n)
        p,q = endpoints(x,y)
        print """cylinder {
  <%0.2f, %0.2f, %0.2f>, <%0.2f, %0.2f, %0.2f>, 0.08
  texture {
    pigment {color %s}
    finish { reflection {0.04} ambient 0 diffuse 1 }
  }
}""" % (p+q+(c,))