# -*- coding: utf-8 -*-
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Ui_ting import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import urllib.request
import pygame,threading,queue,time,json,os,pydub
from docx import Document
from pydub import AudioSegment
from functools import reduce
from docx.shared import Inches
my_text_queue_flag=queue.Queue(10)
my_mp3_queue_flag=queue.Queue(10)
my_text_queue = queue.Queue(102400)
my_mp3_queue = []
def writeQ(queue,data):
    queue.put(data, 1)
def readQ(queue):
    val = queue.get(1)
    return val
def text_to_mp3(queue,filename,per):
    i=0
    while queue.qsize():
        me=readQ(queue)
        cuid = '2cc70758f7a04435b3f8e386c986fe'#这个需要自己去百度云语音获取
        tex = urllib.parse.quote(me)
        tok = '23.5488fa28e5fc7545ae7c26f78af78df6.2592000.1485133745.1462177047-9016631'#有效期为一个月，用完可以自己获取，也可以通过函数实现
        url = "http://tsn.baidu.com/text2audio?tex=" + tex + '&lan=zh&cuid=' + cuid + '&ctp=1&tok=' + tok + '&per=' + per
        response = urllib.request.Request(url)
        html = urllib.request.urlopen(response).read()
        if len(html)<43:
            pass
        else:
            file_name = u'%s.mp3' %i
            f = open(file_name, 'wb')
            f.write(html)
            f.close()
            my_mp3_queue.append(file_name)
            print(file_name)
            i+=1
            time.sleep(2)
    time.sleep(2)
    self.progressBar.setValue(60)
    meke_one_file(my_mp3_queue)
def come_mp3(song1,song2):#合成mp3
    f1=AudioSegment.from_mp3(song1)
    f2 =AudioSegment.from_mp3(song2)
    silent = AudioSegment.silent(duration=1000)
    new = AudioSegment.empty()
    new+=f1+f2
    new.export('listening.mp3', format='mp3')
    if song1=='listening.mp3':
        pass
    else:
        os.remove(song1)
    os.remove(song2)
    return 'listening.mp3'
def playaudio(file):#利用pygame播放
    pygame.mixer.init()
    track = pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    time.sleep(10)
    pygame.mixer.music.stop()
def meke_one_file(queue):
    reduce(come_mp3, queue)
    ui.progressBar.setValue(100)
    file_name=u'listening.mp3'
    playaudio(file_name)
class MyThread(threading.Thread):#多线程
    def __init__(self, func,filename,per, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.filename = filename
        self.per=per
        self.my_text_queue=my_text_queue
        print(filename,per,func)
    def getResult(self):
        return self.res
    def run(self):
        self.res = self.func(self.my_text_queue,self.filename,self.per)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):

        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.per='0'

    @pyqtSlot()
    def on_textEdit_textChanged(self):
        mr=self.textEdit.toPlainText()
        self.label_4.setText(u'已经输入%s个字'%len(mr))
    @pyqtSlot(bool)
    def on_pushButton_clicked(self, checked):
        me=self.textEdit.toPlainText()
        me=me.replace('\n',',')
        me = me.replace('\r\n', ',')
        me = me.replace('\n\r', ',')
        me = me.replace('\t', ',')
        me = me.replace(' ', '_')
        text = me.replace(u' ', u'_')
        text = me.replace(u'　', u'_')
        text = me.replace(u'，', u',')
        text = me.split(u',')
        for data in text:
            if data != u'__':
                writeQ(my_text_queue, data)
        filename = (r'\\')
        per=self.per
        text_2_mp3_thread = MyThread(text_to_mp3,(my_text_queue,filename,per),text_to_mp3.__name__)  # 新建线程，负责读取串口数据
        text_2_mp3_thread.start()  # 开启线程
    @pyqtSlot()
    def on_actionDakai_triggered(self):
        my_file = QFileDialog.getOpenFileName(self, u'打开文件', '/')
        if my_file[0][-4:] == '.txt':
            f = open(my_file[0])
            my_data = f.read()
            f.close()
            self.textEdit.clear()
            self.textEdit.append(my_data)
            QMessageBox.information(self, u'提示', u'倒入成功')
            self.progressBar.setValue(30)
        elif my_file[0][-4:] == '.doc' or my_file[0][-5:] == '.docx':
            doc=Document(u"%s"%(my_file[0].replace(u'/',u'\\')))
            for paragraph in doc.paragraphs:
                self.textEdit.insertPlainText(paragraph.text)
            QMessageBox.information(self,u'提示',u'倒入成功')
            self.progressBar.setValue(30)
        else:
            QMessageBox.information(self,u'错误',u'暂时不支持这个格式的文件')
    @pyqtSlot()
    def on_action_triggered(self):
        pass

    @pyqtSlot()
    def on_radioButton_clicked(self):
        self.per='1'
    @pyqtSlot()
    def on_radioButton_2_clicked(self):
        self.per='0'
    @pyqtSlot()
    def on_actionTuichu_triggered(self):
        sys.exit()
    @pyqtSlot()
    def on_actionQingkong_triggered(self):
        self.be=self.textEdit.clear()
    @pyqtSlot()
    def on_actionJianqie_triggered(self):
        pass
    @pyqtSlot()
    def on_actionFuzhi_triggered(self):
        self.textEdit.selectAll()
    @pyqtSlot()
    def on_actionZhantie_triggered(self):
        pass
    @pyqtSlot()
    def on_actionZuozhe_triggered(self):
        QMessageBox.about(self, u'作者简介', u'雷子，一个测试工程师，一个北漂，自学python')
    @pyqtSlot()
    def on_actionRuanjian_triggered(self):
        QMessageBox.about(self,u'关于软件',u'雷子听书，雷子学习pyqt5写的小程序，仅供学习')

    @pyqtSlot()
    def on_action_triggered(self):
        pass
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pixmap = QtGui.QPixmap(r"C:\Users\Administrator\Desktop\pyqt5\leizitingshu\icon\下载.jpg")
    pixmap = QSplashScreen(pixmap)
    pixmap.show()
    pixmap.showMessage(u'加在资源')
    time.sleep(1)
    pixmap.showMessage(u'加在配置')
    time.sleep(1)
    ui = MainWindow()
    ui.setWindowTitle( '雷子听书')
    ui.setWindowIcon(QIcon(r'C:\Users\Administrator\Desktop\pyqt5\leizitingshu\icon\雷子.jpg'))
    ui.show()
    pixmap.finish(ui)
    sys.exit(app.exec_())
