import sys
from PySide2.QtWidgets import QWidget, QApplication, QMainWindow, QStatusBar, QGraphicsScene, QGraphicsSceneMouseEvent
from PySide2.QtGui import QImage, QPainter, QPen, QCursor
from PySide2.QtCore import Qt, QPointF, QPoint

class MyMain(QMainWindow):
    def __init__(self):
        super().__init__()

        self.statusbar = self.statusBar()

        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        print(self.hasMouseTracking())
        self.setMouseTracking(False)   # True 면, mouse button 안눌러도 , mouse move event 추적함.
        print(self.hasMouseTracking())


    def mouseMoveEvent(self, event):
        txt = "Mouse 위치 ; x={0},y={1}, global={2},{3}".format(event.x(), event.y(), event.globalX(), event.globalY())
        self.statusbar.showMessage(txt)
        print(event.globalX())

        orig_cursor_position = event.lastScenePos()
        print("1:",orig_cursor_position)
        updated_cursor_position = event.scenePos()
        print("2",updated_cursor_position)

        orig_position = self.scenePos()
 
        updated_cursor_x = updated_cursor_position.x() - orig_cursor_position.x() + orig_position.x()
        updated_cursor_y = updated_cursor_position.y() - orig_cursor_position.y() + orig_position.y()

        painter = QPainter(self.image)
        painter.setPen(QPen(Qt.black, 30, Qt.SolidLine, Qt.RoundCap))
        painter.drawPoint(QPoint(updated_cursor_position.x,updated_cursor_position.y))
        self.update()

    def paintEvent(self, event):
        canvasPainter  = QPainter(self)
        canvasPainter.drawImage(self.rect(),self.image, self.image.rect())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyMain()
    ex.showMaximized()
    app.exec_()