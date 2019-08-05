from PyQt5 import QtWidgets
from grafic.select_user import Ui_selectUserWindow
from grafic.design import Ui_MainWindow
from grafic.user_form import Ui_NewUserWindow


class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.ui = Ui_selectUserWindow()
        self.ui.setupUi(self)


class NewUserWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(NewUserWindow, self).__init__()
        self.ui = Ui_NewUserWindow()
        self.ui.setupUi(self)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


