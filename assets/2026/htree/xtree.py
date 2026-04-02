from PADS.SVG import SVG,colors
import sys

scale = 600
bbox = scale*(1+1j)
power = 32
radius = 4
svg = SVG(bbox,sys.stdout)

svg.group(stroke=colors.green)
for i in range(power):
    x = i*(scale/power)
    svg.segment(x,bbox-x*1j)
    svg.segment(scale-x,(scale-x)*1j)
    if x:
        svg.segment(x*1j,bbox-x)
        svg.segment(scale+x*1j,scale*1j+x)
svg.ungroup()

svg.group(fill=colors.white)
for i in range(power+1):
    for j in range(power+1):
        if (i ^ (i-1)) != (j ^ (j-1)):
            svg.circle(i*(scale/power)+j*(scale*1j/power),radius)
svg.ungroup()

svg.close()