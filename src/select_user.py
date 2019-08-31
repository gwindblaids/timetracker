from PyQt5 import QtCore, QtGui, QtWidgets
from settings import *

class SelectUserWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("selectUserWindow")
        self.resize(390, 277)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(390, 277))
        self.setMaximumSize(QtCore.QSize(390, 277))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(IMAGES_DIR+"icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("background-color: #414053;")
        self.setAnimated(True)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("central_widget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 331, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.select_user_label = QtWidgets.QLabel(self.verticalLayoutWidget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_user_label.sizePolicy().hasHeightForWidth())

        self.select_user_label.setSizePolicy(sizePolicy)
        self.select_user_label.setMaximumSize(QtCore.QSize(16777215, 60))
        self.select_user_label.setBaseSize(QtCore.QSize(0, 0))

        font = QtGui.QFont()
        font.setPointSize(16)

        self.select_user_label.setFont(font)
        self.select_user_label.setStyleSheet("color: white;")
        self.select_user_label.setScaledContents(False)
        self.select_user_label.setAlignment(QtCore.Qt.AlignCenter)
        self.select_user_label.setObjectName("select_user_label")

        self.verticalLayout.addWidget(self.select_user_label)

        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.new_user = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.new_user.setEnabled(True)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_user.sizePolicy().hasHeightForWidth())

        self.new_user.setSizePolicy(sizePolicy)
        self.new_user.setMaximumSize(QtCore.QSize(75, 75))
        self.new_user.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.new_user.setText("")

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(IMAGES_DIR + "users_photo/addNewUser.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.new_user.setIcon(icon1)
        self.new_user.setIconSize(QtCore.QSize(120, 120))
        self.new_user.setFlat(True)
        self.new_user.setObjectName("new_user")

        self.gridLayout_2.addWidget(self.new_user, 0, 2, 1, 1)

        self.default_user = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.default_user.setEnabled(True)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.default_user.sizePolicy().hasHeightForWidth())

        self.default_user.setSizePolicy(sizePolicy)
        self.default_user.setMaximumSize(QtCore.QSize(75, 75))
        self.default_user.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.default_user.setText("")

        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(IMAGES_DIR + "users_photo/default.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.default_user.setIcon(icon2)
        self.default_user.setIconSize(QtCore.QSize(70, 70))
        self.default_user.setFlat(True)
        self.default_user.setObjectName("default_user")

        self.gridLayout_2.addWidget(self.default_user, 0, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout_2)

        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)

        self.verticalLayout.addItem(spacerItem)

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.create = QtWidgets.QPushButton(self.verticalLayoutWidget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.create.sizePolicy().hasHeightForWidth())

        self.create.setSizePolicy(sizePolicy)
        self.create.setMaximumSize(QtCore.QSize(80, 50))
        self.create.setSizeIncrement(QtCore.QSize(0, 0))

        font = QtGui.QFont()
        font.setPointSize(14)

        self.create.setFont(font)
        self.create.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.create.setStyleSheet("background-color: green;color: white;")
        self.create.setObjectName("create")

        self.horizontalLayout.addWidget(self.create)

        spacerItem1 = QtWidgets.QSpacerItem(10, 5, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.exit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exit.clicked.connect(self.close)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit.sizePolicy().hasHeightForWidth())

        self.exit.setSizePolicy(sizePolicy)
        self.exit.setMaximumSize(QtCore.QSize(80, 50))

        font = QtGui.QFont()
        font.setPointSize(14)

        self.exit.setFont(font)
        self.exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit.setStyleSheet("background-color: red;color: white;")
        self.exit.setObjectName("exit")

        self.horizontalLayout.addWidget(self.exit)

        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("selectUserWindow", "TimeTracker"))
        self.select_user_label.setText(_translate("selectUserWindow", "Выберите пользователя:"))
        self.create.setText(_translate("selectUserWindow", "Ок"))
        self.exit.setText(_translate("selectUserWindow", "Выход"))
