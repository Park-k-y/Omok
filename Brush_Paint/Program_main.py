import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import QFile, Qt, QRectF
from PySide2.QtGui import QImage, QBrush, QColor, QCursor, QKeySequence, QPen
from Ui_Brush_main import Ui_MainWindow
from Brush_Scene import Mainscene
from ui_Poly_Gui import Ui_Dialog
import Poly_foundation as Pf
import circle as cir
import keyboard
import os


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.scene = Mainscene() 

        self.ui.graphicsView.setScene(self.scene)

        self.ui.action_New.triggered.connect(self.make_file)
        self.ui.action_Load.triggered.connect(self.open)
        self.ui.action_Size.triggered.connect(self.getInt)
        self.ui.action_Red.triggered.connect(self.red)
        self.ui.action_Yellow.triggered.connect(self.yellow)
        self.ui.action_Green.triggered.connect(self.green)
        self.ui.action_Black.triggered.connect(self.black)
        self.ui.action_Blue.triggered.connect(self.blue)
        self.ui.action_Polygon.triggered.connect(self.make_Polygon)
        self.ui.action_Circle.triggered.connect(self.make_Circle)
        
    
        self.data_list1 = []
        self.data_list2 = []

    def open(self):
        fileName, _ = QFileDialog.getOpenFileName(self,"Open Data File",".","i/o file (*.txt)")
        if fileName != "":
            self.load(fileName)

    def load(self,filename):
        if filename[-3:] != 'txt':
            QMessageBox.information(self,QApplication.applicationName(),"Cannot load"+fileName)
        
        self.load_poly(filename)

            
    def load_poly(self, filename):
        poly_data = []
        tmp = []
        temp= []
        temp_cir = []
        f = open(filename,'r')
        lines = f.readlines()

        for line in lines:
            
            if line[0] == 'P':
                if len(tmp) != 0:
                    temp_poly = Pf.Polygon(temp)
                    tmp.append(temp_poly)
                    poly_data.append(tmp)
                    tmp = []
                    temp = []
                tmp.append(line[0:-2])

            elif line[0] == 'C':
                if len(tmp) != 0:
                    temp_poly = Pf.Polygon(temp)
                    tmp.append(temp_poly)
                    poly_data.append(tmp)
                    tmp = []
                    temp = []
                tmp.append(line[0:-2])

            elif line[0] == 'x':
                pass

            else:
                tab = line.find('\t')
                x = float(line[0:tab])

                if line[12:] != '':
                    y = float(line[tab+1: 11])
                    r = float(line[12:])
                    tmp.append(cir.Circle(x,y,r))
                    poly_data.append(tmp)
                    tmp = []

                else:
                    y = float(line[tab+1:])
                    temp.append(Pf.Point(x,y))

        if len(tmp) != 0:
            temp_poly = Pf.Polygon(temp)
            tmp.append(temp_poly)
            poly_data.append(tmp)

        self.load_dialog(poly_data)
        
    def load_dialog(self,poly_data):
        dialog = QDialog()

        dialog.ui = Ui_Dialog()
        dialog.ui.setupUi(dialog)
        dialog.ui.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        for i in range(len(poly_data)):
            dialog.ui.listWidget.addItem(poly_data[i][0])
        
        # Item 이 True 이면, 데이터 불러오는 함수
        dialog.exec_()
        for i in range(len(poly_data)):
            if dialog.ui.listWidget.item(i).isSelected() == True:

                if type(poly_data[i][1]) == Pf.Polygon:
                    self.scene.draw_polygon(poly_data[i][1])

                else:
                    self.scene.draw_circle(poly_data[i][1])

            
    def make_Circle(self):
        self.scene.set_circle_to_true()

    def red(self):
        self.scene.set_brushcolor(Qt.red)        
    
    def yellow(self):
        self.scene.set_brushcolor(Qt.yellow)
    
    def green(self):
        self.scene.set_brushcolor(Qt.green)

    def blue(self):
        self.scene.set_brushcolor(Qt.blue)

    def black(self):
        self.scene.set_brushcolor(Qt.black)

    def getInt(self):
        value,ok = QInputDialog.getInt(self,"Input value", "Brush size:",3,0,100,1)
        if ok:
            self.scene.set_brushsize(value)
        
    def make_Polygon(self):
        self.scene.set_poly_to_true()

    def make_file(self):
        file_num = 1
        self.data_list1 = self.scene.get_poly_data()
        self.data_list2 = self.scene.get_circle_data()
        filename = 'C:\pySideTest\Data\Brush_polygon%d.txt'%(file_num)
        while os.path.isfile(filename):

            filename = 'C:\pySideTest\Data\Brush_polygon%d.txt'%(file_num +1)
            file_num += 1

        f = open('C:\pySideTest\Data\Brush_polygon%d.txt'%(file_num),'w+')
        print("File is created!\n The file directory is {0}".format(filename))
            
        try:
            for i in range(len(self.data_list1)):
                f.write("Polygon %d \n"%i)
                f.write("x"+"\t"+"y"+"\n")
                tmp_list = self.data_list1[i].point_list
                for j in range(len(tmp_list)):
                     f.write(str(tmp_list[j].x)+"\t"+str(tmp_list[j].y)+"\n")
            
            for i in range(len(self.data_list2)):
                f.write('Circle %d \n'%i)
                f.write("x"+"\t"+"y"+"\t"+"r"+"\n")
                f.write(str(self.data_list2[i].center_x)+"\t"+str(self.data_list2[i].center_y)+"\t"+str(self.data_list2[i].radius)+"\n")

        except KeyboardInterrupt:
            pass
        f.close()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(app.exec_())