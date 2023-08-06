'''
Objective:
1. Read data from database
2. Convert to readable markdown format
3. Convert to readable (and format-able) pdf format
    - allow user to customize font/size/color
'''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, \
    QVBoxLayout, QGridLayout, QLabel, QLineEdit, QFormLayout, QCheckBox, QMessageBox
from PyQt5.QtCore import Qt
from file_browser import FileBrowser
import generator
import config_reader


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

        # Setting window color based on theme from settings
        self.setBaseSize(400, 300)
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

        self.mdCheck = QCheckBox()
        self.mdPath = FileBrowser(0, FileBrowser.OpenDirectory)
        self.mdName = QLineEdit()
        self.pdfCheck = QCheckBox()
        self.pdfPath = FileBrowser(1, FileBrowser.OpenDirectory)
        self.pdfName = QLineEdit()

        self.warning = QMessageBox()
        self.warning.setStyleSheet(Settings.get_theme("background_color"))
        self.warning.setText("Make sure the file(s) exist in the directory you want before closing. "
                             "Depending on your settings the generator might take a while and "
                             "I don't have a progress bar yet love you")

        if config_reader.getXML('mdLastSetting') == '2':
            self.mdCheck.setChecked(True)
        if config_reader.getXML('pdfLastSetting') == '2':
            self.pdfCheck.setChecked(True)
        self.mdName.setText(config_reader.getXML('mdLastName'))
        self.pdfName.setText(config_reader.getXML('pdfLastName'))

        settingsButton = QPushButton("Settings")
        settingsButton.setStyleSheet(Settings.get_theme("button_color"))
        settingsButton.setFixedSize(200, 40)
        generate = QPushButton("Generate")
        generate.setStyleSheet(Settings.get_theme("button_color"))
        generate.setFixedSize(200, 40)

        mdCheckL = QLabel("generate markdown file")
        mdCheckL.setStyleSheet(Settings.get_theme("text_color"))
        mdPathL = QLabel("md output location")
        mdPathL.setStyleSheet(Settings.get_theme("text_color"))
        mdNameL = QLabel("markdown file name")
        mdNameL.setStyleSheet(Settings.get_theme("text_color"))
        pdfCheckL = QLabel("generate PDF file")
        pdfCheckL.setStyleSheet(Settings.get_theme("text_color"))
        pdfPathL = QLabel("pdf output location")
        pdfPathL.setStyleSheet(Settings.get_theme("text_color"))
        pdfNameL = QLabel("pdf file name")
        pdfNameL.setStyleSheet(Settings.get_theme("text_color"))

        self.mdCheck.setStyleSheet(Settings.get_theme("text_color"))
        self.mdPath.setStyleSheet(Settings.get_theme("open_item_color"))
        self.mdName.setStyleSheet(Settings.get_theme("open_item_color"))
        self.pdfCheck.setStyleSheet(Settings.get_theme("text_color"))
        self.pdfPath.setStyleSheet(Settings.get_theme("open_item_color"))
        self.pdfName.setStyleSheet(Settings.get_theme("open_item_color"))

        buttonsLayout.addRow("", settingsButton)
        buttonsLayout.addRow(mdCheckL, self.mdCheck)
        buttonsLayout.addRow(mdPathL, self.mdPath)
        buttonsLayout.addRow(mdNameL, self.mdName)
        buttonsLayout.addRow(pdfCheckL, self.pdfCheck)
        buttonsLayout.addRow(pdfPathL, self.pdfPath)
        buttonsLayout.addRow(pdfNameL, self.pdfName)
        buttonsLayout.addRow("", generate)
        # buttonsLayout.setLabelAlignment(Qt.AlignCenter)

        self.generalLayout.addLayout(buttonsLayout)
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
        x = self.warning.exec_()
        if self.mdCheck.checkState() == 2:
            generator.generateMarkdown(self.mdName.text(), self.mdPath.getPaths()[0], True)
        if self.pdfCheck.checkState() == 2:
            generator.generatePdf(self.pdfName.text(), self.pdfPath.getPaths()[0])

    def settings_closed(self):
        self.settings_open = False

    def closeEvent(self, event):
        # recording settings in config
        config_reader.setXML('mdLastSetting', str(self.mdCheck.checkState()))
        config_reader.setXML('mdLastName', str(self.mdName.text()))
        config_reader.setXML('pdfLastSetting', str(self.pdfCheck.checkState()))
        config_reader.setXML('pdfLastName', str(self.pdfName.text()))
        if len(self.mdPath.getPaths()) != 0:
            config_reader.setXML('mdLastDirectory', str(self.mdPath.getPaths()[0]))
        else:
            config_reader.setXML('mdLastDirectory', '[]')
        if len(self.pdfPath.getPaths()) != 0:
            config_reader.setXML('pdfLastDirectory', str(self.pdfPath.getPaths()[0]))
        else:
            config_reader.setXML('pdfLastDirectory', '[]')

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
            self.setWindowTitle('Rox Loves Gus')
            # Central widget and general layout of window
            self.generalLayout = QVBoxLayout()
            self._centralWidget = QWidget(self)
            self.setCentralWidget(self._centralWidget)
            self._centralWidget.setLayout(self.generalLayout)
            self.dialogs = list()
            # Display and buttons
            self._createButtons()


def main():
    maeve = QApplication(sys.argv)
    maeve.setStyle("Fusion")
    view = MaeveUI()
    view.show()
    view.Maeve_open = True
    sys.exit(maeve.exec_())

if __name__ == '__main__':
    main()
