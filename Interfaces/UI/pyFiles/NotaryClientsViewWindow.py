import sys

# Importing PyQt files
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtCore import Qt

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

        self.ui.clientsTable.selectionModel().selectionChanged.connect(self.getInfoByClientID)

        self.ui.searchEdit.textChanged.connect(self.searchData)

    def searchData(self, text):
        TableModel.search(table=self.ui.clientsTable, text=text)

    def getInfoByClientID(self):
        selected_row = self.ui.clientsTable.currentRow()
        if selected_row != -1:
            clientID = self.ui.clientsTable.item(selected_row, 0).text()
            res = DB.getInfoFromCompletedDeals(clientID=clientID)
            if res:
                deals_info = [f"Название услуг-/и: {name}\nДата сделки: {date}\nЦена сделки: {price}\n"
                              "------------------------------------------------------------"
                              for name, date, price in res]
                message = f"Количество сделок с данным клиентом: {len(res)}\n" + "\n".join(deals_info)
                QMessageBox.information(self, "Информация о сделке", message)
            else:
                QMessageBox.information(self, "Информация о сделке", "Это не Ваш клиент!")

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
