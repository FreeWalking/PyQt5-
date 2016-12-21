# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\pyqt5\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(357, 320)
        Dialog.setStyleSheet("font: 75 16pt \"Aharoni\";\n"
"background-color: rgb(206, 255, 251);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(201, 210, 301, 21))
        self.label.setText("")
        self.label.setObjectName("label")
        self.Edit_xianshi = QtWidgets.QTextEdit(Dialog)
        self.Edit_xianshi.setGeometry(QtCore.QRect(0, 0, 351, 41))
        self.Edit_xianshi.setStyleSheet("font: 75 16pt \"Aharoni\";")
        self.Edit_xianshi.setObjectName("Edit_xianshi")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 30, 351, 281))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Button_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_6.setObjectName("Button_6")
        self.gridLayout.addWidget(self.Button_6, 2, 2, 1, 1)
        self.Button_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_2.setObjectName("Button_2")
        self.gridLayout.addWidget(self.Button_2, 3, 1, 1, 1)
        self.Button_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_3.setObjectName("Button_3")
        self.gridLayout.addWidget(self.Button_3, 3, 2, 1, 1)
        self.Button_fenzhi = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_fenzhi.setObjectName("Button_fenzhi")
        self.gridLayout.addWidget(self.Button_fenzhi, 1, 3, 1, 1)
        self.Button_pingfang = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_pingfang.setObjectName("Button_pingfang")
        self.gridLayout.addWidget(self.Button_pingfang, 0, 3, 1, 1)
        self.Button_add = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_add.setObjectName("Button_add")
        self.gridLayout.addWidget(self.Button_add, 2, 3, 1, 1)
        self.Button_jian = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_jian.setObjectName("Button_jian")
        self.gridLayout.addWidget(self.Button_jian, 3, 3, 1, 1)
        self.Button_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_9.setObjectName("Button_9")
        self.gridLayout.addWidget(self.Button_9, 1, 2, 1, 1)
        self.Button_chu = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_chu.setObjectName("Button_chu")
        self.gridLayout.addWidget(self.Button_chu, 0, 2, 1, 1)
        self.Button_cheng = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_cheng.setObjectName("Button_cheng")
        self.gridLayout.addWidget(self.Button_cheng, 0, 1, 1, 1)
        self.Button_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_8.setObjectName("Button_8")
        self.gridLayout.addWidget(self.Button_8, 1, 1, 1, 1)
        self.Button_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_4.setObjectName("Button_4")
        self.gridLayout.addWidget(self.Button_4, 2, 0, 1, 1)
        self.Button_esc = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_esc.setObjectName("Button_esc")
        self.gridLayout.addWidget(self.Button_esc, 0, 0, 1, 1)
        self.Button_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_7.setObjectName("Button_7")
        self.gridLayout.addWidget(self.Button_7, 1, 0, 1, 1)
        self.Button_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_1.setObjectName("Button_1")
        self.gridLayout.addWidget(self.Button_1, 3, 0, 1, 1)
        self.Button_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_5.setObjectName("Button_5")
        self.gridLayout.addWidget(self.Button_5, 2, 1, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_17.setText("")
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout.addWidget(self.pushButton_17, 4, 0, 1, 1)
        self.Button_xiaoshu = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_xiaoshu.setObjectName("Button_xiaoshu")
        self.gridLayout.addWidget(self.Button_xiaoshu, 4, 1, 1, 1)
        self.Button_0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_0.setStyleSheet("")
        self.Button_0.setObjectName("Button_0")
        self.gridLayout.addWidget(self.Button_0, 4, 2, 1, 1)
        self.Button_dengyu = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Button_dengyu.setObjectName("Button_dengyu")
        self.gridLayout.addWidget(self.Button_dengyu, 4, 3, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Edit_xianshi.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Aharoni\'; font-size:16pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-weight:400;\">0</span></p></body></html>"))
        self.Button_6.setText(_translate("Dialog", "6"))
        self.Button_2.setText(_translate("Dialog", "2"))
        self.Button_3.setText(_translate("Dialog", "3"))
        self.Button_fenzhi.setText(_translate("Dialog", "1/^"))
        self.Button_pingfang.setText(_translate("Dialog", "^2"))
        self.Button_add.setText(_translate("Dialog", "+"))
        self.Button_jian.setText(_translate("Dialog", "-"))
        self.Button_9.setText(_translate("Dialog", "9"))
        self.Button_chu.setText(_translate("Dialog", "/"))
        self.Button_cheng.setText(_translate("Dialog", "*"))
        self.Button_8.setText(_translate("Dialog", "8"))
        self.Button_4.setText(_translate("Dialog", "4"))
        self.Button_esc.setText(_translate("Dialog", "esc"))
        self.Button_7.setText(_translate("Dialog", "7"))
        self.Button_1.setText(_translate("Dialog", "1"))
        self.Button_5.setText(_translate("Dialog", "5"))
        self.Button_xiaoshu.setText(_translate("Dialog", "."))
        self.Button_0.setText(_translate("Dialog", "0"))
        self.Button_dengyu.setText(_translate("Dialog", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

