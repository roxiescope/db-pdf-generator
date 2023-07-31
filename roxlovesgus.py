'''
Objective:
1. Read data from database
2. Convert to readable markdown format
3. Convert to readable (and format-able) pdf format
    - allow user to customize font/size/color
'''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, \
    QVBoxLayout, QGridLayout, QLabel, QLineEdit, QFormLayout, QCheckBox, QDialog, QFileDialog
from PyQt5.QtCore import Qt


__version__ = '0.1'

from Settings import MSettings
import Settings

ERROR_MSG = 'ERROR'

class MaeveUI(QMainWindow):
    def __init__(self):
        super().__init__()
        # Variables to track which windows are open
        self.settings_open = False
        self.Maeve_open = False
        self.Todo_open = False
        self.Reading_open = False
        # Setting window color based on theme from settings
        self.setBaseSize(300, 300)
        self.setStyleSheet(Settings.get_theme('background_color'))
        self.setWindowTitle('Rox Loves Gus')
        # Central widget and general layout of window
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # List of windows created
        self.dialogs = list()
        # Display and buttons
        self._createButtons()

    def _createButtons(self):
        buttonsLayout = QFormLayout()

        settingsButton = QPushButton("Settings")
        settingsButton.setStyleSheet(Settings.get_theme("button_color"))
        settingsButton.setFixedSize(200, 40)
        mdSearchButton = QPushButton("Browse")
        mdSearchButton.setStyleSheet(Settings.get_theme("text_color"))
        mdSearchButton.setFixedSize(200, 40)
        pdfSearchButton = QPushButton("Browse")
        pdfSearchButton.setStyleSheet(Settings.get_theme("text_color"))
        pdfSearchButton.setFixedSize(200, 40)
        generate = QPushButton("Generate")
        generate.setStyleSheet(Settings.get_theme("button_color"))
        generate.setFixedSize(200, 40)


        mdCheckL = QLabel("generate markdown file")
        mdCheckL.setStyleSheet(Settings.get_theme("text_color"))
        mdPathL = QLabel("markdown output location")
        mdPathL.setStyleSheet(Settings.get_theme("text_color"))
        mdNameL = QLabel("markdown file name")
        mdNameL.setStyleSheet(Settings.get_theme("text_color"))
        pdfCheckL = QLabel("generate PDF file")
        pdfCheckL.setStyleSheet(Settings.get_theme("text_color"))
        pdfPathL = QLabel("pdf output location")
        pdfPathL.setStyleSheet(Settings.get_theme("text_color"))
        pdfNameL = QLabel("pdf file name")
        pdfNameL.setStyleSheet(Settings.get_theme("text_color"))

        mdCheck = QCheckBox()
        mdCheck.setStyleSheet(Settings.get_theme("text_color"))
        mdPath = QLineEdit()
        mdPath.setStyleSheet(Settings.get_theme("open_item_color"))
        mdName = QLineEdit()
        mdName.setStyleSheet(Settings.get_theme("open_item_color"))
        pdfCheck = QCheckBox()
        pdfCheck.setStyleSheet(Settings.get_theme("text_color"))
        pdfPath = QLineEdit()
        pdfPath.setStyleSheet(Settings.get_theme("open_item_color"))
        pdfName = QLineEdit()
        pdfName.setStyleSheet(Settings.get_theme("open_item_color"))


        buttonsLayout.addRow("", settingsButton)
        buttonsLayout.addRow(mdCheckL, mdCheck)
        buttonsLayout.addRow(mdPathL, mdPath)
        buttonsLayout.addRow("", mdSearchButton)
        buttonsLayout.addRow(mdNameL, mdName)
        buttonsLayout.addRow(pdfCheckL, pdfCheck)
        buttonsLayout.addRow(pdfPathL, pdfPath)
        buttonsLayout.addRow("", pdfSearchButton)
        buttonsLayout.addRow(pdfNameL, pdfName)
        buttonsLayout.addRow("", generate)
        buttonsLayout.setAlignment(Qt.AlignRight)

        self.generalLayout.addLayout(buttonsLayout)
        # mdSearchButton.clicked.connect(self.browseFiles())
        settingsButton.clicked.connect(self.settings_clicked)
        generate.clicked.connect(self.generate_clicked)

    def settings_clicked(self):
        if self.settings_open:
            print("Settings is already open")
        else:
            self.settings_dialog = MSettings()
            self.dialogs.append(self.settings_dialog)
            self.settings_dialog.location_on_the_screen()
            self.settings_dialog.show()
            self.settings_open = True
            self.settings_dialog.theme_changed.connect(self.reload_windows)
            self.settings_dialog.window_closed.connect(self.settings_closed)

    def generate_clicked(self):
        print("generate files")

    def settings_closed(self):
        self.settings_open = False

    def closeEvent(self, event):
        for window in QApplication.topLevelWidgets():
            window.close()

    def reload_windows(self):
        if self.settings_open:
            self.settings_dialog.close()
            self.settings_open = False
            self.settings_clicked()
        if self.Maeve_open:
            d = self._centralWidget.children()
            e = reversed(d)

            for g in e:
                g.deleteLater()
            self.setStyleSheet(Settings.get_theme('background_color'))
            self.setWindowTitle('Maeve')
            # Central widget and general layout of window
            self.generalLayout = QVBoxLayout()
            self._centralWidget = QWidget(self)
            self.setCentralWidget(self._centralWidget)
            self._centralWidget.setLayout(self.generalLayout)
            self.dialogs = list()
            # Display and buttons
            self._createButtons()

    def browseFiles(self):
        fname = QFileDialog.getOpenFileName(self, 'Open Folder','./')
        print(str(fname))
        # self.filename.setText(fname[0])

def main():
    # todo: make app run in taskbar
    # check if any items are past due on startup
    # check if toast_test.py is running
    # if it is: do nothing
    # if it isn't: start it up
    maeve = QApplication(sys.argv)
    maeve.setStyle("Fusion")
    view = MaeveUI()
    view.show()
    view.Maeve_open = True
    sys.exit(maeve.exec_())

if __name__ == '__main__':
    main()
