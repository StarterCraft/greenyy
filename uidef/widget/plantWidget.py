# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'g:\Work\Code\grassyy\uisrc\widget\plantWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PlantWidget(object):
    def setupUi(self, PlantWidget):
        PlantWidget.setObjectName("PlantWidget")
        PlantWidget.resize(400, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PlantWidget.sizePolicy().hasHeightForWidth())
        PlantWidget.setSizePolicy(sizePolicy)
        PlantWidget.setMinimumSize(QtCore.QSize(400, 500))
        self.gridLayout = QtWidgets.QGridLayout(PlantWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(PlantWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(PlantWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(PlantWidget)
        self.groupBox_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setContentsMargins(7, 7, 7, 7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.liwPlantRules = QtWidgets.QListWidget(self.groupBox_2)
        self.liwPlantRules.setObjectName("liwPlantRules")
        self.verticalLayout.addWidget(self.liwPlantRules)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnPlantRuleAdd = QtWidgets.QPushButton(self.groupBox_2)
        self.btnPlantRuleAdd.setObjectName("btnPlantRuleAdd")
        self.horizontalLayout.addWidget(self.btnPlantRuleAdd)
        self.btnPlantRuleRmv = QtWidgets.QPushButton(self.groupBox_2)
        self.btnPlantRuleRmv.setObjectName("btnPlantRuleRmv")
        self.horizontalLayout.addWidget(self.btnPlantRuleRmv)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnWaterNow = QtWidgets.QPushButton(PlantWidget)
        self.btnWaterNow.setObjectName("btnWaterNow")
        self.horizontalLayout_2.addWidget(self.btnWaterNow)
        self.btnSettings = QtWidgets.QPushButton(PlantWidget)
        self.btnSettings.setObjectName("btnSettings")
        self.horizontalLayout_2.addWidget(self.btnSettings)
        self.btnTerminate = QtWidgets.QPushButton(PlantWidget)
        self.btnTerminate.setObjectName("btnTerminate")
        self.horizontalLayout_2.addWidget(self.btnTerminate)
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 0, 1, 2)
        self.lblNextWatering = QtWidgets.QLabel(PlantWidget)
        self.lblNextWatering.setObjectName("lblNextWatering")
        self.gridLayout.addWidget(self.lblNextWatering, 3, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(PlantWidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setContentsMargins(7, 7, 7, 7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblPlantDesc = QtWidgets.QLabel(self.groupBox)
        self.lblPlantDesc.setObjectName("lblPlantDesc")
        self.verticalLayout_2.addWidget(self.lblPlantDesc)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(PlantWidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setContentsMargins(7, 7, 7, 7)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gfwTemp = QtWidgets.QGraphicsView(self.groupBox_3)
        self.gfwTemp.setObjectName("gfwTemp")
        self.verticalLayout_3.addWidget(self.gfwTemp)
        self.gfwHumidity = QtWidgets.QGraphicsView(self.groupBox_3)
        self.gfwHumidity.setObjectName("gfwHumidity")
        self.verticalLayout_3.addWidget(self.gfwHumidity)
        self.gridLayout.addWidget(self.groupBox_3, 1, 0, 1, 2)
        self.lblLastWatering = QtWidgets.QLabel(PlantWidget)
        self.lblLastWatering.setObjectName("lblLastWatering")
        self.gridLayout.addWidget(self.lblLastWatering, 2, 1, 1, 1)

        self.retranslateUi(PlantWidget)
        QtCore.QMetaObject.connectSlotsByName(PlantWidget)

    def retranslateUi(self, PlantWidget):
        _translate = QtCore.QCoreApplication.translate
        PlantWidget.setWindowTitle(_translate("PlantWidget", "Грядка по умолчанию"))
        self.label_2.setText(_translate("PlantWidget", "Последний полив:"))
        self.label_4.setText(_translate("PlantWidget", "Следующий полив:"))
        self.groupBox_2.setTitle(_translate("PlantWidget", "Правила"))
        self.btnPlantRuleAdd.setText(_translate("PlantWidget", "Добавить..."))
        self.btnPlantRuleRmv.setText(_translate("PlantWidget", "Удалить"))
        self.btnWaterNow.setText(_translate("PlantWidget", "Полить сейчас"))
        self.btnSettings.setText(_translate("PlantWidget", "Настройки..."))
        self.btnTerminate.setText(_translate("PlantWidget", "Остановить"))
        self.lblNextWatering.setText(_translate("PlantWidget", "TextLabel"))
        self.groupBox.setTitle(_translate("PlantWidget", "Описание"))
        self.lblPlantDesc.setText(_translate("PlantWidget", "TextLabel"))
        self.groupBox_3.setTitle(_translate("PlantWidget", "Статистика"))
        self.lblLastWatering.setText(_translate("PlantWidget", "TextLabel"))
