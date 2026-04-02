from PADS.SVG import SVG,colors
import sys

bbox = 500*(2**0.5+1j)
svg = SVG(bbox,sys.stdout)

def htree(n,b,o):
    if b.real > b.imag:
        off = b.real/2
    else:
        off = (b.imag/2) * 1j
    svg.segment(o+(b-off)/2,o+(b+off)/2)
    if n > 1:
        htree(n-1,b-off,o)
        htree(n-1,b-off,o+off)

def loop(b):
    b /= 2
    yield b
    yield b - b.real/2
    b /= 2
    yield b
    p = b
    for i in range(10):
        p += b.real/2
        yield p
        p += (b.imag/2) * 1j
        yield p
        b /= 2

svg.group(stroke=colors.blue)
htree(12,bbox,0)
svg.ungroup()

L = list(loop(bbox))
L.append(L[0])
svg.polyline(L,style={"stroke":colors.red,"stroke-width":"3","fill":"none"})

svg.close()