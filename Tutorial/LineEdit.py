from PySide2.QtWidgets import QApplication, QLineEdit, QWidget, QVBoxLayout
from PySide2.QtGui import QPalette, QColor

import sys

class LineEdit(QLineEdit):
    def __init__(self,parent=None):
        QLineEdit.__init__(self,parent)
        self.clearOnFocus = False
        self.originalPalette = self.palette()
        self.newPalette = QPalette(self.palette())

        self.newPalette.setColor(QPalette.Normal,QPalette.Base,QColor(200,255,125))

    def setColorOnFocus(self,color):
        self.newPalette.setColor(QPalette.Normal, QPalette.Base,color)

    def setClearOnFocus(self,clear):
        self.clearOnFocus = clear
    
    def focusInEvent(self,e):
        self.setPalette(self.newPalette)
        if self.clearOnFocus :
            self.clear()
        
        QLineEdit.focusInEvent(self,e)

    def focusOutEvent(self,e):
        self.setPalette(self.originalPalette)
        QLineEdit.focusOutEvent(self,e)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = QWidget()

    lineEditId = LineEdit(mainWindow)
    lineEditPW = LineEdit(mainWindow)
    lineEditPW.setEchoMode(QLineEdit.Password)
    lineEditPW.setClearOnFocus(True)

    layout = QVBoxLayout()
    layout.addWidget(lineEditId)
    layout.addWidget(lineEditPW)

    mainWindow.setLayout(layout)
    mainWindow.setWindowTitle("Line Edit")

    mainWindow.show()
    app.exec_()