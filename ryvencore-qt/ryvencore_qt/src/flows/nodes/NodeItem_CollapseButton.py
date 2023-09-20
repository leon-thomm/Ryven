from qtpy.QtCore import QSize, QRectF, QPointF, QSizeF, Qt
from qtpy.QtWidgets import QGraphicsWidget, QGraphicsLayoutItem
from qtpy.QtGui import QColor

from ...GlobalAttributes import Location
from ...utils import change_svg_color, get_resource


class NodeItem_CollapseButton(QGraphicsWidget):
    def __init__(self, node_gui, node_item):
        super().__init__(parent=node_item)

        self.node_gui = node_gui
        self.node_item = node_item

        self.size = QSizeF(14, 7)

        self.setGraphicsItem(self)
        self.setCursor(Qt.PointingHandCursor)


        self.collapse_pixmap = change_svg_color(
            get_resource('node_collapse_icon.svg'),
            self.node_gui.color
        )
        self.expand_pixmap = change_svg_color(
            get_resource('node_expand_icon.svg'),
            self.node_gui.color
        )


    def boundingRect(self):
        return QRectF(QPointF(0, 0), self.size)

    def setGeometry(self, rect):
        self.prepareGeometryChange()
        QGraphicsLayoutItem.setGeometry(self, rect)
        self.setPos(rect.topLeft())

    def sizeHint(self, which, constraint=...):
        return QSizeF(self.size.width(), self.size.height())

    def mousePressEvent(self, event):
        event.accept()  # make sure the event doesn't get passed on
        self.node_item.flow_view.mouse_event_taken = True

        if self.node_item.collapsed:
            self.node_item.expand()
        else:
            self.node_item.collapse()

    # def hoverEnterEvent(self, event):

    def paint(self, painter, option, widget=None):

        # doesn't work: ...
        # painter.setRenderHint(QPainter.Antialiasing, True)
        # painter.setRenderHint(QPainter.HighQualityAntialiasing, True)
        # painter.setRenderHint(QPainter.SmoothPixmapTransform, True)

        if not self.node_item.hovered:
            return

        if self.node_item.collapsed:
            pixmap = self.expand_pixmap
        else:
            pixmap = self.collapse_pixmap

        painter.drawPixmap(
            0, 0,
            self.size.width(), self.size.height(),
            pixmap
        )
