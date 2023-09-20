from qtpy.QtCore import QRectF, QPointF, QSizeF, Property
from qtpy.QtGui import QFont, QFontMetricsF, QColor
from qtpy.QtWidgets import QGraphicsWidget, QGraphicsLayoutItem, QGraphicsItem

from ...utils import get_longest_line


class TitleLabel(QGraphicsWidget):

    def __init__(self, node_gui, node_item):
        super(TitleLabel, self).__init__(parent=node_item)

        self.setGraphicsItem(self)

        self.node_gui = node_gui
        self.node_item = node_item

        font = QFont('Poppins', 15) if self.node_gui.style == 'normal' else \
            QFont('K2D', 20, QFont.Bold, True)  # should be quite similar to every specific font chosen by the painter
        self.fm = QFontMetricsF(font)
        self.title_str, self.width, self.height = None, None, None
        self.update_shape()

        self.color = QColor(30, 43, 48)
        self.pen_width = 1.5
        self.hovering = False  # whether the mouse is hovering over the parent NI (!)

        # # Design.flow_theme_changed.connect(self.theme_changed)
        # self.update_design()

    def update_shape(self):
        self.title_str = self.node_gui.display_title

        # approximately!
        self.width = self.fm.width(get_longest_line(self.title_str)+'___')
        self.height = self.fm.height() * 0.7 * (self.title_str.count('\n') + 1)

    def boundingRect(self):
        return QRectF(QPointF(0, 0), self.geometry().size())

    def setGeometry(self, rect):
        self.prepareGeometryChange()
        QGraphicsLayoutItem.setGeometry(self, rect)
        self.setPos(rect.topLeft())

    def sizeHint(self, which, constraint=...):
        return QSizeF(self.width, self.height)

    def paint(self, painter, option, widget=None):
        self.node_item.session_design.flow_theme.paint_NI_title_label(
            self.node_gui, self.node_item.isSelected(), self.hovering, painter, option,
            self.design_style(), self.title_str,
            self.node_item.color, self.boundingRect()
        )

    def design_style(self):
        return self.node_gui.style

    def set_NI_hover_state(self, hovering: bool):
        self.hovering = hovering
        # self.update_design()
        self.update()

    # ANIMATION STUFF
    def get_color(self):
        return self.color

    def set_color(self, val):
        self.color = val
        QGraphicsItem.update(self)

    p_color = Property(QColor, get_color, set_color)