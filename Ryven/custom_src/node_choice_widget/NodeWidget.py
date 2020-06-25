from PySide2.QtWidgets import QWidget, QLabel, QGridLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QStyleOption, QStyle
from PySide2.QtGui import QFont, QPainter
from PySide2.QtCore import Signal


class NodeWidget(QWidget):

    chosen = Signal()
    custom_focused_from_inside = Signal()

    def __init__(self, parent, node):  # , node_image):
        super(NodeWidget, self).__init__(parent)

        self.custom_focused = False
        self.custom_focused_stylesheet = '''
NodeWidget {
    border: 2px solid #49aeed;
    background-color: #246187;
}
        '''
        self.custom_unfocused_stylesheet = '''
NodeWidget {
    border: 2px solid #3d3d3d;
}
        '''
        self.contents_stylesheet = '''
QLabel {
    color: '''+node.color.name()+''';
    border: None;
    background: transparent;
}
QToolTip {
    background-color: #040f16;
    color: #3B9CD9;
    border: 2px solid #144a6b;
    border-radius: 3px;
    padding: 5px;
}
        '''

        # UI
        main_layout = QGridLayout()

        name_label = QLabel(node.title)
        name_label.setFont(QFont('Poppins', 12))

        package_name_layout = QHBoxLayout()

        package_name_label = QLabel(node.package)
        package_name_label.setFont(QFont('Arial', 8, italic=True))
        package_name_label.setStyleSheet('color: white;')

        package_name_layout_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        package_name_layout.addItem(package_name_layout_spacer)
        package_name_layout.addWidget(package_name_label)

        main_layout.addWidget(name_label, 0, 0)
        main_layout.addLayout(package_name_layout, 1, 0)


        # # ------------------------------------------
        # img_label = QLabel()
        # img_label.setStyleSheet('padding: 20px;')
        # pix = QPixmap(self.node_image)
        # img_label.setPixmap(pix)
        # main_layout.addWidget(img_label, 2, 0)
        # # ------------------------------------------


        self.setLayout(main_layout)


        main_layout.setVerticalSpacing(0)
        main_layout.setSpacing(0)
        self.setContentsMargins(-6, -6, -6, -6)
        main_layout.setContentsMargins(-6, -6, -6, -6)
        self.setToolTip(node.description)
        self.setStyleSheet(self.custom_unfocused_stylesheet+'\n'+self.contents_stylesheet)
        # self.setMinimumWidth(70)



    def mousePressEvent(self, event):
        self.custom_focused_from_inside.emit()

    def mouseReleaseEvent(self, event):
        if self.geometry().contains(self.mapToParent(event.pos())):
            self.chosen.emit()

    def set_custom_focus(self, new_focus):
        self.custom_focused = new_focus
        if new_focus:
            self.setStyleSheet(self.custom_focused_stylesheet + '\n' + self.contents_stylesheet)
        else:
            self.setStyleSheet(self.custom_unfocused_stylesheet + '\n' + self.contents_stylesheet)


    def paintEvent(self, event):  # just to enable stylesheets
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, o, p, self)