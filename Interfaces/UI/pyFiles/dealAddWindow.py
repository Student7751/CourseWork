import sys

# Importing PyQt files
from PyQt5.QtWidgets import QApplication, QMessageBox

# Importing based class
from interfaces import MainWindow
from DB import DB

class DealAddWindow(MainWindow):
    def __init__(self, userData=()):
        super().__init__(10)

        self.userData = userData

        # Connecting signals to slots
        self.ui.cancelBtn.clicked.connect(self.toMainWindow)
        self.ui.addDealBtn.clicked.connect(self.addDeal)

    # Adding deal into table by using DB function
    def addDeal(self):
        # Getting data from the fields
        dealName = self.ui.dealName.text()
        dealPrice = self.ui.dealPrice.text()
        dealDescr = self.ui.dealDescr.toPlainText()
        # If all fields are filled
        if dealName and dealPrice and dealDescr:
            # Adding deal into unconfirmed table
            DB.addUnconfRecord(self.userData[0], "Добавление заявки", ";".join([dealName, dealDescr, dealPrice]))
            # Notify that everything in order
            QMessageBox.information(self, "Уведомление", "Услуга добавлена к рассмотрению!")
            # Open main window for this window
            self.toMainWindow()
        else:
            QMessageBox.information(self, "Уведомление", "Заполните все поля!")


    # Opening main window for this window
    def toMainWindow(self):
        from dealsViewWindow import DealsViewWindow
        self.openWindow(DealsViewWindow(self.userData))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DealAddWindow()
    window.show()
    sys.exit(app.exec_())
