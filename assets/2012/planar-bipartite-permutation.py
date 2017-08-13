# Draw a bipartite permutation graph in such a way that,
# if it is planar, it will be drawn planarly

import sys
from PADS import SVG

scale = 36
radius = 6

graph = {}
red = blue = level = 0

for c in sys.argv[-1]:
    if c not in ">/\<":
        print >>sys.stderr,"Unexpected character in input"
        sys.exit(-1)
    if c == "<":
        if level == 0:
            print >>sys.stderr,"Mismatched brackets"
            sys.exit(-1)
        level -= 1
    else:
        if c != "/":
            red += 1
            graph[red] = [blue-i for i in range(level)]
        if c == ">":
            level += 1
        if c != "\\":
            blue += 1
            for i in range(level):
                graph[red-i].append(blue)

if level != 0:
    print >>sys.stderr,"Unbalanced brackets"
    sys.exit(-1)

bbox = ((red+1)+(blue+1)*1j)*scale
origin = (red//2+0.5+((blue//2+0.5)*1j))*scale
output = SVG.SVG(bbox,sys.stdout)

def redpoint(r):
    x = (r-1)//2+1
    if r & 1 == 0:
        x = -x
    return x*scale+origin    
    
def bluepoint(b):
    y = (b-1)//2+1
    if b & 1 == 0:
        y = -y
    return y*1j*scale+origin    

output.group(fill=SVG.colors.none,stroke=SVG.colors.green)
for r in range(1,red+1):
    for b in graph[r]:
        output.segment(redpoint(r),bluepoint(b))
output.ungroup()

output.group(fill=SVG.colors.red,stroke=SVG.colors.black)
for r in range(1,red+1):
    output.circle(redpoint(r),radius)
output.ungroup()

output.group(fill=SVG.colors.blue,stroke=SVG.colors.black)
for b in range(1,blue+1):
    output.circle(bluepoint(b),radius)
output.ungroup()

output.close()
