from qtpy.QtCore import QSize, QRectF, QPointF, QSizeF
from qtpy.QtGui import QPixmap, QImage, QPainter, QIcon, QPicture
from qtpy.QtWidgets import QGraphicsPixmapItem, QGraphicsWidget, QGraphicsLayoutItem

from ...utils import change_svg_color


class NodeItem_Icon(QGraphicsWidget):
    def __init__(self, node_gui, node_item):
        super().__init__(parent=node_item)

        if node_gui.style == 'normal':
            self.size = QSize(20, 20)
        else:
            self.size = QSize(50, 50)

        self.setGraphicsItem(self)

        image = QImage(node_gui.icon)
        self.pixmap = QPixmap.fromImage(image)
        # self.pixmap = change_svg_color(node.icon, node.color)


    def boundingRect(self):
        return QRectF(QPointF(0, 0), self.size)

    def setGeometry(self, rect):
        self.prepareGeometryChange()
        QGraphicsLayoutItem.setGeometry(self, rect)
        self.setPos(rect.topLeft())

    def sizeHint(self, which, constraint=...):
        return QSizeF(self.size.width(), self.size.height())


    def paint(self, painter, option, widget=None):

        # TODO: anti aliasing for node icons

        # this doesn't work: ...
        # painter.setRenderHint(QPainter.Antialiasing, True)
        # painter.setRenderHint(QPainter.HighQualityAntialiasing, True)
        # painter.setRenderHint(QPainter.SmoothPixmapTransform, True)


        painter.drawPixmap(
            0, 0,
            self.size.width(), self.size.height(),
            self.pixmap
        )
