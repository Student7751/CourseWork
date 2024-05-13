import sys

# Importing PyQt files
from PyQt5.QtWidgets import QApplication, QMessageBox

# Importing base class
from interfaces import MainWindow

# Importing DataBase
from DB import DB

# Importing input validator
from inputValidator import InputValidator


class RegisterWindow(MainWindow):
    def __init__(self, parent=None):
        super().__init__(4)

        self.ui.cancelBtn.clicked.connect(self.exit_btn)
        self.ui.registrBtn.clicked.connect(self.addUser)
        self.checkingInput()

    def checkingInput(self, type=0):
            # Checking input data
            self.ui.passEdit.textChanged.connect(lambda: InputValidator.checkPass(self.ui.passEdit.text(), self))
            self.ui.logEdit.textChanged.connect(lambda: InputValidator.checkLogin(self.ui.logEdit.text(), self, type))
            self.ui.numberEdit.textChanged.connect(lambda: InputValidator.checkNumber(self.ui.numberEdit.text(), self))
            self.ui.initialsEdit.textChanged.connect(lambda: InputValidator.checkInitials(self.ui.initialsEdit.text().split(), self))

    # Checking input values and adding user to DB
    def addUser(self, type=0):
        # Reading input data
        initials = self.ui.initialsEdit.text().split()
        login = self.ui.logEdit.text()
        password = self.ui.passEdit.text()
        number = self.ui.numberEdit.text()

        # Checking input data to correct with all parameters
        if all([InputValidator.checkInitials(initials, self), InputValidator.checkLogin(login, self, type),
                InputValidator.checkPass(password, self), InputValidator.checkNumber(number, self),
                not DB.isLoginExists(login)]):
            # Using DB class method to add new user into DataBase
            if login.endswith("@client.com"):
                DB.addUser("clients", *initials, number, login, password)
            else:
                DB.addUser("notaries", *initials, number, login, password)

            QMessageBox.information(self, "Успех", "Пользователь успешно добавлен!")
            return 0
        QMessageBox.warning(self, "Неверные данные", "Данные введены неверно!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegisterWindow()
    window.show()
    sys.exit(app.exec_())
