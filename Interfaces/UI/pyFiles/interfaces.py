# Importing Qt files
from PyQt5.QtWidgets import QMainWindow

# Importing interface files
from Auth_UI import Ui_AuthWindow
from AdminWindow_UI import Ui_AdminWindow
from NotariesViewWindow_UI import Ui_NotariesViewWindow
from NotaryAddWindow_UI import Ui_NotaryAddWindow
from registrWindow_UI import Ui_RegistrWindow
from ClientWindow_UI import Ui_ClientWindow
from CompletedDealsWindow_UI import Ui_CompletedDealsWindow
from ConfirmDealWindow_UI import Ui_ConfirmDealWindow
from MakeDealWindow_UI import Ui_MakeDealWindow
from NotaryWindow_UI import Ui_NotaryWindow
from DealAddWindow_UI import Ui_DealAddWindow
from DealsViewWindow_UI import Ui_DealViewWindow
from ClientViewWindow_UI import Ui_ClientViewWindow


# Based class for all interfaces
class MainWindow(QMainWindow):
    """Base class for all windows in the program"""
    __interfaces = (Ui_AuthWindow, Ui_AdminWindow, Ui_NotariesViewWindow, Ui_NotaryAddWindow, Ui_RegistrWindow,
                    Ui_ClientWindow, Ui_CompletedDealsWindow, Ui_ConfirmDealWindow, Ui_MakeDealWindow, Ui_NotaryWindow,
                    Ui_DealAddWindow, Ui_DealViewWindow, Ui_ClientViewWindow)

    def __init__(self, interfaceIndex):
        super().__init__()

        self.ui = self.get_interface(interfaceIndex)()
        self.ui.setupUi(self)

    # Opening any window in the program
    def openWindow(self, window):
        self.close()
        self.wndw = self.createWindow(window)
        self.wndw.show()

    # Creating any window in the program
    def createWindow(self, window):
        self.w = window
        return self.w
    @classmethod
    def get_interface(cls, indx):
        return cls.__interfaces[indx]

    # Opening the Authorization window when the exit button is clicked
    def exit_btn(self):
        from AuthWindow import AuthWindow
        self.openWindow(AuthWindow())