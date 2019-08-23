"""drawbelts.py -- draw system of belts and pulleys
David Eppstein, Feb 2017

Standard input should be a sequence of lines, of two types:

"disk d x y r" defines a disk named d, centered at (x,y), of radius abs(r),
spinning clockwise if r is positive and counterclockwise if r is negative.

"belt n n n ..." defines a belt connecting the given disks in order.
"""

import sys
from PADS import SVG
from math import asin
from cmath import exp

disks = {}
belts = []

def disk(diskname, x, y, radius):
    disks[diskname] = (x,y,abs(radius),radius > 0)

def belt(disks):
    belts.append(disks)

# Parse input
for line in sys.stdin:
    line = line.split()
    if line[0] == "disk":
        disk(line[1], float(line[2]), -float(line[3]), float(line[4]))
    else:
        belt(line[1:])

# Set up SVG
scale = 100
margin = 5
minx = min(x-r for x,y,r,cw in disks.values())
maxx = max(x+r for x,y,r,cw in disks.values())
miny = min(y-r for x,y,r,cw in disks.values())
maxy = max(y+r for x,y,r,cw in disks.values())
def rescale(p):
    return (p - minx - miny*1j)*scale + margin*(1+1j)

bbox = (maxx-minx)*scale+2*margin + ((maxy-miny)*scale+2*margin)*1j

svg = SVG.SVG(bbox,sys.stdout)

# Complex number calculations
cdisks = {}
for d in disks:
    x,y,r,cw = disks[d]
    c = x + y*1j
    if not cw:
        r = -r
    cdisks[d] = (c,r)

def angleFrom(p,q):
    """Complex unit vector representing the angle from p to q"""
    return (q-p)/abs(q-p)

def bitangentAngle(disk1,disk2):
    """Complex unit vector representing the angle of the bitangency points"""
    c1,r1 = cdisks[disk1]
    c2,r2 = cdisks[disk2]
    d = abs(c1 - c2)
    theta = (c2-c1)/d               # unit vector from c1 to c2
    theta *= 1j                     # rotate 90 degrees ccw
    a = (r1-r2)/d
    psi = asin((r1-r2)/d)
    theta *= exp(-1j*psi)           # rotate some more
    return theta

# Output SVG
svg.group(stroke = SVG.colors.black, fill = SVG.colors.yellow)
for c,r in cdisks.values():
    svg.circle(rescale(c),abs(r)*scale)
svg.ungroup()

def drawbelt(disk1,disk2):
    theta = bitangentAngle(disk1,disk2)
    c1,r1 = cdisks[disk1]
    c2,r2 = cdisks[disk2]
    svg.segment(rescale(c1 + theta*r1),rescale(c2 + theta*r2))

def drawarc(disk1,disk2,disk3):
    theta1 = bitangentAngle(disk1,disk2)
    theta2 = bitangentAngle(disk2,disk3)
    c,r = cdisks[disk2]
    if r < 0:
        theta1,theta2 = theta2,theta1
    large = ((theta2/theta1).imag > 0)
    svg.arc(rescale(c+theta1*r),rescale(c+theta2*r),scale*abs(r),large)
 
svg.group({"stroke": SVG.colors.blue, "fill": "none", "stroke-width": "3"})
for belt in belts:
    if len(belt) == 1:
        c,r = cdisks[belt[0]]
        svg.circle(rescale(c),abs(r)*scale)
    else:
        for i in range(len(belt)):
            drawarc(belt[i],belt[i-1],belt[i-2])
            drawbelt(belt[i],belt[i-1])
svg.ungroup()

svg.close()
