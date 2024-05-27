# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Kursach\Interfaces\UI\NotaryWindows\NotaryClientViewWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NotaryClientViewWindow(object):
    def setupUi(self, NotaryClientViewWindow):
        NotaryClientViewWindow.setObjectName("NotaryClientViewWindow")
        NotaryClientViewWindow.resize(873, 595)
        self.centralwidget = QtWidgets.QWidget(NotaryClientViewWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-6, -5, 881, 601))
        self.label.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.0201244, y1:0.96, x2:1, y2:0, stop:0.0746269 rgba(74, 74, 74, 255), stop:0.950249 rgba(197, 197, 197, 255));")
        self.label.setText("")
        self.label.setObjectName("label")
        self.clientsTable = QtWidgets.QTableWidget(self.centralwidget)
        self.clientsTable.setGeometry(QtCore.QRect(50, 100, 781, 411))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.clientsTable.setFont(font)
        self.clientsTable.setStyleSheet("background-color: rgb(182, 182, 182);")
        self.clientsTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.clientsTable.setTabKeyNavigation(False)
        self.clientsTable.setProperty("showDropIndicator", False)
        self.clientsTable.setDragDropOverwriteMode(False)
        self.clientsTable.setAlternatingRowColors(False)
        self.clientsTable.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.clientsTable.setShowGrid(True)
        self.clientsTable.setGridStyle(QtCore.Qt.SolidLine)
        self.clientsTable.setWordWrap(False)
        self.clientsTable.setCornerButtonEnabled(False)
        self.clientsTable.setObjectName("clientsTable")
        self.clientsTable.setColumnCount(5)
        self.clientsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(32, 34, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.clientsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(32, 34, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.clientsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(32, 34, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.clientsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(32, 34, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.clientsTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(32, 34, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.clientsTable.setHorizontalHeaderItem(4, item)
        self.clientsTable.horizontalHeader().setVisible(True)
        self.clientsTable.horizontalHeader().setSortIndicatorShown(False)
        self.clientsTable.horizontalHeader().setStretchLastSection(True)
        self.clientsTable.verticalHeader().setCascadingSectionResizes(False)
        self.clientsTable.verticalHeader().setStretchLastSection(False)
        self.backBtn = QtWidgets.QPushButton(self.centralwidget)
        self.backBtn.setGeometry(QtCore.QRect(670, 530, 161, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.backBtn.setFont(font)
        self.backBtn.setStyleSheet("border-color: rgb(255, 249, 62);\n"
"border-radius: 20px;\n"
"background-color: rgb(255, 192, 66);\n"
"border: 1px solid #000000")
        self.backBtn.setObjectName("backBtn")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(32, 34, 156);")
        self.label_2.setObjectName("label_2")
        self.onlyNotaryBox = QtWidgets.QCheckBox(self.centralwidget)
        self.onlyNotaryBox.setGeometry(QtCore.QRect(50, 530, 271, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.onlyNotaryBox.setFont(font)
        self.onlyNotaryBox.setStyleSheet("")
        self.onlyNotaryBox.setObjectName("onlyNotaryBox")
        self.searchEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.searchEdit.setGeometry(QtCore.QRect(50, 60, 681, 31))
        self.searchEdit.setStyleSheet("border-radius: 10px;")
        self.searchEdit.setObjectName("searchEdit")
        self.searchBtn = QtWidgets.QPushButton(self.centralwidget)
        self.searchBtn.setGeometry(QtCore.QRect(740, 60, 91, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.searchBtn.setFont(font)
        self.searchBtn.setStyleSheet("border-color: rgb(255, 249, 62);\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 192, 66);\n"
"border: 1px solid #000000")
        self.searchBtn.setObjectName("searchBtn")
        NotaryClientViewWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(NotaryClientViewWindow)
        QtCore.QMetaObject.connectSlotsByName(NotaryClientViewWindow)

    def retranslateUi(self, NotaryClientViewWindow):
        _translate = QtCore.QCoreApplication.translate
        NotaryClientViewWindow.setWindowTitle(_translate("NotaryClientViewWindow", "MainWindow"))
        self.clientsTable.setSortingEnabled(False)
        item = self.clientsTable.horizontalHeaderItem(0)
        item.setText(_translate("NotaryClientViewWindow", "ID"))
        item = self.clientsTable.horizontalHeaderItem(1)
        item.setText(_translate("NotaryClientViewWindow", "Name"))
        item = self.clientsTable.horizontalHeaderItem(2)
        item.setText(_translate("NotaryClientViewWindow", "Surname"))
        item = self.clientsTable.horizontalHeaderItem(3)
        item.setText(_translate("NotaryClientViewWindow", "Patronymic"))
        item = self.clientsTable.horizontalHeaderItem(4)
        item.setText(_translate("NotaryClientViewWindow", "Phone_Number"))
        self.backBtn.setText(_translate("NotaryClientViewWindow", "НАЗАД"))
        self.label_2.setText(_translate("NotaryClientViewWindow", "Данные о клиентах"))
        self.onlyNotaryBox.setText(_translate("NotaryClientViewWindow", "Показывать только моих клиентов"))
        self.searchBtn.setText(_translate("NotaryClientViewWindow", "ПОИСК"))
