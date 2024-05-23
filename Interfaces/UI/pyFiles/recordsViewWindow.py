import sys

# Importing PyQt files
from PyQt5.QtWidgets import QApplication
# Importing based class
from interfaces import MainWindow
# Importing linked classes
from mainTableModel import TableModel
from DB import DB


class RecordsViewWindow(MainWindow):
    def __init__(self):
        super().__init__(15)

        # Filling the table
        TableModel.fillTable(self.ui.RecordsTable, "UnconfirmedRecords")
        # Connecting signals to slots
        self.ui.RecordsTable.clicked.connect(self.getDescr)
        self.ui.applyBtn.clicked.connect(self.applyRecord)
        self.ui.backBtn.clicked.connect(self.toMainWindow)

    # Opening main window for this window
    def toMainWindow(self):
        from AdminWindow import AdminWindow
        self.openWindow(AdminWindow())

    # Adding new record to table
    def applyRecord(self):
        # Getting data
        name, description, price = self.ui.recordDescr.toPlainText().split(";")
        # Adding new record with data
        DB.addOffer(name, description, price)

    # Getting description of the selected row
    def getDescr(self):
        # Setting enabled buttons
        self.ui.applyBtn.setEnabled(True)
        # Getting selected row
        selected_row = self.ui.RecordsTable.currentRow()
        # Getting description
        descr = DB.getUnconfRecordDescr(self.ui.RecordsTable.item(selected_row, 0).text())
        # Setting description to widget
        self.ui.recordDescr.setText(*descr)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RecordsViewWindow()
    window.show()
    sys.exit(app.exec_())
