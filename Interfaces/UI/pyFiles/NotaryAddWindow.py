import sys

# Importing PyQt files
from PyQt5.QtWidgets import QApplication

# Importing based class
from interfaces import MainWindow
from registrWindow import RegisterWindow

class NotaryAddWindow(MainWindow):
    def __init__(self, parent=None):
        super().__init__(3)

        # Connecting buttons with its functions
        self.ui.cancelBtn.clicked.connect(self.toMainWindow)
        self.ui.addNotaryBtn.clicked.connect(lambda: RegisterWindow.addUser(self, ut=1))
        # Checking data by use method from other class
        RegisterWindow.checkingInput(self, userType=1)


    # Opening main window for this window
    def toMainWindow(self):
        from NotariesViewWindow import NotariesViewWindow
        self.openWindow(NotariesViewWindow())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NotaryAddWindow()
    window.show()
    sys.exit(app.exec_())
