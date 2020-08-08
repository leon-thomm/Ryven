from NIWENV import *

# from PySide2.QtWidgets import ...
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap, QPainter, QPen, QColor, QBrush

from PySide2.QtWidgets import QWidget, QVBoxLayout, QLabel

import random


class %NODE_TITLE%_NodeInstance_MainWidget(QWidget):
    def __init__(self, parent_node_instance):
        super(%NODE_TITLE%_NodeInstance_MainWidget, self).__init__()

        # leave these lines ------------------------------
        self.parent_node_instance = parent_node_instance
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

    def randomize(self, num_points):
        self.points.clear()

        for i in range(num_points):
            x = random.randint(0, self.label.pixmap().width())
            y = random.randint(0, self.label.pixmap().height())
            self.points.append({'x': x, 'y': y})

        self.draw_points(self.points)

        return self.points

    def draw_points(self, points):
        painter = QPainter(self.label.pixmap())
        painter.setRenderHint(QPainter.Antialiasing)

        painter.setPen(QPen('#333333'))
        painter.setBrush(QColor('#333333'))
        painter.drawRect(self.rect())

        pen = QPen(QColor(255, 255, 255))
        painter.setPen(pen)
        painter.setBrush(QBrush(Qt.white))

        for p in points:
            painter.drawEllipse(p['x'], p['y'], 4, 4)

        self.repaint()

    def get_data(self):
        return {'points': self.points}

    def set_data(self, data):
        self.points = data['points']
        self.draw_points(self.points)


    def remove_event(self):
        pass
