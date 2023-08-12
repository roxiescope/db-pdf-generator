from PyQt5.QtWidgets import QMainWindow, QWidget, QLineEdit, QPushButton, \
    QCheckBox, QVBoxLayout, QLabel, QComboBox, QDesktopWidget, QFormLayout
from PyQt5 import QtCore
import Settings
import config_reader, rlog
import re


class MTag(QMainWindow):
    window_closed = QtCore.pyqtSignal()
    theme_changed = QtCore.pyqtSignal()

    def __init__(self, tagList):
        super().__init__()
        # Default Theme
        # Main window properties
        self.setStyleSheet(Settings.get_theme('background_color'))
        self.setWindowTitle('Settings')
        self.setBaseSize(250, 300)
        generalLayout = QVBoxLayout()
        tagsXML = str(config_reader.getXML("tagsToInclude"))
        self.check = []

        self.title = QLabel("<b>Select which page tags to include in the export:</b>")
        self.title.setStyleSheet(Settings.get_theme('text_color'))
        generalLayout.addWidget(self.title)

        for x in tagList:
            self.check.append(QCheckBox(x))
            self.check[tagList.index(x)].setStyleSheet(Settings.get_theme('open_item_color'))
            # print(self.check[tagList.index(x)].text())
            if re.search(self.check[tagList.index(x)].text(), tagsXML):
                self.check[tagList.index(x)].setChecked(True)
            generalLayout.addWidget(self.check[tagList.index(x)])

        self.submit = QPushButton("Submit")
        self.submit.setStyleSheet(Settings.get_theme('button_color'))
        generalLayout.addWidget(self.submit)
        self.submit.clicked.connect(self.setTags)
        widget = QWidget()
        widget.setLayout(generalLayout)
        self.setCentralWidget(widget)
        self.move(900, 400)

    def setTags(self):
        tagSettings = []
        for x in self.check:
            if x.checkState() == 2:
                tagSettings.append(x.text())
        config_reader.setXML("tagsToInclude", str(tagSettings))
