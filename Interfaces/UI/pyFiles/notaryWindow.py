import sys

# Importing PyQt files
from PyQt5.QtWidgets import QApplication

# Importing based class
from interfaces import MainWindow


class NotaryWindow(MainWindow):
    def __init__(self, parent=None):
        super().__init__(9)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NotaryWindow()
    window.show()
    sys.exit(app.exec_())
