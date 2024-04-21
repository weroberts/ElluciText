#from gui.builder.qaction_builder import QActionBuilder
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QFileDialog,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar
)
import sys


class QActionBuilder:
    def __init__(self, actionName, qMainWindow):
        self.qAction = QAction(actionName, qMainWindow)
        
    def connectAction(self, action):
        print(action)
        self.qAction.triggered.connect(action)
        return self.qAction
        
    def setShortcut(self, shortcutText):
        self.qAction.setShortcut(QKeySequence(keySequence))
        return self.qAction

class MainWindow(QMainWindow):

    def save(self):
        # Save the file if it has been previously saved, otherwise, call save_as
        if hasattr(self, 'current_file'):
            with open(self.current_file, 'w') as file:
                # Perform saving logic here
                file.write("This is a sample content.")
        else:
            self.saveAs()

    def saveAs(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt)")
        if file_name:
            self.current_file = file_name
            self.save()

    def __init__(self):
        super().__init__()

        print(self.save)
        saveAction = QActionBuilder("Save", self).connectAction(self.save).setShortcut("Ctrl+s")
        #self.buildAction("Save", self.save, "Ctrl+s")
        saveAsAction = self.buildAction("Save As...", self.saveAs, "Ctrl+alt+s")

        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        file_menu.addAction(saveAction)
        file_menu.addAction(saveAsAction)

    def buildAction(self, actionName, action, keySequence):
        qAction = QAction(actionName, self)
        qAction.triggered.connect(action)
        qAction.setShortcut(QKeySequence(keySequence))
        return qAction

      


