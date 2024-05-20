import sys

# Importing PyQt files
from PyQt5.QtWidgets import QApplication

# Importing based class
from interfaces import MainWindow

# Importing linked classes
from makeDealWindow import MakeDealWindow
from CompletedDealsWindow import CompletedDealsWindow

class ClientWindow(MainWindow):
    def __init__(self, userData=None):
        super().__init__(5)

        self.ui.welcome.setText(f"Добро пожаловать в систему, {userData[2]}!")
        # Connecting signals to slots
        self.ui.makeDealBtn.clicked.connect(lambda : self.openWindow(MakeDealWindow(userData)))
        self.ui.completedDealsBtn.clicked.connect(lambda : self.openWindow(CompletedDealsWindow(userData)))
        self.ui.exitBtn.clicked.connect(self.exit_btn)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClientWindow("name")
    window.show()
    sys.exit(app.exec_())
