import sys

# Importing PyQt files
from PyQt5.QtWidgets import QApplication

# Importing based class
from interfaces import MainWindow
from mainTableModel import TableModel


class CompletedDealsWindow(MainWindow):
    def __init__(self, data=[]):
        super().__init__(6)
        # Getting main client data
        self.clientData = data
        # Filling table
        TableModel.fillTable(self.ui.DealsTable, "completeddeals", False, self.clientData[0])
        # Connecting signals to slots
        self.ui.BackBtn.clicked.connect(self.toMainWindow)
        self.ui.searchEdit.textChanged.connect(self.searchData)

        self.ui.DealsTable.setSortingEnabled(True)

    def searchData(self, text):
        TableModel.search(table=self.ui.DealsTable, text=text)

    # Opening main window for this window
    def toMainWindow(self):
        from ClientWindow import ClientWindow
        self.openWindow(ClientWindow(self.clientData))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CompletedDealsWindow()
    window.show()
    sys.exit(app.exec_())
