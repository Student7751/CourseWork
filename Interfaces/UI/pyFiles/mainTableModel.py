# Importing based class
from DB import DB
# Importing PyQt5 widget
from PyQt5.QtWidgets import QTableWidgetItem

class TableModel(DB):
    """Base class for all QTableWidget object in program. Include functions to fill, load, delete tables"""

    # Filling any table
    @staticmethod
    def fillTable(table_widget, table):
        # Getting tuple with the data by table name
        data = DB.getUsers(table)
        # Getting row count and column count
        table_widget.setRowCount(len(data))
        column_count = table_widget.columnCount()
        # Filling the table
        for row_index, row_data in enumerate(data):
            for column_index in range(column_count):
                item = QTableWidgetItem(str(row_data[column_index]))
                table_widget.setItem(row_index, column_index, item)