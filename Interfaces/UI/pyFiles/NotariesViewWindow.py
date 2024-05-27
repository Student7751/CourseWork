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
        TableModel.fillTable(table_widget=self.ui.NotariesTable, withCheckboxes=True, table="notaries")
        # Connecting buttons for its slots
        self.ui.updateBtn.clicked.connect(self.updateTable)
        self.ui.backBtn.clicked.connect(self.toMainWindow)
        self.ui.addBtn.clicked.connect(lambda: self.openWindow(NotaryAddWindow()))

        self.ui.searchEdit.textChanged.connect(self.searchData)

    def searchData(self, text):
        TableModel.search(table=self.ui.NotariesTable, text=text)

    # Updating table by user TableModel function
    def updateTable(self):
        if not TableModel.updateTable(table=self.ui.NotariesTable, tableName="notaries", isAdmin=True):
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
