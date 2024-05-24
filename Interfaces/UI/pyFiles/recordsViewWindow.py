import sys

# Importing PyQt files
from PyQt5.QtWidgets import QApplication, QMessageBox
# Importing based class
from interfaces import MainWindow
# Importing linked classes
from mainTableModel import TableModel
from DB import DB


class RecordsViewWindow(MainWindow):
    def __init__(self):
        super().__init__(15)

        # Filling the table
        TableModel.fillTable(table_widget=self.ui.RecordsTable, table="UnconfirmedRecords")
        # Connecting signals to slots
        self.ui.RecordsTable.clicked.connect(self.getDescr)
        self.ui.applyBtn.clicked.connect(self.applyRecord)
        self.ui.backBtn.clicked.connect(self.toMainWindow)
        self.ui.denialBtn.clicked.connect(self.deleteRecord)
        # Checking buttons when any row was selected
        self.ui.RecordsTable.selectionModel().selectionChanged.connect(self.checkBtns)

    # Deletion record
    def deleteRecord(self):
        # Getting index of selected row
        selected_row = self.ui.RecordsTable.currentRow()
        # Getting record ID
        recordID = self.ui.RecordsTable.item(selected_row, 0).text()
        # Delete record from unconfirmed table
        DB.deleteUnconfRecord(recordID)
        # Update table
        TableModel.fillTable(table_widget=self.ui.RecordsTable, table="UnconfirmedRecords")
        # Clear description edit
        self.ui.recordDescr.clear()

    # Checking buttons and setting its enabled of disabled
    def checkBtns(self):
        # Getting selected row
        selected_rows = self.ui.RecordsTable.selectionModel().selectedRows()
        buttons_enabled = bool(selected_rows)
        # Setting buttons visible
        self.ui.applyBtn.setEnabled(buttons_enabled)
        self.ui.denialBtn.setEnabled(buttons_enabled)
        # Setting empty text in description
        self.ui.recordDescr.clear()

    # Opening main window for this window
    def toMainWindow(self):
        from AdminWindow import AdminWindow
        self.openWindow(AdminWindow())

    # Adding new record to table
    def applyRecord(self):
        # Getting index of selected row
        selected_row = self.ui.RecordsTable.currentRow()
        # Getting type and ID of record
        recType = self.ui.RecordsTable.item(selected_row, 3).text()
        recID = self.ui.RecordsTable.item(selected_row, 2).text()

        # Do something depending on the type of record
        if recType == "Добавление услуги":
            # Getting data
            name, description, price = self.ui.recordDescr.toPlainText().split(";")
            # Adding new record with data
            DB.addOffer(name=name, descr=description, price=price)

            QMessageBox.information(self, "Уведомление", "Заявка успешно добавлена!")
        elif recType == "Удаление услуги":
            # Delete offer from table
            DB.deleteUser(userID=recID, table="OFFERS")

            QMessageBox.information(self, "Уведомление", "Услуга успешно удалена!")

        # Deletion record from table
        self.deleteRecord()

    # Getting description of the selected row
    def getDescr(self):
        # Getting selected row
        selected_row = self.ui.RecordsTable.currentRow()
        # Getting description
        descr = DB.getUnconfRecordDescr(recordID=self.ui.RecordsTable.item(selected_row, 0).text())
        # Setting description to widget
        self.ui.recordDescr.setText(*descr)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RecordsViewWindow()
    window.show()
    sys.exit(app.exec_())
