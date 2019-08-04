# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class UiMainWindow(object):
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(884, 638)
        MainWindow.setMinimumSize(QtCore.QSize(860, 0))
        MainWindow.setAutoFillBackground(True)

        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("centralwidget")

        self.horizontal_layout_widget_2 = QtWidgets.QWidget(self.central_widget)
        self.horizontal_layout_widget_2.setGeometry(QtCore.QRect(50, 10, 781, 551))
        self.horizontal_layout_widget_2.setObjectName("horizontalLayoutWidget_2")

        self.horizontal_layout_2 = QtWidgets.QHBoxLayout(self.horizontal_layout_widget_2)
        self.horizontal_layout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout_2.setObjectName("horizontalLayout_2")

        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.setObjectName("horizontalLayout")

        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.vertical_layout.setObjectName("verticalLayout")

        self.timer_inner_label = QtWidgets.QLabel(self.horizontal_layout_widget_2)

        font = QtGui.QFont()
        font.setPointSize(16)

        self.timer_inner_label.setFont(font)
        self.timer_inner_label.setTextFormat(QtCore.Qt.PlainText)
        self.timer_inner_label.setAlignment(QtCore.Qt.AlignCenter)
        self.timer_inner_label.setObjectName("timerInnerLabel")

        self.vertical_layout.addWidget(self.timer_inner_label)

        self.timer_text = QtWidgets.QTextEdit(self.horizontal_layout_widget_2)

        font = QtGui.QFont()
        font.setPointSize(14)

        self.timer_text.setFont(font)
        self.timer_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.timer_text.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.timer_text.setObjectName("timerText")

        self.vertical_layout.addWidget(self.timer_text)

        self.line_2 = QtWidgets.QFrame(self.horizontal_layout_widget_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.vertical_layout.addWidget(self.line_2)

        self.time_label = QtWidgets.QLabel(self.horizontal_layout_widget_2)
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label.setObjectName("timeLabel")

        self.vertical_layout.addWidget(self.time_label)

        self.set_time = QtWidgets.QTimeEdit(self.horizontal_layout_widget_2)
        self.set_time.setObjectName("setTime")

        self.vertical_layout.addWidget(self.set_time)

        self.sound_label = QtWidgets.QLabel(self.horizontal_layout_widget_2)
        self.sound_label.setTextFormat(QtCore.Qt.AutoText)
        self.sound_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sound_label.setObjectName("soundLabel")

        self.vertical_layout.addWidget(self.sound_label)

        self.select_signal = QtWidgets.QComboBox(self.horizontal_layout_widget_2)
        self.select_signal.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.select_signal.setEditable(False)
        self.select_signal.setObjectName("selectSignal")

        self.vertical_layout.addWidget(self.select_signal)

        self.volume_label = QtWidgets.QLabel(self.horizontal_layout_widget_2)
        self.volume_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.volume_label.setStyleSheet("")
        self.volume_label.setAlignment(QtCore.Qt.AlignCenter)
        self.volume_label.setObjectName("volumeLabel")

        self.vertical_layout.addWidget(self.volume_label)

        self.volume = QtWidgets.QSlider(self.horizontal_layout_widget_2)
        self.volume.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.volume.setMinimum(0)
        self.volume.setMaximum(100)
        self.volume.setPageStep(1)
        self.volume.setOrientation(QtCore.Qt.Horizontal)
        self.volume.setInvertedAppearance(False)
        self.volume.setInvertedControls(False)
        self.volume.setObjectName("volume")

        self.vertical_layout.addWidget(self.volume)

        self.line = QtWidgets.QFrame(self.horizontal_layout_widget_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.vertical_layout.addWidget(self.line)

        self.start_button = QtWidgets.QPushButton(self.horizontal_layout_widget_2)

        font = QtGui.QFont()
        font.setPointSize(16)

        self.start_button.setFont(font)
        self.start_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_button.setStyleSheet("background-color: green;")
        self.start_button.setDefault(False)
        self.start_button.setObjectName("startButton")

        self.vertical_layout.addWidget(self.start_button)

        self.horizontal_layout.addLayout(self.vertical_layout)

        self.horizontal_layout_2.addLayout(self.horizontal_layout)

        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)

        self.horizontal_layout_2.addItem(spacer_item)
        self.vertical_layout_2 = QtWidgets.QVBoxLayout()
        self.vertical_layout_2.setObjectName("verticalLayout_2")
        self.timer = QtWidgets.QLabel(self.horizontal_layout_widget_2)

        font = QtGui.QFont()
        font.setFamily("Hack")
        font.setPointSize(48)

        self.timer.setFont(font)
        self.timer.setAlignment(QtCore.Qt.AlignCenter)
        self.timer.setObjectName("timer")

        self.vertical_layout_2.addWidget(self.timer)

        self.tableUserData = QtWidgets.QTableView(self.horizontal_layout_widget_2)

        font = QtGui.QFont()
        font.setPointSize(14)

        self.tableUserData.setFont(font)
        self.tableUserData.setSortingEnabled(True)
        self.tableUserData.setObjectName("tableUserData")

        self.vertical_layout_2.addWidget(self.tableUserData)
        self.horizontal_layout_2.addLayout(self.vertical_layout_2)

        MainWindow.setCentralWidget(self.central_widget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 884, 30))
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
        MainWindow.setWindowTitle(_translate("TimeTracker v.1.0", "TimeTracker v.1.0"))
        self.timer_inner_label.setText(_translate("Timer text", "Описание:"))
        self.time_label.setText(_translate("Time", "Время"))
        self.sound_label.setText(_translate("Sound", "Звук"))
        self.volume_label.setText(_translate("Volume", "Громкость"))
        self.start_button.setText(_translate("START", "ПУСК"))
        self.timer.setText(_translate("00:00:00", "00:00:00"))
        self.menu.setTitle(_translate("Users", "Пользователи"))
        self.menu_2.setTitle(_translate("Settings", "Настройки"))
        self.menu_3.setTitle(_translate("About TimeTracker", "О программе"))
        self.action_2.setText(_translate("New user", "Новый пользователь"))
        self.action_4.setText(_translate("Select user", "Выбрать пользователя"))
        self.action_5.setText(_translate("Exit", "Выход"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setup_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
