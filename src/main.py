import sys
from PySide6.QtWidgets import QApplication
from code_editor import CodeEditor

if __name__ == "__main__":
    app = QApplication([])
    editor = CodeEditor()
    editor.setWindowTitle("ElluciText")
    editor.setGeometry(0, 0, 800, 600)
    editor.show()
    sys.exit(app.exec())
