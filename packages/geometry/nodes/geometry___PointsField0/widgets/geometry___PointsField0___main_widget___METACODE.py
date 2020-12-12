from NIWENV import *
from PySide2.QtWidgets import QGraphicsView, QGraphicsScene
from PySide2.QtGui import QPainter, QColor, QPen
from PySide2.QtCore import Qt


class %CLASS%(QGraphicsView, MWB):
    def __init__(self, params):
        MWB.__init__(self, params)
        QGraphicsView.__init__(self)

        self.setFixedWidth(300);
        self.setFixedHeight(300);

        scene = QGraphicsScene(self)
        scene.setSceneRect(0,0, self.width()-5, self.height()-5)
        self.setScene(scene)
        self.setCacheMode(QGraphicsView.CacheBackground)
        self.setRenderHint(QPainter.Antialiasing)

        self.setStyleSheet('''
border: none;
        ''')

    def mousePressEvent(self, event):
        p = [event.pos().x()/self.scene().width(), 
             event.pos().y()/self.scene().height()]
        self.parent_node_instance.add_point(p)
        self.update()

    def drawBackground(self, painter, rect):
        painter.setPen(Qt.NoPen)
        painter.fillRect(rect, QColor('#0C1C23'))
        # painter.drawRect ???

    def drawForeground(self, painter, rect):
        pen = QPen('#ffffff')
        painter.setPen(pen)
        w = self.scene().width()
        h = self.scene().height()
        for p in self.parent_node_instance.points:
            painter.drawEllipse(p[0]*w, p[1]*h, 3, 3)

    def draw(self):
        self.update()

    # def get_data(self):
    #     data = {}
    #     return data
    
    # def set_data(self, data):
    #     pass
    
    # def remove_event(self):
    #     pass
