import sys

# Importing based classes
from interfaces import MainWindow
from DB import DB

# Importing PyQt files
from PyQt5.QtWidgets import QApplication

# Importing linked classes
from ClientsViewWindow import ClientsViewWindow
from NotariesViewWindow import NotariesViewWindow

class AdminWindow(MainWindow):
    def __init__(self, name):
        super().__init__(1)

        self.ui.toAuthWindow.clicked.connect(self.exit_btn)
        self.ui.toClientsViewWindow.clicked.connect(lambda: self.openWindow(ClientsViewWindow()))
        self.ui.toEditNotaryWindow.clicked.connect(lambda: self.openWindow(NotariesViewWindow()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdminWindow()
    window.show()
    sys.exit(app.exec_())
