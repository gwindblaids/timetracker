from PyQt5 import QtWidgets
from src.select_user import Ui_selectUserWindow
from src.main_window import Ui_MainWindow
from src.user_form import Ui_NewUserWindow
from src.about_us import Ui_AboutWindow


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


class AboutWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(AboutWindow, self).__init__()
        self.ui = Ui_AboutWindow()
        self.ui.setupUi(self)


