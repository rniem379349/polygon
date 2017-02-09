#!/usr/bin/env python

import math

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
    return str(round(area,2))

with open("polygon_tests.txt","w") as file:
    file.write("Area for polygon with 4 vertices and a circumradius of 23.25: %s\n" % poly_area([0,0],4,23.25))
    file.write("Area for polygon with 7 vertices and a circumradius of 0.68: %s\n" % poly_area([0,0],7,0.68))
    file.write("Area for polygon with 3 vertices and a circumradius of 2.76: %s\n" % poly_area([0,0],3,2.76))
    file.write("Area for polygon with 13 vertices and a circumradius of 9: %s\n" % poly_area([0,0],13,9))
