from custom_src.retain import M

# from PySide2.QtWidgets import ...
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap, QPainter, QPen, QColor, QBrush

from PySide2.QtWidgets import QWidget, QVBoxLayout, QLabel

from PySide2.QtWidgets import QWidget
import os


class %NODE_TITLE%_NodeInstance_MainWidget(QWidget):
    def __init__(self, parent_node_instance):
        super(%NODE_TITLE%_NodeInstance_MainWidget, self).__init__()

        # leave these lines ------------------------------
        self.parent_node_instance = parent_node_instance
        self.package_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../')
        # ------------------------------------------------

        self.setStyleSheet('''
            background-color: #333333;
        ''')

        self.setLayout(QVBoxLayout())
        self.label = QLabel()
        pix = QPixmap(200,200)
        self.label.setPixmap(pix)
        self.layout().addWidget(self.label)
        self.resize(200, 200)

        self.points = []


    def show_points(self, points):
        self.points = points

        painter = QPainter(self.label.pixmap())
        painter.setRenderHint(QPainter.Antialiasing)

        painter.setPen(QPen('#333333'))
        painter.setBrush(QColor('#333333'))
        painter.drawRect(self.rect())

        pen = QPen(QColor(255, 255, 255))
        painter.setPen(pen)
        painter.setBrush(QBrush(Qt.white))

        for p in self.points:
            painter.drawEllipse(p['x'], p['y'], 4, 4)

        self.repaint()


    def get_data(self):
        data = {'pints': self.points}
        # ...
        return data

    def set_data(self, data):
        self.points = data['points']


    def remove_event(self):
        pass
