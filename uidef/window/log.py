# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uisrc\LogWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Log(object):
    def setupUi(self, LogWindow):
        LogWindow.setObjectName("LogWindow")
        LogWindow.resize(600, 400)
        LogWindow.setMinimumSize(QtCore.QSize(600, 400))
        self.centralwidget = QtWidgets.QWidget(LogWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 7, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.txtLogDisplay = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        self.txtLogDisplay.setFont(font)
        self.txtLogDisplay.setReadOnly(True)
        self.txtLogDisplay.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.txtLogDisplay.setObjectName("txtLogDisplay")
        self.verticalLayout.addWidget(self.txtLogDisplay)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, -1, 11, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cbbPort = QtWidgets.QComboBox(self.centralwidget)
        self.cbbPort.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        self.cbbPort.setFont(font)
        self.cbbPort.setObjectName("cbbPort")
        self.cbbPort.addItem("")
        self.horizontalLayout.addWidget(self.cbbPort)
        self.lneMessage = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        self.lneMessage.setFont(font)
        self.lneMessage.setObjectName("lneMessage")
        self.horizontalLayout.addWidget(self.lneMessage)
        self.btnSend = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSend.sizePolicy().hasHeightForWidth())
        self.btnSend.setSizePolicy(sizePolicy)
        self.btnSend.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        self.btnSend.setFont(font)
        self.btnSend.setObjectName("btnSend")
        self.horizontalLayout.addWidget(self.btnSend)
        self.verticalLayout.addLayout(self.horizontalLayout)
        LogWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LogWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setToolTipsVisible(True)
        self.menu_2.setObjectName("menu_2")
        self.meiOpenLog = QtWidgets.QMenu(self.menubar)
        self.meiOpenLog.setObjectName("meiOpenLog")
        LogWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LogWindow)
        self.statusbar.setObjectName("statusbar")
        LogWindow.setStatusBar(self.statusbar)
        self.macLogLvl_DEBUG = QtWidgets.QAction(LogWindow)
        self.macLogLvl_DEBUG.setObjectName("macLogLvl_DEBUG")
        self.macLogLvl_INFO = QtWidgets.QAction(LogWindow)
        self.macLogLvl_INFO.setObjectName("macLogLvl_INFO")
        self.macLogLvl_WARNING = QtWidgets.QAction(LogWindow)
        self.macLogLvl_WARNING.setObjectName("macLogLvl_WARNING")
        self.macLogLvl_ERROR = QtWidgets.QAction(LogWindow)
        self.macLogLvl_ERROR.setObjectName("macLogLvl_ERROR")
        self.macLogLvl_CRITICAL = QtWidgets.QAction(LogWindow)
        self.macLogLvl_CRITICAL.setObjectName("macLogLvl_CRITICAL")
        self.menu_2.addAction(self.macLogLvl_DEBUG)
        self.menu_2.addAction(self.macLogLvl_INFO)
        self.menu_2.addAction(self.macLogLvl_WARNING)
        self.menu_2.addAction(self.macLogLvl_ERROR)
        self.menu_2.addAction(self.macLogLvl_CRITICAL)
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.meiOpenLog.menuAction())

        self.retranslateUi(LogWindow)
        self.lneMessage.returnPressed.connect(self.btnSend.click)
        QtCore.QMetaObject.connectSlotsByName(LogWindow)
        LogWindow.setTabOrder(self.cbbPort, self.lneMessage)
        LogWindow.setTabOrder(self.lneMessage, self.txtLogDisplay)

    def retranslateUi(self, LogWindow):
        _translate = QtCore.QCoreApplication.translate
        LogWindow.setWindowTitle(_translate("LogWindow", "Журнал и последовательный порт"))
        self.cbbPort.setItemText(0, _translate("LogWindow", "COM1"))
        self.lneMessage.setPlaceholderText(_translate("LogWindow", "Отправить сообщение на COM-порт..."))
        self.btnSend.setText(_translate("LogWindow", "=>"))
        self.menu_2.setTitle(_translate("LogWindow", "Уровень журнала"))
        self.meiOpenLog.setTitle(_translate("LogWindow", "Открыть файл"))
        self.macLogLvl_DEBUG.setText(_translate("LogWindow", "Отладка (DEBUG)"))
        self.macLogLvl_DEBUG.setToolTip(_translate("LogWindow", "Уровень журналирования: Отладка (DEBUG)"))
        self.macLogLvl_INFO.setText(_translate("LogWindow", "Информирование (INFO)"))
        self.macLogLvl_INFO.setToolTip(_translate("LogWindow", "Уровень журналирования: Информирование (INFO)"))
        self.macLogLvl_WARNING.setText(_translate("LogWindow", "Предупреждение (WARNING)"))
        self.macLogLvl_WARNING.setToolTip(_translate("LogWindow", "Уровень журналирования: Предупреждение (WARNING)"))
        self.macLogLvl_ERROR.setText(_translate("LogWindow", "Ошибки (ERROR)"))
        self.macLogLvl_ERROR.setToolTip(_translate("LogWindow", "Уровень журналирования: Ошибки (ERROR)"))
        self.macLogLvl_CRITICAL.setText(_translate("LogWindow", "Критические ошибки (CRITICAL)"))
        self.macLogLvl_CRITICAL.setToolTip(_translate("LogWindow", "Уровень журналирования: Критические ошибки (CRITICAL)"))