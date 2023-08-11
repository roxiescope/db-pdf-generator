import re
import sys
from PyQt5.QtCore import Qt
import config_reader
from PyQt5.QtWidgets import QMainWindow, QWidget, QLineEdit, QPushButton, \
    QCheckBox, QVBoxLayout, QLabel, QComboBox, QDesktopWidget, QFormLayout, QScrollArea
from PyQt5 import QtCore
import generator
from TagDialog import MTag

# 2-d list telling me the XML attribute and sub-attribute for every widget created
widgets = []



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
        self.setFixedSize(400, 600)
        self.scroll = QScrollArea()
        self.generalLayout = QFormLayout()
        # database credentials
        self.createDatabaseOptions()
        # font options
        self.createTextOptions()
        self.createBulletOptions()
        self.createH1Options()
        self.createH2Options()
        self.createH3Options()
        self.createH4Options()
        # page options
        self.createPageOptions()
        # tag options
        self.createTagOptions()
        # theme options
        self.createThemeOptions()

        save = QPushButton('Save')
        save.setStyleSheet(get_theme('button_color'))

        # create layout and add widgets

        self.generalLayout.addRow(save)
        self.addToWidgets("Save", "0")

        # set on-click actions
        self.theme.currentTextChanged.connect(self.set_Theme)
        save.clicked.connect(self.setEverything)
        self.tags.clicked.connect(self.getTags)

        # add everything into the window
        widget = QWidget()
        widget.setLayout(self.generalLayout)
        self.scroll.setWidget(widget)
        self.setCentralWidget(self.scroll)

    def createDatabaseOptions(self):
        attributes = config_reader.getXMLChildren("databaseCreds")
        title = QLabel("<b>" + config_reader.getXMLName("databaseCreds") + "</b>")
        title.setStyleSheet(get_theme('text_color'))
        self.generalLayout.addRow(title)
        self.addToWidgets("databaseCreds", "0")
        for x in attributes:
            label = QLabel(config_reader.getXMLName(x.tag))
            label.setStyleSheet(get_theme('text_color'))
            value = QLineEdit(x.text)
            value.setStyleSheet(get_theme('open_item_color'))
            self.generalLayout.addRow(label, value)
            self.addToWidgets("databaseCreds", x.tag)
            self.addToWidgets("databaseCreds", x.tag)

    def createTextOptions(self):
        attributes = config_reader.getXMLChildren("text")
        title = QLabel("<b>" + config_reader.getXMLName("text") + "</b>")
        title.setStyleSheet(get_theme('text_color'))
        self.generalLayout.addRow(title)
        self.addToWidgets("text", "0")
        for x in attributes:
            label = QLabel(config_reader.getXMLName(x.tag))
            label.setStyleSheet(get_theme('text_color'))
            value = QLineEdit(x.text)
            value.setStyleSheet(get_theme('open_item_color'))
            self.generalLayout.addRow(label, value)
            self.addToWidgets("text", x.tag)
            self.addToWidgets("text", x.tag)


    def getTags(self):
        # 1st column: id of relation, 2nd column: id of page, 3rd column: name of tag
        tags = generator.getTags()
        tagList = []

        for r in tags:
            if r[1] not in tagList:
                tagList.append(r[1])

        self.tagD = MTag(tagList)
        self.tagD.show()

    def getTheme(self):
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
        for x in range(self.generalLayout.count()):
            if self.generalLayout.itemAt(x).widget():
                w = self.generalLayout.itemAt(x).widget()
                if isinstance(w, QLineEdit):
                    y = widgets[x]
                    config_reader.setXML(str(y[0]), w.text(), str(y[1]))
        # todo - refresh pages
        self.theme_changed.emit()

    def closeEvent(self, event):
        self.window_closed.emit()
        event.accept()
        # event.ignore() # if you want the window to never be closed

    def createBulletOptions(self):
        attributes = config_reader.getXMLChildren("bullet")
        title = QLabel("<b>" + config_reader.getXMLName("bullet") + "</b>")
        title.setStyleSheet(get_theme('text_color'))
        self.generalLayout.addRow(title)
        self.addToWidgets("bullet", "0")
        for x in attributes:
            label = QLabel(config_reader.getXMLName(x.tag))
            label.setStyleSheet(get_theme('text_color'))
            value = QLineEdit(x.text)
            value.setStyleSheet(get_theme('open_item_color'))
            self.generalLayout.addRow(label, value)
            self.addToWidgets("bullet", x.tag)
            self.addToWidgets("bullet", x.tag)

    def createH1Options(self):
        attributes = config_reader.getXMLChildren("heading1")
        title = QLabel("<b>" + config_reader.getXMLName("heading1") + "</b>")
        title.setStyleSheet(get_theme('text_color'))
        self.generalLayout.addRow(title)
        self.addToWidgets("heading1", "0")
        for x in attributes:
            label = QLabel(config_reader.getXMLName(x.tag))
            label.setStyleSheet(get_theme('text_color'))
            value = QLineEdit(x.text)
            value.setStyleSheet(get_theme('open_item_color'))
            self.generalLayout.addRow(label, value)
            self.addToWidgets("heading1", x.tag)
            self.addToWidgets("heading1", x.tag)

    def createH2Options(self):
        attributes = config_reader.getXMLChildren("heading2")
        title = QLabel("<b>" + config_reader.getXMLName("heading2") + "</b>")
        title.setStyleSheet(get_theme('text_color'))
        self.generalLayout.addRow(title)
        self.addToWidgets("heading2", "0")
        for x in attributes:
            label = QLabel(config_reader.getXMLName(x.tag))
            label.setStyleSheet(get_theme('text_color'))
            value = QLineEdit(x.text)
            value.setStyleSheet(get_theme('open_item_color'))
            self.generalLayout.addRow(label, value)
            self.addToWidgets("heading2", x.tag)
            self.addToWidgets("heading2", x.tag)

    def createH3Options(self):
        attributes = config_reader.getXMLChildren("heading3")
        title = QLabel("<b>" + config_reader.getXMLName("heading3") + "</b>")
        title.setStyleSheet(get_theme('text_color'))
        self.generalLayout.addRow(title)
        self.addToWidgets("heading3", "0")
        for x in attributes:
            label = QLabel(config_reader.getXMLName(x.tag))
            label.setStyleSheet(get_theme('text_color'))
            value = QLineEdit(x.text)
            value.setStyleSheet(get_theme('open_item_color'))
            self.generalLayout.addRow(label, value)
            self.addToWidgets("heading3", x.tag)
            self.addToWidgets("heading3", x.tag)

    def createH4Options(self):
        attributes = config_reader.getXMLChildren("heading4")
        title = QLabel("<b>" + config_reader.getXMLName("heading4") + "</b>")
        title.setStyleSheet(get_theme('text_color'))
        self.generalLayout.addRow(title)
        self.addToWidgets("heading4", "0")
        for x in attributes:
            label = QLabel(config_reader.getXMLName(x.tag))
            label.setStyleSheet(get_theme('text_color'))
            value = QLineEdit(x.text)
            value.setStyleSheet(get_theme('open_item_color'))
            self.generalLayout.addRow(label, value)
            self.addToWidgets("heading4", x.tag)
            self.addToWidgets("heading4", x.tag)

    def createPageOptions(self):
        attributes = config_reader.getXMLChildren("PageSettings")
        title = QLabel("<b>" + config_reader.getXMLName("PageSettings") + "</b>")
        title.setStyleSheet(get_theme('text_color'))
        self.generalLayout.addRow(title)
        self.addToWidgets("PageSettings", "0")
        for x in attributes:
            label = QLabel(config_reader.getXMLName(x.tag))
            label.setStyleSheet(get_theme('text_color'))
            value = QLineEdit(x.text)
            value.setStyleSheet(get_theme('open_item_color'))
            self.generalLayout.addRow(label, value)
            self.addToWidgets("PageSettings", x.tag)
            self.addToWidgets("PageSettings", x.tag)

    def createTagOptions(self):
        self.tags = QPushButton('Select Tags')
        self.tags.setStyleSheet(get_theme('button_color'))
        self.generalLayout.addRow(self.tags)
        self.addToWidgets("Tags", "0")

    def createThemeOptions(self):
        self.themeL = QLabel("App Theme:")
        self.theme = QComboBox()
        self.theme.addItems(["Light Mode", "Dark Mode", "Hawkeye", "Daredevil", "Cottage Life", "Teal", "Pastel"])
        self.themeL.setStyleSheet(get_theme('text_color'))
        self.theme.setStyleSheet(get_theme('open_item_color'))
        self.getTheme()
        self.generalLayout.addRow(self.themeL, self.theme)
        self.addToWidgets("Theme", "0")
        self.addToWidgets("Theme", "0")

    def addToWidgets(self, att, sub):
        xmlref = [att, sub]
        widgets.append(xmlref)

