from gui.builder.code_editor_builder import CodeEditorBuilder
from PySide6.QtWidgets import QApplication

app = QApplication([])

def test_main_window_displayed():
    editor = CodeEditorBuilder().build("ElluciText", 800, 600)
    editor.show()
    assert editor.isVisible()

def test_maximize_application():
    editor = CodeEditorBuilder().build("ElluciText", 800, 600)
    editor.show()
    editor.showMaximized()
    assert editor.isMaximized()

def test_minimize_application():
    editor = CodeEditorBuilder().build("ElluciText", 800, 600)
    editor.show()
    editor.showMinimized()
    assert editor.isMinimized()
