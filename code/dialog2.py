# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Admin\Desktop\Rodrigo\Programs\Horarios\untitled2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from dialog3 import Ui_Dialog3
from BackLog import BackLog
from Main import Main
import time
class Ui_Dialog2(QWidget):
    def setupUi(self, Dialog,BackLog):
        self.Dialog = Dialog
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(564, 375)
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(170, 0, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(100, 100, 311, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 70, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 140, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(480, 340, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textEdit = QtWidgets.QTextEdit(self.Dialog)
        self.textEdit.setGeometry(QtCore.QRect(100, 170, 351, 181))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_3.clicked.connect(self.window3)    
        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)
        self.backlog = BackLog
        self.configuration = self.backlog.getConfiguration()
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Welcome to SenderSN1"))
        self.lineEdit.setText(_translate("Dialog", "Subject of your email"))
        self.label_2.setText(_translate("Dialog", "Subject"))
        self.label_3.setText(_translate("Dialog", "Body"))
        self.pushButton_3.setText(_translate("Dialog", "Send"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Greetings,</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">I\'m sending your schdule of this year.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Best Regards,</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Team NoRep</p></body></html>"))
    
    
    def window3(self):
        
        if ( len(self.lineEdit.text()) > 0 and len(self.textEdit.toPlainText()) > 0 ):
            self.configuration['Subject'] = self.lineEdit.text()
            self.configuration['Msg'] = self.textEdit.toPlainText()
            self.window = QtWidgets.QMainWindow()
            self.w = Ui_Dialog3()
            self.w.setupUi(self.window, self.backlog)
            self.Dialog.hide()
            self.w.start()
            self.w.join()
            self.window.show()
        else:
            msg = QtWidgets.QMessageBox.about(self,'Error','You must insert a Subject and a message. \nPlease verify your input')
    