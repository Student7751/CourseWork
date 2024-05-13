# Importing based class
from DB import DB
# Importing PyQt5 widget
from PyQt5.QtWidgets import QTableWidgetItem, QCheckBox

class TableModel(DB):
    """Base class for all QTableWidget object in program. Include functions to fill, load, delete tables"""

    # Filling any table
    @staticmethod
    def fillTable(table_widget, table, a=0):
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
                cb = QCheckBox(table_widget)
                # Set checkbox object into row
                table_widget.setCellWidget(row_index, 0, cb)
            # Inserting data to each row
            for column_index in range(column_count - a):
                # Creating data item
                item = QTableWidgetItem(str(row_data[column_index]))
                # insert item to table
                table_widget.setItem(row_index, column_index + a, item)