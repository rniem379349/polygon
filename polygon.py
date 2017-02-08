#!/usr/bin/env python
import math

def dist_calc(x, y):
    x_dist = abs(x[0] - y[0])
    y_dist = abs(x[1] - y[1])
    print "x distance: ", x_dist
    print "y distance: ", y_dist
    return math.sqrt(x_dist**2 + y_dist**2)


def poly_area(midpt, vertex_num, vert_to_midpt_dist):
    area = 0
    angle = 360.0/vertex_num
    tri_area = 0.5 * vert_to_midpt_dist**2 * math.sin(math.radians(angle))
    for i in range(vertex_num):
        area += tri_area
    return area

# print dist_calc([0,0],[1,1])
print poly_area([0,0],3,5)
