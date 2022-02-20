from PyQt5.QtGui import QFont, QTextLine
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from PyQt5 import QtWidgets
from dataclasses import *

from data_handling import get_mat_names




def build_mats_vlayout() -> QVBoxLayout:
    layout = QVBoxLayout()
    mats_names = get_mat_names()
    for mat_name in mats_names:
        layout.addWidget(build_hbox(mat_name))
    return layout

def build_hbox(name:str):
    inner_box = QHBoxLayout()
    label = QLabel(name)
    #label.setMinimumWidth(60)
    #label.setMinimumHeight(25)
    label.adjustSize()
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    label.setStyleSheet("background-color: lightgray; border: none; font-size: 15px;")

    inner_box.addWidget(label)

    text_box = QLineEdit()
    text_box.setText("0")
    text_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
    text_box.setStyleSheet("background-color: lightgray; font-size: 15px;")

    inner_box.addWidget(text_box)

    box = QFrame()
    box.setLayout(inner_box)
    box.setStyleSheet("QFrame {background-color: lightgray; border-width: 1; border-radius: 3; border-style: solid; border-color: rgb(10, 10, 10)}")
    return box
