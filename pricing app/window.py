import sys
from tkinter import Image

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QToolBar
from PyQt5.QtGui import *
from centralW import CentralWidg
from update_dialog import UpdateDialog
from delete_dialog import DeleteDialog



class Window(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle('Quote Pricing')
        self.setCentralWidget(CentralWidg())
        self._createMenu()
        self.statusBar()
        self.setGeometry(500,250,1000,500)

    def _createMenu(self):
        self.menu = self.menuBar().addMenu("&Menu")
        #self.menu.addAction('&Exit', self.close)
        self.menu.addAction("Update Materials",self.updateDialog)
        self.menu.addAction("Delete Materials",self.deleteDialog)

    def updateDialog(self):
        updateDialog = UpdateDialog(parent = self)
        updateDialog.exec()

    def deleteDialog(self):
        deleteDialog = DeleteDialog()
        deleteDialog.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.setWindowIcon(QIcon("logo.png"))
    win.show()
    sys.exit(app.exec_())