import json

from qtpy.QtWidgets import QLineEdit, QWidget, QLabel, QGridLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QStyleOption, QStyle
from qtpy.QtGui import QFont, QPainter, QColor, QDrag
from qtpy.QtCore import Signal, Qt, QMimeData, QByteArray


class NodeWidget(QWidget):

    chosen = Signal()
    custom_focused_from_inside = Signal()

    @staticmethod
    def _create_mime_data(node) -> QMimeData:
        mime_data = QMimeData()
        mime_data.setData('application/json', QByteArray(bytes(json.dumps(
                {
                    'type': 'node',
                    'node identifier': node.identifier,
                }
            ), encoding='utf-8')))
        return mime_data
    
    def __init__(self, parent, node):
        super(NodeWidget, self).__init__(parent)

        self.custom_focused = False
        self.node = node

        self.left_mouse_pressed_on_me = False

        # UI
        main_layout = QGridLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)

        self_ = self
        class NameLabel(QLineEdit):
            def __init__(self, text):
                super().__init__(text)

                self.setReadOnly(True)
                self.setFont(QFont('Source Code Pro', 8))
            def mouseMoveEvent(self, ev):
                self_.custom_focused_from_inside.emit()
                ev.ignore()
            def mousePressEvent(self, ev):
                ev.ignore()
            def mouseReleaseEvent(self, ev):
                ev.ignore()

        name_label = NameLabel(node.title)

        type_layout = QHBoxLayout()

        #type_label = QLabel(node.type_)
        #type_label.setFont(QFont('Segoe UI', 8, italic=True))
        # type_label.setStyleSheet('color: white;')

        main_layout.addWidget(name_label, 0, 0)
        #main_layout.addWidget(type_label, 0, 1)

        self.setLayout(main_layout)
        self.setContentsMargins(0, 0, 0, 0)
        self.setMaximumWidth(250)

        self.setToolTip(node.__doc__)
        self.update_stylesheet()


    def mousePressEvent(self, event):
        self.custom_focused_from_inside.emit()
        if event.button() == Qt.LeftButton:
            self.left_mouse_pressed_on_me = True

    def mouseMoveEvent(self, event):
        if self.left_mouse_pressed_on_me:
            drag = QDrag(self)
            mime_data = QMimeData()
            mime_data.setData('application/json', bytes(json.dumps(
                {
                    'type': 'node',
                    'node identifier': self.node.identifier,
                }
            ), encoding='utf-8'))
            drag.setMimeData(mime_data)
            drop_action = drag.exec_()

    def mouseReleaseEvent(self, event):
        self.left_mouse_pressed_on_me = False
        if self.geometry().contains(self.mapToParent(event.pos())):
            self.chosen.emit()

    def set_custom_focus(self, new_focus):
        self.custom_focused = new_focus
        self.update_stylesheet()

    def update_stylesheet(self):
        color = self.node.GUI.color if hasattr(self.node, 'GUI') else '#888888'

        r, g, b = QColor(color).red(), QColor(color).green(), QColor(color).blue()

        new_style_sheet = f'''
NodeWidget {{
    border: 1px solid rgba(255,255,255,150);
    border-radius: 2px;
    {(
        f'background-color: rgba(255,255,255,80);'
    ) if self.custom_focused else ''}
}}
QLabel {{
    background: transparent;
}}
QLineEdit {{
    background: transparent;
    border: none;
    padding: 2px;
}}
        '''

        self.setStyleSheet(new_style_sheet)

    def paintEvent(self, event):  # just to enable stylesheets
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, o, p, self)