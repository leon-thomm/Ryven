# from PySide2.QtWidgets import ...
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap, QPainter, QPen, QColor, QBrush

from PySide2.QtWidgets import QWidget, QVBoxLayout, QLabel

import random


class PointsField_NodeInstance_MainWidget(QWidget):
    def __init__(self, parent_node_instance):
        super(PointsField_NodeInstance_MainWidget, self).__init__()

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

        painter = QPainter(self.label.pixmap())

        painter.setPen(QPen('#333333'))
        painter.setBrush(QColor('#333333'))
        painter.drawRect(self.rect())

        pen = QPen(QColor(255, 255, 255))
        painter.setPen(pen)
        painter.setBrush(QBrush(Qt.white))

        for i in range(num_points):
            x = random.randint(0, self.label.pixmap().width())
            y = random.randint(0, self.label.pixmap().height())
            self.points.append({'x': x, 'y': y})
            painter.drawEllipse(x, y, 4, 4)

        self.repaint()
        
        return self.points

    def deleted(self):
        pass

    def get_data(self):
        return {}

    def set_data(self, data):
        # self.setText(data)
        pass
