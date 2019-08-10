import sys
from grafic.interface import QtWidgets, MainWindow, LoginWindow, NewUserWindow


app = QtWidgets.QApplication([])

application = MainWindow()
application.show()

login_app = LoginWindow()
login_app.show()

new_user_app = NewUserWindow()
new_user_app.show()

sys.exit(app.exec())