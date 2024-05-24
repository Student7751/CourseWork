import sys

# Importing PyQt files
from PyQt5.QtWidgets import QApplication

# Importing based class
from interfaces import MainWindow
from mainTableModel import TableModel


class NotaryClientsViewWindow(MainWindow):
    def __init__(self, userData=(1, "Name", "surname")):
        super().__init__(13)

        self.userData = userData

        TableModel.fillTable(table_widget=self.ui.clientsTable, table="clients")

        self.ui.backBtn.clicked.connect(self.toMainWindow)

    # Opening main window for this window
    def toMainWindow(self):
        from notaryWindow import NotaryWindow
        self.openWindow(NotaryWindow(self.userData))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NotaryClientsViewWindow()
    window.show()
    sys.exit(app.exec_())
