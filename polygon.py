import math

def dist_calc(x,y):
    x_dist = abs(x[0] - y[0])
    y_dist = abs(x[1] - y[1])
    print "x distance: ", x_dist
    print "y distance: ", y_dist
    return math.sqrt(x_dist**2 + y_dist**2)
