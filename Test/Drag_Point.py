import sys
from PySide2.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem
from PySide2.QtGui import QPen
from PySide2.QtCore import Qt, QPointF
 
 
class MovingObject(QGraphicsEllipseItem):
    def __init__(self, x, y, r):
        super().__init__(0, 0, r, r)
        self.setPos(x, y)
        self.setPen(QPen(Qt.gray,0))
        self.setAcceptHoverEvents(True)
 
    # mouse hover event
    def hoverEnterEvent(self, event):
        app.instance().setOverrideCursor(Qt.OpenHandCursor)
 
    def hoverLeaveEvent(self, event):
        app.instance().restoreOverrideCursor() 
 
    # mouse click event
    def mousePressEvent(self, event):
        pass
 
    def mouseMoveEvent(self, event):
        orig_cursor_position = event.lastScenePos()
        updated_cursor_position = event.scenePos()
 
        orig_position = self.scenePos()
 
        updated_cursor_x = updated_cursor_position.x() - orig_cursor_position.x() + orig_position.x()
        updated_cursor_y = updated_cursor_position.y() - orig_cursor_position.y() + orig_position.y()
        self.setPos(QPointF(updated_cursor_x, updated_cursor_y))
 
    def mouseReleaseEvent(self, event):
        print('x: {0}, y: {1}'.format(self.pos().x(), self.pos().y()))
 
class GraphicView(QGraphicsView):
    def __init__(self):
        super().__init__()
 
        self.scene = QGraphicsScene()
        self.setScene(self.scene)       
        self.setSceneRect(0, 0, 300, 400)
 
        self.moveObject = MovingObject(50, 50, 40)
        self.moveObject2 = MovingObject(100, 100, 100)
        self.scene.addItem(self.moveObject)
        self.scene.addItem(self.moveObject2)
 
 
app = QApplication(sys.argv)
view = GraphicView()
view.show()
sys.exit(app.exec_())
