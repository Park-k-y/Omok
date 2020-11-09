from PySide2.QtWidgets import QGraphicsScene, QGraphicsEllipseItem
from PySide2.QtGui import QImage, QBrush, QColor, QCursor, QKeySequence, QPen
from PySide2.QtCore import QPoint, Qt
import Poly_foundation as pf
import circle as cir
import keyboard
import time
import os

class Mainscene(QGraphicsScene):
    def __init__(self):
        super().__init__()
        # 객체 리스트
        
        self.__brushSize = 3
        self.__brushColor = Qt.black
        self.lastPoint = QPoint()
        self.__poly_drawing = False
        self.__brush_drawing = True
        self.__circle_drawing = False
        self.__point_list = []
        self.__poly_list = []
        self.__circle_list = []
        # self.__items = []

    def  keyPressEvent(self, event):
        if keyboard.is_pressed('esc'):
            if len(self.__point_list) !=0:
                self.addLine(self.__point_list[0].x,self.__point_list[0].y,self.__point_list[-1].x,self.__point_list[-1].y,QPen(self.__brushColor, self.__brushSize, Qt.SolidLine, Qt.RoundCap))
                polygon = pf.Polygon(self.__point_list)
                self.set_brush_to_true()
                self.__poly_list.append(polygon)
                self.__point_list = []
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.lastScenePos()
            self.addEllipse(self.lastPoint.x()-self.__brushSize/2,self.lastPoint.y()-self.__brushSize/2,self.__brushSize,self.__brushSize,QPen(self.__brushColor,0, Qt.SolidLine, Qt.RoundCap), QBrush(self.__brushColor,Qt.SolidPattern))

            if self.__poly_drawing == True:
                self.__point_list.append(pf.Point(self.lastPoint.x(),self.lastPoint.y()))
                if len(self.__point_list) > 1:
                    self.addLine(self.__point_list[-2].x,self.__point_list[-2].y,self.__point_list[-1].x,self.__point_list[-1].y,QPen(self.__brushColor, self.__brushSize, Qt.SolidLine, Qt.RoundCap))

            elif self.__circle_drawing == True:
                self.__point_list.append(pf.Point(self.lastPoint.x(),self.lastPoint.y()))
        


    def mouseMoveEvent(self, event):
        if(event.buttons() & Qt.LeftButton) & self.__brush_drawing:
            self.lastPoint = event.lastScenePos()
            updated_cursor_position = event.scenePos()
    
            self.addLine(self.lastPoint.x(),self.lastPoint.y(),updated_cursor_position.x(),updated_cursor_position.y(),QPen(self.__brushColor, self.__brushSize, Qt.SolidLine, Qt.RoundCap))
        
        elif self.__circle_drawing:
            self.lastPoint = event.lastScenePos()
            temp_distance= pf.Point(self.lastPoint.x(),self.lastPoint.y())
            temp_line = pf.Line(self.__point_list[0],temp_distance)
            radius = temp_line.distance()
            if len(self.items()) != 0:
                self.removeItem(self.items()[0])

            self.addEllipse(self.__point_list[0].x-radius,self.__point_list[0].y-radius,radius*2,radius*2,QPen(self.__brushColor,self.__brushSize, Qt.SolidLine, Qt.RoundCap), QBrush(self.__brushColor,Qt.NoBrush))

    def mouseReleaseEvent(self,event):
        if self.__circle_drawing:
            self.lastPoint = event.lastScenePos()
            temp_distance= pf.Point(self.lastPoint.x(),self.lastPoint.y())
            temp_line = pf.Line(self.__point_list[0],temp_distance)
            radius = temp_line.distance()
            self.__circle_list.append(cir.Circle(self.__point_list[0],radius))
            self.set_brush_to_true()
            self.__point_list = []
            

    def set_poly_to_true(self):
        self.__poly_drawing = True
        self.__brush_drawing = False
        self.__circle_drawing = False

    def set_brush_to_true(self):
        self.__poly_drawing = False
        self.__brush_drawing = True
        self.__circle_drawing = False

    def set_circle_to_true(self):
        self.__poly_drawing = False
        self.__brush_drawing = False
        self.__circle_drawing = True

    def set_brushsize(self,size):
        self.__brushSize = size
    
    def set_brushcolor(self,color):
        self.__brushColor = color

    @property
    def brushSize(self):
        return self.__brushSize

    @property
    def brushColor(self):
        return self.__brushColor

    def get_poly_data(self):
        return self.__poly_list
    
    def get_circle_data(self):
        return self.__circle_list

    def draw_polygon(self,polygon):
        for i in range(polygon.count_point()-1):
            self.addLine(polygon.point_list[i].x,polygon.point_list[i].y,polygon.point_list[i+1].x,polygon.point_list[i+1].y,QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap))
        self.addLine(polygon.point_list[-1].x,polygon.point_list[-1].y,polygon.point_list[0].x,polygon.point_list[0].y,QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap))

    def draw_circle(self,circle):
        self.addEllipse(circle.center_x-circle.radius,circle.center_y-circle.radius,circle.radius*2,circle.radius*2,QPen(self.__brushColor,self.__brushSize, Qt.SolidLine, Qt.RoundCap), QBrush(self.__brushColor,Qt.NoBrush))