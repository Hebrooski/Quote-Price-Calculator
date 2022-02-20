from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import *
from materials import Material
from data_handling import *

class UpdateDialog(QDialog):

    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.materials = []
        self.setWindowTitle("Update Materials")
        self.vlayout = QVBoxLayout()
        self.instructions = QPlainTextEdit()
        self.instructions.setPlainText("Add Materials: Enter the name and price per foot of a material you'd like in the system.\n"
        "Update Material's Price: Enter the name of the material you would like to update, then enter the new price. \n"
        "Click \"Next\" if you wish to add more. Click \"Done\" if you are finished adding materials.")
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
        self.label2 = QLabel("Price:")
        self.typingBox.addWidget(self.label2)
        self.pricebox = QLineEdit()
        self.typingBox.addWidget(self.pricebox)

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
        if(not(self.namebox.text() == "") and not(self.pricebox.text() == "")):
            self.materials.append(Material(str.lower(self.namebox.text()),float(self.pricebox.text())))
            self.namebox.setText("")
            self.pricebox.setText("")

    def donePressed(self):
        if(not(self.namebox.text() == "") and not(self.pricebox.text() == "")):
            self.materials.append(Material(str.lower(self.namebox.text()),float(self.pricebox.text())))
        update_mats_file(self.materials)
        self.close()
        


