# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Kursach\Interfaces\UI\NotaryWindows\DealsViewWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DealViewWindow(object):
    def setupUi(self, DealViewWindow):
        DealViewWindow.setObjectName("DealViewWindow")
        DealViewWindow.resize(800, 603)
        self.centralwidget = QtWidgets.QWidget(DealViewWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 611))
        self.label.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.0201244, y1:0.96, x2:1, y2:0, stop:0.0746269 rgba(74, 74, 74, 255), stop:0.950249 rgba(197, 197, 197, 255));")
        self.label.setText("")
        self.label.setObjectName("label")
        self.dealsTable = QtWidgets.QTableWidget(self.centralwidget)
        self.dealsTable.setGeometry(QtCore.QRect(30, 110, 751, 411))
        self.dealsTable.setStyleSheet("background-color: rgb(161, 161, 161);")
        self.dealsTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.dealsTable.setProperty("showDropIndicator", False)
        self.dealsTable.setDragDropOverwriteMode(False)
        self.dealsTable.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.dealsTable.setObjectName("dealsTable")
        self.dealsTable.setColumnCount(5)
        self.dealsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(32, 34, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.dealsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(32, 34, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.dealsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(32, 34, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.dealsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(32, 34, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.dealsTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(32, 34, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.dealsTable.setHorizontalHeaderItem(4, item)
        self.dealsTable.horizontalHeader().setStretchLastSection(True)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 20, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(32, 34, 156);")
        self.label_2.setObjectName("label_2")
        self.BackBtn = QtWidgets.QPushButton(self.centralwidget)
        self.BackBtn.setGeometry(QtCore.QRect(640, 540, 141, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.BackBtn.setFont(font)
        self.BackBtn.setStyleSheet("border-color: rgb(255, 249, 62);\n"
"border-radius: 20px;\n"
"background-color: rgb(255, 192, 66);\n"
"border: 1px solid #000000")
        self.BackBtn.setObjectName("BackBtn")
        self.updateBtn = QtWidgets.QPushButton(self.centralwidget)
        self.updateBtn.setGeometry(QtCore.QRect(250, 540, 171, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.updateBtn.setFont(font)
        self.updateBtn.setStyleSheet("border-color: rgb(255, 249, 62);\n"
"border-radius: 20px;\n"
"background-color: rgb(255, 192, 66);\n"
"border: 1px solid #000000")
        self.updateBtn.setObjectName("updateBtn")
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(40, 540, 181, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.addBtn.setFont(font)
        self.addBtn.setStyleSheet("border-color: rgb(255, 249, 62);\n"
"border-radius: 20px;\n"
"background-color: rgb(255, 192, 66);\n"
"border: 1px solid #000000")
        self.addBtn.setObjectName("addBtn")
        self.searchEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.searchEdit.setGeometry(QtCore.QRect(80, 60, 701, 31))
        self.searchEdit.setStyleSheet("border-radius: 10px\n"
"")
        self.searchEdit.setObjectName("searchEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 60, 31, 31))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/icons/search_200941.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        DealViewWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(DealViewWindow)
        QtCore.QMetaObject.connectSlotsByName(DealViewWindow)

    def retranslateUi(self, DealViewWindow):
        _translate = QtCore.QCoreApplication.translate
        DealViewWindow.setWindowTitle(_translate("DealViewWindow", "MainWindow"))
        item = self.dealsTable.horizontalHeaderItem(0)
        item.setText(_translate("DealViewWindow", "to_Delete"))
        item = self.dealsTable.horizontalHeaderItem(1)
        item.setText(_translate("DealViewWindow", "ID"))
        item = self.dealsTable.horizontalHeaderItem(2)
        item.setText(_translate("DealViewWindow", "Name"))
        item = self.dealsTable.horizontalHeaderItem(3)
        item.setText(_translate("DealViewWindow", "Description"))
        item = self.dealsTable.horizontalHeaderItem(4)
        item.setText(_translate("DealViewWindow", "Price"))
        self.label_2.setText(_translate("DealViewWindow", "Данные об услугах"))
        self.BackBtn.setText(_translate("DealViewWindow", "НАЗАД"))
        self.updateBtn.setText(_translate("DealViewWindow", "ОБНОВИТЬ ТАБЛИЦУ"))
        self.addBtn.setText(_translate("DealViewWindow", "ДОБАВИТЬ ЭЛЕМЕНТ"))

