import sys

# Importing PyQt files
from PyQt5.QtWidgets import QApplication, QMessageBox

# Importing based class
from interfaces import MainWindow
from mainTableModel import TableModel
from DB import DB

# Importing linked classes
from ConfirmDealWindow import ConfirmDealWindow

# Importing other tools
from datetime import date


class MakeDealWindow(MainWindow):
    def __init__(self, data=()):
        super().__init__(8)
        # Getting main user data
        self.data = data
        # Filling table with checkboxes (third parameter = 1)
        TableModel.fillTable(table_widget=self.ui.NotariesTable, table="OFFERS", withCheckboxes=True)
        # Getting list of notaries data
        self.res = DB.getNotariesNames()
        # Adding all notaries into combobox ([1:] uses to miss the ID)
        self.ui.notariesBox.addItems([" ".join(i[1:]) for i in self.res])
        # Connecting slot
        self.ui.makeDealBtn.clicked.connect(self.toConfirmClicked)
        self.ui.BackBtn.clicked.connect(self.toMainWindow)

        self.ui.searchEdit.textChanged.connect(self.searchData)

        self.ui.NotariesTable.selectionModel().selectionChanged.connect(self.displayDescr)

        self.ui.NotariesTable.setSortingEnabled(True)

    def displayDescr(self):
        selected_row = self.ui.NotariesTable.currentRow()
        descr = self.ui.NotariesTable.item(selected_row, 3).text()
        self.ui.descrEdit.setText(descr)


    def searchData(self, text):
        TableModel.search(table=self.ui.NotariesTable, text=text)
    # Opening the main window for this window
    def toMainWindow(self):
        from ClientWindow import ClientWindow
        self.openWindow(ClientWindow(self.data))

    # Getting notary ID by the data from combobox
    def getNotaryID(self, data):
        for notary in self.res:
            if all(part in notary for part in data.split()):
                print(notary)
                return notary[0]
        # Else returning None
        return None

    def createDealInfo(self, checked_items):
        dealInfo = {
            "Дата": date.today(),
            "Название услуг/(-и)": [item[1] for item in checked_items],
            "Описание услуг/(-и)": [item[2] for item in checked_items],
            "Нотариус": self.ui.notariesBox.currentText(),
            "Комиссионные": '7,2 %',
            "Скидка": 0,
            "Сумма сделки": [],
            "UserID": self.data[0],
            "NotaryID": self.getNotaryID(self.ui.notariesBox.currentText())
        }

        sums = [int(item[3]) for item in checked_items]
        discount = len(sums) * 4
        totalSum = sum(sums) * (1 - discount / 100) * 1.072
        dealInfo["Скидка"] = discount
        dealInfo["Сумма сделки"] = totalSum

        return dealInfo

    # Filling the dict and opening the window
    def toConfirmClicked(self):
        # Getting list of checked rows
        checkedItems = TableModel.getCheckedItems(table=self.ui.NotariesTable)
        # If any row checked
        if checkedItems:
            dealInfo = self.createDealInfo(checkedItems)
            print(dealInfo)
            print(self.data)
            # Opening other window
            self.openWindow(ConfirmDealWindow(dealInfo, self.data))
            return 0
        else:
            QMessageBox.warning(self, "Уведомление", "Выберите хотя бы одну сделку!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MakeDealWindow()
    window.show()
    sys.exit(app.exec_())
