# from PySide2.QtWidgets import ...
# from PySide2.QtCore import ...
from PySide2.QtGui import QPixmap, QPainter, QPen, QColor

from PySide2.QtWidgets import QWidget, QVBoxLayout, QLabel

import random


class %NODE_TITLE%_NodeInstance_MainWidget(QWidget):
    def __init__(self, parent_node_instance):
        super(%NODE_TITLE%_NodeInstance_MainWidget, self).__init__()

        # leave these lines ------------------------------
        self.parent_node_instance = parent_node_instance
        # ------------------------------------------------

        self.setLayout(QVBoxLayout())
        self.label = QLabel()
        self.layout().addWidget(self.label)
        self.resize(300, 300)

        self.points = []

    def randomize(self, num_points):
        self.points.clear()
        
        pix = QPixmap(self.label.width(), self.label.height())
        painter = QPainter(pix)
        pen = QPen(QColor(255, 255, 255))
        painter.setPen(pen)
                    
        for i in range(num_points):
            x = random.randint(0, self.width())
            y = random.randint(0, self.height())
            self.points.append({'x': x, 'y': y})
            painter.drawEllipse(x, y, 3, 3)

        self.label.setPixmap(pix)

        return self.points

    def deleted(self):
        pass

    def get_data(self):
        return self.text()

    def set_data(self, data):
        self.setText(data)
