import sys

# Importing PyQt files
from PyQt5.QtWidgets import QApplication, QMessageBox

# Importing based classes
from interfaces import MainWindow
from mainTableModel import TableModel


class ClientsViewWindow(MainWindow):
    def __init__(self):
        super().__init__(12)

        # Connecting signals to slots
        self.ui.backBtn.clicked.connect(self.toMainWindow)
        self.ui.updateBtn.clicked.connect(self.updateTable)

        # Filling the table
        TableModel.fillTable(table_widget=self.ui.clientsTable, table="clients", withCheckboxes=True)

    # Updating table by use TableModel function
    def updateTable(self):
        if not TableModel.updateTable(table=self.ui.clientsTable, tableName="clients", isAdmin=True):
            QMessageBox.information(self, "Уведомление", "Нечего обновлять")

    # Opening main window for this window
    def toMainWindow(self):
        from AdminWindow import AdminWindow
        self.openWindow(AdminWindow())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClientsViewWindow()
    window.show()
    sys.exit(app.exec_())