from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from PyQt5 import QtWidgets
from testing import program_exit
from gui_support import *

def get_central_widget() -> QWidget:
    w = QtWidgets.QWidget()

    label = QtWidgets.QLabel("Write the quantity of each material needed by the foot.")
    buttonC = QtWidgets.QPushButton("Calculate")
    buttonU = QtWidgets.QPushButton("Update Materials")

    left_verticallayout = build_mats_vlayout()
    right_gridlayout = QVBoxLayout()
    totals_display = QPlainTextEdit()
    totals_display.setPlainText("Waiting on calculation...")
    totals_display.setStyleSheet("background-color: white; font-size: 15px;")
    totals_display.setReadOnly(True)
    Tscroll = QScrollArea()
    Tscroll.setWidget(totals_display)
    Tscroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
    Tscroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    Tscroll.setWidgetResizable(True)
    Tscroll.setStyleSheet("QScrollBar {background-color : lightgray;} QScrollBar::handle {background : LightGray;} QScrollBar::handle::pressed {background : SlateGray;}")

    right_gridlayout.addWidget(Tscroll)
    total_display = QLineEdit()
    total_display.setText("Total pending...")
    total_display.setStyleSheet("background-color: white; font-size: 20px; border: solid 1px black")
    total_display.setReadOnly(True)
    right_gridlayout.addWidget(total_display)


    left_widget = QtWidgets.QWidget()
    left_widget.setContentsMargins(0, 0, 0, 0)
    vbox = QtWidgets.QVBoxLayout(left_widget)
    vbox.setContentsMargins(0, 0, 0, 0)
    vbox.addWidget(label)

    button_and_lineedit_container = QtWidgets.QWidget()
    hlay_2 = QtWidgets.QHBoxLayout(button_and_lineedit_container)
    hlay_2.setContentsMargins(0, 0, 0, 0)
    hlay_2.addWidget(buttonC)
    hlay_2.addWidget(buttonU, stretch=1)
    vbox.addWidget(button_and_lineedit_container)
    bottom_container = QtWidgets.QWidget()
    bottom_container.setContentsMargins(0, 0, 0, 0)
    bottom_container.setLayout(left_verticallayout)

    scroll = QScrollArea()
    scroll.setWidget(bottom_container)
    scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
    scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    scroll.setWidgetResizable(True)
    #scroll.setStyleSheet("QScrollBar {background : DarkSlateBlue;} QScrollBar::handle {background : LightSeaGreen;} QScrollBar::handle::pressed {background : DarkGreen;}")

    vbox.addWidget(scroll, stretch=1)

    right_widget = QtWidgets.QWidget()
    right_widget.setLayout(right_gridlayout)

    hlay = QtWidgets.QHBoxLayout(w)
    hlay.addWidget(left_widget, stretch=1)
    hlay.addWidget(right_widget, stretch=2)

    bottom_container.setStyleSheet("background-color:Moccasin;")
    right_widget.setStyleSheet("background-color:Moccasin; border: solid 1px black;")

    w.resize(640, 480)
    return w