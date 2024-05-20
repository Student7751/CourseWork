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
    def fillTable(table_widget, table, a=0, b=0):
        # b - is a ID of client and needs to determine what type of table we gets
        if b:
            data = DB.getNotariesNameByID(b)
        else:
            # Getting tuple with the data by table name
            data = DB.getUsers(table)
        # Getting row count and column count
        table_widget.setRowCount(len(data))
        column_count = table_widget.columnCount()
        # Filling the table
        for row_index, row_data in enumerate(data):
            # a - is a flag, need to determine type of table (0 - if table not support checkboxes, 1 - if table support)
            if a:
                # Creating checkbox to table
                cb = TableModel.createCheckboxForTable()
                # Set checkbox object into row
                table_widget.setCellWidget(row_index, 0, cb)
                
            # Inserting data to each row
            for column_index in range(column_count - a):
                # Creating data item
                item = QTableWidgetItem(str(row_data[column_index]))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                # insert item to table
                table_widget.setItem(row_index, column_index + a, item)

    # Getting data of the checked rows
    @staticmethod
    def getCheckedItems(table):
        # Creating list with the results
        data = list()

        for row in range(table.rowCount()):
            # Getting widget from the first column
            item = table.cellWidget(row, 0)
            # Getting checkbox from the widget
            cb = item.layout().itemAt(0).widget()
            if cb.isChecked():
                # Creating temp list with row data
                lst = list()
                # Starting iteration by columns (-1 and +1 needs to skip checkbox object)
                for column in range(table.columnCount() - 1):
                    # Appending data to the temp list
                    lst.append(table.item(row, column + 1).text())
                # Appending temp list to the result list
                data.append(lst)
        # Returning result list
        return data
