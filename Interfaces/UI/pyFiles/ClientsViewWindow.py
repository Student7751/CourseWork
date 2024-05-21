import sys

# Importing PyQt files
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QTableWidget

# Importing based classes
from interfaces import MainWindow
from mainTableModel import TableModel


class ClientsViewWindow(MainWindow):
    def __init__(self, wt=0):
        super().__init__(12)
        self.wt = wt
        self.ui.backBtn.clicked.connect(self.toMainWindow)

        # Filling the table
        TableModel.fillTable(self.ui.clientsTable, "clients")

    # Opening main window for this window
    def toMainWindow(self):
        if self.wt:
            from notaryWindow import NotaryWindow
            self.openWindow(NotaryWindow())
        else:
            from AdminWindow import AdminWindow
            self.openWindow(AdminWindow("name"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClientsViewWindow()
    window.show()
    sys.exit(app.exec_())