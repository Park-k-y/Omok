import sys
sys.path.append('C:\pySideTest\Brush_Paint\Poly_foundation.py')
import numpy as np
import matplotlib.pyplot as plt
import math

def draw_polygon(polygon):
    np.poly_x = []
    np.poly_y = []
    point_num = len(polygon.point_list)
    sorted_line = []
    for i in range(point_num):
        np.poly_x.append(polygon.point_list[i].x)
        np.poly_y.append(polygon.point_list[i].y)

    center_point = [np.sum(np.poly_x)/point_num, np.sum(np.poly_y)/point_num]
    angles = np.arctan2(np.poly_x-center_point[0], np.poly_y-center_point[1])

    sort_tups = sorted([(i,j,k) for i,j,k in zip(np.poly_x,np.poly_y,angles)], key = lambda t: t[2])

    if len(sort_tups) != len(set(sort_tups)):
        raise Exception('two equal coordinates -- exiting')

    sorted_x,sorted_y,sorted_ang = zip(*sort_tups)
    sorted_x = list(sorted_x)
    sorted_y = list(sorted_y)

    sorted_x.append(sorted_x[0])
    sorted_y.append(sorted_y[0])
    plt.plot(sorted_x,sorted_y)
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    

    plt.title("Area :"+str(polygon.poly_area()))

    plt.show()
