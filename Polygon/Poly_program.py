import Poly_main as Pm
import sys
sys.path.append('C:\pySideTest\Brush_Paint\Poly_foundation.py')
import Poly_foundation as Pf
import os.path

point_list = []
file_num = 1

while True:
    case_num = input("program type (1: make_polygon, 2: show point list, 0: exit) : ")

    if case_num == "1":
        filename = 'C:\pySideTest\collect_points_%d.txt'%(file_num)
        while os.path.isfile(filename):

            filename = 'C:\pySideTest\collect_points_%d.txt'%(file_num +1)
            file_num += 1

        f = open('C:\pySideTest\collect_points_%d.txt'%(file_num),'w+')
        print("File is created!\n The file directory is {0}".format(filename))

        f.write("x"+"\t"+"y"+"\n")
        try:
            while True:
                x,y = input("Input point (Exit = Ctrl + c): ").split(' ')
                point_list.append(Pf.Point(float(x),float(y)))
                f.write(str(x)+"\t"+str(y)+"\n")
                
        except KeyboardInterrupt:
            pass
        
        polygon = Pf.Polygon(point_list)
        Pm.draw_polygon(polygon)
        
        f.close()

    elif case_num == "2":
        #data show
        filename = input("Input file dir: ")
        f = open(filename,'r')
        lines = f.readlines()
        for line in lines:
            if line[0] == "x":
                pass
            else:
                tab = line.find('\t')
                x = float(line[0:tab])
                y = float(line[tab+1:])
                print("x: {0}, y: {1}".format(x,y))
                point_list.append(Pf.Point(x,y))
        polygon = Pf.Polygon(point_list)
        print("This polygon's area is ",polygon.poly_area())
        f.close()

    elif case_num == "0":
        break

    else:
        continue