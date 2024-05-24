class InputValidator:
    """A class for checking input data for correctness"""
    @staticmethod
    def checkPass(text, window):
        if len(text) < 8:
            txt = "Минимальная длина пароля 8 символов!"
        elif not any(c in "abcdefghijklmniopqrtsuvwxyz" for c in text):
            txt = "В пароле должны встречаться латинские буквы!"
        elif not any(c.isdigit() for c in text):
            txt = "В пароле должны быть цифры!"
        else:
            txt = "Пароль подходит!"
        window.ui.passLine.setText(txt)
        return txt == "Пароль подходит!"

    @staticmethod
    def checkLogin(login, window, userType=0):
        validPostfixes = {
            0: ("@client.com", "@notary.com"),
            1: ("@notary.com",),
            2: ("@client.com",)
        }
        if not any(login.endswith(postfix) for postfix in validPostfixes[userType]):
            txt = f"Не найден один из постфиксов: {', '.join(validPostfixes[userType])}"
        else:
            txt = "Логин подходит!"
        window.ui.logLine.setText(txt)
        return txt == "Логин подходит!"

    @staticmethod
    def checkNumber(number, window):
        if not number.startswith("+7"):
            txt = "Номер телефона должен начинаться с +7"
        elif not number[2:].isdigit() or len(number) != 12:
            txt = "Номер должен состоять из 12 цифр"
        else:
            txt = "Номер подходит!"
        window.ui.numberLine.setText(txt)
        return txt == "Номер подходит!"

    @staticmethod
    def checkInitials(initials, window):
        if len(initials) != 3 or any(not i for i in initials):
            txt = "Введите корректные данные через пробел"
        else:
            txt = "Данные подходят!"
        window.ui.initialsLine.setText(txt)
        return txt == "Данные подходят!"
