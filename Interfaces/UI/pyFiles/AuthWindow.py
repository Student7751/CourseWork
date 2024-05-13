import sys

# Importing PyQt files
from PyQt5.QtWidgets import QApplication, QMessageBox

# Importing based classes
from interfaces import MainWindow
from DB import DB

# Importing linked classes
from ClientWindow import ClientWindow
from registrWindow import RegisterWindow
from notaryWindow import NotaryWindow


class AuthWindow(MainWindow):
    # Role:Window dictionary
    ROLE_WINDOWS = {
        "CLIENTS": ClientWindow,
        "NOTARIES": NotaryWindow
    }

    def __init__(self, parent=None):
        super().__init__(0)

        self.ui.AuthBtn.clicked.connect(self.toRoleWindow)
        self.ui.RegistrBtn.clicked.connect(lambda: self.openWindow(RegisterWindow()))

    # Getting a role by login postfix
    def getUserRole(self, login):
        if login.endswith("@client.com"):
            return "CLIENTS"
        elif login.endswith("@notary.com"):
            return "NOTARIES"
        else:
            return None

    # Getting tuple((name, surname), role) if role exists
    def authenticateUser(self, login, password):
        role = self.getUserRole(login)
        if role:
            return DB.getUser(role, login, password), role
        return None

    # Opening window for each role
    def toRoleWindow(self):
        # Getting login and password
        login = self.ui.logEdit.text()
        password = self.ui.passEdit.text()
        # Getting tuple with the data
        res = self.authenticateUser(login, password)
        # If result is not None and tuple with data is not Empty
        if res and res[0]:
            # Open role window
            self.openWindow(self.ROLE_WINDOWS.get(res[1])(res[0][0]))
        else:
            QMessageBox.warning(self, "Неверные данные", "Неверный логин или пароль!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AuthWindow()
    window.show()
    sys.exit(app.exec_())
