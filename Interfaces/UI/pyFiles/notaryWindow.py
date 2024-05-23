import sys

# Importing PyQt files
from PyQt5.QtWidgets import QApplication

# Importing based class
from interfaces import MainWindow

# Importing linked classes
from NotaryClientsViewWindow import NotaryClientsViewWindow
from dealsViewWindow import DealsViewWindow
from ProfileWindow import ProfileWindow

class NotaryWindow(MainWindow):
    def __init__(self, userData=(1, "Surname", "Name", "Patronymic", "Phone_number", "login", "password")):
        super().__init__(9)

        # Displaying welcome text
        self.ui.welcome.setText(f"Добро пожаловать в систему, {userData[2]}!")
        # Connecting signals to slots
        self.ui.clientListBtn.clicked.connect(lambda: self.openWindow(NotaryClientsViewWindow()))
        self.ui.editDealBtn.clicked.connect(lambda: self.openWindow(DealsViewWindow()))
        self.ui.toProfileBtn.clicked.connect(lambda : self.openWindow(ProfileWindow(1, userData + ("notaries", ))))
        self.ui.exitBtn.clicked.connect(self.exit_btn)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NotaryWindow()
    window.show()
    sys.exit(app.exec_())
