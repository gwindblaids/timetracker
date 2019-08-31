import sys
from PyQt5 import QtWidgets
from main_window import MainWindow

app = QtWidgets.QApplication([])

application = MainWindow()
application.show()

sys.exit(app.exec())
