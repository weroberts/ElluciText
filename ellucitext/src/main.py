import sys
from PySide6.QtWidgets import QApplication
from gui.builder.code_editor_builder import CodeEditorBuilder
from gui.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication([])
    editor = CodeEditorBuilder().build("ElluciText", 800, 600)
    editor.show()
    MainWindow().show()
    sys.exit(app.exec())
