# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'label.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 847)
        font = QtGui.QFont()
        font.setPointSize(20)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_image = QtWidgets.QLabel(self.centralwidget)
        self.main_image.setGeometry(QtCore.QRect(0, 0, 1024, 1024))
        self.main_image.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.main_image.setText("")
        self.main_image.setObjectName("main_image")
        self.message_box = QtWidgets.QLabel(self.centralwidget)
        self.message_box.setGeometry(QtCore.QRect(40, 2050, 1851, 80))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.message_box.setFont(font)
        self.message_box.setObjectName("message_box")
        self.image_rgb_front = QtWidgets.QLabel(self.centralwidget)
        self.image_rgb_front.setGeometry(QtCore.QRect(4920, 1160, 640, 360))
        self.image_rgb_front.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.image_rgb_front.setText("")
        self.image_rgb_front.setObjectName("image_rgb_front")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1040, 70, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1040, 200, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(1110, 120, 311, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.map_back = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.map_back.setFont(font)
        self.map_back.setObjectName("map_back")
        self.horizontalLayout.addWidget(self.map_back)
        self.map_next = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.map_next.setFont(font)
        self.map_next.setObjectName("map_next")
        self.horizontalLayout.addWidget(self.map_next)
        self.map_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.map_comboBox.setGeometry(QtCore.QRect(1140, 70, 281, 26))
        self.map_comboBox.setObjectName("map_comboBox")
        self.index_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.index_comboBox.setGeometry(QtCore.QRect(1144, 200, 271, 41))
        self.index_comboBox.setObjectName("index_comboBox")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(1110, 250, 311, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.index_back = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.index_back.setFont(font)
        self.index_back.setObjectName("index_back")
        self.horizontalLayout_2.addWidget(self.index_back)
        self.index_next = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.index_next.setFont(font)
        self.index_next.setObjectName("index_next")
        self.horizontalLayout_2.addWidget(self.index_next)
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(1110, 390, 311, 45))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.save_button.setFont(font)
        self.save_button.setObjectName("save_button")
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(1110, 470, 311, 45))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.clear_button.setFont(font)
        self.clear_button.setObjectName("clear_button")
        self.show_result_button = QtWidgets.QPushButton(self.centralwidget)
        self.show_result_button.setGeometry(QtCore.QRect(1110, 540, 311, 45))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.show_result_button.setFont(font)
        self.show_result_button.setObjectName("show_result_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.message_box.setText(_translate("MainWindow", "Please click point on image"))
        self.label.setText(_translate("MainWindow", "Map :"))
        self.label_2.setText(_translate("MainWindow", "Index :"))
        self.map_back.setText(_translate("MainWindow", "BACK"))
        self.map_next.setText(_translate("MainWindow", "NEXT"))
        self.index_back.setText(_translate("MainWindow", "BACK"))
        self.index_next.setText(_translate("MainWindow", "NEXT"))
        self.save_button.setText(_translate("MainWindow", "Save Points"))
        self.clear_button.setText(_translate("MainWindow", "Clear Points"))
        self.show_result_button.setText(_translate("MainWindow", "Show Results"))
