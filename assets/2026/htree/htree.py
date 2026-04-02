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

svg.group(stroke=colors.blue)
htree(12,bbox,0)
svg.ungroup()

svg.close()