# polygon
Regular Polygon Area Calculator
Author: Robert Niemiec
Date: 08.02.2017
This is a simple regular polygon area calculator, which takes three arguments:
1) midpt - these are the carthesian coordinates for the midpoint of the polygon (supplied in an array/tuple),
2) vertex_num - this is the number of vertices,
3) circumradius - this is the distance from the midpoint to any vertice of the polygon.
The program divides the polygon into several equal triangles (as many as there are vertices), calculates their areas and adds them together,
resulting in the area of the entire polygon.

Required python libraries:
- math
