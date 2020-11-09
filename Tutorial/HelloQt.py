from PySide2.QtWidgets import QApplication, QWidget, QLabel
import sys

app = QApplication(sys.argv)

window = QWidget()
window.resize(289,170)
window.setWindowTitle("First Qt Program")

label = QLabel('Hello Qt',window)
label.move(110,80)

window.show()
app.exec_()