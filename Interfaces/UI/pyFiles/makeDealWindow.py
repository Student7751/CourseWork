import sys

# Importing PyQt files
from PyQt5.QtWidgets import QApplication

# Importing based class
from interfaces import MainWindow
from mainTableModel import TableModel

class MakeDealWindow(MainWindow):
    def __init__(self, parent=None):
        super().__init__(8)

        TableModel.fillTable(self.ui.NotariesTable, "OFFERS", 1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MakeDealWindow()
    window.show()
    sys.exit(app.exec_())
