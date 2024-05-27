import sys

# Importing PyQt files
from PyQt5.QtWidgets import QApplication

# Importing based class
from interfaces import MainWindow
from mainTableModel import TableModel

from DB import DB


class NotaryClientsViewWindow(MainWindow):
    def __init__(self, userData=(1, "Name", "surname")):
        super().__init__(13)

        self.userData = userData

        TableModel.fillTable(table_widget=self.ui.clientsTable, table="clients")

        self.ui.backBtn.clicked.connect(self.toMainWindow)

        self.ui.onlyNotaryBox.stateChanged.connect(self.fillOtherClients)

    def fillOtherClients(self, state):
        if state:
            TableModel.fillClientsOfNotary(table_widget=self.ui.clientsTable, notaryID=self.userData[0])
        else:
            TableModel.fillTable(table_widget=self.ui.clientsTable, table="clients")

    # Opening main window for this window
    def toMainWindow(self):
        from notaryWindow import NotaryWindow
        self.openWindow(NotaryWindow(self.userData))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NotaryClientsViewWindow()
    window.show()
    sys.exit(app.exec_())
