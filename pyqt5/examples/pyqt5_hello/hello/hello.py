# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\hello.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_hello(object):
    def setupUi(self, hello):
        hello.setObjectName("hello")
        hello.resize(285, 116)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\hello.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        hello.setWindowIcon(icon)
        self.date_time_lb = QtWidgets.QLabel(hello)
        self.date_time_lb.setGeometry(QtCore.QRect(20, 70, 251, 31))
        font = QtGui.QFont()
        font.setFamily("D2Coding")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.date_time_lb.setFont(font)
        self.date_time_lb.setText("")
        self.date_time_lb.setObjectName("date_time_lb")
        self.date_time_date_time_label_2 = QtWidgets.QLabel(hello)
        self.date_time_date_time_label_2.setGeometry(QtCore.QRect(10, 10, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.date_time_date_time_label_2.setFont(font)
        self.date_time_date_time_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.date_time_date_time_label_2.setObjectName("date_time_date_time_label_2")

        self.retranslateUi(hello)
        QtCore.QMetaObject.connectSlotsByName(hello)

    def retranslateUi(self, hello):
        _translate = QtCore.QCoreApplication.translate
        hello.setWindowTitle(_translate("hello", "Hello"))
        self.date_time_date_time_label_2.setText(_translate("hello", "Hello!"))

