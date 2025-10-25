from PADS.SVG import *
from math import cos,sin,pi
import sys

o = 550+500j
bbox = 1000+1000j
a = 450j
xproj = -300
radius=4

svg = SVG(bbox,sys.stdout)

def spiral(theta):
    return a*(sin(theta)+1j*cos(theta))/theta

angles=[2,2.3,2.6,2.9]
anglepoise = [spiral(t) for t in angles]
extrema = [-abs(p) for p in anglepoise]
vex = [x-a for x in extrema]
projects = [a+v*xproj/v.real for v in vex]

dark = colors.yellow
light = "#FFE07F"

# equally spaced stripes and angles
def prect(i):
    svg.rectangle(o+projects[i],o+projects[i+1]-500)

def wedge(i):
    svg.polygon([o,o+anglepoise[i]*4,o+anglepoise[i+1]*4])

svg.group(fill=dark,stroke=colors.none)
prect(0)
prect(2)
wedge(0)
wedge(2)
svg.ungroup()
svg.group(fill=light,stroke=colors.none)
prect(1)
wedge(1)
svg.ungroup()

# asymptotic line and axis
svg.group(fill=colors.none,stroke="#666666")
svg.segment(o+a-1500j,o+a+500j)
svg.segment(o+xproj-2000j,o+xproj+2000j)
svg.segment(o+a-2000,o+a+2000)
svg.segment(o-2000,o+2000)
svg.ungroup()

# other construction lines
svg.group(fill=colors.none,stroke=colors.blue)
for p in anglepoise:
    svg.segment(o,o+p*4)
for p in extrema:
    svg.segment(o+a,o+a+3*(p-a))
for p in projects:
    svg.segment(o+p,o+p-500)
for p in anglepoise:
    svg.circle(o,abs(p))
svg.ungroup()

# spiral
angles = [0.9**i*pi for i in range(20,0,-1)] + \
         [(1+0.125*i)*pi for i in range(300)]
svg.polycurve([o+spiral(t) for t in angles],fill=colors.none,stroke=colors.red)

# points
svg.group(fill=colors.black,stroke=colors.black)
svg.circle(o,radius)
svg.circle(o+a,radius)
svg.circle(o+xproj,radius)
svg.circle(o+a+xproj,radius)
svg.ungroup()

svg.group(fill=colors.blue,stroke=colors.black)
for p in anglepoise+extrema+projects:
    svg.circle(o+p,radius)
svg.ungroup()

svg.group(style={"font-family":"Times,serif", "font-style":"italic", "font-size":"24px"})
svg.text("O",o+5-10j)
svg.text("A",o+a+5-10j)
svg.text("B",o+a+xproj+5-10j)
svg.text("C",o+xproj+5-10j)
for i in range(4):
    svg.text("PQRS"[i], o+anglepoise[i]+5+20j)
for i in range(4):
    svg.text("PQRS"[i]+'′', # unicode prime symbol
             o+extrema[0]-30+25j+35*i)
for i in range(4):
    svg.text("PQRS"[i]+'″', o+projects[i]+5+10j)
svg.ungroup()

svg.close()