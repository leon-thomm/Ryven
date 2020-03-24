# from PySide2.QtWidgets import ...
from PySide2.QtCore import Qt
# from PySide2.QtGui import ...
from PySide2.QtGui import QPixmap, QPainter, QPen, QColor, QBrush

from PySide2.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QCheckBox, QLabel


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
        # settings widget
        settings_widget = QWidget()
        settings_widget.setLayout(QHBoxLayout())
        self.connect_lines_check_box = QCheckBox('connect lines linear')
        settings_widget.layout().addWidget(self.connect_lines_check_box)
        self.layout().addWidget(settings_widget)
        # points area
        self.label = QLabel()
        pix = QPixmap(200,200)
        self.label.setPixmap(pix)
        self.layout().addWidget(self.label)

        self.resize(200, 200)
        
        self.values = []

    def update(self, new_vals):
        self.values = new_vals
        
        painter = QPainter(self.label.pixmap())
        painter.setRenderHint(QPainter.Antialiasing)

        painter.setPen(QPen('#333333'))
        painter.setBrush(QColor('#333333'))
        painter.drawRect(self.label.rect())

        pen = QPen(QColor(255, 255, 255))
        pen.setWidth(2)
        painter.setPen(pen)
        painter.setBrush(QBrush(Qt.white))

        x_old = -1
        y_old = -1
                
        for i in range(len(self.values)):
            v = self.values[i]
            x = i * (self.label.width()/len(self.values))
            y = self.label.height()-self.label.height()*v
            painter.drawEllipse(x-1, y-1, 2, 2)

            if self.connect_lines_check_box.isChecked() and i>0:
                painter.drawLine(x_old, y_old, x, y)
            x_old = x
            y_old = y

        self.repaint()

    def deleted(self):
        pass

    def get_data(self):
        return {'connect lines linear': self.connect_lines_check_box.isChecked()}

    def set_data(self, data):
        self.connect_lines_check_box.setChecked(data['connect lines linear'])
        self.update(self.values)
