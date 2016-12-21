# -*- coding: utf-8 -*-
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_untitled import Ui_Dialog
from jisuan import remove_bracket
class Dialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
    @pyqtSlot()
    def on_Button_6_clicked(self):
        self.Edit_xianshi.insertPlainText('6')
    @pyqtSlot()
    def on_Button_2_clicked(self):
        self.Edit_xianshi.insertPlainText('2')
    @pyqtSlot()
    def on_Button_3_clicked(self):
        self.Edit_xianshi.insertPlainText('3')
    @pyqtSlot()
    def on_Button_pingfang_clicked(self):
        me=self.Edit_xianshi.toPlainText()
        m=int(me) *int(me)
        self.Edit_xianshi.clear()
        self.Edit_xianshi.append(str(m))
    @pyqtSlot()
    def on_Button_add_clicked(self):
        h=self.Edit_xianshi.toPlainText()
        self.Edit_xianshi.clear()
        self.Edit_xianshi.append(h+'+')
    @pyqtSlot()
    def on_Button_jian_clicked(self):
        h = self.Edit_xianshi.toPlainText()
        self.Edit_xianshi.clear()
        self.Edit_xianshi.append(h + '-')
    @pyqtSlot()
    def on_Button_9_clicked(self):
        self.Edit_xianshi.insertPlainText('9')
    @pyqtSlot()
    def on_Button_chu_clicked(self):
        h = self.Edit_xianshi.toPlainText()
        self.Edit_xianshi.clear()
        self.Edit_xianshi.append(h + '/')
    @pyqtSlot()
    def on_Button_cheng_clicked(self):
        h = self.Edit_xianshi.toPlainText()
        self.Edit_xianshi.clear()
        self.Edit_xianshi.append(h + '*')
    @pyqtSlot()
    def on_Button_8_clicked(self):
        self.Edit_xianshi.insertPlainText('8')
    @pyqtSlot()
    def on_Button_4_clicked(self):
        self.Edit_xianshi.insertPlainText('4')
    @pyqtSlot()
    def on_Button_esc_clicked(self):
        self.Edit_xianshi.clear()
    @pyqtSlot()
    def on_Button_7_clicked(self):
        self.Edit_xianshi.insertPlainText('7')
    @pyqtSlot()
    def on_Button_1_clicked(self):
        self.Edit_xianshi.insertPlainText('1')
    @pyqtSlot()
    def on_Button_5_clicked(self):
        self.Edit_xianshi.insertPlainText('5')
    @pyqtSlot()
    def on_Button_xiaoshu_clicked(self):
        self.Edit_xianshi.insertPlainText('.')
    @pyqtSlot()
    def on_Button_0_clicked(self):
        self.Edit_xianshi.insertPlainText('0')
    @pyqtSlot()
    def on_Button_dengyu_clicked(self):
        pe=self.Edit_xianshi.toPlainText()
        m=remove_bracket(pe)
        self.Edit_xianshi.clear()
        self.Edit_xianshi.append(str(m))
if __name__ =="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.processEvents()
    ui = Dialog()
    ui.show()

    sys.exit(app.exec_())