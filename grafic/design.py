# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './grafic/design.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 626)
        MainWindow.setMinimumSize(QtCore.QSize(860, 626))
        MainWindow.setMaximumSize(QtCore.QSize(860, 626))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: #414053;")
        MainWindow.setDocumentMode(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(50, 10, 781, 551))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.timerInnerLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.timerInnerLabel.setFont(font)
        self.timerInnerLabel.setStyleSheet("color:white;")
        self.timerInnerLabel.setTextFormat(QtCore.Qt.PlainText)
        self.timerInnerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timerInnerLabel.setObjectName("timerInnerLabel")
        self.verticalLayout.addWidget(self.timerInnerLabel)
        self.timerText = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.timerText.setFont(font)
        self.timerText.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.timerText.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.timerText.setToolTipDuration(-6)
        self.timerText.setStyleSheet("background-color: #E0E0E0; color: black; ")
        self.timerText.setObjectName("timerText")
        self.verticalLayout.addWidget(self.timerText)
        self.line_2 = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.timeLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.timeLabel.setStyleSheet("color:white;")
        self.timeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeLabel.setObjectName("timeLabel")
        self.verticalLayout.addWidget(self.timeLabel)
        self.setTime = QtWidgets.QTimeEdit(self.horizontalLayoutWidget_2)
        self.setTime.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.setTime.setObjectName("setTime")
        self.verticalLayout.addWidget(self.setTime)
        self.soundLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.soundLabel.setStyleSheet("color:white;")
        self.soundLabel.setTextFormat(QtCore.Qt.AutoText)
        self.soundLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.soundLabel.setObjectName("soundLabel")
        self.verticalLayout.addWidget(self.soundLabel)
        self.selectSignal = QtWidgets.QFontComboBox(self.horizontalLayoutWidget_2)
        self.selectSignal.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.selectSignal.setEditable(False)
        self.selectSignal.setObjectName("selectSignal")
        self.verticalLayout.addWidget(self.selectSignal)
        self.volumeLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.volumeLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.volumeLabel.setStyleSheet("color:white;")
        self.volumeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.volumeLabel.setObjectName("volumeLabel")
        self.verticalLayout.addWidget(self.volumeLabel)
        self.volume = QtWidgets.QSlider(self.horizontalLayoutWidget_2)
        self.volume.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.volume.setStyleSheet("")
        self.volume.setMinimum(0)
        self.volume.setMaximum(100)
        self.volume.setPageStep(1)
        self.volume.setOrientation(QtCore.Qt.Horizontal)
        self.volume.setInvertedAppearance(False)
        self.volume.setInvertedControls(False)
        self.volume.setObjectName("volume")
        self.verticalLayout.addWidget(self.volume)
        self.line = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.startButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.startButton.setFont(font)
        self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startButton.setToolTipDuration(-4)
        self.startButton.setStyleSheet("background-color: green; color: white;")
        self.startButton.setDefault(False)
        self.startButton.setObjectName("startButton")
        self.verticalLayout.addWidget(self.startButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.timer = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Hack")
        font.setPointSize(48)
        self.timer.setFont(font)
        self.timer.setStyleSheet("color:white;")
        self.timer.setAlignment(QtCore.Qt.AlignCenter)
        self.timer.setObjectName("timer")
        self.verticalLayout_2.addWidget(self.timer)
        self.tableUserData = QtWidgets.QTableView(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tableUserData.setFont(font)
        self.tableUserData.setStyleSheet("background-color:light; color: white;")
        self.tableUserData.setSortingEnabled(True)
        self.tableUserData.setObjectName("tableUserData")
        self.verticalLayout_2.addWidget(self.tableUserData)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 860, 30))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.menu.addSeparator()
        self.menu.addAction(self.action_2)
        self.menu.addSeparator()
        self.menu.addAction(self.action_4)
        self.menu.addSeparator()
        self.menu.addAction(self.action_5)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TimeTracker v.1.0"))
        self.timerInnerLabel.setText(_translate("MainWindow", "Содержимое таймера:"))
        self.timeLabel.setText(_translate("MainWindow", "Время"))
        self.soundLabel.setText(_translate("MainWindow", "Звук"))
        self.volumeLabel.setText(_translate("MainWindow", "Громкость"))
        self.startButton.setText(_translate("MainWindow", "START"))
        self.timer.setText(_translate("MainWindow", "12:00:32"))
        self.menu.setTitle(_translate("MainWindow", "Пользователи"))
        self.menu_2.setTitle(_translate("MainWindow", "Настройки"))
        self.menu_3.setTitle(_translate("MainWindow", "О программе"))
        self.action_2.setText(_translate("MainWindow", "Новый пользователь"))
        self.action_4.setText(_translate("MainWindow", "Выбрать пользователя"))
        self.action_5.setText(_translate("MainWindow", "Выход"))