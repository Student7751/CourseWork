# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Kursach\Interfaces\UI\AuthWindows\Auth.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AuthWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(872, 631)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(False)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 871, 631))
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-6, -5, 461, 641))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/woman.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.AuthBtn = QtWidgets.QPushButton(self.centralwidget)
        self.AuthBtn.setGeometry(QtCore.QRect(570, 400, 221, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.AuthBtn.setFont(font)
        self.AuthBtn.setStyleSheet("border-color: rgb(255, 249, 62);\n"
"border-radius: 20px;\n"
"background-color: rgb(255, 192, 66);\n"
"border: 1px solid #000000")
        self.AuthBtn.setObjectName("AuthBtn")
        self.RegistrBtn = QtWidgets.QPushButton(self.centralwidget)
        self.RegistrBtn.setGeometry(QtCore.QRect(540, 460, 281, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.RegistrBtn.setFont(font)
        self.RegistrBtn.setStyleSheet("border-color: rgb(255, 249, 62);\n"
"border-radius: 20px;\n"
"background-color: rgb(255, 192, 66);\n"
"border: 1px solid #000000")
        self.RegistrBtn.setObjectName("RegistrBtn")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(540, 330, 291, 31))
        self.lineEdit_2.setStyleSheet("border-radius: 10px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(540, 270, 291, 31))
        self.lineEdit_3.setStyleSheet("border-radius: 10px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(580, 180, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(113, 58, 13);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(490, 40, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(113, 58, 13);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(490, 90, 391, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(500, 270, 31, 31))
        self.label_6.setStyleSheet("")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/icons/user-orange_25327.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(500, 330, 31, 31))
        self.label_7.setStyleSheet("")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/icons/cslogin_104358.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.AuthBtn.setText(_translate("MainWindow", "ВОЙТИ"))
        self.RegistrBtn.setText(_translate("MainWindow", "РЕГИСТРАЦИЯ"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Введите пароль"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Введите логин"))
        self.label_3.setText(_translate("MainWindow", "АВТОРИЗАЦИЯ"))
        self.label_4.setText(_translate("MainWindow", "Добро пожаловать!"))
        self.label_5.setText(_translate("MainWindow", "Войдите в свою учетную запись или зарегистрируйтесь"))
import UI.Icons.icons