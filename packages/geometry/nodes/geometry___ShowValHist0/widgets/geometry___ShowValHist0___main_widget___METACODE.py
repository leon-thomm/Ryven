from NIWENV import *

# from PySide2.QtWidgets import ...
from PySide2.QtCore import Qt
# from PySide2.QtGui import ...
from PySide2.QtGui import QPixmap, QPainter, QPen, QColor, QBrush

from PySide2.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QCheckBox, QLabel


class %CLASS%(QWidget, MWB):
    def __init__(self, params):
        MWB.__init__(self, params)
        QWidget.__init__(self)

        

        self.setStyleSheet('''
            background-color: #333333;
        ''')

        self.setLayout(QVBoxLayout())
        # settings widget
        settings_widget = QWidget()
        settings_widget.setLayout(QHBoxLayout())
        self.connect_lines_check_box = QCheckBox('connect lines linear')
        settings_widget.layout().addWidget(self.connect_lines_check_box)
        self.layout().addWidget(settings_widget)
        # points area
        self.label = QLabel()
        pix = QPixmap(300,200)
        self.label.setPixmap(pix)
        self.layout().addWidget(self.label)

        self.resize(300, 200)

        self.values = []

    def update(self, new_vals):
        self.values = new_vals
        if len(self.values) == 0:
            return

        painter = QPainter(self.label.pixmap())
        painter.setRenderHint(QPainter.Antialiasing)

        painter.setPen(QPen('#333333'))
        painter.setBrush(QColor('#333333'))
        painter.drawRect(self.label.rect())

        pen = QPen(QColor(255, 255, 255))
        pen.setWidth(1)
        painter.setPen(pen)
        painter.setBrush(QBrush(Qt.white))

        x_old = -1
        y_old = -1

        div = max(self.values)

        for i in range(len(self.values)):
            v = self.values[i]
            x = i * (self.label.width()/len(self.values))
            y = self.label.height()-self.label.height()*v/div

            if self.connect_lines_check_box.isChecked() and i>0:
                painter.drawLine(x_old, y_old, x, y)
            else:

                painter.drawEllipse(x-1, y-1, 2, 2)

            x_old = x
            y_old = y

        self.repaint()

    def get_data(self):
        return {'connect lines linear': self.connect_lines_check_box.isChecked()}

    def set_data(self, data):
        self.connect_lines_check_box.setChecked(data['connect lines linear'])


    def remove_event(self):
        pass
