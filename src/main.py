import sys
from PySide6.QtWidgets import QApplication
from codeeditor import CodeEditor

if __name__ == "__main__":
    app = QApplication([])
    editor = CodeEditor()
    editor.setWindowTitle("ElluciText")
    editor.show()
    sys.exit(app.exec())