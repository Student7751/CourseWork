# Importing based class
from DB import DB
# Importing PyQt5 widget
from PyQt5.QtWidgets import QTableWidgetItem, QCheckBox, QHBoxLayout, QWidget
from PyQt5 import QtCore

class TableModel(DB):
    """Base class for all QTableWidget object in program. Include functions to fill, load, delete tables"""

    # Creating checkbox with align on center
    @staticmethod
    def createCheckboxForTable():
        # Creating widget
        Widget = QWidget()
        # Creating standard checkbox
        CheckBox = QCheckBox()
        # Creating the layout
        Layout = QHBoxLayout(Widget)
        # Adding our checkbox and align it
        Layout.addWidget(CheckBox)
        Layout.setAlignment(QtCore.Qt.AlignCenter)
        Layout.setContentsMargins(0, 0, 0, 0)
        Widget.setLayout(Layout)
        # Returning widget
        return Widget

    # Filling any table
    @staticmethod
    def fillTable(table_widget, table, withCheckboxes=False, clientID=0):
        # Getting data determine by type of client
        data = DB.getNotariesNameByID(clientID) if clientID else DB.getUsers(table)
        # Getting row count and column count
        table_widget.setRowCount(len(data))
        column_count = table_widget.columnCount()
        # Filling the table
        for row_index, row_data in enumerate(data):
            # withCheckboxes - is a flag, need to determine type of table (0 - if table not support checkboxes, 1 - if table support)
            if withCheckboxes:
                # Creating checkbox to table
                cb = TableModel.createCheckboxForTable()
                # Set checkbox object into row
                table_widget.setCellWidget(row_index, 0, cb)
                
            # Inserting data to each row
            for column_index in range(column_count - int(withCheckboxes)):
                # Creating data item
                item = QTableWidgetItem(str(row_data[column_index]))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                # insert item to table
                table_widget.setItem(row_index, column_index + int(withCheckboxes), item)

    # Getting data of the checked rows
    @staticmethod
    def getCheckedItems(table):
        # Creating list with the results
        checkedItems = list()

        for row in range(table.rowCount()):
            # Getting widget from the first column
            item = table.cellWidget(row, 0)
            # Getting checkbox from the widget
            cb = item.layout().itemAt(0).widget()
            if cb.isChecked():
                # Creating temp list with row data
                row_data = [table.item(row, col).text() for col in range(1, table.columnCount())]
                checkedItems.append(row_data)
        # Returning result list
        return checkedItems

    @staticmethod
    # Deletion record from table
    def updateTable(table, tableName, userID=0, isAdmin=False):
        # Getting checked rows data
        res = TableModel.getCheckedItems(table)
        # If any checked row exists
        if res:
            # Starting iteration by data list
            for i in res:
                if isAdmin:
                    # Deleting user by ID
                    DB.deleteUser(i[0], tableName)
                else:
                    # Inserting record to unconfirmed table
                    DB.addUnconfRecord(userID, i[0], "Удаление услуги", ";".join(i))
            TableModel.fillTable(table, tableName, withCheckboxes=True)
            # Returning value to exit the function
            return True
        return False
