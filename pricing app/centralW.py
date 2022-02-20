from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from PyQt5 import QtWidgets
from gui_support import *
from data_handling import *
from functools import partial
from PyQt5.QtGui import *

class CentralWidg(QWidget):
    
    def __init__(self) -> None:
        super().__init__()
        self.widgets = []
        #label = QtWidgets.QLabel("Write the quantity of each material needed by the foot.")
        self.buttonC = QtWidgets.QPushButton("Calculate")
        self.buttonR = QtWidgets.QPushButton("Refresh")
        
        self.search_bar = ClickableLineEdit("Search...",self)
        self.search_bar.clicked.connect(self.searchClciked)
        self.search_bar.textEdited.connect(self.search)
        #self.search_bar.keyPressEvent
        self.search_bar.setStyleSheet("color:grey; border-color: solid 1px black; background-color: white;")

        self.left_verticallayout = build_mats_vlayout()
        self.right_gridlayout = QVBoxLayout()
        self.totals_display = QPlainTextEdit()
        self.totals_display.setPlainText("Waiting on calculation...")
        self.totals_display.setStyleSheet("background-color: white; font-size: 15px;")
        self.totals_display.setReadOnly(True)
        self.Tscroll = QScrollArea()
        self.Tscroll.setWidget(self.totals_display)
        self.Tscroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.Tscroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.Tscroll.setWidgetResizable(True)
        self.Tscroll.setStyleSheet("QScrollBar {background-color : lightgray;} QScrollBar::handle {background : LightGray;} QScrollBar::handle::pressed {background : SlateGray;}")

        self.right_gridlayout.addWidget(self.Tscroll)
        self.total_display = QLineEdit()
        self.total_display.setText("Total pending...")
        self.total_display.setStyleSheet("background-color: white; font-size: 20px; border-color: solid 1px black")
        self.total_display.setReadOnly(True)
        self.buttonC.clicked.connect(partial(mat_quantity,self.left_verticallayout,self.totals_display,self.total_display))
        self.buttonR.clicked.connect(self.refreshClicked)
        self.right_gridlayout.addWidget(self.total_display)

        self.left_widget = QtWidgets.QWidget()
        self.left_widget.setContentsMargins(0, 0, 0, 0)
        self.vbox = QtWidgets.QVBoxLayout(self.left_widget)
        self.vbox.setContentsMargins(0, 0, 0, 0)
        #vbox.addWidget(label)

        self.button_and_lineedit_container = QtWidgets.QWidget()
        
        #self.vbox.addWidget(self.search_bar)
        self.bottom_container = QtWidgets.QWidget()
        self.bottom_container.setContentsMargins(0, 0, 0, 0)
        self.bottom_container.setLayout(self.left_verticallayout)

        self.scroll = QScrollArea()
        self.scroll.setWidget(self.bottom_container)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        #scroll.setStyleSheet("QScrollBar {background : DarkSlateBlue;} QScrollBar::handle {background : LightSeaGreen;} QScrollBar::handle::pressed {background : DarkGreen;}")

        self.vbox.addWidget(self.scroll, stretch=1)
        self.hlay_2 = QtWidgets.QHBoxLayout(self.button_and_lineedit_container)
        self.hlay_2.setContentsMargins(0, 0, 0, 0)
        self.hlay_2.addWidget(self.buttonR)
        self.hlay_2.addWidget(self.buttonC)
        self.vbox.addWidget(self.button_and_lineedit_container)

        self.right_widget = QtWidgets.QWidget()
        self.right_widget.setLayout(self.right_gridlayout)

        self.hlay = QtWidgets.QHBoxLayout(self)
        self.hlay.addWidget(self.left_widget, stretch=1)
        self.hlay.addWidget(self.right_widget, stretch=2)

        self.bottom_container.setStyleSheet("background-color:Moccasin;")
        self.right_widget.setStyleSheet("background-color:Moccasin; border-color: solid 1px black;")

        self.resize(1040, 480)
        self.lastText = ""

    
    def keyPressEvent2(self, event: QKeyEvent) -> None:
        print(event.key())

    def refreshClicked(self):
        #left_verticallayout = build_mats_vlayout()
        current_names = (get_names_listed(self.bottom_container.layout()))
        new_current_names = (get_mat_names())
        #print(current_names)
        #print(new_current_names)
        for new_name in new_current_names:
            if(not(new_name in current_names)):
                self.bottom_container.layout().addWidget(build_hbox(new_name))
        for current_name in current_names:
            if(not(current_name in new_current_names)):
                widgets = []
                for i in range(self.bottom_container.layout().count()):
                    step = self.bottom_container.layout().itemAt(i)
                    layer1 = step.widget()
                    layer2 = layer1.layout()
                    for v in range(layer2.count()):
                        inner = layer2.itemAt(v).widget()
                        if(isinstance(inner,QLabel)):
                            if((str.lower(current_name) == str.lower(inner.text()))):
                                widgets.append(layer1)
                for widg in widgets:
                    self.bottom_container.layout().removeWidget(widg)


    def searchClciked(self):
        if(self.search_bar.text() == "Search..."):
            self.search_bar.setText("")
            self.search_bar.setStyleSheet("color:black; border-color: solid 1px black; background-color: white;")
    
    def search(self):
        if(not(len(self.lastText) > len(self.search_bar.text()))):
            self.lastText = self.search_bar.text()
            for i in range(self.bottom_container.layout().count()):
                step = self.bottom_container.layout().itemAt(i)
                layer1 = step.widget()
                layer2 = layer1.layout()
                for v in range(layer2.count()):
                    inner = layer2.itemAt(v).widget()
                    if(isinstance(inner,QLabel)):
                        if(not(str.lower(self.search_bar.text()) in str.lower(inner.text()))):
                            self.widgets.append(layer1)
            widgets = self.widgets
            for widg in widgets:
                self.bottom_container.layout().removeWidget(widg)
        else:
            widgets = self.widgets
            filter = self.search_bar.text()
            for widg in widgets:
                layer2 = widg.layout()
                for v in range(layer2.count()):
                    inner = layer2.itemAt(v).widget()
                    if(isinstance(inner,QLabel)):
                        print(str.lower(filter) in (str.lower(inner.text())))
                        if(str.lower(filter) in str.lower(inner.text())):
                            self.bottom_container.layout().addWidget(widg)
                            self.widgets.remove(widg)
        

    def searchReturn(self):
        #print(self.widgets)
        filter = self.search_bar.text()
        #new_current_names = (get_mat_names())
        for widg in self.widgets:
            layer2 = widg.layout()
            for v in range(layer2.count()):
                inner = layer2.itemAt(v).widget()
                if(isinstance(inner,QLabel)):
                    print(str.lower(filter) in (str.lower(inner.text())))
                    if(str.lower(filter) in str.lower(inner.text())):
                        self.bottom_container.layout().addWidget(widg)
                        self.widgets.remove(widg)

        

class ClickableLineEdit(QLineEdit):
    clicked = pyqtSignal() # signal when the text entry is left clicked
    def __init__(self,name,Cwidg) -> None:
        self.CWidg = Cwidg
        return super().__init__(name)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton: self.clicked.emit()
        else: super().mousePressEvent(event)

    # def keyPressEvent(self, event: QKeyEvent) -> None:
    #     if(event.key() == Qt.Key.Key_Backspace):
    #         self.CWidg.searchReturn()
    #     else:
    #         self.CWidg.search()
    #     return super().keyPressEvent(event)
