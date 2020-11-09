# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Logon.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Logon(object):
    def setupUi(self, Logon):
        if not Logon.objectName():
            Logon.setObjectName(u"Logon")
        Logon.resize(366, 208)
        self.widget = QWidget(Logon)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 40, 315, 61))
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)

        self.widget1 = QWidget(Logon)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(60, 140, 251, 36))
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(128, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.widget1)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.lineEdit)
        self.label_2.setBuddy(self.lineEdit_2)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.lineEdit, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.pushButton)

        self.retranslateUi(Logon)

        QMetaObject.connectSlotsByName(Logon)
    # setupUi

    def retranslateUi(self, Logon):
        Logon.setWindowTitle(QCoreApplication.translate("Logon", u"Form", None))
        self.label.setText(QCoreApplication.translate("Logon", u"&ID", None))
        self.label_2.setText(QCoreApplication.translate("Logon", u"&Password", None))
        self.lineEdit_2.setText("")
        self.pushButton.setText(QCoreApplication.translate("Logon", u"Ok", None))
    # retranslateUi

