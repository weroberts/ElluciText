from PySide6.QtCore import Qt
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
        
    
        
    
