import sys

# Importing PyQt5 widgets
from PyQt5.QtWidgets import QApplication, QMessageBox

# Importing base classes
from interfaces import MainWindow
from DB import DB

# Importing linked classes
from registrWindow import RegisterWindow


class ProfileWindow(MainWindow):
    def __init__(self, wt=0,
                 userData=(1, "Surname", "Name", "Patronymic", "Phone_number", "Login", "Password", "clients")):
        super().__init__(14)
        # Getting user data
        self.userData = userData
        # Getting windows type
        self.wt = wt
        # Changing widgets
        self.changeWidgets(userData)
        # Connecting signals to slots
        self.ui.applyBtn.clicked.connect(self.applyChanges)
        self.ui.backBtn.clicked.connect(self.toMainWindow)
        # Checking any changes
        RegisterWindow.checkingInput(self, wt)

    # Changing widgets and setting user data to fields
    def changeWidgets(self, userData):
        # Getting user data ([1:] needs to ignore ID)
        userSurname, userName, userPatronymic, userPhone_number, userLogin, userPassword, userType = userData[1:]
        self.ui.initialsEdit.setText(f"{userSurname} {userName} {userPatronymic}")
        self.ui.numberEdit.setText(userPhone_number)
        self.ui.logEdit.setText(userLogin)
        self.ui.passEdit.setText(userPassword)

    # Opening main window for this window
    def toMainWindow(self):
        if self.wt == 2:
            from ClientWindow import ClientWindow
            self.openWindow(ClientWindow(self.userData[:-1]))
        else:
            from notaryWindow import NotaryWindow
            self.openWindow(NotaryWindow(self.userData[:-1]))

    # Applying changes
    def applyChanges(self):
        # Getting user data
        newData = RegisterWindow.getDataFromFields(self)
        print(self.userData)
        print(newData)
        # If nothing changes
        if set(newData) <= set(self.userData):
            QMessageBox.warning(self, "Ошибка", "Измените хотя бы одно поле!")
            return 0

        if newData[4] != self.userData[5] and DB.isLoginExists(newData[4]):
            QMessageBox.warning(self, "Ошибка", "Такой логин уже существует!")
            return 0

        # If all fields are correct
        if RegisterWindow.isCorrectFields(self, *newData, self.wt):
            # Updating table, [-1] - table name, [0] - user ID
            DB.updateTable(self.userData[-1], self.userData[0], *newData)
            # Notification that everything was successful
            QMessageBox.information(self, "Уведомление", "Данные успешно обновлены!")
            self.userData = (self.userData[0],) + newData + ("23", )
            # Returning to main window
            self.toMainWindow()
            # Returning 0 to exit the function
            return 0
        else:
            QMessageBox.warning(self, "Неверные данные", "Данные введены неверно!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProfileWindow()
    window.show()
    sys.exit(app.exec_())
