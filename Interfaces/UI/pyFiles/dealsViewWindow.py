import sys

# Importing PyQt files
from PyQt5.QtWidgets import QApplication, QMessageBox

# Importing based class
from interfaces import MainWindow
from mainTableModel import TableModel

# Importing linked classes
from dealAddWindow import DealAddWindow


class DealsViewWindow(MainWindow):
    def __init__(self, userData=()):
        super().__init__(11)

        self.userData = userData

        # Filling table
        TableModel.fillTable(self.ui.dealsTable, "OFFERS", 1)
        # Connecting signals to slots
        self.ui.updateBtn.clicked.connect(self.updateTable)
        self.ui.addBtn.clicked.connect(lambda: self.openWindow(DealAddWindow(userData)))
        self.ui.BackBtn.clicked.connect(self.toMainWindow)

    # Opening main window for this window
    def toMainWindow(self):
        from notaryWindow import NotaryWindow
        self.openWindow(NotaryWindow(self.userData))

    # Updating table when btn was clicked
    def updateTable(self):
        if TableModel.updateTable(self.ui.dealsTable, "OFFERS") is None:
            QMessageBox.information(self, "Уведомление", "Нечего обновлять")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DealsViewWindow()
    window.show()
    sys.exit(app.exec_())
