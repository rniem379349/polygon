#!/usr/bin/env python

import math

def dist_calc(x, y):
    x_dist = abs(x[0] - y[0])
    y_dist = abs(x[1] - y[1])
    print "x distance: ", x_dist
    print "y distance: ", y_dist
    return math.sqrt(x_dist**2 + y_dist**2)


def poly_area(midpt, vertex_num, circumradius):
    """
    This function calculates and returns the area of the specified polygon.
    For more information on the program consult the readme file.
    """
    area = 0
    angle = 360.0/vertex_num # the interior angle of each triangle
    tri_area = 0.5 * circumradius**2 * math.sin(math.radians(angle)) # calculate area of triangle using the side-angle-side formula
    for i in range(vertex_num):
        area += tri_area # add the areas of the triangles
    return area


print poly_area([0,0],4,23.25)
print poly_area([0,0],7,0.68)
