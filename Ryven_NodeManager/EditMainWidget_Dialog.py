from PySide2.QtWidgets import QSplitter, QTextEdit, QSizePolicy, QDialog, QGridLayout, QVBoxLayout, QHBoxLayout, QGroupBox, QScrollArea, QWidget, QCheckBox, QPushButton, QLabel, QLineEdit, QFileDialog, QDialogButtonBox
from PySide2.QtCore import Qt

from CodeEditor import CodeEditor


instructions_text = '''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;">
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:10pt; font-weight:600;">Instructions</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Programming a node's main widget is not very difficult.</p></body></html>
'''


class EditMainWidgetDialog(QDialog):
    def __init__(self, parent):
        super(EditMainWidgetDialog, self).__init__(parent)

        # create UI
        self.main_grid_layout = QGridLayout(self)

        main_vertical_splitter = QSplitter()
        main_vertical_splitter.setOrientation(Qt.Vertical)

        #   instructions and actions layout
        header_widget = QWidget()
        header_layout = QHBoxLayout()

        instructions_text_edit = QTextEdit()
        instructions_text_edit.setText(instructions_text)
        instructions_text_edit.setEnabled(False)

        reset_button = QPushButton()
        reset_button.setText('reset')
        reset_button.clicked.connect(self.reset)

        header_layout.addWidget(instructions_text_edit)
        header_layout.addWidget(reset_button)

        header_widget.setLayout(header_layout)


        main_vertical_splitter.addWidget(header_widget)

        #   code text edit
        self.code_text_edit = CodeEditor()
        self.code_text_edit.static_elements = ['def get_data(self):',
                                               'def set_data(self, data):',
                                               'class %NODE_TITLE%_NodeInstance_MainWidget',
                                               '''def __init__(self, parent_node_instance):
		super(%NODE_TITLE%_NodeInstance_MainWidget, self).__init__()'''
                                               ]
        self.code_text_edit.components = ['self.parent_node_instance',
                                          'self.parent_node_instance.update_shape()']
        main_vertical_splitter.addWidget(self.code_text_edit)



        self.main_grid_layout.addWidget(main_vertical_splitter)


        button_box = QDialogButtonBox()
        button_box.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        self.main_grid_layout.addWidget(button_box)

        self.setWindowTitle('Edit Source Code')
        self.resize(1300, 950)


        self.reset()


    def reset(self):
        # load template
        f = open('template files/main_widget_default_template.txt', 'r')
        self.code_text_edit.set_code(f.read())
        f.close()

    def set_code(self, code):
        self.code_text_edit.setPlainText(code)

    def get_code(self):
        return self.code_text_edit.toPlainText()