class InputValidator:
    """A class for checking input data for correctness"""
    @staticmethod
    def checkPass(text, window):
        if len(text) < 8:
            txt = "Минимальная длина пароля 8 символов!"
        elif not any(i in "abcdefghijklmniopqrtsuvwxyz" for i in text.lower()):
            txt = "В пароле должны встречаться латинские буквы!"
        elif not any(i in "0123456789" for i in text):
            txt = "В пароле должны быть цифры!"
        else:
            txt = "Пароль подходит!"
        window.ui.passLine.setText(txt)
        return len(txt) == 16

    @staticmethod
    def checkLogin(login, window):
        if not (login.endswith("@client.com") or login.endswith("@notary.com")):
            txt = "Не найден один из постфиксов: @client.com или @notary.com"
        else:
            txt = "Логин подходит!"
        window.ui.logLine.setText(txt)
        return len(txt) == 15

    @staticmethod
    def checkNumber(number, window):
        if not number.startswith("+7"):
            txt = "Номер телефона должен начинаться с +7"
        elif len(number) != 11:
            txt = "Номер должен состоять из 11 цифр"
        else:
            txt = "Номер подходит!"
        window.ui.numberLine.setText(txt)
        return len(txt) == 15

    @staticmethod
    def checkInitials(initials, window):
        if not len(initials) == 3:
            txt = "Введите корректные данные через пробел"
        else:
            txt = "Данные подходят!"
        window.ui.initialsLine.setText(txt)
        return len(txt) == 16