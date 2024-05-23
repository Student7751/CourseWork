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
        TableModel.fillTable(self.ui.NotariesTable, "OFFERS", 1)
        # Getting list of notaries data
        self.res = DB.getNotariesNames()
        # Adding all notaries into combobox ([1:] uses to miss the ID)
        self.ui.notariesBox.addItems([" ".join(i[1:]) for i in self.res])
        # Connecting slot
        self.ui.makeDealBtn.clicked.connect(self.toConfirmClicked)
        self.ui.BackBtn.clicked.connect(self.toMainWindow)

    # Opening the main window for this window
    def toMainWindow(self):
        from ClientWindow import ClientWindow
        self.openWindow(ClientWindow(self.data))

    # Getting notary ID by the data from combobox
    def getNotaryID(self, data):
        # Spliting data for get initials
        for i in data.split():
            # If any initial in the notaries list returning it
            for j in self.res:
                if i in j:
                    return j[0]
        # Else returning None
        return None

    # Filling the dict and opening the window
    def toConfirmClicked(self):
        # Getting list of checked rows
        rt = TableModel.getCheckedItems(self.ui.NotariesTable)
        # If any row checked
        if rt:
            # Creating dict with the default parameters
            d = {"Дата": str(date.today()),
                 "Название услуг/(-и)": [],
                 "Описание услуг/(-и)": [],
                 "Нотариус": self.ui.notariesBox.currentText(),
                 "Комиссионные": '7,2 %',
                 "Скидка": 0,
                 "Сумма сделки": [],
                 "UserID": self.data[0],
                 "NotaryID": self.getNotaryID(self.ui.notariesBox.currentText())
                 }

            # Filling the dict
            for i in range(len(rt)):
                d["Название услуг/(-и)"].append(rt[i][1])
                d["Описание услуг/(-и)"].append(rt[i][2])
                d["Сумма сделки"].append(int(rt[i][3]))

            # Discount calculation
            p = d["Сумма сделки"]
            d["Скидка"] = (len(p) * 4)
            p = sum(p) - (sum(p) * (d["Скидка"] / 100))
            d["Сумма сделки"] = p + (p * 0.07)
            # Opening other window
            self.openWindow(ConfirmDealWindow(d, self.data))
            return 0

        QMessageBox.warning(self, "Уведомление", "Выберите хотя бы одну сделку!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MakeDealWindow()
    window.show()
    sys.exit(app.exec_())
