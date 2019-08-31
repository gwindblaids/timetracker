from PyQt5 import QtCore, QtGui, QtWidgets
from os import listdir
from os.path import isfile, join
from datetime import datetime, timedelta
from dbconnect import Database
from vlc import MediaPlayer
from settings import *
from about_us import AboutWindow
from user_form import NewUserWindow
from select_user import SelectUserWindow


class MainWindow(QtWidgets.QMainWindow):
    """main application window"""

    def __init__(self):
        """initialize window object"""
        super().__init__()
        self.initUI()

    def initUI(self):
        """initialize users UI"""
        self.setObjectName("MainWindow")
        self.resize(860, 618)
        self.setMinimumSize(QtCore.QSize(860, 618))
        self.setMaximumSize(QtCore.QSize(860, 618))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(IMAGES_DIR + "icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setAutoFillBackground(False)
        self.setStyleSheet("background-color: #414053;")
        self.setDocumentMode(False)
        self.setUnifiedTitleAndToolBarOnMac(True)

        self.about_window = AboutWindow()
        self.about_window.setWindowModality(QtCore.Qt.ApplicationModal)

        self.new_user_window = NewUserWindow()
        self.new_user_window.setWindowModality(QtCore.Qt.ApplicationModal)

        self.select_user_window = SelectUserWindow()
        self.select_user_window.setWindowModality(QtCore.Qt.ApplicationModal)

        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setObjectName("central_widget")

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.central_widget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 10, 781, 551))
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
        spacerItem = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.timer_text = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)

        font.setPointSize(14)

        self.timer_text.setFont(font)
        self.timer_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.timer_text.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.timer_text.setToolTipDuration(-6)
        self.timer_text.setStyleSheet("background-color: #E0E0E0; color: black; ")
        self.timer_text.setObjectName("timer_text")

        self.verticalLayout.addWidget(self.timer_text)

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
        self.setTime.setStyleSheet("color:white;")
        self.setTime.setObjectName("setTime")
        self.setTime.setDisplayFormat("HH:mm:ss")

        self.verticalLayout.addWidget(self.setTime)

        self.soundLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.soundLabel.setStyleSheet("color:white;")
        self.soundLabel.setTextFormat(QtCore.Qt.AutoText)
        self.soundLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.soundLabel.setObjectName("soundLabel")

        self.verticalLayout.addWidget(self.soundLabel)

        self.selectSignal = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.selectSignal.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.selectSignal.setStyleSheet("color:white;")
        self.selectSignal.setEditable(False)
        self.selectSignal.setObjectName("selectSignal")
        self.selectSignal.addItems([f.replace(".mp3", "") for f in listdir(MUSIC_DIR) if isfile(join(MUSIC_DIR, f))])

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

        font.setPointSize(16)

        self.startButton.setFont(font)
        self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startButton.setToolTipDuration(-4)
        self.startButton.setStyleSheet("background-color: green; color: white;")
        self.startButton.setDefault(False)
        self.startButton.setObjectName("startButton")
        self.startButton.clicked.connect(self.start_timer)

        self.verticalLayout.addWidget(self.startButton)

        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.timer = QtWidgets.QLabel(self.horizontalLayoutWidget_2)

        font.setFamily("Hack")
        font.setPointSize(48)

        self.timer.setFont(font)
        self.timer.setStyleSheet("color:white;")
        self.timer.setAlignment(QtCore.Qt.AlignCenter)
        self.timer.setObjectName("timer")

        self.verticalLayout_2.addWidget(self.timer)

        self.tableUserData = QtWidgets.QTableView(self.horizontalLayoutWidget_2)
        self.tableUserData.setFont(font)
        self.tableUserData.setStyleSheet("background-color:rgb(211, 215, 207); color: black;")
        self.tableUserData.setSortingEnabled(True)
        self.tableUserData.setObjectName("tableUserData")

        self.verticalLayout_2.addWidget(self.tableUserData)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.setCentralWidget(self.central_widget)

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 860, 29))
        self.menubar.setStyleSheet("""color: white;
                                    QMenu {
                                        background-color: rgb(190, 206, 221);
                                        border: 1px solid black;
                                    }""")
        self.menubar.setObjectName("menubar")

        self.users = QtWidgets.QMenu(self.menubar)
        self.users.setObjectName("users")

        self.settings_menu = QtWidgets.QMenu(self.menubar)
        self.settings_menu.setObjectName("settings_menu")

        self.about_menu = QtWidgets.QMenu(self.menubar)
        self.about_menu.setObjectName("about_menu")

        self.about_timetracker = QtWidgets.QAction(QtGui.QIcon(IMAGES_DIR + 'about_timetraker.png'), 'О Timetracker',
                                                   self)
        self.about_timetracker.setStatusTip('Информация о приложении')
        self.about_timetracker.triggered.connect(self.create_about_window)

        self.about_qt = QtWidgets.QAction(self)
        self.about_qt.setStatusTip("Информация о используемой версии Qt")
        self.about_qt.triggered.connect(lambda: QtWidgets.QMessageBox.aboutQt(self))

        self.about_menu.addAction(self.about_timetracker)
        self.about_menu.addAction(self.about_qt)
        self.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.new_user = QtWidgets.QAction(self)
        self.new_user.setObjectName("new_user")
        self.new_user.setShortcut("Ctrl+N")
        self.new_user.setStatusTip("Создать нового пользователя")
        self.new_user.triggered.connect(self.create_new_user_window)

        self.select_user = QtWidgets.QAction(self)
        self.select_user.setObjectName("select_user")
        self.select_user.setShortcut("Ctrl+O")
        self.select_user.setStatusTip("Выбор текущего пользователя")
        self.select_user.triggered.connect(self.create_select_user_window)

        self.exit = QtWidgets.QAction(self)
        self.exit.setShortcut("Ctrl+Q")
        self.exit.setObjectName("exit")
        self.exit.setStatusTip('Выйти из приложения')
        self.exit.triggered.connect(self.close)

        self.view_action = QtWidgets.QAction(self)
        self.view_action.setObjectName("action")
        self.language_action = QtWidgets.QAction(self)
        self.language_action.setObjectName("language_action")
        self.additionally_action = QtWidgets.QAction(self)
        self.additionally_action.setObjectName("additionally_action")

        self.users.addSeparator()
        self.users.addAction(self.new_user)
        self.users.addSeparator()
        self.users.addAction(self.select_user)
        self.users.addSeparator()
        self.users.addAction(self.exit)

        self.settings_menu.addAction(self.view_action)
        self.settings_menu.addAction(self.language_action)
        self.settings_menu.addAction(self.additionally_action)

        self.menubar.addAction(self.users.menuAction())
        self.menubar.addAction(self.settings_menu.menuAction())
        self.menubar.addAction(self.about_menu.menuAction())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()

    def create_select_user_window(self):
        """create select window object"""
        self.select_user_window.show()

    def create_new_user_window(self):
        """create new window object"""
        self.new_user_window.show()

    def create_about_window(self):
        self.about_window.show()

    def start_timer(self):
        """Run when timer started"""
        time_start = datetime.now()
        counter = self.setTime.time().toString()
        counter = datetime.strptime(counter, "%H:%M:%S")

        def handler(select_signal, timer_text, window):
            """Handler function for one tick timer"""
            nonlocal counter
            counter -= timedelta(seconds=1)
            self.update_time(counter.strftime("%H:%M:%S"))
            if counter.second <= 0 and counter.minute <= 0 and counter.hour <= 0:
                player = MediaPlayer(MUSIC_DIR + "{}.mp3".format(select_signal.currentText()))
                player.play()
                timer.stop()
                timer.deleteLater()
                time_end = datetime.now()
                db_connect = Database()
                db_connect.create_track(time_start, time_end, timer_text.toPlainText())
                QtWidgets.QMessageBox.about(window, "Timetracker", "Время вышло")
                player.stop()

        timer = QtCore.QTimer()
        timer.timeout.connect(
            lambda select_signal=self.selectSignal, timer_text=self.timer_text, window=self: handler(select_signal,
                                                                                                     timer_text,
                                                                                                     window))
        timer.start(1000)

    def update_time(self, time):
        """Update time in time label"""
        self.timer.setText(time)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "TimeTracker v.1.0"))
        self.timerInnerLabel.setText(_translate("MainWindow", "Содержимое таймера:"))
        self.timer_text.setPlaceholderText(_translate("MainWindow", "Пишите здесь..."))
        self.timeLabel.setText(_translate("MainWindow", "Время"))
        self.soundLabel.setText(_translate("MainWindow", "Звук"))
        self.volumeLabel.setText(_translate("MainWindow", "Громкость"))
        self.startButton.setText(_translate("MainWindow", "START"))
        self.timer.setText(_translate("MainWindow", "00:00:00"))
        self.users.setTitle(_translate("MainWindow", "Пользователи"))
        self.settings_menu.setTitle(_translate("MainWindow", "Настройки"))
        self.about_menu.setTitle(_translate("MainWindow", "О программе"))
        self.about_qt.setText(_translate("MainWindow", "О Qt"))
        self.new_user.setText(_translate("MainWindow", "Новый пользователь"))
        self.select_user.setText(_translate("MainWindow", "Выбрать пользователя"))
        self.exit.setText(_translate("MainWindow", "Выход"))
        self.view_action.setText(_translate("MainWindow", "Вид"))
        self.language_action.setText(_translate("MainWindow", "Язык"))
        self.additionally_action.setText(_translate("MainWindow", "Дополнительно"))
