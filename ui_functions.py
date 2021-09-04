# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 2.7.17 (default, Sep 30 2020, 13:38:04) 
# [GCC 7.5.0]
# Warning: this version of Python has problems handling the Python 3 "byte" type in constants properly.

# Embedded file name: C:\Users\Professional\PycharmProjects\pythonProject2\ui_functions.py
# Compiled at: 2021-04-19 16:22:26
# Size of source mod 2**32: 8667 bytes
from main import *
GLOBAL_STATE = 0
GLOBAL_TITLE_BAR = True
count = 1

class UIFunctions(MainWindow):
    GLOBAL_STATE = 0
    GLOBAL_TITLE_BAR = True

    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.btn_maximize_restore.setToolTip('Restore')
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(':/16x16/icons/16x16/cil-window-restore.png'))
            self.ui.frame_top_btns.setStyleSheet('background-color: rgb(27, 29, 35)')
            self.ui.frame_size_grip.hide()
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.ui.horizontalLayout.setContentsMargins(10, 10, 10, 10)
            self.ui.btn_maximize_restore.setToolTip('Maximize')
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(':/16x16/icons/16x16/cil-window-maximize.png'))
            self.ui.frame_top_btns.setStyleSheet('background-color: rgba(27, 29, 35, 200)')
            self.ui.frame_size_grip.show()

    def returStatus(self):
        return GLOBAL_STATE

    def setStatus(status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    def enableMaximumSize(self, width, height):
        if width != '':
            if height != '':
                self.setMaximumSize(QSize(width, height))
                self.ui.frame_size_grip.hide()
                self.ui.btn_maximize_restore.hide()

    def toggleMenu(self, maxWidth, enable):
        if enable:
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b'minimumWidth')
            self.animation.setDuration(1000)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def toggleMenu1(self, maxHeight, enable):
        if enable:
            width = self.ui.frame_4.height()
            maxExtend = maxHeight
            standard = 0
            if width == 0:
                widthExtended = maxExtend
            else:
                widthExtended = standard
            self.animation = QPropertyAnimation(self.ui.frame_4, b'maximumHeight'), QPropertyAnimation(self.ui.frame_4, b'minimumHeight')
            self.animation[0].setDuration(2000)
            self.animation[1].setDuration(2000)
            self.animation[0].setStartValue(width)
            self.animation[1].setStartValue(width)
            self.animation[0].setEndValue(widthExtended)
            self.animation[1].setEndValue(widthExtended)
            self.animation[0].setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation[1].setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation[0].start()
            self.animation[1].start()

    def removeTitleBar(status):
        global GLOBAL_TITLE_BAR
        GLOBAL_TITLE_BAR = status

    def labelTitle(self, text):
        self.ui.label_title_bar_top.setText(text)

    def labelDescription(self, text):
        self.ui.label_top_info_1.setText(text)

    def addNewMenu(self, name, objName, icon, isTopMenu):
        font = QFont()
        font.setFamily('Segoe UI')
        button = QPushButton(str(count), self)
        button.setObjectName(objName)
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
        button.setSizePolicy(sizePolicy3)
        button.setMinimumSize(QSize(0, 70))
        button.setLayoutDirection(Qt.LeftToRight)
        button.setFont(font)
        button.setStyleSheet(Style.style_bt_standard.replace('ICON_REPLACE', icon))
        button.setText(name)
        button.setToolTip(name)
        button.clicked.connect(self.Button)
        if isTopMenu:
            self.ui.layout_menus.addWidget(button)
        else:
            self.ui.layout_menu_bottom.addWidget(button)

    def selectMenu(getStyle):
        select = getStyle + 'QPushButton { border-right: 7px solid rgb(44, 49, 60); }'
        return select

    def deselectMenu(getStyle):
        deselect = getStyle.replace('QPushButton { border-right: 7px solid rgb(44, 49, 60); }', '')
        return deselect

    def selectStandardMenu(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

    def resetStyle(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))

    def labelPage(self, text):
        newText = '| ' + text.upper()
        self.ui.label_top_info_2.setText(newText)

    def userIcon(self, initialsTooltip, icon, showHide):
        if showHide:
            self.ui.label_user_icon.setText(initialsTooltip)
            if icon:
                style = self.ui.label_user_icon.styleSheet()
                setIcon = 'QLabel { background-image: ' + icon + '; }'
                self.ui.label_user_icon.setStyleSheet(style + setIcon)
                self.ui.label_user_icon.setText('')
                self.ui.label_user_icon.setToolTip(initialsTooltip)
        else:
            self.ui.label_user_icon.hide()

    def uiDefinitions(self):

        def dobleClickMaximizeRestore(event):
            if event.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(250, lambda : UIFunctions.maximize_restore(self))

        if GLOBAL_TITLE_BAR:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            self.ui.frame_label_top_btns.mouseDoubleClickEvent = dobleClickMaximizeRestore
        else:
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.frame_label_top_btns.setContentsMargins(8, 0, 0, 5)
            self.ui.frame_label_top_btns.setMinimumHeight(42)
            self.ui.frame_icon_top_bar.hide()
            self.ui.frame_btns_right.hide()
            self.ui.frame_size_grip.hide()
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.frame_main.setGraphicsEffect(self.shadow)
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet('width: 20px; height: 20px; margin 0px; padding: 0px;')
        self.ui.btn_minimize.clicked.connect(lambda : self.showMinimized())
        self.ui.btn_maximize_restore.clicked.connect(lambda : UIFunctions.maximize_restore(self))
        self.ui.btn_close.clicked.connect(lambda : self.close())