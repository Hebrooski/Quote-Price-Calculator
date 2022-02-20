from PyQt5.QtGui import QFont, QTextLine
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from PyQt5 import QtWidgets




def build_mats_vlayout() -> QVBoxLayout:
    layout = QVBoxLayout()
    mats_names = get_mats_names()
    for mat_name in mats_names:
        inner_box = QHBoxLayout()

        label = QLabel(mat_name)
        label.setFixedWidth(60)
        label.setFixedHeight(25)
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
        box.setStyleSheet("QFrame {background-color: lightgray;"
                                "border-width: 1;"
                                "border-radius: 3;"
                                "border-style: solid;"
                                "border-color: rgb(10, 10, 10)}")

        layout.addWidget(box)
    return layout
