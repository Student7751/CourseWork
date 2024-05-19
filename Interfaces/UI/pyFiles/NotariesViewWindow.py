import sys

# Importing PyQt files
from PyQt5.QtWidgets import QApplication, QMessageBox

# Importing based classes
from interfaces import MainWindow
from mainTableModel import TableModel
from DB import DB

# Importing linked class
from NotaryAddWindow import NotaryAddWindow
class NotariesViewWindow(MainWindow):
    def __init__(self, parent=None):
        super().__init__(2)

        # Filling the table by the opening window
        TableModel.fillTable(self.ui.NotariesTable, "notaries", 1)
        # Connecting buttons for its functions
        self.ui.updateBtn.clicked.connect(self.updateTable)
        self.ui.backBtn.clicked.connect(self.toMainWindow)
        self.ui.addBtn.clicked.connect(lambda: self.openWindow(NotaryAddWindow()))

    # Updating table
    def updateTable(self):
        # Flag needs to determine when any checkbox is activated
        isAnyChecked = False
        # Going to each row on the table
        for row in range(self.ui.NotariesTable.rowCount()):
            # Getting widget from the first column
            item = self.ui.NotariesTable.cellWidget(row, 0)
            # Getting checkbox from the widget
            cb = item.layout().itemAt(0).widget()

            if cb.isChecked():
                # Determine checkbox changes
                isAnyChecked = True
                # Getting ID from row needs to delete
                data = self.ui.NotariesTable.item(row, 1)
                # Deleting record from the Database
                DB.deleteUser(data.text(), "notaries")
        # Update table if any checkbox checked
        if isAnyChecked:
            TableModel.fillTable(self.ui.NotariesTable, "notaries", 1)
            return 0

        QMessageBox.information(self, "Уведомление", "Нечего обновлять")

    # Opening main window for this window
    def toMainWindow(self):
        from AdminWindow import AdminWindow
        self.openWindow(AdminWindow("name"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NotariesViewWindow()
    window.show()
    sys.exit(app.exec_())
