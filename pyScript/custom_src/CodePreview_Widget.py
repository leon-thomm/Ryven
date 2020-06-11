from PySide2.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QRadioButton, QLabel
from PySide2.QtGui import QFont
from PySide2.QtCore import QEvent
import inspect

from custom_src.CodePreview_TextEdit import CodePreview_TextEdit


class CodePreview_Widget(QWidget):
    def __init__(self):
        super(CodePreview_Widget, self).__init__()

        self.text_edit = CodePreview_TextEdit()
        self.code_obj = None

        settings_widget = QWidget()
        settings_layout = QHBoxLayout()
        info_label = QLabel('You can zoom!')
        info_label.setFont(QFont('Poppins', 8))
        settings_layout.addWidget(info_label)
        self.show_class_radio_button = QRadioButton('show whole class')
        self.show_class_radio_button.toggled.connect(self.show_class_button_toggled)
        show_update_event_radio_button = QRadioButton('only show update event')
        self.show_class_radio_button.setChecked(True)
        settings_layout.addWidget(self.show_class_radio_button)
        settings_layout.addWidget(show_update_event_radio_button)
        settings_widget.setLayout(settings_layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(settings_widget)
        main_layout.addWidget(self.text_edit)
        self.setLayout(main_layout)

        self.setStyleSheet('border: none;')

    def update_code(self, obj):
        if obj is None:  # no NI selected
            self.text_edit.setText('')
            return

        self.code_obj = obj
        if self.show_whole_class():
            self.text_edit.setText(inspect.getsource(obj.__class__))
        else:
            self.text_edit.setText(inspect.getsource(obj.__class__.update_event))

    def show_whole_class(self):
        return self.show_class_radio_button.isChecked()

    def show_class_button_toggled(self, event):
        self.update_code(self.code_obj)