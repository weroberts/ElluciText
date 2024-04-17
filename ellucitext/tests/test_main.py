from gui.builder.code_editor_builder import CodeEditorBuilder

def test_main_window_displayed(qapp):
    editor = CodeEditorBuilder().build("ElluciText", 800, 600)
    editor.show()
    assert editor.isVisible()

def test_maximize_application(qapp):
    editor = CodeEditorBuilder().build("ElluciText", 800, 600)
    editor.show()
    editor.showMaximized()
    assert editor.isMaximized()

def test_minimize_application(qapp):
    editor = CodeEditorBuilder().build("ElluciText", 800, 600)
    editor.show()
    editor.showMinimized()
    assert editor.isMinimized()
