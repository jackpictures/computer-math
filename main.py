# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 2.7.17 (default, Sep 30 2020, 13:38:04) 
# [GCC 7.5.0]
# Warning: this version of Python has problems handling the Python 3 "byte" type in constants properly.

# Embedded file name: C:\Users\Professional\PycharmProjects\pythonProject2\main.py
# Compiled at: 2021-04-20 19:46:23
# Size of source mod 2**32: 58291 bytes
import sys, platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent
from PySide2.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient
from PySide2.QtWidgets import *
from app_modules import *
import lab1_1 as l1_1, tests5_1 as t5

class EmittingStream(QtCore.QObject):
    textWritten = QtCore.Signal(str)

    def write(self, text):
        self.textWritten.emit(str(text))


class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        sys.stdout = EmittingStream()
        sys.stdout.textWritten.connect(self.normalOutputWritten)
        self.ui.pushButton_2.clicked.connect(self.lab1_1)
        self.ui.pushButton_9.clicked.connect(self.lab1_2)
        self.ui.pushButton_10.clicked.connect(self.lab1_3)
        self.ui.pushButton_11.clicked.connect(self.lab1_4)
        self.ui.pushButton_12.clicked.connect(self.lab1_5)
        self.ui.pushButton_4.clicked.connect(self.lab2_1)
        self.ui.pushButton_90.clicked.connect(self.lab2_2)
        self.ui.pushButton_96.clicked.connect(self.lab2_3)
        self.ui.pushButton_97.clicked.connect(self.lab2_4)
        self.ui.pushButton_98.clicked.connect(self.lab2_5)
        self.ui.pushButton_5.clicked.connect(self.lab2_6)
        self.ui.pushButton_6.clicked.connect(self.lab3_1)
        self.ui.pushButton_111.clicked.connect(self.lab3_2)
        self.ui.pushButton_7.clicked.connect(self.lab4_1)
        self.ui.pushButton_118.clicked.connect(self.lab4_2)
        self.ui.pushButton_14.clicked.connect(self.lab5_1)
        self.ui.pushButton_130.clicked.connect(self.lab5_2)
        UIFunctions.labelPage(self, '')
        UIFunctions.labelDescription(self, u'\u0413\u043b\u0430\u0432\u043d\u0430\u044f')
        self.ui.pushButton_20.hide()
        self.ui.pushButton_21.hide()
        self.ui.pushButton_22.hide()
        self.ui.pushButton_23.hide()
        self.ui.pushButton_24.hide()
        self.ui.pushButton_25.hide()
        self.ui.lineEdit_2.hide()
        self.ui.lineEdit_3.hide()
        self.ui.textEdit.hide()
        self.ui.pushButton_100.hide()
        self.ui.pushButton_101.hide()
        self.ui.pushButton_102.hide()
        self.ui.pushButton_103.hide()
        self.ui.pushButton_104.hide()
        self.ui.pushButton_99.hide()
        self.ui.lineEdit_18.hide()
        self.ui.lineEdit_19.hide()
        self.ui.textEdit_2.hide()
        self.ui.pushButton_105.hide()
        self.ui.pushButton_106.hide()
        self.ui.pushButton_107.hide()
        self.ui.pushButton_108.hide()
        self.ui.pushButton_109.hide()
        self.ui.pushButton_110.hide()
        self.ui.lineEdit_20.hide()
        self.ui.lineEdit_21.hide()
        self.ui.textEdit_3.hide()
        self.ui.pushButton_113.hide()
        self.ui.pushButton_114.hide()
        self.ui.pushButton_115.hide()
        self.ui.pushButton_116.hide()
        self.ui.pushButton_117.hide()
        self.ui.pushButton_112.hide()
        self.ui.lineEdit_22.hide()
        self.ui.lineEdit_23.hide()
        self.ui.textEdit_4.hide()
        self.ui.pushButton_125.hide()
        self.ui.pushButton_126.hide()
        self.ui.pushButton_127.hide()
        self.ui.pushButton_128.hide()
        self.ui.pushButton_129.hide()
        self.ui.pushButton_131.hide()
        self.ui.textEdit_5.hide()
        UIFunctions.removeTitleBar(True)
        self.setWindowTitle(u'\u041a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u043d\u0430\u044f \u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430')
        UIFunctions.labelTitle(self, u'\u041a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u043d\u0430\u044f \u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430')
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        self.ui.btn_toggle_menu.clicked.connect(lambda : UIFunctions.toggleMenu(self, 220, True))
        self.ui.pushButton_3.clicked.connect(lambda:UIFunctions.toggleMenu1(self,self.ui.stackedWidget.height()-100,True))
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, u'\u0413\u043b\u0430\u0432\u043d\u0430\u044f', 'home', 'url(:/16x16/icons/16x16/cil-home.png)', True)
        UIFunctions.addNewMenu(self, u'\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430 \u21161', 'laba1', 'url(:/16x16/icons/16x16/cil-circle.png)', True)
        UIFunctions.addNewMenu(self, u'\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430 \u21162', 'laba2', 'url(:/16x16/icons/16x16/cil-circle(1).png)', True)
        UIFunctions.addNewMenu(self, u'\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430 \u21163', 'laba3', 'url(:/16x16/icons/16x16/cil-circle(2).png)', True)
        UIFunctions.addNewMenu(self, u'\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430 \u21164', 'laba4', 'url(:/16x16/icons/16x16/cil-circle(3).png)', True)
        UIFunctions.addNewMenu(self, u'\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430 \u21165', 'laba5', 'url(:/16x16/icons/16x16/cil-circle(4).png)', True)
        UIFunctions.selectStandardMenu(self, 'btn_home')
        self.ui.label_user_icon.hide()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        UIFunctions.userIcon(self, '', 'url(:/16x16/icons/16x16/cil-equalizer.png)', True)

        def moveWindow(event):
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        UIFunctions.uiDefinitions(self)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.show()

    def __del__(self):
        sys.stdout = sys.__stdout__

    def normalOutputWritten(self, text):
        cursor = self.ui.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        cursor1 = self.ui.textEdit_2.textCursor()
        cursor1.movePosition(QtGui.QTextCursor.End)
        cursor1.insertText(text)
        cursor2 = self.ui.textEdit_3.textCursor()
        cursor2.movePosition(QtGui.QTextCursor.End)
        cursor2.insertText(text)
        cursor3 = self.ui.textEdit_4.textCursor()
        cursor3.movePosition(QtGui.QTextCursor.End)
        cursor3.insertText(text)
        cursor4 = self.ui.textEdit_5.textCursor()
        cursor4.movePosition(QtGui.QTextCursor.End)
        cursor4.insertText(text)
        self.ui.textEdit.setTextCursor(cursor)
        self.ui.textEdit.ensureCursorVisible()
        self.ui.textEdit_2.setTextCursor(cursor1)
        self.ui.textEdit_2.ensureCursorVisible()
        self.ui.textEdit_3.setTextCursor(cursor2)
        self.ui.textEdit_3.ensureCursorVisible()
        self.ui.textEdit_4.setTextCursor(cursor3)
        self.ui.textEdit_4.ensureCursorVisible()
        self.ui.textEdit_5.setTextCursor(cursor4)
        self.ui.textEdit_5.ensureCursorVisible()

    def lab1_1(self):
        self.ui.label_top_info_1.setText(u'\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u043e\u043b\u0438\u043d\u043e\u043c\u0430 \u0432 \u0442\u043e\u0447\u043a\u0435 \u043f\u043e \u0441\u0445\u0435\u043c\u0435 \u0413\u043e\u0440\u043d\u0435\u0440\u0430')
        self.ui.label_top_info_2.setText('|1')
        self.ui.lineEdit_2.setPlaceholderText('f(x)')
        self.ui.lineEdit_3.setPlaceholderText('a')
        self.ui.pushButton_20.show()
        self.ui.pushButton_21.show()
        self.ui.pushButton_22.show()
        self.ui.pushButton_23.show()
        self.ui.pushButton_24.show()
        self.ui.pushButton_25.show()
        self.ui.lineEdit_2.show()
        self.ui.lineEdit_3.show()
        self.ui.textEdit.show()
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton_9.setEnabled(True)
        self.ui.pushButton_10.setEnabled(True)
        self.ui.pushButton_11.setEnabled(True)
        self.ui.pushButton_12.setEnabled(True)
        self.ui.pushButton_23.hide()
        self.ui.pushButton_24.hide()
        self.ui.pushButton_23.hide()
        self.ui.pushButton_24.hide()
        self.ui.lineEdit_3.show()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        try:
            self.ui.pushButton_25.clicked.disconnect()
        except:
            pass

        try:
            self.ui.pushButton_20.clicked.disconnect()
            self.ui.pushButton_21.clicked.disconnect()
            self.ui.pushButton_22.clicked.disconnect()
            self.ui.pushButton_23.clicked.disconnect()
            self.ui.pushButton_24.clicked.disconnect()
            self.ui.pushButton_25.clicked.disconnect()
        except:
            pass

        def lab1_1_test1():
            self.ui.lineEdit_2.setText('-5 -1 3 -2 5')
            self.ui.lineEdit_3.setText('-1')

        def lab1_1_test2():
            self.ui.lineEdit_2.setText('-3 -2 0 -2 1')
            self.ui.lineEdit_3.setText('1.3')

        def lab1_1_test3():
            self.ui.lineEdit_2.setText('-0.9 2.1 3.7 -2.4 0.8')
            self.ui.lineEdit_3.setText('3')

        def lab1_1run():
            l1_1.lab1_1(self.ui.lineEdit_2.text(), self.ui.lineEdit_3.text())

        self.ui.textEdit.clear()
        self.ui.pushButton_20.clicked.connect(lab1_1_test1)
        self.ui.pushButton_21.clicked.connect(lab1_1_test2)
        self.ui.pushButton_22.clicked.connect(lab1_1_test3)
        self.ui.pushButton_25.clicked.connect(lab1_1run)

    def lab1_2(self):
        self.ui.label_top_info_1.setText(u'\u0427\u0430\u0441\u0442\u043d\u043e\u0435 \u043e\u0442 \u0434\u0435\u043b\u0435\u043d\u0438\u044f \u043f\u043e\u043b\u0438\u043d\u043e\u043c\u0430 \u043d\u0430 (\U0001d465\u2212\U0001d44e)')
        self.ui.label_top_info_2.setText('|2')
        self.ui.lineEdit_2.setPlaceholderText('f(x)')
        self.ui.lineEdit_3.setPlaceholderText('a')
        self.ui.pushButton_20.show()
        self.ui.pushButton_21.show()
        self.ui.pushButton_22.show()
        self.ui.pushButton_23.show()
        self.ui.pushButton_24.show()
        self.ui.pushButton_25.show()
        self.ui.lineEdit_2.show()
        self.ui.lineEdit_3.show()
        self.ui.textEdit.show()
        self.ui.pushButton_2.setEnabled(True)
        self.ui.pushButton_9.setEnabled(False)
        self.ui.pushButton_10.setEnabled(True)
        self.ui.pushButton_11.setEnabled(True)
        self.ui.pushButton_12.setEnabled(True)
        self.ui.pushButton_23.hide()
        self.ui.pushButton_24.hide()
        self.ui.lineEdit_3.show()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        try:
            self.ui.pushButton_25.clicked.disconnect()
        except:
            pass

        try:
            self.ui.pushButton_20.clicked.disconnect()
            self.ui.pushButton_21.clicked.disconnect()
            self.ui.pushButton_22.clicked.disconnect()
            self.ui.pushButton_23.clicked.disconnect()
            self.ui.pushButton_24.clicked.disconnect()
        except:
            pass

        def lab1_2_test1():
            self.ui.lineEdit_2.setText('3 1 -8 0 8 7 6')
            self.ui.lineEdit_3.setText('-2')

        def lab1_2_test2():
            self.ui.lineEdit_2.setText('8 -7 28 -5 -40 10 -3 -28 -17 -9')
            self.ui.lineEdit_3.setText('1')

        def lab1_2_test3():
            self.ui.lineEdit_2.setText('1 -1 -6 4 8')
            self.ui.lineEdit_3.setText('2')

        def lab1_2run():
            l1_1.lab1_2(self.ui.lineEdit_2.text(), self.ui.lineEdit_3.text())

        self.ui.textEdit.clear()
        self.ui.pushButton_20.clicked.connect(lab1_2_test1)
        self.ui.pushButton_21.clicked.connect(lab1_2_test2)
        self.ui.pushButton_22.clicked.connect(lab1_2_test3)
        self.ui.pushButton_25.clicked.connect(lab1_2run)

    def lab1_3(self):
        self.ui.label_top_info_1.setText(u'\u0417\u0430\u043c\u0435\u043d\u0430 \u043f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445 \u0432 \u043f\u043e\u043b\u0438\u043d\u043e\u043c\u0435 (x=y+a)')
        self.ui.label_top_info_2.setText('|3')
        self.ui.lineEdit_2.setPlaceholderText('f(x)')
        self.ui.lineEdit_3.setPlaceholderText('a')
        self.ui.pushButton_20.show()
        self.ui.pushButton_21.show()
        self.ui.pushButton_22.show()
        self.ui.pushButton_23.show()
        self.ui.pushButton_24.show()
        self.ui.pushButton_25.show()
        self.ui.lineEdit_2.show()
        self.ui.lineEdit_3.show()
        self.ui.textEdit.show()
        self.ui.pushButton_2.setEnabled(True)
        self.ui.pushButton_9.setEnabled(True)
        self.ui.pushButton_10.setEnabled(False)
        self.ui.pushButton_11.setEnabled(True)
        self.ui.pushButton_12.setEnabled(True)
        self.ui.pushButton_23.hide()
        self.ui.pushButton_24.hide()
        self.ui.lineEdit_3.show()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        try:
            self.ui.pushButton_25.clicked.disconnect()
        except:
            pass

        try:
            self.ui.pushButton_20.clicked.disconnect()
            self.ui.pushButton_21.clicked.disconnect()
            self.ui.pushButton_22.clicked.disconnect()
            self.ui.pushButton_23.clicked.disconnect()
            self.ui.pushButton_24.clicked.disconnect()
        except:
            pass

        def lab1_3_test1():
            self.ui.lineEdit_2.setText('1 -8 5 2 -7')
            self.ui.lineEdit_3.setText('2')

        def lab1_3_test2():
            self.ui.lineEdit_2.setText('1 -3 -12 52 -48')
            self.ui.lineEdit_3.setText('3')

        def lab1_3_test3():
            self.ui.lineEdit_2.setText('1 13 57 83 -34 -120 0')
            self.ui.lineEdit_3.setText('-1')

        def lab1_3run():
            l1_1.lab1_3(self.ui.lineEdit_2.text(), self.ui.lineEdit_3.text())

        self.ui.textEdit.clear()
        self.ui.pushButton_20.clicked.connect(lab1_3_test1)
        self.ui.pushButton_21.clicked.connect(lab1_3_test2)
        self.ui.pushButton_22.clicked.connect(lab1_3_test3)
        self.ui.pushButton_25.clicked.connect(lab1_3run)

    def lab1_4(self):
        self.ui.label_top_info_1.setText(u'\u0413\u0440\u0430\u043d\u0438\u0446\u044b \u043a\u043e\u0440\u043d\u0435\u0439 \u043f\u043e\u043b\u0438\u043d\u043e\u043c\u0430')
        self.ui.label_top_info_2.setText('|4')
        self.ui.lineEdit_2.setPlaceholderText('f(x)')
        self.ui.pushButton_20.show()
        self.ui.pushButton_21.show()
        self.ui.pushButton_22.show()
        self.ui.pushButton_23.show()
        self.ui.pushButton_24.show()
        self.ui.pushButton_25.show()
        self.ui.lineEdit_2.show()
        self.ui.lineEdit_3.show()
        self.ui.textEdit.show()
        self.ui.pushButton_2.setEnabled(True)
        self.ui.pushButton_9.setEnabled(True)
        self.ui.pushButton_10.setEnabled(True)
        self.ui.pushButton_11.setEnabled(False)
        self.ui.pushButton_12.setEnabled(True)
        self.ui.lineEdit_3.hide()
        self.ui.pushButton_23.show()
        self.ui.pushButton_24.hide()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        try:
            self.ui.pushButton_25.clicked.disconnect()
        except:
            pass

        try:
            self.ui.pushButton_20.clicked.disconnect()
            self.ui.pushButton_21.clicked.disconnect()
            self.ui.pushButton_22.clicked.disconnect()
            self.ui.pushButton_23.clicked.disconnect()
            self.ui.pushButton_24.clicked.disconnect()
        except:
            pass

        def lab1_4_test1():
            self.ui.lineEdit_2.setText('1 0 -12 -16 0')

        def lab1_4_test2():
            self.ui.lineEdit_2.setText('2 -13 1 103 -183 90')

        def lab1_4_test3():
            self.ui.lineEdit_2.setText('-2 -13 -13 28')

        def lab1_4_test4():
            self.ui.lineEdit_2.setText('0 0 5 -16 -45 0')

        def lab1_4run():
            l1_1.lab1_4(self.ui.lineEdit_2.text())

        self.ui.textEdit.clear()
        self.ui.pushButton_20.clicked.connect(lab1_4_test1)
        self.ui.pushButton_21.clicked.connect(lab1_4_test2)
        self.ui.pushButton_22.clicked.connect(lab1_4_test3)
        self.ui.pushButton_23.clicked.connect(lab1_4_test4)
        self.ui.pushButton_25.clicked.connect(lab1_4run)

    def lab1_5(self):
        self.ui.label_top_info_1.setText(u'\u041d\u0430\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u0435 \u043a\u043e\u0440\u043d\u0435\u0439 \u043f\u043e\u043b\u0438\u043d\u043e\u043c\u0430 \u043c\u0435\u0442\u043e\u0434\u043e\u043c \u0434\u0438\u0445\u043e\u0442\u043e\u043c\u0438\u0438')
        self.ui.label_top_info_2.setText('|5')
        self.ui.lineEdit_2.setPlaceholderText('f(x)')
        self.ui.pushButton_20.show()
        self.ui.pushButton_21.show()
        self.ui.pushButton_22.show()
        self.ui.pushButton_23.show()
        self.ui.pushButton_24.show()
        self.ui.pushButton_25.show()
        self.ui.lineEdit_2.show()
        self.ui.lineEdit_3.show()
        self.ui.textEdit.show()
        self.ui.pushButton_2.setEnabled(True)
        self.ui.pushButton_9.setEnabled(True)
        self.ui.pushButton_10.setEnabled(True)
        self.ui.pushButton_11.setEnabled(True)
        self.ui.pushButton_12.setEnabled(False)
        self.ui.lineEdit_3.hide()
        self.ui.pushButton_23.hide()
        self.ui.pushButton_24.hide()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        try:
            self.ui.pushButton_25.clicked.disconnect()
        except:
            pass

        try:
            self.ui.pushButton_20.clicked.disconnect()
            self.ui.pushButton_21.clicked.disconnect()
            self.ui.pushButton_22.clicked.disconnect()
            self.ui.pushButton_23.clicked.disconnect()
            self.ui.pushButton_24.clicked.disconnect()
        except:
            pass

        def lab1_4_test1():
            self.ui.lineEdit_2.setText('1 -7 7 15 0 0 0')

        def lab1_4_test2():
            self.ui.lineEdit_2.setText('4 0 -95 75 226 -120')

        def lab1_4_test3():
            self.ui.lineEdit_2.setText('1 3 -14 -30 49 27 -36')

        def lab1_4run():
            l1_1.lab1_5(self.ui.lineEdit_2.text())

        self.ui.textEdit.clear()
        self.ui.pushButton_20.clicked.connect(lab1_4_test1)
        self.ui.pushButton_21.clicked.connect(lab1_4_test2)
        self.ui.pushButton_22.clicked.connect(lab1_4_test3)
        self.ui.pushButton_25.clicked.connect(lab1_4run)

    def lab2_1(self):
        self.ui.label_top_info_1.setText(u'\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u043d\u0430\u044f \u043f\u043e\u043b\u0438\u043d\u043e\u043c\u0430')
        self.ui.label_top_info_2.setText('|1')
        self.ui.lineEdit_18.setPlaceholderText('f(x)')
        self.ui.pushButton_100.show()
        self.ui.pushButton_101.show()
        self.ui.pushButton_102.show()
        self.ui.pushButton_103.show()
        self.ui.pushButton_104.show()
        self.ui.pushButton_99.show()
        self.ui.lineEdit_18.show()
        self.ui.lineEdit_19.show()
        self.ui.textEdit_2.show()
        self.ui.pushButton_4.setEnabled(False)
        self.ui.pushButton_90.setEnabled(True)
        self.ui.pushButton_96.setEnabled(True)
        self.ui.pushButton_97.setEnabled(True)
        self.ui.pushButton_98.setEnabled(True)
        self.ui.pushButton_5.setEnabled(True)
        self.ui.textEdit_2.clear()
        self.ui.lineEdit_19.hide()
        self.ui.pushButton_103.show()
        self.ui.pushButton_104.hide()
        self.ui.lineEdit_18.clear()
        self.ui.lineEdit_19.clear()
        try:
            self.ui.pushButton_99.clicked.disconnect()
        except:
            pass

        try:
            self.ui.pushButton_100.clicked.disconnect()
            self.ui.pushButton_101.clicked.disconnect()
            self.ui.pushButton_102.clicked.disconnect()
            self.ui.pushButton_103.clicked.disconnect()
            self.ui.pushButton_104.clicked.disconnect()
        except:
            pass

        def lab1_4_test1():
            self.ui.lineEdit_18.setText('1 0 -12 -16 0')

        def lab1_4_test2():
            self.ui.lineEdit_18.setText('2 -13 1 103 -183 90')

        def lab1_4_test3():
            self.ui.lineEdit_18.setText('-2 -13 -13 28')

        def lab1_4_test4():
            self.ui.lineEdit_18.setText('0 0 5 -16 -45 0')

        def lab2_1run():
            l1_1.lab2_1(self.ui.lineEdit_18.text())

        self.ui.textEdit_2.clear()
        self.ui.pushButton_100.clicked.connect(lab1_4_test1)
        self.ui.pushButton_101.clicked.connect(lab1_4_test2)
        self.ui.pushButton_102.clicked.connect(lab1_4_test3)
        self.ui.pushButton_103.clicked.connect(lab1_4_test4)
        self.ui.pushButton_99.clicked.connect(lab2_1run)

    def lab2_2(self):
        self.ui.label_top_info_1.setText(u'\u041a\u043e\u0440\u043d\u0438 \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f \u043c\u0435\u0442\u043e\u0434\u043e\u043c \u0445\u043e\u0440\u0434')
        self.ui.label_top_info_2.setText('|2')
        self.ui.lineEdit_18.setPlaceholderText('f(x)')
        self.ui.lineEdit_19.setPlaceholderText('a')
        self.ui.pushButton_100.show()
        self.ui.pushButton_101.show()
        self.ui.pushButton_102.show()
        self.ui.pushButton_103.show()
        self.ui.pushButton_104.show()
        self.ui.pushButton_99.show()
        self.ui.lineEdit_18.show()
        self.ui.lineEdit_19.show()
        self.ui.textEdit_2.show()
        self.ui.pushButton_4.setEnabled(True)
        self.ui.pushButton_90.setEnabled(False)
        self.ui.pushButton_96.setEnabled(True)
        self.ui.pushButton_97.setEnabled(True)
        self.ui.pushButton_98.setEnabled(True)
        self.ui.pushButton_5.setEnabled(True)
        self.ui.textEdit_2.clear()
        self.ui.lineEdit_19.show()
        self.ui.pushButton_103.show()
        self.ui.pushButton_104.show()
        self.ui.lineEdit_18.clear()
        self.ui.lineEdit_19.clear()
        try:
            self.ui.pushButton_99.clicked.disconnect()
        except:
            pass

        try:
            self.ui.pushButton_100.clicked.disconnect()
            self.ui.pushButton_101.clicked.disconnect()
            self.ui.pushButton_102.clicked.disconnect()
            self.ui.pushButton_103.clicked.disconnect()
            self.ui.pushButton_104.clicked.disconnect()
        except:
            pass

        def lab1_4_test1():
            self.ui.lineEdit_18.setText('1 -4 -42 104 361 -420')
            self.ui.lineEdit_19.setText('9')

        def lab1_4_test2():
            self.ui.lineEdit_18.setText('10 42 -137 -604 -615 -100')
            self.ui.lineEdit_19.setText('5')

        def lab1_4_test3():
            self.ui.lineEdit_18.setText('1 -2 -39 148 -140')
            self.ui.lineEdit_19.setText('8')

        def lab1_4_test4():
            self.ui.lineEdit_18.setText('1 -13 47 -23 -48 36')
            self.ui.lineEdit_19.setText('13')

        def lab1_4_test5():
            self.ui.lineEdit_18.setText('1 -1 -3 -9')
            self.ui.lineEdit_19.setText('3')

        def lab2_1run():
            l1_1.lab2_2(self.ui.lineEdit_18.text(), self.ui.lineEdit_19.text())

        self.ui.textEdit_2.clear()
        self.ui.pushButton_100.clicked.connect(lab1_4_test1)
        self.ui.pushButton_101.clicked.connect(lab1_4_test2)
        self.ui.pushButton_102.clicked.connect(lab1_4_test3)
        self.ui.pushButton_103.clicked.connect(lab1_4_test4)
        self.ui.pushButton_104.clicked.connect(lab1_4_test5)
        self.ui.pushButton_99.clicked.connect(lab2_1run)

    def lab2_3(self):
        self.ui.label_top_info_1.setText(u'\u041a\u043e\u0440\u043d\u0438 \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f \u043c\u0435\u0442\u043e\u0434\u043e\u043c \u041d\u044c\u044e\u0442\u043e\u043d\u0430')
        self.ui.label_top_info_2.setText('|3')
        self.ui.lineEdit_18.setPlaceholderText('f(x)')
        self.ui.lineEdit_19.setPlaceholderText('a')
        self.ui.pushButton_100.show()
        self.ui.pushButton_101.show()
        self.ui.pushButton_102.show()
        self.ui.pushButton_103.show()
        self.ui.pushButton_104.show()
        self.ui.pushButton_99.show()
        self.ui.lineEdit_18.show()
        self.ui.lineEdit_19.show()
        self.ui.textEdit_2.show()
        self.ui.pushButton_4.setEnabled(True)
        self.ui.pushButton_90.setEnabled(True)
        self.ui.pushButton_96.setEnabled(False)
        self.ui.pushButton_97.setEnabled(True)
        self.ui.pushButton_98.setEnabled(True)
        self.ui.pushButton_5.setEnabled(True)
        self.ui.textEdit_2.clear()
        self.ui.lineEdit_19.show()
        self.ui.pushButton_103.show()
        self.ui.pushButton_104.show()
        self.ui.lineEdit_18.clear()
        self.ui.lineEdit_19.clear()
        try:
            self.ui.pushButton_99.clicked.disconnect()
        except:
            pass

        try:
            self.ui.pushButton_100.clicked.disconnect()
            self.ui.pushButton_101.clicked.disconnect()
            self.ui.pushButton_102.clicked.disconnect()
            self.ui.pushButton_103.clicked.disconnect()
            self.ui.pushButton_104.clicked.disconnect()
        except:
            pass

        def lab1_4_test1():
            self.ui.lineEdit_18.setText('1 -4 -42 104 361 -420')
            self.ui.lineEdit_19.setText('9')

        def lab1_4_test2():
            self.ui.lineEdit_18.setText('10 42 -137 -604 -615 -100')
            self.ui.lineEdit_19.setText('5')

        def lab1_4_test3():
            self.ui.lineEdit_18.setText('1 -2 -39 148 -140')
            self.ui.lineEdit_19.setText('8')

        def lab1_4_test4():
            self.ui.lineEdit_18.setText('1 -13 47 -23 -48 36')
            self.ui.lineEdit_19.setText('13')

        def lab1_4_test5():
            self.ui.lineEdit_18.setText('1 -1 -3 -9')
            self.ui.lineEdit_19.setText('3')

        def lab2_1run():
            l1_1.lab2_3(self.ui.lineEdit_18.text(), self.ui.lineEdit_19.text())

        self.ui.textEdit_2.clear()
        self.ui.pushButton_100.clicked.connect(lab1_4_test1)
        self.ui.pushButton_101.clicked.connect(lab1_4_test2)
        self.ui.pushButton_102.clicked.connect(lab1_4_test3)
        self.ui.pushButton_103.clicked.connect(lab1_4_test4)
        self.ui.pushButton_104.clicked.connect(lab1_4_test5)
        self.ui.pushButton_99.clicked.connect(lab2_1run)

    def lab2_4(self):
        self.ui.label_top_info_1.setText(u'\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u043e\u043b\u0438\u043d\u043e\u043c\u0430 \u043e\u0442 \u0434\u0432\u0443\u0445 \u043f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445 \u0432 \u0442\u043e\u0447\u043a\u0435 \u043f\u043e \u0441\u0445\u0435\u043c\u0435 \u0413\u043e\u0440\u043d\u0435\u0440\u0430')
        self.ui.label_top_info_2.setText('|4')
        self.ui.lineEdit_18.setPlaceholderText('A(x,y)')
        self.ui.lineEdit_19.setPlaceholderText('x0 y0')
        self.ui.pushButton_100.show()
        self.ui.pushButton_101.show()
        self.ui.pushButton_102.show()
        self.ui.pushButton_103.show()
        self.ui.pushButton_104.show()
        self.ui.pushButton_99.show()
        self.ui.lineEdit_18.show()
        self.ui.lineEdit_19.show()
        self.ui.textEdit_2.show()
        self.ui.pushButton_4.setEnabled(True)
        self.ui.pushButton_90.setEnabled(True)
        self.ui.pushButton_96.setEnabled(True)
        self.ui.pushButton_97.setEnabled(False)
        self.ui.pushButton_98.setEnabled(True)
        self.ui.pushButton_5.setEnabled(True)
        self.ui.textEdit_2.clear()
        self.ui.pushButton_103.hide()
        self.ui.pushButton_104.hide()
        self.ui.lineEdit_18.clear()
        self.ui.lineEdit_19.clear()
        try:
            self.ui.pushButton_99.clicked.disconnect()
        except:
            pass

        try:
            self.ui.pushButton_100.clicked.disconnect()
            self.ui.pushButton_101.clicked.disconnect()
            self.ui.pushButton_102.clicked.disconnect()
            self.ui.pushButton_103.clicked.disconnect()
            self.ui.pushButton_104.clicked.disconnect()
        except:
            pass

        def lab1_4_test1():
            self.ui.lineEdit_18.setText('8 0 3 8;1 7 1 4')
            self.ui.lineEdit_19.setText('-1 2')

        def lab1_4_test2():
            self.ui.lineEdit_18.setText('-3 2 3;2 -1 -4;2 2 4;1 -4 4')
            self.ui.lineEdit_19.setText('1 -3')

        def lab1_4_test3():
            self.ui.lineEdit_18.setText('3.2 4.5; 2.3 -4.5')
            self.ui.lineEdit_19.setText('2 1')

        def lab2_1run():
            l1_1.lab2_4(self.ui.lineEdit_18.text(), self.ui.lineEdit_19.text())

        self.ui.textEdit_2.clear()
        self.ui.pushButton_100.clicked.connect(lab1_4_test1)
        self.ui.pushButton_101.clicked.connect(lab1_4_test2)
        self.ui.pushButton_102.clicked.connect(lab1_4_test3)
        self.ui.pushButton_99.clicked.connect(lab2_1run)

    def lab2_5(self):
        self.ui.label_top_info_1.setText(u'\u0427\u0430\u0441\u0442\u043d\u044b\u0435 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u043d\u044b\u0435 \u043f\u043e\u043b\u0438\u043d\u043e\u043c\u0430 \u043e\u0442 \u0434\u0432\u0443\u0445 \u043f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445')
        self.ui.label_top_info_2.setText('|5')
        self.ui.lineEdit_18.setPlaceholderText('A(x,y)')
        self.ui.pushButton_100.show()
        self.ui.pushButton_101.show()
        self.ui.pushButton_102.show()
        self.ui.pushButton_103.show()
        self.ui.pushButton_104.show()
        self.ui.pushButton_99.show()
        self.ui.lineEdit_18.show()
        self.ui.lineEdit_19.show()
        self.ui.textEdit_2.show()
        self.ui.pushButton_4.setEnabled(True)
        self.ui.pushButton_90.setEnabled(True)
        self.ui.pushButton_96.setEnabled(True)
        self.ui.pushButton_97.setEnabled(True)
        self.ui.pushButton_98.setEnabled(False)
        self.ui.pushButton_5.setEnabled(True)
        self.ui.textEdit_2.clear()
        self.ui.lineEdit_19.hide()
        self.ui.pushButton_103.hide()
        self.ui.pushButton_104.hide()
        self.ui.lineEdit_18.clear()
        self.ui.lineEdit_19.clear()
        try:
            self.ui.pushButton_99.clicked.disconnect()
        except:
            pass

        try:
            self.ui.pushButton_100.clicked.disconnect()
            self.ui.pushButton_101.clicked.disconnect()
            self.ui.pushButton_102.clicked.disconnect()
            self.ui.pushButton_103.clicked.disconnect()
            self.ui.pushButton_104.clicked.disconnect()
        except:
            pass

        def lab1_4_test1():
            self.ui.lineEdit_18.setText('-1 4 3;1 3 -4;-4 1 -3')

        def lab1_4_test2():
            self.ui.lineEdit_18.setText('4 3 0 -3;1 1 3 -4')

        def lab1_4_test3():
            self.ui.lineEdit_18.setText('3 -4;0 -1;-2 -4')

        def lab2_1run():
            l1_1.lab2_5(self.ui.lineEdit_18.text())

        self.ui.textEdit_2.clear()
        self.ui.pushButton_100.clicked.connect(lab1_4_test1)
        self.ui.pushButton_101.clicked.connect(lab1_4_test2)
        self.ui.pushButton_102.clicked.connect(lab1_4_test3)
        self.ui.pushButton_99.clicked.connect(lab2_1run)

    def lab2_6(self):
        self.ui.label_top_info_1.setText(u'\u041a\u043e\u0440\u043d\u0438 \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f \u043c\u0435\u0442\u043e\u0434\u043e\u043c \u041d\u044c\u044e\u0442\u043e\u043d\u0430 \u0434\u043b\u044f \u0441\u0438\u0441\u0442\u0435\u043c \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0439 \u0441 \u0434\u0432\u0443\u043c\u044f \u043d\u0435\u0438\u0437\u0432\u0435\u0441\u0442\u043d\u044b\u043c\u0438')
        self.ui.label_top_info_2.setText('|6')
        self.ui.lineEdit_18.setPlaceholderText('A(x,y)')
        self.ui.lineEdit_19.setPlaceholderText('B(x,y)')
        self.ui.pushButton_100.show()
        self.ui.pushButton_101.show()
        self.ui.pushButton_102.show()
        self.ui.pushButton_103.show()
        self.ui.pushButton_104.show()
        self.ui.pushButton_99.show()
        self.ui.lineEdit_18.show()
        self.ui.lineEdit_19.show()
        self.ui.textEdit_2.show()
        self.ui.pushButton_4.setEnabled(True)
        self.ui.pushButton_90.setEnabled(True)
        self.ui.pushButton_96.setEnabled(True)
        self.ui.pushButton_97.setEnabled(True)
        self.ui.pushButton_98.setEnabled(True)
        self.ui.pushButton_5.setEnabled(False)
        self.ui.textEdit_2.clear()
        self.ui.pushButton_103.hide()
        self.ui.pushButton_104.hide()
        self.ui.lineEdit_18.clear()
        self.ui.lineEdit_19.clear()
        try:
            self.ui.pushButton_99.clicked.disconnect()
        except:
            pass

        try:
            self.ui.pushButton_100.clicked.disconnect()
            self.ui.pushButton_101.clicked.disconnect()
            self.ui.pushButton_102.clicked.disconnect()
            self.ui.pushButton_103.clicked.disconnect()
            self.ui.pushButton_104.clicked.disconnect()
        except:
            pass

        def lab1_4_test1():
            self.ui.lineEdit_18.setText('0 0 -2;0 0 0;2 2 3')
            self.ui.lineEdit_19.setText('0 0 0;0 4 2;0 0 0')

        def lab1_4_test2():
            self.ui.lineEdit_18.setText('0 0 -5;0 0 0;5 7 10')
            self.ui.lineEdit_19.setText('0 0 0;0 10 7;0 0 0')

        def lab1_4_test3():
            self.ui.lineEdit_18.setText('0 0 -2;0 0 0;2 3 7')
            self.ui.lineEdit_19.setText('0 0 0;0 4 3;0 0 0')

        def lab2_1run():
            l1_1.lab2_6(self.ui.lineEdit_18.text(), self.ui.lineEdit_19.text())

        self.ui.textEdit_2.clear()
        self.ui.pushButton_100.clicked.connect(lab1_4_test1)
        self.ui.pushButton_101.clicked.connect(lab1_4_test2)
        self.ui.pushButton_102.clicked.connect(lab1_4_test3)
        self.ui.pushButton_99.clicked.connect(lab2_1run)

    def lab3_1(self):
        self.ui.label_top_info_1.setText(u'\u0423\u043c\u043d\u043e\u0436\u0435\u043d\u0438\u0435 \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u043d\u044b\u0445 \u043c\u0430\u0442\u0440\u0438\u0446 \u0440\u0430\u0437\u043b\u043e\u0436\u0435\u043d\u0438\u0435\u043c \u043d\u0430 \u0431\u043b\u043e\u043a\u0438')
        self.ui.label_top_info_2.setText('|1')
        self.ui.lineEdit_20.setPlaceholderText('A(x,y)')
        self.ui.lineEdit_21.setPlaceholderText('B(x,y)')
        self.ui.pushButton_105.show()
        self.ui.pushButton_106.show()
        self.ui.pushButton_107.show()
        self.ui.pushButton_108.show()
        self.ui.pushButton_109.show()
        self.ui.pushButton_110.show()
        self.ui.lineEdit_20.show()
        self.ui.lineEdit_21.show()
        self.ui.textEdit_3.show()
        self.ui.pushButton_6.setEnabled(False)
        self.ui.pushButton_111.setEnabled(True)
        self.ui.textEdit_3.clear()
        self.ui.lineEdit_21.show()
        self.ui.pushButton_109.hide()
        self.ui.lineEdit_20.clear()
        self.ui.lineEdit_21.clear()
        try:
            self.ui.pushButton_110.clicked.disconnect()
        except:
            pass

        try:
            self.ui.pushButton_105.clicked.disconnect()
            self.ui.pushButton_106.clicked.disconnect()
            self.ui.pushButton_107.clicked.disconnect()
            self.ui.pushButton_108.clicked.disconnect()
            self.ui.pushButton_109.clicked.disconnect()
        except:
            pass

        def lab1_4_test1():
            self.ui.lineEdit_20.setText('2 0;1 0')
            self.ui.lineEdit_21.setText('1 -3;4 -2')

        def lab1_4_test2():
            self.ui.lineEdit_20.setText('0 1;1 0')
            self.ui.lineEdit_21.setText('0 1;1 0')

        def lab1_4_test3():
            self.ui.lineEdit_20.setText('0 -1 2;1 0 3;4 -3 -2')
            self.ui.lineEdit_21.setText('1 0 0;0 1 0;0 0 1')

        def lab1_4_test4():
            self.ui.lineEdit_20.setText('7 7 3;-2 -4 1;2 7 -7')
            self.ui.lineEdit_21.setText('2 -8 -4;-4 2 1;-5 -6 1')

        def lab2_1run():
            l1_1.lab3_1(self.ui.lineEdit_20.text(), self.ui.lineEdit_21.text())

        self.ui.textEdit_3.clear()
        self.ui.pushButton_105.clicked.connect(lab1_4_test1)
        self.ui.pushButton_106.clicked.connect(lab1_4_test2)
        self.ui.pushButton_107.clicked.connect(lab1_4_test3)
        self.ui.pushButton_108.clicked.connect(lab1_4_test4)
        self.ui.pushButton_110.clicked.connect(lab2_1run)

    def lab3_2(self):
        self.ui.label_top_info_1.setText(u'\u041d\u0430\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u0435 \u043e\u0431\u0440\u0430\u0442\u043d\u043e\u0439 \u043c\u0430\u0442\u0440\u0438\u0446\u044b \u0447\u0435\u0440\u0435\u0437 \u043e\u043a\u0430\u0439\u043c\u043b\u044f\u044e\u0449\u0438\u0435 \u0431\u043b\u043e\u043a\u0438, \u043d\u0430\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u0435 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044f \u043c\u0430\u0442\u0440\u0438\u0446\u044b')
        self.ui.label_top_info_2.setText('|2,3')
        self.ui.lineEdit_20.setPlaceholderText('A(x,y)')
        self.ui.pushButton_6.setEnabled(True)
        self.ui.pushButton_111.setEnabled(False)
        self.ui.pushButton_105.show()
        self.ui.pushButton_106.show()
        self.ui.pushButton_107.show()
        self.ui.pushButton_108.show()
        self.ui.pushButton_109.show()
        self.ui.pushButton_110.show()
        self.ui.lineEdit_20.show()
        self.ui.lineEdit_21.show()
        self.ui.textEdit_3.show()
        self.ui.textEdit_3.clear()
        self.ui.lineEdit_21.hide()
        self.ui.pushButton_109.show()
        self.ui.lineEdit_20.clear()
        self.ui.lineEdit_21.clear()
        try:
            self.ui.pushButton_110.clicked.disconnect()
        except:
            pass

        try:
            self.ui.pushButton_105.clicked.disconnect()
            self.ui.pushButton_106.clicked.disconnect()
            self.ui.pushButton_107.clicked.disconnect()
            self.ui.pushButton_108.clicked.disconnect()
            self.ui.pushButton_109.clicked.disconnect()
        except:
            pass

        def lab1_4_test1():
            self.ui.lineEdit_20.setText('1 -2;3 -2')

        def lab1_4_test2():
            self.ui.lineEdit_20.setText('1 0 0;0 1 0;0 0 1')

        def lab1_4_test3():
            self.ui.lineEdit_20.setText('1 6 -4;-8 6 7;-7 0 8')

        def lab1_4_test4():
            self.ui.lineEdit_20.setText('1 2 3;4 5 6;7 8 9')

        def lab1_4_test5():
            self.ui.lineEdit_20.setText('-4.6 -1.71 -3.06;2.66 -3.52 0.22;-0.79 -1.9 -4.04')

        def lab2_1run():
            l1_1.lab3_2(self.ui.lineEdit_20.text())

        self.ui.textEdit_3.clear()
        self.ui.pushButton_105.clicked.connect(lab1_4_test1)
        self.ui.pushButton_106.clicked.connect(lab1_4_test2)
        self.ui.pushButton_107.clicked.connect(lab1_4_test3)
        self.ui.pushButton_108.clicked.connect(lab1_4_test4)
        self.ui.pushButton_109.clicked.connect(lab1_4_test5)
        self.ui.pushButton_110.clicked.connect(lab2_1run)

    def lab4_1(self):
        self.ui.label_top_info_1.setText(u'\u041d\u0430\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u0435 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u043f\u043e\u043b\u0438\u043d\u043e\u043c\u0430 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u043b\u044c\u043d\u043e\u0439 \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u043d\u043e\u0439 \u043c\u0430\u0442\u0440\u0438\u0446\u044b \u043f\u043e \u043c\u0435\u0442\u043e\u0434\u0443 \u041b\u0430\u0432\u0435\u0440\u0440\u044c\u0435')
        self.ui.label_top_info_2.setText('|1')
        self.ui.lineEdit_22.setPlaceholderText('A=')
        self.ui.pushButton_113.show()
        self.ui.pushButton_114.show()
        self.ui.pushButton_115.show()
        self.ui.pushButton_116.show()
        self.ui.pushButton_117.show()
        self.ui.pushButton_112.show()
        self.ui.lineEdit_22.show()
        self.ui.lineEdit_23.show()
        self.ui.textEdit_4.show()
        self.ui.pushButton_7.setEnabled(False)
        self.ui.pushButton_118.setEnabled(True)
        self.ui.textEdit_4.clear()
        self.ui.lineEdit_23.hide()
        self.ui.pushButton_117.hide()
        self.ui.lineEdit_22.clear()
        self.ui.lineEdit_23.clear()
        try:
            self.ui.pushButton_112.clicked.disconnect()
        except:
            pass

        try:
            self.ui.pushButton_113.clicked.disconnect()
            self.ui.pushButton_114.clicked.disconnect()
            self.ui.pushButton_115.clicked.disconnect()
            self.ui.pushButton_116.clicked.disconnect()
            self.ui.pushButton_117.clicked.disconnect()
        except:
            pass

        def lab1_4_test1():
            self.ui.lineEdit_22.setText('5 4;3 -2')

        def lab1_4_test2():
            self.ui.lineEdit_22.setText('4 -4 0;3 1 3;1 2 -3')

        def lab1_4_test3():
            self.ui.lineEdit_22.setText('3 4 -1 -1;-1 -3 1 -1;-2 -4 4 2;-1 0 -5 0')

        def lab1_4_test4():
            self.ui.lineEdit_22.setText('-6.5 7.8 8.1;1.6 2.4 -9.1;-8.1 3.1 -1')

        def lab2_1run():
            l1_1.lab4_1(self.ui.lineEdit_22.text())

        self.ui.textEdit_4.clear()
        self.ui.pushButton_113.clicked.connect(lab1_4_test1)
        self.ui.pushButton_114.clicked.connect(lab1_4_test2)
        self.ui.pushButton_115.clicked.connect(lab1_4_test3)
        self.ui.pushButton_116.clicked.connect(lab1_4_test4)
        self.ui.pushButton_112.clicked.connect(lab2_1run)

    def lab4_2(self):
        self.ui.label_top_info_1.setText(u'\u041d\u0430\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u0435 \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u0441\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0433\u043e \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u043c\u0430\u0442\u0440\u0438\u0446\u044b 3 \xd7 3')
        self.ui.label_top_info_2.setText('|2')
        self.ui.lineEdit_22.setPlaceholderText('A=')
        self.ui.pushButton_113.show()
        self.ui.pushButton_114.show()
        self.ui.pushButton_115.show()
        self.ui.pushButton_116.show()
        self.ui.pushButton_117.show()
        self.ui.pushButton_112.show()
        self.ui.lineEdit_22.show()
        self.ui.lineEdit_23.show()
        self.ui.textEdit_4.show()
        self.ui.pushButton_7.setEnabled(True)
        self.ui.pushButton_118.setEnabled(False)
        self.ui.textEdit_4.clear()
        self.ui.lineEdit_23.hide()
        self.ui.pushButton_117.hide()
        self.ui.lineEdit_22.clear()
        self.ui.lineEdit_23.clear()
        try:
            self.ui.pushButton_112.clicked.disconnect()
        except:
            pass

        try:
            self.ui.pushButton_113.clicked.disconnect()
            self.ui.pushButton_114.clicked.disconnect()
            self.ui.pushButton_115.clicked.disconnect()
            self.ui.pushButton_116.clicked.disconnect()
            self.ui.pushButton_117.clicked.disconnect()
        except:
            pass

        def lab1_4_test1():
            self.ui.lineEdit_22.setText('2 1 -4;-3 4 0;-3 -1 8')

        def lab1_4_test2():
            self.ui.lineEdit_22.setText('1 -3 -2;-1 4 4;-2 3 6')

        def lab1_4_test3():
            self.ui.lineEdit_22.setText('-1 7 2;9 8 1;5 2 7')

        def lab1_4_test4():
            self.ui.lineEdit_22.setText('-10 1 -1;-4 -8 -1;-2 -5 -9')

        def lab2_1run():
            l1_1.lab4_2(self.ui.lineEdit_22.text())

        self.ui.textEdit_4.clear()
        self.ui.pushButton_113.clicked.connect(lab1_4_test1)
        self.ui.pushButton_114.clicked.connect(lab1_4_test2)
        self.ui.pushButton_115.clicked.connect(lab1_4_test3)
        self.ui.pushButton_116.clicked.connect(lab1_4_test4)
        self.ui.pushButton_112.clicked.connect(lab2_1run)

    def lab5_1(self):
        self.ui.label_top_info_1.setText(u'\u041d\u0430\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u0435 \u043f\u0440\u0438\u0431\u043b\u0438\u0436\u0451\u043d\u043d\u043e\u0439 \u0441\u0435\u0442\u043e\u0447\u043d\u043e\u0439 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u043d\u043e\u0439 \u043f\u043e \u0437\u0430\u0434\u0430\u043d\u043d\u043e\u0439 \u0441\u0435\u0442\u043e\u0447\u043d\u043e\u0439 \u0444\u0443\u043d\u043a\u0446\u0438\u0438')
        self.ui.label_top_info_2.setText('|1')
        self.ui.lineEdit_26.setPlaceholderText('f(x)')
        self.ui.lineEdit_27.setPlaceholderText(u'\u043f\u0440\u043e\u043c\u0435\u0436\u0443\u0442\u043e\u043a,\u0448\u0430\u0433')
        self.ui.pushButton_125.show()
        self.ui.pushButton_126.show()
        self.ui.pushButton_127.show()
        self.ui.pushButton_128.show()
        self.ui.pushButton_129.show()
        self.ui.pushButton_131.show()
        self.ui.lineEdit_26.show()
        self.ui.lineEdit_27.show()
        self.ui.textEdit_5.show()
        self.ui.pushButton_14.setEnabled(False)
        self.ui.pushButton_130.setEnabled(True)
        self.ui.textEdit_5.clear()
        self.ui.pushButton_129.hide()
        self.ui.lineEdit_26.clear()
        self.ui.lineEdit_27.clear()
        try:
            self.ui.pushButton_131.clicked.disconnect()
        except:
            pass

        try:
            self.ui.pushButton_125.clicked.disconnect()
            self.ui.pushButton_126.clicked.disconnect()
            self.ui.pushButton_127.clicked.disconnect()
            self.ui.pushButton_128.clicked.disconnect()
            self.ui.pushButton_129.clicked.disconnect()
        except:
            pass

        def lab1_4_test1():
            t5.lab5_1tests(1)

        def lab1_4_test2():
            t5.lab5_1tests(2)

        def lab1_4_test3():
            t5.lab5_1tests(3)

        def lab1_4_test4():
            t5.lab5_1tests(4)

        def lab2_1run():
            l1_1.lab5_1(self.ui.lineEdit_26.text(), self.ui.lineEdit_27.text())

        self.ui.textEdit_5.clear()
        self.ui.pushButton_125.clicked.connect(lab1_4_test1)
        self.ui.pushButton_126.clicked.connect(lab1_4_test2)
        self.ui.pushButton_127.clicked.connect(lab1_4_test3)
        self.ui.pushButton_128.clicked.connect(lab1_4_test4)
        self.ui.pushButton_131.clicked.connect(lab2_1run)

    def lab5_2(self):
        self.ui.label_top_info_1.setText(u'\u0418\u043d\u0442\u0435\u0433\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0441\u0435\u0442\u043e\u0447\u043d\u043e\u0439 \u0444\u0443\u043d\u043a\u0446\u0438\u0438 \u043d\u0430 \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u043e\u043c \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b\u0435 \u043f\u043e \u043e\u0431\u043e\u0431\u0449\u0451\u043d\u043d\u043e\u043c\u0443 \u043c\u0435\u0442\u043e\u0434\u0443 \u0421\u0438\u043c\u043f\u0441\u043e\u043d\u0430')
        self.ui.label_top_info_2.setText('|2')
        self.ui.lineEdit_26.setPlaceholderText('f(x)')
        self.ui.lineEdit_27.setPlaceholderText(u'\u043f\u0440\u043e\u043c\u0435\u0436\u0443\u0442\u043e\u043a,\u0448\u0430\u0433')
        self.ui.pushButton_125.show()
        self.ui.pushButton_126.show()
        self.ui.pushButton_127.show()
        self.ui.pushButton_128.show()
        self.ui.pushButton_129.show()
        self.ui.pushButton_131.show()
        self.ui.lineEdit_26.show()
        self.ui.lineEdit_27.show()
        self.ui.textEdit_5.show()
        self.ui.pushButton_14.setEnabled(True)
        self.ui.pushButton_130.setEnabled(False)
        self.ui.textEdit_5.clear()
        self.ui.pushButton_129.hide()
        self.ui.lineEdit_26.clear()
        self.ui.lineEdit_27.clear()
        try:
            self.ui.pushButton_131.clicked.disconnect()
        except:
            pass

        try:
            self.ui.pushButton_125.clicked.disconnect()
            self.ui.pushButton_126.clicked.disconnect()
            self.ui.pushButton_127.clicked.disconnect()
            self.ui.pushButton_128.clicked.disconnect()
            self.ui.pushButton_129.clicked.disconnect()
        except:
            pass

        def lab1_4_test1():
            self.ui.lineEdit_26.setText('(sin(x))^3-(cos(x/2))^2+2')
            self.ui.lineEdit_27.setText('-3 3 0.2')

        def lab1_4_test2():
            self.ui.lineEdit_26.setText('-x^4+3*x^3+4*x-5')
            self.ui.lineEdit_27.setText('0 2 0.1')

        def lab1_4_test3():
            self.ui.lineEdit_26.setText('(sin(x))^3-3*sin(x^2)+4*sin(x)+4*x')
            self.ui.lineEdit_27.setText('0 4 0.2')

        def lab1_4_test4():
            self.ui.lineEdit_26.setText('log(10*sin((3*x/5)^2)+1)')
            self.ui.lineEdit_27.setText('-3 3 0.005')

        def lab2_1run():
            l1_1.lab5_2(self.ui.lineEdit_26.text(), self.ui.lineEdit_27.text())

        self.ui.textEdit_5.clear()
        self.ui.pushButton_125.clicked.connect(lab1_4_test1)
        self.ui.pushButton_126.clicked.connect(lab1_4_test2)
        self.ui.pushButton_127.clicked.connect(lab1_4_test3)
        self.ui.pushButton_128.clicked.connect(lab1_4_test4)
        self.ui.pushButton_131.clicked.connect(lab2_1run)

    def eventFilter(self, watched, event):
        if watched == self.le:
            if event.type() == QtCore.QEvent.MouseButtonDblClick:
                print('pos: ', event.pos())

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            pass
        if event.buttons() == Qt.RightButton:
            pass
        if event.buttons() == Qt.MidButton:
            pass

    def keyPressEvent(self, event):
        pass

    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        pass

    def Button(self):
        btnWidget = self.sender()
        if btnWidget.objectName() == 'laba1':
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_laba1)
            UIFunctions.resetStyle(self, 'btn_home')
            UIFunctions.labelPage(self, '')
            self.ui.label_title_bar_top.setText(u'\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430 \u21161')
            self.ui.label_top_info_1.setText(u'\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430 \u21161')
            self.ui.label_top_info_2.setText('')
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            self.ui.textEdit.clear()
            if self.ui.pushButton_2.isEnabled() == False:
                self.ui.label_top_info_1.setText(u'\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u043e\u043b\u0438\u043d\u043e\u043c\u0430 \u0432 \u0442\u043e\u0447\u043a\u0435 \u043f\u043e \u0441\u0445\u0435\u043c\u0435 \u0413\u043e\u0440\u043d\u0435\u0440\u0430')
                self.ui.label_top_info_2.setText('|1')
                self.ui.lineEdit_2.setPlaceholderText('f(x)')
                self.ui.lineEdit_3.setPlaceholderText('a')
            else:
                if self.ui.pushButton_9.isEnabled() == False:
                    self.ui.label_top_info_1.setText(u'\u0427\u0430\u0441\u0442\u043d\u043e\u0435 \u043e\u0442 \u0434\u0435\u043b\u0435\u043d\u0438\u044f \u043f\u043e\u043b\u0438\u043d\u043e\u043c\u0430 \u043d\u0430 (\U0001d465\u2212\U0001d44e)')
                    self.ui.label_top_info_2.setText('|2')
                    self.ui.lineEdit_2.setPlaceholderText('f(x)')
                    self.ui.lineEdit_3.setPlaceholderText('a')
                else:
                    if self.ui.pushButton_10.isEnabled() == False:
                        self.ui.label_top_info_1.setText(u'\u0417\u0430\u043c\u0435\u043d\u0430 \u043f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445 \u0432 \u043f\u043e\u043b\u0438\u043d\u043e\u043c\u0435 (x=y+a)')
                        self.ui.label_top_info_2.setText('|3')
                        self.ui.lineEdit_2.setPlaceholderText('f(x)')
                        self.ui.lineEdit_3.setPlaceholderText('a')
                    else:
                        if self.ui.pushButton_11.isEnabled() == False:
                            self.ui.label_top_info_1.setText(u'\u0413\u0440\u0430\u043d\u0438\u0446\u044b \u043a\u043e\u0440\u043d\u0435\u0439 \u043f\u043e\u043b\u0438\u043d\u043e\u043c\u0430')
                            self.ui.label_top_info_2.setText('|4')
                            self.ui.lineEdit_2.setPlaceholderText('f(x)')
                        else:
                            if self.ui.pushButton_12.isEnabled() == False:
                                self.ui.label_top_info_1.setText(u'\u041d\u0430\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u0435 \u043a\u043e\u0440\u043d\u0435\u0439 \u043f\u043e\u043b\u0438\u043d\u043e\u043c\u0430 \u043c\u0435\u0442\u043e\u0434\u043e\u043c \u0434\u0438\u0445\u043e\u0442\u043e\u043c\u0438\u0438')
                                self.ui.label_top_info_2.setText('|5')
                                self.ui.lineEdit_2.setPlaceholderText('f(x)')
        if btnWidget.objectName() == 'laba2':
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_laba2)
            UIFunctions.resetStyle(self, 'btn_new_user')
            UIFunctions.labelPage(self, '')
            self.ui.label_title_bar_top.setText(u'\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430 \u21162')
            self.ui.label_top_info_1.setText(u'\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430 \u21162')
            self.ui.label_top_info_2.setText('')
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            self.ui.textEdit_2.clear()
            if self.ui.pushButton_4.isEnabled() == False:
                self.ui.label_top_info_1.setText(u'\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u043d\u0430\u044f \u043f\u043e\u043b\u0438\u043d\u043e\u043c\u0430')
                self.ui.label_top_info_2.setText('|1')
                self.ui.lineEdit_18.setPlaceholderText('f(x)')
            if self.ui.pushButton_90.isEnabled() == False:
                self.ui.label_top_info_1.setText(u'\u041a\u043e\u0440\u043d\u0438 \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f \u043c\u0435\u0442\u043e\u0434\u043e\u043c \u0445\u043e\u0440\u0434')
                self.ui.label_top_info_2.setText('|2')
                self.ui.lineEdit_18.setPlaceholderText('f(x)')
                self.ui.lineEdit_19.setPlaceholderText('a')
            if self.ui.pushButton_96.isEnabled() == False:
                self.ui.label_top_info_1.setText(u'\u041a\u043e\u0440\u043d\u0438 \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f \u043c\u0435\u0442\u043e\u0434\u043e\u043c \u041d\u044c\u044e\u0442\u043e\u043d\u0430')
                self.ui.label_top_info_2.setText('|3')
                self.ui.lineEdit_18.setPlaceholderText('f(x)')
                self.ui.lineEdit_19.setPlaceholderText('a')
            if self.ui.pushButton_97.isEnabled() == False:
                self.ui.label_top_info_1.setText(u'\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u043e\u043b\u0438\u043d\u043e\u043c\u0430 \u043e\u0442 \u0434\u0432\u0443\u0445 \u043f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445 \u0432 \u0442\u043e\u0447\u043a\u0435 \u043f\u043e \u0441\u0445\u0435\u043c\u0435 \u0413\u043e\u0440\u043d\u0435\u0440\u0430')
                self.ui.label_top_info_2.setText('|4')
                self.ui.lineEdit_18.setPlaceholderText('A(x,y)')
                self.ui.lineEdit_19.setPlaceholderText('x0 y0')
            if self.ui.pushButton_98.isEnabled() == False:
                self.ui.label_top_info_1.setText(u'\u0427\u0430\u0441\u0442\u043d\u044b\u0435 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u043d\u044b\u0435 \u043f\u043e\u043b\u0438\u043d\u043e\u043c\u0430 \u043e\u0442 \u0434\u0432\u0443\u0445 \u043f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0445')
                self.ui.label_top_info_2.setText('|5')
                self.ui.lineEdit_18.setPlaceholderText('A(x,y)')
            if self.ui.pushButton_5.isEnabled() == False:
                self.ui.label_top_info_1.setText(u'\u041a\u043e\u0440\u043d\u0438 \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f \u043c\u0435\u0442\u043e\u0434\u043e\u043c \u041d\u044c\u044e\u0442\u043e\u043d\u0430 \u0434\u043b\u044f \u0441\u0438\u0441\u0442\u0435\u043c \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0439 \u0441 \u0434\u0432\u0443\u043c\u044f \u043d\u0435\u0438\u0437\u0432\u0435\u0441\u0442\u043d\u044b\u043c\u0438')
                self.ui.label_top_info_2.setText('|6')
                self.ui.lineEdit_18.setPlaceholderText('A(x,y)')
                self.ui.lineEdit_19.setPlaceholderText('B(x,y)')
        if btnWidget.objectName() == 'laba3':
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_laba3)
            UIFunctions.resetStyle(self, 'btn_widgets')
            UIFunctions.labelPage(self, '')
            self.ui.label_title_bar_top.setText(u'\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430 \u21163')
            self.ui.label_top_info_1.setText(u'\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430 \u21163')
            self.ui.label_top_info_2.setText('')
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            self.ui.textEdit_3.clear()
            if self.ui.pushButton_6.isEnabled() == False:
                self.ui.label_top_info_1.setText(u'\u0423\u043c\u043d\u043e\u0436\u0435\u043d\u0438\u0435 \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u043d\u044b\u0445 \u043c\u0430\u0442\u0440\u0438\u0446 \u0440\u0430\u0437\u043b\u043e\u0436\u0435\u043d\u0438\u0435\u043c \u043d\u0430 \u0431\u043b\u043e\u043a\u0438')
                self.ui.label_top_info_2.setText('|1')
                self.ui.lineEdit_20.setPlaceholderText('A(x,y)')
                self.ui.lineEdit_21.setPlaceholderText('B(x,y)')
            if self.ui.pushButton_111.isEnabled() == False:
                self.ui.label_top_info_1.setText(u'\u041d\u0430\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u0435 \u043e\u0431\u0440\u0430\u0442\u043d\u043e\u0439 \u043c\u0430\u0442\u0440\u0438\u0446\u044b \u0447\u0435\u0440\u0435\u0437 \u043e\u043a\u0430\u0439\u043c\u043b\u044f\u044e\u0449\u0438\u0435 \u0431\u043b\u043e\u043a\u0438, \u043d\u0430\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u0435 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044f \u043c\u0430\u0442\u0440\u0438\u0446\u044b')
                self.ui.label_top_info_2.setText('|2,3')
                self.ui.lineEdit_20.setPlaceholderText('A(x,y)')
        if btnWidget.objectName() == 'laba4':
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_laba4)
            UIFunctions.resetStyle(self, 'btn_new_user')
            UIFunctions.labelPage(self, '')
            self.ui.label_title_bar_top.setText(u'\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430 \u21164')
            self.ui.label_top_info_1.setText(u'\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430 \u21164')
            self.ui.label_top_info_2.setText('')
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            self.ui.textEdit_4.clear()
            if self.ui.pushButton_7.isEnabled() == False:
                self.ui.label_top_info_1.setText(u'\u041d\u0430\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u0435 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u043f\u043e\u043b\u0438\u043d\u043e\u043c\u0430 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u043b\u044c\u043d\u043e\u0439 \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u043d\u043e\u0439 \u043c\u0430\u0442\u0440\u0438\u0446\u044b \u043f\u043e \u043c\u0435\u0442\u043e\u0434\u0443 \u041b\u0430\u0432\u0435\u0440\u0440\u044c\u0435')
                self.ui.label_top_info_2.setText('|1')
                self.ui.lineEdit_22.setPlaceholderText('A=')
            if self.ui.pushButton_118.isEnabled() == False:
                self.ui.label_top_info_1.setText(u'\u041d\u0430\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u0435 \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u0441\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0433\u043e \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u043c\u0430\u0442\u0440\u0438\u0446\u044b 3 \xd7 3')
                self.ui.label_top_info_2.setText('|2')
                self.ui.lineEdit_22.setPlaceholderText('A=')
        if btnWidget.objectName() == 'laba5':
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_laba5)
            UIFunctions.resetStyle(self, 'btn_new_user')
            UIFunctions.labelPage(self, '')
            self.ui.label_title_bar_top.setText(u'\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430 \u21165')
            self.ui.label_top_info_1.setText(u'\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430 \u21165')
            self.ui.label_top_info_2.setText('')
            if self.ui.pushButton_14.isEnabled() == False:
                self.ui.label_top_info_1.setText(u'\u041d\u0430\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u0435 \u043f\u0440\u0438\u0431\u043b\u0438\u0436\u0451\u043d\u043d\u043e\u0439 \u0441\u0435\u0442\u043e\u0447\u043d\u043e\u0439 \u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u043d\u043e\u0439 \u043f\u043e \u0437\u0430\u0434\u0430\u043d\u043d\u043e\u0439 \u0441\u0435\u0442\u043e\u0447\u043d\u043e\u0439 \u0444\u0443\u043d\u043a\u0446\u0438\u0438')
                self.ui.label_top_info_2.setText('|1')
                self.ui.lineEdit_26.setPlaceholderText('f(x)')
                self.ui.lineEdit_27.setPlaceholderText(u'\u043f\u0440\u043e\u043c\u0435\u0436\u0443\u0442\u043e\u043a,\u0448\u0430\u0433')
            if self.ui.pushButton_130.isEnabled() == False:
                self.ui.label_top_info_1.setText(u'\u0418\u043d\u0442\u0435\u0433\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0441\u0435\u0442\u043e\u0447\u043d\u043e\u0439 \u0444\u0443\u043d\u043a\u0446\u0438\u0438 \u043d\u0430 \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u043e\u043c \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b\u0435 \u043f\u043e \u043e\u0431\u043e\u0431\u0449\u0451\u043d\u043d\u043e\u043c\u0443 \u043c\u0435\u0442\u043e\u0434\u0443 \u0421\u0438\u043c\u043f\u0441\u043e\u043d\u0430')
                self.ui.label_top_info_2.setText('|2')
                self.ui.lineEdit_26.setPlaceholderText('f(x)')
                self.ui.lineEdit_27.setPlaceholderText(u'\u043f\u0440\u043e\u043c\u0435\u0436\u0443\u0442\u043e\u043a,\u0448\u0430\u0433')
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
            self.ui.textEdit_5.clear()
        if btnWidget.objectName() == 'btn_widgets':
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_widgets)
            UIFunctions.resetStyle(self, 'btn_new_user')
            UIFunctions.labelPage(self, 'New User')
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
        if btnWidget.objectName() == 'home':
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, 'btn_new_user')
            UIFunctions.labelPage(self, u'\u0413\u043b\u0430\u0432\u043d\u0430\u044f')
            UIFunctions.labelPage(self, '')
            self.ui.label_title_bar_top.setText(u'\u041a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u043d\u0430\u044f \u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430')
            UIFunctions.labelDescription(self, u'\u0413\u043b\u0430\u0432\u043d\u0430\u044f')
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())