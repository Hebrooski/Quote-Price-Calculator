from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import *
from materials import Material
from data_handling import *

class DeleteDialog(QDialog):

    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.materials = []
        self.setWindowTitle("Delete Materials")
        self.vlayout = QVBoxLayout()
        self.instructions = QPlainTextEdit()
        self.instructions.setPlainText("Remove Materials: Enter the name of a material you'd like deleted from the system.\n"
        "Click \"Next\" if you wish to delete more. Click \"Done\" if you are finished removing materials.")
        self.instructions.setReadOnly(True)
        self.instructions.setStyleSheet("border-color: solid 2px black; font-size: 15px; text-align: center;")
        self.instructions.setFixedWidth(720)
        self.instructions.setFixedHeight(120)
        self.vlayout.addWidget(self.instructions)

        self.typingBox = QHBoxLayout()
        self.label1 = QLabel("Name:")
        self.typingBox.addWidget(self.label1)
        self.namebox = QLineEdit()
        self.typingBox.addWidget(self.namebox)

        self.vlayout.addLayout(self.typingBox) 
        
        self.buttonbox = QHBoxLayout()
        self.nextbutton = QPushButton("Next")
        self.donebutton = QPushButton("Done")
        self.cancelbutton = QPushButton("Cancel")
        self.cancelbutton.clicked.connect(self.cancelPressed)
        self.nextbutton.clicked.connect(self.nextPressed)
        self.donebutton.clicked.connect(self.donePressed)
        self.buttonbox.addWidget(self.cancelbutton)
        self.buttonbox.addWidget(self.nextbutton)
        self.buttonbox.addWidget(self.donebutton)
        self.vlayout.addLayout(self.buttonbox)
        self.setLayout(self.vlayout)

    def cancelPressed(self):
        self.close()

    def nextPressed(self):
        if(not(self.namebox.text() == "")):
            self.materials.append((str.lower(self.namebox.text())))
            self.namebox.setText("")

    def donePressed(self):
        if(not(self.namebox.text() == "")):
            self.materials.append((str.lower(self.namebox.text())))
        delete_mats_file(self.materials)
        self.close()
        


