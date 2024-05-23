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

        # Connecting signals to slots
        self.ui.cancelBtn.clicked.connect(self.exit_btn)
        self.ui.registrBtn.clicked.connect(self.addUser)
        self.checkingInput()

    # Checking any changes of fields, type needs to determine type of login
    def checkingInput(self, type=0):
        # Checking input data
        self.ui.passEdit.textChanged.connect(lambda: InputValidator.checkPass(self.ui.passEdit.text(), self))
        self.ui.logEdit.textChanged.connect(lambda: InputValidator.checkLogin(self.ui.logEdit.text(), self, type))
        self.ui.numberEdit.textChanged.connect(lambda: InputValidator.checkNumber(self.ui.numberEdit.text(), self))
        self.ui.initialsEdit.textChanged.connect(lambda: InputValidator.checkInitials(self.ui.initialsEdit.text().split(), self))

    # Getting data from fields, return tuple with the data
    def getDataFromFields(self):
        initials = self.ui.initialsEdit.text().split()
        login = self.ui.logEdit.text()
        password = self.ui.passEdit.text()
        number = self.ui.numberEdit.text()

        return *initials, number, login, password

    # Checking that all fields are correct, type need to determine the login
    def isCorrectFields(self, name, surname, patronymic, number, login, password, type=0):
        return all([InputValidator.checkInitials([name, surname, patronymic], self),
                    InputValidator.checkLogin(login, self, type),
                    InputValidator.checkPass(password, self), InputValidator.checkNumber(number, self)])

    # Checking input values and adding user to DB
    def addUser(self, type=0):
        # Reading input data
        surname, name, patronymic, number, login, password = self.getDataFromFields()

        # Checking input data to correct with all parameters
        if self.isCorrectFields(surname, name, patronymic, number, login, password) and not DB.isLoginExists(login):
            # Using DB class method to add new user into DataBase
            if login.endswith("@client.com"):
                DB.addUser("clients", surname, name, patronymic, number, login, password)
            else:
                DB.addUser("notaries", surname, name, patronymic, number, login, password)

            QMessageBox.information(self, "Успех", "Пользователь успешно добавлен!")
            return 0
        QMessageBox.warning(self, "Неверные данные", "Данные введены неверно!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegisterWindow()
    window.show()
    sys.exit(app.exec_())
