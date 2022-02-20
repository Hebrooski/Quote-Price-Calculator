import sys
from materials import Material
from window import Window
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from gui_logic import GUILogic

print(Material("Poop",1))

app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())

# filename = "supporting files/mats.txt"
# mock_mats = [Material("Test1",50),Material("Test2",90)]
# override_file_data(filename,mock_mats)
# print(read_file_data(filename))