from gui.code_editor import CodeEditor

class CodeEditorBuilder:
    def build(self, title, width, height):
        editor = CodeEditor()
        editor.setWindowTitle(title)
        editor.setGeometry(0, 0, width, height)
        return editor
