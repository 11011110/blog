from pyx import canvas,path,color
from math import *

# Coordinates from Zitnik, Horvat, and Pisanski
scale=5 # 5-inch radius
R = (6 + 7*3**0.5 + 15**0.5)/12
r = (6 + 7*3**0.5 - 15**0.5)/12
L = (R - 1)
l = (r - 1)

pointsize = 0.025
 
c = canvas.canvas()

def edge(p,q):
    c.stroke(path.line(scale*p.real,scale*p.imag,scale*q.real,scale*q.imag),
             [color.rgb.black])

def point(p,x):
    c.fill(path.circle(scale*p.real,scale*p.imag,scale*pointsize),x)

for i in range(6):
    edge(R * e**((2*i)*pi*1j/6), r * e**((2*i+1)*pi*1j/6))
    edge(R * e**((2*i)*pi*1j/6), r * e**((2*i-1)*pi*1j/6))
    edge(L * e**((2*i)*pi*1j/6), l * e**((2*i+5)*pi*1j/6))
    edge(L * e**((2*i)*pi*1j/6), l * e**((2*i-5)*pi*1j/6))
    edge(R * e**((2*i)*pi*1j/6), L * e**((2*i)*pi*1j/6))
    edge(r * e**((2*i+1)*pi*1j/6), l * e**((2*i+1)*pi*1j/6))

for i in range(6):
    point(R * e**((2*i)*pi*1j/6), [color.rgb.red])
    point(r * e**((2*i+1)*pi*1j/6), [color.rgb.blue])
    point(L * e**((2*i)*pi*1j/6), [color.rgb.blue])
    point(l * e**((2*i+1)*pi*1j/6), [color.rgb.red])

c.writePDFfile("Nauru_unit_distance")
