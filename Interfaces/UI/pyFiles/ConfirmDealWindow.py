import sys

# Importing PyQt files
from PyQt5.QtWidgets import QApplication, QMessageBox, QFileDialog

# Importing based class
from interfaces import MainWindow
from DB import DB

from fpdf import FPDF


class ConfirmDealWindow(MainWindow):
    def __init__(self, data={}, clientData=[]):
        super().__init__(7)
        # Getting data for the deal
        self.data = data
        # Getting main client data
        self.clientData = clientData
        # Filling deal edit
        self.fillData()
        # Connecting signals to slots
        self.ui.confirmBtn.clicked.connect(self.confirmDeal)
        self.ui.cancelBtn.clicked.connect(self.toMainWindow)
        self.ui.downloadBtn.clicked.connect(self.savePDF)

    def createPDF(self, fontName):
        pdf = FPDF()
        pdf.add_page()
        pdf.add_font('DejaVu', '', f'../font/{fontName}.ttf', uni=True)
        pdf.set_font("DejaVu", size=25)

        return pdf

    def savePDF(self):
        # Getting filename from user
        filename, _ = QFileDialog.getSaveFileName(self, "", "", "PDF Files (*.pdf)")
        if not filename:
            # If user cancels the file dialog, exit the function
            QMessageBox.information(self, "Уведомление", "Файл не выбран, пожалуйста выберите файл перед сохранением!")
            return 0
        # Creating pdf and setting it
        pdf = self.createPDF("DejaVuSerif")
        # Getting text from offer and splitting it
        text = self.ui.aboutOffer.toPlainText()
        header = text[:text.find(":") + 1]
        body = text[text.find(":"):]
        # Filling the pdf
        pdf.multi_cell(195, 10, txt=header + "\n\n", border=0, align="C")
        for i in body.split("\n")[1:]:
            pdf.multi_cell(195, 10, txt=i, border=1, align="C")
        # Saving new pdf file
        pdf.output(filename)

        QMessageBox.information(self, "Уведомление", "Ваш файл успешно сохранен!")

    # Opening main window for this window
    def toMainWindow(self):
        from makeDealWindow import MakeDealWindow
        self.openWindow(MakeDealWindow(self.clientData))

    # Confirming deal
    def confirmDeal(self):
        # DB.addUnconfRecord(self.clientData[0], self.data["NotaryID"],
        #                    "Совершение сделки", self.ui.aboutOffer.toPlainText())

        # Adding deal parameters into table
        DB.addDeal(self.data["Дата"], self.data["Название услуг/(-и)"], self.data["Скидка"],
                   self.data["Сумма сделки"], self.data["UserID"], self.data["NotaryID"])
        # Message that adding done
        QMessageBox.information(self, "Уведомление", "Сделка успешно совершена!")
        # Returning to the main window
        self.toMainWindow()

    # Filling edit
    def fillData(self):
        # Filling the edit about offer
        for k, v in self.data.items():
            # If key is not private
            if k not in ('UserID', 'NotaryID'):
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
