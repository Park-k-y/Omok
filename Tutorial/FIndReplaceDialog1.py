from PySide2.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction
import sys

from PySide2.QtWidgets import (QDialog, QLabel, QComboBox, QPushButton, QGroupBox, QCheckBox, QGridLayout, QVBoxLayout, QHBoxLayout)
from PySide2.QtGui import QIcon
from PySide2.QtCore import Signal

class FindReplaceDialog(QDialog):
    find = Signal(str, bool, bool, bool)
    replace = Signal(str, str, bool, bool, bool)
    replaceAll = Signal(str, str, bool, bool, bool)

    def __init__ (self, parent = None):
        QDialog.__init__(self,parent)

        self.setWindowTitle("Find/Replace...")
        
        self.findLabel = QLabel("&Option")
        self.replaceLabel = QLabel("Re&place with:")

        self.findComboBox = QComboBox()
        self.replaceComboBox = QComboBox()

        self.optionGroupBox = QGroupBox("&Option")
        self.wordCheckBox = QCheckBox("Match whole word")
        self.caseCheckBox = QCheckBox("Match case")
        self.upwardCheckBox = QCheckBox("Upward")

        self.findButton = QPushButton("&Find")
        self.replaceButton = QPushButton("&Replace")
        self.replaceAllButton = QPushButton("Replace &All")
        self.closeButton = QPushButton("&Close")

        formLayout = QGridLayout()
        formLayout.addWidget(self.findLabel,0,0)
        formLayout.addWidget(self.findComboBox,0,1)
        formLayout.addWidget(self.replaceLabel,1,0)
        formLayout.addWidget(self.replaceComboBox,1,1)

        groupBoxLayout = QVBoxLayout()
        groupBoxLayout.addWidget(self.wordCheckBox)
        groupBoxLayout.addWidget(self.caseCheckBox)
        groupBoxLayout.addWidget(self.upwardCheckBox)
        self.optionGroupBox.setLayout(groupBoxLayout)

        leftLayout = QVBoxLayout()
        leftLayout.addLayout(formLayout)
        leftLayout.addWidget(self.optionGroupBox)

        rightLayout = QVBoxLayout()
        rightLayout.addWidget(self.findButton)
        rightLayout.addWidget(self.replaceButton)
        rightLayout.addWidget(self.replaceAllButton)
        rightLayout.addWidget(self.closeButton)
        rightLayout.addStretch()

        mainLayout = QHBoxLayout()
        mainLayout.addLayout(leftLayout)
        mainLayout.addLayout(rightLayout)
        self.setLayout(mainLayout)

        self.findLabel.setBuddy(self.findComboBox)
        self.replaceLabel.setBuddy(self.replaceComboBox)

        self.findComboBox.setMinimumWidth(160)
        self.findComboBox.setEditable(True)
        self.replaceComboBox.setEditable(True)

        self.findButton.setDefault(True)
        self.findButton.setEnabled(False)

        self.replaceButton.setEnabled(False)
        self.replaceAllButton.setEnabled(False)

        self.closeButton.clicked.connect(self.close)
        
        self.findComboBox.editTextChanged.connect(self.enableButtons)
        self.findComboBox.currentIndexChanged.connect(self.enableButtons)
        self.replaceComboBox.editTextChanged.connect(self.enableButtons)
        self.replaceComboBox.currentIndexChanged.connect(self.enableButtons)

        self.findButton.clicked.connect(self.onFind)
        self.replaceButton.clicked.connect(self.onReplace)
        self.replaceAllButton.clicked.connect(self.onReplaceAll)

    def enableButtons(self):
        findText = self.findComboBox.currentText()
        if findText != "":
            self.findButton.setEnabled(True)

        replaceText = self.replaceComboBox.currentText()
        if findText != "" and replaceText != "":
            self.replaceButton.setEnabled(True)
            self.replaceAllButton.setEnabled(True)

    def onFind(self):
        findText = self.findComboBox.currentText()
        matchWholeWord = self.wordCheckBox.isChecked()
        matchCase = self.caseCheckBox.isChecked()
        upward = self.upwardCheckBox.isChecked()

        index = self.findComboBox.findText(findText)
        if index != 1:
            self.findComboBox.removeItem(index)
        self.findComboBox.insertItem(0,findText)
        self.findComboBox.setCurrentIndex(0)

        self.find.emit(findText,matchWholeWord, matchCase, upward)

    def onReplace(self):
        findText = self.findComboBox.currentText()
        replaceText = self.replaceComboBox.currentText()
        matchWholeWord = self.wordCheckBox.isChecked()
        matchCase = self.caseCheckBox.isChecked()
        upward = self.upwardCheckBox.isChecked()

        index = self.findComboBox.findText(findText)
        if index != 1:
            self.findComboBox.removeItem(index)
        self.findComboBox.insertItem(0,findText)
        self.findComboBox.setCurrentIndex(0)

        index = self.replaceComboBox.findText(replaceText)
        if index != 1:
            self.replaceComboBox.removeItem(index)
        self.replaceComboBox.insertItem(0,replaceText)
        self.replaceComboBox.setCurrentIndex(0)

        self.replace.emit(findText,replaceText,matchWholeWord, matchCase, upward)

    def onReplaceAll(self):
        findText = self.findComboBox.currentText()
        replaceText = self.replaceComboBox.currentText()
        matchWholeWord = self.wordCheckBox.isChecked()
        matchCase = self.caseCheckBox.isChecked()
        upward = self.upwardCheckBox.isChecked()

        index = self.findComboBox.findText(findText)
        if index != 1:
            self.findComboBox.removeItem(index)
        self.findComboBox.insertItem(0,findText)
        self.replaceComboBox.setCurrentIndex(0)

        self.replaceAll.emit(findText,replaceText,matchWholeWord, matchCase,upward)

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self,parent)
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        action = QAction("Text",self)
        action.triggered.connect(self.findReplace)

        myMenu = self.menuBar().addMenu("&Test")
        myMenu.addAction(action)

        self.findReplaceDialog = None

    def findReplace(self):
        if self.findReplaceDialog is None:
            self.findReplaceDialog = FindReplaceDialog()
            self.findReplaceDialog.find.connect(self.find)
            self.findReplaceDialog.replace.connect(self.replace)
            self.findReplaceDialog.replaceAll.connect(self.replaceAll)
        self.findReplaceDialog.show()
        self.findReplaceDialog.raise_()
        self.findReplaceDialog.activateWindow()

    def find(self,findText,matchWholeWord,matchCase,upward):
        log = "Find operation " + findText + \
              "\nMatchWholeWord : " + str(matchWholeWord) + \
              "\nMatchCase : " + str(matchCase) + \
              "\nUpward : " + str(upward)
        self.textEdit.append(log)

    def replace(self, findText, replaceText, matchWholeWord, matchCase, upward):
        log = "Replace operation " + findText + " " + replaceText + \
              "\nMatchWholeWord : " + str(matchWholeWord) + \
              "\nMatchCase : " + str(matchCase) + \
              "\nUpward : " + str(upward)
        self.textEdit.append(log)

    def replaceAll(self,findText,replaceText,matchWholeWord,matchCase,upward):
        log = "ReplaceAll operation " + findText + " " + replaceText + \
              "\nMatchWholeWord : " + str(matchWholeWord) + \
              "\nMatchCase : " + str(matchCase) + \
              "\nUpward : " + str(upward) 
        self.textEdit.append(log)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()

    app.exec_()