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
        # Connecting buttons for its slots
        self.ui.updateBtn.clicked.connect(self.updateTable)
        self.ui.backBtn.clicked.connect(self.toMainWindow)
        self.ui.addBtn.clicked.connect(lambda: self.openWindow(NotaryAddWindow()))

    # Updating table
    def updateTable(self):
        # Getting checked rows data
        res = TableModel.getCheckedItems(self.ui.NotariesTable)
        # If any checked row exists
        if res:
            # Starting iteration by data list
            for i in res:
                # Deleting user by ID
                DB.deleteUser(i[0], "notaries")
                # Updating table
                TableModel.fillTable(self.ui.NotariesTable, "notaries", 1)
            # Returning value to exit the function
            return 0
        # Creating message if nothing has been checked
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
