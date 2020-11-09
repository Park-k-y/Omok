import math
import numpy as np
import inspect

class Point():
    def __init__(self, x = 0, y = 0):
        self.__types = (float,int)
        self.__x = x
        self.checktype(self.__x, self.__types, "Invalid type")
        self.__y = y
        self.checktype(self.__y, self.__types, "Invalid type")
        
    def checktype(self,value, type, error):
        if isinstance(value, type):
            return True
        raise TypeError(error)
    
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y
    
    @x.setter
    def x(self, new_x):
        self.__x = new_x
    @y.setter
    def set_y(self,new_y):
        self.__y = new_y
    
    def transposition(self,new_x,new_y):
        self.__x = new_x
        self.__y = new_y
    
    def multiple(self,size):
        self.__x *= size
        self.__y *= size
    
    def show_point(self):
        print("x: {0}, y: {1}".format(self.__x, self.__y))



class Line():
    def __init__(self, *args):
        self.__start = Point()
        self.__end = Point()

        if(len(args) == 4):
            start_x = args[0]
            start_y = args[1]
            end_x = args[2]
            end_y = args[3]
            self.__start = Point(start_x, start_y)
            self.__end = Point(end_x, end_y)
        elif(len(args) == 2):
            self.__start = args[0]
            self.__end = args[1]
        else:
            raise TypeError("You must input 2 points or 4 coordinates")
            
    # def __init__(self, startpoint, endpoint): 
    #     self.__types = Point
        
    #     self.__start = startpoint
    #     self.checktype(self.__start, self.__types, "Invalid type")
        
    #     self.__end = endpoint
    #     self.checktype(self.__end, self.__types, "Invalid type")

    # def checktype(self,value, types, error): 
    #     if isinstance(value, types):
    #         return True
    #     raise TypeError(error)

    @property
    def start(self):
        return self.__start
    
    @property
    def end(self):
        return self.__end

    @start.setter
    def start(self, new):
        self.__start = new 

    @end.setter
    def end(self, new):
        self.__end = new

    def distance(self):
        return math.sqrt(math.pow((self.__start.x - self.__end.x),2)+math.pow((self.__start.y - self.__end.y),2))
    
    def show_line(self):
        print("start : ({0},{1}), end:({2},{3})".format(self.__start.x, self.__start.y, self.__end.x, self.__end.y))


class Polygon():
    def __init__(self, point_list):
        self.__type1 = list
        self.__type2 = Point
        self.__point_list = []
        self.checktype(self.__point_list,self.__type1, "Invalid type")
        self.__line_list  = []
        self.__make_line(point_list)

    @property
    def point_list(self):
        return self.__point_list
    
    def checktype(self,value, types, error): 
        if isinstance(value, types):
            return True
        raise TypeError(error)

    def count_point(self):
        return len(self.__point_list)

    def __make_line(self, point_list):
        for i in range(len(point_list)):
            self.__point_list.append(point_list[i])
            self.checktype(self.__point_list[i],self.__type2, "Invalid type")
        if len(self.__point_list) >=2:
            for i in range(len(self.__point_list)-1):
                self.__line_list.append(Line(self.__point_list[i],self.__point_list[i+1]))
            self.__line_list.append(Line(self.__point_list[-1],self.__point_list[0]))

    def add_point(self,point):
        self.__point_list.append(point)   
        del self.__line_list[-1]
        self.__line_list.append(Line(self.__point_list[-2],self.__point_list[-1]))
        self.__line_list.append(Line(self.__point_list[-1],self.__point_list[0]))  

    def show_lines(self):
        for i in range(len(self.__line_list)):
            self.__line_list[i].show_line()

    def show_points(self):
        for i in range(len(self.__point_list)):
            self.__point_list[i].show_point()
    
    def simple_polygon(self):
        np.poly_x = []
        np.poly_y = []
        point_num = len(self.__point_list)
        sorted_line = []
        for i in range(point_num):
            np.poly_x.append(self.__point_list[i].x)
            np.poly_y.append(self.__point_list[i].y)

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

        for i in range(point_num):
            sorted_line.append(Line(sorted_x[i],sorted_y[i],sorted_x[i+1],sorted_y[i+1]))

        return sorted_line

    def polygon_outline(self):
        outline = 0
        for i in range(len(self.__point_list)-1):
            outline += Line.distance(Line(self.__point_list[i],self.__point_list[i+1]))
        outline += Line.distance(Line(self.__point_list[-1], self.__point_list[0]))
        return outline

    def poly_area(self):

        # 간단한 도형일 경우 
        sorted_line_list = self.simple_polygon()
        polygon_area = 0
        poly_x = []
        poly_y = []

        for i in range(len(self.__point_list)):
            poly_x.append(sorted_line_list[i].start.x)
            poly_y.append(sorted_line_list[i].start.y)

        center_point = [sum(poly_x)/len(self.__point_list), sum(poly_y)/len(self.__point_list)] 
        
        poly_x.append(sorted_line_list[0].start.x)
        poly_y.append(sorted_line_list[0].start.y)

        for i in range(len(self.__point_list)):
            a = poly_y[i+1] - poly_y[i]
            b = poly_x[i] - poly_x[i+1]
            c = poly_y[i] * (-b) - poly_x[i] * a
            height = abs(a*center_point[0]+b*center_point[1]+c)/math.sqrt(pow(a,2)+pow(b,2))
            polygon_area += sorted_line_list[i].distance() * height /2
        
        # 일 직선 상의 점이 3개 존재하지 않을 경우 
        # sum_x = 0
        # sum_y = 0

        # for i in range(len(self.__point_list)):
        #     poly_x.append(sorted_line_list[i].start.x)
        #     poly_y.append(sorted_line_list[i].start.y)
        # poly_x.append(sorted_line_list[0].start.x)
        # poly_y.append(sorted_line_list[0].start.y)

        # for i in range(len(sorted_line_list)-1):
        #     sum_x += poly_x[i] * poly_y[i+1]
        #     sum_y += poly_y[i] * poly_x[i+1]
        
        # polygon_area = (sum_x - sum_y) / 2

        return polygon_area
