# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Brush_main_2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.action_New = QAction(MainWindow)
        self.action_New.setObjectName(u"action_New")
        self.action_Load = QAction(MainWindow)
        self.action_Load.setObjectName(u"action_Load")
        self.action_Size = QAction(MainWindow)
        self.action_Size.setObjectName(u"action_Size")
        self.action_Polygon = QAction(MainWindow)
        self.action_Polygon.setObjectName(u"action_Polygon")
        self.action_Circle = QAction(MainWindow)
        self.action_Circle.setObjectName(u"action_Circle")
        self.action_Red = QAction(MainWindow)
        self.action_Red.setObjectName(u"action_Red")
        self.action_Yellow = QAction(MainWindow)
        self.action_Yellow.setObjectName(u"action_Yellow")
        self.action_Green = QAction(MainWindow)
        self.action_Green.setObjectName(u"action_Green")
        self.action_Blue = QAction(MainWindow)
        self.action_Blue.setObjectName(u"action_Blue")
        self.action_Black = QAction(MainWindow)
        self.action_Black.setObjectName(u"action_Black")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        #GraphicsScene 고정
        self.graphicsView.setSceneRect(QRectF(0, 0, 1000, 1000))
        self.graphicsView.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.graphicsView.setResizeAnchor(QGraphicsView.AnchorViewCenter)

        self.verticalLayout.addWidget(self.graphicsView)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menu_FIle = QMenu(self.menubar)
        self.menu_FIle.setObjectName(u"menu_FIle")
        self.menu_Brush = QMenu(self.menubar)
        self.menu_Brush.setObjectName(u"menu_Brush")
        self.menu_Color = QMenu(self.menu_Brush)
        self.menu_Color.setObjectName(u"menu_Color")
        self.menu_Poly = QMenu(self.menubar)
        self.menu_Poly.setObjectName(u"menu_Poly")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_FIle.menuAction())
        self.menubar.addAction(self.menu_Brush.menuAction())
        self.menubar.addAction(self.menu_Poly.menuAction())
        self.menu_FIle.addAction(self.action_New)
        self.menu_FIle.addAction(self.action_Load)
        self.menu_Brush.addAction(self.action_Size)
        self.menu_Brush.addAction(self.menu_Color.menuAction())
        self.menu_Color.addAction(self.action_Red)
        self.menu_Color.addAction(self.action_Yellow)
        self.menu_Color.addAction(self.action_Green)
        self.menu_Color.addAction(self.action_Blue)
        self.menu_Color.addAction(self.action_Black)
        self.menu_Poly.addAction(self.action_Polygon)
        self.menu_Poly.addAction(self.action_Circle)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_New.setText(QCoreApplication.translate("MainWindow", u"&New", None))
        self.action_Load.setText(QCoreApplication.translate("MainWindow", u"&Load", None))
        self.action_Size.setText(QCoreApplication.translate("MainWindow", u"&Size", None))
        self.action_Polygon.setText(QCoreApplication.translate("MainWindow", u"&Polygon", None))
        self.action_Circle.setText(QCoreApplication.translate("MainWindow", u"&Circle", None))
        self.action_Red.setText(QCoreApplication.translate("MainWindow", u"&Red", None))
        self.action_Yellow.setText(QCoreApplication.translate("MainWindow", u"&Yellow", None))
        self.action_Green.setText(QCoreApplication.translate("MainWindow", u"&Green", None))
        self.action_Blue.setText(QCoreApplication.translate("MainWindow", u"&Blue", None))
        self.action_Black.setText(QCoreApplication.translate("MainWindow", u"&Black", None))
        self.menu_FIle.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menu_Brush.setTitle(QCoreApplication.translate("MainWindow", u"&Brush", None))
        self.menu_Color.setTitle(QCoreApplication.translate("MainWindow", u"&Color", None))
        self.menu_Poly.setTitle(QCoreApplication.translate("MainWindow", u"&Poly", None))
    # retranslateUi

