import sys

# Importing PyQt files
from PyQt5.QtWidgets import QApplication

# Importing based class
from interfaces import MainWindow


class CompletedDealsWindow(MainWindow):
    def __init__(self, parent=None):
        super().__init__(6)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CompletedDealsWindow()
    window.show()
    sys.exit(app.exec_())
