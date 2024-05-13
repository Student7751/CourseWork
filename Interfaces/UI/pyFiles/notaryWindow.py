import sys

# Importing PyQt files
from PyQt5.QtWidgets import QApplication

# Importing based class
from interfaces import MainWindow


class NotaryWindow(MainWindow):
    def __init__(self, name):
        super().__init__(9)
        self.ui.welcome.setText(f"Добро пожаловать в систему, {name}!")

        self.ui.exitBtn.clicked.connect(self.exit_btn)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NotaryWindow("NAME")
    window.show()
    sys.exit(app.exec_())
