import sys

# Importing PyQt files
from PyQt5.QtWidgets import QApplication

# Importing based class
from interfaces import MainWindow

# Importing linked classes
from NotaryClientsViewWindow import NotaryClientsViewWindow
from dealsViewWindow import DealsViewWindow


class NotaryWindow(MainWindow):
    def __init__(self, userData=(1,"Name", "surname")):
        super().__init__(9)

        # Displaying welcome text
        self.ui.welcome.setText(f"Добро пожаловать в систему, {userData[1]}!")
        # Connecting signals to slots
        self.ui.clientListBtn.clicked.connect(lambda: self.openWindow(NotaryClientsViewWindow()))
        self.ui.editDealBtn.clicked.connect(lambda: self.openWindow(DealsViewWindow()))
        self.ui.exitBtn.clicked.connect(self.exit_btn)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NotaryWindow()
    window.show()
    sys.exit(app.exec_())
