import sys

# Importing PyQt files
from PyQt5.QtWidgets import QApplication

# Importing based class
from interfaces import MainWindow


class ConfirmDealWindow(MainWindow):
    def __init__(self, data={}):
        super().__init__(7)

        # Filling the edit about offer
        for k, v in data.items():
            # If deal consist more than one offer
            if isinstance(v, list):
                v = "; ".join(v)
            # Creating and adding text into text edit
            new_text = f"<div style='text-align: left; font-size: 11pt;'><b>{k}</b>: {v}</div>"
            self.ui.aboutOffer.append(new_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConfirmDealWindow()
    window.show()
    sys.exit(app.exec_())
