import sys

# Importing based class
from interfaces import MainWindow

# Importing PyQt files
from PyQt5.QtWidgets import QApplication


class AdminWindow(MainWindow):
    def __init__(self, parent=None):
        super().__init__(1)

        # self.ui.toAuthWindow.clicked.connect(self.toAuthWindow)

    # def toAuthWindow(self):
    #     try:
    #         from UI.pyFiles.AuthWindow import AuthWindow
    #         self.close()
    #         self.AW = AuthWindow()
    #         self.AW.show()
    #     except:
    #         print("Error")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdminWindow()
    window.show()
    sys.exit(app.exec_())
