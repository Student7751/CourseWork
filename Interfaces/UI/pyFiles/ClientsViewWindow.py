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
        TableModel.fillTable(self.ui.clientsTable, "clients", 1)

    # Updating table by use TableModel function
    def updateTable(self):
        if TableModel.updateTable(self.ui.clientsTable, "clients") is None:
            QMessageBox.information(self, "Уведомление", "Нечего обновлять")

    # Opening main window for this window
    def toMainWindow(self):
        from AdminWindow import AdminWindow
        self.openWindow(AdminWindow("name"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClientsViewWindow()
    window.show()
    sys.exit(app.exec_())