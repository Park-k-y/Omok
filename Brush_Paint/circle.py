import Poly_foundation as pf
import math

class Circle():
    def __init__(self,*args):
        if len(args) == 3:
            self.__center_x = args[0]
            self.__center_y = args[1]
            self.__radius = args[2]
        
        elif len(args) == 2:
            self.__center_x = args[0].x
            self.__center_y = args[0].y
            self.__radius = args[1]

    @property
    def center_x(self):
        return self.__center_x

    @center_x.setter
    def center_x(self,new_x):
        self.__center_x = new_x

    @property
    def center_y(self):
        return self.__center_y

    @center_y.setter
    def center_y(self,new_y):
        self.__center_y = new_y

    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, new_r):
        self.__radius = new_r
    
    def area(self):
        return math.pi * math.pow(self.__radius,2)
    
    def perimeter(self):
        return 2*math.pi*self.__radius
    