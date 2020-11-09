from PySide2.QtWidgets import (QApplication, QMainWindow, QTextEdit, QAction, QErrorMessage, QInputDialog, QLineEdit, QMessageBox)
import sys

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self,parent)
        self.logWindow = QTextEdit(self)
        self.logWindow.setReadOnly(True)
        self.setCentralWidget(self.logWindow)

        actionInt = QAction("QInputDialog::getInt()",self)
        actionDouble = QAction("QUnputDialog::getDouble()",self)
        actionText = QAction("QInputDialog::getText()",self)
        actionMultiLineText = QAction("QInputDialog::getMultiLineText",self)
        actionItem = QAction("QInputDialog::getItem()",self)

        inputDialogMenu = self.menuBar().addMenu("Q&InputDialog")
        inputDialogMenu.addAction(actionInt)
        inputDialogMenu.addAction(actionDouble)
        inputDialogMenu.addAction(actionText)
        inputDialogMenu.addAction(actionMultiLineText)
        inputDialogMenu.addAction(actionItem)

        actionInt.triggered.connect(self.getInt)
        actionDouble.triggered.connect(self.getDouble)
        actionText.triggered.connect(self.getText)
        actionMultiLineText.triggered.connect(self.getMultiLineText)
        actionItem.triggered.connect(self.getItem)

        actionAbout = QAction("QMessageBox::about()",self)
        actionInformation = QAction("QMessageBox::information()",self)
        actionQuestion = QAction("QMessageBox::question()",self)
        actionWarning = QAction("QMessageBox::warning()",self)
        actionCritical = QAction("QMessageBox::critical()",self)

        messgeWidgetMenu = self.menuBar().addMenu("Q&MessageBox")
        messgeWidgetMenu.addAction(actionAbout)
        messgeWidgetMenu.addAction(actionInformation)
        messgeWidgetMenu.addAction(actionQuestion)
        messgeWidgetMenu.addAction(actionWarning)
        messgeWidgetMenu.addAction(actionCritical)

        actionAbout.triggered.connect(self.aboutMessage)
        actionInformation.triggered.connect(self.informationMessage)
        actionQuestion.triggered.connect(self.questionMessage)
        actionWarning.triggered.connect(self.warningMessage)
        actionCritical.triggered.connect(self.criticalMessage)

        self.errorMessageDialog = QErrorMessage(self)
        self.errorMessageDialog.setWindowTitle("Error")

        actionErrorMessage = QAction("QErrorMessage::show()",self)
        errorWidgetMenu = self.menuBar().addMenu("QErrorMessage")
        errorWidgetMenu.addAction(actionErrorMessage)
        actionErrorMessage.triggered.connect(self.errorMessage)

    def getInt(self):
        value,ok = QInputDialog.getInt(self,"Input value", "Percentage:",25,0,100,1)
        if ok:
            self.logWindow.append(">>>" + str(value))
    
    def getDouble(self):
        value,ok = QInputDialog.getDouble(self, "Input Value","Amout:",37.56,-1000,1000,2)
        if ok:
            self.logWindow.append(">>>" +str(value))
        
    def getText(self):
        text,ok = QInputDialog.getText(self,"Input text","Enter text:",QLineEdit.Normal,"Enter")
        if ok and text != "":
            self.logWindow.append(">>>" + text)

    def getMultiLineText(self):
        text,ok = QInputDialog.getMultiLineText(self,"Input text","Adress:","Jihn Doe\nFredom Stress")
        if ok and text != "":
            self.logWindow.append(">>>"+text)
    
    def getItem(self):
        text,ok = QInputDialog.getItem(self,"Select season","Season:",["Spring","Summer","Fall","Winter"],0,False)
        if ok and text !="":
            self.logWindow.append(">>>" + text)

    def aboutMessage(self):
        QMessageBox.about(self,"About SectionDesigner","<h2>Section Designer 1.1</h2>""<p>Copyright &copy; 2014 Qt5Programming Inc.""<p> SectionDesigner is a small appliaction that ""computes section properties, moment - curvature diagram, and many other. ") 
    
    def questionMessage(self):
        r = QMessageBox.question(self,"Licence agreement","Do you agree the following license?""<p> 1. Use the SW as <strong>educational purpose</strong>""<p> 2. Report the bugs in use",QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        if r == QMessageBox.Yes:
            self.logWindow.append("Yes")
        elif r == QMessageBox.No:
            self.logWindow.append("No")
        else:
            self.logWindow.append("Cancel")
    def informationMessage(self):
        r = QMessageBox.information(self,"Assgin Workspace","Failed to assign the directory as workspace")

    def warningMessage(self):
        r = QMessageBox.warning(self,"Warning: Delete Node","Connot delete the connected node only.""<p>Delete all connected line?",QMessageBox.Yes | QMessageBox.No)
        if r == QMessageBox.Yes:
            self.logWindow.append("Yes")
        else:
            self.logWindow.append("No")

    def criticalMessage(self):
        r = QMessageBox.critical(self,"Error: Analysis error","Some input is not proper",QMessageBox.Abort | QMessageBox.Retry | QMessageBox.Ignore)
        if r == QMessageBox.Abort:
            self.logWindow.append("Abort")
        elif r == QMessageBox.Retry:
            self.logWindow.append("Retry")
        else:
            self.logWindow.append("Ignore")

    def errorMessage(self):
        self.errorMessageDialog.showMessage("<h2>Error 663</h2><p>Connot find file")
    
if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.resize(400,300)
    mainWindow.setWindowTitle("Feedback dialog")

    mainWindow.show()
    mainWindow.show()
    app.exec_()