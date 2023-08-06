import sys
from PyQt5.QtCore import Qt
import config_reader
from PyQt5.QtWidgets import QMainWindow, QWidget, QLineEdit, QPushButton, \
    QCheckBox, QVBoxLayout, QLabel, QComboBox, QDesktopWidget, QFormLayout
from PyQt5 import QtCore

'''
Settings for:
Page size, color, margins

1. get values on the form and send them to setXML()
2. update the form values with getXML()
'''


def get_theme(attribute):
    thm_value = config_reader.getXML('theme')
    background_color = "background-color: white; color: black;"
    button_color = "background-color: gray; color: black;"
    unused_button_color = "background-color: gray; color: black; text-decoration: line-through"
    open_item_color = "background-color: gray; color: black;"
    completed_item_color = "background-color: dark-gray; color: white; text-decoration: line-through;"
    text_color = "color: black;"
    list_item_color = "QListWidget{color: black;}" \
                      "QListWidget QScrollBar{background : white;}" \
                      "QListView::item:selected{background: dark-gray; color: white;}"
    if thm_value == "light":
        background_color = "background-color: #c0c2ce; color: black;"
        button_color = "background-color: #e9e9ef; color: black;"
        open_item_color = "background-color: #e5e6eb; color: black;"
        completed_item_color = "background-color: #d2d4dc; color: black; text-decoration: line-through;"
        list_item_color = "QListWidget{color: black;}" \
                          "QListWidget QScrollBar{background : #c0c2ce;}" \
                          "QListView::item:selected{background: #d2d4dc; color: black;}"
        unused_button_color = "background-color: #b6b6c4; color: black; text-decoration: line-through;"
        text_color = "color: black;"
    elif thm_value == "dark":
        background_color = "background-color: #1e2020; color: white;"
        button_color = "background-color: #3b444b; color: white;"
        unused_button_color = "background-color: gray; color: black; text-decoration: line-through"
        open_item_color = "background-color: #232b2b; color: white;"
        completed_item_color = "background-color: #0e1111; color: white; text-decoration: line-through;"
        list_item_color = "QListWidget{color: white;}" \
                          "QListWidget QScrollBar{background : #1e2020; color: white;}" \
                          "QListView::item:selected{background: #232b2b; color: white;}"
        text_color = "color: white;"
    elif thm_value == "hawkeye":
        background_color = "background-color: #4a454f; color: #e2cfe6;"
        button_color = "background-color: #5f68ab; color: #cfd1e5;"
        open_item_color = "background-color: #bc8fc4; color: black;"
        completed_item_color = "background-color: #79519a; color: white;"
        list_item_color = "QListWidget{color: #e2cfe6;}" \
                          "QListWidget QScrollBar{background : #4a454f;}" \
                          "QListView::item:selected{background: #bc8fc4; color: black;}"
        unused_button_color = "background-color: #393e66; color: #cfd1e5; text-decoration: line-through;"
        text_color = "color: #e2cfe6;"
    elif thm_value == "daredevil":
        background_color = "background-color: #522022; color: #f4e4e5;"
        button_color = "background-color: #3a1618; color: #f4e4e5;"
        open_item_color = "background-color: #873438; color: #f4e4e5;"
        completed_item_color = "background-color: #ac4e48; color: #f4e4e5; text-decoration: line-through;"
        list_item_color = "QListWidget{color: #f4e4e5;}" \
                          "QListWidget QScrollBar{background : #522022;}" \
                          "QListView::item:selected{background: #873438; color: black;}"
        unused_button_color = "background-color: #230d0e; color: #f4e4e5; text-decoration: line-through;"
        text_color = "color: #f4e4e5;"
    elif thm_value == "cottage":
        background_color = "background-color: #4a3636; color: #d7bebe;"
        button_color = "background-color: #7b2727; color: #d7bebe;"
        unused_button_color = "background-color: #31413f; color: #d7bebe; text-decoration: line-through"
        open_item_color = "background-color: #819b97; color: black;"
        completed_item_color = "background-color: dark-gray; color: white; text-decoration: line-through;"
        text_color = "color: #d7bebe;"
        list_item_color = "QListWidget{color: #d7bebe;}" \
                          "QListWidget QScrollBar{background : #4a3636;}" \
                          "QListView::item:selected{background: #819b97; color: black;}"
    elif thm_value == "teal":
        background_color = "background-color: #007777; color: black;"
        button_color = "background-color: #004444; color: #e5f1f1"
        unused_button_color = "background-color: #003333; color: #e5f1f1; text-decoration: line-through"
        open_item_color = "background-color: #005555; color: black;"
        completed_item_color = "background-color: #003333; color: #e5f1f1; text-decoration: line-through;"
        text_color = "color: black;"
        list_item_color = "QListWidget{color: black;}" \
                          "QListWidget QScrollBar{background : #007777;}" \
                          "QListView::item:selected{background: #003333; color: #e5f1f1;}"
    elif thm_value == "pastel":
        background_color = "background-color: #f7cac9; color: black;"
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
        generalLayout = QFormLayout()
        # create widgets
        self.dataNameL = QLabel("Database Name:")
        self.dataName = QLineEdit()
        self.userNameL = QLabel("User:")
        self.userName = QLineEdit()
        self.hostNameL = QLabel("Host:")
        self.hostName = QLineEdit()
        self.passNameL = QLabel("Password:")
        self.passName = QLineEdit()
        self.portNameL = QLabel("User:")
        self.portName = QLineEdit()
        self.themeL = QLabel("App Theme:")
        self.theme = QComboBox()
        self.theme.addItems(["Light Mode", "Dark Mode", "Hawkeye", "Daredevil", "Cottage Life", "Teal", "Pastel"])

        self.dataNameL.setStyleSheet(get_theme('text_color'))
        self.dataName.setStyleSheet(get_theme('open_item_color'))
        self.userNameL.setStyleSheet(get_theme('text_color'))
        self.userName.setStyleSheet(get_theme('open_item_color'))
        self.hostNameL.setStyleSheet(get_theme('text_color'))
        self.hostName.setStyleSheet(get_theme('open_item_color'))
        self.passNameL.setStyleSheet(get_theme('text_color'))
        self.passName.setStyleSheet(get_theme('open_item_color'))
        self.portNameL.setStyleSheet(get_theme('text_color'))
        self.portName.setStyleSheet(get_theme('open_item_color'))

        # todo get a list of tags from the generator and provide a ton of checkboxes for them
        # weather_checkbox = QCheckBox("checkbox template")
        # weather_checkbox.setStyleSheet(get_theme('text_color'))
        self.themeL.setStyleSheet(get_theme('text_color'))
        self.theme.setStyleSheet(get_theme('open_item_color'))
        save = QPushButton('Save')
        save.setStyleSheet(get_theme('button_color'))

        # get current values
        self.get_Everything()

        # create layout and add widgets
        generalLayout.addRow(self.dataNameL, self.dataName)
        generalLayout.addRow(self.userNameL, self.userName)
        generalLayout.addRow(self.hostNameL, self.hostName)
        generalLayout.addRow(self.passNameL, self.passName)
        generalLayout.addRow(self.portNameL, self.portName)

        generalLayout.addRow(self.themeL, self.theme)
        generalLayout.addRow("", save)

        # set on-click actions
        self.theme.currentTextChanged.connect(self.set_Theme)
        save.clicked.connect(self.setEverything)
        # add everything into the window
        widget = QWidget()
        widget.setLayout(generalLayout)
        self.setCentralWidget(widget)

    def createButtons(self):
        print("creating buttons")
    def get_Everything(self):
        # database credentials
        self.dataName.setText(config_reader.getXML('database'))
        self.userName.setText(config_reader.getXML('user'))
        self.hostName.setText(config_reader.getXML('host'))
        self.passName.setText(config_reader.getXML('password'))
        self.portName.setText(config_reader.getXML('port'))
        # theme
        thm_value = config_reader.getXML('theme')
        if thm_value == "light":
            self.theme.setCurrentText("Light Mode")
        elif thm_value == "dark":
            self.theme.setCurrentText("Dark Mode")
        elif thm_value == "hawkeye":
            self.theme.setCurrentText("Hawkeye")
        elif thm_value == "daredevil":
            self.theme.setCurrentText("Daredevil")
        elif thm_value == "cottage":
            self.theme.setCurrentText("Cottage Life")
        elif thm_value == "teal":
            self.theme.setCurrentText("Teal")
        elif thm_value == "pastel":
            self.theme.setCurrentText("Pastel")
        else:
            print("get_Everything invalid value for theme")

    def location_on_the_screen(self):
        self.move(600, 400)

    def set_Theme(self, s):
        if s == "Light Mode":
            config_reader.setXML('theme', 'light')
        elif s == "Dark Mode":
            config_reader.setXML('theme', 'dark')
        elif s == "Hawkeye":
            config_reader.setXML('theme', 'hawkeye')
        elif s == "Daredevil":
            config_reader.setXML('theme', 'daredevil')
        elif s == "Cottage Life":
            config_reader.setXML('theme', 'cottage')
        elif s == "Teal":
            config_reader.setXML('theme', 'teal')
        elif s == "Pastel":
            config_reader.setXML('theme', 'pastel')
        else:
            print("invalid theme")
        self.theme_changed.emit()

    def setEverything(self):
        if self.dataName != "":
            config_reader.setXML('database', self.dataName.text())
        if self.userName != "":
            config_reader.setXML('user', self.userName.text())
        if self.hostName != "":
            config_reader.setXML('host', self.hostName.text())
        if self.passName != "":
            config_reader.setXML('password', self.passName.text())
        if self.portName != "":
            config_reader.setXML('port', self.portName.text())

    def closeEvent(self, event):
        self.window_closed.emit()
        event.accept()
        # event.ignore() # if you want the window to never be closed

