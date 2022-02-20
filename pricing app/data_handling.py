from PyQt5.QtWidgets import QLabel, QLineEdit, QPlainTextEdit, QVBoxLayout
from file_work import *
from materials import Material
filename = "supporting files/mats.txt"
mats = read_file_data(filename)

def get_mat_names() ->list[str]:
    mat_names = []
    mats = read_file_data(filename)
    for mat in mats:
        mat_names.append(str.title(mat.mat_name))
    return mat_names

def testing_input(display_box : QPlainTextEdit):
    display_box.setPlainText("pressed")

def mat_quantity(layout:QVBoxLayout,display_box:QPlainTextEdit,total_display:QLineEdit):
    output = ""
    totals = []
    totalFeet = 0
    for i in range(layout.count()):
        step = layout.itemAt(i)
        layer1 = step.widget()
        layer2 = layer1.layout()
        if(True):
            name = ""
            value = ""
            for v in range(layer2.count()):
                inner = layer2.itemAt(v).widget()
                if(isinstance(inner,QLineEdit)):
                    value = inner.text()
                if(isinstance(inner,QLabel)):
                    name = inner.text()
            if(not(value == "0") and not(value == "")):
                formated_string = display_totals_line(name,value)
                output = output + formated_string
                totals.append(float(formated_string.split("=")[1].replace("$","")))
    total = 0
    for tot in totals:
        total = total + tot
  #  total = total + (totalFeet*12)
    total_display.setText("$"+str(round(total,2)))
   # output = output + f"Wields: {totalFeet}ft x $1 = ${round(totalFeet*12,2)}\n"
    display_box.setPlainText(output)

def display_totals_line(name,value) -> str:
    output = ""
    for mat in mats:
        if(str.lower(name) == str.lower(mat.mat_name)):
            total = float(value)*float(mat.mat_price)
            if(str.lower(name) == "welds"):
                output = f"{name}: {value}in x ${mat.mat_price} = ${round(total,2)}\n"
            else:
                output = f"{name}: {value}ft x ${mat.mat_price} = ${round(total,2)}\n"
    return output

def update_mats_file(new_mats : list[Material]):
    for mat in new_mats:
        no_matches = True
        for mater in mats:
            if(mat.mat_name == mater.mat_name):
                mater.mat_price = mat.mat_price
                no_matches = False
        if(no_matches):
            mats.append(mat)
    override_file_data(filename,mats)

def delete_mats_file(mat_names : list[str]):
    for matName in mat_names:
        for mater in mats:
            if(matName == mater.mat_name):
                mats.remove(mater)
    override_file_data(filename,mats)
            
def get_names_listed(layout:QVBoxLayout) -> list[str]:
    names = []
    for i in range(layout.count()):
        step = layout.itemAt(i)
        layer1 = step.widget()
        layer2 = layer1.layout()
        for v in range(layer2.count()):
            inner = layer2.itemAt(v).widget()
            if(isinstance(inner,QLabel)):
                names.append(inner.text())
    return names

    