# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Kursach\Interfaces\UI\ClientWindows\CompletedDealsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CompletedDealsWindow(object):
    def setupUi(self, CompletedDealsWindow):
        CompletedDealsWindow.setObjectName("CompletedDealsWindow")
        CompletedDealsWindow.resize(802, 596)
        self.centralwidget = QtWidgets.QWidget(CompletedDealsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 821, 601))
        self.label.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.0201244, y1:0.96, x2:1, y2:0, stop:0.0746269 rgba(74, 74, 74, 255), stop:0.950249 rgba(197, 197, 197, 255));")
        self.label.setText("")
        self.label.setObjectName("label")
        self.DealsTable = QtWidgets.QTableWidget(self.centralwidget)
        self.DealsTable.setGeometry(QtCore.QRect(30, 100, 751, 411))
        self.DealsTable.setStyleSheet("background-color: rgb(161, 161, 161);")
        self.DealsTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.DealsTable.setTabKeyNavigation(False)
        self.DealsTable.setProperty("showDropIndicator", False)
        self.DealsTable.setDragDropOverwriteMode(False)
        self.DealsTable.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.DealsTable.setObjectName("DealsTable")
        self.DealsTable.setColumnCount(6)
        self.DealsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(32, 34, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.DealsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(32, 34, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.DealsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(32, 34, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.DealsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(32, 34, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.DealsTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(32, 34, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.DealsTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(32, 34, 156))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.DealsTable.setHorizontalHeaderItem(5, item)
        self.DealsTable.horizontalHeader().setStretchLastSection(True)
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
        self.BackBtn.setGeometry(QtCore.QRect(640, 530, 141, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.BackBtn.setFont(font)
        self.BackBtn.setStyleSheet("border-color: rgb(255, 249, 62);\n"
"border-radius: 20px;\n"
"background-color: rgb(255, 192, 66);\n"
"border: 1px solid #000000")
        self.BackBtn.setObjectName("BackBtn")
        self.searchEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.searchEdit.setGeometry(QtCore.QRect(80, 60, 691, 31))
        self.searchEdit.setStyleSheet("border-radius:10px")
        self.searchEdit.setObjectName("searchEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 60, 31, 31))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/icons/search_200941.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        CompletedDealsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CompletedDealsWindow)
        QtCore.QMetaObject.connectSlotsByName(CompletedDealsWindow)

    def retranslateUi(self, CompletedDealsWindow):
        _translate = QtCore.QCoreApplication.translate
        CompletedDealsWindow.setWindowTitle(_translate("CompletedDealsWindow", "MainWindow"))
        item = self.DealsTable.horizontalHeaderItem(0)
        item.setText(_translate("CompletedDealsWindow", "ID"))
        item = self.DealsTable.horizontalHeaderItem(1)
        item.setText(_translate("CompletedDealsWindow", "Deal_Name"))
        item = self.DealsTable.horizontalHeaderItem(2)
        item.setText(_translate("CompletedDealsWindow", "Discount"))
        item = self.DealsTable.horizontalHeaderItem(3)
        item.setText(_translate("CompletedDealsWindow", "Notary"))
        item = self.DealsTable.horizontalHeaderItem(4)
        item.setText(_translate("CompletedDealsWindow", "Price"))
        item = self.DealsTable.horizontalHeaderItem(5)
        item.setText(_translate("CompletedDealsWindow", "Date"))
        self.label_2.setText(_translate("CompletedDealsWindow", "Данные о совершённых сделках"))
        self.BackBtn.setText(_translate("CompletedDealsWindow", "НАЗАД"))
