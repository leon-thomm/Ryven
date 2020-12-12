from NIWENV import *

# from PySide2.QtWidgets import ...
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap, QPainter, QPen, QColor, QBrush

from PySide2.QtWidgets import QWidget, QVBoxLayout, QLabel

from PySide2.QtWidgets import QWidget



class %CLASS%(QWidget, MWB):
    def __init__(self, params):
        MWB.__init__(self, params)
        QWidget.__init__(self)

        

        self.setStyleSheet('''
background-color: #0C1C23;
border: none;
        ''')

        self.setLayout(QVBoxLayout())
        self.label = QLabel()
        pix = QPixmap(200, 200)
        self.label.setPixmap(pix)
        #self.setContentMargins(0)
        self.layout().addWidget(self.label)
        self.resize(200, 200)


    def show_points(self, points):
        painter = QPainter(self.label.pixmap())
        painter.setRenderHint(QPainter.Antialiasing)

        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor('#0C1C23'))
        painter.drawRect(self.rect())

        pen = QPen(QColor('#ffffff'))
        painter.setPen(pen)
        painter.setBrush(QBrush(QColor('#ffffff')))

        for p in points:
            painter.drawEllipse(p[0]*self.label.pixmap().width(), p[1]*self.label.pixmap().height(), 2, 2)

        self.repaint()


    def get_data(self):
        return {}

    def set_data(self, data):
        pass


    def remove_event(self):
        pass
