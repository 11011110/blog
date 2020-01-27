from math import pi,acos
print """#version 3.5;#include "colors.inc"#include "textures.inc"global_settings {  assumed_gamma 1.0  max_trace_level 5}// ----------------------------------------camera {  location  <7.5, 8.5, -6.5>  direction 1.5*z  right     x*image_width/image_height  look_at   <1, 0.0,  -0.5>}"""

lights = [(-28,30,-30),(-30,28,-30),(-30,30,-28),(30,0,0),(24,24,-21),(-30,0,0)]
for i in range(3):
    for j in range(4):
        L = [30,30,30]
        L[i] -= 5
        if j < 3:
            L[j] += 2
        lights.append(tuple(L))

for L in lights:
    for i in range(3):
        L = list(L)
        L[i] -= 1
        L = tuple(L)
        print """light_source {  <0, 0, 0>  color rgb <0.04, 0.04, 0.04>  translate <%d, %d, %d>}""" % L

print """sky_sphere {  pigment {    gradient y    color_map { [0.0 color rgb <0.1,0.1,0.1>] [1.0 color rgb <0.3,0.3,0.3>] }  }}"""

facecolors = [
    "texture { pigment { color rgb <1,1,0.7> } }",
    "texture { pigment { color rgb <0.7,1,1> } }",
    "texture { pigment { color rgb <1,0.7,1> } }",
]
edgecolor = "texture { pigment { color rgb <0,0,0> } }"

L=0.5   # scale of cubes
R=0.15  # radius of vertex spheres
CR=0.025 # radius of edge cylinders

for x,y,z,s in [(0,0,0,0),(3,3,0,1),(3,-3,0,1),(-3,3,0,1),(-3,-3,0,1)]:
    for i,j,k in [(0,1,2),(1,2,0),(2,0,1)]:
        for d in (-L,L):
            print "polygon {"
            points = ["5"]
            for (u,v) in [(L,L),(L,-L),(-L,-L),(-L,L),(L,L)]:
                point = [x,y,z]
                point[i] += d
                point[j] += u
                point[k] += v
                point = (point[0],point[2],point[1]) # (screwy x,z,y order)
                points.append("<%s,%s,%s>" % point)
            print "  " + ", ".join(points)
            c = i
            if i != 2 and s:
                c = 1 - c
            print "  " + facecolors[c]
            print "}"
        for (u,v) in [(L,L),(L,-L),(-L,-L),(-L,L)]:
            point = [x,y,z]
            point[i] += d-R
            point[j] += u
            point[k] += v
            print "cylinder {"
            print "  <%s,%s,%s>," % (point[0],point[2],point[1])
            point[i] -= 2*(d-R)
            print "  <%s,%s,%s>," % (point[0],point[2],point[1])
            print "  " + str(CR)
            print "  " + edgecolor
            print "}"
    if x:
        u,v = L*(-y/3), L*(x/3)
        for p in (-L,L):
            for q in (-L,L):
                for r in (-L,L):
                    if (p,q,r) != (u,v,-L) and (p,q,r) != (-u,-v,L):
                        point = (x+p,z+r,y+q) # again the screwy order
                        print "sphere {"
                        print ("  <%s,%s,%s>," % point)+str(R)
                        print "  texture {"
                        if p*q*r > 0:
                            print "        Ruby_Glass"
                        else:
                            print "        Vicks_Bottle_Glass"
                        print """        finish {            ambient <0.9,0.9,0.9>            diffuse 0.2            reflection .5            specular 2            roughness .001        }      }"""
                        print "}"

r1 = (1.5**2 + (1.5-L)**2 + L**2)**0.5
r2 = (1.5**2 + (1.5+L)**2 + L**2)**0.5
h=L*2./3
r3 = ((1.5+L-h)**2 + (1.5+h-L)**2 + h**2)**0.5

for u,v in [(1,1),(1,-1),(-1,1),(-1,-1)]:
    print """disc {
  <%s,0,%s>
  <%s,1,%s>""" % (1.5*u,1.5*v,-v,u)
    print r2,r1
    print """  %s
}""" % facecolors[2]

top = "  clipped_by { box { <-5,0,-5>, <5,5,5> } }"
bottom = "  clipped_by { box { <-5,-5,-5>, <5,0,5> } }"

theta=acos(3**-0.5)*360/(2*pi)
for i in range(4):
    for outer in (r1,r2,r3,-r3):
        print """torus {
  %s, %s""" % (abs(outer),CR)
        print  "  " + edgecolor
        print "  rotate <%s,45,0>" % theta
        print "  translate <1.5,0,-1.5>"
        if outer == r3:
            print "  translate <%s,%s,%s>" % (h,h,h)
            print bottom
        elif outer == -r3:
            print "  translate <%s,%s,%s>" % (-h,-h,-h)
            print top
        if i: print "  rotate <0,%d,0>" % 90*i
        print "}"

for i in range(4):
    for R in r1,r2:
        for s in (-1,1):
            print "cone {"
            print "  <%s, %s, %s>," % (1.5+s*h,0+s*h,-1.5+s*h),
            print r3
            print "  <%s, %s, %s>," % (1.5,0,-1.5),
            print R,"open"
            print "  " + facecolors[(R == r2) ^ (i&1) ^ (s<0)]
            print s > 0 and bottom or top
            if i: print "  rotate <0,%d,0>" % 90*i
            print "}"

