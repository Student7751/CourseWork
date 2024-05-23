import sys

# Importing PyQt5 widgets
from PyQt5.QtWidgets import QApplication, QMessageBox

# Importing base classes
from interfaces import MainWindow
from DB import DB

# Importing linked classes
from registrWindow import RegisterWindow
from inputValidator import InputValidator


class ProfileWindow(MainWindow):
    def __init__(self, wt=0,
                 userData=(1, "Surname", "Name", "Patronymic", "Phone_numbe", "Login", "Password", "clients")):
        super().__init__(14)
        # Getting user data
        self.userData = userData
        self.wt = wt
        self.changeWidgets(userData)
        self.ui.applyBtn.clicked.connect(lambda: self.applyChanges(userData))
        self.ui.backBtn.clicked.connect(lambda: self.toMainWindow(userData[:-1]))
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
    def toMainWindow(self, data):
        from ClientWindow import ClientWindow
        self.openWindow(ClientWindow(data))

    # Applying changes
    def applyChanges(self, userData):
        # Getting user data
        newData = RegisterWindow.getDataFromFields(self)
        # If any field was changed
        if not (set(newData) <= set(userData)):
            # If all fields are correct
            if RegisterWindow.isCorrectFields(self, *newData):
                # Updating table, [-1] - table name, [0] - user ID
                DB.updateTable(userData[-1], userData[0], *newData)
                # Notification that everything was successful
                QMessageBox.information(self, "Уведомление", "Данные успешно обновлены!")
                # Returning to main window
                self.toMainWindow((userData[0], *newData))
                # Returning 0 to exit the function
                return 0
            else:
                QMessageBox.warning(self, "Неверные данные", "Данные введены неверно!")
        else:
            QMessageBox.warning(self, "Ошибка", "Измените хотя бы одно поле!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProfileWindow()
    window.show()
    sys.exit(app.exec_())
