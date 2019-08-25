import sys
from src import interface

app = interface.QtWidgets.QApplication([])

application = interface.MainWindow()
application.show()

login_app = interface.LoginWindow()
login_app.show()

new_user_app = interface.NewUserWindow()
new_user_app.show()

about_window = interface.AboutWindow()
about_window.show()


sys.exit(app.exec())