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
            QWidget {
                background-color: #333333;
            }
        ''')

        self.setLayout(QVBoxLayout())  # creating a layout - the widget must have one so that we can add stuff on top of it
        self.label = QLabel()  # creating a label for the pixmap to sit on
        pix = QPixmap(200,200)
        self.label.setPixmap(pix)
        self.layout().addWidget(self.label)  # adding the label with the pixmap to the layout
        self.resize(200, 200)

        self.points = []

    def randomize(self, num_points, relative_scale):
        self.points.clear()

        for i in range(num_points):
            x = random.uniform(0, 1)
            y = random.uniform(0, 1)
            if not relative_scale:
                x *= 200
                y *= 200
            self.points.append({'x': x, 'y': y})

        self.draw_points(self.points, 1 if not relative_scale else 200)

        return self.points

    def draw_points(self, points, mult):
        painter = QPainter(self.label.pixmap())  # initialize the painter with the pixmap, we want to draw on, so it will paint on that pixmap
        painter.setRenderHint(QPainter.Antialiasing)  # turn antialiasing on to make it look smooth

        painter.setPen(QPen('#333333'))  # set a pen color
        painter.setBrush(QColor('#333333'))  # same for 'brush'
        painter.drawRect(self.rect())  # the pixmap cannot have a transparent background, so we need to draw it's background manually with the background color of the widget (see style sheet above)

        pen = QPen(QColor(255, 255, 255))  # set pen color white
        painter.setPen(pen)
        painter.setBrush(QBrush(Qt.white))  # brush also white (fills the circle)

        for p in points:  # draw every point
            painter.drawEllipse(p['x']*mult, p['y']*mult, 4, 4)

    def get_data(self):
        return {'points': self.points}

    def set_data(self, data):
        self.points = data['points']
        self.draw_points(self.points)



    # optional - important for threading - stop everything here
    def removing(self):
        pass
