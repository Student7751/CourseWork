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
        # Getting user data
        self.userData = userData
        # Filling table
        TableModel.fillTable(table_widget=self.ui.dealsTable, table="OFFERS", withCheckboxes=True)
        # Connecting signals to slots
        self.ui.updateBtn.clicked.connect(self.updateTable)
        self.ui.addBtn.clicked.connect(lambda: self.openWindow(DealAddWindow(self.userData)))
        self.ui.BackBtn.clicked.connect(self.toMainWindow)
        self.ui.searchEdit.textChanged.connect(self.searchData)
        self.ui.dealsTable.setSortingEnabled(True)

    def searchData(self, text):
        TableModel.search(table=self.ui.dealsTable, text=text)

    # Opening main window for this window
    def toMainWindow(self):
        from notaryWindow import NotaryWindow
        self.openWindow(NotaryWindow(self.userData))

    # Updating table when btn was clicked
    def updateTable(self):
        if not TableModel.updateTable(table=self.ui.dealsTable, tableName="OFFERS", userID=self.userData[0]):
            QMessageBox.information(self, "Уведомление", "Нечего обновлять")
        else:
            QMessageBox.information(self, "Уведомление", "Запрос на удаление отправлен!")
            TableModel.fillTable(table_widget=self.ui.dealsTable, table="OFFERS", withCheckboxes=True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DealsViewWindow()
    window.show()
    sys.exit(app.exec_())
