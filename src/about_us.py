from PyQt5 import QtCore, QtGui, QtWidgets
from settings import *


class AboutWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setObjectName("AboutWindow")
        self.resize(293, 266)
        self.setMinimumSize(QtCore.QSize(293, 266))
        self.setMaximumSize(QtCore.QSize(293, 266))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(IMAGES_DIR + "icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("background-color:rgb(38, 38, 38);")

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("central_widget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 231, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser.setStyleSheet("""background-color: #414053;
                                          color: white;""")
        self.textBrowser.setObjectName("textBrowser")

        self.verticalLayout.addWidget(self.textBrowser)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.verticalLayout.addItem(spacerItem)

        self.acceptButton = QtWidgets.QPushButton(self.verticalLayoutWidget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.acceptButton.sizePolicy().hasHeightForWidth())

        self.acceptButton.setSizePolicy(sizePolicy)
        self.acceptButton.setMinimumSize(QtCore.QSize(0, 40))
        self.acceptButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.acceptButton.setStyleSheet("""background-color:green;
                                           color: white;""")
        self.acceptButton.setObjectName("acceptButton")
        self.acceptButton.clicked.connect(self.close)

        self.verticalLayout.addWidget(self.acceptButton)

        self.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("AboutWindow", "О Timetracker"))
        self.textBrowser.setHtml(_translate("AboutWindow", open("src/about.html", "r").read()))
        self.acceptButton.setText(_translate("AboutWindow", "Ок"))
