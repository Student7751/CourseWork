import sys

# Importing PyQt files
from PyQt5.QtWidgets import QApplication

# Importing based class
from interfaces import MainWindow

# Importing linked classes
from makeDealWindow import MakeDealWindow
from CompletedDealsWindow import CompletedDealsWindow
from ProfileWindow import ProfileWindow

class ClientWindow(MainWindow):
    def __init__(self, userData=(1, "Surname", "Name", "Patronymic", "Phone_number", "login", "password")):
        super().__init__(5)

        self.ui.welcome.setText(f"Добро пожаловать в систему, {userData[2]}!")
        # Connecting signals to slots
        self.ui.makeDealBtn.clicked.connect(lambda : self.openWindow(MakeDealWindow(userData)))
        self.ui.completedDealsBtn.clicked.connect(lambda : self.openWindow(CompletedDealsWindow(userData)))
        self.ui.profileBtn.clicked.connect(lambda : self.openWindow(ProfileWindow(2, userData + ("clients",))))
        self.ui.exitBtn.clicked.connect(self.exit_btn)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClientWindow()
    window.show()
    sys.exit(app.exec_())
