# Run with python3 grunbaum.py

import numpy, svg3d, pyrr, math

def get_faces():
    ends = [((2*i,1*j,0*k),(1*i,0*j,2*k),(0*i,2*j,1*k))
            for i in (-1,1) for j in (-1,1) for k in (-1,1)]
    mids = [((2,i,0),(-2,i,0),(0,2*i,j)) for i in (-1,1) for j in (-1,1)]+\
           [((i,0,2),(i,0,-2),(2*i,j,0)) for i in (-1,1) for j in (-1,1)]+\
           [((0,2,i),(0,-2,i),(j,0,2*i)) for i in (-1,1) for j in (-1,1)]
    return 7.5*numpy.float32(mids+ends)

def generate_svg(filename):
    view = pyrr.matrix44.create_look_at(
        eye=[66, 36, 108], target=[0, 0, 0], up=[0, 1, 0]
    )
    projection = pyrr.matrix44.create_perspective_projection(
        fovy=15, aspect=1, near=10, far=200
    )
    camera = svg3d.Camera(view, projection)

    style = dict(
        fill="#D8F0FF",
        fill_opacity="0.8",
        stroke="black",
        stroke_linejoin="round",
        stroke_width="0.005",
    )

    mesh = svg3d.Mesh(get_faces(), style=style)
    view = svg3d.View(camera, svg3d.Scene([mesh]))
    svg3d.Engine([view]).render(filename)


generate_svg("jessen.svg")
