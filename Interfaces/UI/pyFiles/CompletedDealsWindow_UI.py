# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Kursach\Interfaces\UI\ClientWindows\CompletedDealsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CompletedDealsWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 564)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 821, 601))
        self.label.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.0201244, y1:0.96, x2:1, y2:0, stop:0.0746269 rgba(74, 74, 74, 255), stop:0.950249 rgba(197, 197, 197, 255));")
        self.label.setText("")
        self.label.setObjectName("label")
        self.NotariesTable = QtWidgets.QTableWidget(self.centralwidget)
        self.NotariesTable.setGeometry(QtCore.QRect(30, 60, 751, 411))
        self.NotariesTable.setStyleSheet("background-color: rgb(161, 161, 161);")
        self.NotariesTable.setObjectName("NotariesTable")
        self.NotariesTable.setColumnCount(4)
        self.NotariesTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(32, 34, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.NotariesTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(32, 34, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.NotariesTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(32, 34, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.NotariesTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(32, 34, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.NotariesTable.setHorizontalHeaderItem(3, item)
        self.NotariesTable.horizontalHeader().setStretchLastSection(True)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 20, 261, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(32, 34, 156);")
        self.label_2.setObjectName("label_2")
        self.BackBtn = QtWidgets.QPushButton(self.centralwidget)
        self.BackBtn.setGeometry(QtCore.QRect(640, 490, 141, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.BackBtn.setFont(font)
        self.BackBtn.setStyleSheet("border-color: rgb(255, 249, 62);\n"
"border-radius: 20px;\n"
"background-color: rgb(255, 192, 66);\n"
"border: 1px solid #000000")
        self.BackBtn.setObjectName("BackBtn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.NotariesTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.NotariesTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Notary"))
        item = self.NotariesTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Name"))
        item = self.NotariesTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Price"))
        self.label_2.setText(_translate("MainWindow", "Данные о совершённых сделках"))
        self.BackBtn.setText(_translate("MainWindow", "НАЗАД"))
