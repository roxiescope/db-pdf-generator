import sys
from PyQt5.QtCore import Qt
import config_reader
from PyQt5.QtWidgets import QMainWindow, QWidget, QLineEdit, QPushButton, \
    QCheckBox, QVBoxLayout, QLabel, QComboBox, QDesktopWidget
from PyQt5 import QtCore

# TODO - option to open on startup

'''
Settings for:
Page size, color, margins

1. get values on the form and send them to setXML()
2. update the form values with getXML()
'''

global text
global heading1
global heading2
global heading3
global heading4
global PageSettings
global LayoutSettings


def setText(a, s, t=0):
    if t==0:
        print("missing requested value")
    elif a not in ('text', 'h1', 'h2', 'h3', 'h4'):
        print("missing requested attribute")
    else:
        if s=='font':
            config_reader.setXML(a,'font',t)
        elif s=='size':
            config_reader.setXML(a,'size',t)
        elif s=='color':
            config_reader.setXML(a,'color',t)
        else:
            print("attribute name not valid")

def setPage(s, t=0):
    if t==0:
        print("missing requested value")
    else:
        if s=='font':
            config_reader.setXML('font',t)
        elif s=='size':
            config_reader.setXML('size',t)
        elif s=='color':
            config_reader.setXML('color',t)
        else:
            print("attribute name not valid")

def setLayout(s, t=0):
    if t==0:
        print("missing requested value")
    else:
        if s=='font':
            config_reader.setXML('font',t)
        elif s=='size':
            config_reader.setXML('size',t)
        elif s=='color':
            config_reader.setXML('color',t)
        else:
            print("attribute name not valid")

def setTheme(s, t=0):
    if t==0:
        print("missing requested value")
    else:
        if s=='font':
            config_reader.setXML('font',t)
        elif s=='size':
            config_reader.setXML('size',t)
        elif s=='color':
            config_reader.setXML('color',t)
        else:
            print("attribute name not valid")

def get_Everything(thm):
    # weather value
    # weath_value = config_reader.getXML('weather')
    # if weath_value == str(0):
    #     weath.setCheckState(Qt.Unchecked)
    # elif weath_value == str(2):
    #     weath.setCheckState(Qt.Checked)
    # else:
    #     print("get_Everything invalid value for weather")
    # # banking value
    # bank_value = config_reader.getXML('banking')
    # if bank_value == str(0):
    #     bank.setCheckState(Qt.Unchecked)
    # elif bank_value == str(2):
    #     bank.setCheckState(Qt.Checked)
    # else:
    #     print("get_Everything invalid value for banking")
    # # to-do value
    # td_value = config_reader.getXML('todo')
    # if td_value == str(0):
    #     td.setCheckState(Qt.Unchecked)
    # elif td_value == str(2):
    #     td.setCheckState(Qt.Checked)
    # else:
    #     print("get_Everything invalid value for todo")
    # # reading value
    # read_value = config_reader.getXML('reading')
    # if read_value == str(0):
    #     read.setCheckState(Qt.Unchecked)
    # elif read_value == str(2):
    #     read.setCheckState(Qt.Checked)
    # else:
    #     print("get_Everything invalid value for reading")
    # # wardrobe value
    # ward_value = config_reader.getXML('wardrobe')
    # if ward_value == str(0):
    #     ward.setCheckState(Qt.Unchecked)
    # elif ward_value == str(2):
    #     ward.setCheckState(Qt.Checked)
    # else:
    #     print("get_Everything invalid value for wardrobe")
    # theme value
    thm_value = config_reader.getXML('theme')
    if thm_value == "light":
        thm.setCurrentText("Light Mode")
    elif thm_value == "dark":
        thm.setCurrentText("Dark Mode")
    elif thm_value == "hawkeye":
        thm.setCurrentText("Hawkeye")
    elif thm_value == "daredevil":
        thm.setCurrentText("Daredevil")
    elif thm_value == "cottage":
        thm.setCurrentText("Cottage Life")
    elif thm_value == "teal":
        thm.setCurrentText("Teal")
    elif thm_value == "pastel":
        thm.setCurrentText("Pastel")
    else:
        print("get_Everything invalid value for theme")

def get_theme(attribute):
    thm_value = config_reader.getXML('theme')
    background_color = "background-color: white;"
    button_color = "background-color: gray; color: black;"
    unused_button_color = "background-color: gray; color: black; text-decoration: line-through"
    open_item_color = "background-color: gray; color: black;"
    completed_item_color = "background-color: dark-gray; color: white; text-decoration: line-through;"
    text_color = "color: black;"
    list_item_color = "QListWidget{color: black;}" \
                      "QListWidget QScrollBar{background : white;}" \
                      "QListView::item:selected{background: dark-gray; color: white;}"
    if thm_value == "light":
        background_color = "background-color: #c0c2ce;"
        button_color = "background-color: #e9e9ef; color: black;"
        open_item_color = "background-color: #e5e6eb; color: black;"
        completed_item_color = "background-color: #d2d4dc; color: black; text-decoration: line-through;"
        list_item_color = "QListWidget{color: black;}" \
                          "QListWidget QScrollBar{background : #c0c2ce;}" \
                          "QListView::item:selected{background: #d2d4dc; color: black;}"
        unused_button_color = "background-color: #b6b6c4; color: black; text-decoration: line-through;"
        text_color = "color: black;"
    elif thm_value == "dark":
        background_color = "background-color: #1e2020;"
        button_color = "background-color: #3b444b; color: white;"
        unused_button_color = "background-color: gray; color: black; text-decoration: line-through"
        open_item_color = "background-color: #232b2b; color: white;"
        completed_item_color = "background-color: #0e1111; color: white; text-decoration: line-through;"
        list_item_color = "QListWidget{color: white;}" \
                          "QListWidget QScrollBar{background : #1e2020; color: white;}" \
                          "QListView::item:selected{background: #232b2b; color: white;}"
        text_color = "color: white;"
    elif thm_value == "hawkeye":
        background_color = "background-color: #4a454f;"
        button_color = "background-color: #5f68ab; color: #cfd1e5;"
        open_item_color = "background-color: #bc8fc4; color: black;"
        completed_item_color = "background-color: #79519a; color: white;"
        list_item_color = "QListWidget{color: #e2cfe6;}" \
                          "QListWidget QScrollBar{background : #4a454f;}" \
                          "QListView::item:selected{background: #bc8fc4; color: black;}"
        unused_button_color = "background-color: #393e66; color: #cfd1e5; text-decoration: line-through;"
        text_color = "color: #e2cfe6;"
    elif thm_value == "daredevil":
        background_color = "background-color: #522022;"
        button_color = "background-color: #3a1618; color: #f4e4e5;"
        open_item_color = "background-color: #873438; color: #f4e4e5;"
        completed_item_color = "background-color: #ac4e48; color: #f4e4e5; text-decoration: line-through;"
        list_item_color = "QListWidget{color: #f4e4e5;}" \
                          "QListWidget QScrollBar{background : #522022;}" \
                          "QListView::item:selected{background: #873438; color: black;}"
        unused_button_color = "background-color: #230d0e; color: #f4e4e5; text-decoration: line-through;"
        text_color = "color: #f4e4e5;"
    elif thm_value == "cottage":
        background_color = "background-color: #4a3636;"
        button_color = "background-color: #7b2727; color: #d7bebe;"
        unused_button_color = "background-color: #31413f; color: #d7bebe; text-decoration: line-through"
        open_item_color = "background-color: #819b97; color: black;"
        completed_item_color = "background-color: dark-gray; color: white; text-decoration: line-through;"
        text_color = "color: #d7bebe;"
        list_item_color = "QListWidget{color: #d7bebe;}" \
                          "QListWidget QScrollBar{background : #4a3636;}" \
                          "QListView::item:selected{background: #819b97; color: black;}"
    elif thm_value == "teal":
        background_color = "background-color: #007777;"
        button_color = "background-color: #004444; color: #e5f1f1"
        unused_button_color = "background-color: #003333; color: #e5f1f1; text-decoration: line-through"
        open_item_color = "background-color: #005555; color: black;"
        completed_item_color = "background-color: #003333; color: #e5f1f1; text-decoration: line-through;"
        text_color = "color: black;"
        list_item_color = "QListWidget{color: black;}" \
                          "QListWidget QScrollBar{background : #007777;}" \
                          "QListView::item:selected{background: #003333; color: #e5f1f1;}"
    elif thm_value == "pastel":
        background_color = "background-color: #f7cac9;"
        button_color = "background-color: #c5b9cd; color: black;"
        unused_button_color = "background-color: #92a8d1; color: black; text-decoration: line-through"
        open_item_color = "background-color: #dec2cb; color: black;"
        completed_item_color = "background-color: #abb1cf; color: black; text-decoration: line-through;"
        text_color = "color: black;"
        list_item_color = "QListWidget{color: black;}" \
                          "QListWidget QScrollBar{background : #f7cac9;}" \
                          "QListView::item:selected{background: #abb1cf; color: black;}"
    else:
        print("theme is fucked up")

    if attribute == "background_color":
        return background_color
    elif attribute == "button_color":
        return button_color
    elif attribute == "open_item_color":
        return open_item_color
    elif attribute == "completed_item_color":
        return completed_item_color
    elif attribute == "list_item_color":
        return list_item_color
    elif attribute == "text_color":
        return text_color
    elif attribute == "unused_button_color":
        return unused_button_color
    else:
        print("theme attribute doesn't exist")


class MSettings(QMainWindow):
    window_closed = QtCore.pyqtSignal()
    theme_changed = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        # Default Theme
        # Main window properties
        self.setStyleSheet(get_theme('background_color'))
        self.setWindowTitle('Settings')
        self.setBaseSize(180, 300)
        # create widgets
        displayed_label = QLabel("label template")
        weather_checkbox = QCheckBox("checkbox template")
        weather_zip = QLineEdit("line template")
        weather_zip_submit = QPushButton('button template')
        theme = QComboBox()
        theme.addItems(["Light Mode", "Dark Mode", "Hawkeye", "Daredevil", "Cottage Life", "Teal", "Pastel"])
        displayed_label.setStyleSheet(get_theme('text_color'))
        weather_checkbox.setStyleSheet(get_theme('text_color'))
        weather_zip.setStyleSheet(get_theme('open_item_color'))
        weather_zip_submit.setStyleSheet(get_theme('button_color'))
        theme.setStyleSheet(get_theme('open_item_color'))

        get_Everything(theme)

        # create layout and add widgets
        generalLayout = QVBoxLayout()
        generalLayout.addWidget(displayed_label)
        generalLayout.addWidget(weather_checkbox)
        generalLayout.addWidget(weather_zip)
        generalLayout.addWidget(weather_zip_submit)
        generalLayout.addWidget(theme)

        # set on-click actions
        # weather_checkbox.stateChanged.connect(setText)
        theme.currentTextChanged.connect(self.set_Theme)

        # add everything into the window
        widget = QWidget()
        widget.setLayout(generalLayout)
        self.setCentralWidget(widget)

    def location_on_the_screen(self):
        self.move(600, 400)

    def set_Theme(self, s):
        if s == "Light Mode":
            config_reader.setXML('theme', 0, 'light')
        elif s == "Dark Mode":
            config_reader.setXML('theme', 0, 'dark')
        elif s == "Hawkeye":
            config_reader.setXML('theme', 0, 'hawkeye')
        elif s == "Daredevil":
            config_reader.setXML('theme', 0, 'daredevil')
        elif s == "Cottage Life":
            config_reader.setXML('theme', 0, 'cottage')
        elif s == "Teal":
            config_reader.setXML('theme', 0, 'teal')
        elif s == "Pastel":
            config_reader.setXML('theme', 0, 'pastel')
        else:
            print("invalid theme")
        self.theme_changed.emit()

    def closeEvent(self, event):
        self.window_closed.emit()
        event.accept()
        # event.ignore() # if you want the window to never be closed

