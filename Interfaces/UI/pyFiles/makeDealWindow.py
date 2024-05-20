import sys

# Importing PyQt files
from PyQt5.QtWidgets import QApplication

# Importing based class
from interfaces import MainWindow
from mainTableModel import TableModel
from DB import DB

# Importing linked classes
from ConfirmDealWindow import ConfirmDealWindow

# Importing other tools
from datetime import date


class MakeDealWindow(MainWindow):
    def __init__(self, parent=None):
        super().__init__(8)

        # Filling table with checkboxes (third parameter = 1)
        TableModel.fillTable(self.ui.NotariesTable, "OFFERS", 1)
        # Adding all notaries into combobox
        self.ui.notariesBox.addItems([" ".join(i[1:]) for i in DB.getNotariesNames()])
        # Connecting slot
        self.ui.makeDealBtn.clicked.connect(self.toConfirmClicked)

    # Filling the dict and opening the window
    def toConfirmClicked(self):
        # Getting list of checked rows
        rt = TableModel.getCheckedItems(self.ui.NotariesTable)
        # Creating dict with the default parameters
        d = {"Дата": str(date.today()),
             "Название услуг/(-и)": [],
             "Описание услуг/(-и)": [],
             "Нотариус": self.ui.notariesBox.currentText(),
             "Комиссионные": '7,2 %',
             "Скидка": 0,
             "Сумма сделки": []}
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
        self.openWindow(ConfirmDealWindow(d))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MakeDealWindow()
    window.show()
    sys.exit(app.exec_())
