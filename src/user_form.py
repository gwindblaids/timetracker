from PyQt5 import QtCore, QtGui, QtWidgets
from settings import *

class NewUserWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.setObjectName("NewUserWindow")
        self.resize(395, 435)
        self.setMinimumSize(QtCore.QSize(395, 435))
        self.setMaximumSize(QtCore.QSize(395, 435))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(IMAGES_DIR+"icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("background-color: #414053;")

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("central_widget")

        self.verticalWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget.setGeometry(QtCore.QRect(40, 20, 321, 381))
        self.verticalWidget.setStyleSheet("""QLineEdit {
                                             color: white;
                                            }""")
        self.verticalWidget.setObjectName("verticalWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.newUserLabel = QtWidgets.QLabel(self.verticalWidget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newUserLabel.sizePolicy().hasHeightForWidth())

        self.newUserLabel.setSizePolicy(sizePolicy)
        self.newUserLabel.setMaximumSize(QtCore.QSize(16777215, 100))

        font = QtGui.QFont()
        font.setPointSize(16)

        self.newUserLabel.setFont(font)
        self.newUserLabel.setStyleSheet("color: white;")
        self.newUserLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.newUserLabel.setObjectName("newUserLabel")

        self.verticalLayout.addWidget(self.newUserLabel)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.verticalLayout.addItem(spacerItem)
        self.profilePhoto = QtWidgets.QPushButton(self.verticalWidget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profilePhoto.sizePolicy().hasHeightForWidth())

        self.profilePhoto.setSizePolicy(sizePolicy)
        self.profilePhoto.setMaximumSize(QtCore.QSize(200, 120))

        font.setPointSize(14)

        self.profilePhoto.setFont(font)
        self.profilePhoto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.profilePhoto.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.profilePhoto.setLayoutDirection(QtCore.Qt.LeftToRight)

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(IMAGES_DIR+"users_photo/default.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.profilePhoto.setIcon(icon1)
        self.profilePhoto.setIconSize(QtCore.QSize(50, 50))
        self.profilePhoto.setFlat(True)
        self.profilePhoto.setObjectName("profilePhoto")

        self.verticalLayout.addWidget(self.profilePhoto, 0, QtCore.Qt.AlignHCenter)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.verticalLayout.addItem(spacerItem1)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.name = QtWidgets.QLabel(self.verticalWidget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())

        self.name.setSizePolicy(sizePolicy)
        self.name.setMaximumSize(QtCore.QSize(100, 45))

        font.setPointSize(14)

        self.name.setFont(font)
        self.name.setStyleSheet("color: white;")
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        
        self.horizontalLayout_3.addWidget(self.name)
        self.name_edit = QtWidgets.QLineEdit(self.verticalWidget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_edit.sizePolicy().hasHeightForWidth())

        self.name_edit.setSizePolicy(sizePolicy)
        self.name_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.name_edit.setPlaceholderText("")
        self.name_edit.setObjectName("name_edit")

        self.horizontalLayout_3.addWidget(self.name_edit)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.verticalLayout.addItem(spacerItem2)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.last_name = QtWidgets.QLabel(self.verticalWidget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.last_name.sizePolicy().hasHeightForWidth())

        self.last_name.setSizePolicy(sizePolicy)
        self.last_name.setMaximumSize(QtCore.QSize(100, 45))

        font.setPointSize(14)

        self.last_name.setFont(font)
        self.last_name.setStyleSheet("color: white;")
        self.last_name.setAlignment(QtCore.Qt.AlignCenter)
        self.last_name.setObjectName("last_name")

        self.horizontalLayout.addWidget(self.last_name)

        self.surname_edit = QtWidgets.QLineEdit(self.verticalWidget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.surname_edit.sizePolicy().hasHeightForWidth())

        self.surname_edit.setSizePolicy(sizePolicy)
        self.surname_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.surname_edit.setObjectName("surname_edit")

        self.horizontalLayout.addWidget(self.surname_edit)

        self.verticalLayout.addLayout(self.horizontalLayout)

        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.verticalLayout.addItem(spacerItem3)

        self.create_button = QtWidgets.QPushButton(self.verticalWidget)

        font.setPointSize(16)

        self.create_button.setFont(font)
        self.create_button.setStyleSheet("background-color: green;color: white;")
        self.create_button.setObjectName("create_button")

        self.verticalLayout.addWidget(self.create_button)

        self.setCentralWidget(self.centralwidget)
        
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("NewUserWindow", "Новый пользователь"))
        self.newUserLabel.setText(_translate("NewUserWindow", "Создать нового пользователя:"))
        self.name.setText(_translate("NewUserWindow", "Имя :"))
        self.last_name.setText(_translate("NewUserWindow", "Фамилия: "))
        self.create_button.setText(_translate("NewUserWindow", "Создать"))
