import sys

# Importing PyQt files
from PyQt5.QtWidgets import QApplication, QMessageBox

# Importing based class
from interfaces import MainWindow
from DB import DB

class ConfirmDealWindow(MainWindow):
    def __init__(self, data={}, clientData=[]):
        super().__init__(7)
        # Getting data for the deal
        self.data = data
        # Getting main client data
        self.clientData = clientData
        # Filling deal edit
        self.fillData()
        # Connecting signals to slots
        self.ui.confirmBtn.clicked.connect(self.confirmDeal)
        self.ui.cancelBtn.clicked.connect(self.toMainWindow)

    # Opening main window for this window
    def toMainWindow(self):
        from makeDealWindow import MakeDealWindow
        self.openWindow(MakeDealWindow(self.clientData))

    # Confirming deal
    def confirmDeal(self):
        # Adding deal parameters into table
        DB.addDeal(self.data["Дата"], self.data["Название услуг/(-и)"], self.data["Скидка"],
                   self.data["Сумма сделки"], self.data["UserID"], self.data["NotaryID"])
        # Message that adding done
        QMessageBox.information(self, "Уведомление", "Сделка успешно совершена!")
        # Returning to the main window
        self.toMainWindow()

    # Filling edit
    def fillData(self):
        # Filling the edit about offer
        for k, v in self.data.items():
            # If key is not private
            if k not in ('UserID', 'NotaryID'):
                # If deal consist more than one offer
                if isinstance(v, list):
                    v = "; ".join(v)
                # Creating and adding text into text edit
                new_text = f"<div style='text-align: left; font-size: 11pt;'><b>{k}</b>: {v}</div>"
                self.ui.aboutOffer.append(new_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConfirmDealWindow()
    window.show()
    sys.exit(app.exec_())
