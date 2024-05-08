import sys

# Importing PyQt files
from PyQt5.QtWidgets import QApplication

# Importing based class
from interfaces import MainWindow

# Importing linked classes
from UI.pyFiles.AdminWindow import AdminWindow


class AuthWindow(MainWindow):
    def __init__(self, parent=None):
        super().__init__(0)

        self.test = None
        self.ui.AuthBtn.clicked.connect(self.to_role_window)

    def to_role_window(self):
        self.close()
        self.test = AdminWindow()
        self.test.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AuthWindow()
    window.show()
    sys.exit(app.exec_())
