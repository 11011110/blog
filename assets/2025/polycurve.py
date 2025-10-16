from SVG import *
import sys,random

svg = SVG(1000+200j,sys.stdout)

points = [50*i+1j*random.randint(0,101)+50j for i in range(1,20)]

svg.group(fill=colors.yellow,stroke=colors.black)
for p in points:
    svg.circle(p,10)
svg.ungroup()

svg.polycurve(points,fill=colors.none,stroke=colors.blue)

svg.close()